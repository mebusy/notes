
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




> FIGURE 4.2 Gradient-mapped samples of F₁, F₂, F₃, and F₂ − F₁.




