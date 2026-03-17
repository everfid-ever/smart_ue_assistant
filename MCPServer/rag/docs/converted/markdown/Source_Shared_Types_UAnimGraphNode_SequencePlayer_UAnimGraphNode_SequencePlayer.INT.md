# Source Shared Types UAnimGraphNode SequencePlayer UAnimGraphNode SequencePlayer.INT

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UAnimGraphNode_SequencePlayer_UAnimGraphNode_SequencePlayer.INT.udn -->

## Content

### SyncGroup

Sync group settings for this player.  Sync groups keep related animations with different lengths synchronized.

Sync Groups solve this problem by allowing one primary animation node to serve as the Leader, and all other related animations will simply scale their time length to match. Typically, the leader is the node with the greatest blend weight. As the weight blends and the follower's weight exceeds the leader, the follower becomes the leader. In this way, the two animations can work smoothly together offering a seamless transition from one motion to the next.