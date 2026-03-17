# ASpectatorPawn

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_ASpectatorPawn_ASpectatorPawn.INT.udn -->

## Overview

Overview of the SpectatorPawn class

## Content

### ASpectatorPawn

The SpectatorPawn class is a subclass of DefaultPawn.

Like DefaultPawn, it has a spherical CollisionComponent, although the StaticMeshComponent is not created. The movement for the SpectatorPawn class is handled in the SpectatorPawnMovementComponent; the no-gravity flying behavior is the same as in the DefaultPawnMovementComponent, with added code for handling or ignoring time dilation as necessary.