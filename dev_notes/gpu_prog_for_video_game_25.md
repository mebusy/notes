
# 25: Environment Mapping

- If you want an accurate simulation of those kind of effects ( e.g. reflection ) you need to go to something like ray tracing.

## Vector Notation

- ![](../imgs/gpu_vector_notation.png)


- what's a little bit confusing is that in this lecture, we're mostly going to want to be **reflecting the eye vector**.


## Reflection

- N needs to be normalized
- R has same length as L
    - R = L - 2N(N·L)
- fortunately there is a command built into most shading languages
    - R = reflect( L,N ) 


## Cube Maps

- The way we're going to fake reflection effects is using a cube map.
- The reflection that we're seeing depends on the eye position.
- to lookup a cube map:
    - `texCUBE( (samplerCUBE) envMap, (float3)vec )`
    - the 2nd parameter `vec` doesn't need to be normalized.

## Refraction

- in addition to reflection effects, we can also use cube maps for refraction effects, where we're imagining that the object is translucent and we're seeing light waves from things on the other side but they're distorted a bit because those light waves are being bent as they're going through the surface.
- ![](../imgs/gpu_refraction_1.png)
    - T = refract( I, N, etaRatio )
    - etaRatio = η₁ / η₂ 
        - η₁ , η₂ is the index of refraction


## Different indices of refraction

- Vacuum: 1.0
- Air: 1.0003
- Water: 1.333
- Glass: 1.5 (ordinary window glass)
- Plastic: 1.5
- Diamond: 2.417
- Data from "The Cg Tutorial", p.184


## EnvMap ( per vertex ) -- setup

- ![](../imgs/gpu_envmap_per_vert_1.png)
- `_Cube ("Reflection Cubemap", CUBE )` = "white" {}
- for this shader, I created a `_crossfade` slider that lets you crossfade between a pure reflection effect and a pure refraction effect.


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










