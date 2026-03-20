# Smart UE Assistant

运行于 Unreal Engine 5 编辑器的本地化 AI 助手系统。针对国内开发团队的实际痛点而设计：支持本地引擎修改代码的索引与检索、使用 Claude 替代 GPT 解决网络访问问题、并提供与编辑器的双向交互能力。

---

## 项目背景

UE 5.7 内置的 AI Assistant 存在以下限制：

- 仅支持官方引擎源码，不支持团队对引擎的本地修改
- 使用 GPT，国内无法直接访问
- 只能回答文档问题，无法直接操控编辑器

本项目在编辑器内嵌入 Slate 聊天窗口，接入 API，并通过 MCP 协议实现对编辑器的程序化控制，支持本地代码、文档、资产的 RAG 检索。

---

## 架构总览

```
┌─────────────────────────────────────────────────────┐
│                  Unreal Editor                      │
│                                                     │
│  ┌────────────────────┐   ┌──────────────────────┐  │
│  │ SmartUEAssistant   │   │   UnrealAgent Plugin  │  │
│  │  Slate 聊天 UI     │   │   TCP Server :55557   │  │
│  │  场景上下文采集     │   │   JSON-RPC 2.0        │  │
│  │  HTTP SSE 客户端   │   │   20 类编辑器操作     │  │
│  └────────┬───────────┘   └──────────┬────────────┘  │
│           │ HTTP SSE /chat            │ TCP           │
└───────────┼───────────────────────────┼───────────────┘
            │                           │
            ▼                           │
┌───────────────────────────────────────────────────┐
│              Python 服务层（server/）              │
│                                                   │
│  ┌─────────────────┐   ┌───────────────────────┐  │
│  │  MCP stdio      │   │  HTTP Gateway :8765   │  │
│  │  供 Claude      │   │  供 Slate UI /chat    │  │
│  │  Desktop/Cursor │   │                       │  │
│  └─────────────────┘   └───────────────────────┘  │
│                                                   │
│  ┌─────────────────────────────────────────────┐  │
│  │              RAG 检索系统                    │  │
│  │  本地 C++ 源码 / UE 文档 / 项目资产          │  │
│  └─────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────┘
            │
            ▼
┌───────────────────────┐
│   knowledge/（数据层）  │
│   cpp_source/          │
│   ue_docs/             │
│   project_assets/      │
└───────────────────────┘
```

**三层职责：**

| 层 | 目录 | 职责 |
|---|---|---|
| 编辑器层 | `Plugins/` | UI 呈现、场景感知、编辑器操控执行 |
| 服务层 | `server/` | AI 协议桥接、RAG 检索、HTTP 网关 |
| 数据层 | `knowledge/` | 本地索引数据存储 |

---

## 插件说明

### UnrealAgent（执行层）

在编辑器内启动 TCP 服务器（默认 `:55557`），接收 JSON-RPC 2.0 指令，执行编辑器操作后返回结果。

**职责边界：只管执行，不含任何 AI 或 UI 逻辑。**

支持的操作类别（20 类）：

| 类别 | 说明 |
|---|---|
| Actor | 增删改查、变换（位置/旋转/缩放） |
| 属性 | 单 Actor 深层属性精确读写、批量模糊修改 |
| Blueprint | 节点查询、创建节点、连线 |
| 材质 | 材质与材质实例读写 |
| 资产查询 | list、search、get_info、引用关系 |
| 资产管理 | create、duplicate、rename、delete、save |
| 批量操作 | 批量重命名、可见性、Mobility、Tag |
| 关卡分析 | 统计、缺失引用、重复名、超大网格检测 |
| World/Level | 加载、保存、切换 |
| 编辑器控制 | PIE 控制、撤销重做 |
| Python 执行 | 在编辑器内运行 Python 脚本 |
| 截图 | 视口截图 |
| 摄像机 | 视口导航 |
| 项目信息 | 引擎版本、模块、插件列表 |
| 事件 | 订阅并推送编辑器事件 |
| 日志 | 捕获 UE 输出日志 |
| 场景上下文 | 当前关卡信息、选中 Actor 列表 |

### SmartUEAssistant（UI 层）

编辑器内嵌 Slate 聊天窗口，**职责边界：只管呈现和场景感知，不直接操控编辑器。**

- 聊天窗口 UI（流式文字渲染、消息历史）
- 发消息前自动采集当前场景上下文并附加到请求
- 通过 HTTP SSE 与 Python 服务层通信
- 控制台命令白名单（限制 AI 可触发的命令范围）

两个插件均在 `SmartUEAssistant.uproject` 中启用，要求 UE 5.7+。**C++ 层完全隔离，不互相依赖，通过 Python 服务层间接协作。**

---

## Python 服务层快速启动

### 前置要求

- Python 3.10+
- UE 编辑器已运行并加载 `UnrealAgent` 插件（TCP :55557 已就绪）

### 安装依赖

```bash
cd server
pip install -e .
```

### 配置环境变量

```bash
cp server/.env.example server/.env
```

| 变量 | 用途 | 是否必须 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude API Key，HTTP 模式（Slate UI）使用 | HTTP 模式必须 |
| `UNREAL_ENGINE_PATH` | UE 引擎根目录，build/launch 工具使用 | 可选 |
| `UNREAL_AGENT_HOST` | UnrealAgent TCP 地址，默认 `127.0.0.1` | 可选 |
| `UNREAL_AGENT_PORT` | UnrealAgent TCP 端口，默认 `55557` | 可选 |
| `MCP_HTTP_PORT` | HTTP Gateway 端口，默认 `8765` | 可选 |
| `SMART_UE_MODE` | 运行模式：`stdio` / `http` / `both`，默认 `stdio` | 可选 |

---

## 运行模式

### 模式 A：MCP stdio（与 Claude Desktop / Cursor 集成）

AI 客户端通过 stdin/stdout 与服务层通信，服务层经 TCP 控制编辑器。

```bash
cd server
python -m unreal_agent_mcp
```

**Claude Desktop 配置**（`claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "unreal-agent": {
      "command": "python",
      "args": ["-m", "unreal_agent_mcp"],
      "cwd": "D:/ue-ai/smart_ue_assistant/server",
      "env": {
        "SMART_UE_MODE": "stdio"
      }
    }
  }
}
```

### 模式 B：HTTP Gateway（配合编辑器内 Slate 聊天 UI）

```bash
# Linux/macOS
SMART_UE_MODE=http python -m unreal_agent_mcp

# PowerShell
$env:SMART_UE_MODE="http"; python -m unreal_agent_mcp
```

服务启动后监听 `http://127.0.0.1:8765`，`SmartUEAssistant` 插件自动向该地址发送请求。

调试用 curl：

```bash
curl -X POST http://127.0.0.1:8765/chat \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"message": "场景里有多少个 Actor？", "history": [], "scene_context": ""}'
```

### 模式 C：同时运行两种模式

```bash
SMART_UE_MODE=both python -m unreal_agent_mcp
```

HTTP Server 在后台线程运行，MCP stdio 在主线程运行。

---

## MCP 工具一览

| 工具模块 | 说明 |
|---|---|
| `actors` | Actor 增删改查、变换 |
| `asset_query` | 资产查询（只读：list、search、get_info、references） |
| `asset_write` | 资产写操作（create、duplicate、rename、delete、save） |
| `properties` | `get_property` / `set_property` / `list_properties` / `modify_property` |
| `world` | World / Level 操作 |
| `blueprints` | Blueprint 节点查询与创建连线 |
| `materials` | 材质与材质实例 |
| `scene_analysis` | 关卡统计、缺失引用、重复名、超大网格、Level 验证（5个工具） |
| `batch_ops` | 批量重命名、可见性、Mobility、移动到 Level、Tag（7个工具） |
| `screenshots` | 视口截图 |
| `viewport` | 摄像机导航 |
| `python` | 在编辑器内执行 Python 脚本 |
| `build` | `build_project` / `launch_editor` / `build_and_launch` / `get_build_status` |
| `knowledge` | 本地知识库读写 |
| `rag` | RAG 检索（本地代码、文档、资产） |
| `context` | 场景上下文摘要 |

> **`set_property` vs `modify_property`：**
> - `set_property` — 精确单 Actor + 深层属性路径（如 `LightComponent.Intensity`）
> - `modify_property` — 模糊目标（`selected` / `lights`）+ 顶层属性名，支持批量

---

## RAG 知识库

知识库数据存储在 `knowledge/`，由 `server/rag/indexers/` 生成，**不入 git**（在 `.gitignore` 中排除）。

### 数据来源

| 目录 | 内容 | 来源 |
|---|---|---|
| `knowledge/cpp_source/converted/` | 项目 C++ 源码摘要（77 个文件） | `cpp_indexer.py` 自动生成 |
| `knowledge/ue_docs/raw/` | UE 引擎原始文档（markdown + udn） | 脚本从引擎目录收集 |
| `knowledge/ue_docs/converted/` | udn 转换后的 markdown（172 个文件） | `udn_to_markdown.py` 转换 |
| `knowledge/index_cache/` | 向量索引缓存 | `build_index.py` 生成 |

### 重建索引

```bash
# 收集 UE 文档（需配置 settings.yaml 中的引擎路径）
cd server/rag/scripts
bash run_collection.sh

# 转换 udn 格式
python converters/udn_to_markdown.py

# 构建 C++ 源码索引
cd server/rag/indexers
python cpp_indexer.py

# 构建向量索引
cd server/rag/pageindex/scripts
python build_index.py

# 验证检索效果
cd server/rag/scripts
python simple_rag_query.py "如何获取 Actor 的位置"
```

---

## 项目结构

```
smart_ue_assistant/
├── SmartUEAssistant.uproject       # UE 项目文件（UE 5.7）
├── SmartUEAssistant.sln            # Visual Studio 解决方案
│
├── Plugins/
│   ├── UnrealAgent/                # 编辑器执行层插件（C++）
│   │   └── Source/UnrealAgent/
│   │       ├── Private/
│   │       │   ├── Commands/       # 20 个命令模块
│   │       │   ├── Server/         # TCP Server / Client Connection
│   │       │   ├── Protocol/       # JSON-RPC 解析与路由
│   │       │   └── Settings/       # 插件配置
│   │       └── Public/             # 头文件
│   │
│   └── SmartUEAssistant/           # 编辑器 UI 层插件（C++）
│       └── Source/SmartUEAssistant/
│           ├── Private/
│           │   ├── AIAssistantWindow.cpp   # Slate 聊天窗口
│           │   ├── AIService.cpp           # HTTP SSE 客户端
│           │   ├── SceneContextProvider.cpp # 场景上下文采集
│           │   └── ConsoleCommandWhitelist.cpp
│           └── Public/
│
├── server/                         # Python 服务层
│   ├── pyproject.toml
│   ├── .env                        # 环境变量（不入 git）
│   ├── src/unreal_agent_mcp/
│   │   ├── __main__.py             # 入口，SMART_UE_MODE 分发
│   │   ├── server.py               # FastMCP 实例 + TCP 连接单例
│   │   ├── connection.py           # JSON-RPC TCP 客户端
│   │   ├── app.py                  # FastAPI HTTP Gateway
│   │   ├── http_server.py          # HTTP 服务器启动器
│   │   ├── knowledge_store.py      # 本地知识库（JSON 文件）
│   │   ├── ast_fingerprint.py      # 代码变更检测
│   │   ├── telemetry.py            # 工具调用统计
│   │   └── tools/                  # MCP 工具接口（每文件一个领域）
│   │       ├── asset_query.py      # 资产查询（只读）
│   │       ├── asset_write.py      # 资产写操作
│   │       └── ...
│   └── rag/                        # RAG 检索系统
│       ├── service.py              # 检索服务统一入口
│       ├── retriever/              # 向量检索器
│       ├── indexers/               # 索引构建器（cpp/doc/asset）
│       ├── agents/                 # 检索 Agent（qa/ue_dev）
│       ├── config/settings.yaml    # RAG 配置
│       └── scripts/                # 数据收集与转换脚本
│           ├── collectors/         # 文档收集脚本
│           └── converters/         # 格式转换脚本
│
├── knowledge/                      # 知识库数据层（不入 git，本地生成）
│   ├── cpp_source/converted/       # C++ 源码索引
│   ├── ue_docs/
│   │   ├── raw/                    # 原始文档（入 git）
│   │   └── converted/              # 转换后文档（不入 git）
│   └── index_cache/                # 向量索引缓存（不入 git）
│
├── docs/                           # 系统设计文档
│   ├── api-reference.md
│   ├── design-build-and-launch.md
│   ├── design-universal-execution.md
│   ├── knowledge-base-design.md
│   ├── expansion-plan.md
│   ├── test-plan.md
│   └── development-log.md
│
└── Config/                         # UE 项目配置
    ├── DefaultEngine.ini
    └── DefaultInput.ini
```

---

## 开发说明

### 新增 MCP 工具

1. 在 `server/src/unreal_agent_mcp/tools/` 创建新文件
2. 用 `@mcp.tool()` 装饰器注册工具函数
3. 在 `server/src/unreal_agent_mcp/__main__.py` 的 import 列表里加入新模块
4. 如需对应 C++ 命令，在 `Plugins/UnrealAgent/Source/UnrealAgent/Private/Commands/` 新增命令并在 `UACommandRegistry` 注册

### 更新 C++ 源码索引

修改插件源码后重新运行：

```bash
cd server/rag/indexers
python cpp_indexer.py
```

### 本地调试 RAG

```bash
cd server/rag/scripts
python simple_rag_query.py "你的查询"
```