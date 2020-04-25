
# Trigonometry fundamentals | Lockdown math ep. 2

```
cos(x)² = (1+cos(2x)) /2
```

In particular the one thing I want you to take note of is the weird fact that, when you sqaure cos, it's not equal to but it's somewhat related to the idea of scaling up that intput

```
cos(x)² ←→  cos(2x)
```

Now if you were clever there is another function that behaves very similarly to this

```
f(x) = 2ˣ
```

Maybe, just maybe cosine is somehow related to exponents. It's not at all obvious how it is , but it absolutely is. 


**Trigonometry Basis**: **You think its about triangles, but really it's about circles.**

![](../imgs/3b1b_triangle_circles.png)

Here, θ is the input, and it's going to be a measure of how far you've walked around a unit circle.  sin(θ) give you the y-axis value -- the distance between you and the x-axis.

![](../imgs/3b1b_triangle_circles_cos.png)

By contrast consine is defined very similarly but it's giving you the x coordinat. 

----

```
cos(x)² + sin(x)² = 1 
```

If fact this is equivalent to the Pythagorean theorem(勾股定理).

But you never see it written down like that. 

Because people don't want to write too many paranthesis , instead they write 

```
cos²(x) + sin²(x) = 1 
```

How lovely we don't have to write too many symbols, what a wonderful convention except for the fact that literally every other time in math you see something written as `f²(x)`, what that means is not `(f(x))²` ,that's almost never what it means.

instead what it's supposed to mean for most of math is taking a function and applying it to itself `f(f(x))` . 

THe idea is that it's very different from the convention in trigonometry. Trigonometry is just flying by its own rules: I understand some students will be confused but I'm trigonometry I don't care. 

---

Now we will walk back to the very beginning , associated with cos²(θ) and cos(2θ). 

```
cos(x)² = (1+cos(2x)) /2
```

cos²(x) which looks like little scaled-down version of cosine, oscillating more quickly is the same as cos(2x) that quicker oscillation, but we had to kind of shift it and rescale it to make them equal. 

what is the cos(π/12) ?

We'll find next time is that this is actually a shadow of the fact that trigonometric functions are related to complex numbers. 

And the idea of doubling the angle (cos(2x))  correspoinding to multiplying by something twice (cos²(x)) not at all a coincidence. 

**Where is tan(θ) ?** 

![](../imgs/3b1b_tangent.png)

It actually lies tangent to the circle, so is where the word "tan" comes from. 

**Where is cos²(θ) ?**

If we draw the graph of cos(x) and cos²(x) simultaneously 

![](../imgs/3b1b_trig_cos_sqaure.png)

The square of that value looks like anothe cosine wave.

Where is the cos²(x) on the unit circle ?

![](../imgs/3b1b_cos_squre_on_circle.png)


# Complex number fundamentals | Lockdown math ep. 3

```
cos(α+β) = cos(α)cos(β) - sin(α)sin(β)
sin(α+β) = cos(α)sin(β) + cos(β)sin(α)
```

It's something that's very error-prone if you're just trying to memorize it as it is. 

However if you come at it with complex numbers this is not only much less error-prone it has a very beautiful meaning and it just falls right out. 

So even if you don't necessarily believe in the reality of the √-1 , you at the very least have to admit that it's interesting that it can make other pieces of math useful that other pieces of math a little bit more understandable too. And trigonometry is just the tip of the iceberg. 

If talk to anybody who's in engineering anybody who's going into serious math they'll tell you that complex numbers are as real a part of their work in their life as real numbers are. 

But the starting point looks very strange 

- Weird assumptions:
    - **i² = -1**

The *i* does not exist on the real number line, it on the line perpendicular to it. 

--- 

You have a vector (3,2),  rotated by 90 degree, you get (-2,3).  

(x,y) -> rotate 90 degree -> (-y,x)

What's result of i·(3+2i) ?  -2+3i. 

So that should give you some indication that , ok multiplying by *i* has this action of rotating things by 90 degrees. 

It turns out that if you have a number that behaves this way it gives you a computational mechanism for all of the types of rotations that you might want to do that might not necessarily be 90 degree. 

- 3 Facts about Multiplication, suppose we have a complex number
    1. z·1 = z
    2. z·i = rot 90(z)
    3. z·(c+di) = c·z + d·zi
        - we know what z is, and we also know what zi is.
        - linear combinaton of 2 perpendicular vectors z , zi 

Q: What is the complex number z, so that multiplying by z has the effect of rotating 30°, or π/6 radians, counterclockwise ?
A: z = cos(π/6) + isin(π/6)





