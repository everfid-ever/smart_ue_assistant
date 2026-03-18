# SmartUEAssistant\Source\SmartUEAssistant\Public\PropertyModificationHelper.h

## 类定义

- `FPropertyModificationHelper`

## 函数

- `SetPropertyValue`
- `FindPropertyByPath`
- `SetPropertyValueDirect`
- `ParseColor`
- `ParseVector`
- `ParseRotator`
- `GetPropertyValueAsJson`
- `IsPropertyEditable`
- `GetPropertyTypeName`

## 文档注释

> * 通用属性修改助手  * Universal property modification helper  *   * 使用正确的 UE 通知和事务处理所有属性修改  * Handles all property modifications with proper UE notifications and transactions

> * 在任何 UObject 上修改属性值，完整支持 UE 通知 	 * Modify a property value on any UObject with full UE notification support 	 *  	 * 这是在 UE 中修改属性的正确方式： 	 * This is the CORRECT way to modify properties in UE: 	 * 1. 创建作用域事务（用于撤销/重做）/ Create scoped transaction (for undo/redo) 	 * 2. 调用对象的 Modify()（标记为脏）/ Call Modify

> * 按路径查找属性（支持嵌套路径和组件导航） 	 * Find property by path (supports nested paths and component navigation) 	 *  	 * @param Object 起始对象 / Starting object 	 * @param PropertyPath 属性路径 / Property path 	 * @param OutContainer 输出：包含属性的对象 / Output: the object that contains the property 	 * @return 找到的属性，未找到则返回 nul

> * 使用反射设置属性值（低级别，无通知） 	 * Set property value using reflection (low-level, no notifications) 	 *  	 * 请使用 SetPropertyValue() 以获得正确的 UE 集成 	 * Use SetPropertyValue() instead for proper UE integration

> * 从 JSON 解析颜色（支持 RGB 对象和颜色名称） 	 * Parse color from JSON (supports RGB objects and color names)

> * 从 JSON 解析向量 	 * Parse vector from JSON

> * 从 JSON 解析旋转器 	 * Parse rotator from JSON

> * 将属性值转换为 JSON 	 * Get property value as JSON

> * 检查属性是否可编辑 	 * Check if property is editable

> * 获取用于显示的属性类型名称 	 * Get property type name for display
