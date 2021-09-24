# GPU Programming for Video Games, Summer 2020, Georgia Tech

- book
    - 3D Game Engine Design --  A practical approach to real-time computer graphics


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
    - M<sub>dif</sub> is an RGB color of this diffuse reflection
    - the circled time ⊗ is a `colorwise product`.
        - red times red, green times green, blue times blue.

## Illumination: specular lighting





