
# GPU Programming for Video Games

https://www.youtube.com/watch?v=i5yK56XFbrU&list=PLOunECWxELQQwayE8e3WjKPJsTGKknJ8w

# 1. Introduction

- CS4455: Video Game Design
- CS4731: Game AI
- CS4496/7496: Computer Animation
- CS4480: Digital Video Special Effects

# 2. 3D Coordinate Systems

- The model for creating computer graphics in this class is generally called rasterization model.
    - this is in contrast to something like ray tracing.


Stage | Geometry Pipline |  Rasterization Pipeline
 --- | --- | --- 
Processing what | Vertices | Pixels
Mainly operations |  **floating-point** operations |   **integer** operations
Shader | vertex shader(3d vertex) | fragment shader(final color of pixel)

- Something about the vertex shader is that they process each vertex individually and they don't create new vertices. 
- There are other kinds of shader called geometry shaders that can create new vertices
    - and there's also computer shaders that are much more general kinds of things that might be thought of as more general-purpose GPU programming.
- We'll be focusing on vertex shader and fragment shader.

## 3D Coord

- Math textbooks use z-up
    - ![](../imgs/gpu_zup_righthand.png)
    - Z-up, Right-Handed System
- Real games tend to use y-up
    - if we enter the realm of computer graphics
    - ![](../imgs/gpu_y_up_righthand.png)
    - Right-Handed System, +z toward the viewer
    - OpenGL, XNA
- There are also tools that use left-handed coordinate system ( Y-up )
    - ![](../imgs/gpu_yup_lefthand.png)
    - Left-Handed System, +z away from the viewer
    - Direct3D, Unity3D
- I shoud note that in traditional 2D games , Y values go downward.
- There are some tools out there that use a **Z-up** approach which is closer to math books
    - Z-up, Left-Handed System: Unreal
        - ![](../imgs/gpu_zup_lefthand.png)
    - Z-up, RHS: Quake/Radiant, Source/Hammer, C4 Engine
        - ![](../imgs/gpu_zup_righthand.png)
    - Nearly everything still use Y-up for screen coordinates
        - even though these kinds of tools use Z-up when it concerns 3D coordinates, when do their final projection onto the 2D screen, they go ahead and use Y for the vertical coordinates.
    - if you take the left-handed system here, and rotate 90 degrees (along z axis), you can redraw it, and this is probably what you would see when you pull up the Unreal editor.
        - ![](../imgs/gpu_zup_lefthanded_rotate.png)
        - Unreal, Z-up, Left-Handed (rotate)

- 3D object modeling software
    - ![](../imgs/gpu_zup_righthand.png)
        - Z-up, Right-Handed System
        - 3D Studio Max, Blender
    - ![](../imgs/gpu_y_up_righthand.png)
        - Y-up, Right-Handed System
        - Maya, Milkshape

---

Summary | Left-Handed | Right-Handed
--- | --- | ---
Z-up | Unreal  |  Math textbook, Quake/Radiant, Source/Hammer, C4 Engine, 3D Studio Max, Blender
Y-up | Direct3D, Unity3D  |  OpenGL, XNA, Maya, Milkshape


## Geometry format -- vertex coordinates

- At least at present , the models used in 3D games are formed from triangels.
    - each vertex of the triangle also has an associated unit normal, and this arises from the export process that your 3D artist will make from their 3D modeling software.

## Geometry format -- vertex color

- Some 3D models may also have color information associated with the different vertices. 
- But nowadays vertex colors are not actually used very much.
    - because usually that color information is embedded in some sort of 2D texture.
- Sometimes you will see this color slot being used, but it may be used form some other kind of information used in the rendering process and not typical color information.


## Specifying a 3D object 

![](../imgs/gpu_specify_obj.png)

- Vertex ordering is critical when culling model enabled
    - we essentially only want to render the triangles that are faced towards the viewer.
    - when approached this is to use the normal vector for the facet. 
        - **PS. these normals for culling are different than the vertex normals used for lighting.**
        - different vertices have different normals, but only 1 normal for a triangle.
    - The way we embed that kind of information is by choosing some sort of order to list the vertices.         - in either a left handed system, which in this case, { v1,v3,v2 }
- Question:
    - Are you using a LH or RH curlling convention for these normal vectors ? 
    - That could be completely independent about rather your actual 3D coordinate system in your engine is LH or RH.


## Transformation Pipeline

- Model(World) Transformation
    - Model coordinates -> World coordinates
    - Model coordinates is what your artist works with. That's the coordinate system they're working within blender, maya, etc... 
    - We need to transform those coordinates into the world coordinate space and that's basically the view space of the level editor.
- View Transformation
    - World coordinates -> Camera space
- Projection Transformation
    - Camera space -> View plane


# 3D Vertex Transformations


