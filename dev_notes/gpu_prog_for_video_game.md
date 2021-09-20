
# GPU Programming for Video Games

https://www.youtube.com/watch?v=i5yK56XFbrU&list=PLOunECWxELQQwayE8e3WjKPJsTGKknJ8w


# Notes

- Unreal(z-up), Unity3D(y-up) use LHS
- moving camera is equivalent to inverse moving the entire world
- rotation  must take the coordinate system into consideration.
    - LHS , clockwise if looking against axis
    - RHS , counter clockwise if looking against axis

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
    - Are you using a LH or RH culling convention for these normal vectors ? 
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

- Model(World) Transformation
    - ![](../imgs/gpu_model_transform1.png)
- View Transformation
    - ![](../imgs/gpu_view_transform1.png)
    - there are various ways to define a view transformation. but a nice conceptual way is to just imagine that the camera itself is another object in the scene like the box and teapot.
        - and if you create the equivalent world transformation matrix that would take a camera, place it at the correct orientation at a certain point in the scene, 
        - you can then imagine making the view matrix the inverse of that transformation, the inverse of that matrix.
        - and if you apply that to all the objects in the scene, it will orbit them around, and rearrange them.
- Projection Transformation
    - Set up camera internals
        - view frustum
        - view planes
    - Field of View(FoV)
    - There is a rich set of mathematical techniques concerning a concept called 

## homogeneous coordinates

- Enable all transformations to be done by "multiplication".
    - primarily for translation
    - so we can deal with a series of transformations by pre-multiplying those matrices together before applying them to 10000 vertices.
- Add 4th coordinate (w) to a 3D vecto.
    - translation itself can't be accommodated by multiplying a 3x3 matrix.
- Each vertex has [x,y,z,w]
    - w will be useful for perspective projection
        - where we need to divide by distance, and there is a convention for handling that by sticking the distance into the `w`.
    - w should be 1 in Cartesian coordinate system

## Transformation 1:  translation( offset )

- Example of a **row**-coordinate converion here
    - ![](../imgs/gpu_translation1.png)
    - (**row**-coordinate)
    - ![](../imgs/gpu_translation2.png) 
    - Direct3D, XNA use row coordinates
        - also most documentation for HLSL/Cg uses this row vector convention
        - but HLSL itself doesn't really know what convention you're using, it just has these 4D vectors.
    - OpenGL, Unity & non-graphics world use column coordinates
- Example of **column**-coordinate
    ```ocatve
    ⎡Xt⎤   ⎡ 1   0   0  Tx⎤  ⎡X⎤
    ⎢Yt⎥ = ⎢ 0   1   0  Ty⎥· ⎢Y⎥
    ⎢Zt⎥   ⎢ 0   0   1  Tz⎥  ⎢Z⎥
    ⎣1 ⎦   ⎣ 0   0   0  1 ⎦  ⎣1⎦
    ```

## Transformation 2:  scaling

- ![](../imgs/gpu_scaling1.png)
- **row**-coordinate
    ```ocatve
    [Xs,Ys,Zs,1] = 

                ⎡ Sx  0   0  0 ⎤  
     [X,Y,Z,1]· ⎢ 0   Sy  0  0 ⎥  
                ⎢ 0   0   Sz 0 ⎥  
                ⎣ 0   0   0  1 ⎦  
    ```


## Transformation 3:  rotation

- Rotation is a lot trickier.
    - there is lots of different ways to represent rotations. 
    - some game engine like unity actually use a fairly sophisticated mathematical structure called `quaternions`, which are a 4D extension of the complex number to represent rotations.
    - dealing with quaternions gives a natural way of interpolating camera angles and also dealing with an issue called `gimbal lock`.
    - people design control systems for aircraft, we'll talk about pitch, roll, yaw.
    - unity and many other game engines think about a rotation around x-axis , and then rotation around y-axis, and then z-axis. The order you do these things are important.
- Rotation around x, y,z , in LEFT-Handed System
    - ![](../imgs/gpu_rotate_LHS1.png)
    - clockwise if you're thinking about looking again the particular axis
    - counter clockwise if you're thinking about looking down a particular axis
- If you're in a RHS, the clockwise/counter clockwise should inverse.
    - so you may have to check to see what conventions your game engine is using.

- 2D Rotation
    ```octave
    [X',Y',1] = 

              ⎡ cosθ sinθ 0 ⎤  
     [X,Y,1]· ⎢-sinθ cosθ 0 ⎥  
              ⎣  0    0   1 ⎦  
    ```
- 3D Rotation ( LHS )
    - for 3D: Rotate along which axis ?
    - Rotation along **Z** axis ( fix z )
        ```octave
        [X',Y',Z',1] = 

                    ⎡ cosθ sinθ 0  0 ⎤  
         [X,Y,Z,1]· ⎢-sinθ cosθ 0  0 ⎥  
                    ⎢  0    0   ⑴  0 ⎥  
                    ⎣  0    0   0  1 ⎦  
        ```
    - Rotation along **Y** axis ( fix y )
        - be careful about the sign of `sinθ`, it's switched
        ```octave
        [X',Y',Z',1] = 

                    ⎡ cosθ  0 -sinθ 0 ⎤  
         [X,Y,Z,1]· ⎢  0    ⑴   0   0 ⎥  
                    ⎢ sinθ  0  cosθ 0 ⎥  
                    ⎣  0    0   0   1 ⎦  
        ```
    - Rotation along **X** axis ( fix x )
        ```octave
        [X',Y',Z',1] = 

                    ⎡ ⑴   0    0   0 ⎤  
         [X,Y,Z,1]· ⎢ 0  cosθ sinθ 0 ⎥ 
                    ⎢ 0 -sinθ cosθ 0 ⎥  
                    ⎣ 0   0    0   1 ⎦  
        ```


## Specifying the view transformation

- Most commonly parameterized by
    - Position of camera
    - Position of point to look at
    - Vector indicating "up" direction of camera
- In Direct3D: D3DXMatrixLookAtLH
    - D3D use a LHS, but also have D3DXMatrixLookAtRH
- In XNA, Matrix.CreateLookAt (RHS)
- In OpenGL: gluLookAT (RHS)
- In Unity: Matrix4x4.LookAt (LHS)
    - but usually a programmer will only call this if they're doing some specialized weird thing because usually there's a camera class with various built-in scripts associated with it that will call such `LookAt` routine for you.


# 4 Orthogonal Projection 


