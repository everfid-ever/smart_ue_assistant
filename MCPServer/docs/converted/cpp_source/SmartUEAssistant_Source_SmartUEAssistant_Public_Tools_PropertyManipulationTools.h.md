# SmartUEAssistant\Source\SmartUEAssistant\Public\Tools\PropertyManipulationTools.h

## 函数

- `FSetActorPropertyTool`
- `GetSpec`
- `Execute`
- `SetPropertyValue`
- `FBatchSetPropertiesTool`
- `FGetAvailablePropertiesTool`
- `DiscoverProperties`
- `FSmartSetPropertyTool`
- `FindMatchingProperties`
- `GetPropertyPath`
- `FAdjustPropertyTool`
- `FCopyPropertiesTool`

## 文档注释

> * 为选中的 Actor 设置属性值  * Set property value for selected actors  *   * 这是一个通用属性设置器，使用反射系统工作。  * 支持常见属性类型：float、int、bool、FVector、FRotator、FLinearColor、FColor  *   * This is a universal property setter that works with reflection system.  * Supports common property types: float, int, bool, FVector, FRotat

> 供其他工具使用的公共辅助方法 / Public helper for other tools to use

> * 批量设置选中 Actor 的属性  * Batch set properties for selected actors  *   * 在一次调用中设置多个属性以提高效率  * Set multiple properties in one call for efficiency  *   * 参数 / Parameters:  * - Properties (object): 属性路径到值的映射 / Map of property paths to values  *   示例 / Example: {"LightColor": {"R":1.0,"G":0.0,"B":0.0}, "In

> * 获取 Actor 的可用属性  * Get available properties for an actor  *   * 发现选中 Actor 上可以修改的属性。  * 对 AI 了解可用属性很有用。  *   * Discover what properties can be modified on selected actors.  * Useful for the AI to know what properties are available.  *   * 参数 / Parameters:  * - ActorName (string, 可选): 特定 Actor 名称，或使

> * 智能属性设置器 - 支持自然语言  * Smart property setter with natural language support  *   * 基于语义理解智能设置属性  * Intelligently sets properties based on semantic understanding  *   * 示例 / Examples:  * - "color" -> 搜索 Color、LightColor 等 / searches for Color, LightColor, etc.  * - "brightness" -> 搜索 Intensity、Brightne

> * 按偏移量调整数值属性（相对变化）  * Adjust numeric property by offset (relative change)  *   * 用于"增加"、"减少"操作  * Useful for "increase by", "decrease by" operations  *   * 参数 / Parameters:  * - PropertyPath (string): 属性路径 / Property path  * - Offset (number): 要添加的量（可以为负）/ Amount to add (can be negative)  * - Multip

> * 在 Actor 之间复制属性值  * Copy property values between actors  *   * 参数 / Parameters:  * - SourceActor (string): 源 Actor 名称 / Source actor name  * - PropertyPaths (array of strings): 要复制的属性 / Properties to copy  * - ApplyToSelected (boolean): 应用到所有选中的 Actor / Apply to all selected actors
