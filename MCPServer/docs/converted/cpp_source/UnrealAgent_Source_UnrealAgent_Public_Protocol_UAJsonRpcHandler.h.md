# UnrealAgent\Source\UnrealAgent\Public\Protocol\UAJsonRpcHandler.h

## 函数

- `UAJsonRpcHandler`
- `HandleRequest`
- `MakeSuccessResponse`
- `MakeErrorResponse`
- `JsonToString`

## 文档注释

> * Handles JSON-RPC 2.0 request parsing, dispatch, and response construction.

> * Process a JSON-RPC request string and return a response string. 	 * @param JsonString  The raw JSON-RPC request 	 * @return JSON-RPC response string

> Build a JSON-RPC success response

> Build a JSON-RPC error response

> Serialize a JSON object to string

> Command registry for dispatching method calls
