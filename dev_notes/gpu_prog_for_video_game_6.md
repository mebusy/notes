# GPU Programming for Video Games, Summer 2020, Georgia Tech

- book
    - 3D Game Engine Design --  A practical approach to real-time computer graphics

- Notes
    - Texture Coordinates Conventions
        - OpenGL/Unity: (0,0) = lower left corner



# 6 Backface Culling

- Determin "facing direction"
- Triangle order matters
- How to compute a normal vector for 2 given vectors ?
    - Using **cross product** , depends on LHS/RHS you are actually using.
    - so if you load in the 3d model, and you have back face culling activated in your game engine, and the object disappears, then that probably is a suggestion that there's a different convention (LHS/RHS) being used by the model than what the softward rendering it is expecting it to be.
    - again, the face normal is not the normals exported by the 3d modeling software.


## Backface culling method

- Check if the normal is facing the camera
- How the determine that ?
    - use **Dot Product**: `n̂·ê`


## When to perform backface culling ?

1. world transform
2. view transform
3. vertex lighting
4. projection transform
5. clipping 
6. perspective divide
7. viewport transform
8. Rasterization

- can perform in different places
    - after step 2 ( common )
    - after step 1
    - even before step 1.
- mostly nowadays, this kind of optimization is actually done further down in the chain. 
    - after step 6, check "winding order" in 2D
        - this comes from the fact that GPUs are so powerful nowadays, you're usually better off just sending a bunch of stuff to the card, and letting the card go ahead , do these computations (step 1-6) on the vertex side, and then make decision about whether to call a triangle before you that final pixel shader stage.
    - after viewport transform, as "officially" done by OpenGL


# 7 Basic Lighting

## Local vs. global illumination

- Local illumination
    - Direct illumination: light shine on all objects without blocking or reflection
    - used in most games
    - can ncorporate shadows with a lot of work

- Global illumination
    - Indirect illumination: light bounces from one object to other objects
    - Adds more realism
    - Computationally much more expensive
    - Ray tracing, radiosity
    - We'll look at ways of approximating this effect


## Elements of PBR(physically-based rendering)

- Linear space lighting
- Energy conservation
- Reciprocity
- Metallic/dielectric distinction
    - dielectric means "not metal" in this class
- "Everything is shiny" (i.e., has specular)
- "Everything has Fresnel"
    - wet pavement with sun near horizon
- Bonus: high definition render buffers and tonemapping to handle high dynamic range.


## Illumination: diffuse lighting

- Light sources are given
- Assume light bounces in all directions
    - **reflected light will reach the camera no matter where the camera is!**
- Light intensity calculation
    - Reflectivity ∝ the entry angle
    - use **Lambert's consine Law**
- **C<sub>dif</sub> = C<sub>light</sub> ⊗ M<sub>dif</sub> * max( 0, n̂·l̂ )**
    - diffuse intensity is proportional to cos(θ), where θ is the angle between the normal vector and light source vector.
    - when normal vector and light source vector are both unit vectors, `cos(θ) = n̂·l̂`.
    - use `max` function to avoid the negative value of dot product
    - C<sub>light</sub>  is the RGB color of the light
    - M<sub>dif</sub> is an RGB color of this diffuse reflection, basically the material color
    - the circled time ⊗ is a `colorwise product`.
        - red times red, green times green, blue times blue.

## Illumination: specular lighting

- Create shinning surface ( surface perfectly reflects )
- Viewpoint dependent
- Blinn-Phong model
    - but it is not a physically plausible model
- A physically-based model : Bidirectional Reflectance Functions
    - For "punctal" light ( typical point, directional, spotlight... )
    - **C<sub>final</sub> = C<sub>light</sub> ⊗ π*BRDF( l̂ , ê ) * max(0, n̂·l̂ )**
        - BRDF: Bidirectional Reflectance Function
        - ê : the vector torwards the eye ball
    - classic diffuse lighting model:
        - BRDF = M<sub>dif</sub> / π
    - what is the π ?

## BRDF 

- BRDFs should have reciprocity
    - Reciprocity means we can swap the incoming and outgoing light directions:
    - BRDF( l̂ , ê ) = BRDF( ê , l̂ )
- Energy conservation
    - "Total amount of reflected light cannot be more thant the amount of incoming light" -- Rory Driscoll
    - For classic diffuse model BRDF = M<sub>dif</sub> / π , turns out you *technically* need `πM<sub>dif</sub> < 1`
    - Since π is just a constant, "we usually just ignore it and assume that our lights are just π times too bright. " -- Steve McAuley.
- A common yet confusing convention
    - For classic diffuse model BRDF = M<sub>dif</sub> / π
        - we'll pretend you *practically* need `M<sub>dif</sub> < 1`
    - Convenient for artists: 
        - hit a diffuse surface with a material color of "1" with a directinal light with an "intensity" of "1" parallel with its normal and you get "1".
    - We will generally use the same convention.
    - If you are implementing global illumination, be careful !





## Light source properties

- Postion ( point of spot ) , or angle ( directinal )
- Range
    - Specifying the visibility
- Attenuation
    - The farther the light source, the dimmer the color
    - Writing it as a multiplier
        - `Atten = 1/( a₀ + a₁d + a₂d² )`

## Spot light effect 

[cg tutorial: 5.5.2 Adding a Spotlight Effect](https://developer.download.nvidia.com/CgTutorial/cg_tutorial_chapter05.html)


# 8 Rasterization

## Shading methods

- flat shading
- Gouraud shading
    - supported by (even old) 3D graphics hardward
- Phong shading
    - requires generating per-pixel normals to computer light intensity for each pixel , which is computationally expensive...
    - Can be done on modern GPUs

## Z-Buffer

- so in additon to painting light information to a buffer sitting there somewhere in your video memory, we also going to be filling out something called z-buffer.
    - this is another image you're writing, but instead of containing color information, it contains depth information.
- also called *depth buffer*
- Draw the pixel which is nearest to the viewer
- Number of the entries corresponding to the screen resolution ( e.g. 1024x768 sould have a 768k-entry Z-buufer )
- Granularity matters
    - 8-bit nerver used
    - 16-bit z value could generate artifacts


# 9 Introduction to Textures

## Texture

- Rendering tiny triangles is slow
- Players won't even look at some certain details
    - sky, clouds, walls, terrain, wood patterns, etc.
- Simple way to add details and enhance realism.
- Use 2D images to map polygons.
- Images are composed of 2D "texels"
    - texels are like the pixels of a 2D image that's going to be stretched around and placed on the object.


## Texture Coordinates

- Introduce one more component to geometry
    - position coordinates
    - normal vector ( used in lighting calculation)
    - color ( may not need now )
    - **Texture coordinates** (2D)

## Texture Coordinates Conventions

- Direct3D / XNA texture convention
    - (u,v) coordinates for each vertex
    - (0,0) = upper left corner
    - (1,1) = lower right corner
- OpenGL/Unity texture convention
    - (s,t)/(u,v) coordinates for each vertex
    - (0,0) = lower left corner
    - (1,1) = upper right corder


## Mip-mapping

- Multiple versions are provided for the same texture
- Different versions have different levels of details
    - e.g. 7 LOD maps: 256x256, 128x128, 64x64, 32x32, 16x16, 8x8, 4x4
    - Choose the closest maps to render a surface
- Maps can be automatically generated by 3D API
- API or hardware can 
    - choose the right one for the viewer
        - good performance for far triangles
        - good LOD for close-by objects
    - Trilinearly interpolate


# 10 Advanced Texture Techniques

## Normal mapping

- **Per-fragment lighting** using bump map (normal map) to perturb surface normal
- No geometry tessellation, avoid geometric complexity
- Store normal vectors rather than RGB color for bump map
- Apply per-pixel shading (w/light vector, e.g. Phong shading)
- ![](../imgs/gpu_bump_mapped_sphere.png)
- ![](../imgs/gpu_bump_mapped_sphere2.png)

---

- Normal map was derived from a height field map
    - Height field stores the "elevation" for each texel.
    - Sample texel's height as well as texels to the right and above.
    - ![](../imgs/gpu_height_field.png)
        - right side: height map, maybe something that grayscale indicates the height , created by something like photoshop.
        - left side: 2D conceptual exsample, where the grascale values in this texture indicate height variations. And then you can run a piece of software that would use that information ,  the normal vector along the height field surface.
        - ![](../imgs/gpu_range_compressed_normal.png)
        - Game engines like Unity3D provide the ability to create normal map from height map.
    - [normal map example on web](http://cpetry.github.io/NormalMap-Online/)
        - ![](../imgs/gpu_normal_map_example.png)
        - why does the normal map has such weird particular color pattern ?
            - see next paragraph

 
## Creating normal map from height field

- To compute the normal vector, you basically want to take the partial derivatives of the height field along the various directions.
- Height Field H(u,v)
    - ![](../imgs/gpu_create_normal_map_from_height_map.png)
    - here we are essentially doing the calculus type trick of using a first difference , and the horizontal and the vertical direction , in order to compute the approximation to those partial derivatives.
    - and to normalize it to unit length.
- In flat regions , normal is (0,0,1), i.e. pointing "up".
- And this is why you typically see big blue sections in normal map, because the Blue component always be 1 before normalization
    - and you see RED along x axis, because that represents the changes in horizontal direction
    - and you see GREEN along y axis, beause that represents the variations in vertical direction
- From "The Cg Tutorial", p.203


## Storing normals in textures

- Textures don't have to store color; we can store another things as well, like normals
    - Use r,g,b components to store x,y,z of normal
- Problem: Texture take [0,1] values; normals need [-1,1] values
- Easy solution: "Range Compression"
    ```c
    colorComponnet = 0.5 * normalComponnet + 0.5;
    normalcomponent = 2 * ( colorComponent - 0.5);
    ```

## Environment mapping

- ![](../imgs/gpu_cube_map.png)
- Here is another technique where the texture values here are indeed RGB colors, but, this is very different kind of texture.
    - called Cube Map Texutre ( in world coordinate )
    - Each face encodes 1/6 of the panoramic environment 
- You can imagine going to the world, and taking the camera, and pointing up,down,left, right, forward, back, and each time you do that, you take a picture.
    - and then you load them into photoshop, and find the edge to line them up.
    - and what you built is basically a description of the overall light environment of the scene.
    - this is something called *image-based lighting*. this gives us the ability to make some really cool looking kind of reflection

- You can create cube map by yourown, and the game engine like Unity3D can create cube map for you,  using "reflection probes"

---

- ![](../imgs/gpu_env_mapping_teapot.png) ,  ![](../imgs/gpu_env_mapping_teapot2.png)
    - The teapot here is reacting to light an specular fashion. 
    - Look up the environment map
        - shader language also have a particular function `texCUBE()` for sampling the texel in cube map.
    - Add reflection to a fragment's final color
    - r̂ = 2 * (n̂·l̂)*n̂ - l̂
- Rendered Image:
    - ![](../imgs/gpu_cube_map_rendered_image.png)

## Alpha test

- Reject pixels by checking their alpha values
- Model fences, chicken wires, etc.

```c
if ( α op val )
    reject pixel
else
    accept pixel
```

## Multi-texturing example: light mapping

- ![](../imgs/gpu_multi_tex_lighting.png)
- used for old games
- it is reasonable for diffuse, not specualr , and can not handle moving light


# 11 Color Spaces


