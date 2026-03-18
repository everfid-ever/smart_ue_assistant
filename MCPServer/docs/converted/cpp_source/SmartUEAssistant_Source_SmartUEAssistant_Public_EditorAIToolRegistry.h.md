# SmartUEAssistant\Source\SmartUEAssistant\Public\EditorAIToolRegistry.h

## 函数

- `Get`
- `Register`
- `Unregister`
- `UnregisterAll`
- `HasTool`
- `GetAll`
- `Dispatch`

## 文档注释

> * 编辑器 AI 工具的注册表和调度器  * Registry and dispatcher for Editor AI Tools  *   * 管理所有可用 AI 工具的单例注册表。  * 工具可以在模块启动时注册，并通过名称调度。  *   * Singleton registry that manages all available AI tools.  * Tools can be registered at module startup and dispatched by name.  *   * 用法 / Usage:  *   FEditorAIToolRegistry::Ge

> * 获取单例实例 	 * Get the singleton instance 	 *  	 * @return 全局工具注册表的引用 / Reference to the global tool registry

> * 注册新工具 	 * Register a new tool 	 *  	 * @param Tool 工具实现的共享引用 / Shared reference to the tool implementation

> * 按名称注销工具 	 * Unregister a tool by name 	 *  	 * @param Name 要移除的工具名称 / Name of the tool to remove

> * 注销所有工具（用于模块关闭） 	 * Unregister all tools (for module shutdown)

> * 检查工具是否已注册 	 * Check if a tool is registered 	 *  	 * @param Name 要检查的工具名称 / Tool name to check 	 * @return 如果工具存在于注册表中则返回 true / True if the tool exists in the registry

> * 获取所有已注册的工具 	 * Get all registered tools 	 *  	 * @return 工具名称到工具实现的映射 / Map of tool names to tool implementations

> * 按名称调度工具执行 	 * Dispatch a tool execution by name 	 *  	 * @param Name 要执行的工具名称 / Tool name to execute 	 * @param Args 工具的 JSON 参数 / JSON arguments for the tool 	 * @return 执行结果 / Execution result

> 已注册工具的映射表 / Map of registered tools
