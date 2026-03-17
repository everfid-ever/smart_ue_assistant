# Components Mode

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Editors_BlueprintEditor_ComponentsMode_ComponentsMode.INT.udn -->

## Overview

Overview of Components mode.

## Content

### RootComponent

The root component represents the root of the Blueprint's visible scene hierarchy when it is placed into the world.

Additional components are attached to it and use a relative transform.

If the root component is constructed by the Blueprint, you can replace it in the editor by dragging and dropping a child component onto the root.

Only the Scale and Mobility fields of the root component's transform can be edited in the Details tab. Location and Rotation fields are linked to the Actor's overall location and rotation in the scene, and are automatically set by the editor.

### NativeComponents

A "native" component is a component that will be constructed by a native C++ parent class.

If it is the root component, it cannot be replaced. Constructed components are always attached to a native root component.

Native components cannot be renamed, moved, or deleted within the overall scene hierarchy. A native component also cannot be duplicated within the hierarchy if its class is abstract or otherwise is not marked as a BlueprintSpawnableComponent.

### InheritedComponents

An "inherited" component is a component that will be constructed by a parent Blueprint class.

If it is the root component, it cannot be replaced. Constructed components are always attached to an inherited root component.

Inherited components also cannot be renamed, moved, or deleted within the overall scene hierarchy.