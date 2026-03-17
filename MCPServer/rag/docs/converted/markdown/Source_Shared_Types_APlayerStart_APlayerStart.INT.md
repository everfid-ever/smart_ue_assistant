# APlayerStart

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_APlayerStart_APlayerStart.INT.udn -->

## Overview

Overview of the PlayerStart class

## Content

### APlayerStart

The Player Start actor specifies a possible starting point for a player.

-   If the level contains more than one Player Start actor, the engine chooses one at random.

-   The newly spawned player character adopts both the position and rotation of the chosen Player Start actor. The facing direction of the Player Start actor is shown in the editor viewport by the light blue arrow on its gizmo.

-   If the Player Start gizmo shows a "bad size" warning in the editor viewport, move the actor so that it doesn't overlap any other objects in the level.