...menustart

- [25: Environment Mapping](#19ffde22bc6feb61e5d45a4a82a2e5c0)
    - [Vector Notation](#902405de406cdbad4b017ad8413eee37)
    - [Reflection](#aea1e492943ccbad7ee270ec1e064758)
    - [Cube Maps](#ea850b88c9ce09cfa7b387d36fc78ae6)
    - [Refraction](#fb2aa8b231ad4c797a5c90db33ab8c31)
    - [Different indices of refraction](#09d1424d7efc049cd01af1c62c53abc0)
    - [EnvMap ( per vertex ) -- setup](#4a3f2ae28dfb34e06e7277eeeef33318)
    - [EnvMap ( per vertex ) -- structures](#10151d62f4134fd920294f01e38dd4cc)
    - [EnvMap ( per vertex ) -- Vertex Program](#69f80be069e649041614a547a54bc7a2)
    - [EnvMap ( per vertex ) -- Fragment Program](#18a4618e54cea64f8bb11b09ff0bdd30)
    - [Fresnel effect](#a6977b0b6db1f017d37ea6684915d2e0)
    - [EnvMap ( per Pixel ) -- structures](#ebe635d89f50c22c0d296cf85a87d802)
    - [EnvMap ( per Pixel ) -- Vertex Program](#be232993bbebdcb5c0f45b4ca6059311)
    - [EnvMap ( per Pixel ) -- Fragment Program](#7c43ebcad7b9462cfe2d235796672691)

...menuend


<h2 id="19ffde22bc6feb61e5d45a4a82a2e5c0"></h2>


# 25: Environment Mapping

- If you want an accurate simulation of those kind of effects ( e.g. reflection ) you need to go to something like ray tracing.

<h2 id="902405de406cdbad4b017ad8413eee37"></h2>


## Vector Notation

- ![](../imgs/gpu_vector_notation.png)


- what's a little bit confusing is that in this lecture, we're mostly going to want to be **reflecting the eye vector**.


<h2 id="aea1e492943ccbad7ee270ec1e064758"></h2>


## Reflection

- N needs to be normalized
- R has same length as L
    - R = L - 2N(N·L)
- fortunately there is a command built into most shading languages
    - R = reflect( L,N ) 


<h2 id="ea850b88c9ce09cfa7b387d36fc78ae6"></h2>


## Cube Maps

- The way we're going to fake reflection effects is using a cube map.
- The reflection that we're seeing depends on the eye position.
- to lookup a cube map:
    - `texCUBE( (samplerCUBE) envMap, (float3)vec )`
    - the 2nd parameter `vec` doesn't need to be normalized.

<h2 id="fb2aa8b231ad4c797a5c90db33ab8c31"></h2>


## Refraction

- in addition to reflection effects, we can also use cube maps for refraction effects, where we're imagining that the object is translucent and we're seeing light waves from things on the other side but they're distorted a bit because those light waves are being bent as they're going through the surface.
- ![](../imgs/gpu_refraction_1.png)
    - T = refract( I, N, etaRatio )
    - etaRatio = η₁ / η₂ 
        - η₁ , η₂ is the index of refraction


<h2 id="09d1424d7efc049cd01af1c62c53abc0"></h2>


## Different indices of refraction

- Vacuum: 1.0
- Air: 1.0003
- Water: 1.333
- Glass: 1.5 (ordinary window glass)
- Plastic: 1.5
- Diamond: 2.417
- Data from "The Cg Tutorial", p.184


<h2 id="4a3f2ae28dfb34e06e7277eeeef33318"></h2>


## EnvMap ( per vertex ) -- setup

- ![](../imgs/gpu_envmap_per_vert_1.png)
- `_Cube ("Reflection Cubemap", CUBE )` = "white" {}
- for this shader, I created a `_crossfade` slider that lets you crossfade between a pure reflection effect and a pure refraction effect.


<h2 id="10151d62f4134fd920294f01e38dd4cc"></h2>


## EnvMap ( per vertex ) -- structures

```c
samplerCUBE _Cube;
float _etaRatio;
float _crossfade;

struct a2v { // application to vertex
    float4 positionOS: POSITION;
    float3 normalOS: NORMAL;
}; 

struct v2f { // vertex 2 fragment
    float4 sv: SV_POSITION;
    float3 reflectWS: TEXCOORD0;
    float3 refractWS: TEXCOORD1;
};
```

<h2 id="69f80be069e649041614a547a54bc7a2"></h2>


## EnvMap ( per vertex ) -- Vertex Program

- ![](../imgs/gpu_envmap_per_vert_2.png)
- we're going to compute the incident light vector that's pointing from where the camera is to the vertex
    ```c
    // incident is opposite the dir of eyedir in other programs
    float3 incidentWS = normalize(
        positionWS - _WorldSpaceCameraPos ).xyz; 
    ```
- and then we use the `reflect` and `refract` command to find the reflected and refracted vector
    ```c
    output.reflectWS = reflect( incidentWS, normalWS ) ;
    output.refractWS = refract( incidentWS, normalWS, _etaRatio );
    ```


<h2 id="18a4618e54cea64f8bb11b09ff0bdd30"></h2>


## EnvMap ( per vertex ) -- Fragment Program

- ![](../imgs/gpu_envmap_per_vert_3.png)
- `texCUBE` don't care about whether the 2nd parameter is unit vector, it cares about only the direction.
- `lerp(reflectColor, refractColor, _corrsfade)`
    - linearly interpolate between those 2 colors it looks up depending on `_crossfade`
- per-vertex shader creates some problems with some clearly visible artifacts.
    - ![](../imgs/gpu_envmap_per_vert_4.png)

<h2 id="a6977b0b6db1f017d37ea6684915d2e0"></h2>


## Fresnel effect 

before we look at the per pixel code, I want to talk about an effect that I added to the per-pixel code.

- from "The Cg Tutorial" p.189
- Fresnel effect
    - Some light reflects and some refracts
    - Think about looking into water
        - At shallow angles, a lot of reflection and little refraction
        - Looking straight in, a lot of refraction and a little reflection
    - Empirical approximation: I = -E
        - remember that the incident vector for whatever historical reason is defined as being opposite of our usual Eye vector. So I is pointing from the camera to the surface instead of the other way around.
        - reflectCoeff = max( 0, min( 1, bias+scale(1 + I·n )<sup>power</sup> ) )
        - C<sub>final</sub> = reflectCoeff x C<sub>reflected</sub> + ( 1-reflectCeoff)C<sub>refracted</sub>
        - comments
            - bias, scale, power are parameters you can use to adjust this effect.
            - you get a reflect coefficient in [0,1] that you use to interpolate between the reflected and refracted colors ( C<sub>reflected</sub> & C<sub>refracted</sub> ) .

- ![](../imgs/gpu_envmap_per_pixel_fresnel_1.png)
    - 3 new properties: _fresnelBias , _fresnelScal, _fresnelPower
    - `Toggle`
        - will actually create a little checkmark box that will be filled with either 0 or 1, 0 means unchecked.
        - this is what I'm going to use to select a certain diagnostic mode that ignores all the cube lookups and just replaces them with a color blue and yellow.
        - this will give us a way to visualize the Fresnel reflect coefficient calculation.
    - `KeywordEnum`
        - drop-down menu
        - let us switch between using the original crossfade I already used in the per-vertex shader and the fancier Fersnel effect.
    - the way that you actually use the `Toggle` and `KeywordEnum` is by placing some `#pragma`  into your shader code
        ```c
        #pragma shader_feature BLUE_YELLOW
        #pragma multi_compile _BLEND_CROSSFADE _BLEND_FRESNEL
        ```
    - "\_BLEND" + "_" +  upcase( "Crossfade" )

<h2 id="ebe635d89f50c22c0d296cf85a87d802"></h2>


## EnvMap ( per Pixel ) -- structures


```c
samplerCUBE _Cube;
float _etaRatio;
float _crossfade;
float _fresnelBias ; // new
float _fresnelScale ; // new
float _fresnelPower ; // new

struct a2v { // application to vertex
    float4 positionOS: POSITION;
    float3 normalOS: NORMAL;
}; 

struct v2f { // vertex 2 fragment
    float4 sv: SV_POSITION;
    float3 positionWS: TEXCOORD0;   // changed
    float3 normalWS: TEXCOORD1;     // changed
};
```

<h2 id="be232993bbebdcb5c0f45b4ca6059311"></h2>


## EnvMap ( per Pixel ) -- Vertex Program

- ![](../imgs/gpu_envmap_per_pixel_fresnel_2.png)


<h2 id="7c43ebcad7b9462cfe2d235796672691"></h2>


## EnvMap ( per Pixel ) -- Fragment Program

- ![](../imgs/gpu_envmap_per_pixel_1.png)
- ![](../imgs/gpu_envmap_per_pixel_2.png)


