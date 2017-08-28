
# Unity Shaders and Effects Cookbook

# 1 Diffuse Shading

## Creating a basic Surface Shader

 - Getting Ready ...
     - create a `Materials` folder
     - create a shader, create a material
     - edit material, choose the shader you created
     - apply material to an object

 - The Surface Shader language is a more component-based way of writing Shaders. 
    - Tasks such as processing your own texture coordinates and transformation matrices have already been done for you
 - See also 
    - For more information on where to  nd a large portion of the built-in Cg functions for Unity
    - go to your Unity install directory and navigate to 
        - `CGIncludes\UnityCG.cginc`
        - `CGIncludes\Lighting.cginc`
        - `CGIncludes\UnityShaderVariables.cginc`

## Adding properties to a Surface Shader

```
Properties {
    _Color ("Color", Color) = (1,1,1,1)
}
```

 - from left to right, they are 
    - variable name
    - inspector GUI name
    - type 
    - Default value

---

Surface Shader property types | ·
 --- | ---
Range (min, max) | float property as a slider
Color | a color picker = (float,float,float,float)
2D  |   a texture
Rect |  a non-power-of-2 texture , functions the same as the 2D GUI element
Cube  |  a cube map 
Float |  a float value
Vector |  four-float property

 - See also
    - https://docs.unity3d.com/Manual/SL-Properties.html

---

Property attributes

attributes | /
 --- | ---
[HideInInspector] | does not show the property value in the material inspector.
[NoScaleOffset] | material inspector will not show texture tiling/offset fields for texture properties with this attribute.
[Normal] | indicates that a texture property expects a normal-map.
[HDR] | indicates that a texture property expects a high-dynamic range (HDR) texture.
[Gamma] | indicates that a float/vector property is specified as sRGB value in the UI (just like colors are), and possibly needs conversion according to color space used. See Properties in Shader Programs.
[PerRendererData] | indicates that a texture property will be coming from per-renderer data in the form of a MaterialPropertyBlock. Material inspector changes the texture slot UI for these properties.




## Using properties in a Surface Shader

 1. add a property
    - `_AmbientColor ("Ambient Color", Range(0,10)) = 2`
 2. declare the properties variable type inside of the CGPROGRAM, so we can access its value from the properties block
    - in SubShader{} block , define subshader variables
    - `float4 _AmbientColor;`
 3. using it the `surf()` function
    - `float4 c =  pow((_EmissiveColor + _AmbientColor), _MySliderValue);`

## Creating a custom diffuse lighting model

 1. modify the #pragma statement to
    - `#pragma surface surf BasicDiffuse`  光照模型改成自定义的 `BasicDiffuse`
 2. Add the following code to the subshader:
 3. Save the Shader and return to Unity.
    - you will see that no real visible change has happened to our Material
    - What we have done is removed the connection to the built-in Unity diffuse lighting and created our own lighting model that we can customize.

```
inline float4 LightingBasicDiffuse (SurfaceOutput s, fixed3
        lightDir, fixed atten)
{
    float difLight = max(0, dot (s.Normal, lightDir));  // saturate()
    float4 col;
    col.rgb = s.Albedo * _LightColor0.rgb * (difLight * atten * 2);
    col.a = s.Alpha;
    return col;
}
```

How it works ?

 - The #pragma surface directive tells the Shader which lighting model to use for its calculation
    - when we first create the Shader, the light modle which use is defined in `Lighting.cginc` file
    - We have now told the Shader to look for a lighting model by the name **BasicDiffuse**
 - Creating a new lighting model is done by declaring a new lighting model function. There are 3 types of lighting model functions that you can use:   
    - `half4 Lighting<Your Chosen Name> (SurfaceOutput s, half3 lightDir, half atten){}`
        - This function is used for forward rendering when the view direction is not needed.
    - `half4 Lighting<Your Chosen Name> (SurfaceOutput s, half3 lightDir, half3 viewDir, half atten){}`
        - This function is used in forward rendering when a view direction is needed
    - `half4 Lighting<Your Chosen Name>_PrePass (SurfaceOutput s, half4 light){}`
        - This function is used when you are using deferred rendering for your project
 - To complete the diffuse calculation, we need to multiply `difLight` with 
    - the s.Albedo value (which comes from our surf function) 
    - with the incoming `_LightColor0.rgb` value (which Unity provides)
    - and then multiply the result of that with (difLight * atten) 
 - finally, return that value as the color. See the following code:


[rending path 介绍](https://github.com/mebusy/notes/blob/master/dev_notes/renderingPath.md)


## Creating a Half Lambert lighting model

 - Half Lambert was a technique created by Valve as a way of getting the lighting to show the surface of an object in low-light areas
 - It basically brightens up the diffuse lighting of the Material and wraps the diffuse light around an object's surface
 - It is designed to prevent the rear of an object losing its shape and looking too flat. 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_half_lambert_01.png)

> Alyx model showing Lambertian lighting (left) and Half Lambert lighting (right)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_half_lambert_02.png)

> The Lambertian dot product lobe (red) vs. the Half Lambertian dot product lobe (blue)

 - Using the basic Shader that we created in the last recipe, let's update the diffuse calculation:

```
    float difLight = max(0, dot (s.Normal, lightDir));  // saturate()
    float HLAMBERT = difLight*0.5 + 0.5 ;

    float4 col;
    col.rgb = s.Albedo * _LightColor0.rgb * ( HLAMBERT * atten * 2);
    col.a = s.Alpha;
    return col;
```

 - 原来的 0-1 的值，现在变成了 0.5-1, 整体增强了。


## Creating a ramp texture to control diffuse shading

 - Another great tool in your Shader writing toolbox is the use of a ramp texture to drive the color of the diffuse lighting.
 - This allows you to accentuate the surface's colors to fake the effects of more bounce light or a more advanced lighting setup. 
 - You see this technique used a lot more for cartoony games
    - where you need a more artist-driven look to your Shaders and not so much of a physically-accurate lighting model.
 
 ![](http://www.68idc.cn/help/uploads/allimg/150307/1504334Q2_0.jpg)

 - To get this started you will need to create a ramp texture
    - any image editing application should be able to make a gradient
    - 


