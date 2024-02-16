[](...menustart)

- [WebGL Tips](#20cf1d566508f29fb50f5da48374ba38)
    - [Qualifiers](#619dd4db8171a8f1bf978f44c9cf10c4)
    - [BUILT-IN VARIABLES](#435827c0432e29e22a2b69df5c4a9db4)
- [Three.js Tips](#bcf2f4a04de7d50e787ded8c2c14e655)

[](...menuend)


<h2 id="20cf1d566508f29fb50f5da48374ba38"></h2>

# WebGL Tips

[OpenGL-ES-2_0-Reference-card](https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf)



<h2 id="619dd4db8171a8f1bf978f44c9cf10c4"></h2>

## Qualifiers

1.0 name | 2.0 name | Facility | Data 
--- | --- | --- | ---
attribute | in | store current vertex data |  per vertex parameters
varying | out | interpolated data between vertex/fragment shaders(e.g. pass the vertex position to fragment shader) | per-fragment(or per-pixel)
uniform | uniform | store "constant" data during entire draw call | per primitive parameters


<h2 id="435827c0432e29e22a2b69df5c4a9db4"></h2>

## BUILT-IN VARIABLES

variable name | Description | Shading Stage | Access
--- | --- | --- | ---
gl_Position | output vertex position | Vertex |  Must be writen
gl_FragColor | output fragment color | Fragment |  Must (in WebGL 1.0)
gl_FragCoord | viewport position | Fragment | Read only
gl_FragDepth | depth value in [0,1] | Fragment | Read only



<h2 id="bcf2f4a04de7d50e787ded8c2c14e655"></h2>

# Three.js Tips

- All objects by default automatically update their matrices, or if they are the child of another object that has been added to the scene
    - However, if you know the object will be static, you can disable this and update the transform matrix manually just when needed.
    ```javascript
    object.matrixAutoUpdate = false;
    object.updateMatrix();
    ```
- built-in uniform & attributes
    - https://threejs.org/docs/#api/en/renderers/webgl/WebGLProgram 


## custom shader

```javascript
import vertexShader from './shaders/vertex.glsl'
import fragmentShader from './shaders/fragment.glsl'

//...

  // meshes
  const geometry = new THREE.PlaneGeometry(2, 2)
  const material = new THREE.ShaderMaterial({
    vertexShader: vertexShader,
    fragmentShader: fragmentShader,
    // wireframe: true,
  })
  // ...
```

- three.js ShaderMaterial class create some attributes, uniform for you
    - such like `projectionMatrix`, `modelViewMatrix`, `position`
    - if you want take control everything yourself, you should use `THREE.RawShaderMaterial`
        - when using `THREE.RawShaderMaterial`, you need to specify a precision for floats
        ```c
        precision mediump float;
        ```

## custom uniform

e.g. create a float uniform named `uTime`

```javascript
    // in javascript
    material.uniforms.uTime = {value: 0}
```

```c
// in shader
uniform float uTime;
```


