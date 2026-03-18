# UnrealAgent\Source\UnrealAgent\Public\Commands\UACommandBase.h

## 函数

- `MakeToolSchema`

## 文档注释

> * Abstract base class for all command groups.  * Each subclass represents a group of related tool commands.

> Return the list of method names this command group supports

> Return the JSON schema for a specific method (for MCP tools/list)

> * Execute a command. 	 * @param MethodName  The method to execute (e.g., "list_assets") 	 * @param Params      Request parameters as JSON object 	 * @param OutResult   Output result JSON object 	 * @param OutError    Output error message (if returning false) 	 * @return true on success, false on fai

> Helper: Create a simple tool schema JSON object
