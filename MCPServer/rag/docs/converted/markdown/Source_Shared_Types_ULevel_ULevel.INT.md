# ULevel

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_ULevel_ULevel.INT.udn -->

## Overview

Overview of the Level class

## Content

### ULevel

The Unreal Engine organizes Actors into what are called Levels. Each Level can contain a number of Actors of different types (meshes, lights, effects, landscape, volumes, etc). Each level can be loaded and unloaded independently, and usually exists as a separate file on disk. Levels can overlap spatially, so you can use them as a way of organizing your world, to allow multiple people to work on different aspects at once. There is also a World Composition system that will automatically break up your world into multiple levels and load and unload them as you move around.