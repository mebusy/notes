
# Multivariable Calculus

```bash
f(x,y) = x² + y
f(x,y) = |3x|
         |2y|
```

The convention is to usually think if there's multiple numbers that go into the output,  think of it as a vector.

It would probably be more accurate to call it multidimensional calculus. Because, instead of thinking of 2 separate entities, whenever you see 2 things like that,  you're gonna be thinking about the x-y plane. And thinking about just a single point.

**And you'd think of this as a function that takes a point to a number, or a point to a vector.**



## Vector Fields

This concept comes up all the time in multivariable calculus, and that's probably because they come up all the time in physics.

- What is vector field ?
    - It is pretty much a way of visualizing functions that have the same number of dimensions in their input as in their output.

```bash
f(x,y) = |y³-9y|
         |x³-9x|
```

So if you imagin trying to visualize a function like this, it would be really hard because you somehow to visualize this thing in four dimensions.

So instead what we do, we look only in the input space, x-y plane. And for each individual input point, for example (1,2), I'm gonna consider the vector that it outputs and attach that vector to the point.

- ![](../imgs/mc_vector_field_0.png)

This is a really big vector.  If we draw a whole bunch of diffrent points and see what vectors attach to them, this would be a real mess.  So instead we scale them down, this is common.

- ![](../imgs/mc_vector_field_1.png)

You're kind of lying about what the vectors themselves are, but you get a much better feel for what each thing corresponds to. 

And another thing about this drawing that's not entirely faithful to the original function that we have  is that all of these vectors are the same length. This is kind of common practice when vector fields are drawn. There are ways of getting around this, one way is just use colors with your vectors. 

- ![](../imgs/mc_vector_field_2.png)

Here the color is used to give a hint of length.

Another thing you can do is cale them to be roughly proportional to what they should be. 

- ![](../imgs/mc_vector_field_3.png)

```bash
           |x|
f(x,y,z) = |y|
           |z|
```

- ![](../imgs/mc_vector_field_4.png)


## Transformations

```bash
         |3cos(t)+cos(t)cos(s)|
f(t,s) = |3sin(t)+sin(t)cos(s)|
         |        sin(s)      |
```

- ![](../imgs/mc_transform_0.png)


How you might think of this **torus**  as a transformation ?

First let me just get straight what the input space here is.  You could think the input space as the entire t-s plance.

- ![](../imgs/mc_transform_1.png) ![](../imgs/mc_transform_2.png)

So what we can do is think about this portion of t-s plane as living inside 3-D space as a sort of cheating...


- ![](../imgs/mc_transform_3.png) ![](../imgs/mc_transform_4.png) ![](../imgs/mc_transform_5.png) ![](../imgs/mc_transform_6.png) ![](../imgs/mc_transform_7.png) ![](../imgs/mc_transform_8.png)

The general idea of starting with a square and somehow warping that  is acutally a pretty powerful thought. 

And as we get into multi variable calculus and you start thinking a little more deeply about surfaces, I think it really helps if you think about a slight little movement on your input space, what happens to that tiny little movement, or that tiny little traversal, what it looks like if you do that same movement somewhere on the output space.


## Partial derivatives

```
f(x,y) = x²y + sin(y)
```

∂f/∂x 

∂f/∂y

why do we call these partical derivatives? It's sort of like, this doesn't tell the full story of how F changes cause it only cares about the x/y direction.

To compute the partical derivative, just pretend another variable is constant, and you take ordinary derivative.

- ![](../imgs/mc_partical_0.png)
- ![](../imgs/mc_partical_1.png)

You're thinking this is because you're just moving in one direction for the input and you're seeing how that influences things.

- ![](../imgs/mc_partical_2.png)


## Formal definition of partial derivatives

![](../imgs/mc_partical_3.png) ![](../imgs/mc_partical_4.png)


## Symmetry of second partial derivatives

![](../imgs/mc_partical_5.png)

> notice the x,y order in 2 different notations for second partial derivatives.

That is a pretty cool result.   What's surprising is that  this turns out to be true under certain criterion , **not all functions**. There's a special theorem called **Schwarz's theorem**, where if the second partial derivatives of your function are continuous at the relevant point, that's the circumstance for this being true. But for all intents and purposes, the kind of functions you can expect to run into , this is the case.  **The order of partial derivatives doesn't matter.**


## Gradient

> The gradient captures all the partial derivative information of a scalar-valued multivariable function.

![](../imgs/mc_radient_0.png)

This is a vector-valued function.   More general...

![](../imgs/mc_radient_1.png)

I like to think about the gradient as the **full** derivative cuz it kind of captures all of the information that you need.

A very helpful mnemonic advice with the gradient is to think about this nabla ∇ as being a vector full of partial derivative operators.


The gradient can be thought of as pointing in the "**direction of steepest ascent**".  This is a rather important interpretation for the gradient.

![](../imgs/mc_radient_2.png)

![](../imgs/mc_radient_3.png)


## Directional derivative

Directional derivatives tell you how a multivariable function changes as you move along some vector in its input space.  That is, what does a nudge in that vector's direction do to the function itself? 

But you're not really thinking of the actuall vector, but you'be be thinking of taking a very very small step along it , maybe h·v.

![](../imgs/mc_direct_deriv.png)

So, the directional derivative is saying,  when you take a slight nudge in the direction of that vector, what is the resulting change to the output.

- ![](../imgs/mc_direct_deriv_2.png)
- The right bottom term is just w·∇f.


Formal definition:

- ![](../imgs/mc_direct_deriv_3.png)


## Why the gradient is the direction of steepest ascent

```bash
f(x,y) = x² + y²
```

If you have a given point somewhere in the input x-y plane, the question is, of all the possible directions that you can move away from this point, which one of them results in the greastes increase to your function ?

- ![](../imgs/mc_direct_deriv_4.png)

Why does the gradient, the combination of partial derivatives, has anything to do with choosing the best direction ?

- ![](../imgs/mc_direct_deriv_5.png)

When ∇f(a,b) has the same direction as v , dot product has the greatest value.


## Gradient and contour maps

Question:  of all of the vectors that move from this output of 2 , up to the value of 2.1 , which one dest it the fastest ?


- ![](../imgs/mc_direct_deriv_6.png) ![](../imgs/mc_direct_deriv_7.png)

Which one does it with the shortest distance ? It's gonna be the one that connects them pretty much perpendicular to the original line. Because if you think about these as lines, and the more you zoom in, the more the pretty much look like parallel lines, the path that connects one to the other is gonna be perpendicular to both of them.

Keep it in the back of you mind: **Gradient is always perpendicular to contour lines**.















