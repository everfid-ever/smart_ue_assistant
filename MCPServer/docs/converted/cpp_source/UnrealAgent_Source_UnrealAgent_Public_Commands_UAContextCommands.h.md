# UnrealAgent\Source\UnrealAgent\Public\Commands\UAContextCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteGetOpenEditors`
- `ExecuteGetSelectedAssets`
- `ExecuteGetBrowserPath`
- `ExecuteGetMessageLog`
- `ExecuteGetOutputLog`

## 文档注释

> * 编辑器上下文感知命令 — 让 Agent 知道 "用户正在干什么"。  *  * 支持的方法:  *   - get_open_editors:    获取当前打开的所有资产编辑器  *   - get_selected_assets: 获取 Content Browser 中选中的资产  *   - get_browser_path:    获取 Content Browser 当前浏览路径  *   - get_message_log:     获取消息日志（编译错误等）  *   - get_output_log:      获取输出日志最近 N 条
