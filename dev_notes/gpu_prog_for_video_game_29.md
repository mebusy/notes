
# 29: Cook-Torrance Specular Models

- most popular model for specular reflections and physically based rendering

## Elements of PBR

- Linear space lighting
    - don't use gamma color space
- **Energy conservation**
    - unless you have a material that is emissive (i.e. it is its own light source) it can't be reflecting **more** energy than is coming in.
- **Reciprocity**
    - which says you need to be able to swap the viewer and the light source and get the same answer.
- Metallic/dielectric distinction
    - we're going to be using the term `dielectric` in a much more general sense, basically a dielectric is anything that's not metal.
- "Everything is shiny" (i.e. has specular)
- "Everything has Fresnel"
    - here we're using the term `fresnel` in a different way. It has the same ideas but we're going to be a little more specific about it, and essentially apply it to everything not just things that are refracting.
- Bonus: high definition render buffers and tonemapping to handle high dynamic range
    - now if you actually implement all of these above things and try to put in some realistic light sources and materials you will find that the kinds of light your camera is receiving will cover an extreme dynamic range.
    - previously when people weren't trying to go for physically based rendering they're just trying to go for something that looked decent, you would take a lot of time scaling your light sources to try to not blow out your image. But if you are trying to do something somewhat realistic you have to encapsulate the fact that you will have some very dim parts of your scene and some very bright parts of your scene.
    - so you may need a high definition render buffer that can handle this high dynamic range and then various techniques such as tone mapping or bloom to take that high dynamic range information and compress it into what can actually be shown on a display.


## Bidirectional Reflectance Functions 

- For "punctal" lights ( typical point, directional , spotlight... )
    - C<sub>final</sub> = C<sub>light</sub> ⊗ πBRDF(L,V) max(0, n·L)
    - BRDF: bidirectional reflectance distribution function
    - L: light coming in
    - V: viewer
    - π: magic ...
    - ⊗: color-wise multiplication
        - multiply red by red, green by green, blue by blue
- Classic diffuse lighting model:
    - BRDF = M<sub>dif</sub> / π
    - C<sub>final</sub> = C<sub>light</sub> ⊗ M<sub>dif</sub>  max(0, n·L)
- Classic Blinn-Phong lighting model:
    - ![](../imgs/gpu_blinn_phong_specular_brdf.png)
    - C<sub>final</sub> = C<sub>light</sub> ⊗ M<sub>spec</sub> (n·H)<sup>s</sup>
    - H: unit half vector between the light vector and the viewing vector
    - unfortunately it's not physically plausible for a couple of reasons.

## BRDFs should have reciprocity

- Reciprocity means we can swap the incoming and outgoing light directions:
    - BRDF(L,V) = BRDF(V,L)
- Obviously true for classic diffuse lighting, because that's just a contant, doesn't have L or V in it anyway.
    - BRDF = M<sub>dif</sub> / π
- Reciprocity does not hold for classic Blinn-Phong:
    - ![](../imgs/gpu_blinn_phong_specular_brdf_full.png)
        - ![](../imgs/gpu_blinn_phong_specular_brdf_full_swap.png)
        - n·L ≠ n·V
    - so later when people introduced the idea of physically based rendering they thought how can we give it reciprocity. And the obivous thing to do is just drop the this denominator `/ n·L`


## Modified Blin-Phong

- BRDF = ( M<sub>dif</sub> / π ) (n·H)<sup>s</sup> 
    - s parameter:  let us scale the width of the spot. 
        - if s is very small,  I get a broad peak , while if s is large, I get a narrow peak , because `n·H < 1`
- C<sub>final</sub> = C<sub>light</sub> ⊗ M<sub>spec</sub> (n·H)<sup>s</sup> max(0, n·L)
- But there is a problem with this `s`. In general this `s` is not enery conservation. 


## Energy conservation

- "Total amount of reflected light cannot be more than the amount of incoming light" -- Rory Driscoll
- For classic diffuse model BRDF = M<sub>dif</sub> / π 
    - turns out you techinically nedd πM<sub>dif</sub> `< 1` ( need calculus to derive)
- since π is just a constant, "we usually just ignore it and assume that our lights are just π times too bright." -- Steve McAuley


## A common yet confusing convention

- For classic diffuse model BRDF = M<sub>dif</sub> / π 
    - We'll pretend you practically need M<sub>dif</sub> `< 1`
- Convenient for artists: hit a diffuse surface with a materialo color of "1" with a directional light with an "intensity" of "1" parallel with its normal and you get "1"
- If you are implementing global illumination, be careful !
    - if you have something that's sending out more light than it's taking in when it's not supposed to that can cause your numeric solutions to freak out.

## Normalized modified Blinn-Phong

- To achieve energy conservation
    - ![](../imgs/gpu_normialzed_mod_blinn_phong.png)
    - it turns out if you work through a bunch of multi-dimensional integrals you can figour out that if you stick this fact `(S+8)/(8Π)` out in front, then the reflected energy is going to be conserved as you change `s`.
    - and having this term `s+8` in the numerator means that as we shrink the sport , we're making that spot brighter.

## Combining specular and diffuse

- Combined BRDF:
    - ![](../imgs/gpu_combined_specular_diffuse.png)


## Normalized specular helps your artists

- ![](../imgs/gpu_brdf_w_wo_norm.png)


## Metals vs. dielectrics

- Dielectrics have diffuse and specular reflections
    - Specular reflection is white
- Metals have purely specular reflections
    - specular reflection may be non-white
        - particularly if you're looking at them head on
    - Still white at large grazing angles.

## Fresnel effect

- Specular reflections increase dramatically at high grazing angles
- Schlick aporoximation:
    - F(V,H) = F₀ + (1-F₀)(1-***V***·H)⁵ 
        - = F₀ + (1-F₀)(1-***L***·H)⁵
    - F₀ : reflection when view and ligth vector align ( grey for dielectrics, but metals can have color )
    - since H is the half vector of L and V,  V·H == L·H
    - ( 1 - L·H )⁵ this gives us a really aggressive slope off near the edge.  Essentially this becomes an interpolation factor. 
- one thing that's confusing is you'll often see a different formulation used here 
    - F₀ + (1-F₀)(1-***n***·H)⁵
    - indead of `V·H` you see `n·V`
    - this is a special form of the fresnel effect that you use for global illumination effects where you know where the camera is and you have a normal vector associated with your surface, but the lights coming from all over in some sense , you don't really have an L vector that you can use.


## F₀ for dielectrics(linear)

- here are some example of F₀ for various dielectrics.
    - ![](../imgs/gpu_f0_dielectrics.png)
    - these numbers are all not very big, and as a result a lot of game engines don't even really let you select this, it's just built into the shader code somewhere because these small little variations are hardly noticed.
    - ![](../imgs/gpu_f0_dielectric_unity.png)
- Remember specular reflection of dielectrics is white.


## F₀ for metals (linear)

- ![](../imgs/gpu_f0_metal.png)

## Incorporating Fresnel term

- ![](../imgs/gpu_brdf_plus_fresnel.png)
- we're not really going to use this expression anyway because we'd like to take a few more steps and do something a little more complicated.

## A reflective paradox ?

- ![](../imgs/gpu_reflective_paradox.png)
- it's particularly weird here because this road is black asphalt, and it's been raining so there is water on top and you would expect the main issus is that there's water on it and the sun is reflecting off of the water.
    - now what's weird about his is that F₀ is actually higher for the asphalt that it is for the water.
    - so it makes you wonder why are the puddles reflecting more than the places without puddles.
    - well all of thing being equal, it would, the asphalt would be more reflective than the water, but the main difference here is that the water will pool and form smooth surfaces whereas the asphalt is fairly rough. So we're getting strong reflections off of the water even though the water technically has a lower F₀ , because those surfaces are smoother than the surfaces formed by the asphalt.
    - so we would like to take this effect into account.
    - ![](../imgs/gpu_roughness_blurry.png)

## General Cook-Torrance specular

- ![](../imgs/gpu_general_cook_torrance_specular.png)
    - G(n,L,V) the geometric term
    - D(n·H)  the distribution term
        - this is the term that encapsulates the effect we saw on the slide about the asphalt and the water. 
        - it's something that is parameterized by smoothness.
        - one term we might use is the following modified blinn-phong term.


## Blinn-Phong microfacet distribution

- Microfacet Blinn-Phong
    - ![](../imgs/gpu_blinn_phong_microfacet_distribution.png)
- Throughout rest of slides , imagine the artist makes "smoothness maps" containing "gloss" *g* in the range [0,1]
- Call of Duty: Black Ops 
    - s = 8192<sup>g</sup> = 2<sup>(13g)</sup>
- But it turns out people tend not to use this modified blinn-phong that much anymore anyway. 
    - A different *g* called GGX has become much more popular and is pretty much the dominant distribution term that you'll see in cook-torrance specular models and in modern game engines.

## GGX microfacet distribution 

- GGX:
    - ![](../imgs/gpu_ggx_distribution.png)
    - α: roughness parameter. Artists do not like to think in terms of roughness they like to think in terms of smoothness.
- Crytex:  α = (1-0.7g)²
- Unreal: α = (disney roughness)² = (1-g)²
- objects tended to have a much quicker fall off right around the peak, and then very long tails that will go out a lot further than you could get from the modified blinn-phong model.
    - ![](../imgs/gpu_shape_blinnmod_vs_ggx.png)
    - so you've got narrower tighter spots but a very wide dim helo around it. 


## The geometric term 

- The last thing we need to look at is the *g* term.
    - ![](../imgs/gpu_g_term_1.png)
    - *g* term is trying to deal with the effect that variation of height has both blocking light coming in and blocking light that's trying to come out.
    - Now the kind of effectes we're talking about here are at an even smaller level than the kinds of effects we're trying to achieve with normal maps. This is trying to capture the effects of roughness variations that you couldn't see with the naked eye.


## Original Cook-Torrance geometric term

- From original Cook-Torrance paper:
    - ![](../imgs/gpu_original_g_term.png)
    - there is no roughness parameter α here

## GGX-based geometric term 

- ![](../imgs/gpu_ggx_g_term.png)
    - it is expressed in this form of factors:  <sub>GGX-R</sub>(n·L) and G<sub>GGX-R</sub>(n·V)
    - the 2nd equation is the core formula to expand the factors.
- Used in The Order: 1886
    - I haven't seen this particular full ggx form used in very many games.
- Ideal of a "visualization" term:
    - ![](../imgs/gpu_ggx_g_term_cancelled.png)
    - 4(n·L)(n·V) is cancelled
    - but the square root does potentially take a while to compute. So maybe we would want to come up with a variation that doesn't require that square root.

## GGX-matched to GGX geometric term

- GGX-form matched to GGX distribution
    - ![](../imgs/gpu_ggx_matched_g_term.png)
- Disney standard: k = α/2 = (g-1)²/2
- Disney "hotness remapping": k = [0.5 + (1-g)/2]²/2

## Implicit geometric term

- Now imagine for a second that you picked this geometric term
    - G<sub>I</sub>(n,L,V) = 4(n·L)(n·V)
        - there is no reason why you might expect that to be useful.
        - but it just happens that if you plug that in for you actual *g* and divide by the `4(n·L)(n·V)`
    - Viz<sub>I</sub>(n,L,V) = G<sub>I</sub>(n,L,V) /( 4(n·L)(n·V) ) = 1
- If you're on a resource limited platform you might want to use this Kelemen geometric term.

## Kelemen Geometric term

- Facilitates fast implementation:
    - ![](../imgs/gpu_kelemen_g_term.png)
    - which gives you something that's decent looking but very importantly it's easy to compute.












