# UnrealAgent\Source\UnrealAgent\Public\Commands\UAAssetManageCommands.h

## 函数

- `GetSupportedMethods`
- `GetToolSchema`
- `Execute`
- `ExecuteCreateAsset`
- `ExecuteDuplicateAsset`
- `ExecuteRenameAsset`
- `ExecuteDeleteAsset`
- `ExecuteSaveAsset`
- `ExecuteCreateFolder`

## 文档注释

> * 资产管理操作命令 — 补全资产的"增删改"操作。  *  * 支持的方法:  *   - create_asset:    创建新资产（Material, Blueprint, MaterialInstance, DataTable 等）  *   - duplicate_asset: 复制资产  *   - rename_asset:    重命名/移动资产  *   - delete_asset:    删除资产（带引用安全检查）  *   - save_asset:      保存资产或全部保存  *   - create_folder:   创建文件夹
