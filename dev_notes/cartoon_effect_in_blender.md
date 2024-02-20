
# cartoon effect in blender


1. add a monkey
2. ctrl+3 to add a subdivision modifier, apply it
3. right click on money,  click `Shader smooth`
4. switch 'Veiwport shading' (right top) to the 3rd one (Material Preview)
5. create 2 material,
    - the 1st one is in white color (default, change nothing)
    - the 2nd one,  change its 'Surface' from `Principled BSDF` to `Emission`, and set color to black, and activate `Settings/Backface Culling`
6. add a `Solidify` modifier.
    - set `Thickness` to `-0.01m`
    - activate `Normals/Flip`
    - set `Materials/Material Offset` to `1` (the 2nd material)

now the monkey has a black outline.

