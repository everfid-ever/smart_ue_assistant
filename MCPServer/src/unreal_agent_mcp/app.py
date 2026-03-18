"""FastAPI app — /chat endpoint, SSE streaming response."""

import json
import logging
import os
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title="SmartUEAssistant HTTP Gateway")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["POST", "GET"],
        allow_headers=["*"],
    )

    @app.post("/chat")
    async def chat(request: Request):
        """接收 Slate 的消息，转发给 Claude API，返回 SSE 流。"""
        try:
            body = await request.json()
        except Exception:
            return JSONResponse({"error": "Invalid JSON"}, status_code=400)

        user_message = body.get("message", "")
        history = body.get("history", [])
        scene_context = body.get("scene_context", "")

        if not user_message:
            return JSONResponse({"error": "Missing message"}, status_code=400)

        accept = request.headers.get("Accept", "")
        if "text/event-stream" in accept:
            return StreamingResponse(
                _stream_response(user_message, history, scene_context),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "X-Accel-Buffering": "no",
                },
            )
        else:
            # 非 SSE 客户端：收集完整响应后返回 JSON
            chunks = []
            async for chunk in _stream_response(user_message, history, scene_context):
                if chunk.startswith("data:"):
                    data = chunk[5:].strip()
                    if data and data != "[DONE]":
                        try:
                            obj = json.loads(data)
                            chunks.append(obj.get("content", data))
                        except Exception:
                            chunks.append(data)
            return JSONResponse({"response": "".join(chunks)})

    return app


async def _stream_response(
    message: str,
    history: list,
    scene_context: str,
) -> AsyncGenerator[str, None]:
    """调用 Anthropic API 并以 SSE 格式流式返回。"""
    import anthropic

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        yield f"data: {json.dumps({'content': '[ERR:AUTH] ANTHROPIC_API_KEY 未配置'})}\n\n"
        yield "data: [DONE]\n\n"
        return

    client = anthropic.Anthropic(api_key=api_key)

    # 构建消息列表
    messages = []
    for h in history:
        role = h.get("role", "user")
        content = h.get("content", "")
        if role in ("user", "assistant") and content:
            messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": message})

    system_prompt = (
        "你是 SmartUEAssistant，运行于 Unreal Editor 的 AI 助手。"
        "你可以帮助用户操作编辑器、分析场景、修改属性。"
        "请用中文回答，保持简洁专业。"
    )
    if scene_context:
        system_prompt += f"\n\n当前场景摘要：\n{scene_context}"

    try:
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            system=system_prompt,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                payload = json.dumps({"content": text}, ensure_ascii=False)
                yield f"data: {payload}\n\n"
        yield "data: [DONE]\n\n"
    except Exception as e:
        logger.error(f"Anthropic API error: {e}")
        error_payload = json.dumps({"content": f"[ERR:SERVER] API 调用失败：{str(e)}"})
        yield f"data: {error_payload}\n\n"
        yield "data: [DONE]\n\n"