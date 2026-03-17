# UMaterialInstanceConstant

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_Types_UMaterialInstanceConstant_UMaterialInstanceConstant.INT.udn -->

## Overview

Overview of the MaterialInstanceConstant class

## Content

### UMaterialInstanceConstant

Material Instances may be used to change the appearance of a material without incurring an expensive recompilation of the material.  General modification of the material cannot be supported without recompilation, so the instances are limited to changing the values of predefined material parameters.  The parameters are statically defined in the compiled material by a unique name, type, and default value.