# UnrealAgent\Source\UnrealAgent\Public\UALogCapture.h

## 函数

- `Get`
- `Initialize`
- `Shutdown`
- `Clear`
- `IsInitialized`
- `Serialize`
- `VerbosityToString`

## 文档注释

> * 日志条目结构体

> * 日志截获系统 — 截获 UE 输出日志到环形缓冲区。  * 在插件 StartupModule 时注册，ShutdownModule 时反注册。  *   * 使用方式:  *   UALogCapture::Get().Initialize();    // 开始截获  *   UALogCapture::Get().Shutdown();      // 停止截获  *   UALogCapture::Get().GetRecent(50);   // 获取最近50条

> 注册为全局输出设备，开始截获日志

> 从全局输出设备列表中移除

> 获取最近 N 条日志，可选按类别过滤

> 获取指定时间之后的日志

> 清空缓冲区

> 是否已初始化

> 将 ELogVerbosity 转换为可读字符串
