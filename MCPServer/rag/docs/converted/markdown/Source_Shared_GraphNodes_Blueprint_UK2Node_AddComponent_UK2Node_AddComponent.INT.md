# UK2Node_AddComponent

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_GraphNodes_Blueprint_UK2Node_AddComponent_UK2Node_AddComponent.INT.udn -->

## Overview

Overview of the Blueprint "Add Component" nodes.

## Content

### ArrowComponent

ArrowComponent is a simple arrow shape rendered using lines (useful for indicating which was an object is facing). When executed, this node creates a new ArrowComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created ArrowComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### AtmosphericFogComponent

AtmosphericFogComponents are used to create fogging effects (such as clouds). When executed, this node creates a new AtmosphericFogComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created AtmosphericFogComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### AudioComponent

AudioComponents are used to provide objects with audio. When executed, this node creates a new AudioComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created AudioComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### BoxComponent

BoxComponent is a simple box shape rendered using lines (generally used for simple collision). When executed, this node creates a new BoxComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created BoxComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### CapsuleComponent

CapsuleComponent is a simple capsule shape rendered using lines (generally used for simple collision). When executed, this node creates a new CapsuleComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created CapsuleComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### CustomMeshComponent

The CustomMeshComponent allows you to generate custom triangle mesh geometry. When executed, this node creates a new CustomMeshComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created CustomMeshComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### DecalComponent

DecalComponent is a material that is rendered onto the surface of a mesh (a kind of 'bumper sticker' for a model). When executed, this node creates a new DecalComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created DecalComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### DestructibleComponent

A DestructibleComponent hold the physics data for a DestructibleActor. When executed, this node creates a new DestructibleComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created DestructibleComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### DirectionalLightComponent

The DirectionalLightComponent acts as a sun like light source. It provides uniform lighting across any surface in its light-mass importance volume. When executed, this node creates a new DirectionalLightComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created DirectionalLightComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### ExponentialHeightFogComponent

The ExponentialHeightFogComponent is much like the AtmosphericFogComponent (used to create fogging effects such as clouds), but with a density that is related to the height of the fog. When executed, this node creates a new ExponentialHeightFogComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created ExponentialHeightFogComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### InstancedStaticMeshComponent

An InstancedStaticMeshComponent is a Static Mesh that can have multiple instances. When executed, this node creates a new InstancedStaticMeshComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created InstancedStaticMeshComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### MaterialBillboardComponent

UMaterialBillboardComponent is a 2d material that will be rendered always facing the camera. When executed, this node creates a new UMaterialBillboardComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created UMaterialBillboardComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### ParticleSystemComponent

A ParticleSystemComponent acts as a particle emitter. When executed, this node creates a new ParticleSystemComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created ParticleSystemComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PawnNoiseEmitterComponent

PawnNoiseEmitterComponent tracks noise event data used by PawnSensingComponents. This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients. 

When executed, this node creates a new PawnNoiseEmitterComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PawnNoiseEmitterComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PawnSensingComponent

PawnSensingComponent encapsulates sensory (i.e. sight and hearing) settings and functionality for an Actor, allowing the Actor to see/hear Pawns in the world. It does nothing on network clients. 

When executed, this node creates a new PawnSensingComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PawnSensingComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PhysicsConstraintComponent

PhysicsConstraintComponent is effectively a joint that allows you to connect two rigid bodies together. You can create different types of joints using the various parameters of this component.

When executed, this node creates a new PhysicsConstraintComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PhysicsConstraintComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PhysicsHandleComponent

PhysicsHandleComponents are utility objects for moving physics Actors around.  When executed, this node creates a new PhysicsHandleComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PhysicsHandleComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PhysicsThrusterComponent

PhysicsThrusterComponents are utility objects for moving physics Actors around. When executed, this node creates a new PhysicsThrusterComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PhysicsThrusterComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PointLightComponent

PointLightComponents are light components that emit light from a single point equally in all directions. When executed, this node creates a new PointLightComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PointLightComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### PoseableMeshComponent

PoseableMeshComponent allows bone Transforms to be driven through Blueprints. When executed, this node creates a new PoseableMeshComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created PoseableMeshComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### ProjectileMovementComponent

ProjectileMovementComponents update position of the associated component during its tick. If the updated component is simulating physics, only the initial launch parameters (when initial velocity is non-zero) will affect the projectile, and the physics sim will take over from there.

When executed, this node creates a new ProjectileMovementComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created ProjectileMovementComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### RadialForceComponent

RadialForceComponents are used to emit a radial force/impulse that can affect physics objects and or destructible objects. When executed, this node creates a new RadialForceComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created RadialForceComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### RotatingMovementComponent

The RotatingMovementComponents are used to update position of their associated PrimitiveComponent each tick. When executed, this node creates a new RotatingMovementComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created RotatingMovementComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SceneCaptureComponent2D

SceneCaptureComponent2D can be used to capture a 'snapshot' of the scene from a single plane and feed it to a render target. 

When executed, this node creates a new SceneCaptureComponent2D for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SceneCaptureComponent2D is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SceneCaptureComponentCube

SceneCaptureComponentCube can be used to capture a 'snapshot' of the scene from 6 planes and feed it to a render target. 

When executed, this node creates a new SceneCaptureComponentCube for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SceneCaptureComponentCube is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SceneComponent

When executed, this node creates a new SceneComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SceneComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SkeletalMeshComponent

When executed, this node creates a new SkeletalMeshComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SkeletalMeshComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SphereComponent

SphereComponent is a simple sphere shape rendered using lines (generally used for simple collision). When executed, this node creates a new SphereComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SphereComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SpotLightComponent

A SpotLightComponent emits a directional cone shaped light (like a Torch). When executed, this node creates a new SpotLightComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SpotLightComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### DecalComponent

DecalComponent acts as a material that is rendered onto the surface of a mesh (a kind of 'bumper sticker' for a model). When executed, this node creates a new DecalComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created DecalComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### SpringArmComponent

SpringArmComponents are used to try and maintain their children at a fixed distance from the parent, but will retract the children if there is a collision and spring back when there is no collision. For example, it could be used as a 'camera boom' to keep the follow camera for a player from colliding into the world.

When executed, this node creates a new SpringArmComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created SpringArmComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### BillboardComponent

UBillboardComponent represents a 2d texture that will be rendered always facing the camera. When executed, this node creates a new UBillboardComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created UBillboardComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### StaticMeshComponent

StaticMeshComponent is used for meshes that do not animate. When executed, this node creates a new StaticMeshComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created StaticMeshComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### TextRenderComponent

TextRenderComponents render text in the world with given font. The component contains usual font related attributes such as Scale, Alignment, Color etc. 

When executed, this node creates a new TextRenderComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created TextRenderComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.

### VectorFieldComponent

When executed, this node creates a new VectorFieldComponent for the specified 'Target' Actor.  

If the 'Manual Attachment' input is left unset (False), then the new component will automatically be attached under the Actor's root (or made the root if one did not previously exist). If the 'Manual Attachment' input is set (True), then the new component is left unattached.

The newly created VectorFieldComponent is returned to the user via the 'Return Value' output. If 'Manual Attachment' was selected, then the user can take it and attach it themselves (via an "Attach to" node).

The 'Relative Transform' input defines where to position and orient the component relative to its parent. If left unattached, then this Transform is relative to the world.