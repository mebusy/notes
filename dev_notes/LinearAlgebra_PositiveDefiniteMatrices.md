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

