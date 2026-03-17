# UPhysicsConstraintComponent RTTs

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UPhysicsConstraintComponent_UPhysicsConstraintComponent.INT.udn -->

## Content

### ConstraintActor1

This is the first actor attached to the joint. The joint is not effective if this is empty.

### ComponentName1

If you would like to constrain a specific component of the specified actor above, you can provide a Component Name here. If the root of the Actor is of a type that can be constrained, it will be the default Component that is constrained. However, if you provide a valid Component Name here, that Component will become the target of the Physics Constraint. If that Component is a Skeletal Mesh, you must also provide a Bone name in the appropriate property.

### ConstraintActor2

This is the second actor attached to the joint.

### ComponentName2

If you would like to constrain a specific component of the specified actor above, you can provide a Component Name here. If the root of the Actor is of a type that can be constrained, it will be the default Component that is constrained. However, if you provide a valid Component Name here, that Component will become the target of the Physics Constraint. If that Component is a Skeletal Mesh, you must also provide a Bone name in the appropriate property.