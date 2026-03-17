# Animation Node Reference

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_GraphNodes_Animation_BlendNodes.INT.udn -->

## Overview

Descriptions of the various animation nodes available for use in Animation Blueprints

## Content

### UAnimGraphNode_LayeredBoneBlend

Layered blend (per bone) has a dynamic number of blendposes that can blend per different bone sets.

### UAnimGraphNode_BlendListByBool

This node is effectively a 'branch', picking one of two input poses based on an input Boolean value.

### UAnimGraphNode_BlendListByEnum

Blend List by Enum allows a blend pose to be selected based on a supplied enum value.

### UAnimGraphNode_BlendListByInt

Blend list by int allows a blend pose to be selected based on a supplied index.

### UAnimGraphNode_TwoWayBlend

The standard **Blend** node is a straight mixing of the two input poses based on an alpha input.

---

**Input Pins**

A - The first pose to be blended. 
B - The second pose to be blended. 
Alpha - A `float` value in the range **[0.0, 1.0]** to use as the alpha value to determine the weighting of the two poses. A value of **0.0** gives full weighting to the **A** input pose, while a value of **1.0** gives full weighting to the **B** input pose. 

---

**Output Pins**

Pose - The final pose after the blending has been applied.

### UAnimGraphNode_ApplyAdditive

Applies the supplied additive pose blended by the Alpha parameter.

### UAnimGraphNode_ComponentToLocalSpace

Convert a pose in component space (each bones transform is relative to the mesh component) to local space (each bones transform is relative to its parent bone).

### UAnimGraphNode_LocalToComponentSpace

Convert a pose in local space (each bones transform is relative to its parent bone) to component space (each bones transform is relative to the mesh component).

### UAnimGraphNode_MeshRefPose

Outputs the reference pose of the mesh.

### UAnimGraphNode_IdentityPose

Returns an identity pose.

### UAnimGraphNode_LocalRefPose

Returns the reference pose of the mesh in local space.

### UAnimGraphNode_RotateRootBone

Rotate Root Bone allows the arbitrary rotation of a bone outside of animation data.

### UAnimGraphNode_SaveCachedPose

Saves the supplied pose so that it can be accessed and used at a later point.

### UAnimGraphNode_SequenceEvaluator

Evaluates the specified animation at a single specified frame.

### UAnimGraphNode_SequencePlayer

Plays back the specified animation.

### UAnimGraphNode_Slot

A slot node blends animation data from the named slot on the currently playing animation montages onto the pose.

### UAnimGraphNode_UseCachedPose

Allows the use of a previously cached pose.

### UAnimGraphNode_CopyBone

Copies a transform from one bone to another. This can copy translation, rotation, and scale or a combination of all three.

### UAnimGraphNode_ModifyBone

Modifies the transform of a bone.

### UAnimGraphNode_RotationMultiplier

The Apply a Percentage of Rotation control drives the Rotation of a target bone at some specified percentage of the Rotation of another bone within the Skeleton.

### UAnimGraphNode_SpringBone

The Spring Controller applies a spring solver that can be used to limit how far a bone can stretch from its reference pose position and apply a force in the opposite direction.

### UAnimGraphNode_TwoBoneIK

The Two Bone IK control applies an inverse kinematic (IK) solver to a 3-joint chain, such as the limbs of a character.

### UAnimGraphNode_BlendSpacePlayer

Plays back the specified BlendSpace.

### UAnimGraphNode_BlendSpaceEvaluator

Evaluates the BlendSpace at the single frame specified.

### UAnimGraphNode_RotationOffsetBlendSpace

Applies a rotational offset BlendSpace.

### UAnimGraphNode_Fabrik

Applies the FaBRIK (Forward and Backward Reaching Inverse Kinematics) algorithm to a bone chain to solve bone transforms relative to an end effector.

### UAnimGraphNode_BoneDrivenController

Drives the transform component of a bone based on the transform component of another. Each component of translation and rotation can be used as a source and target for this node, or the scale as a whole. For example driving the Z translation from the X rotation of another bone. The final output can be modifier using a multiplier.

### UAnimGraphNode_LookAt

Modifies a bone transform to look at another bone along a specified axis, or to look at a specified location.

### UAnimGraphNode_HandIKRetargeting

Handles re-targeting of an IK Bone chain. Moves IK bone chain to meet FK hand bones, based on HandFKWeight (to favor either side). (0 = favor left hand, 1 = favor right hand, 0.5 = equal weight).

### GraphNode_FastPathInfo

Animation nodes can use the 'fast path', avoiding somewhat slower Blueprint usage by ensuring that they either:
- Access member variables directly.
- Access a negated boolean member variable.
- Access members of a nested struct.
- Access some "Break Struct" cases as well (Break Transform being a notable exception).