
# 27: Projective Textures

## What is projective texturing ?

- An intuition for projective texturing
    - The slide projector analogy
    - ![](../imgs/gpu_projective_tex_ex_1.png)
    - project onto various objects in the scene

- Another exmaple:  different locations
    - ![](../imgs/gpu_projective_tex_ex_2.png)


## Texture matrix

from "The Cg Tutorial", p.252

- ![](../imgs/gpu_projective_tex_matrix_1.png)
- The way we formulate this is basically to setup the same set of matrix transformation we would, when taking 3D object in the scene and projecting them onto a camera plane, except here we're using the light position and orientation as if the light itself is the camera.
- so we still have the same  modeling matrix which translates model coordiantes into world space.
- and then transform into a view space, but this view space is from the point of the projecting light, not the camera.
- similarly we will go through a projection matrix, again, from the point of view of the light, not the camera.
- the last matrix is used to shift  everything from [-1,1] to [0,1] because that's what texture lookups expect.



