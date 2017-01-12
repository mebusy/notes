...menustart

 - [6 Positive Definite Matrices](#c4ac5577c068be490d5dc0e124314e32)
	 - [6.1 MINIMA , MAXIMA , AND SADDLE POINTS](#b7b91c67e89390f8298af104c60585f7)

...menuend




<h2 id="c4ac5577c068be490d5dc0e124314e32"></h2>
# 6 Positive Definite Matrices

<h2 id="b7b91c67e89390f8298af104c60585f7"></h2>
## 6.1 MINIMA , MAXIMA , AND SADDLE POINTS

Up to now, we have hardly thought about the **signs of the eigenvalues**. 

We couldn't ask whether λ was positive before it was known to be real. Chapter 5 established that every symmetric matrix has real eigenvalues. 

Now we will find a test that can be applied directly to A, without computing its eigenvalues, which will guarantee that all those eigenvalues are positive. 

The test brings together three of the most basic ideas in the book *pivots*, *determinants*, and *eigenvalues*.

---

The signs of the eigenvalues are often crucial. For stability in differential equations, we needed negative eigenvalues so that e<sup>λt</sup> would decay. 

The new and highly important problem is to recognize a ***minimum point***. This arises throughout science and engineering and every problem of optimization. The mathematical problem is to move the second derivative test F" > 0 into n dimensions. Here are two examples:

```
F(x,y) = 7 + 2(x+y)² - ysiny - x³
f(x,y) = 2x² + 4xy + y²
```

Does either F(x, y) or f(x, y) have a minimum at the point x = y = 0 ?

***Remark 1*** The ***zero-order*** terms F(0, 0) = 7 and f(0, 0) = 0 have no effect on the answer. They simply raise or lower the graphs of F and f .

***Remark 2*** The ***linear terms*** give a necessary condition: To have any chance of a minimum, the first derivatives must vanish at x = y = 0:


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_minima_example.png)

Thus (x,y) = (0,0) is a stationary point for both functions.  The surface z = F(x,y) is tangent to the horizontal plane z = 7 , and the surface z = f(x,y) is tangent to the plane z = 0.  The question is whether the graphs *go above those planes or not*, as we move away from the tangency point x = y = 0.

***Remark 3*** The second derivatives at (0, 0) are decisive:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_minima_remark3.png)

These second derivatives 4, 4, 2 contain the answer. Since they are the same for F and f, they must contain the same answer. The two functions behave in exactly the same way near the origin. ***F has a minimum if and only if f has a minimum***. I am going to show that those functions don't!

***Remark 4*** The *higher-degree terms* in F have no effect on the question of a local minimum, but they can prevent it from being a global minimum. In our example the term -x³ must sooner or later pull F toward -∞. For f(x, y), with no higher terms, all the action is at (0, 0).

*Every quadratic form f = ax² + 2bxy + cy² has a stationary point at the origin, where ∂f/∂x = ∂f/∂y = 0.*  A local minimum would also be a global minimum. The surface z = f (x, y) will then be shaped like a bowl, resting on the origin (Figure 6.1).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F6.1.png)

If the stationary point of F is at x = α, y = β, the only change would be to use the second derivatives at α, β:  



This f(x, y) behaves near (0, 0) in the same way that F(x, y) behaves near (α, β).


The third derivatives are drawn into the problem when the second derivatives fail to give a definite decision. That happens when the quadratic part is singular. For a true
 





