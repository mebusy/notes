...menustart

 - [Calculus One](#37c5cffe5f40cb8a09855f57171e9646)
	 - [limit of  sinx / x](#0da07c5934b4b53cf509da017f8ad52a)
		 - [f(x) = sinx / x , 求 lim x→0](#ad4e9bc62cea4aecede40005fb701b5a)
		 - [limit of product](#4483c04fa3ccf44c111cde358f218561)
		 - [lim<sub>x→3</sub> x/(x-3)](#2b2077c392ecb1166a2447a64365cf3e)
		 - [Continuity](#f73d2c55dc3628b7071e45104874c485)
			 - [One-Sided Limit:](#5573e33b0dfdea6caa96ddf3f7165cfd)
			 - [Continuous:](#fb5871c79f8440fc2a2836470cdba81f)
			 - [Intermediate Value Theorem](#1a8e4c42735dd5a29342c3b0badaa173)
			 - [How to approximate √2 ?](#6a73f242eea2fe23cbe69f07c9597926)
		 - [Infinity](#eb2ac5b04180d8d6011a016aeb8f75b3)
			 - [Why is there an x so that f(x) = x](#589b6a791407525e9ab8f6723184c6a5)
			 - [What means lim<sub>x→a</sub>f(x) = ∞ ?](#31d71cf51302b193ce93c8b285844bb6)
			 - [What means lim<sub>x→∞</sub>f(x) = L ?](#78a1c1c2fa16d034391c0bdd36f154fe)
	 - [Derivative](#70ae6e285cc14c8486e3cf5bec39d1fd)
		 - [What are derivatives](#de47fb5a83cb8dd572de532fa514a58f)
			 - [definition](#30618b3b44fa316257d07e387759fae5)
			 - [Why is f(x) = |x| not differentiable at x =0 ?](#f4d55e88765552127f1f67cba00e367f)
			 - [How does wiggling x affect f(x) ?](#96bad87f34b364bbd46c6a9956c56a84)
		 - [Why would I care to find derivatives ?](#7b4dd7708b6861a409a55f8ae5f03d2f)
			 - [Why is sqrt(9999) so close to 99.995?](#233cda2b0da7e06ce36ab30e5002482a)
			 - [What information is recorded in the sign of the derivative ?](#e89d54795bc4804fe364603cdb6baed4)
		 - [How do differentiability and continuity relate ?](#164411132b76dd8051c2291ff508048b)
			 - [Why is a differentiable function necessarily continuous ?](#399fa607fbcbfea19b9078d5cac8c8e7)
			 - [可微分、连续与可导的关系？](#d20283b049281436b4b7c193d945d561)
		 - [How do I find the derivative ?](#03435db2c86b05d2ec72446257663903)
		 - [How do I differentiate a product ?](#f196de79cd46bd81851a3f8fed50f480)
		 - [How do I differentiate a quotient ?](#1fd4d879c6db3b22c521e30c2fb08385)
		 - [d/dx is just a function](#1288f1095d59ece946013bc62c26a401)

...menuend


<h2 id="37c5cffe5f40cb8a09855f57171e9646"></h2>

# Calculus One

<h2 id="0da07c5934b4b53cf509da017f8ad52a"></h2>

## limit of  sinx / x

<h2 id="ad4e9bc62cea4aecede40005fb701b5a"></h2>

###  f(x) = sinx / x , 求 lim x→0

f(1) = 0.8414...
f(0.1) = 0.998...
f(0.01) = 0.99998...
...
f(0.000001) = 0.9999999999 ...

Is the limit 1 ?

It's just a idean, we don't yet have a rigorous argument. 

Here's a sketch of a more rigorous argument that the limit of sinx/x , as x approaches 0 , is equal to one.

```
cosx < sinx/x < 1
```

is true if x close to 0 but not 0. 

**Squeeze theorum**

```
g(x)≤f(x)≤h(x) , x near a 
lim g(x) = lim h(x) = L
then lim f(x) = L 
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CalculusOne_squeezed_theorum.png)


<h2 id="4483c04fa3ccf44c111cde358f218561"></h2>

### limit of product

if lim<sub>x→a</sub>f(x) = L , 

   lim<sub>x→a</sub>g(x) = M , then

   lim<sub>x→a</sub>(f(x)·g(x)) = L·M


<h2 id="2b2077c392ecb1166a2447a64365cf3e"></h2>

### lim<sub>x→3</sub> x/(x-3) 

我们不应该除以0， 实际上我们也并没有除以0. 我们实际上只是除以了一个接近0的数。而当我们除以一个接近0的数的时候，会发生什么呢？ 如果分母是一个很小的正数，会得到一个很大的正数，如果分母是接近0的负数，会得到一个很大的负数。 这意味着该极限应该 既接近于 很大的正数，又接近一个很大的负数。这个数不可能接近任何固定的值。

注意：这里分子极限为3，  根前面的 sinx / x  不一样， sinx/x 是 0/0型极限。

lim<sub>x→1</sub> (x²-1)/(x-1) = lim<sub>x→1</sub> (x+1)(x-1)/(x-1) = lim<sub>x→1</sub> (x+1) 

PS. `(x+1)(x-1)/(x-1)`  and `(x+1)` not the same function, 一个在 x=1 处 没定义， 一个在 x=1处有定义。 ***But the limit doesn't care***. 极限只取决于 1 附近的函数值。 而在 1附近，这两个函数实际上是一样的。 


<h2 id="f73d2c55dc3628b7071e45104874c485"></h2>

### Continuity

<h2 id="5573e33b0dfdea6caa96ddf3f7165cfd"></h2>

#### One-Sided Limit:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CalculusOne_one_side_limit.png)

 - If lim<sub>x→a⁺</sub>f(x) != lim<sub>x→a⁻</sub>f(x) , then lim<sub>x→a</sub>f(x)  does not exist.
 - if lim<sub>x→a⁺</sub>f(x) =  lim<sub>x→a⁻</sub>f(x) = L,  then lim<sub>x→a</sub>f(x)  = L .

---

<h2 id="fb5871c79f8440fc2a2836470cdba81f"></h2>

####  Continuous:

f(x) is continuous at *a* , means that input near *a* are sent to outputs near f(a). 

more precise :  

 - f(x) is continuouse at *a* means that lim<sub>x→a</sub>f(x) = f(a).  That is:
    - f(x) is defined at x=a
    - lim<sub>x→a</sub>f(x) exists
    - lim<sub>x→a</sub>f(x) = f(a)

---

<h2 id="1a8e4c42735dd5a29342c3b0badaa173"></h2>

#### Intermediate Value Theorem

 - Suppose f(x) is continuous on [a,b] , and y is between f(a) and f(b).
 - Then , there is an x between a and b  , so that f(x) = y .
 - 既： [f(a), f(b)] 之间随机选取一个值 y,  应该存在对应的 x ，使得 f(x) = y.



---

<h2 id="6a73f242eea2fe23cbe69f07c9597926"></h2>

#### How to approximate √2 ?

 - use intermediate value theorem , to try and find x, so that f(x) = x² - 2 = 0

---

<h2 id="eb2ac5b04180d8d6011a016aeb8f75b3"></h2>

### Infinity

---

<h2 id="589b6a791407525e9ab8f6723184c6a5"></h2>

#### Why is there an x so that f(x) = x

 - f(x) cts on [0,1],  0 ≤ x ≤ 1 ; Then there is an x , 0 ≤ x ≤ 1 , and f(x) = x. 
 - 称这个点 (x, f(x)) 为函数的不动点
 - Proof:
    - g(x) = f(x) - x is cts
    - g(0) = f(0) - 0 ≥ 0
    - g(1) = f(1) - 1 ≤ 0
    - by IVT , find x  , so that g(x) = 0, that is f(x) - x = 0 => f(x) = x.

 - 应用：
    - f(x) = cosx 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CalcusOne_cosx_equal_x.png)


---

<h2 id="31d71cf51302b193ce93c8b285844bb6"></h2>

#### What means lim<sub>x→a</sub>f(x) = ∞ ?

 - f(x) is as large as you like , if provide x is close enough to a.


 - 极限不存在 case 
    - 极限无穷大 
    - 左右极限不相等
    - 在正负无穷之间来回震荡
 - 极限无穷大 是 极限值收敛于无穷。但左右极限不等、震荡仍判定为极限不存在。

---

<h2 id="78a1c1c2fa16d034391c0bdd36f154fe"></h2>

#### What means lim<sub>x→∞</sub>f(x) = L ?
    
 - f(x) is as close as you want to L , provided x is large enough.

 - 求 lim<sub>x→∞</sub> 2x/(x+1) 
    - 这里无法再使用 商的极限法则，因为分子分母的极限都不存在
    - 但是可以 通过 分子分母都 乘上 1/x 来求解， 结果为 2.  ( 测试：代入 1000， 10000 ，其结果接近2 )
    - x→∞ ,∞/∞型极限， 算法中 big O的思想



---

<h2 id="70ae6e285cc14c8486e3cf5bec39d1fd"></h2>

## Derivative

<h2 id="de47fb5a83cb8dd572de532fa514a58f"></h2>

### What are derivatives

<h2 id="30618b3b44fa316257d07e387759fae5"></h2>

#### definition 

The ***derivative*** of f at the point x is defined to be :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculus1_derivative_def.png)

其他等价的定义：

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Calculus1_derivative_def2.png) , or  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Calculus1_derivative_def3.png)

 - If the derivative of f exists at x , we say that the function is **differentiable** at x.
 - If the derivative of f exists at x ,  whenever x is between a and b, then we say that f is **defferentiable** on (a,b).
 - The **derivative** of f at the point x , is written as f'(x).
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Calculus1_derivative_written.png)

 - **Derivative is slope !**

<h2 id="f4d55e88765552127f1f67cba00e367f"></h2>

#### Why is f(x) = |x| not differentiable at x =0 ? 

When I say a function is differentiable , what I really mean is that when I zoom in, the function looks like a straight line, but not  `f(x) = |x|` .

f'(0) = lim<sub>x→0</sub> |h|/h , DNE.

 - Why should you care about differentiable function at all ?
    - If a terrible looking function is differentiable , if I zoom in on some point, the thing looks like a straight line. 
    - Calculus is all about replacing the curved objects that we can't understand with straight line , which we have some hope of understanding.

---

<h2 id="96bad87f34b364bbd46c6a9956c56a84"></h2>

#### How does wiggling x affect f(x) ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/caculus1_slope_f201.png)

f'(x) = 3x , f(2) = 4,  f(2.01) = ? 

f(2.01) = f(2) + 0.01·f'(2) = 4 + 0.01·6 = 4.06.


---

<h2 id="7b4dd7708b6861a409a55f8ae5f03d2f"></h2>

### Why would I care to find derivatives ?

<h2 id="233cda2b0da7e06ce36ab30e5002482a"></h2>

#### Why is sqrt(9999) so close to 99.995? 

 - √9999 = √(10000-1) ≈ √10000 - 1·(derivate at 10000) = 100 - 1· 1/(2·100) = 100 - 0.005 = 99.995


<h2 id="e89d54795bc4804fe364603cdb6baed4"></h2>

#### What information is recorded in the sign of the derivative ?

```
f(x+h) ≈ f(x) + h·f'(x) 
```

It means that if the sign of f'(x) is negative , f(x+h) is decreasing , otherwise it is increasing.

---

<h2 id="164411132b76dd8051c2291ff508048b"></h2>

### How do differentiability and continuity relate ? 

<h2 id="399fa607fbcbfea19b9078d5cac8c8e7"></h2>

#### Why is a differentiable function necessarily continuous ?

 - Theorem :  if *f* is differentiable at *a* , then *f* is continuous at *a*.
    - 可微必(原)连续
 - Proof:
    - if f'(a) exist , then  lim<sub>x→a</sub> (f(x)-f(a)) = 0·f'(a) = 0 
    - that means  f(x) = f(a) , while lim<sub>x→a</sub> , it is the definition of continuity. 

<h2 id="d20283b049281436b4b7c193d945d561"></h2>

#### 可微分、连续与可导的关系？

 - 一元函数：
    - 可导必 连续，连续推不出可导，
    - 可导与可微等价。
 - 多元函数：
    - 可偏导与连续之间没有联系，也就是说可偏导推不出连续，连续推不出可偏导。
    - 可微必可偏导，可微必连续，可偏导推不出可微，但若一阶偏导具有连续性则可推出可微。
        - 某点处偏导数存在与否与该点连续性无关.（即使所有偏导数都存在也不能保证该点连续）.
        - 偏导数存在是可微的必要条件,但非充分条件（可微一定偏导数存在,反之不然）； 
        - 偏导数存在且偏导数连续是可微的充分条件,但非必要条件（偏导数存在且(导)连续一定可微,反之不然）.


---

<h2 id="03435db2c86b05d2ec72446257663903"></h2>

### How do I find the derivative ?

 - `d/dx xⁿ = n·xⁿ⁻¹`

---

<h2 id="f196de79cd46bd81851a3f8fed50f480"></h2>

### How do I differentiate a product ?

```
d/dx (f(x)·g(x)) = f'(x)·g(x) + f(x)·g'(x)
```

```
d/dx ((1+2x)·(1+x²)) 
    = 2·(1+x²) + (1+2x)·2x 
    = 2 + 2x² + 2x + 4x² 
    = 2 + 2x + 6x²
```
 
Why is it true ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculus_one_derivative_of_product_area_change.png)

---

<h2 id="1fd4d879c6db3b22c521e30c2fb08385"></h2>

### How do I differentiate a quotient ?

```
Let h(x) = f(x)/g(x).

If g(a) ≠ 0 , and 
    f and g are differentiable at a , then
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_derivative_quotient_rule.png)


下乘上导，减上乘下导，除以 下下

--- 

<h2 id="1288f1095d59ece946013bc62c26a401"></h2>

### d/dx is just a function

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusOne_ddx_is_func.png)


---

## Extreme values 

### How can I find extreme values ?

 - If either f'(c) does not exist , or f'(c) = 0 , call *c* a ***critical point*** of f.
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculusone_derivative_func_graph.png)


### How do I differentiate eˣ ?

f(x) = 1 + x + x²/2 + x³/6 + x⁴/24 + ...  = eˣ

---

## Chain Rule

### China Rule

 - d/dx g(f(x)) = g'(f(x))·f'(x)
    - d/dx g(f(x))  :  change in g(f(x)) / change in x
    - g'(f(x)) :   change in g(f(x)) / change in f(x)
    - f'(x)  :  change in f(x) / change in x






------




  [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/ex_constructor.png
