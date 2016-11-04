
# Textuer and Modeling

# Renderman Shading Language

```
$ renderdl -v

```

Hello world shader: 

```
surface helloWorld() {
	Oi = Os ; 
	Ci = Oi * Cs ;
}
```

 - Oi : output opacity ?
 - Os : input opacity 
 - Ci : output color
 - Cs : intput color

Compile the shader :

```
$ shaderdl -h
$ shaderdl -d bin src/helloWorld.sl
```

RIB file:  a file that will define the scene.

create rib file :  rib/sphere.rib    (TODO)

render :

```
$ renderdl rib/sphere.rib
```

enhance 

```
surface helloWorld( 
		uniform float Kd = 1;
	) {

	// Local Variables
	normal Nn = normalize(N) ;

	Oi = Os ; 
	Ci = Oi * Cs * ( Kd * diffuse(Nn) );
}
```

 - N is the normal vector

recompile & render !


Use a Makefile: 

```makefile
all: render

compile:
	shaderdl -d bin src/helloWorld.sl

render: compile
	renderdl rib/sphere.rib
```

enhance  again

```
surface helloWorld( 
		uniform float Kd = 1;
		uniform float Ks = 1;
		uniform float roughness = 0.15 ;
		color specularColor = color(1) ;
	) {

	// Local Variables
	normal Nn = normalize(N) ;
	vector V = -normalize(I) ;

	Oi = Os ; 
	Ci = Oi * Cs * (( Kd * diffuse(Nn) ) + (Ks * specular( Nn, V, roughness ) * specularColor ) )  ;
}
```

 - I : the vector that is coming from the camera all the way to the surface



# CHAPTER 2  BUILDING PROCEDURAL TEXTURES

## INTRODUCTION

Throughout the short history of computer graphics, researchers have sought to improve the realism of their synthetic images by finding better ways to render the appearance of surfaces. This work can be divided into *shading* and *texturing*.

 - Shading is the process of calculating the color of a pixel or shading sample from user-specified surface properties and the shading model. 
 - Texturing is a method of varying the surface properties from point to point in order to give the appearance of surface detail that is not actually present in the geometry of the surface.

Shading models (sometimes called illumination models, lighting models, or reflection models) simulate the interaction of light with surface materials. Shading models are usually based on physics, but they always make a great number of simplifying assumptions. Fully detailed physical models would be overkill for most computer graphics purposes and would involve intractable calculations.

The simplest realistic shading model, and the one that was used first in computer graphics, is the diffuse model, sometimes called the Lambertian model. A diffuse surface has a dull or matte appearance. 

All of the shading models described above are so-called local models, which deal only with light arriving at the surface directly from light sources. In the early 1980s, most research on shading models turned to the problem of simulating global illumination effects, which result from indirect lighting due to reflection, refraction, and scattering of light from other surfaces or participating media in the scene. Raytracing and radiosity techniques typically are used to simulate global illumination effects.

## PROCEDURAL PATTERN GENERATION

Most surface shaders can be split into two components called *pattern generation* and the *shading model*.

 - Pattern generation defines the texture pattern and sets the values of surface properties that are used by the shading model. 
 - Shading model simulates the behavior of the surface material with respect to diffuse and specular re- flection.

## Shading Models

Most surface shaders use one of a small number of shading models. The most common model includes diffuse and specular reflection and is called the “plastic” shading model. It is expressed in the RenderMan shading language as follows:

```
surface
plastic(float Ka = 1, Kd = 0.5, Ks = 0.5;
float roughness = 0.1;
color specularcolor = color (1,1,1))
{
	point Nf = faceforward(normalize(N), I); 
	point V = normalize(-I);
	Oi = Os;
	Ci = Os * (Cs * (Ka * ambient()
		+ Kd * diffuse(Nf)) 
		+ specularcolor * Ks
			* specular(Nf, V, roughness));
}
```

 - Colors are represented by RGB triples ， 0 ~ 1
 - Any RenderMan surface shader can reference a large collection of built-in quan- tities , such as
 	- P , the 3D coordinates of the point on the surface being shaded
 	- N , the surface normal at P
 		- Because surfaces can be two-sided, it is possible to see the inside of a surface; 
 		- in that case we want the normal vector to point toward the camera, not away from it.
 	- I , the vector from the camera position to the point P	
 	- built-in function *faceforward* ,  simply compares I with N 
 		- Flip N so that it faces in the direction opposite to I,
 		- If the two vectors I and N point in the same direction (i.e., if their dot product is positive), faceforward returns -N instead of N.
 - The first statement declares and initializes a surface normal vector Nf
 	- which is normalized and faces toward the camera
 - The second statement declares and initializes a vector V that is normalized and gives the direction to the camera.
 - The third statement sets the output opacity `Oi` to be equal to the input surface opacity `Os`
 - Actually, `Os` is color type,  For an opaque surface, `Os` is color(1,1,1).
 - The final statement in the shader does the interesting work
 	- The output color `Ci` is set to the product of the opacity and a color. 
 	- The color is the sum of an ambient term and a diffuse term multiplied by the input surface color `Cs` , added to a specular term whose color is determined by the parameter *specularcolor*
 - The built-in functions *ambient*, *diffuse*, and *specular* gather up all of the light from multiple light sources according to a particular reflection model. 
 	- diffuse computes the sum of the intensity of each light source multiplied by the dot product of the direction to the light source and the surface normal Nf (which is passed as a parameter to diffuse).


The plastic shading model is flexible enough to include the other two most com- mon RenderMan shading models, the “matte” model and the “metal” model, as special cases. 

 - The matte model is a perfectly diffuse reflector, which is equivalent to plastic with a Kd of 1 and a Ks of 0. ( 没有高光反射 )
 - The metal model is a perfectly specular reflector ， which is equivalent to plastic with a Kd of 0, a Ks of 1, and a specularcolor the same as Cs.
 	- specularcolor parameter is important ， For example, gold has a gold-colored highlight.

The plastic shader is a good starting point for many procedural texture shaders. We will simply replace the Cs in the last statement of the shader with a new color variable Ct, the texture color that is computed by the pattern generation part of the shader.

## Pattern Generation

 - usually the hard part

If the texture pattern is simply an image texture, the shader can call the built-in function *texture*:

```
Ct = texture(“name.tx”,s,t);
```

 - texture function looks up pixel values from the specified image texture “name.tx” and performs filtering calculations as needed to prevent aliasing artifacts.
 - texture function has the usual 2D texture space with the texture image in the unit square.
 - built-in variables *s* and *t* are the standard RenderMan texture coordinates range over the interval [0, 1] , 

The shading language also provides an *environment* function whose 2D texture space is accessed using a 3D direction vector that is converted internally into 2D form to access a latitude-longitude or cube-face environment map.


## Texture Spaces

The RenderMan shading language provides many different built-in coordinate systems (also called *spaces*). 

A coordinate system is defined by the concatenated stack of transformation matrices that is in effect at a given point in the hierarchical structure of the RenderMan geometric model.

 - current space
 	- the one in which shading calculations are normally done.
 	- In most renderers, current space will turn out to be either *camera* space or *world* space, but you shouldn’t depend on this.
 - world space 
 	- the coordinate system in which the overall layout of your scene is defined. 
 	- It is the starting point for all other spaces.
 - object space 
 	- the one in which the surface being shaded was defined
 	- For instance, if the shader is shading a sphere, the object space of the sphere is the coordinate system that was in effect when the *RiSphere* call was made to create the sphere. 
 	- Note that an object made up of several surfaces all using the same shader might have different object spaces for each of the surfaces if there are geometric transformations between the surfaces.
 - shader space
 	- the coordinate system that existed when the shader was invoked (e.g., by an *RiSurface* call). 
 	- This is a very useful space because it can be attached to a user-defined collection of surfaces at an appropriate point in the hierarchy of the geometric model so that all of the related surfaces share the same shader space.

In addition, user-defined coordinate systems can be created and given names using the *RiCoordinateSystem* call. These coordinate systems can be referenced by name in the shading language.

It is very important to choose the right texture space when defining your texture.

Using the 2D surface texture coordinates (s, t) or the surface parameters (u, v) is fairly safe, but might cause problems due to nonuniformities in the scale of the parameter space (e.g., compression of the parameter space at the poles of a sphere). Solid textures avoid that problem because they are defined in terms of the 3D coordinates of the sample point.  If a solid texture is based on the *camera* space coordinates of the point , the texture on a surface will change whenever either the camera or the object is moved. If the texture is based on world space coordinates, it will change whenever the object is moved.  In most cases, solid textures should be based on the shader space coordinates of the shading samples, so that the texture will move properly with the object.  The shader space is defined when the shader is invoked, and that can be done at a suitable place in the transformation hierarchy of the model so that everything works out.

It is a simplification to say that a texture is defined in terms of a single texture space. In general a texture is a combination of a number of separate “features,” each of which might be defined in terms of its own *feature* space. If the various feature spaces that are used in creating the texture are not based on one underlying texture space, great care must be exercised to be sure that texture features don’t shift with respect to one another. The feature spaces should have a fixed relationship that doesn’t change when the camera or the object moves.

## Layering and Composition

The best approach to writing a complex texture pattern generator is to build it up from simple parts. There are a number of ways to combine simple patterns to make complex patterns.

One technique is *layering*, in which simple patterns are placed on top of one another. 

For example, the colors of two texture layers could be added together. Usually, it is better to have some texture function control how the layers are combined. The *mix* function is a convenient way of doing this.

```
C = mix(C0, C1, f);
```

 - The number f, between 0 and 1, is used to select one of the colors C0 and C1
 - If f is 0, the result of themixisC0
 - If f is 1, the result isC1
 - If f is between 0 and 1, the re- sult is a linearly interpolated mixture of C0 and C1


```
color
mix(color C0, color Cl, float f) {
	return (1-f) * C0 + f * Cl;
}
```

When two colors are multiplied together in the shading language, the result is a color , whose RGB components are the product of the corresponding components from the input colors. Color multiplication can simulate the ***filtering*** of one color by the other. If color C0 represents the transparency of a filter to red, green, and blue light, then C0*C1 represents the color C1 as viewed through the filter.

Be careful when using a four-channel image texture that was created from an RGBA image (an image with an opacity or “alpha” channel) because the colors in such an image are normally premultiplied by the value of the alpha channel. In this case, it is not correct simply to combine the RGB channels with another color under control of the alpha channel. The correct way to merge an RGBA texture over another texture color Ct is

```
color C; float A;
C = color texture(“mytexture”,s,t); 
A = texture(“mytexture”[3],s,t); 
result = C + (1-A) * Ct;
```

 - C is the image texture color, and A is the alpha channel of the image texture (channel number 3)
 - Since C has already been multiplied by A, the expression C + (1—A)*Ct is the right way to *lerp* between C and Ct.

Another way to combine simple functions to make complex functions is *functional composition*, using the outputs of one or more simple functions as the inputs of another function. Composition is very powerful and is so fundamental to programming that you really can’t avoid using it.


## Steps, Clamps, and Conditionals

function *step(a,x)* returns the value 0 when x is less than a and returns 1 otherwise.

```c
float
step(float a, float x) {
	return (float) (x >= a);
}
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_step.png)

The main use of the step function is to replace an if statement or to produce a sharp transition between one type of texture and another type of texture. For example, an if statement such as 

```
if (u < 0.5)
	Ci = color (1, 1, .5);
else
	Ci = color ( .5 , .3, 1);
```

can be rewritten to use the step function as follows:

```
Ci = mix(color (1,1,.5), color (.5,.3,1), step(0.5, u));
```

Later in this chapter when we examine antialiasing, you’ll learn how to create an antialiased version of the step function. Writing a procedural texture with a lot of if statements instead of step functions can make antialiasing much harder.

Two step functions can be used to make a rectangular pulse as follows:

```
#define PULSE(a,b,x) (step((a),(x)) - step((b),(x)))
```

This preprocessor macro generates a pulse that begins at x = a and ends at x = b.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_pulse.png)

function *clamp(x,a,b)* returns the value a when x is less than a, the value of x when x is between a and b, and the value b when x is greater than b. The clamp function can be written in C as follows:

```
float
clamp(float x, float a, float b) {
	return (x < a ? a: (x > b ? b : x));
}
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_clamp.png)

The well-known min and max functions are closely related to clamp. In fact, min and max can be written as clamp calls, as follows:

```
min(x, b) ≡ clamp(x, x, b)
max(x, a) ≡ clamp(x, a, x)
```

Alternatively, clamp can be expressed in terms of min and max:

```
clamp(x, a, b) ≡ min(max(x, a), b)
```

Another special conditional function is the *abs* function.

In addition to the “pure” or “sharp” conditionals step, clamp, min, max, and abs, RenderMan shading language provides a “smooth” conditional function called *smoothstep*. This function is similar to step, but instead of a sharp transition from 0 to 1 at a specified threshold, smoothstep(a,b,x) makes a gradual transition from 0 to 1 beginning at threshold a and ending at threshold b.  In order to do this, smoothstep contains a cubic function whose slope is 0 at a and b and whose value is 0 at a and 1 at b.  There is only one cubic function that has these properties for a = 0 and b = 1, namely, the function 3x² − 2x³. 

```
float
smoothstep(float a, float b, float x) {
	if (x < a) return 0;
	if (x >= b) return 1;
	x = (x - a)/(b - a); 
	return (x*x * (3 - 2*x));
}
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ML_smoothStep.png)


## Periodic Functions

The best-known periodic functions are sin and cos.  It can be shown that other functions can be built up from a sum of sinusoidal terms of different frequencies and phases.

Another important periodic function is the *mod* function. *mod(a,b)* gives the positive remainder obtained when dividing a by b.  C users beware! Although C has a built-in integer remainder operator “%” and math library functions fmod and fmodf for double and float numbers, all of these are really remainder functions, not modulus functions, in that they will return a negative result if the first operand, a, is negative.  Instead, you might use the following C implementation of mod:

```

float
mod(float a, float b) {
	int n = (int)(a/b); 
	a -= n*b;
	if (a < 0)
		a += b; 
	return a;
}
```

A graph of the periodic sawtooth function mod(x,a)/a is shown in Figure 2.14. This function has an amplitude of one and a period of a.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ML_mod_sawteech.png)

By applying mod to the inputs of some other function, we can make the other function periodic too. Take any function, say, f (x), defined on the interval from 0 to 1 (technically, on the half-open interval [0, 1]). Then f (mod(x,a)/a) is a periodic function.  To make this work out nicely, it is best if f(0) = f(1) and even better if the derivatives of f are also equal at 0 and 1. 

For example, the pulse function PULSE(0.4,0.6,x) can be combined with the mod function to get the periodic square wave function PULSE(0.4,0.6,mod(x,a)/a) with its period equal to a (see Figure 2.15).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ML_periodic_pulse.png)

It’s often preferable to use another mod-like idiom instead of mod in your shaders. We can think of xf = mod(a,b)/b as the fractional part of the ratio a/b.  In many cases it is useful to have the integer part of the ratio, xi, as well.

```
float xf, xi; 
xf = a/b;
xi = floor(xf); 
xf -= xi;
```

In C, the following macro is an alternative to the built-in floor function:

```
#define FLOOR(x) ((int)(x) - ((x) < 0 && (x) != (int)(x)))
```

FLOOR isn’t precisely the same as floor, because FLOOR returns a value of int type rather than double type.  Be sure that the argument passed to FLOOR is the name of a variable, since the macro may evaluate its argument up to four times.

A closely related function is the ceiling function ceil(x).  The following macro is an alternative to the C library function:

```
#define CEIL(x) ((int)(x) + ((x) > 0 && (x) != (int)(x)))
```

## Splines and Mappings

Built-in *spline* function is a one-dimensional Catmull-Rom interpolating spline through a set of so-called *knot* values. The parameter of the spline is a floating-point number.

```
result = spline(parameter,
		knotl, knot2, . . . , knotN-1, knotN);
```

In the shading language, the knots can be numbers, colors, or points (but all knots must be of the same type). The result has the same data type as the knots.   If parameter is 0, the result is knot2. If parameter is 1, the result is knotN-1.  For values of parameter between 0 and 1, the value of result interpolates smoothly between the values of the knots from **knot2** to **knotN-1**.  The knotl and knotN values determine the derivatives of the spline at its end points.  Because the spline is a cubic polynomial, there must be at least four knots.

Here is a C language implementation of spline in which the knots must be floating-point numbers:

```
/* Coefficients of basis matrix. */
#define CROO  -0.5
#define CR01   1.5
#define CR02  -1.5
#define CR03   0.5
#define CR10   1.0
#define CR11  -2.5
#define CR12   2.0
#define CR13  -0.5
#define CR20  -0.5
#define CR21   0.0
#define CR22   0.5
#define CR23   0.0
#define CR30   0.0
#define CR31   1.0
#define CR32   0.0
#define CR33   0.0

float
spline(float x, int nknots, float *knot) 
{
	int span;
	int nspans = nknots - 3;
	float cO, cl, c2, c3; /* coefficients of the cubic.*/ 
	if (nspans < 1){/* illegal */
		fprintf(stderr, “Spline has too few knots.\n”); 
		return 0;
	}
	/* Find the appropriate 4-point span of the spline. */ 
	x = clamp(x, 0, 1) * nspans;
	span = (int) x;
	if (span >= nknots - 3)
		span = nknots - 3; 
	x -= span;
	knot += span;
	
	/* Evaluate the span cubic at x using Horner’s rule. */
	c3 = CROO*knot[0] + CR01*knot[l] + CR02*knot[2] + CR03*knot[3]; 
	c2 = CR10*knot[0] + CRll*knot[l] + CR12*knot[2] + CR13*knot[3]; 
	cl = CR20*knot[0] + CR21*knot[l] + CR22*knot[2] + CR23*knot[3]; 
	cO = CR30*knot[0] + CR31*knot[l] + CR32*knot[2] + CR33*knot[3];

	return ((c3*x + c2)*x + cl)*x + cO;
}
```

A graph of a particular example of the spline function is shown in Figure 2.16.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TM_spline.png)

This code can easily be adapted to work with knots that are colors or points. Just do the same thing three times, once for each of the components of the knots. In
other words,

```
spline(parameter, (xl,yl,zl), . . . , (xN,yN,zN))
```

is exactly equivalent to

```
( spline(parameter, xl, . . . , xN), 
  spline(parameter, yl, . . . , yN), 
  spline(parameter, zl, . . . , zN) )
```

The spline function is used to map a number into another number or into a color.  A spline can approximate any function on the [0, 1] interval by giving values of the function at equally spaced sample points as the knots of the spline. In other words, the spline can interpolate function values from a table of known values at equally spaced values of the input parameter. A spline with colors as knots can be used as a *color map* or *color table*.

An example of this technique is a shader that simulates a shiny metallic surface by a procedural reflection map texture. The shader computes the reflection direction R of the viewer vector V. The vertical component of R in world space is used to look up a color value in a spline that goes from brown earth color below to pale bluish-white at the horizon and then to deeper shades of blue in the sky. Note that the shading language’s built-in *vtransform* function properly converts a direction vector from the current rendering space to another coordinate system specified by name.

```
#define BROWN color (0.1307,0.0609,0.0355) 
#define BLUEO color (0.4274,0.5880,0.9347) 
#define BLUE1 color (0.1221,0.3794,0.9347) 
#define BLUE2 color (0.1090,0.3386,0.8342) 
#define BLUES color (0.0643,0.2571,0.6734) 
#define BLUE4 color (0.0513,0.2053,0.5377) 
#define BLUES color (0.0326,0.1591,0.4322) 
#define BLACK color (0,0,0)

surface 
metallic( ) {
	point Nf = normalize(faceforward(N, I)); V = normalize(-I);
	point V = normalize(-I);
	point R; /* reflection direction */
	point Rworld; /* R in world space */
	color Ct;
	float altitude;

	R = 2 * Nf * (Nf . V ) - V ; 
	Rworld = normalize(vtransform(“world”, R)); 
	altitude = 0.5 * zcomp(Rworld) + 0.5;
	Ct = spline(altitude,
			BROWN, BROWN, BROWN, BROWN, BROWN, 
			BROWN, BLUEO, BLUE1, BLUE2, BLUES, 
			BLUE4, BLUES, BLACK);
	Oi = Os;
	Ci = Os * Cs * Ct;
}
```



Figure 2.17 is an image shaded with the metallic reflection map shader.












