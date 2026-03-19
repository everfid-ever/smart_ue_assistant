"""
RAG 统一检索层

职责：
  - 封装底层检索实现（当前：关键词匹配，未来：向量检索）
  - 统一三类资源（文档/代码/资产）的检索接口和返回格式
  - 管理各类资源的 SimpleRAGClient 实例生命周期
  - 不知道 MCP 的存在，不知道调用者是谁

未来扩展：
  - 替换 SimpleRAGClient 为向量检索时，只改这个文件
  - 增加新的资源类型，在 SourceType 里添加即可
"""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ── 数据结构 ─────────────────────────────────────────────────────────────────

class SourceType(str, Enum):
    DOCS   = "docs"    # UE 官方文档
    CODE   = "code"    # 项目 C++ 源码
    ASSETS = "assets"  # 资产元数据（离线索引）


@dataclass
class RetrievalResult:
    """单条检索结果，格式统一，与底层实现无关"""
    name:    str
    score:   float
    snippet: str            # 最相关的一段文本，已裁剪
    source:  SourceType
    path:    str = ""       # 原始文件路径，调试用

    def is_empty(self) -> bool:
        return not self.snippet.strip()


@dataclass
class RetrievalResponse:
    """检索响应，包含结果列表和状态信息"""
    results: list[RetrievalResult] = field(default_factory=list)
    source:  SourceType = SourceType.DOCS
    query:   str = ""
    error:   Optional[str] = None       # 非 None 表示检索失败

    def ok(self) -> bool:
        return self.error is None

    def empty(self) -> bool:
        return self.ok() and len(self.results) == 0


# ── 内部工具函数 ──────────────────────────────────────────────────────────────

def _load_simple_rag(simple_rag_path: Path, docs_dir: Path):
    """
    加载 SimpleRAGClient 实例。
    用 importlib 是因为 simple_rag_query.py 不在包结构里，
    这里集中处理，避免在多处重复这段丑陋的代码。
    """
    if not simple_rag_path.exists():
        raise FileNotFoundError(f"simple_rag_query.py 不存在: {simple_rag_path}")
    if not docs_dir.exists():
        raise FileNotFoundError(f"文档目录不存在: {docs_dir}")

    spec = importlib.util.spec_from_file_location("simple_rag_query", simple_rag_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SimpleRAGClient(docs_dir=str(docs_dir))


def _build_result(raw: dict, source: SourceType) -> RetrievalResult:
    """将 SimpleRAGClient 返回的原始 dict 转换为 RetrievalResult"""
    snippets = raw.get("snippets", [])
    snippet  = snippets[0].strip().replace("\n", " ")[:400] if snippets else ""
    return RetrievalResult(
        name    = raw.get("name", ""),
        score   = float(raw.get("score", 0)),
        snippet = snippet,
        source  = source,
        path    = raw.get("path", ""),
    )


# ── 核心检索器 ────────────────────────────────────────────────────────────────

class Retriever:
    """
    统一检索接口。

    使用方式：
        retriever = Retriever.from_settings(settings_path)
        response  = retriever.search("Actor BeginPlay", SourceType.DOCS)

    替换检索后端：
        只需修改 _get_client() 的实现，其余代码不变。
    """

    def __init__(
            self,
            simple_rag_path: Path,
            docs_dir:        Path,
            code_dir:        Path,
            assets_dir:      Path,
    ):
        self._simple_rag_path = simple_rag_path
        self._dirs = {
            SourceType.DOCS:   docs_dir,
            SourceType.CODE:   code_dir,
            SourceType.ASSETS: assets_dir,
        }
        # 懒加载：第一次使用时才初始化，避免启动时因目录不存在而崩溃
        self._clients: dict[SourceType, object] = {}
        self._init_errors: dict[SourceType, str] = {}

    # ── 工厂方法 ──────────────────────────────────────────────────────────────

    @classmethod
    def from_settings(cls, settings_path: Path) -> "Retriever":
        """从 settings.yaml 构造 Retriever，路径计算逻辑集中在这里"""
        import yaml
        cfg = yaml.safe_load(settings_path.read_text(encoding="utf-8"))
        pi  = cfg.get("private_index", {})

        rag_root       = settings_path.parent.parent          # MCPServer/rag/
        mcp_root       = rag_root.parent                      # MCPServer/
        simple_rag_path = rag_root / "tools" / "simple_rag_query.py"

        docs_dir   = rag_root / pi.get("docs_output_dir",   "../docs/converted/markdown")
        code_dir   = mcp_root / pi.get("cpp_output_dir",    "docs/converted/cpp_source")
        assets_dir = mcp_root / pi.get("assets_output_dir", "docs/converted/assets")

        # 规范化路径（处理 .. ）
        docs_dir   = docs_dir.resolve()
        code_dir   = code_dir.resolve()
        assets_dir = assets_dir.resolve()

        return cls(simple_rag_path, docs_dir, code_dir, assets_dir)

    # ── 公开接口 ──────────────────────────────────────────────────────────────

    def search(
            self,
            query:       str,
            source:      SourceType,
            max_results: int = 5,
    ) -> RetrievalResponse:
        """
        检索指定类型的资源。

        Args:
            query:       查询词，支持中英文
            source:      检索来源，见 SourceType
            max_results: 最多返回条数，上限 10

        Returns:
            RetrievalResponse，通过 .ok() / .empty() 判断状态
        """
        max_results = min(max_results, 10)

        client, error = self._get_client(source)
        if error:
            return RetrievalResponse(source=source, query=query, error=error)

        try:
            raws    = client.search(query, max_results=max_results)
            results = [_build_result(r, source) for r in raws]
            return RetrievalResponse(results=results, source=source, query=query)
        except Exception as e:
            return RetrievalResponse(
                source=source, query=query,
                error=f"检索执行失败: {e}",
            )

    def status(self) -> dict:
        """
        返回各资源类型的就绪状态，供 query_docs_status MCP 工具调用。

        Returns:
            {source_name: {"ready": bool, "doc_count": int, "error": str}}
        """
        result = {}
        for source in SourceType:
            client, error = self._get_client(source)
            if error:
                result[source.value] = {"ready": False, "doc_count": 0, "error": error}
            else:
                doc_count = len(getattr(client, "index", {}))
                result[source.value] = {"ready": True, "doc_count": doc_count, "error": None}
        return result

    # ── 内部方法 ──────────────────────────────────────────────────────────────

    def _get_client(self, source: SourceType):
        """
        懒加载并缓存 SimpleRAGClient 实例。
        返回 (client, error_str)，两者必有一个为 None。

        未来替换向量检索时，只改这个方法。
        """
        # 已缓存
        if source in self._clients:
            return self._clients[source], None
        if source in self._init_errors:
            return None, self._init_errors[source]

        # 首次初始化
        try:
            client = _load_simple_rag(self._simple_rag_path, self._dirs[source])
            self._clients[source] = client
            return client, None
        except FileNotFoundError as e:
            err = str(e)
            self._init_errors[source] = err
            return None, err
        except Exception as e:
            err = f"初始化 {source.value} 检索器失败: {e}"
            self._init_errors[source] = err
            return None, err