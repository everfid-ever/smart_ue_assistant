# Source Shared GraphNodes Material Material.INT

<!-- Document metadata -->
<!-- Availability: NoPublish -->
<!-- Source: Source_Shared_GraphNodes_Material_Material.INT.udn -->

## Content

### UMaterialExpressionAtmosphericFogColor

The Atmospheric Fog Material Expression allows you to query the current color of the level's Atmospheric Fog, at any position in World Space. If no World Position is fed into it, then the world position of the pixel in question is used. This is useful when you need Materials to appear to fade into a distant fog color.

### UMaterialExpressionAtmosphericLightVector

The Atmospheric Light Vector Material Expression returns the Light Vector for the Directional Light in the scene with 'Atmosphere Sun Light' checked. Useful for effects materials that may want to perform some custom shading using the sun's Light Vector.

### UMaterialExpressionAtmosphericLightColor

The Atmospheric Light Color Material Expression returns the Light Color for the Directional Light in the scene with 'Atmosphere Sun Light' checked. Useful for effects materials that may want to perform some custom shading using the sun's Light Color.

### UMaterialExpressionDesaturation

The Desaturation expression desaturates its input, or converts the colors of its input into shades of gray, based a certain percentage.

### UMaterialExpressionConstant

The Constant expression outputs a single float value. It is one of the most commonly used expressions and can be connected to any input, regardless of the number of channels the input expects. For instance, if you connect a Constant to an input expecting a 3 Vector, the constant value will be used for all 3 elements. When supplying a single number, it can be useful to collapse the node using the small triangle icon in the description area.

### UMaterialExpressionConstant2Vector

The Constant2Vector expression outputs a two-channel vector value, in other words, two constants numbers.

### UMaterialExpressionConstant3Vector

The Constant3Vector expression outputs a three-channel vector value, in other words, three constants numbers. An RGB color can be thought of as a Constant3Vector, where each channel is assigned to a color (red, green, blue).

### UMaterialExpressionConstant4Vector

The Constant4Vector expression outputs a four-channel vector value, in other words, four constants numbers. An RGBA color can be thought of as a Constant4Vector, where each channel is assigned to a color (red, green, blue, alpha).

### UMaterialExpressionDistanceCullFade

The DistanceCullFade expression outputs a scalar value that fades from black to white and can be used to fade an object in once it comes within the cull distance. It should be noted that it does not fade the object out.

### UMaterialExpressionParticleColor

The ParticleColor expression ties into the current color of a given particle based on any per-particle color data defined within Cascade. This must be plugged into the appropriate channel (emissive color).

### UMaterialExpressionParticleDirection

The ParticleDirection expression outputs 3vector (RGB) data on a per-particle basis, representing the direction a given particle is currently traveling.

### UMaterialExpressionParticleMotionBlurFade

The ParticleMotionBlurFade expression outputs a value representing the amount of fade on a particle as a result of motion blur. A value of 1 represents no blur, black represents complete blur.

### UMaterialExpressionParticleRadius

The ParticleRadius expression outputs the radius in Unreal units of each particle individually. This allows, for example, for changes to be made to a material once the radius has reached a certain point.

### UMaterialExpressionParticleRelativeTime

The ParticleRelativeTime expression outputs a number between 0 and 1 representing a particle's age, with 0 being the moment of birth and 1 being the moment of death.

### UMaterialExpressionParticleSize

The Particle Size expression outputs the X and Y size of a particle sprite. This can then be used to drive some aspect of a Material.

### UMaterialExpressionParticleSpeed

ParticleSpeed outputs the current speed each particle is traveling, measured in Unreal units per second.

### UMaterialExpressionPerInstanceFadeAmount

The PerInstanceFadeAmount expression outputs a float value associated with the amount of fade applied to an instanced Static Mesh, such as foliage. It is constant, but can be a different number for each individual instance of a mesh. 

Note: This only works when applied to an InstancedStaticMesh Actor or other Actor which utilizes InstancedStaticMeshComponents.

### UMaterialExpressionPerInstanceRandom

The PerInstanceRandom expression outputs a different random float value per Static Mesh instance to which the material is applied. InstancedStaticMeshComponent sets a random float for instance, which is exposed so that it can be used for whatever is desired (e.g. random light level behind a window). It is constant, but different, for each instance of the mesh.

The output value will be a whole number between 0 and RAND_MAX for the target platform. 

Note: This only works when applied to an InstancedStaticMesh Actor or other Actor which utilizes InstancedStaticMeshComponents.

### UMaterialExpressionTime

The Time node is used to add the passage of time to a material, such as a Panner, Cosine, or other time-dependent operation.

### UMaterialExpressionTwoSidedSign

The TwoSidedSign expression is useful for flipping the normal on backfaces of two sided custom lighting materials to match the functionality of Phong. +1 for frontfaces, -1 for backfaces of a twosided material.

### UMaterialExpressionVertexColor

The VertexColor expression is the access point for the material to the outputs of color modules affecting sprite particles emitters.

### UMaterialExpressionActorPositionWS

ActorPositionWS outputs 3vector (RGB) data representing the location of the object with this material on it in world space.

### UMaterialExpressionCameraPositionWS

The CameraWorldPosition expression outputs a three-channel vector value representing the camera's position in world space.

### UMaterialExpressionLightmapUVs

The LightmapUVs expression outputs the lightmap UV texture coordinates in the form of a two-channel vector value. If lightmap UVs are unavailable, it will output a two-channel vector value of (0,0).

### UMaterialExpressionObjectOrientation

The ObjectOrientation expression outputs the world-space up vector of the object. In other words, this is the direction the local positive Z-axis of the object the material is applied to is pointing. For deferred decal, material domain returns decal projection direction (X-axis).

### UMaterialExpressionObjectPositionWS

The ObjectPositionWS expression outputs the world-space center position of the object's bounds. This is useful for creating spherical lighting for foliage, for example.

### UMaterialExpressionObjectRadius

The object radius outputs a value equal to the radius of a given object in Unreal units. Scaling is taken into account and the results can be unique for each individual object.

### UMaterialExpressionPanner

The Panner expression outputs UV texture coordinates that can be used to create panning, or moving, textures. 

Panner generates UVs that change according to the Time input. The Coordinate input can be used to manipulate (e.g. offset) the UVs generated by the Panner node.

### UMaterialExpressionParticlePositionWS

The ParticlePositionWS expression outputs 3vector (RGB) data representing each individual particle's position in world space.

### UMaterialExpressionPixelNormalWS

The PixelNormalWS expression outputs vector data representing the direction that pixels are facing based on the current normal.

### UMaterialExpressionRotator

The Rotator expression outputs UV texture coordinates in the form of a two-channel vector value that can be used to create rotating textures.

### UMaterialExpressionSceneTexelSize

The SceneTexelSize expression allows you to offset by texel sizes, as you would when using the SceneColor and SceneDepth expressions. This is useful for edge detection in multi-resolution systems, as without this calculation you would be forced to use a small static value, resulting in inconsistent results at lower resolutions.

### UMaterialExpressionScreenPosition

The ScreenPosition expression outputs the screen-space position of the pixel currently being rendered.

### UMaterialExpressionTextureCoordinate

The TextureCoordinate expression outputs UV texture coordinates in the form of a two-channel vector value allowing materials to use different UV channels, specify tiling, and otherwise operate on the UVs of a mesh.

### UMaterialExpressionVertexNormalWS

The VertexNormalWS expression outputs the world space vertex normal. It can only be used in material inputs that are executed in the vertex shader, like WorldPositionOffset. This is useful for making a mesh grow or shrink. Note that offsetting position along the normal will cause the geometry to split apart along UV seams.

### UMaterialExpressionViewProperty

The ViewProperty expression outputs a view dependant constant property. The view property to be accessed can be configured, and the type of the output depends on the configured accessed property.

### UMaterialExpressionViewSize

The ViewSize expression outputs a 2D vector giving the size of the current view in pixels. This is useful for causing various changes in your materials based on the current resolution of the screen.

### UMaterialExpressionWorldPosition

The WorldPosition expression outputs the position of the current pixel in world space. To visualize, simply plug the output into Emissive. 

Common uses are to find the radial distance from the camera to a pixel (as opposed to the orthogonal distance from PixelDepth). WorldPosition is also useful to use as a texture coordinate and have unrelated meshes using the texture coord match up when they are near each other. Here is a basic example of using WorldPosition.xy to planar map a texture.

### UMaterialExpressionCustom

The Custom expression allows you to write custom HLSL shader code operating on an arbitrary amount of inputs and outputting the result of the operation.

### UMaterialExpressionCustomTexture

The CustomTexture expression allows you to refer to a texture in the HLSL code inside a Custom expression, typically to sample it inside the HLSL using the tex2D or similar function.

### UMaterialExpressionDecalDerivative

The DecalDerivative is used to explicitly compute a decal's texture coordinate's derivative assuming there is no custom uv, to avoid the 2x2 pixel mipmap artefacts on the edges where the decal is project to, but still with support of anisotropic filtering.

### UMaterialExpressionDecalMipmapLevel

Deprecated. Use DecalDerivative instead.

### UMaterialExpressionDepthFade

The DepthFade expression is used to hide unsightly seams that take place when translucent objects intersect with opaque ones.

### UMaterialExpressionPixelDepth

The PixelDepth expression outputs the depth, or distance from the camera, of the pixel currently being rendered.

### UMaterialExpressionSceneDepth

The SceneDepth expression outputs the existing scene depth. This is similar to PixelDepth, except that PixelDepth can sample the depth only at the pixel currently being drawn, whereas SceneDepth can sample depth at any location. 

Note: Only Translucent Materials may utilize SceneDepth.

### UMaterialExpressionFontSample

The FontSample expression allows you to sample the texture pages out of a font resource as regular 2D textures. The alpha channel of the font will contain the font outline value. Only valid font pages are allowed to be specified.

### UMaterialExpressionFontSampleParameter

The FontSampleParameter expression provides a way to expose a font-based parameter in a material instance constant, making it easy to use different fonts in different instances. The alpha channel of the font will contain the font outline value. Only valid font pages are allowed to be specified.

### UMaterialExpressionMaterialFunctionCall

The MaterialFunctionCall expression allows you to use an external MaterialFunction from another material or function. The external function's input and output nodes become inputs and outputs of the function call node. If a MaterialFunction is selected in the Content Browser when placing one of these expressions, it will automatically be assigned.

### UMaterialExpressionStaticBool

The StaticBool expression is used to provide a default bool value for a static bool function input within a function. This node does not switch between anything, so it must be used in conjunction with a StaticSwitch node.

### UMaterialExpressionStaticSwitch

The StaticSwitch expression works like a StaticSwitchParameter, except that it only implements the switch and does not create a parameter.

### UMaterialExpressionTextureObject

The TextureObject expression is used to provide a default texture to sample from. In order to actually sample from the Texture Object, it must be used in conjunction with a TextureSample node.

### UMaterialExpressionLandscapeLayerBlend

The LandscapeLayerBlend node enables you to blend together multiple Landscape layers in a single node, as Textures or material network inputs. For more information, see Using LandscapeLayerBlend Nodes. 

You can set the properties of the LandscapeLayerBlend node in the Details panel. The properties for this node include an array for you to enter information about the layers to blend together.

### UMaterialExpressionLandscapeLayerCoords

The LandscapeLayerCoords node generates UV coordinates that can be used to map Material networks to Landscape terrains.

### UMaterialExpressionLandscapeLayerSwitch

The LandscapeLayerSwitch node allows you to exclude some Material operations when a particular layer is not contributing to a region of the Landscape. This allows you to optimize your Material by removing calculations that are not necessary when a particular layer's weight is zero.

### UMaterialExpressionLandscapeLayerWeight

The LandscapeLayerWeight expression allows Material networks to be blended based on the weight for the associated layer obtained from the Landscape the Material is applied to. For more information, see Using LandscapeLayerWeight Nodes.

### UMaterialExpressionLandscapeVisibilityMask

The LandscapeVisibilityMask node is used for removing the visibility of parts of your Landscape, so you can create holes, for example, for creating caves.

### UMaterialExpressionBreakMaterialAttributes

The Break Material Attributes expression is ideal when using a Layered Material - a feature of the Material Functions system. When using a Material Layer Function within a Material, you may want to use only one aspect of the layer. 

For example, you may have a Material Layer that defines a nice looking generic Material, such as steel. You may want to use only the Roughness and Base Color attributes from that layer in your final Material, rather than using the whole thing. 

In such cases, you can use a Break Material Attributes node to split up all of the incoming attributes of the Material Layer, and then just plug in the ones you want. This also allows for complex blending of various Material Attributes.

### UMaterialExpressionMakeMaterialAttributes

The Make Material Attributes node does exactly the opposite of the Break Material Attributes node. Instead of splitting attributes apart, this brings them together. This is useful when creating your own Material Layer functions, as you will have access to all of the standard attributes for your output. 

This can also be used for complex Material setups in which you want to define more than one type of Material and blend them together, all within one Material.

### UMaterialExpressionAbs

Abs is an abbreviation for the mathematical term "absolute value". The Abs expression outputs the absolute, or unsigned, value of the input it receives. Essentially, this means it turns negative numbers into positive numbers by dropping the minus sign, while positive numbers and zero remain unchanged.

### UMaterialExpressionAdd

The Add expression takes two inputs, adds them together and outputs the result. This addition operation is performed on a per channel basis, meaning that the inputs' R channels get added, G channels get added, B channels get added, etc. Both inputs must have the same number of channels unless one of them is a single Constant value. Constants can be added to a vector with any number of inputs.

### UMaterialExpressionAppendVector

The AppendVector expression allows you to combine channels together to create a vector with more channels than the original. For example, you can take two individual Constants values and append them to make a two-channel Constant2Vector value. This can be useful for reordering the channels within a single texture or for combining multiple grayscale textures into one RGB color texture.

### UMaterialExpressionCeil

The Ceil expression takes in value(s), rounds them up to the next integer, and outputs the result. See also Floor and Frac.

### UMaterialExpressionClamp

The Clamp expression takes in value(s) and constrains them to a specified range, defined by a minimum and maximum value. A minimum value of 0.0 and maximum value of 0.5 means that the resulting value(s) will never be less than 0.0 and never greater than 0.5.

### UMaterialExpressionComponentMask

The ComponentMask expression allows you to select a specific subset of channels (R, G, B, and/or A) from the input to pass through to the output. Attempting to pass a channel through that does not exist in the input will cause an error, unless the input is a single constant value. In that case, the single value is passed through to each channel. The current channels selected to be passed through are displayed in the title bar of the expression.

### UMaterialExpressionCosine

The Cosine expression outputs the cosine of the input, where an input value of 1 corresponds to 2*pi radians. (The input mapping is controlled by the Period value. For example, the Period should be set to 360 if the input is in degrees). Most commonly, Cosine is used to output a continuous oscillating waveform by connecting a Time expression to its input. The output value will cycle back and forth between -1 and 1.

### UMaterialExpressionCrossProduct

The CrossProduct expression computes the cross product of two three-channel vector value inputs and outputs the resulting three-channel vector value. Given two lines (or vectors) in space, the cross product is a line (or vector) which is perpendicular to both of the inputs.

### UMaterialExpressionDivide

The Divide expression takes two inputs and outputs the result of the first divided by the second. The division happens per channel, meaning that the R channel of the first is divided by the second, the G channel of the first is divided by the second, and so on. Both inputs must have the same number of values unless the divisor is a single float value.

### UMaterialExpressionDotProduct

The DotProduct expression computes the dot product, or the length of one vector projected onto the other. This calculation is used by many techniques for computing falloff. DotProduct requires both vector inputs to have the same number of channels.

### UMaterialExpressionFloor

The Floor expression takes in value(s), rounds them down to the previous integer, and outputs the result. See also Ceil and Frac.

### UMaterialExpressionFmod

The FMod expression returns the floating-point remainder of the division operation of the two inputs.

### UMaterialExpressionFrac

The Frac expression takes in value(s) and outputs the decimal part of those values. See also Ceil and Floor.

### UMaterialExpressionIf

The If expression compares two inputs and then passes through one of three other input values based on the result of the comparison. The two inputs to be compared must be single float values.

### UMaterialExpressionLinearInterpolate

The LinearInterpolate expression blends between two input value(s) based on a third input value used as a mask. This can be thought of as a mask to define transitions between two textures, like a layer mask in Photoshop. The intensity of the mask Alpha determines the ratio of color to take from the two input values. 

If Alpha is 0.0, the first input is used. If Alpha is 1.0, the second input is used. If Alpha is grey (somewhere between 0.0 and 1.0), the output is a blend between the two inputs. Keep in mind that the blend happens per channel.  So, if Alpha is an RGB color, Alpha's red channel value defines the blend between A and B's red channels independently of Alpha's green channel, which defines the blend between A and B's green channels.

### UMaterialExpressionMultiply

The Multiply expression takes two inputs, multiplies them together, and outputs the result. Similar to Photoshop's multiply layer blend. The multiplication happens per channel, meaning that the R channel of the first is multiplied by the second; the G channel of the first is multiplied by the second, and so on. Both inputs must have the same number of values unless one of the values is a single float value. 

Note: Do not forget that materials in UE are not limited to [0,1]! If colors/values are greater than 1, Multiply will actually brighten colors.

### UMaterialExpressionNormalize

The Normalize expression calculates and outputs the normalized value of its input. This means each component of the input is divided by the L-2 norm (length) of the vector. 

Note: It is not necessary to normalize an expression which plugs into the Normal material output.

### UMaterialExpressionOneMinus

The OneMinus expression takes an input value and outputs one minus that value. This operation is performed per channel.

### UMaterialExpressionPower

The Power expression takes two inputs, raises Base to the Exp power, and outputs the result; in other words, Base multiplied by itself Exp times.

### UMaterialExpressionLogarithm2

The Logarithm expression takes two inputs, compute X's logarithm base 2, and outputs the result; in other words, the number of time you should get 2 multiply itself to find X. The logarithm computation happens per channel. Both inputs must have the same number of values unless one of the values is a single float value.

### UMaterialExpressionSine

The Sine expression outputs the sine of the input, where an input value of 1 corresponds to 2*pi radians. (The input mapping is controlled by the Period value. For example, the Period should be set to 360 if the input is in degrees). Most commonly, Sine is used to output a continuous oscillating waveform by connecting a Time expression to its input. The output value will cycle back and forth between -1 and 1. The difference between this and the output of the Cosine expression is the output waveform is offset half the Period.

### UMaterialExpressionSquareRoot

The SquareRoot expression outputs the square root of the input value. SquareRoot can operate only on a single float input value.

### UMaterialExpressionSubtract

The Subtract node takes in two inputs, subtracts the second input from the first, and outputs the difference. The subtraction happens per channel, meaning that the R channel of the second input gets subtracted from the first; the G channel of the second input gets subtracted from the first, and so on. 

Both inputs must have the same number of channels unless the second input is a single Constant value. Constants can be subtracted from a vector with any number of inputs.

### UMaterialExpressionCollectionParameter

A Collection Parameter expression is used to reference a Parameter Collection asset. These are groups of parameters that can easily be reused by many different assets such as Materials, Blueprints, and much more. For more information on Parameter Collections, be sure to read the Parameter Collections Documentation.

Note: A Material can reference at most two different MaterialParameterCollections. One is typically used for game-wide values, and the other can be used for level specific parameters. A collection can have at most 1024 scalar parameters and 1024 vector parameters.

### UMaterialExpressionDynamicParameter

The DynamicParameter expression provides a conduit for particle emitters to pass up to four values to the material to be used in any manner. These values are set in Cascade via a ParameterDynamic module placed on an emitter.

### UMaterialExpressionScalarParameter

The ScalarParameter expression outputs a single float value (Constant) that can be accessed and changed in an instance of the material or on the fly by code.

### UMaterialExpressionStaticBoolParameter

The StaticBoolParameter works like StaticSwitchParameter, except that it only creates a bool parameter and does not implement the switch.

### UMaterialExpressionStaticSwitchParameter

The StaticSwitchParameter expression takes in two inputs, and outputs the first if the value of the parameter is true, and the second otherwise.

### UMaterialExpressionVectorParameter

The VectorParameter expression is identical to the Constant4Vector, except that it is a parameter and can be modified in instances of the material and through code. One nicety of the VectorParameter is that its value can be set using the Color picker.

### UMaterialExpressionTextureObjectParameter

The TextureObjectParameter expression defines a texture parameter and outputs the texture object, used in materials that call a function with texture inputs. This node does not actually sample the texture, so it must be used in conjunction with a TextureSample node.

### UMaterialExpressionTextureSampleParameter2D

The TextureSampleParameter2D expression is identical to the TextureSample except that it is a parameter that can be modified in instances of the material and through code.

### UMaterialExpressionTextureSampleParameterCube

The TextureSampleParameterCube expression is identical to the TextureSample except that it only accepts cubemaps and it is a parameter that can be modified in instances of the material and through code.

### UMaterialExpressionTextureSampleParameterSubUV

The TextureSampleParameterSubUV expression is identical to the ParticleSubUV except that it is a parameter that can be modified in instances of the material and through code.

### UMaterialExpressionParticleMacroUV

The ParticleMacroUV expression outputs UV texture coordinates that can be used to map any 2d texture onto the entire particle system in a continuous way, meaning the texture will be seamless across particles. 

The UVs will be centered around MacroUVPosition (specified in Cascade on the ParticleSystem, under the MacroUV category) and MacroUVRadius determines the world space radius that the UVs should tile at.

The ParticleMacroUV node is useful for mapping continuous noise onto particles to break up the pattern introduced by mapping a texture onto each particle with normal texture coordinates.

### UMaterialExpressionParticleSubUV

The ParticleSubUV expression is used to render sub-images of a texture to a particle. ParticleSubUV is similar to a flipbook, except that ParticleSubUV allows the texture animation to be manipulated in Cascade.

### UMaterialExpressionSphericalParticleOpacity

The SphericalParticleOpacity expression creates a procedural opacity map to cause sprite particles to appear spherical. This can be much simpler than having to create an import a texture map for a similar effect.

### UMaterialExpressionSceneColor

The SceneColor expression outputs the existing scene color.

### UMaterialExpressionTextureSample

The TextureSample expression outputs the color value(s) from a texture. This texture can be a regular Texture2D (including normal maps), a cubemap, or a movie texture.

### UMaterialExpressionTextureProperty

The TextureProperty expression exposes a texture's properties such as the texture's size or the texel size.

### UMaterialExpressionBlackBody

The Black Body expression simulates the effects of black body radiation within your Material. The user inputs a temperature (in Kelvin) and the resulting color and intensity can be used to drive Base Color and Emissive values to get a physically accurate result.

### UMaterialExpressionBumpOffset

BumpOffset is the Unreal Engine term for what is commonly known as 'parallax mapping'. The BumpOffset expression allows a material to give the illusion of depth without the need for additional geometry.

 BumpOffset materials use a grayscale heightmap to give depth information. The brighter the value in the heightmap, the more 'popped out' the material will be; these areas will parallax (shift) as a camera moves across the surface. Darker areas in the heightmap are 'further away' and will shift the least.

### UMaterialExpressionConstantBiasScale

The ConstantBiasScale expression takes an input value, adds a bias value to it, and then multiplies it by a scaling factor outputting the result. So for example, to convert input data from [-1,1] to [0,1] you would use a bias of 1.0 and a scale of 0.5.

### UMaterialExpressionDDX

The DDX expression exposes DDX derivative calculation, a GPU hardware feature used in pixel shader calculation.

### UMaterialExpressionDDY

The DDY expression exposes DDX derivative calculation, a GPU hardware feature used in pixel shader calculation.

### UMaterialExpressionDepthOfFieldFunction

The Depth of Field Function expression is designed to give artists control over what happens to a Material when it is being blurred by Depth of Field. It outputs a value between 0-1 such that 0 represents "in focus" and 1 represents "completely blurred."

This is useful for interpolating between sharp and blurry versions of a texture, for instance. The Depth input allows for the existing results from the scene's Depth of Field calculations to be overridden by other calculations.

### UMaterialExpressionDistance

The Distance expression computes the (Euclidian) distance between two points/colors/positions/vectors and outputs the resulting value. This works on one, two, three, and four component vectors, but both inputs to the expression must have the same number of channels.

### UMaterialExpressionFresnel

The Fresnel expression calculates a falloff based on the dot product of the surface normal and the direction to the camera. When the surface normal points directly at the camera, a value of 0 is output. 

When the surface normal is perpendicular to the camera, a value of 1 is output. The result is clamped to [0,1] so you do not have any negative color in the center.

### UMaterialExpressionLightmassReplace

The LightmassReplace expression simply passes through the Realtime input when compiling the material for normal rendering purposes, and passes through the Lightmass input when exporting the material to Lightmass for global illumination.

This is useful to workaround material expressions that the exported version cannot handle correctly, for example WorldPosition.

### UMaterialExpressionNoise

The Noise expression creates a procedural noise field, giving you control over how it is generated.

### UMaterialExpressionQualitySwitch

The QualitySwitch expression allows for the use of different expression networks based on the engine is switched between quality levels, such as using lower quality on lower-end devices.

### UMaterialExpressionRotateAboutAxis

The RotateAboutAxis expression rotates a three-channel vector input given the rotation axis, a point on the axis, and the angle to rotate. It is useful for animations using WorldPositionOffset that have better quality than simple shears. 

Note: An Absolute World Position node is automatically created when a RotateAboutAxis node is added.

### UMaterialExpressionAntialiasedTextureMask

The AntialiasedTextureMask expression allows you to create a material using a soft (anti-aliased) transition mask. The mask can be used to blend between two complex material properties or to fade out an alpha blended material (works well with SoftMasked). 

Simply specify a texture with the mask specified in one channel (red, green, blue, or alpha), set the used channel in the expression and specify the comparison value.

Assuming the channel stores a grayscale value in the range 0=black to 1=white the comparison function defines if the resulting mask should be 0 or 1. This expression is a parameter, allowing the Texture property to be overridden by child MaterialInstances.

### UMaterialExpressionDeriveNormalZ

The DeriveNormalZ expression derives the Z component of a tangent space normal given the X and Y components and outputs the resulting three-channel tangent space normal. Z is calculated as Z = sqrt(1 - (x x + y y));

### UMaterialExpressionTransform

The Transform expression converts a three-channel vector value from one reference coordinate system to another. 

By default, all shader calculations in a material are done in tangent space. The vector constants, camera vector, light vector, etc are all transformed to tangent space before being used in a material.

The Transform expression allows these vectors to be transformed from tangent space to world-space, local-space, or view-space coordinate systems. In addition, it allows world-space and local-space vectors to be transformed to any of the other reference coordinate systems.

### UMaterialExpressionTransformPosition

The TransformPosition expression can transform any position from screen space to the destination space specified by the expression's TransformType variable. Currently only transforming into world space is supported.

This expression can be used to get world space coordinates in the material. To visualize world position, you can plug it straight into emissive.

### UMaterialExpressionCameraVectorWS

The CameraVector expression outputs a three-channel vector value representing the direction of the camera with respect to the surface, in other words, the direction from the pixel to the camera. 

Example Usage: CameraVector is often used to fake environment maps by connecting the CameraVector to a ComponentMask and use the x and y channels of the CameraVector as texture coordinates.

### UMaterialExpressionLightVector

This expression is deprecated as lighting calculations are now deferred.

### UMaterialExpressionObjectBounds

The Object Bounds expression outputs the size of the object in each axis. If used as color, the X, Y, and Z axes correspond to R, G, and B, respectively.

### UMaterialExpressionReflectionVectorWS

The ReflectionVectorWS expression is similar in spirit to CameraVectorWS, but it outputs a three-channel vector value representing the camera direction reflected across the surface normal. 

Example Usage: ReflectionVector is commonly used in environment maps, where the x/y components of the reflection vector are used as UVs into a cubemap texture.

### UMaterialExpressionStaticComponentMaskParameter

The StaticComponentMaskParameter expression behaves just like an ordinary Component Mask, except that the mask values can be set by instances.

### UMaterialExpressionSpeedTree

The SpeedTree node allows you to access and gain SpeedTree wind and smooth LOD transitions. Geometry Type, Wind Type, LOD Type and Billboard Threshold can be set via the Details panel.

### UMaterialExpressionSceneTexture

Using the SceneTexture material expression, you can choose a texture you want to reference in the expression's properties, then using the input and output nodes, you can compute the depth difference of the current pixel to a neighbor pixel (e.g. In = 0,1 to return the delta to the pixel below).

### UMaterialExpressionFeatureLevelSwitch

The Feature Level Switch node allows you to make simplified materials for lower powered devices. 

Example Usage: You might have a material with 10 textures overlapping and complex math, but just a single static texture for mobile (feature level ES2).

### UMaterialExpressionGIReplace

GIReplace allows artists to specify a different, usually simpler, expression chain when the material is being used for GI.  

Example Usage: Lightmass static GI and LPV dynamic GI use it.

### UMaterialExpressionSpriteTextureSampler

A custom sprite material can be created by duplicating one of the existing ones, or creating a new material in the Content Browser. When a sprite is rendered, the texture defined in a sprite asset will be piped into any texture parameters named "SpriteTexture" in the material. The SpriteTextureSampler node can be placed to do this automatically.

### UMaterialExpressionMax

The Max expression takes in two inputs then takes the maximum of the two. 

This node is similar to Photoshop's Lighten.

### UMaterialExpressionMin

The Min expression takes in two inputs then takes the minimum of the two. 

This node is similar to Photoshop's Darken.