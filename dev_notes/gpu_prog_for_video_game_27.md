[](...menustart)

- [27: Projective Textures](#3037d1aee3dbe87b7c6cfd54b93e9076)
    - [What is projective texturing ?](#9c98f87935de072fe08a8a44c16fb59a)
    - [Texture matrix](#39745511f68e78b75ef8d614d1a7cb0f)
    - [ProjectTexture -- setup](#5a58a9056874e1d2458521976f667a70)
    - [ProjectTexture -- uniforms](#d5f409ac7d9ee2c916763d5f31290c21)
    - [ProjectTexture -- structures](#2c0007b7b967ea830273fbe9e9ea38c1)
    - [ProjectTexture -- vertex program](#5d59a90b289ef216c29995159eb7e874)
    - [ProjectTexture -- fragment program](#810d334284b3e4ecbaec32b318395082)
    - [C# script to set up projector matrix](#e2dd661e030d10dae5388ff8097b1df7)
    - [Watch out for the reverse projection!](#5188162a545a23b057c660be02d12070)

[](...menuend)


<h2 id="3037d1aee3dbe87b7c6cfd54b93e9076"></h2>

# 27: Projective Textures

<h2 id="9c98f87935de072fe08a8a44c16fb59a"></h2>

## What is projective texturing ?

- An intuition for projective texturing
    - The slide projector analogy
    - ![](../imgs/gpu_projective_tex_ex_1.png)
    - project onto various objects in the scene

- Another exmaple:  different locations
    - ![](../imgs/gpu_projective_tex_ex_2.png)


<h2 id="39745511f68e78b75ef8d614d1a7cb0f"></h2>

## Texture matrix

from "The Cg Tutorial", p.252

- ![](../imgs/gpu_projective_tex_matrix_1.png)
- The way we formulate this is basically to setup the same set of matrix transformation we would, when taking 3D object in the scene and projecting them onto a camera plane, except here we're using the light position and orientation as if the light itself is the camera.
- so we still have the same  modeling matrix which translates model coordiantes into world space.
- and then transform into a view space, but this view space is from the point of the projecting light, not the camera.
- similarly we will go through a projection matrix, again, from the point of view of the light, not the camera.
- the last matrix is used to shift  everything from [-1,1] to [0,1] because that's what texture lookups expect.

<h2 id="5a58a9056874e1d2458521976f667a70"></h2>

## ProjectTexture -- setup

- ![](../imgs/gpu_project_texture_setup.png)
    - "ForwardAdd" lightmode


<h2 id="d5f409ac7d9ee2c916763d5f31290c21"></h2>

## ProjectTexture -- uniforms

```c
sampler2D _BaseTex;
float4 _BaseTex_ST;
sampler2D _SpotPower;

float _SpotPower;

float4x4 _myProjectorMatrixVP;
float3 _spotlightDir;
```

- `_myProjectorMatrixVP` view projection matrix for the light


<h2 id="2c0007b7b967ea830273fbe9e9ea38c1"></h2>

## ProjectTexture -- structures

```c
struct a2v { // application to vertex
    float4 positionOS: POSITION;
    float3 normalOS: NORMAL;
    float2 uv : TEXCOORD0;
}; 

struct v2f { // vertex 2 fragment
    float4 sv: SV_POSITION;
    float2 uv: TEXCOORD0;
    float3 positionWS: TEXCOORD1;
    float3 normalWS: TEXCOORD2;
    float4 positionProjected: TEXCOORD3;
};
```

<h2 id="5d59a90b289ef216c29995159eb7e874"></h2>

## ProjectTexture -- vertex program

- ![](../imgs/gpu_project_tex_vertex.png)


<h2 id="810d334284b3e4ecbaec32b318395082"></h2>

## ProjectTexture -- fragment program

- ![](../imgs/gpu_project_tex_fragment.png)
    - the `lightDir` vector is pointing from vertex to the light, the `_spotlightDir` is pointing out of the light, so I put the minus sign on `lightDir` in `spotlightEffect` computation, and take dot product on that to get something falls off as the angle increases to get nice spot effect.
        - and then we take it to some `pow`, and by changing the power we can change the size of the spot.
    ```c
    diffAlmost *= tex2Dproj( _ProjTex, input.positionProjected );
    ```
        - new version of `tex2D` : `tex2Dproj`
        - instead of giving a 2D `uv` coordinate, you give it a 4D vector that represents s,t,r,q coordinates space related to the light source.  and this `tex2Dproj` handles that divide by q.



<h2 id="e2dd661e030d10dae5388ff8097b1df7"></h2>

## C# script to set up projector matrix

- ![](../imgs/gpu_project_tex_setup_matrix_1.png)
- this is a c# script to define component that will attach to a camera object. but this camera object is attached to is not the main camera, it's sort of a fake camera we're using for the spot light effect.
- I set this `[ExecuteInEditMode]` directive that tells unity to run this in editor, not just in game.
- once we have `myCamera` component, we can go ask it what's the projection matrix that you're using and what the world to camera matrix is.
    - `myCamera.projectionMatrix` , `myCamera.worldToCameraMatrix`
- And now I'm goging to engage in some bad programming practice.
    ```c
    // Quick & dirty; it would generally be better to set properties in specific materials.
    // :  use component.material.Setxxxx ?
    Shader.SetGlobalMatrix( "_myProjectorMatrixVP", projectionMatrix );
    Shader.SetGlobalVector( "_spotlightDir", transform.forward );
    ```
    - the `Shader` class has some static methods, those static methods will go through **EVERY** single material . And each time they find a shader that has the variable with the specific name they set the values. But it does that for **EVERY** single material. So this wouldn't work if you want to have multiple spot light. And looking string in unity is extreamly time comsuming.


<h2 id="5188162a545a23b057c660be02d12070"></h2>

## Watch out for the reverse projection!

- ![](../imgs/gpu_reverse_projection_watch_out.png)

- There is one  interesting effect that sometimes you have to watch out for ,  the underlying projection matrix math doesn't care which direction you're going.
    - so you can have this weird mirrored projections what you might have to be careful about.
- The most common use actually is as the core of implementing shadows maps, which is method of handling shadow effects.
- I should let you know that unity does have spot light builtin to it, along with the ability for those spot light to project textures.
    - Unity implements this in the way that is different that what I describes here.




