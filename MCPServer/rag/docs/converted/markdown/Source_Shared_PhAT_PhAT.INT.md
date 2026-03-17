# PhAT RTTs

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_PhAT_PhAT.INT.udn -->

## Content

### SimulationNormal

Toggling the Simulation will set all the Physics Bodies in the Physics Asset to Awake and apply gravity. This will preview how the Physics Asset will work when enabled in the engine.

It will also show you if you have any Physics Bodies that start interpenetrating each other as the system will expel them from each other using a sizable force. This will result in your skeletal mesh looking like it has exploded.

Also you can check to see how long the Physics Asset takes to come to rest and set itself back to Sleep. If the Skeletal Mesh proceeds to "vibrate" on the ground for long periods of time, you can adjust which Physics Bodies collide with each other, increase the damping on the Physics Bodies and/or Constraints, or even increase the solver iterations for individual Physics Bodies.

![](PhAT_Sim.png)

### SimulationNoGravity

Toggling the Simulation will set all the Physics Bodies in the Physics Asset to Awake. This will preview how the Physics Asset will work when enabled in the engine.

It will also show you if you have any Physics Bodies that start interpenetrating each other as the system will expel them from each other using a sizable force. This will result in your skeletal mesh looking like it has exploded.

Without gravity, unless some Physics Bodies are interpenetrating, the Physics Asset will most likely go to sleep immediately. You can use the Ctrl + Left or Ctrl + Right mouse buttons to interact with the Physics Asset.

![](PhAT_Sim.png)

### TranslationMode

Enables the Translation tool in the Physics Asset Editor. This works the same as the normal Translation tool in the main editor. Both Physics Bodies and Constraints can be moved.

When moving a Constraint, only one of the effectors will be movable. It will offset the Bone that Constraint is associated with to the location you move it to.

![](PhAT_moveTool.png)

### RotationMode

Enables the Rotation tool in the Physics Asset Editor. This works the same as the normal Rotation tool in the main editor. Both Physics Bodies and Constraints can be rotated.

When rotating a Constraint, only one of the effectors will be rotatable. It will offset the Bone that Constraint is associated with to the orientation you rotate it to.

![](PhAT_rotateTool.png)

### ScaleMode

Enables the Scale tool in the Physics Asset Editor. This works the same as the normal Scale tool in the main editor. Only Physics Bodies can be scaled.
![](PhAT_scaleTool.png)

### Snap

After a re-factor of the viewports, the snap settings were moved to the main editor viewport. Due to this, the local snapping tools within the Physics Asset Editor have been disabled.

### ResetEntireAsset

Given this process will remove all changes you have made to the Physics Asset, you will be given a warning:
![](PhAT_restetWarning.png)

Upon accepting this, the New Physics Asset dialog with the default settings will show:

![](PhAT_restetDefault.png)

[For more information on the New Physics Asset dialog, click here.](Engine/Physics\PhAT)

### CopyProperties

Copies all the properties from one Physics Body to another, or from one Constraint to another. This includes things like the type of Physics Body (box, sphere, or sphyl), relative position, rotation, and scale.

This is primarily useful for copying down a long chain of Bones where the orientation of the Bones does not change. It can be used to mirror a humanoid character, but only if the mirrored joints have the same orientation.

### EditingMode_Body

The default editing mode of the Physical Asset Tool. This mode will allow you to select, manipulate, adjust properties on, add, or remove Physics Bodies.

If no Physics Body is selected, only the New Body tool will be available to use.
![](PhAT_bodyEditing.png)

It is worth noting that both the Body Editing and Constraint Editing modes remember which Modes are enabled in the viewport.

### EditingMode_Constraint

Enabling the Constraint Editing mode will allow you to select and edit the Physics Constraints of the Physics Asset. Outside of the properties of the constraints, you can change their position and rotation.

If no Constraint is selected, only the Snap All tool will be available to use.
![](PhAT_constraintEditing.png)

It is worth noting that both the Body Editing and Constraint Editing modes remember which Modes are enabled in the viewport.

### AddSphere

This will add a Sphere to the currently selected Physics Body or the Bone selected in the Hierarchy Panel.
![](PhAT_addSphere.png)

### AddSphyl

This will add a Sphyl to the currently selected Physics Body or the Bone selected in the Hierarchy Panel.
![](PhAT_addSphyl.png)

### AddBox

This will add a Box to the currently selected Physics Body or the Bone selected in the Hierarchy Panel.
![](PhAT_addBox.png)

### EnableCollision

This will enable collision between two Physics Bodies in the Physics Asset. The work flow for this tool is:
1. Select two or more Physics Bodies.
1. Click the "Collision On" button.

![](PhAT_collisionOn.png)

Physics Bodies that the currently selected Physics Body can collide with will appear bluish, while ones that will not collide are gray. Yellow Physics Bodies are welded to the currently selected Physics Body.

### DisableCollision

This will disable collision between two Physics Bodies in the Physics Asset. The work flow for this tool is:

1. Select two or more Physics Bodies, using Ctrl + left mouse click.
1. Click the "Collision Off" button.

![](PhAT_collisionOff.png)

Physics Bodies that the currently selected Physics Body can collide with will appear bluish, while ones that will not collide are gray. Yellow Physics Bodies are welded to the currently selected Physics Body.

### WeldToBody

1. Select 2 or more Physics Bodies, using  Ctrl + left mouse click.
1. Click the "Weld" button or use the right click context menu "Weld" command.

Yellow Physics Bodies are welded to the currently selected Physics Body.

### DuplicatePrimitive

This will duplicate the currently selected Physics Body, including all properties, scale, and rotation. However, to make it easier to manipulate, the new Physics Body's location will be offset from the Original's.

### RestetBoneCollision

This will reset the selected Physics Body, by using the New Physics Asset dialog. Since this operation is not Undoable, it will give you a chance to stop:

![](PhAT_resetBone.png)

If you continue, you will receive the New Physics Asset dialog, but unlike "Reset Asset," after clicking "Ok" only the selected Physics Body will have its properties regenerated.

![](PhAT_restetDefault.png)

### DeletePrimitive

Deletes the currently selected Physics Body, you can also use the "Del" key. This will also remove the constraint associated with the Physics Body and it will remove any non-generated collision settings.

If "Prompt on Bone Delete" in the Advanced category of the Physics Asset Tools options (deselect any Physics Bodies or Constraints) is set to True, you will get this warning.

![](PhAT_DelBone.png)

### PlayAnimation

This is only available during Simulation.

![](PhAT_playAnim.png)

If "Physics Blend" in the Anim category of the Physics Asset Tools options (deselect any Physics Bodies or Constraints) is set to anything less than 1.0, some amount of animation will be played on the Skeletal Mesh in the viewport of the Physics Asset Tool.

### ConvertToBallAndSocket

Sets the Constraint's properties to mimic the motion of a Ball and Socket Joint. Locked linear motion but free angular motion on all axes.

### ConvertToHinge

Sets the Constraint's properties to mimic the motion of a Hinge Joint. Locked linear motion but free rotational on Angular Twist Motion.

Using the "Q" key will cycle which axis is the hinge.

### ConvertToPrismatic

Sets the Constraint's properties to mimic the motion of a Prismatic Joint. Locked angular motion on all axes, Linear YMotion, and Linear ZMotion, but free movement along Linear XMotion. This would be like the legs of a camera tripod or a hydraulic piston.

Using the "Q" will cycle which axis is the prismatic axis.

### ConvertToSkeletal

Sets the Constraint's properties to mimic the motion of a Skeletal Joint. Locked on all Linear Motions, but limited on all the Angular Motions. The defaults will work much like Ball and Socket Joint, but its angular movements are limited and Soft Swing and Twist limits are set (but extremely liberal).

Using the "Q" key will cycle which axis is the Twist Motion axis.

### SnapConstraint

This will set the location and rotation of the currently selected constraint to the position and rotation of the Bone it is associated with.

![](PhAT_SnapConstraint.png)

### SnapAllConstraints

Like Snap Constraint, this will take all constraints in the Physics Asset and set their locations and rotations to the location and rotation of the Bones they are associated with.

### CopyJointSettings

This will copy the currently selected Constraint's settings to all other Constraints in the Physics Asset.

![](PhAT_copyAllConstraintsWarn.png)

This is process is undoable.

### DeleteConstraint

This will delete the currently selected Constraint. This will completely free the Physics Bodies down the Bone chain from the Constraint, they will operate as a separate entity.

This is process is undoable.

To regenerate a delete Constraint, you must delete one of the Physics Bodies that it was associated with, then use "New Body" to recreate the Physics Body, thusly recreating the Constraint.

### ShowSkeleton

This option will enable a line representation of the skeleton of the Skeletal Mesh. While working with the Physics Asset Tool, it will be rendered in white, but while simulating it will be rendered in red.
![](PhAT_showSkel.png)

### DrawGroundBox

Enables or disables the ground box. Does not disable collision with the ground box, just the showing of the box.

### ShowFixedBodies

This will show any Physics Body set to "Fixed" in its Physics Type property to render red.

### ToggleGraphicsHierarchy

Similar to Toggle Skeleton, in that it will render a line representation of the Skeleton of the Skeletal Mesh, but show Hierarchy will also (by default) show the names of the Bones in the Skeleton.

![](PhAT_toggleHier.png)

If "Show Names in Hierarchy" is set to False in the Physics Asset Tool's settings (accessed in the Details pane by deselecting any Physics Body or Constraint), this will appear to work exactly like Toggle Skeleton.

### ToggleBoneInfuences

With a Physics Body selected, the vertices of the Bone the selected Physics Body is associated with, will show as green lines extending in the direction of the normal of the vertex.
![](PhAT_showInf.png)

### ToggleMassProperties

During Simulation in the Physics Asset Tool, this will show the masses of the Physics Bodies as they simulate.
![](PhAT_massProps.png)

### MovementSpace_Local

Sets the movement and rotation widgets to operate in Local Space.
![](PhAT_widgetLocal.png)

### MovementSpace_World

Sets the movement and rotation widgets to operate in World Space.
![](PhAT_widgetWorld.png)

### MeshRenderingMode_Solid

![](PhAT_meshRenderSolid.png)

### MeshRenderingMode_Wireframe

![](PhAT_meshRenderWire.png)

### MeshRenderingMode_None

![](PhAT_meshRenderOff.png)

### CollisionRenderingMode_Solid

Sets the rendering mode for the Physics Bodies to translucent solid.
![](PhAT_solidShowBodies.png)

### CollisionRenderingMode_Wireframe

Changes the rendering mode for the Physics Bodies to wireframe.
![](PhAT_wireShowBodies.png)

### CollisionRenderingMode_None

Turns off rendering of Physics Bodies.
![](PhAT_noShowBodies.png)

### ConstraintRenderingMode_None

Hides all Constraints.
![](PhAT_showNoConst.png)

### ConstraintRenderingMode_AllPositions

This mode will simply show the Constraint positions.
![](PhAT_shoConstraints.png)

### ConstraintRenderingMode_AllLimits

This mode will show all Constraint positions and their Limits representations.
![](PhAT_showConstraintandLimits.png)