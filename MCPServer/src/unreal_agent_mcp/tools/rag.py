"""
RAG 检索工具 - 接入 unreal_rag 的文档检索能力
暴露为 MCP 工具供 CodeBuddy / Slate UI 调用
"""

import importlib.util
from pathlib import Path

from ..server import mcp, connection

# ── 路径定位 ──────────────────────────────────────────────
# 本文件: MCPServer/src/unreal_agent_mcp/tools/rag.py
# RAG根目录: MCPServer/rag/
_MCP_DIR  = Path(__file__).parent.parent.parent.parent  # MCPServer/
_RAG_ROOT = _MCP_DIR / "rag"
_DOCS_DIR = _RAG_ROOT / "docs" / "converted" / "markdown"
_SIMPLE_RAG = _RAG_ROOT / "tools" / "simple_rag_query.py"


# ── 加载 SimpleRAGClient（启动时执行一次）────────────────
def _load_rag_client():
    if not _SIMPLE_RAG.exists():
        return None, f"❌ 文件不存在: {_SIMPLE_RAG}"
    if not _DOCS_DIR.exists():
        return None, f"❌ 文档目录不存在: {_DOCS_DIR}"
    try:
        spec = importlib.util.spec_from_file_location("simple_rag_query", _SIMPLE_RAG)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        client = mod.SimpleRAGClient(docs_dir=str(_DOCS_DIR))
        return client, None
    except Exception as e:
        return None, f"❌ 加载 SimpleRAGClient 失败: {e}"


_rag_client, _rag_error = _load_rag_client()


# ── MCP 工具 ─────────────────────────────────────────────

@mcp.tool()
async def query_docs_status() -> str:
    """查看 RAG 文档知识库当前状态，确认文档是否已正确加载。"""
    if _rag_client is None:
        return f"❌ RAG 未初始化\n原因：{_rag_error}"
    doc_count = len(_rag_client.index)
    status = "✅ 就绪" if doc_count > 0 else "⚠️  文档数为 0，请检查目录"
    return (
        f"RAG 知识库状态\n"
        f"  已索引文档：{doc_count} 个\n"
        f"  文档目录：{_DOCS_DIR}\n"
        f"  状态：{status}"
    )


@mcp.tool()
async def query_docs(query: str, max_results: int = 5) -> str:
    """
    查询 UE 官方文档知识库（221个文档）。
    适用于：UE API、Blueprint、C++ 编程规范、编辑器操作等问题。
    关键词全文检索，无需 API Key，响应极快。

    Args:
        query: 查询内容，支持中英文。例如：
               "Actor BeginPlay 调用时机"
               "Material Parameter Collection 用法"
        max_results: 返回结果数量，默认 5，最多 10
    """
    if _rag_client is None:
        return _rag_error or "❌ RAG 客户端未初始化"

    try:
        results = _rag_client.search(query, max_results=min(max_results, 10))

        if not results:
            return (
                f"未找到与「{query}」相关的文档。\n"
                f"建议：尝试换用英文关键词，或拆分为更短的词组。"
            )

        lines = [f"找到 {len(results)} 条相关文档（查询：{query}）\n"]
        for i, r in enumerate(results, 1):
            lines.append(f"[{i}] {r['name']}  (相关度: {r['score']})")
            snippets = r.get("snippets", [])
            if snippets:
                snippet = snippets[0].strip().replace("\n", " ")[:400]
                lines.append(f"    {snippet}...")
            lines.append("")

        return "\n".join(lines)

    except Exception as e:
        return f"❌ 查询出错：{e}"


@mcp.tool()
async def query_code(query: str, max_results: int = 5) -> str:
    """
    查询项目本地 C++ 源码索引（Phase 5 功能，当前尚未启用）。
    当前建议使用 execute_python 在编辑器内直接查询。

    Args:
        query: 查询内容，例如 "UABlueprintCommands 如何注册工具"
        max_results: 返回结果数量
    """
    return (
        f"🚧 本地代码索引功能尚未启用（Phase 5）\n\n"
        f"查询：{query}\n\n"
        f"当前替代方案：使用 execute_python 工具在 UE 编辑器内直接执行 Python 查询\n"
        f"例如：import unreal; print(dir(unreal.Actor))"
    )


@mcp.tool()
async def query_assets(query: str, asset_type: str = None) -> str:
    """
    在 UE 项目中检索资产（材质、蓝图、静态网格等）。
    需要 UE 编辑器正在运行且 UnrealAgent Plugin 已加载。

    Args:
        query: 资产名称或关键词，例如 "M_Rock" "BP_Player"
        asset_type: 可选，限定资产类型：Blueprint / StaticMesh / Material / Texture2D
    """
    try:
        params = {"query": query}
        if asset_type:
            params["class_filter"] = asset_type
        result = await connection.send_request("search_assets", params)
        if not result:
            return f"未找到与「{query}」相关的资产"
        import json
        return f"资产检索结果（查询：{query}）\n\n{json.dumps(result, indent=2, ensure_ascii=False)}"
    except Exception as e:
        return (
            f"❌ 资产检索失败：{e}\n"
            f"请确认 UE Editor 正在运行，且 Output Log 显示 TCP server listening on :55557"
        )