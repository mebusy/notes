...menustart

 - [Calculus One , Part II](#fa33d1b29e3eccffe78a5783a9d43764)
 - [Week 11 Antidifferentiation](#f2b7b4d00d78e3fd5414e3486cced898)
	 - [How do we handle the fact that there are many antiderivatives?](#e5f2ceb4aa78ecec5012e1f271ec48d0)
	 - [How am I supposed to compute antiderivatives ?](#f3171cf7edd44fec9674414241d559a1)
		 - [What is the antiderivative of a sum?](#9a774c13632f99aade9ae58467e1839b)
		 - [What is an antiderivative for xⁿ ?](#2b4ad78f06a02378ecd2fb58fa1e0d88)
		 - [What is the most general antiderivative of 1/x?](#9602e1d6d174f0797eea3631e85257b0)
		 - [What are antiderivatives of trigonometric functions?](#ef8ce61c6eaaba0c86730eee57732a7a)
		 - [What are antiderivatives of eˣ and natural log?](#f25d9687ab2a19385a54403be540b9fa)
	 - [Why is this so hard ?](#884aac3316eafa26375608fe965ec95b)
		 - [What is the antiderivative of f(mx+b)?](#f4ad4b23e7f189ae03e08f4479b96fad)
		 - [What is an antiderivative for e^(-x²) ?](#51698d7dfac653ae45039307500ba6ed)
	 - [Why would anybody want to do this ?](#eed598ddc44da35152d9cd8fa4f72500)
		 - [Knowing my velocity, what is my position?](#53f3b74109dd53d0637327e1c4461353)
		 - [Knowing my acceleration, what is my position?](#2d170c5dab6fbe2b16e00620d9777204)
		 - [What is the antiderivative of sine squared?](#1278e0b4deef4be8e19deb27ec0db474)
		 - [What is a slope field?](#4f9b1095d71cf63bce0bd635d59babae)

...menuend


<h2 id="fa33d1b29e3eccffe78a5783a9d43764"></h2>

# Calculus One , Part II 

<h2 id="f2b7b4d00d78e3fd5414e3486cced898"></h2>

# Week 11 Antidifferentiation

You can really think of anti-differentiation as a sort of bridge between the, the differentiation section of this course, and the integration section of this course.


<h2 id="e5f2ceb4aa78ecec5012e1f271ec48d0"></h2>

## How do we handle the fact that there are many antiderivatives?

 - f(x) = 2x
    - F(x) = x²
    - G(x) = x²+ 17
    - H(x) = x²+ C

<h2 id="f3171cf7edd44fec9674414241d559a1"></h2>

## How am I supposed to compute antiderivatives ?

<h2 id="9a774c13632f99aade9ae58467e1839b"></h2>

### What is the antiderivative of a sum?

 - F is an antiderivative of f 
    - `∫f(x)dx = F(x)+C`
 
---

 - if ∫f(x)dx = F(x)+C ,  ∫g(x)dx = G(x)+C
 - then ∫(f(x)+g(x))dx = F(x) + G(x) + C  , 
 - or ∫(f(x)+g(x))dx = ∫f(x)dx + ∫g(x)dx. 
 - The antiderivative of the sum is the sum of the antiderivative . 

<h2 id="2b4ad78f06a02378ecd2fb58fa1e0d88"></h2>

### What is an antiderivative for xⁿ ?

 - ∫xⁿdx = xⁿ⁺¹/(n+1) + C

--- 

```
f(x) = 15x² -4x +3 
∫(15x² -4x +3)dx 
= ∫15x²dx - ∫4xdx + ∫3dx 
= 15∫x²dx - 4∫xdx + ∫3dx
= 15·x³/3 - 4·x²/2 + 3x + C
= 5x³ - 2x² + 3x + C
```

 - Constant multiple rule:
    - ∫a·f(x)dx = a·∫f(x)dx

<h2 id="9602e1d6d174f0797eea3631e85257b0"></h2>

### What is the most general antiderivative of 1/x?

 - The most genral antiderivative of 1/x has the form 

```
      ⎧ logx + C , if x>0
F(x)= ⎨ 
      ⎩ log(-x) + D , if x<0>
```

 - for constant C and D.

---

 - Suppose f is a function with **an** antiderivative F ,
 - Then any another antiderivative for f has the form 
    - F(x) + C(x)
 - for some **"locally constant"** function C
    - C不仅仅是一个常数，C是一个局部常值函数
    - 关键在于，这个C可以在不同的区间值不通

---

 - 很不幸， Some textbooks write 
    - ∫1/xdx = log|x| + C 
 - is fine **provided C is a locally constant function of x**.


<h2 id="ef8ce61c6eaaba0c86730eee57732a7a"></h2>

### What are antiderivatives of trigonometric functions?

 - ∫cosxdx = sinx + C
 - ∫sinxdx = -cosx + C
 - ∫tanxdx = log(secx) + C
 - ∫secxdx = log|secx + tanx| + C 

 - anti-differentiation is HARD.


<h2 id="f25d9687ab2a19385a54403be540b9fa"></h2>

### What are antiderivatives of eˣ and natural log?

 - ∫eˣdx = eˣ + C
 - ∫log(x)dx = x·log(x) - x + C


<h2 id="884aac3316eafa26375608fe965ec95b"></h2>

## Why is this so hard ?

<h2 id="f4ad4b23e7f189ae03e08f4479b96fad"></h2>

### What is the antiderivative of f(mx+b)?

 - if we have ∫f(x)dx = F(x) + C 
 - ∫f(mx+b)dx = F(mx+b)/m + C 
 - eg.
    - ∫sin(2x+1)dx = -cos(2x+1)/2 + C  
    - ∫sec²xdx = sin(x)/cos(x)+C , ∫sec²(-5x+7)dx = sin(-5x+7)/cos(-5x+7)/-5 + C = sin(5x-7)/cos(5x-7)/5 +C
     
<h2 id="51698d7dfac653ae45039307500ba6ed"></h2>

### What is an antiderivative for e^(-x²) ?

 - ∫e<sup>-x²</sup>dx **can not be expressed using elementary functions**.
    - elementary function means  polynomials, trig functions, eˣ, log, etc...
 - **many functions are impossible to antidifferentiate**.


<h2 id="eed598ddc44da35152d9cd8fa4f72500"></h2>

## Why would anybody want to do this ?

<h2 id="53f3b74109dd53d0637327e1c4461353"></h2>

### Knowing my velocity, what is my position?

 - p(t) = position
 - v(t) = velocity
 - p'(t) = v(t)
 - p(t) = ∫v(t)dt
 - eg.
    - v(t) = 3-10t
    - p(t) = ∫(3-10t)dt = 3x - 5t² +C 
    - and now , the +C has a prefectly reasonable physical interpretation. If I know my velocity, I know my position as long as I know my initial position. 
        - p(0) = 4
        - p(t) = 3x - 5t² + 4

<h2 id="2d170c5dab6fbe2b16e00620d9777204"></h2>

### Knowing my acceleration, what is my position?

 - a(t) = 8
 - v(t) = ∫a(t)dt = ∫8dt = 8t + C
    - knowning my acceleration doesn't detemine my velociy, it only detemines my velocity up to some constant. 
    - it could be going really fast or really slow , but still accelerating at the same rate. 
    - C is v(0)
 - p(t) = ∫v(t)dt = ∫(8t + C)dt = ∫8tdt + ∫Cdt = 4t² + Ct + D.  
    - where C is v(0) , D is p(0)


<h2 id="1278e0b4deef4be8e19deb27ec0db474"></h2>

### What is the antiderivative of sine squared?

```
  ∫sin²xdx = ∫(1-cos(2x))/2dx
= 1/2∫(1-cos(2x))dx
= 1/2( ∫1dx - ∫cos(2x)dx )
= 1/2( x - sin(2x)/2 ) + C
= x/2 - sin(2x)/4 + C 
``` 

<h2 id="4f9b1095d71cf63bce0bd635d59babae"></h2>

### What is a slope field?

There's a visual way to gain some insight into these anti-differentiation problems. 


 - slop field of function x² - x
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_slope_field.png)
 - instead of plotting a value at some height, I draw little tiny line segments with that slope.
 
--- 

 - slop field of function xcosx
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_slope_field_xcosx.png)
 - 利用slop field， 可以大致画出 原函数的图像
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_slope_field_xsinx+cosx.png)
    - graph for y = xsinx + cosx 
    - +C can move graph up and down.

# Week12 Integration

## What is summation notation ?

### What is the sum 1 + 2 + ... + k? 

∑<sub>n=</sub>ᵏ₁ n = ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_meaning1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_meaning2.png)


∑<sub>n=</sub>ᵏ₁ n = (k+1)·k/2

### What is the sum of the first k odd numbers?

  ∑<sub>n=</sub>ᵏ₁ (2n-1) 
  
= ∑<sub>n=</sub>ᵏ₁ 2n - ∑<sub>n=</sub>ᵏ₁ 1 

= 2·∑<sub>n=</sub>ᵏ₁ n - ∑<sub>n=</sub>ᵏ₁ 1 

= (k+1)·k - k 

= k² 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_odd.png)

### What is the sum of the first k perfect squares?

  ∑<sub>n=</sub>ᵏ₁ n² = 1² + 2² + ... + k² 

= k·(k+1)·(2k+1) /6

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_square.png)

大图正好是 4个小图的 3倍。 4个小图平铺，等于大图中间部分。

 - the length of buttom of big picture is `2k+1`
 - the height of big picture is ∑<sub>n=</sub>ᵏ₁ n = `(k+1)·k/2`
 - so the sum of small pictures is `(2k+1)·(k+1)·k/6`

### What is the sum of the first k perfect cubes?

  ∑<sub>n=</sub>ᵏ₁ n³ 

= ( ∑<sub>n=</sub>ᵏ₁ n )² 

= (k·(k+1)/2)²

= k²·(k+1)² /4

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_cube.png)


## So how do we calculate area precisely ?

### What is the definition of the integral of f(x) from x = a to b?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integration_ab.png)

 - Thm: If *f* is continuous, then *f* is integrable 
    - means ∫<sub>a,b</sub>f(x)dx  exist.
 
## Can we compute any other integrals ?

### What is the integral of x^2 from x = 0 to 1?

 - What is the ∫<sub>0,1</sub>x²dx ?
 - We divide [0,1] into n pieces,  so each interval is 1/n

  ∫<sub>0,1</sub>x²dx 

= lim<sub>n→∞</sub> ∑<sub>i=</sub>ⁿ₁ (i/n)²·(1/n)

= lim<sub>n→∞</sub> ∑<sub>i=</sub>ⁿ₁ 1/n³·i²

= lim<sub>n→∞</sub> 1/n³·∑<sub>i=</sub>ⁿ₁ i²

= lim<sub>n→∞</sub> ( 1/n³· (n)(n+1)(2n+1)/6  )

= lim<sub>n→∞</sub> (1/n³·(2n³+3n²+n)/6)

求这个极限很简单

= 1/3

### What is the integral of x^3 from x = 1 to 2?

  ∫<sub>0,2</sub>x³dx 
  
= lim<sub>n→∞</sub> ∑<sub>i=</sub>ⁿ₁ (2/n·i)³·2/n

= lim<sub>n→∞</sub> ∑<sub>i=</sub>ⁿ₁ 16/n⁴·i³

= lim<sub>n→∞</sub> 16/n⁴· ∑<sub>i=</sub>ⁿ i³

= lim<sub>n→∞</sub> 16/n⁴· (∑<sub>i=</sub>ⁿ i)²

= lim<sub>n→∞</sub> 16/n⁴·((n)(n+1)/2)²

= lim<sub>n→∞</sub> 4·n²·(n+1)²/n⁴

= 4

repeat this same kind of calculation to deduce that: 

∫<sub>0,1</sub>x³dx  = 1/4

now we get the final answer:

∫<sub>1,2</sub>x³dx  = ∫<sub>0,2</sub>x³dx - ∫<sub>0,1</sub>x³dx = 15/4


## Can we understand anything conceptually about integrals ?





