
# Introduction to WebGL

 - WebGL 1.0 is based on OpenGL ES 2.0, a version designed for use on embedded systems 
 - OpenGL ES 1.0 was very similar to OpenGL 1.1. 
    - OpenGL ES 2.0 introduced major changes. It is actually a smaller, simpler API that puts more responsibility on the programmer. 
    - For example, functions for working with transformations, such as glRotatef and glPushMatrix, were eliminated from the API,making the programmer responsible for keeping track of transformations.
 - WebGL does not use glBegin/glEnd to generate geometry, and it doesn't use function such as `glColor*` or `glNormal*` to specify attributes of vertices. 
 - There are two sides to any WebGL program. 
    - Part of the program is written in *JavaScript*
    - The second part is written in *GLSL*


## Section 1: The Programmable Pipeline

 - OpenGL 1.1 used a *fixed-function pipeline* for graphics processing.
    - data is provided by a program , and passes through a series of processing stages.
    - the program can enable/disable some of the steps in the process, but there is no way for it to change what happends at each stage.
    - The functionality is fixed.
 - OpenGL 2.0 introduced a *programmable pipeline*. 
    - it is possible to replace certain stages in the pipeline with custom program.
    - This gives the programmer complete control over what happens at that stage. 
    - the programmability was optional
        - the complete fixed-function pipeline was still available for programs that didn't need the flexibility of programmability.
    - WebGL uses a programmable pipeline, and it is **mandatory**. 
        - There is no way to use WebGL without writing programs to implement part of the graphics processing pipeline.
 - The programs that are written as part of the pipeline are called *shaders*. 
    - For WebGL, you need to write a *vertex shader*, which is called once for each vertex in a primitive, 
        - and a *fragment shader*, which is called once for each pixel in the primitive.
    - Aside from these two programmable stages, the WebGL pipeline also contains several stages from the original fixed-function pipeline. 
 - This book covers WebGL 1.0. 
    - Version 2.0 was released in January 2017. and it is compatible with version 1.0.
    - At the end of 2017, WebGL 2.0 is available in some browsers.
    - The later versions of OpenGL have introduced **additional** programmable stages into the pipeline.

### 6.1.1  The WebGL Graphics Context

 - To use WebGL, you need a WebGL graphics context. 
    - ( A few browsers (notably Internet Explorer and Edge) require "experimental-webgl"  )

```js
// <canvas width="800" height="600" id="webglcanvas"></canvas>
...
canvas = document.getElementById("webglcanvas");
gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
```

 - `gl` may be null. You'd better catch the exception

```js
function init() {
    try {
        canvas = document.getElementById("webglcanvas");
        gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
        if ( ! gl ) {
            throw "Browser does not support WebGL";
        }
    }
    catch (e) {
          .
          .  // report the error
          .
        return;
    }
      .
      .  // other JavaScript initialization
      .
    initGL();  // a function that initializes the WebGL graphics context
}
```

 - The init() function could be called, for example, by the onload event handler for the `<body>` element of the web page:

```
<body onload="init()">
```


### 6.1.2  The Shader Program

 - Drawing with WebGL requires a shader program. Shaders are written in the language GLSL ES 1.0.
    - The vertex shader and fragment shader are compiled separately,  and then "linked" to produce a complete shader program. 
 - To create the vertex shader.

```js
// vertexShaderSource is a JavaScript string
var vertexShader = gl.createShader( gl.VERTEX_SHADER );
gl.shaderSource( vertexShader, vertexShaderSource );
gl.compileShader( vertexShader );
```

 - Errors in the source code will cause the compilation to fail silently. You need to check for compilation errors by calling the function

```js
gl.getShaderParameter( vertexShader, gl.COMPILE_STATUS )  
```

 - which returns a boolean value to indicate whether the compilation succeeded. 
 - In the event that an error occurred, you can retrieve an error message with

```js
gl.getShaderInfoLog(vertexShader)
```

 - which returns a string containing the result of the compilation. 

 - The fragment shader can be created in the same way. 
 - With both shaders in hand, you can **create** and **link** the **program**. 

```js
var prog = gl.createProgram();
gl.attachShader( prog, vertexShader );
gl.attachShader( prog, fragmentShader );
gl.linkProgram( prog );
```

 - Even if the shaders have been successfully compiled, errors can occur when they are linked into a complete program. 
    - For example, the vertex and fragment shader can share certain kinds of variable.
    - If the two programs declare such variables with the same name but with different types, an error will occur at link time. 
    - Checking for link errors is similar to checking for compilation errors in the shaders.
 - The code for creating a shader program is always pretty much the same.
    - Here is an example function:

```js
/**
 * Creates a program for use in the WebGL context gl, and returns the
 * identifier for that program.  If an error occurs while compiling or
 * linking the program, an exception of type String is thrown.  The error
 * string contains the compilation or linking error. 
 */
function createProgram(gl, vertexShaderSource, fragmentShaderSource) {
   var vsh = gl.createShader( gl.VERTEX_SHADER );
   gl.shaderSource( vsh, vertexShaderSource );
   gl.compileShader( vsh );
   if ( ! gl.getShaderParameter(vsh, gl.COMPILE_STATUS) ) {
      throw "Error in vertex shader:  " + gl.getShaderInfoLog(vsh);
   }
   var fsh = gl.createShader( gl.FRAGMENT_SHADER );
   gl.shaderSource( fsh, fragmentShaderSource );
   gl.compileShader( fsh );
   if ( ! gl.getShaderParameter(fsh, gl.COMPILE_STATUS) ) {
      throw "Error in fragment shader:  " + gl.getShaderInfoLog(fsh);
   }
   var prog = gl.createProgram();
   gl.attachShader( prog, vsh );
   gl.attachShader( prog, fsh );
   gl.linkProgram( prog );
   if ( ! gl.getProgramParameter( prog, gl.LINK_STATUS) ) {
      throw "Link error in program:  " + gl.getProgramInfoLog(prog);
   }
   return prog;
}
```

 - There is one more step: You have to tell the WebGL context to use the program. 

```js
gl.useProgram( prog );
```

 - It is possible to create several shader programs. 
    - You can then switch from one program to another at any time by calling `gl.useProgram`, even in the middle of rendering an image. 
    - (Three.js, for example, uses a different program for each type of Material.)
 - Shaders and programs that are no longer needed can be deleted to free up the resources they consume.
    - Use the functions `gl.deleteShader(shader)` and `gl.deleteProgram(program)`.


### 6.1.3  Data Flow in the Pipeline

 - The basic operation in WebGL is to draw a geometric primitive. 
    - The primitives for drawing quads and polygons have been removed.
    - The remaining primitives draw points, line segments, and triangles.
    - gl.POINTS, gl.LINES, gl.LINE_STRIP, gl.LINE_LOOP, gl.TRIANGLES, gl.TRIANGLE_STRIP, and gl.TRIANGLE_FAN,
 - When WebGL is used to draw a primitive, there are two general categories of data that can be provided for the primitive. 
    - **attribute** variables
    - **uniform** variables
 - A uniform variable has a single value that is the same for the entire primitive, while the value of an attribute variable can be different for different vertices.


must be attribute | attri or uniform | must be uniform  
--- | --- | --- 
coordinates  | | 
     | color | 
     | normal vectors | 
     | material properties | 
Texture coordinates | | 
     |       | geometric transform 



## Section 2: First Examples
## Section 3: GLSL
## Section 4: Image Textures
## Section 5: Implementing 2D Transforms



