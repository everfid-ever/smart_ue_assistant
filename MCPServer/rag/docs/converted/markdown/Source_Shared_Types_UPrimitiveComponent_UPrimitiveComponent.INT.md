# UPrimitiveComponent RTTs

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UPrimitiveComponent_UPrimitiveComponent.INT.udn -->

## Content

### bAlwaysCreatePhysicsState

If disabled, there will be a run time processing overhead for creating the Physics State for this component if it is collided with or starts simulating.

### bGenerateOverlapEvents

An overlap between two objects will register if both objects set this flag to true. This way an object can opt out of all overlap events by turning its own flag off.
Once an overlap event occurs, it will generate an Event for Blueprints or Code to use to define behavior. With Multi Body Overlap disabled, only a single overlap event will be generated when any number of Physics Bodies are overlapping it.
The collision profiles of the overlapping objects determine if an overlap will generate a Hit Event or an Overlap Event.

### bMultiBodyOverlap

If set to True, this will allow this Component to generate overlap events for every Physics Body it contains.

If disabled, only one overlap event will be generated for all the physics bodies this Component contains.

### bCheckAsyncSceneOnMove

This flag, though appearing everywhere, only works on the capsule associated with a movement component, such as the one that comes with creating a Character Blueprint.

Outside of this one case, Physics Bodies can only exist and interact in one of the two scenes.

### bTraceComplexOnMove

This flag, though appearing everywhere, only works on the capsule associated with a movement component, such as the one that comes with creating a Character Blueprint.

Complex Collision is per-face collision, allowing a character to collide and interact with concave shapes or more complicated Actors. However, it is more costly to compute and should only be used if necessary.

### bReturnMaterialOnMove

Only useful when used on the collision object for a Movement Component, such as the one that comes with a Character or Pawn.

When enabled, this will return the Phys Material in the hit result.

![](PhAT_hitReturn.png)

### bCanEverAffectNavigation

Defines if this component can ever influence navigation. If disabled, the component will never influence navigation.