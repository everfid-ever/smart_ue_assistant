# SmartUEAssistant\Source\SmartUEAssistant\Public\SmartUEAssistant.h

## 函数

- `StartupModule`
- `ShutdownModule`
- `RegisterMenus`
- `OpenAIAssistantWindow`
- `OnSpawnPluginTab`

## 文档注释

> * xAssistant 主模块  * xAssistant main module  *   * 管理插件生命周期、UI 注册和编辑器集成。  * 为虚幻引擎开发提供 AI 驱动的辅助。  *   * Manages plugin lifecycle, UI registration, and editor integration.  * Provides AI-powered assistance for Unreal Engine development.

> 模块加载时调用 / Called when module is loaded

> 模块卸载时调用 / Called when module is unloaded

> 注册编辑器菜单和命令 / Register editor menus and commands

> 以可停靠标签页的形式打开 AI 助手窗口 / Open AI assistant window as dockable tab

> * 生成插件标签页内容 	 * Spawn the plugin tab content 	 *  	 * @param Args 标签页管理器的生成参数 / Spawn arguments from tab manager 	 * @return 新的停靠标签页实例 / New dock tab instance

> 插件操作的 UI 命令列表 / UI command list for plugin actions

> 可停靠标签页的唯一名称 / Unique name for the dockable tab
