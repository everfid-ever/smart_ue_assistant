# AController

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_AController_AController.INT.udn -->

## Overview

Overview of the Controller class

## Content

### AController

Controllers are non-physical Actors that can possess a Pawn (or Pawn-derived class like Character) to control its actions. PlayerControllers are used by human players to control Pawns, while AIControllers implement the artificial intelligence for the Pawns they control. Controllers take control of a Pawn with the Possess function, and give up control of the Pawn with the Unpossess function.