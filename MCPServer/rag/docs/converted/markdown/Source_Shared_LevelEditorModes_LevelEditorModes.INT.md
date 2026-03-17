# Source Shared LevelEditorModes LevelEditorModes.INT

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_LevelEditorModes_LevelEditorModes.INT.udn -->

## Content

### EditorMode.PLACEMENT

###Place
Allows the quick placement of recently placed objects, or common primitives such as lights, triggers, or geometry.

### EditorMode.EM_MeshPaint

###Mesh Paint
The Mesh Paint tool allows you to paint vertex colors on Static Meshes interactively in the level viewport. You can paint multiple instances of a single mesh with unique color/alpha values, and use that data however you would like in your materials.

### EditorMode.EM_Landscape

###Landscape
Landscapes can be created in a couple of different ways. The editing tools provide the ability to create a completely new landscape or you can import a heightmap created previously in Unreal Editor or through external tools. Using external tools to create a base to work from can be a good way of speeding up the landscape creation process. That base can then be imported and cleaned up or modified using the editing tools inside Unreal Editor to customize the landscape and make it fit into the world and desired gameplay.

### EditorMode.EM_Foliage

###Foliage
The Unreal Engine's Foliage tool allows you to quickly paint or erase sets of Static Meshes on Landscape Actors, other Static Mesh Actors, and legacy terrain. These meshes are automatically grouped together into batches that are rendered using hardware instancing, meaning that many instances can be rendered with only a single draw call.

### EditorMode.EM_Geometry

###Geometry Editing
Allows you to edit vertices of placed geometry brushes.