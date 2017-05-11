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
 - [Week12 Integration](#514e1caaba7832bf708c3cbba5572912)
	 - [What is summation notation ?](#5b0c78a8b489b5951d6133d512173fd2)
		 - [What is the sum 1 + 2 + ... + k?](#fd783af9af00d3861d1ff94414ccb5fd)
		 - [What is the sum of the first k odd numbers?](#64b7c829a64912cded7e4fb1748bf931)
		 - [What is the sum of the first k perfect squares?](#bb1b3996821d028092f6f37259c6dc7d)
		 - [What is the sum of the first k perfect cubes?](#9a72aabb581b21f673d346308b47b1ec)
	 - [So how do we calculate area precisely ?](#4803201396fe93254689a378f4acea16)
		 - [What is the definition of the integral of f(x) from x = a to b?](#a2a6a595d166557f2b5ba00e7e8f36cc)
	 - [Can we compute any other integrals ?](#0b347bc298049db4ffd8970d79c31ef6)
		 - [What is the integral of x^2 from x = 0 to 1?](#407504fcb5d2b2a2db97282f9349f4c6)
		 - [What is the integral of x^3 from x = 1 to 2?](#6693d9715518594ce91728437de46c79)
	 - [Can we understand anything conceptually about integrals ?](#267eece5a0855676c858702fe0ba61ca)
		 - [What sorts of properties does the integral satisfy?](#5104183620b8440565164d50f7160ce0)
		 - [When is the accumulation function increasing? Decreasing?](#adf7c6d36d552a2cdce06fa0a8c2b306)
 - [Week 13 Fundamental Theorem of Calculus](#76e5d32d317a3d89cedfea3744cc9d75)

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

<h2 id="514e1caaba7832bf708c3cbba5572912"></h2>

# Week12 Integration

<h2 id="5b0c78a8b489b5951d6133d512173fd2"></h2>

## What is summation notation ?

<h2 id="fd783af9af00d3861d1ff94414ccb5fd"></h2>

### What is the sum 1 + 2 + ... + k? 

∑<sub>n=</sub>ᵏ₁ n = ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_meaning1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_meaning2.png)


∑<sub>n=</sub>ᵏ₁ n = (k+1)·k/2

<h2 id="64b7c829a64912cded7e4fb1748bf931"></h2>

### What is the sum of the first k odd numbers?

  ∑<sub>n=</sub>ᵏ₁ (2n-1) 
  
= ∑<sub>n=</sub>ᵏ₁ 2n - ∑<sub>n=</sub>ᵏ₁ 1 

= 2·∑<sub>n=</sub>ᵏ₁ n - ∑<sub>n=</sub>ᵏ₁ 1 

= (k+1)·k - k 

= k² 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_odd.png)

<h2 id="bb1b3996821d028092f6f37259c6dc7d"></h2>

### What is the sum of the first k perfect squares?

  ∑<sub>n=</sub>ᵏ₁ n² = 1² + 2² + ... + k² 

= k·(k+1)·(2k+1) /6

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_square.png)

大图正好是 4个小图的 3倍。 4个小图平铺，等于大图中间部分。

 - the length of buttom of big picture is `2k+1`
 - the height of big picture is ∑<sub>n=</sub>ᵏ₁ n = `(k+1)·k/2`
 - so the sum of small pictures is `(2k+1)·(k+1)·k/6`

<h2 id="9a72aabb581b21f673d346308b47b1ec"></h2>

### What is the sum of the first k perfect cubes?

  ∑<sub>n=</sub>ᵏ₁ n³ 

= ( ∑<sub>n=</sub>ᵏ₁ n )² 

= (k·(k+1)/2)²

= k²·(k+1)² /4

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_2_integration_sum_cube.png)


<h2 id="4803201396fe93254689a378f4acea16"></h2>

## So how do we calculate area precisely ?

<h2 id="a2a6a595d166557f2b5ba00e7e8f36cc"></h2>

### What is the definition of the integral of f(x) from x = a to b?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integration_ab.png)

 - Thm: If *f* is continuous, then *f* is integrable 
    - means ∫<sub>a,b</sub>f(x)dx  exist.
 
<h2 id="0b347bc298049db4ffd8970d79c31ef6"></h2>

## Can we compute any other integrals ?

<h2 id="407504fcb5d2b2a2db97282f9349f4c6"></h2>

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

<h2 id="6693d9715518594ce91728437de46c79"></h2>

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


<h2 id="267eece5a0855676c858702fe0ba61ca"></h2>

## Can we understand anything conceptually about integrals ?

<h2 id="5104183620b8440565164d50f7160ce0"></h2>

### What sorts of properties does the integral satisfy?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integral_satisfied_property1.png)

∑<sub>n=</sub>ᵐ₁ f(n) + ∑<sub>n=</sub>ᵏ<sub>m+1</sub> f(n) = ∑<sub>n=</sub>ᵏ₁ f(n)


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integral_satisfied_property2.png)

∑<sub>n=</sub>ᵇₐ k·f(n)  = k·∑<sub>n=</sub>ᵇₐf(n)


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integral_satisfied_property3.png)

∑<sub>n=</sub>ᵇₐ (f(n)+g(n)) = ∑<sub>n=</sub>ᵇₐ f(n) + ∑<sub>n=</sub>ᵇₐ g(n)

**The derivatives have the same rules about sum !**

<h2 id="adf7c6d36d552a2cdce06fa0a8c2b306"></h2>

### When is the accumulation function increasing? Decreasing?

When is A(x) = ∫ˣₐf(t)dt increasing ? Decreasing ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integral_acc_function.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_integral_acc_function_decreasing.png)

The integrals are not exactly measuring area, they're measuring **singed area**. 

 - f positive
    - A(x) increasing
    - A'(x) > 0
 - f negative 
    - A(x) decreasing
    - A'(x) < 0

---

 - 利用函数的对称性，我们可以简化 积分计算
 - ∫¹₋₁ sinxdx = 0
 - ∫<sup>2π</sup>₀ cosxdx = 0 


<h2 id="76e5d32d317a3d89cedfea3744cc9d75"></h2>

# Week 13 Fundamental Theorem of Calculus

## What is the fundamental theorem of calculus?

 - Suppose f:[a,b] → ℝ is continuous. let F be the accumulation function , given by 
    - F(x) = ∫ᵇₐ f(t)dt.
 - Then F is continuous on [a,b] , differntiable on (a,b) , and F'(x) = f(x) 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculus_integrate_fundamental_theorem.png)

--- 


 - So ∫ˣₐ f(t)dt is an **antiderivative !**

Suppose that ∫³₀ f(x)dx = 9 , and f(3) = 10 , Approximate ∫<sup>3.3</sup>₀ f(x)dx 

  ∫<sup>3.3</sup>₀ f(x)dx 

= ∫<sup>3</sup>₀ f(x)dx + ∫<sup>3.3</sup>₃ f(x)dx 

= 9 + 10\*0.3 = 12 

 


