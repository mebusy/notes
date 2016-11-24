
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


> FIGURE 4.1 F*n* values are the distance to the *n*th closest feature point.