...menustart

- [CELLULAR TEXTURING](#eb512174cb9eab61d18d2b32ac10d757)
    - [THE NEW BASES](#d69d9e02dafa3af0d24ce1601f70a74f)
    - [IMPLEMENTATION STRATEGY](#281ce9a8a2a4d6b847c885aeadb20d87)
        - [Dicing Space](#4edf7eb38d47853aa36e3402b93cf234)
        - [Neighbor Testing](#fa5e753bb6b23904853dbf0639e6201a)
        - [The Subtle Population Table](#46504218a9420f71f7daaed533bed27a)

...menuend


<h2 id="eb512174cb9eab61d18d2b32ac10d757"></h2>


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



<h2 id="d69d9e02dafa3af0d24ce1601f70a74f"></h2>


## THE NEW BASES

The cellular texturing basis functions are based on the fundamental idea of randomly scattering “feature points” throughout 3D space , and building a scalar function based on the distribution of the points near the sample location. 

For any location x, there is some feature point that lies closer to x than any other feature point.  Define F₁(x) as the distance from x to that closest feature point. Figure 4.1 shows an example of this in 2D. 

![](../imgs/TM_F4.1.png) 

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

![](../imgs/TM_F4.2.png) 

> FIGURE 4.2 Gradient-mapped samples of F₁, F₂, F₃, and F₂ − F₁.

Much more interesting behavior begins when we examine F₂ and F₃. These have more rapid changes and internal structure and are slightly more visually interesting. 

These two can be directly mapped into colors and bumps, but they can also produce even more interesting patterns by forming linear combinations with each other.  For example, since F₂ ≥ F₁ for all x, the function F₂(x) − F₁(x) is well defined and very interesting, as shown in the bottom right of the figure. This combination has a value of 0 where F₁ = F₂, which occurs at the Voronoi boundaries. 

F₄ and other high **n** start looking similar, but the lower values of n (up to 4) are quite interesting and distinct.  More importantly, linear combinations of these F<sub>n</sub> have more “character” than the plain F<sub>n</sub> , particularly differences of two or more simple bases. 

Figure 4.3 shows 20 sample surfaces that are all just examples of combinations of these low-n basis functions.

![](../imgs/TM_F4.3.png) 

> FIGURE 4.3 A variety of example appearances formed by linear combinations of the F<sub>n</sub>  functions.

These patterns are interesting and useful, but we can also use the basis functions to make *fractal* versions, much like noise is used to produce fractal noise. By computing multiple “scales” of the function at different weights and scaling factors, a more visually complex appearance can be made. 

This is a simple loop, computing a function G<sub>n</sub> = Σ 2⁻ⁱF<sub>n</sub>(2ⁱx) for moderate ranges of i (i = 0–5), and using G<sub>n</sub> as the index for colors and bumps.

The fractal versions of any of the basic basis function combinations become extremely appealing. Figure 4.4 shows a fractal version of F₁ forming the spotted pattern and bumps on the hide of a creature.

![](../imgs/TM_F4.4.png) 

> FIGURE 4.4 Natural-looking reptile hide using fractal-versions of the F<sub>n</sub> functions.

Fractal noise is used for the tongue, and a linear gradient is applied to the main body for color variation. 

Other fractal versions of primitives are shown in the row of cut tori in Figure 4.5.

![](../imgs/TM_F4.5.png) 

> FIGURE 4.5 More examples of fractal combinations.

The fractal version of F₁ is perhaps the most useful.

Applied solely as a bump map, the surface becomes crumpled like paper or tinfoil.  This surface has been extremely popular with artists as a way to break up a smooth surface, providing a subtle roughening with an appearance unlike fractal noise bumps.

A surprising discovery was that a reflective, bumped-map plane with this “crumple” appearance bears an excellent resemblance to seawater, as shown in Figure 4.6. This bump-only fractal texture has become extremely popular in many renderers.

![](../imgs/TM_F4.6.png) 

> FIGURE 4.6 Sea surface formed from bump-mapped fractal F₁ functions.

Since the cellular texture is a family of bases, it’s fun to try more advanced incestuous combinations!  Nonlinear combinations of simple polynomial products such as F₁F₂ or F₃² − F₂² are also interesting and useful texture bases.  Again, renormalizing by empirically testing the output range makes the new basis easier to apply to color maps.

If the F₁ function returns a unique ID number to represent the closest feature point’s identity, this number can be used to form features that are constant over a cell, for example, to shade the entire cell a single constant color. When combined with bumping based on F₂ − F₁, quite interesting flagstonelike surfaces can be easily generated.  Figure 4.7 shows this technique, which also uses fractal noise discoloration in each cell. 

![](../imgs/TM_F4.7.png) 

> FIGURE 4.7 3D flagstone texture shows Voronoi cells.

Bump mapping of the flagstonelike areas is particularly effective, and it is cheap to add since the gradient of F<sub>n</sub> is just the radial unit vector pointing away from the appropriate feature point toward the sample location.

<h2 id="281ce9a8a2a4d6b847c885aeadb20d87"></h2>


## IMPLEMENTATION STRATEGY

It’s not necessary to understand how to implement the cellular texture basis function in order to use it. 

But more than noise, the basis seems to encourage modifications and adaptations of the main algorithm to produce new effects, often with a very different behavior than the original version.

The following sections describe my implementation method, hopefully to allow you to modify it to make your own alternatives. 

The first step is to define how feature points are spread through space. The density and distribution of points will change the character of the basis functions.

Our first assumption is that we want an *isotropic* function, to avoid any underlying pattern aligned with the world’s axes. A simple idea like adding a point at every integer gridpoint and jittering their locations is easy to implement, but that underlying grid will bias the pattern, and it will be easy to see that “array” point layout.

The correct way to eliminate this bias is to keep the idea of splitting space into cubes, but choosing the number of points inside each cube in a way that will completely obscure the underlying cube pattern. We’ll analyze this separately later.

<h2 id="4edf7eb38d47853aa36e3402b93cf234"></h2>


### Dicing Space

Since space will be filled with an infinite number of feature points, we need to be able to generate and test just a limited region of space at a time. The easiest way to do this is to dice space into cubes and deal with feature points inside each cube. This allows us to look at the points near our sample by examining the cube that the sample location is in plus the immediate neighbor cubes.  An example is shown in Figure 4.8

![](../imgs/TM_F4.8.png) 

> FIGURE 4.8 Searching for local feature points in neighboring cubes of space.

where the “X” marks our sample location and dots show feature points in each cube. We can ignore the more distant cubes as long as we’re assured that the feature points will lie within the 3 × 3 grid of local cubes.

Each “cube” in space can be uniquely represented by its integer coordinates, and by simple floor operations we can determine, for example, that a point like (1.2, 3.33, 2.3) lies within the cube indexed by (1, 3, 2).

Now we determine how many and where feature points lie inside this cube. The “random” number we use to determine the number of points in a cube obviously must be unique to that cube and reproducible at need. There is a similar requirement in the noise function, which also uses a cubic lattice with fixed values associated with each gridpoint. We also need this seed to generate the location of the feature points themselves.

The solution to this problem is to hash the three integer coordinates of a cube into a single 32-bit integer that is used as the seed for a fast random number generator.  This is easy to compute as something like `702395077x + 915488749y + 2120969693z mod 2³²`.  The constants are random but chosen to be odd, and not simple multiples of each other. Like linear congruential random number generators, the low-order bits of this seed value are not very random.

We compute the number of points in the cube using this seed to pick a value from a short lookup table of 256 possibilities.  This hardwired array of possible point populations is carefully precomputed (as described on page 145) to give us the “keep the points isotropic” magic property we desire.  We use the high-order bits from our seed to index into the table to decide how many feature points to add into the cube. Since our table is a nice length of 256, we can just use the eight high-order bits of the seed value to get the index.

<h2 id="fa5e753bb6b23904853dbf0639e6201a"></h2>


### Neighbor Testing

Next, we compute the locations of the *m* feature points inside the sample cube. 

Again, these are values that are random, but fixed for each cube. We use the already initialized random number generator to compute the XYZ locations of each of the feature points. These coordinates are relative to the base of the cube and always range from 0 to 1 for each coordinate.

As we generate each point, we compute its distance to the original function evaluation location and keep a sorted list of the n smallest distances we’ve seen so far.  As we test each point in turn, we effectively do an ***insertion sort*** to include the new point in the current list.  

This procedure finds the closest feature points and the values of F₁ to F<sub>n</sub> for the points within the current cube of space (the one that contains the hit point). However, the feature points within a neighboring cube could quite possibly contain a feature point even closer than the ones we have found already, so we must iterate among the boundary cubes too.  We could just test all 26 immediate neighboring cubes, but by checking the closest distance we’ve computed so far (our tentative nth closest feature distance) we can throw out whole rows of cubes at once by deciding when no point in the neighbor cube could possibly contribute to our list.

Figure 4.9 shows this elimination in a 2D example. 

![](../imgs/TM_F4.9.png) 

> FIGURE 4.9 We don’t need to test neighbor cubes that are too distant.

The central cube has three feature points. We compute F₁ based on the feature point closest to the sample location (marked by “X”). 

We don’t know yet what points are in the adjoining cubes marked by “?,” but if we examine a circle of radius F₁, we can see that it’s possible that the cubes labeled A, B, and C *might* contribute a closer feature point, so we have to check them.  

If we want to make sure our computation of F₂ is accurate, we have to look at a larger circle and additionally test cubes D and E. 

In practice, we can make these decisions quickly since it’s easy to compare the current F distance to the distance of the neighbor cubes (especially since we can just compare the squared distances, which are faster to compute).

This kind of analysis also shows us that we need ***sufficient feature point density*** to make sure that one layer of neighbor cubes is enough to guarantee that we’ve found the closest point. We ***could*** start checking cubes that are even more distant neighbors, but that becomes more and more expensive. Checking all neighbors requires at most 3³=27 cubes, but including more distant neighbors 2 cubes away would need 5³=125 cubes.

After we’ve checked all of the necessary neighbors, we’ve finished computing our values of F. If we computed Fn, we were effectively finding values for all F₁, F₂ , . . . , F<sub>n</sub> simultaneously, which is very convenient. 

<h2 id="46504218a9420f71f7daaed533bed27a"></h2>


### The Subtle Population Table

The desire for an isotropic distribution of points in space requires careful design. It can be done by choosing the number of points in each cube randomly but using a **Poisson 泊松 distribution**. 

This distribution gives the probability of finding a specific number of points in a region when given a mean density. 

There may be more or less than this expected number of points in the region; the exact probabilities of any number of points in a region can be computed by using the discrete Poisson distribution function.

If we generate the points inside of each cube randomly, with the population based on the Poisson probabilities, the feature points will be truly isotropic and the texture function will have no grid bias at all.

Each cube in space may contain zero, one, or more feature points. We determine this on the fly quite simply by noting that the Poisson random distribution function describes the exact probabilities of each of the possible number of feature points occurring in the cube. 
