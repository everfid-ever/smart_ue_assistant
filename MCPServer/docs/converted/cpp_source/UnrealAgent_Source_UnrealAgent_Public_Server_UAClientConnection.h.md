# UnrealAgent\Source\UnrealAgent\Public\Server\UAClientConnection.h

## 函数

- `UAClientConnection`
- `IsConnected`
- `ProcessPendingData`
- `Close`
- `GetEndpointStr`
- `TryExtractMessage`
- `HandleMessage`
- `SendResponse`

## 文档注释

> * Manages a single TCP client connection.  * Handles message framing (Content-Length protocol) and dispatches  * complete JSON-RPC messages to the handler.

> Check if the connection is still alive

> Read and process pending data. Returns false if connection is broken.

> Close the connection

> Get endpoint string for logging

> Try to extract a complete message from the receive buffer

> Handle a complete JSON-RPC message

> Send a response string back to the client

> The underlying socket

> Remote endpoint string (for logging)

> Receive buffer for accumulating partial data

> JSON-RPC request handler
