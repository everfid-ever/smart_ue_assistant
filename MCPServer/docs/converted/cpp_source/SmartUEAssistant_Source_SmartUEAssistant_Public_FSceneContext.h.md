# SmartUEAssistant\Source\SmartUEAssistant\Public\FSceneContext.h

## 结构体

- `FSceneActorBrief`
- `FSceneLevelBrief`
- `FSceneStats`
- `FSceneContext`

## 文档注释

> * 编辑器操作的场景上下文数据模型  * Scene context data model for editor operations  *   * 此数据模型提供关卡信息、选中对象、视口相机和其他上下文数据的统一描述。  * 可以序列化并注入到 AI 提示词中。  *   * This data model provides a unified description of level information, selected objects,  * viewport camera, and other contextual data. It can be serialized and i

> * 场景中 Actor 的简要摘要  * Brief summary of an actor in the scene

> 场景中的 Actor 名称 / Actor name in the scene

> Actor 类名 / Actor class name

> 世界位置 / World location

> 世界旋转 / World rotation

> 世界缩放 / World scale

> 组件数量（可选，由设置控制）/ Number of components (optional, controlled by settings)

> * 关卡及其 Actor 的简要摘要  * Brief summary of a level and its actors

> 关卡名称 / Level name

> 此关卡中的 Actor / Actors in this level

> * 场景统计信息  * Scene statistics

> 已加载的关卡数量 / Number of loaded levels

> 已选择的 Actor 数量 / Number of selected actors

> 场景中的 Actor 总数 / Total number of actors in scene

> Top-N Actor 类计数 / Top-N actor class counts

> * 完整的场景上下文信息  * Complete scene context information  *   * 包含用于 AI 上下文注入的所有相关场景数据：  * Contains all relevant scene data for AI context injection:  * - 关卡层次结构和 Actor / Level hierarchy and actors  * - 已选择的 Actor / Selected actors  * - 视口相机位置 / Viewport camera position  * - 场景统计信息 / Scene statistics

> 世界类型（例如 "Editor"、"PIE"）/ World type (e.g., "Editor", "PIE")

> 所有已加载的关卡及其 Actor / All loaded levels and their actors

> 当前选中的 Actor / Currently selected actors
