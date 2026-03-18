# SmartUEAssistant\Source\SmartUEAssistant\Public\EnhancedToolTypes.h

## 类定义

- `IEnhancedEditorTool`

## 结构体

- `FEnhancedToolSpec`
- `FEnhancedToolResult`

## 函数

- `ToBasicSpec`
- `Success`
- `NotFound`
- `ToBasicResult`
- `GetSpec`
- `GetEnhancedSpec`
- `Execute`

## 文档注释

> * 增强工具类型定义（带扩展元数据）  * Enhanced tool type definitions with extended metadata  *   * 本文件扩展了 EditorAIToolTypes.h，增加了以下特性：  * This file extends EditorAIToolTypes.h with additional features:  * - 工具分类以便更好地组织 / Tool categories for better organization  * - 版本管理 / Version management  * - 弃用支持 / Deprecation 

> * 工具分类枚举  * Tool category enumeration  *   * 按功能区域分组工具，以便更好地发现  * Groups tools by functional area for better discovery

> Actor 操作（创建、变换、删除） / Actor manipulation (creation, transformation, deletion)

> 选择和过滤 / Selection and filtering

> 视口和相机控制 / Viewport and camera control

> 系统操作（保存、PIE 控制、控制台命令） / System operations (save, PIE control, console commands)

> 场景分析和验证 / Scene analysis and validation

> 属性操作 / Property manipulation

> 批量操作 / Batch operations

> 相机书签 / Camera bookmarks

> 光照工具 / Lighting tools

> 调试工具（仅开发使用） / Debug utilities (development only)

> 通用/泛用工具 / Universal/Generic tools

> * 工具执行的详细错误码  * Detailed error codes for tool execution  *   * 提供机器可读的错误分类  * Provides machine-readable error classification  *   * 注意：由于 uint16 限制，不向蓝图公开  * Note: Not exposed to Blueprint due to uint16 limitation

> 操作成功 / Operation succeeded

> 参数无效或格式错误 / Invalid or malformed argument

> 缺少必需参数 / Required parameter missing

> 参数类型不匹配 / Parameter type mismatch

> 参数值超出范围或无效 / Parameter value out of range or invalid

> 场景中找不到 Actor / Actor not found in scene
