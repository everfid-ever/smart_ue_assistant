# UnrealAgent\Source\UnrealAgent\Public\Commands\UAScreenshotCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteTakeScreenshot`
- `ExecuteGetAssetThumbnail`
- `ExecuteEditorScreenshot`
- `FindTargetWidgetForEditorScreenshot`
- `GetResolutionFromQuality`
- `SaveBitmapToPng`
- `GetScreenshotDir`

## 文档注释

> * 截图命令模块 — 视口截图 + 资产缩略图  *  * 支持的方法:  *   - take_screenshot:     截取场景或编辑器窗口截图  *   - get_asset_thumbnail: 获取资产缩略图

> editor 模式：截取编辑器 UI 面板（材质编辑器内容区域、蓝图编辑器、Details 面板等）

> 根据 target 参数定位需要截图的 SWidget（面板级精准截图）

> 根据 quality 字符串获取目标分辨率

> 保存 color 数组为 PNG 文件

> 获取截图保存目录
