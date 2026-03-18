# SmartUEAssistant\Source\SmartUEAssistant\Public\ToolAutoRegister.h

## 文档注释

> * 自动工具注册系统  * Automatic tool registration system  *   * 用法 / Usage:  *   // 在工具实现文件（.cpp）末尾添加：  *   // At the end of your tool implementation file (.cpp):  *   REGISTER_EDITOR_TOOL(FMyCustomTool)  *   * 该宏创建一个静态初始化器，在模块加载时自动注册工具，  * 无需在 SmartUEAssistant.cpp 中手动注册。  *   * This macro creates a static 

> * 条件注册 - 仅在开发/调试版本中注册  * Conditional registration - only registers in Development/Debug builds  *   * 用法 / Usage:  *   REGISTER_EDITOR_TOOL_DEBUG(FDebugTool)  *   * Debug 工具将自动在 Shipping 版本中排除  * Debug tools will be automatically excluded from Shipping builds
