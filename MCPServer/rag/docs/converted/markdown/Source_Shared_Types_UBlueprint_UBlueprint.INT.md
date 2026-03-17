# UBlueprint

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UBlueprint_UBlueprint.INT.udn -->

## Overview

Overview of the Blueprint class

## Content

### UBlueprint

A Blueprint Class is an asset that content creators can use to easily add functionality on top of existing gameplay classes. Often shortened as just Blueprint. Blueprints are created inside of Unreal Editor visually, instead of by typing code, and saved as assets in a content package. They essentially define a new class or type of Actor, which can then be placed into maps as instances that behave like any other type of Actor.

### UBlueprint_FunctionLibrary

Functions are node graphs belonging to a particular Blueprint that can be executed, or called, from another graph within the Blueprint. Functions have a single entry point designated by a node with the name of the function containing a single exec output pin. When the function is called from another graph, the output exec pin is activated causing the connected network to execute.

### UBlueprint_Macro

A Blueprint Macro Library is a Blueprint container that holds a collection of macros or self-contained graphs that can be placed as nodes in other Blueprints. These can be time-savers, because they can store commonly used sequences of nodes, complete with inputs and outputs for both execution and data transfer. Macros are shared among all graphs that reference them, but they are auto-expanded into the graph as if they were a collapsed node during compiling. This means that Blueprint Macro Libraries do not need to be compiled, but changes to a macro are only reflected in graphs that reference that macro when the Blueprint containing those graphs is recompiled.

### UBlueprint_Interface

A Blueprint Interface is a type of asset in which undefined functions are created. Any Blueprint can implement this Interface and then create its own definition of those functions. This serves as one way for Blueprints to communicate to one another, particularly when one Blueprint interacts with many other Blueprints.