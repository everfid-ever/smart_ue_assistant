# UnrealAgent\Source\UnrealAgent\Public\Commands\UABlueprintCommands.h

## 函数

- `DECLARE_LOG_CATEGORY_EXTERN`
- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteGetBlueprintOverview`
- `ExecuteGetBlueprintGraph`
- `ExecuteGetBlueprintVariables`
- `ExecuteGetBlueprintFunctions`
- `ExecuteAddNode`
- `ExecuteDeleteNode`
- `ExecuteConnectPins`
- `ExecuteDisconnectPin`
- `ExecuteAddVariable`
- `ExecuteAddFunction`
- `ExecuteCompileBlueprint`
- `LoadBlueprintFromPath`
- `FindGraphByName`
- `FindNodeByIndex`
- `FindPinByName`
- `NodeToJson`
- `PinToJson`
- `PinTypeToString`
- `StringToPinType`

## 文档注释

> * 蓝图编辑命令组 — 镜像 UAMaterialCommands 的设计模式。  * 提供蓝图节点图的查询、节点创建/删除、引脚连接/断开、变量/函数管理、编译等功能。  *  * 支持的方法:  *   查询:  *     - get_blueprint_overview:    蓝图概览（图列表、变量、事件等）  *     - get_blueprint_graph:       节点图详情（节点+连接）  *     - get_blueprint_variables:   变量定义列表  *     - get_blueprint_functions:   函数签名列表  *  

> 根据资产路径加载 UBlueprint

> 在蓝图中查找指定名称的图

> 根据索引在图中查找节点

> 根据名称在节点上查找引脚

> 将单个节点序列化为 JSON

> 将引脚序列化为 JSON

> 将 FEdGraphPinType 转为可读的类型字符串

> 将类型字符串解析为 FEdGraphPinType
