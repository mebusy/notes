
# Introduction to Compute Graphics

[website](http://math.hws.edu/graphicsbook/)

[course pdf](http://math.hws.edu/eck/cs424/downloads/graphicsbook-linked.pdf)

[labs used to teach course 2017](http://math.hws.edu/eck/cs424/index_f17.html)


In this book , will use a subset of OpenGL 1.1 to introduce the fundamental concepts of three-dimensional graphics. 


## Chapter 1 Introduction

## 1.2 Elements of 3D Graphics

 - geometric primitives
    - such as line, segments and triangles 
 - material
    - the properties that determine the intrinsic visual appearance of a surface.
    - Essentially, this means how the surface interacts with light that hits the surface.
    - can include a basic color as well as other properties such as shininess, roughness, and transparency.
 - texture
    - One of the most useful kinds of material property
    - Textures allow us to add detail to a scene without using a huge number of geometric primitives;


## 1.3 Hardware and Software
 
 - OpenGl
    - designed as a "client/server" system
    - communicating from the client (the CPU) to the server (the GPU)  are very slow
        - One approach is to store information in the GPU's memory.  
            - If some data is going to be used several times, it can be transmitted to the GPU once and stored in memory there.
        - Another approach is to try to decrease the number of OpenGL commands that must be transmitted to the GPU to draw a given image.
            - in OpenGL 1.1, all the data for the object would be loaded into arrays , which could then be sent in a single step to the GPU. 
            - Unfortunately, the data would have to be retransmitted each time the object was drawn.
            - This was fixed in OpenGL 1.5 with *Vertex Buffer Objects* .  A VBO is a block of memory in the GPU that can store the coordinates or attribute values for a set of vertices.

    - OpenGL 1.1 introduced *texture objects to* make it possible to store several images on the GPU for use as textures. 
    - OpenGL was a giant machine, but still not pleasing everyone. The real solution was to make the machine **programmable**.
        - With OpenGL 2.0, it became possible to write programs to be executed as part of the graphical computation in the GPU. 
        - The programs are called *shaders*.
    - In OpenGL 3.0, the usual per-vertex and per-fragment processing was deprecated. 
    - And in OpenGL 3.1, it was removed from the OpenGL standard, although it is still present as an optional extension.
    - In practice, all the original features of OpenGL are still supported in desktop versions of OpenGL and will probably continue to be available in the future. 
        - On the embedded system side, however, with OpenGL ES 2.0 and later, the use of shaders is mandatory, and a large part of the OpenGL 1.1 API has been completely removed. 
        - WebGL, the version of OpenGL for use in web browsers, is based on OpenGL ES 2.0, and it also requires shaders to get anything at all done.
    - Nevertheless, we will begin our study of OpenGL with version 1.1. Most of the concepts and many of the details from that version are still relevant, and it offers an easier entry point for someone new to 3D graphics programming.

 - OpenGL shaders are written in GLSL (OpenGL Shading Language).
    - We will spend some time later in the course studying GLSL ES 1.0, the version used with WebGL 1.0 and OpenGL ES 2.0. 
    - GLSL uses a syntax similar to the C programming language.

---

# Chapter 2 Two-Dimensional Graphics

## 2.1 Pixels, Coordinates, and Colors

 - *Antialiasing* is a term for techniques that are designed to mitigate the effects of aliasing. 
    - The idea is that when a pixel is only partially covered by a shape, the color of the pixel should be a mixture of the color of the shape and the color of the background. 
    - In practice, calculating this area exactly for each pixel would be too difficult, so some approximate method is used.


## Section 2.2 Shapes

 - Line
    - A simple one-pixel-wide line segment, without antialiasing, is the most basic shape.
        - One of the first computer graphics algorithms,  **Bresenham's** algorithm for line drawing, implements a very efficient procedure for doing so. 
    - In any case, lines are typically more complicated. Antialiasing is one complication. Line width is another. A wide line might actually be drawn as a rectangle.
    
## Section 2.3 Transforms

### 2.3.8  Matrices and Vectors

 - If we want to apply a scaling followed by a rotation to the point v = (x,y), we can compute either R(Sv) or (RS)v. 
 - Translation is not a linear transformation. 



