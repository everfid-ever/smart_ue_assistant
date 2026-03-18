# UnrealAgent\Source\UnrealAgent\Public\Commands\UAPythonCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecutePython`
- `ExecuteResetContext`
- `IsPythonAvailable`
- `WrapCodeWithSafeguards`

## 文档注释

> * Python execution command for the universal execution layer.  * Allows AI agents to execute arbitrary Python code in the UE Editor context.  *  * Supported methods:  *   - execute_python: Execute Python code and return output  *   - reset_python_context: Reset the shared Python execution context

> Check if the Python scripting plugin is available

> Wrap user code with timeout watchdog and undo transaction

> Maximum output length in characters (default 64KB)

> Default timeout for Python execution in seconds
