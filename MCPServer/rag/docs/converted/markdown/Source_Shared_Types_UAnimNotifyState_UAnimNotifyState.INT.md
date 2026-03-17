# UAnimNotifyState

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UAnimNotifyState_UAnimNotifyState.INT.udn -->

## Overview

Overview of the AnimNotifyState class

## Content

### UAnimNotifyState

AnimNotifyStates (Notify States) work much like the standard notifies.
 They have 3 distinct events: a start, the "tick," and an end. The start straightforward, firing at the moments the notify begins and ends, and the Event Graphs in them fire off when their time comes up in the animation. The tick fires off every animation update until the end event is hit. The major difference between the standard Notifies is that AnimNotifyStates are self-contained Blueprints.