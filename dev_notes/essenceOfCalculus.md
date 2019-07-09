...menustart

 - [chapter 1: Essense of Calculus](#5c6d0419bdcc965d881019d989ad6f1a)
 - [chapter 2: Paradox of the derivatives](#b872997f4e311706ca6628e823fc3459)

...menuend


<h2 id="5c6d0419bdcc965d881019d989ad6f1a"></h2>

# chapter 1: Essense of Calculus

**The art of doing mathematics is finding that** ***special case*** **that contains all the germs of generality**.

 - how to calculate the area of round ? 
 - hard problem -> sum of many small values -> **Area under a graph**
 - Many of these types of problems turn out be to equivalent to finding the area under some graph.

![](../imgs/eoc_integal.png)

 - What's the are underneath that curve , say between the values of x=0 and x=3 ? 
 - Let's reframe this question in a slightly different way:
    - we'll fix that left endpoint in place at 0, and let the right endpoint vary.
    - Are you able to find a function A(x) that gives you the area under x² between 0 and x?
 - A function `A(x)` like this is called an integral of x².
 - Calculus holds within it the tools to figure out what an integral like this is.
 - Finding this area , this integral function , is genuinely hard. 
    - And whenever you com across a genuinely hard question in math a good policy is to not try too hard to get the answer directly, since usually you just end up banging your head against a wall. 
    - Instead , play around with the idea, with no particular goal in mind. Spend some time building up familiarity with the interplay between the function defining the graph(in this case x²)  and the function give the area. 
 - In that playful spirit , if you are lucky  , here's something that you might notice :
    - When you slightly increase x by some tiny nudge *dx* , looking that resulting change in sliver area  represented with *dA* , for a tiny difference in area. 
    - ![](../imgs/eoc_dA.png)
    - That sliver can be pretty well approximated with a rectanalge : dA ≈ x²·dx.  That is , dA/dx ≈ x².
    - When you look at 2 nearby pointer , 3 & 3.001, ( A(3.001)-A(3) )/0.001 ≈ 9. 
    - this ratio of *dA/dx* is called **derivative** of A. 
 - We care about derivatives because they help us solve problems. Thay are the key to solving integral questions, problem that finding the area under a curve. 
    - Once you gain enough familiarity with computing derivatives, you'll be able to look at a situation like this one:
        - when you don't know what a function is , but you do know that its derivative should be x².
        - and from that , reverse engineer what the function must be. 
 - And this back and forth between integrals and derivatives , where the derivative of a function for the area under a graph gives you back the function defining the graph itself is called the 
    - **Fundamental theorem of calculus**. 
    - It ties together the 2 big ideas of integrals and derivatives.  in some sense , eacho one is an inverse of the other. 


<h2 id="b872997f4e311706ca6628e823fc3459"></h2>

# chapter 2: Paradox of the derivatives
 
 - Goal
    - 1 : Learn Derivatives
    - 2 : Avoid Paradoxes
 - What is Derivatives?
    - Instantaneous rate of change
        - instantaneous means over a very small time 
 - example 
    - 距离时间 s(t) = t³, 计算 t=2 时的速度
    - 
    ```
    ds/dt(2) = ( (2+dt)³ - 2³ ) / dt 
             = ( 2³ + 3(2)²dt + 3(2)(dt)² + (dt)³ - 2³  ) / dt
             = 3(2)² + 3(2)dt + (dt)²
             = 3(2)² , as dt→0
    ```
    - There was nothing special about choosing t=2, more generally we'd say that 
        - the derivative of t³ , as a function of t, is 3t²


# chapter 3: Derivative formulas through geometry 

 - how to calculate the derivative of f(x)=x²
 - let's see what happens when x is increased a bit :
    - ![](../imgs/eoc_fx_x2_incr.png)
    - Since the *dx* is very tiny, a good rule of thumb is that **you can ingore anything that includes a dx raised to a power greate than 1**.
    - so, df = 2xdx  =>   df/dx = 2x 


# chapter 4: Visualizing the chain rule and product rule

**Using the chain rule is like peeling an onion: you have to deal with each layer at a time, and if it is too big you will start crying**,

 - 3 basic ways to combine functions together
    1. Adding them  ( also substracting  )
    2. multiplying them ( also dividing )
    3. puting one inside the other 

## Sum rule

 - sum rule is the easiest. 
    - the derivative of a sum of n functions ,  is the sum of their derivatives.

## Multiply rule

 - thinking df in area increasing 
 - Left·*d(Right)* + Right·*d(Left)*

## Chain rule 
 - g(h(x))
 - for an example: f = sin(x²)
    - let h = x²
    - df = cos(h)dh ,  substitude h with x²
    - df = cos(x²)d(x²) = cos(x²) 2x dx
 - ![](../imgs/eoc_chain_rule.png)
 - ![](../imgs/eoc_chain_of_rule2.png)


# chapter 5: What's so special about Euler's number e?

**Who has not been amazed to learn that the function y=eˣ, like a phoenix rising again from its own ashes, is its own derivative?**

 - exponentials function , like 2ˣ, 7ˣ, eˣ
 - let's start with M(t) = 2ᵗ
 - dM/dt(t) = (2ᵗ⁺ᵈᵗ - 2ᵗ)/dt
    - = (2ᵗ·2ᵈᵗ - 2ᵗ)/dt
    - = 2ᵗ· (2ᵈᵗ-1)/dt
 - 右半部分的 只和 *dt* 有关的项非常重要, 它并不依赖于 *t*
    - when dt→0, this value (right part) approaches a very specific number: 0.6931...
 - so, the derivative of 2ᵗ is itself, but multiplied by some constant. 
 - And there's not too much special about the number 2 here,  if instead we had dealt with the function 3ᵗ, the derivative of 3ᵗ is proportional to itself, but this time it would have had a proportional constant 1.0986... .
 - **d(aᵗ)/dt = aᵗ(some constant)**
    - whether there's some base where that proportional constant is 1 ? 
    - There is !  e = 2.71828... 
 - d(e<sup>ct</sup>)/dt = ce<sup>ct</sup>
    - 2 = e<sup>ln(2)</sup>
    - 2ᵗ = e<sup>ln(2)t</sup>  -- Derivative --> ln(2)e<sup>ln(2)t</sup>  = ln(2)2ᵗ
    - ln(2) = 0.6931...
 - **The mystery proportional constant** that pops up when taking derivatives is just the natural log of the base.
    - 事实上，在微积分的应用中， 你很少见到 aᵗ 这种写法，而经常会以 e<sup>ct</sup> 出现 : 5ᵗ = e<sup>(1.6094...)t</sup>
 - I really want to emphasize that there are many many ways to write down any particular exponential function,
    - ![](../imgs/eoc_e.png)
    - 指数函数之所以 选择使用  e<sup>ct</sup>,  is to gives that constant *c*  a nice, readable meaning. 


# chapter 6: Implicit differentiation, what's going on here? 

 - implicit differentiation 隐微分 是一种在特殊情况下使用的求导方法
    - 一般我们碰到y=xsinx还是可以很轻松的直接求导的，但是面对x²+y²=5² 的时候，就比较棘手了.
    - 这时用implicit differentiation来解决就能方便很多。(要用到chain rule)
 - 举例: x²+y²=5² 求导
    - 方法1: y=±√(5²-x²) ,  看到根号就不想进行下去了...
    - 方法2: 使用隐微分.
 - This curve is not the graph of a function. so we can not take a simple derivative. 
    - x is not an input, and y is not an output. they're both just independent valuse related by some equation. 
    - This is called an "implicit curve".  It's just the set of all points (x,y) that satisfy some property written in terms of 2 variables x and y. 
 - The procedure for how you acutllay find dy/dx for curve like this ( implicit differentiation ) is the thing I fould very weird as a calculus student. 
    1. take derivative of both sides
        - 2xdx + 2ydy = 0 
    2. you get 
        - dy/dx = -x/y
        - this is the slop of point(3,4)  , is -3/4
 - But first, I want to set aside this particular problem, and show how this is related to a different type of calculus problem : **Related rates**. 
    - Imagining a 5 meter long ladder up against a wall, where the top of the ladder starts 4 meters above the ground, which means the bottom is 3 meters away from the wall. 
    - and let's say it's slipping down in such way that the top of the ladder is dropping at 1m/s. 
 - The question is , in that initial moment , what is the rate at which the bottom of the ladder is moving away from the wall. 
    - Let's label that distance from the top of the ladder to the ground y(t) ,  written in a function of time t because it's changing. 
    - Likewise label the distance between the bottom of the ladder to the wall x(t).
    - ![](../imgs/eoc_ralated_rates_0.png)
    - key equation:  x(t)² + y(t)² = 5²
        - The left-hand side is a function of time, it just so **happens to equal a constant**, meaning this value evidently doesn't change while time passes, but it's still written as an expression dependent on time. 
        - In particular, we can take a derivative of the left-hand side, which is a way of saying 
            - "If I let a little bit of time pass, dt, which causes y to slightly decrease, and x to slightly increase, how much does this expression change"
        - d(x(t)² + y(t)²)/dt = 0 
        - what you get when you computing the derivative ? 
        - 2x(t)dx/dt + 2y(t)dy/dt = 0  
        - That is equivalent to saying x²+y² must not change while the ladder moves. 
    - so, at the initial beginning 
        - 2(3)dx/dt + 2(4)-1 = 0  =>  dx/dt = 4/3
 - The reason I bring up this ladder problem is that I want to compare this to the problem of finding the slope of tangent line to the circle.
 - As one more example, let me show how you can use this technique to help find new derivative formulas.
    - d(ln(x))/dx = ???
    - The curve is `y = ln(x)` , first rearrange this equation to be 
        - eʸ = x 
    - take the derivative both sides
        - eʸdy = dx 
    - we get
        - dy/dx = 1/eʸ
 - By the way, all of this a little peek into **multivariable** calculus , where you consider functions with multiple inputs, and how they change as you tweak those multiple inputs. 
    - The key, as always, is to have a clear image in your head of what tiny nudges are at play, and how exactly they depend on each other 

# chapter 7: Limits, L'Hopital's rule, and epsilon delta definitions

 - this course
    1. df/dx
    2. lim
    3. ∫
 - lim
    - Goal 1: Formal definition of a derivative
    - Goal 2: (ε,δ) definition of limits
    - Goal 3: L'Hopital's rule
 - ![](../imgs/eoc_lim_0.png)
    - Lefthand side: Limit idea is built in , it is just a shorthand for what the righthand side 
    - righthand side: Formal derivative difinition
        - here, I want to emphasize that nothing about this righthand side references the paradoxical idea of an "infinitely small" change. 
        - the point of limits is to avoid that. 
        - This value h is the exact something as the *dx* referenced throughout the series. It's a nudge to the input of *f* with some nonzero, finitely small size, like 0.001.
 - when a limit exists , you can make this output range as small as you want, 
    - ![](../imgs/eoc_lim_1.png)
 - but when the limit doesn't exists, that output range can't get smaller thant some value, not matter how much you shrink the input range around the limiting input. 
    - ![](../imgs/eoc_lim_2.png)
 - What it means for the limit to exist is that you can always find a range of inputs around our limiting input , some distance δ around from some value x , 
    - ![](../imgs/eoc_lim_10.png)
    - so that any input within a distance δ of x corresponds to an output with a distance ε of f(x). 
    - ![](../imgs/eoc_lim_11.png)
    - The key point here is that this is true for any ε , no matter how small, you always be able to find a corresponding δ.
 - In contrast, when a limit doesn't exist, as in this example , 
    - ![](../imgs/eoc_lim_20.png)
    - you can find a sufficiently small ε , like 0.4, so that no matter how tiny δ is , the corresponding range of outputs is just always too big. 
 - How do you compute limits ?
    - For example, let's say for some reason you were studying the functiong  sin(πx)/(x²-1)
        - ![](../imgs/eoc_lim_30.png)
        - it looks pretty continuous , but there's a problematic value, x=1. The function is actually not defined there, and the graph should really have a hole there.
    - The graph certainly does seem to approach some distinct value at that point. So you might ask, how do you figure out what output this approaches as x approaches 1, since you can't just plug in 1 ?
    - Well, one way to approximate it would be to plug in a number very close to 1, like 1.00001 , sin(π·1.00001)/(1.00001²-1) = 1.5708...
    - But is there away to know exactly what it is ? Some systematic process to take an expression like this one , 0/0 at some input?
        - ![](../imgs/eoc_lim_31.png)
    - consider what happends just a tiny nudge dx away. 
        - The value of sin(πx) is bumped down. 
        - and the value of that nudge, is d(sin(πx)) = cos(πx)πdx , we plug in x=1 to this expression. we get  -πdx. 
        - similarly , the value of x²-1 graph has changed by some d(x²-1) = 2xdx, plug in x=1, we get 2dx 
        - ![](../imgs/eoc_lim_32.png)
    - so lim<sub>x→1</sub> sin(πx)/(x²-1) ≈ -πdx/2dx = -π/2
    - This ratio -π/2 actually tells us the precise limiting value as x approaches 1. Remember, what that meas is that the limiting height on our original graph is evidently exactly -π/2. 
        - ![](../imgs/eoc_lim_33.png)
 - More generally , think of any 2 functions f(x) and g(x) , which are both 0 at some common value x = a.
    - 0/0 型， 两条曲线 f(x),g(x) 相交于某个点 a  , f(a)=g(a) = 0
    - The only constraints is they have to be functions where you're able to take a derivative of them at x=a. Which means that they each basically look like a line when you zoom in close enough to that value. 
    - ![](../imgs/eoc_lim_34.png)
    - Even though you can't compute f/g at the trouble point, you **CAN** ask about this ratio for values of x very close to a, the limit as x approaches a. 
    -This clever trick is called **L'Hopital's rule**. 


# chapter 8: Integration and the fundamental theorem of calculus

 - 小车匀速行驶 v=10m/s, 8秒后 s=10x8 =80米.
    - ![](../imgs/eoc_integral_0.png)
 - What if the velocity is not constant? 
    - v(t) = t(8-t)
    - ∫₀⁸v(t)dt
    - ![](../imgs/eoc_integral_1.png)
 - But finding the area between a function's graph and the horizontal axis is somewhat a common language for many disparate problems that can be broken down and approximated as the sum of a large number of small things. 
 - How interpret and compute the area under a graph is a very general problem-solving tool. 

---

 - For our velocity example, think of this right endpoint as a variable, T. 
 - So we thinking of this integral of the velocity function between 0 and T , the area under the curve between those two inputs , as a function, where that upper bound is the variable.  ∫₀ᵀ v(t)dt.
 - That area represents the distance the car has traveled after T seconds. So this is really a distance vs. time function s(T).
 - ![](../imgs/eoc_intergral_2.png)
 - Now ask yourself, what is the deriviate of that function ? 
    - A slight nudge of dT to the input causes that area to increase , some little ds represented by the area of this sliver. 
    - The height of that sliver is the height of the graph at that point, v(T),  and its width is dT. 
    - And for small enough dT, we can basically consider that sliver to be a rectangle. 







