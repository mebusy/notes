


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

## Derivative

### What are derivatives

#### definition 

The ***derivative*** of f at the point x is defined to be :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculus1_derivative_def.png)

其他等价的定义：

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Calculus1_derivative_def2.png)  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Calculus1_derivative_def3.png)

If the derivative of f exists at x , we say that the function is ***differentiable*** at x.






------




  [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/ex_constructor.png
