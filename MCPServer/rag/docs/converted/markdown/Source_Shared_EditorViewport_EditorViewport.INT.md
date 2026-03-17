# Source Shared EditorViewport EditorViewport.INT

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_EditorViewport_EditorViewport.INT.udn -->

## Content

### RotateMode

![](EVP_rotate.png)

Enables rotation mode in the 3D viewport. This will allow you to select and rotate Actors in the viewport.

Tip: When selecting multiple Actors (Shift + Left Mouse Click), the last Actor selected will be the rotation point for all the selected Actors:

![](EVP_rotateTip.png)

This works with the Translation and Scale tools as well!

### TranslateMode

![](EVP_translate.png)

Enables translation mode in the 3D viewport. This will allow you to select and move Actors in the viewport.

Tip: You can use the Ctrl + Left Mouse, Right Mouse, or Left + Right Mouse buttons to move an Actor along an axis, without directly interacting with the Translation tool.

* Ctrl + Left Mouse Button constrains to the X axis.
* Ctrl + Right Mouse Button constrains to the Y axis.
* Ctrl + Left and Right Mouse Buttons constrains to the Z axis.

This works with the Rotation tool as well!

### ScaleMode

![](EVP_scale.png)

Enables scale mode in the 3D viewport. This will allow you to select and scale Actors in the viewport.

### CycleTransformGizmoCoordSystem

For rotation and translation only, this will switch between local and world coordinate systems.

While in world mode, the transform tools will align themselves to the grid of the world:

![](EVP_world.png)

While in local mode, the transform tools will align themselves to the rotation of the selected Actor:

![](EVP_local.png)

### LitMode

![](EVP_litMode.png)

The default mode for viewing levels in the main 3D viewport. Lit mode includes all lighting, reflections, and shader details.

### UnlitMode

![](EVP_UnlitMode.png)

Shows the scene as flat lit. No light maps, dynamic lights, static lights, or emissive materials affect the scene.

### BrushWireframeMode

![](EVP_BrushWireframeMode.png)

Displays everything as wireframe, but brushes will be displayed as their brush color and only with their brush shape, not as the triangle they produce.

### WireframeMode

![](EVP_WireframeMode.png)

Displays the raw triangles of everything in the viewport. Turns off back faces to make the scene more readable.

### DetailLightingMode

![](EVP_DetailLightingMode.png)

Only lighting with normal data pulled from materials is rendered. Color emitted from lights will affect the scene.

Roughness and Emissive portions of the material will still affect the output, whereas Metallic and Specular do not.

### LightingOnlyMode

![](EVP_LightingMode.png)

Lighting will be rendered, only taking into account the vertex normals of the scene.

### LightComplexityMode

![](EVP_LightComplexityMode.png)

This view mode shows raw light overlap.

### ShaderComplexityMode

![](EVP_ShaderComplexityMode.png)

Displays the shader complexity in the scene. The darker the green, the more complex the shader, with really complex shaders moving into reds, often seen when many translucent shaders overlap.

### StationaryLightOverlapMode

![](EVP_Overlap.png)

Since only 4 stationary lights can overlap a given location at a time, this view will show you, in red, which stationary lights are being forced to be movable.

### LightmapDensityMode

![](EVP_LightMapDensityMode.png)

Shows the lightmap density of the scene with blue being the least dense and red being the most dense.

### ReflectionOverrideMode

![](EVP_ReflectionsMode.png)

This will render just the reflections of the scene, both from reflection captures and Screen Space Reflections.

### CollisionPawn

![](EVP_PawnCollision.png)

Shows what a Character or Pawn can collide with. Static Mesh collision will show as a green, Volumes as a mild pink, and Brushes as a grayish violet.

### CollisionVisibility

![](EVP_VisMode.png)

Displays what Actors in the scene will block visibility (and only visibility) traces. Static Mesh collision will show as a green, Volumes as a mild pink, and Brushes as a grayish violet.

### ToggleRealTime

Enables the real-time preview of the viewport. This will allow all particle systems, material animations, temporal AA, Skeletal Mesh Actors with a default animation, etc... to animate and update in the viewport.

### ToggleFPS

This will display the viewport's FPS and render time (in ms) on the upper right side of the viewport:

![](EVP_FPS.png)

This will enable Real-Time mode.