# SmartUEAssistant\Source\SmartUEAssistant\Public\EditorAIToolTypes.h

## 文档注释

> * 编辑器操作的权限级别  * Permission level for editor operations  *   * 用于控制危险操作并要求用户确认  * Used to control dangerous operations and require user confirmation

> 安全操作（选择、查询等）/ Safe operations (selection, queries, etc.)

> 修改场景（变换、添加组件等）/ Modify scene (transform, add components, etc.)

> 潜在危险操作（保存、运行命令等）/ Potentially dangerous operations (save, run commands, etc.)

> * AI 工具的参数规范  * Parameter specification for AI tools

> 参数名称 / Parameter name

> 参数类型："string" | "number" | "boolean" | "object" / Parameter type

> 此参数是否可选 / Whether this parameter is optional

> 参数的人类可读描述 / Human-readable description of the parameter

> * 工具规范定义 - 定义工具接口和元数据  * Tool specification defining tool interface and metadata

> 唯一的工具名称 / Unique tool name

> 人类可读的工具描述 / Human-readable tool description

> 参数规范数组 / Array of parameter specifications

> 此工具的权限级别 / Permission level for this tool

> 执行前是否需要明确的用户确认 / Whether explicit user confirmation is required before execution

> * 工具执行结果  * Result of tool execution

> 执行是否成功 / Whether the execution succeeded

> 结果消息或错误描述 / Result message or error description

> 工具返回的可选结构化数据 / Optional structured data returned by the tool

> * 编辑器 AI 工具接口  * Interface for editor AI tools  *   * 实现此接口以创建可被 AI 助手调用的自定义工具。  * 工具接收 JSON 参数并返回结构化结果。  *   * Implement this interface to create custom tools that can be called by the AI assistant.  * Tools receive JSON arguments and return structured results.
