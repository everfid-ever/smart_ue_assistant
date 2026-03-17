# Variable Types

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Editor_Blueprint_VariableTypes_VariableTypes.INT.udn -->

## Content

### Bool

A Bool (or boolean) is a '_true_' or '_false_' value.

### Byte

A byte uses 8 bits and represents a whole number between 0 and 255.

### Int

An integer is a whole number, it cannot have a fractional part. Examples would be 2, -6, 1045.

### Float

A floating point number can contain fractional parts. Examples would be 1.0, -3.7, 10432.89.

### Name

A name is a piece of text that is used to identify something within the game. Comparing two names is much faster than comparing two strings.

### String

A string is a piece of text.

### Text

A Text variable is used for localized text. You should use this if this text will ever be shown to the user so it can be translated to different languages.

### Vector

A Vector describes a position or direction in 3D space and is made up of X, Y, and Z components.

### Rotator

A Rotator describes an orientation in 3D space, and is mode up of X (Roll), Y (Pitch), and Z (Yaw) components.

### Transform

A Transform is a 3D affine transformation containing translation, rotation, and 3D scale.

### Array

An Array is an ordered series. You can have an array of any type of variable. Arrays are useful when you need more than one of something. You can access an entry in an array by its index.

### Object

Hard asset reference. The referenced asset will be:
- Loaded if this asset is. 
- Cooked if this asset is.

### Class

Hard class reference. The referenced class will be:
- Loaded if this asset is. 
- Cooked if this asset is.

### SoftObject

Soft asset reference.The referenced asset will be:
- Not automatically loaded when this asset is.
- Cooked if this asset is.

### SoftClass

Soft class reference.The referenced class will be:
- Not automatically loaded when this asset is.
- Cooked if this asset is.