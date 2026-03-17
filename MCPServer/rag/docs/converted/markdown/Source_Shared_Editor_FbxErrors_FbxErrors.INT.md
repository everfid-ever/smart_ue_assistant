# FBX Import Errors

<!-- Document metadata -->
<!-- Availability: Public -->
<!-- Source: Source_Shared_Editor_FbxErrors_FbxErrors.INT.udn -->

## Overview

Descriptions of errors generated during importing FBX files.
Version: 4.9

[TOC(start:2 end:3)]

This is a list of error or warning messages you may encounter during importing FBX files. 

## Generic 

(#Generic_ImportingNewObjectFailed)

## Content

### Generic_ImportingNewObjectFailed

Importing failed to create new asset. In this case, you are likely to have other warning messages that indicate the cause of the failures.

### Generic_LoadingSceneFailed

Loading FBX Scene has failed. Either the file is corrupted or it is not the correct file type.

### Generic_SameNameAssetExists

An asset already exists with the given name. Make sure to use a different name to import or import into a different folder.

### Generic_SameNameAssetOverriding

Currently importing asset is going to replace currently existing asset of the same name.

### Generic_CannotDeleteReferenced

When overriding existing assets, the importer needs to delete the old asset first, however the importer cannot delete it because of references.

Try using a different name or importing into a different folder.

### Generic_FBXFileParseFailed

Opening file and importing has failed. Either the file is corrupted or it is not the correct file type.

### Generic_MeshNotFound

No Mesh was found in the file. Make sure the FBX contains a mesh object.

### Generic_Mesh_NoGeometry

Mesh object does not contain geometry.

### Generic_Mesh_TriangulationFailed

Mesh is composed of polygons other than triangles, so the importer attempted to triangulate, but failed. Check the source content and triangulate it in your DCC tool.

### Generic_Mesh_ConvertSmoothingGroupFailed

The importer only supports smoothing on a polygon level, and when smoothing was done by edge, the importer will attempt to convert edge smoothing to polygon smoothing, but that has failed.

(FBX API ComputePolygonSmoothingFromEdgeSmoothing.)

### Generic_Mesh_UnsupportingSmoothingGroup

The importer only supports smoothing on a polygon level, and when smoothing was done by vertex, the importer will attempt to convert vertex smoothing to polygon smoothing, but that has failed.

### Generic_Mesh_MaterialIndexInconsistency

Face Material index is not valid. Either it is mapped to the wrong index or the material is not available. The importer forces the index to 0 when this happens.

### Generic_Mesh_MeshNotFound

FBXMesh object is not found in the node given. Make sure the mesh exists in the scene.

### Generic_Mesh_NoSmoothingGroup

No smoothing group information was found in this FBX scene.  Please make sure to enable the "Export Smoothing Groups" option in the FBX Exporter plug-in before exporting the file.

Even for tools that do not support smoothing groups, the FBX Exporter will generate appropriate smoothing data at export-time so that correct vertex normals can be inferred while importing.

### Generic_Mesh_LOD_InvalidIndex

Invalid Mesh LOD index. In order to add LOD(N), the current mesh should contain all of LOD from [0-(N-1)].

### Generic_Mesh_LOD_NoFileSelected

You should select a file for the LOD. No file was selected.

### Generic_Mesh_LOD_MultipleFilesSelected

You may only select one file for the LOD.

### StaticMesh_TooManyMaterials

Currently the importer supports up to MAX_MESH_MATERIAL_INDEX(64) materials. Break your mesh into multiple pieces to fix this.

### StaticMesh_UVSetLayoutProblem

The light map UV set for Static Mesh appears to have layout problems.  Either the triangle UVs are overlapping one another or the UVs are out of bounds (0.0 - 1.0 range.)

### SkeletalMesh_DifferentRoots

This error is thrown when importing an LOD (or importing a Skeletal Mesh with LODs) and the requested mesh for the LOD does not have the same root bone as the original mesh. They should have same root bone.

### SkeletalMesh_DuplicateBones

The importer cannot have bones with the same name in the Skeletal Mesh hierarchy. Make sure each bone name is unique.

### SkeletalMesh_NoInfluences

The importer did not find any vertices weighted to the skeleton. Skeletal Meshes are required to have at least one vertex weighted to the skeleton.

### SkeletalMesh_RestoreSortingMismatchedStrips

While restoring the sort order for the section, strips could not be matched to the new data.

### SkeletalMesh_RestoreSortingNoSectionMatch

Unable to restore triangle sort setting for the section number in the old mesh, as a matching section could not be found in the new mesh. The custom sorting information has been lost.

### SkeletalMesh_RestoreSortingForSectionNumber

Unable to restore triangle sort setting for the section as the new mesh does not contain that many sections. Please find the matching section and apply manually.

### SkeletalMesh_NoMeshFoundOnRoot

Could not find any valid mesh on the root hierarchy. If you have mesh in the sub hierarchy, please enable option of [Import Meshes In Bone Hierarchy] when importing.

### SkeletalMesh_InvalidRoot

Could not find a valid root node.

### SkeletalMesh_InvalidBone

Failed to find any bone hierarchies. Try to import with the Rigid Mesh option enabled.

### SkeletalMesh_InvalidNode

Could not find any valid Nodes.

### SkeletalMesh_Nothe importerightsOnDeformer

Ignoring this deformer because it did not find any the weighting information.

### SkeletalMesh_NoBindPoseInScene

Scene does not contain a Bind Pose. Make sure you have a Bind Pose in the scene. If you do not, import with [Use Time 0 as Reference Pose] enabled.

### SkeletalMesh_NoAssociatedCluster

No cluster is found.

### SkeletalMesh_NoBoneFound

Could not find any bone nodes. If it is rigid, please use the [Import Rigid Body] option.

### SkeletalMesh_InvalidBindPose

Could not find any valid bind poses. A bind pose can exist but be invalid. Often this can be fixed by recreating bind pose in the DCC tool.

### SkeletalMesh_MultipleRoots

Found multiple roots. The importer only supports one root per mesh.

### SkeletalMesh_BonesAreMissingFromBindPose

Some bones are missing from the bind pose data. If you would like to avoid this, you can import with [Use Time 0 as Reference Pose] enabled or fix the bind pose in your DCC tool.

### SkeletalMesh_VertMissingInfluences

There are vertices in the Skeletal Mesh that are not weighted to a bone. These vertices will be fully weighted to the root bone.

### SkeletalMesh_SectionWithNoTriangle

Input mesh has a section with no triangles.  This mesh may not render properly.

### SkeletalMesh_TooManyVertices

Input mesh has too many vertices. The generated mesh will be corrupt!

Consider adding extra materials to split up the source mesh into smaller chunks.

### SkeletalMesh_FailedToCreatePhyscisAsset

If you have [Create Physics Asset] on, it will try to create physics asset. 

It can fail if:

1. The importer failed to create the Skeletal Mesh (and thusly has no bones to build the Physics Asset)

2. The mesh is too small and the Physics Asset creation default setting will not work with it. 

If this fails, you can create physics asset after imported.

Bring up the Right-Click Context menu on the Skeletal Mesh -> Create... -> Create Physics Asset. You can then adjust the settings for creating a Physics Asset to work with the size of your Skeletal Mesh.

### SkeletalMesh_SkeletonRecreateError

The importer is trying to recreate skeleton, but it failed because an asset exists with the same name, but it is of a different type of asset (eg: Static Mesh). Try to import in a different folder or with a different name.

### SkeletalMesh_ExceedsMaxBoneCount

Your Skeletal Mesh has too many bones, Unreal Engine's current max bone count is 65536.

### SkeletalMesh_NoUVSet

Skeletal Mesh does not have any UVSets. Creating a default set.

### SkeletalMesh_LOD_MissingBone

New mesh is missing bones that are required by the LOD(s). Make sure these bones exist in the new mesh.

### SkeletalMesh_LOD_FailedToImport

Failed to import LOD. Please check other warning/error messages that came up.

### SkeletalMesh_LOD_RootNameIncorrect

Root bone name in the LOD does not match with original mesh root bone name. Make sure both root bone names match.

### SkeletalMesh_LOD_BonesDoNotMatch

New mesh for LOD bones should exist in the original mesh. If it has extra bones, the importer cannot match.

### SkeletalMesh_LOD_IncorrectParent

New mesh for LOD bone hierarchy should match with the original bone hierarchy. The parent does not match for the specified bone.

### SkeletalMesh_LOD_HasSoftVerts

The mesh LOD you are importing has some vertices with more than one influence. If you would like to have soft vertex deformation, please set CheckSingleInfluenceLOD to False in the Editor INI file.

### SkeletalMesh_LOD_MissingSocketBone

The mesh LOD is missing a bone that is required by a socket. This can cause game play artifacts when the Actor switches to the LOD.

### SkeletalMesh_LOD_MissingMorphTarget

Could not find morphtarget for the LOD.

### Animation_CouldNotFindRootTrack

Mesh contains the root bone in the description, but animation does not contain that bone track. The animation data should contain at least root bone track. 

- Make sure if this animation FBX is supposed to be for the given skeleton. 
- Make sure the original mesh contains same bone hierarchy as the animation.

### Animation_CouldNotBuildSkeleton

Failed to build skeleton to create animation track.

### Animation_CouldNotFindTrack

Could not find an animation track.

### Animation_ZeroLength

Animation track length is zero. You can try different options of time options. 

1. Exported Time: Find scene's local start and end time
2. Animated Time: Find root's animated time
3. Set Range: Set range of the frame

### Animation_RootTrackMismatch

Root bone of animation does not match with the root bone of the skeleton it is importing for. Is the animation file intended for this skeleton?

### Animation_DuplicatedBone

Animation contains duplicated bones.

### Animation_MissingBones

Animation contains bones that are not found in skeleton.

### Animation_InvalidData

Animation does not contain any valid animation tracks, takes, or blendshapes.

### Animation_TransformError

This can be caused by using shearing or other forms of transforms the importer does not support. Or this can possibly happen due to a math error. If the animation looks fine in Persona, you can ignore this warning.