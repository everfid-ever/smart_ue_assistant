# UnrealAgent\Source\UnrealAgent\Public\UAEventCache.h

## 函数

- `Get`
- `Initialize`
- `Shutdown`
- `Clear`
- `IsInitialized`
- `EventTypeToString`
- `StringToEventType`
- `PushEvent`
- `OnSelectionChanged`
- `OnAssetOpenedInEditor`
- `OnAssetClosedInEditor`
- `OnPIEStarted`
- `OnPIEEnded`
- `OnPackageSaved`
- `OnMapChanged`
- `OnPostUndoRedo`

## 文档注释

> * 事件类型枚举

> * 事件条目

> * UAEventCache — 编辑器事件缓存系统。  *  * 在插件 StartupModule 时调用 Initialize() 注册 Delegate，  * ShutdownModule 时调用 Shutdown() 反注册。  * 将关键编辑器事件缓存到环形队列，供 Agent 按需查询。

> 注册所有 Delegate，开始监听事件

> 反注册所有 Delegate

> 获取最近 N 条事件，可选类型过滤

> 获取指定时间之后的所有事件

> 清空缓冲区

> 是否已初始化

> 事件类型枚举转字符串

> 字符串转事件类型枚举，失败返回 false

> 向缓冲区添加一条事件
