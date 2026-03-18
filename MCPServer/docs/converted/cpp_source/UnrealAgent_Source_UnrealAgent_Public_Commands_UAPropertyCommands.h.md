# UnrealAgent\Source\UnrealAgent\Public\Commands\UAPropertyCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteGetProperty`
- `ExecuteSetProperty`
- `ExecuteListProperties`
- `FindActorByName`
- `FindComponentByName`
- `ResolvePropertyPath`
- `PropertyToJsonValue`
- `JsonValueToProperty`

## 文档注释

> * 通用属性读写命令 — 基于 UE 反射系统，实现任意 UObject 属性的读写。  *  * 支持的方法:  *   - get_property:    通过属性路径读取 Actor/Component 的任意属性值  *   - set_property:    通过属性路径设置 Actor/Component 的任意属性值  *   - list_properties: 列出 Actor 或组件的所有可编辑属性

> 根据名称查找场景中的 Actor

> 根据名称查找 Actor 上的组件

> * 解析属性路径，获取目标对象和属性。 	 * 路径格式: "ComponentName.PropertyName" 或 "ComponentName.StructProp.Field" 	 * 如果只有一段，则直接在 Actor 上查找属性。

> 将 FProperty 值序列化为 JSON Value

> 从 JSON Value 反序列化到 FProperty
