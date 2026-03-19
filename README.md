# Smart UE Assistant

运行于 Unreal Engine 5 编辑器的 AI 助手系统，由两个 UE 插件和一个 Python 后端（MCP Server）组成。

---

## 架构总览

```
┌─────────────────────────────────────────────────────┐
│                  Unreal Editor                      │
│                                                     │
│  ┌────────────────────┐   ┌──────────────────────┐  │
│  │ SmartUEAssistant   │   │   UnrealAgent Plugin  │  │
│  │ (Slate 聊天 UI)    │   │   TCP Server :55557   │  │
│  │                    │   │   JSON-RPC 2.0        │  │
│  └────────┬───────────┘   └──────────┬────────────┘  │
│           │ HTTP SSE /chat            │ TCP           │
└───────────┼───────────────────────────┼───────────────┘
            │                           │
            ▼                           │
┌───────────────────────┐               │
│  Python MCP Server    │───────────────┘
│  (MCPServer/)         │  send_request()
│                       │
│  Mode A: MCP stdio  ──┼──► Claude Desktop / Cursor
│  Mode B: HTTP :8765 ──┼──► Slate UI 的 /chat
│  Mode C: both         │
└───────────────────────┘
```

---

## 插件说明

| 插件 | 功能 |
|---|---|
| **UnrealAgent** | 在 UE 编辑器内启动 TCP 服务器（默认 `:55557`），接收 JSON-RPC 指令，执行 Actor/属性/蓝图/材质等 20 类操作 |
| **SmartUEAssistant** | 编辑器内嵌 Slate 聊天窗口，通过 HTTP SSE 与 Python 后端通信，AI 回复流式显示 |

两个插件均在 `SmartUEAssistant.uproject` 中启用，UE 5.7+。

---

## Python MCP Server 快速启动

### 前置要求

- Python 3.10+
- UE 编辑器已运行并加载 `UnrealAgent` 插件（TCP :55557 已就绪）

### 安装依赖

```bash
cd server
pip install -e .
```

### 配置环境变量

复制并填写 `.env`：

```bash
cp server/.env.example server/.env   # 若无 .env.example 则直接编辑 .env
```

| 变量 | 用途 | 必须 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude API Key，HTTP 模式下与 Slate UI 聊天时使用 | HTTP 模式 |
| `UNREAL_ENGINE_PATH` | UE 引擎根目录，`build_project` / `launch_editor` 工具使用 | 可选 |
| `UNREAL_AGENT_HOST` | UnrealAgent TCP 地址，默认 `127.0.0.1` | 可选 |
| `UNREAL_AGENT_PORT` | UnrealAgent TCP 端口，默认 `55557` | 可选 |
| `MCP_HTTP_PORT` | HTTP Gateway 监听端口，默认 `8765` | 可选 |
| `SMART_UE_MODE` | 运行模式，见下方说明，默认 `stdio` | 可选 |

---

## 两种运行模式

### 模式 A：MCP stdio（与 Claude Desktop / Cursor 集成）

AI 客户端通过 stdin/stdout 与 MCP Server 通信，MCP Server 再经 TCP 控制编辑器。

```bash
# 直接运行（默认模式）
cd server
python -m unreal_agent_mcp

# 或使用入口脚本
unreal-agent-mcp
```

**Claude Desktop 配置示例** (`claude_desktop_config.json`)：

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

启动后 Claude 即可调用 `move_actor`、`set_property`、`analyze_level_stats` 等工具直接操控编辑器。

---

### 模式 B：HTTP Gateway（配合编辑器内 Slate 聊天 UI）

HTTP Server 监听 `/chat` POST 接口，接收 Slate UI 消息，转发给 Claude API，以 SSE 流式返回。

```bash
SMART_UE_MODE=http python -m unreal_agent_mcp
# 或
$env:SMART_UE_MODE="http"; python -m unreal_agent_mcp   # PowerShell
```

服务启动后监听 `http://127.0.0.1:8765`。`SmartUEAssistant` 插件会自动向该地址发送请求。

**请求格式**（供调试）：

```bash
curl -X POST http://127.0.0.1:8765/chat \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"message": "场景里有多少个 Actor？", "history": [], "scene_context": ""}'
```

---

### 模式 C：同时运行两种模式

HTTP Server 在后台线程运行，MCP stdio 在主线程运行，两者可同时服务。

```bash
SMART_UE_MODE=both python -m unreal_agent_mcp
```

---

## MCP 工具一览

| 工具模块 | 工具数 | 说明 |
|---|---|---|
| `actors` | — | Actor 增删改查、变换 |
| `properties` | 4 | `get_property` / `set_property` / `list_properties` / `modify_property` |
| `world` | — | World / Level 操作 |
| `blueprints` | — | Blueprint 节点创建、连线 |
| `materials` | — | 材质与材质实例 |
| `assets` / `asset_manage` | — | 资产查询与管理 |
| `scene_analysis` | 5 | 关卡统计、缺失引用、重复名、超大网格、Level 验证 |
| `batch_ops` | 7 | 批量重命名、可见性、Mobility、移动到 Level、Tag |
| `screenshots` | — | 视口截图 |
| `viewport` | — | 摄像机导航 |
| `python` | — | 在编辑器内执行 Python 脚本 |
| `build` | 4 | `build_project` / `launch_editor` / `build_and_launch` / `get_build_status` |
| `knowledge` | — | 本地知识库读写 |
| `rag` | — | RAG 检索增强 |
| `context` | — | 场景上下文摘要 |

> `set_property` vs `modify_property` 区别：  
> - `set_property` — 精确单 Actor + 深层属性路径（如 `LightComponent.Intensity`）  
> - `modify_property` — 模糊目标（`selected` / `lights`）+ 顶层属性名，支持批量

---

## 项目结构

```
smart_ue_assistant/
├── SmartUEAssistant.uproject      # UE 项目文件（UE 5.7）
├── Plugins/
│   ├── UnrealAgent/               # TCP 服务端插件（C++）
│   │   └── Source/UnrealAgent/
│   │       ├── Private/Commands/  # 20 个命令模块
│   │       └── Private/Server/    # TCP Server / Client Connection
│   └── SmartUEAssistant/          # Slate UI 插件（C++）
│       └── Source/SmartUEAssistant/
│           ├── AIAssistantWindow.cpp   # 聊天窗口
│           └── AIService.cpp           # HTTP 客户端
└── MCPServer/                     # Python MCP Server
    ├── pyproject.toml
    ├── .env                       # 环境变量（不入 git）
    └── src/unreal_agent_mcp/
        ├── __main__.py            # 入口，SMART_UE_MODE 分发
        ├── server.py              # FastMCP 实例 + TCP 连接单例
        ├── connection.py          # JSON-RPC TCP 客户端
        ├── app.py                 # FastAPI HTTP Gateway
        ├── knowledge_store.py     # 本地知识库（JSON 文件）
        └── tools/                 # MCP 工具，每文件一个领域
```