# APlayerCameraManager

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_APlayerCameraManager_APlayerCameraManager.INT.udn -->

## Overview

Overview of the PlayerCameraManager class

## Content

### APlayerCameraManager

The PlayerCameraManager class is a camera manager. By default, its own built-in behavior is blending between pending view targets and debug cameras triggered by console commands. Otherwise, it queries the ViewTarget for what to do for the camera's viewpoint, and all other camera settings.