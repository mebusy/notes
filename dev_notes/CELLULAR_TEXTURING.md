
# CELLULAR TEXTURING

Procedural texturing uses fractal noise extensively. 

This book has multiple chapters that are virtually subtitled “More Applications of Fractal Noise.” The major reason for this popularity is that noise is very *versatile*.

While there are infinitely many functions that can be computed from an input location, noise’s random (but controlled) behavior gives a much more interesting appearance than simple gradients or mixtures of sines.

This simple functional nature of noise makes it an adaptable tool that you might call a texture “basis” function. 

This brings us to the introduction of new basis functions based on *cellular texturing*. 

Cellular texturing is related to randomly distributed discrete features spread through space. 

 - Noise has a “discoloration” 变色 or “mountain range” 山脉 kind of feeling. 
 - Cellular textures evoke more of a “sponge 海绵,”  “lizard scales 蜥蜴鳞,” “pebbles 鹅卵石,” or “flagstones 石板” feeling.

They often split space into small, randomly tiled regions , called cells. Even though these regions are discrete, the cellular basis function itself is continuous and can be evaluated anywhere in space.



## THE NEW BASES

The cellular texturing basis functions are based on the fundamental idea of randomly scattering “feature points” throughout 3D space , and building a scalar function based on the distribution of the points near the sample location. 

For any location x, there is some feature point that lies closer to x than any other feature point.  Define F₁(x) as the distance from x to that closest feature point. Figure 4.1 shows an example of this in 2D. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_F4.1.png) 

> FIGURE 4.1 F*n* values are the distance to the *n*th closest feature point.

As x varies, F₁ varies continuously as the distance *between the sample location and the fixed feature point* varies.

It’s still continuous even when the calculation “switches” from one feature point to its neighbor that has now become the closest. The *derivative* of F₁ will change discontinuously at these boundaries when the two feature points are equidistant from the sample location.

These locations where the function F₁ “switches” from one feature point to the next (where its derivative is discontinuous) are along the equidistance planes 等距离平面 that separate two points in 3D space. These planes are exactly the planes that are computed by a ***Voronoi*** diagram, a partition of space into cellular regions.

The function F₂(x) can be defined as the distance between the location x and the feature point that is the second closest to x. Similarly, we can define F<sub>n</sub>(x) as the distance between x and the *n*th closest feature point.

The functions F have some interesting properties.

 - F<sub>n</sub> are always continuous
 - F<sub>n</sub> are always nondecreasing ; 0 ≤ F₁(x) ≤ F₂(x) ≤ F₃(x).
 	- In general, F<sub>n</sub>(x) ≤ F<sub>n+1</sub>(x) by the definition of F<sub>n</sub>. 
 - The gradient of F<sub>n</sub> is simply the unit direction vector from the nth closest feature point to x.

These careful definitions are very useful when we want to start making interesting textures. Mapping values of the function into a color and normal displacement can produce visually interesting and impressive effects. In the simplest case, F₁(x) can be mapped into a color spline and bump. The character of F₁ is very simple, since the function increases radially around each feature point. Thus, mapping a color to small values of F₁ will cause a surface texture to place spots around each feature point -— polka dots! Figure 4.2 shows this radial behavior in the upper left.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_F4.2.png) 

> FIGURE 4.2 Gradient-mapped samples of F₁, F₂, F₃, and F₂ − F₁.

Much more interesting behavior begins when we examine F₂ and F₃. These have more rapid changes and internal structure and are slightly more visually interesting. 

These two can be directly mapped into colors and bumps, but they can also produce even more interesting patterns by forming linear combinations with each other.  For example, since F₂ ≥ F₁ for all x, the function F₂(x) − F₁(x) is well defined and very interesting, as shown in the bottom right of the figure. This combination has a value of 0 where F₁ = F₂, which occurs at the Voronoi boundaries. 

F₄ and other high **n** start looking similar, but the lower values of n (up to 4) are quite interesting and distinct.  More importantly, linear combinations of these F<sub>n</sub> have more “character” than the plain F<sub>n</sub> , particularly differences of two or more simple bases. 

Figure 4.3 shows 20 sample surfaces that are all just examples of combinations of these low-n basis functions.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_F4.3.png) 

> FIGURE 4.3 A variety of example appearances formed by linear combinations of the F<sub>n</sub>  functions.

These patterns are interesting and useful, but we can also use the basis functions to make *fractal* versions, much like noise is used to produce fractal noise. By computing multiple “scales” of the function at different weights and scaling factors, a more visually complex appearance can be made. 

This is a simple loop, computing a function G<sub>n</sub> = Σ 2⁻ⁱF<sub>n</sub>(2ⁱx) for moderate ranges of i (i = 0–5), and using G<sub>n</sub> as the index for colors and bumps.

The fractal versions of any of the basic basis function combinations become extremely appealing. Figure 4.4 shows a fractal version of F₁ forming the spotted pattern and bumps on the hide of a creature.



FIGURE 4.4 Natural-looking reptile hide using fractal-versions of the F<sub>n</sub> functions.

Fractal noise is used for the tongue, and a linear gradient is applied to the main body for color variation. Other fractal versions of primitives are shown in the row of cut tori in Figure 4.5.




