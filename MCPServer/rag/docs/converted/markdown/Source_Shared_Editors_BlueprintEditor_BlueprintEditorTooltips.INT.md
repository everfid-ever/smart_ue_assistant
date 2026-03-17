# Source Shared Editors BlueprintEditor BlueprintEditorTooltips.INT

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Editors_BlueprintEditor_BlueprintEditorTooltips.INT.udn -->

## Content

### BlueprintActionMenuContextText

This shows the current context for the action menu.  It depends on how the menu was summoned.

If you opened the menu by dragging off of a wire, the context will be actions that operate on that type (functions or member variables for objects).

If you opened the menu by context-clicking on the background, the context will be actions available in the current blueprint (operating on variables and functions declared here or in a parent class).

### BlueprintActionMenuContextToggle

If checked, the list of available actions and nodes will be filtered to only those that are possible in the current 'context' (actions possible given how you opened the menu).

If you opened the menu by dragging off of a wire, then it will be filtered to variables and functions that operate on that type.

If you opened the menu by context-clicking on the background, then it will be filtered to actions available in the current blueprint (operating on variables and functions declared here or in a parent class).

### MyBlueprint_ShowInheritedVariables

If checked, variables that were declared in parent blueprints and classes will also appear in the 'My Blueprints' tree, allowing you to easily drag them into the graph editor.

### DefaultsMode

The defaults mode lets you edit the default values of any properties on the Blueprint.

### ComponentsMode

The component editing mode lets you:
* Edit the default values of any components on the Blueprint.
* Add new components.
* View the results of placing an instance of a Blueprint.
* Visually adjust component transforms.

### GraphMode

The graph editing mode is where you do all Blueprint logic.

### FindInBlueprint_IndexAll

Older Blueprints do not contain the data they need for searching while unloaded and require resaving. This will auto-checkout any files that are uncached if source control is enabled and will report any failures.

### FindInBlueprint_FailedCache

Blueprints can fail to cache for a few reasons:
* Asset is read only, this may be a result of a failure to checkout through source control.
* Asset cannot fully load, this can be a sign of corruption.