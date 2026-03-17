"""Entry point for the UnrealAgent MCP Server."""

import asyncio
import os
import sys


def main():
    """Run the MCP server."""
    from .server import mcp

    # 原有 UnrealAgent 工具（50个，保持不变）
    from .tools import project, assets, world, actors, viewport, python, editor, knowledge, materials  # noqa: F401
    from .tools import context, properties  # noqa: F401
    from .tools import blueprints, asset_manage  # noqa: F401
    from .tools import screenshots, events  # noqa: F401
    from .tools import build  # noqa: F401

    # ── 新增：RAG 检索工具 ──
    from .tools import rag  # noqa: F401

    # ── 新增：C++ 移植工具（Phase 3 完成后取消注释）──
    # from .tools import batch_ops       # noqa: F401
    # from .tools import scene_analysis  # noqa: F401

    # 判断启动模式
    mode = os.environ.get("SMART_UE_MODE", "stdio")

    if mode == "http":
        # HTTP 模式：供 Slate UI 调用（Phase 4）
        _run_http()
    elif mode == "both":
        # 同时启动 stdio MCP + HTTP Server
        _run_both(mcp)
    else:
        # 默认 stdio 模式：供 CodeBuddy 使用
        mcp.run(transport="stdio")


def _run_http():
    """启动 HTTP Server（Phase 4 实现）"""
    try:
        from .http_server import run_http_server
        run_http_server()
    except ImportError:
        print("❌ http_server.py 尚未实现（Phase 4 任务）", file=sys.stderr)
        print("   当前请使用 stdio 模式：python -m unreal_agent_mcp", file=sys.stderr)
        sys.exit(1)


def _run_both(mcp):
    """同时运行 stdio MCP 和 HTTP Server"""
    import threading
    try:
        from .http_server import run_http_server
        # HTTP Server 在后台线程运行
        t = threading.Thread(target=run_http_server, daemon=True)
        t.start()
        print(f"✅ HTTP Server 已在后台启动（端口 {os.environ.get('HTTP_SERVER_PORT', 8765)}）", file=sys.stderr)
    except ImportError:
        print("⚠️  HTTP Server 未实现，仅启动 stdio 模式", file=sys.stderr)

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
