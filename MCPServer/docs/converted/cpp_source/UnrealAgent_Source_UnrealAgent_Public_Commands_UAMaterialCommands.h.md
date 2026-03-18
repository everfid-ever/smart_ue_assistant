# UnrealAgent\Source\UnrealAgent\Public\Commands\UAMaterialCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteGetMaterialGraph`
- `ExecuteCreateExpression`
- `ExecuteDeleteExpression`
- `ExecuteConnectToProperty`
- `ExecuteConnectExpressions`
- `ExecuteSetExpressionValue`
- `ExecuteRecompileMaterial`
- `ExecuteLayoutExpressions`
- `ExecuteGetMaterialParameters`
- `ExecuteSetInstanceParam`
- `ExecuteSetMaterialProperty`
- `LoadMaterialFromPath`
- `LoadMaterialInstanceFromPath`
- `ParseMaterialProperty`
- `FindExpressionByIndex`
- `ExpressionToJson`

## 文档注释

> * 材质编辑命令组  * 提供材质节点的创建、删除、连接、查询以及材质实例参数的管理功能

> 获取材质的完整节点图信息（节点列表、连接关系、材质属性）

> 创建材质表达式节点

> 删除材质表达式节点

> 连接节点到材质属性输出（BaseColor, Metallic 等）

> 连接两个节点之间的输入/输出

> 通过反射设置节点的属性值

> 重新编译材质

> 自动排列材质节点布局

> 获取材质参数列表（Scalar/Vector/Texture/StaticSwitch）

> 设置材质实例参数值

> 设置材质全局属性（BlendMode, ShadingModel, TwoSided 等）

> 根据资产路径加载 UMaterial 对象

> 根据资产路径加载 UMaterialInstanceConstant 对象

> 将 EMaterialProperty 字符串转为枚举值

> 根据索引在材质中查找表达式节点

> 构建单个表达式节点的 JSON 描述
