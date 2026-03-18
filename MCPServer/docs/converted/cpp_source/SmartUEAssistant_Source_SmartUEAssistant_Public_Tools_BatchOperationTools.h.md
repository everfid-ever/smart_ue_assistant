# SmartUEAssistant\Source\SmartUEAssistant\Public\Tools\BatchOperationTools.h

## 函数

- `FBatchRenameActorsTool`
- `GetSpec`
- `Execute`
- `FBatchSetVisibilityTool`
- `FBatchSetMobilityTool`
- `FBatchMoveToLevelTool`
- `FBatchSetTagsTool`
- `FAlignToGroundTool`
- `FDistributeActorsTool`

## 文档注释

> * 批量重命名选中的 Actor，支持前缀、后缀和编号  * Batch rename selected actors with prefix, suffix, and numbering support  *   * 参数 / Parameters:  * - Prefix (string, 可选): 在 Actor 名称前添加的文本 / Text to add before actor names  * - Suffix (string, 可选): 在 Actor 名称后添加的文本 / Text to add after actor names  * - StartIndex (numbe

> * 批量设置选中 Actor 的可见性  * Batch set visibility for selected actors  *   * 参数 / Parameters:  * - Visible (boolean): Actor 是否应该可见 / Whether actors should be visible  * - ApplyToChildren (boolean, 可选): 递归应用到所有子对象 / Apply to all children recursively

> * 批量设置选中 Actor 的移动性  * Batch set mobility for selected actors  *   * 参数 / Parameters:  * - Mobility (string): "Static"、"Stationary" 或 "Movable" / "Static", "Stationary", or "Movable"

> * 批量将选中的 Actor 移动到指定关卡  * Batch move selected actors to a specific level  *   * 参数 / Parameters:  * - LevelName (string): 目标关卡的名称 / Name of the target level

> * 批量设置 Actor 标签  * Batch set actor tags  *   * 参数 / Parameters:  * - Tags (array of strings): 要设置的标签 / Tags to set  * - Mode (string): "Set"、"Add" 或 "Remove" / "Set", "Add", or "Remove"

> * 将选中的 Actor 对齐到地面/表面  * Align selected actors to ground/surface  *   * 参数 / Parameters:  * - AlignRotation (boolean, 可选): 将旋转对齐到表面法线 / Align rotation to surface normal  * - Offset (number, 可选): 距离表面的 Z 轴偏移 / Z-axis offset from surface

> * 按模式分布选中的 Actor  * Distribute selected actors in a pattern  *   * 参数 / Parameters:  * - Pattern (string): "Line"、"Grid"、"Circle" 或 "Random" / "Line", "Grid", "Circle", or "Random"  * - Spacing (number): Actor 之间的距离 / Distance between actors  * - Rows (number, 可选): 网格模式的行数 / For grid pattern  * - Co
