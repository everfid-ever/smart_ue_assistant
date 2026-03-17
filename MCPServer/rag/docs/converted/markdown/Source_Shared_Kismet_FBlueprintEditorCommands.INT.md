# FBlueprintEditorCommands RTTs

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Kismet_FBlueprintEditorCommands.INT.udn -->

## Content

### CompileBlueprint

This will compile the current Blueprint (default keyboard short cut of F7). Any errors or warnings will be flagged in the "Compiler Results" pane, and also any applicable node will have a red warning placed on it.

Performs the same function as the Compile button on the tool bar:

![](k2_compileButton.png)

### RefreshAllNodes

If you are making edits to other Blueprints, and trying to interact or call functions on external Blueprints, the input and output pins for these can change in number and type. This will refresh all the nodes in the current Blueprint, accounting for external changes.

You can do this to an individual node in the graph by right-clicking it and selecting "Refresh Nodes."

### DeleteUnusedVariables

This will go through the Blueprint and find any variable that is not used and remove it.

This process can be undone.

### FindInBlueprints

This will open the "Find Results" pane and set it to search all Blueprints in the project for the given search term.

You can also search all Blueprints by opening the "Find Results" tab (Window -> Find Results) and disabling "Find in Current Blueprint Only."

![](k2_findAll.png)

### FindInBlueprint

This will open the "Find Results" pane and set it to search the current Blueprint for the given search term.

You can also search the current Blueprint by opening the "Find Results" tab (Window -> Find Results) and enabling "Find in Current Blueprint Only."

![](k2_findCurrent.png)

### ReparentBlueprint

This will pop up a dialog enabling you to change the class that the Blueprint inherits from. Really useful if you realize you needed a Character Movement Component, but you started your Blueprint from Actor (that does not contain that component). In this example, you can use this tool to change the parent class of your Blueprint from Actor to Character or Pawn.

![](k2_reparent.png)

### ShowFloor

This will enable or disable the floor in the Viewport of the Component view of the Blueprint Editor.

![](k2_showFloor.png)

### ShowGrid

This will enable or disable the grid in the Viewport of the Component view of the Blueprint Editor.

![](k2_showGrid.png)

### EnableAllBreakpoints

This will enable all disabled breakpoints within the current Blueprint.

Breakpoints can be set on any node in the graph that gets executed, such as "Function Calls" and "Flow Control" operations, by right-clicking on the node and choosing "Add breakpoint." When a breakpoint has been set on a node, a graphic is displayed in the upper-left corner of the node.

![](k2_breakpoint.png)

### DisableAllBreakpoints

This will disable all breakpoints in the current Blueprint, but will keep their locations for future use.

Individual breakpoints can be disabled by right-clicking on the node that has a breakpoint and choosing "Disable breakpoint."

![](k2_breakpoint_disabled.png)

### ClearAllBreakpoints

This will delete all breakpoints in the current Blueprint.

This cannot be undone.

Individual breakpoints can be removed by right-clicking the node with a breakpoint and choosing "Remove breakpoint."

### ClearAllWatches

This will delete all watches in the current Blueprint.

"Watches" are set on non-executing pins, such as the pins on an addition node:

![](k2_watch.png)

They display the value of the pin while the Blueprint is running, say in Play in Editor or Simulate in Editor.

### AddNewVariable

Creates a new variable when clicked. The properties of that variable immediately appear in the Details tab. There, you can change the name, type, and other properties.

By default, the data type of the variable will be the same data type as the last variable created, or if no other variable had been created during the currently running instance of Unreal Editor 4, it will default to the type of Bool.

### AddNewFunction

Creates a new function, then immediately puts focus on the Name field of the Details tab so that it can be named. A new graph view will also be opened where you can define the node network for the function.

### AddNewMacroDeclaration

Creates a new macro, then immediately puts focus on the Name field of the Details tab so that it can be named. A new graph view will also be opened where you can define the node network for the macro.

### AddNewEventGraph

Creates a new Event Graph, then immediately puts focus on the Name field of the Details tab so that it can be named. The new graph appears and is ready to have a node network defined within it.

### AddNewDelegate

Creates a new event dispatcher, then immediately puts focus on the Name field of the Details tab so that it can be named.