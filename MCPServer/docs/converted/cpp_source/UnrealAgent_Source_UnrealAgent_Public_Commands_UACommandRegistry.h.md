# UnrealAgent\Source\UnrealAgent\Public\Commands\UACommandRegistry.h

## 函数

- `UACommandRegistry`
- `RegisterCommand`
- `Dispatch`
- `GetAllToolSchemas`
- `HandleListTools`

## 文档注释

> * Central registry for all command groups.  * Maps method names to their handlers and provides dispatch functionality.

> Register a command group handler

> * Dispatch a method call to the appropriate handler. 	 * @return true on success, false on failure (OutError set)

> Get JSON schemas for all registered tools (for list_tools)

> Handle the built-in list_tools method

> Method name -> Command handler mapping

> All registered command groups
