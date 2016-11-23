

# REAL-TIME PROGRAMMABLE SHADING

There are some significant differences between real-time programmable shading and offline programmable shading. 

## What Makes Real-Time Shading Different?

 - *Most applications are interactive.*
 	- As a result, the shader writer usually does not know which viewpoints will be used to view an object and may not even know which lights will be near an object.
 - *Performance is critical.*
 - *Shaders execute on graphics hardware.*
 	- Graphics hardware provides high performance at low cost, but imposes certain restrictions on shading programs in order to obtain this high performance.


## What You Need to Learn Elsewhere

If you are writing a complete real-time graphics application, you will need to understand the entire graphics pipeline, not just the programmable shading parts of it. 

There are two major interfaces for controlling the entire graphics pipeline -— Direct3D and OpenGL.

## Object Space Shading versus Screen Space Shading

 - Hardware graphics pipelines perform some programmable shading in object space (at vertices) 
 - and some programmable shading in screen space (in effect, at pixels).

In contrast, the REYES algorithm used by Pixar’s PRMan performs all shading in object space, at the vertices of automatically generated micropolygons. (Note that other RenderMan implementations, such as BMRT, use different approaches.)

Hardware pipelines use the hybrid vertex/pixel shading approach for a variety of reasons, including the need for high performance and the evolutionary path that graphics harware has followed in the past. 

We will explain the two approaches to programmable shading in more detail and discuss their advantages and disadvantages.

RenderMan uses curved surfaces (both tensor-product splines and subdivision surfaces) as its primary geometric primitives. To render these surfaces, PRMan dices them into grids, then uniformly tessellates each grid into “micropolygons” that are smaller than a pixel, as in Figure 3.1(a). 




> FIGURE 3.1 Comparison of (a) the REYES pipeline (used in Pixar’s RenderMan) and (b) the pipeline used in real-time graphics hardware.

