[](...menustart)

- [6 Positive Definite Matrices](#c4ac5577c068be490d5dc0e124314e32)
    - [6.1 MINIMA , MAXIMA , AND SADDLE POINTS](#b7b91c67e89390f8298af104c60585f7)
        - [Definite versus Indefinite: Bowl versus Saddle  (TODO)](#e0e36c552eecb66daf84e448cf5ed7e8)
        - [Higher Dimensions: Linear Algebra](#e59a80ec6d81dedf197cebeea3a20a00)
    - [6.2 TESTS FOR POSITIVE DEFINITENESS](#76c7d53a0682ab1c09ff64d5d3549d0f)
        - [Positive Definite Matrices and Least Squares](#01201db7b9090769e9708a314cf02459)
        - [Semidefinite Matrices](#3a253363875ecbb15417db17ec79c263)
        - [Ellipsoids in n Dimensions](#1eaac00e8e99433d989fe0d999f52f5d)
        - [The Law of Inertia](#7d343fcdccb1d971e655a18f0ae0cb60)
        - [The Generalized Eigenvalue Problem (TODO)](#f2b49424030a50bcf8c0ca9cd03ed896)
    - [6.3 SINGULAR VALUE DECOMPOSITION](#d8d1378d745dd94a25a4c239c7c6702b)
        - [Applications of the SVD](#21c1532cf380b35ae96c0d9ac3e130b0)
            - [1. Image processing](#d16545b4b82233fb918b1cb0cb4c09d1)
            - [4. Least squares  TODO](#9cd2bf30f6aa7178d87488ff1960bc07)
    - [6.4 MINIMUM PRINCIPLES  TODO](#fff4369d5b0d5f3458ca8c052d7c2174)
    - [6.5 THE FINITE ELEMENT METHOD  TODO](#913394de1beecf34e858dc7068c2ee86)

[](...menuend)


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


![](../imgs/LA_minima_example.png)

Thus (x,y) = (0,0) is a stationary point for both functions.  The surface z = F(x,y) is tangent to the horizontal plane z = 7 , and the surface z = f(x,y) is tangent to the plane z = 0.  The question is whether the graphs *go above those planes or not*, as we move away from the tangency point x = y = 0.

***Remark 3*** The second derivatives at (0, 0) are decisive:

![](../imgs/LA_minima_remark3.png)

These second derivatives 4, 4, 2 contain the answer. Since they are the same for F and f, they must contain the same answer. The two functions behave in exactly the same way near the origin. ***F has a minimum if and only if f has a minimum***. I am going to show that those functions don't!

***Remark 4*** The *higher-degree terms* in F have no effect on the question of a local minimum, but they can prevent it from being a global minimum. In our example the term -x³ must sooner or later pull F toward -∞. For f(x, y), with no higher terms, all the action is at (0, 0).

*Every quadratic form f = ax² + 2bxy + cy² has a stationary point at the origin, where ∂f/∂x = ∂f/∂y = 0.*  A local minimum would also be a global minimum. The surface z = f (x, y) will then be shaped like a bowl, resting on the origin (Figure 6.1).

![](../imgs/LA_F6.1.png)

![](../imgs/LA_graph_x2_2xy_y2.png)

> function graph of f = x² + 2xy + y²

If the stationary point of F is at x = α, y = β, the only change would be to use the second derivatives at α, β:  

![](../imgs/LA_minima_quad_part_of_F.png)

This f(x, y) behaves near (0, 0) in the same way that F(x, y) behaves near (α, β).


The third derivatives are drawn into the problem when the second derivatives fail to give a definite decision. That happens when the quadratic part is singular. For a true minimum, f is allowed to vanish only at x = y = 0. When f(x, y) is strictly positive at all other points (the bowl goes up), it is called ***positive definite***.

<h2 id="e0e36c552eecb66daf84e448cf5ed7e8"></h2>

### Definite versus Indefinite: Bowl versus Saddle  (TODO)

TODO

<h2 id="e59a80ec6d81dedf197cebeea3a20a00"></h2>

### Higher Dimensions: Linear Algebra

Calculus would be enough to find our conditions F<sub>xx</sub> > 0 and F<sub>xx</sub>F<sub>yy</sub> > F<sub>xy</sub>² for a minimum. But linear algebra is ready to do more, because the second derivatives fit into a symmetric matrix A. The terms ax² and cy² appear *on the diagonal*. The cross derivative 2bxy is split between the same entry b above and below.  A quadratic f(x, y) comes directly from a symmetric 2 by 2 matrix! 

```
xᵀAx in R² :  

ax² + 2bxy + cy² = [x y]⎡a b⎤⎡x⎤.    (4)
                        ⎣b c⎦⎣y⎦
```

This identity (please multiply it out) is the key to the whole chapter.  It generalizes immediately to n dimensions, and it is a perfect shorthand for studying maxima and minima. When the variables are x₁, ... , xn, they go into a column vector x. ***For any symmetric matrix A, the product xᵀAx is a pure quadratic form f(x₁, ... , xn) = a₁₁x₁² + 2a₁₂x₁x₂ + ... + a<sub>nn</sub>x<sub>n</sub>²*** . 


There are no higher-order terms or lower-order terms-only second-order. The function is zero at x = (0, ... , 0), and its first derivatives are zero. The tangent is flat; this is a stationary point. We have to decide if x = 0 is a minimum or a maximum or a saddle point of the function f = xᵀAx.

---

**Example 3** 

```
f = 2x² + 4xy + y² and 

A = ⎡2 2⎤  -> saddle point.
    ⎣2 1⎦
```

![](../imgs/LA_2x2_4xy_y2.png)

> f = 2x² + 4xy + y²

**Example 5**

```
f = 2x₁² - 2x₁x₂ + 2x₂² - 2x₂x₃ + 2x₃² 

    ⎡ 2 -1  0⎤
A = ⎢-1  2 -1⎥
    ⎣ 0 -1  2⎦
```

minimum at (0, 0, 0).

---

Any function F(x₁, ... , xn) is approached in the same way. At a stationary point all first derivatives are zero.  A is the **"second-derivative matrix"** with entries **aᵢⱼ = ∂²F / ∂xᵢ∂xⱼ**. This automatically equals **aⱼᵢ = ∂²F / ∂xⱼ∂xᵢ** , so A is symmetric.  ***Then F has a minimum when the pure quadratic xᵀAx is positive definite.*** These second-order terms control F near the stationary point:


```
Taylor series:   F(x) = F(0) + xᵀ(grad F) + 1/2·xᵀAx + higher order terms.   (6)
```

At a stationary point, grad F = (∂F/∂x₁, ... , ∂F/∂xn) is a vector of zeros. The second derivatives in xᵀAx take the graph up or down (or saddle). If the stationary point is at x₀  instead of 0, F(x) and all derivatives are computed at x₀. Then x changes to x - x₀ on the right-hand side.


The next section contains the tests to decide whether xᵀAx is positive (the bowl goes up from x = 0). Equivalently, the tests decide whether the matrix A is positive definite -- which is the main goal of the chapter.

---

<h2 id="76c7d53a0682ab1c09ff64d5d3549d0f"></h2>

## 6.2 TESTS FOR POSITIVE DEFINITENESS

Which symmetric matrices have the property that xᵀAx > 0 for all nonzero vectors x?

There are 4 or 5 different ways to answer this question, and we hope to find all of them. The previous section began with some hints about the signs of eigenvalues, but that gave place to the tests on a, b, c:

```
A = ⎡a b⎤  is positive definite when a > 0 and ac - b² > 0.
    ⎣b c⎦
```

From those conditions, ***both eigenvalues are positive***.  

- Their product λ₁λ₂ is the determinant ac - b² > 0, so the eigenvalues are either both positive or both negative. 
     - c must be positive
- They must be positive because their sum is the trace a + c > 0.

Looking at a and ac - b², it is even possible to spot the appearance of the ***pivots***. They turned up when we decomposed xᵀAx into a sum of squares:

![](../imgs/LA_sum_of_square.png)

Those coefficients a and (ac - b²)/a are the pivots for a 2 by 2 matrix. For larger matrices the pivots still give a simple test for positive definiteness: xᵀAx stays positive when n independent squares are multiplied by ***positive pivots***.

One more preliminary remark. The two parts of this book were linked by the chapter on determinants. Therefore we ask what part determinants play.

***It is not enough to require that the determinant of A is positive***.

If a = c = -1 and b = 0, then det(A) = 1 but A = -I = negative definite.  The determinant test should apply not only to A itself, giving ac - b² > 0, but also to the 1 by 1 submatrix a in the upper left-hand corner.

The natural generalization will involve all n of the upper left submatrices of A:

![](../imgs/LA_n_submatrices_of_A.png)

Here is the main theorem on positive definiteness, and a reasonably detailed proof:

**6B** ***Each of*** the following tests is a necessary and sufficient condition for the ***real symmetric*** matrix A to be ***positive definite***:

 1. xᵀAx > 0 for all non zero real vectors x.
 2. All the eigenvalues of A satisfy λᵢ > 0.
 3. All the upper left submatrices A<sub>k</sub> have positive determinants.
 4. All the pivots (without row exchanges) satisfy d<sub>k</sub> > 0.

**Proof**:  Condition 1. defines a positive definite matrix. Our first step shows that each eigenvalue will be positive:

```
  If Ax = λx, then xᵀAx = xᵀλx = λ·‖x‖² .
```

***A positive definite matrix has positive eigenvalues, since xᵀAx > 0***.

Now we go in the other direction. If all λᵢ > 0, we have to prove xᵀAx > 0 for every vector x (not just the eigenvectors).

Since symmetric matrices have a full set of orthonormal eigenvectors, any x is a combination c₁x₁ + ... + cnxn. Then

```
Ax = c₁Ax₁ + ... + cnAxn = c₁λx₁ + ... + cnλxn.
```

Because of the orthogonality xᵢᵀxⱼ = 0, and the normalization xᵢᵀxᵢ = 1 , 

```
xᵀAx = (c₁x₁ᵀ + ... + cnxnᵀ )(c₁λx₁ + ... + cnλxn)
     = c₁²λx₁ + ... + cn²λ
```

If every λᵢ > 0, then equation (2) shows that xᵀAx > 0.  Thus condition 2 implies condition 1 .

*If condition 1 holds, so does condition 3*: The determinant of A is the product of the eigenvalues. And if condition 1 holds, we already know that these eigenvalues are positive. But we also have to deal with every upper left submatrix A<sub>k</sub>. The trick is to look at all nonzero vectors whose last n - k components are zero: 

![](../imgs/LA_atAx_n-k_components.png)

Thus A<sub>k</sub> is positive definite. Its eigenvalues (not the same λᵢ!) must be positive. Its determinant is their product, so all upper left determinants are positive.

*If condition 3 holds, so does condition 4* :  According to Section 4.4, the kth pivot d<sub>k</sub> is the ratio of det(A<sub>k</sub>) to det(A<sub>k-1</sub>). If the determinants are all positive, so are the pivots.

*If condition 4 holds, so does condition 1* : We are given positive pivots, and must deduce that xᵀAx > 0. This is what we did in the 2 by 2 case, by completing the square. The pivots were the numbers outside the squares. To see how that happens for symmetric matrices of any size, we go back to *elimination on a symmetric matrix* : A = LDLᵀ .

**Example 1** : Positive pivots 2, 3/2 , 4/3 :

![](../imgs/LA_positive_definite_LDLT.png)

I want to split xᵀAx into xᵀLDLᵀx:

![](../imgs/LA_positive_definite_LDLT_2.png)

So xᵀAx is a sum of squares with the pivots 2, 3/2, and 4/3 as coefficients:

![](../imgs/LA_positive_definite_LDLT_3.png)

Those positive pivots in D multiply perfect squares to make xᵀAx positive. Thus condition 4 implies condition 1 , and the proof is complete.

It is beautiful that elimination and completing the square are actually the same. Elimination removes x₁ from all later equations.  Similarly, the first square accounts for all terms in xᵀAx involving x₁. The sum of squares has the pivots outside. *The multipliers lᵢⱼ are inside* ! You can see the numbers -1/2 and -2/3 inside the squares in the example.

*Every diagonal entry aᵢᵢ must be positive* . As we know from the examples, however, it is ***far from sufficient*** to look only at the diagonal entries.

The pivots dᵢ are not to be confused with the eigenvalues. For a typical positive definite matrix, they are two completely different sets of positive numbers. In our 3 by 3 example, probably the determinant test is the easiest:

```
Determinant test
  det(A₁) = 2, det(A₂) = 3, det(A₃) = det A = 4.
```

The pivots are the ratios d₁ = 2, d₂ = 3/2, d₃ = 4/3. 

Ordinarily the eigenvalue test is the longest computation. For this A we know the λ's are all positive:


```
Eigenvalue test
  λ₁ = 2 - √2, λ₂ = 2, λ₃ = 2 + √2.
```

Even though it is the hardest to apply to a single matrix, eigenvalues can be the most useful test for theoretical purposes. ***Each test is enough by itself***.

---

<h2 id="01201db7b9090769e9708a314cf02459"></h2>

### Positive Definite Matrices and Least Squares

We connected positive definite matrices to pivots (Chapter 1), determinants (Chapter 4), and eigenvalues (Chapter 5). Now we see them in the least-squares problems of Chapter 3, coming from the rectangular matrices of Chapter 2.

The rectangular matrix will be R and the least-squares problem will be Rx = b.  It has m equations with m ≥ n (square systems are included). 

The least-squares choice x̂ is the solution of RᵀRx̂ = Rᵀb.  That matrix A = RᵀRis not only symmetric but positive definite, as we now show -- provided that the n columns of R are linearly independent:

**6C**: The symmetric matrix A is positive definite if and only if

- (V) There is a matrix R with independent columns such that A = RᵀR.

*The key is to recognize xᵀAx as xᵀRᵀRx = (Rx)ᵀ(Rx).*  This squared length ‖Rx‖² is positive (unless x = 0), because R has independent columns. (If x is nonzero then Rx is nonzero.) Thus xᵀRᵀRx  > 0 and RᵀR is positive definite.

It remains to find an R for which A = RᵀR . We have almost done this twice already:

- **Elimination**: A = LDLᵀ = (L√D)(√DLᵀ) . So take R = √DLᵀ .

This ***Cholesky decomposition*** has the pivots split evenly between L and Lᵀ.

- **Eigenvalues**: A = QΛQᵀ = (Q√Λ)(√ΛQᵀ).  So take R = √ΛQᵀ   (3)

A third possibility is R = Q√ΛQᵀ , the ***symmetric positive definite square root*** of A. 

There are many other choices, square or rectangular, and we can see why. If you multiply any R by a matrix Q with orthonormal columns, then (QR)ᵀ(QR) = RᵀQᵀQR = RᵀIR = A. Therefore QR is another choice.

Applications of positive definite matrices are developed in my earlier book ***Introduction to Applied Mathematics*** and also the new ***Applied Mathematics and Scientific Computing***  (see www. wellesleycambridge. com). 

We mention that Ax = λMx arises constantly in engineering analysis. If A and M are positive definite, this generalized problem is parallel to the familiar Ax = λx, and A > 0. M is a mass matrix for the finite element method in Section 6.4.


<h2 id="3a253363875ecbb15417db17ec79c263"></h2>

### Semidefinite Matrices

The tests for semidefiniteness will relax xᵀAx > 0, A > 0, d > 0, and det > 0, to allow zeros to appear. The main point is to see the analogies with the positive definite case.

**6D**:  Each of the following tests is a necessary and sufficient condition for it symmetric matrix A to be ***positive smidefinite***:

 1. xᵀAx ≥ 0 for all vectors x.  ( non zero real vectos for positive definite )
 2. All the eigenvalues of A satisfy λᵢ ≥ 0.
 3. No principal submatriccs have negative determinants.   
 4. No pivots are negative.
 5. There is a matrix R, possibly with dependent columns, such that A = RᵀR.

The diagonalization A = QΛQᵀ leads to xᵀAx = xᵀQΛQᵀx = yᵀΛy. If A has rank r, there are r nonzero λ's and r perfect squares in yᵀΛy = λ₁y₁² + ... + λᵣyᵣ² .

***Note*** The novelty is that condition 3' applies to all the principal submatrices, not only those in the upper left-hand corner. Otherwise, we could not distinguish between two matrices whose upper left determinants were all zero:


```
⎡0 0⎤ is positive semidefinite , and ⎡0  0⎤ is negative semidefinite.  
⎣0 1⎦                                ⎣0 -1⎦
```

A row exchange comes with the same column exchange to maintain symmetry.

**Example 2**

```
    ⎡ 2 -1 -1⎤
A = ⎢-1  2 -1⎥  is positive semidefinite, by all five tests:
    ⎣-1 -1  2⎦
```

 1. xᵀAx = (x₁ - x₂)² + (x₁ - x₃)² + (x₂ - x₃)² > 0 (zero if x₁ = x₂ = x₃)  
 2. The eigenvalues are 0, λ₁ = 0 , λ₂ = λ₃ = 3 (a zero eigenvalue).
 3. det A = 0 and smaller determinants are positive.
 4. ![](../imgs/LA_positive_semidefinite_example_2_test_4.png)
 5. A = RᵀR with dependent columns in R:
     - ![](../imgs/LA_positive_semidefinite_example_2_test_5.png)


***Remark***: The conditions for semidefiniteness could also be deduced from the original conditions 1~5 for definiteness by the following trick: Add a small multiple of the identity, giving a positive definite matrix A + εI. Then let ε approach zero. Since the determinants and eigenvalues depend continuously on ε, they will be positive until the very last moment. At ε = 0 they must still be nonnegative.

My class often asks about *unsymmetric* positive definite matrices. I never use that term.  One reasonable definition is that the symmetric part 1/2 (A + Aᵀ) should be positive definite. That guarantees that *the real parts of the eigenvalues are positive*.  But it is not necessary: 

```
A = ⎡1 4⎤ has λ > 0 , but 1/2(A + Aᵀ) = ⎡1 2⎤ is indefinite.  
    ⎣0 1⎦                               ⎣2 1⎦  
```

If Ax = λx, then xᴴAx = λxᴴx and xᴴAᴴx = λ̅xᴴx .

Adding , 1/2·xᴴ(A+Aᴴ)x = (Re λ)xᴴx > 0 , so that Re λ > 0 . ?


<h2 id="1eaac00e8e99433d989fe0d999f52f5d"></h2>

### Ellipsoids in n Dimensions

For a positive definite matrix and its xᵀAx, we finally get a figure that is curved.  It is an ellipse in two dimensions, and an ellipsoid in n dimensions.

**The equation to consider is xᵀAx = 1**.  A is the identity matrix, this simplifies to x₁² + x₂² + ... + xn² = 1.  This is the equation of the "unit sphere" in Rⁿ. If A = 4I, the sphere gets smaller. The equation changes to 4x₁² + 4x₂² + ... + 4xn² = 1.  Instead of ( 1 , 0, ... , 0), it goes through ( 1/2, 0, ... , 0).  The center is at the origin, because if x satisfies xᵀAx = 1, so does the opposite vector -x.  The important step is to go from the identity matrix to a diagonal matrix:

```
Ellipsoid:

    ⎡4       ⎤
A = ⎢   1    ⎥ , the equation is xᵀAx = 4x₁² + x₂² + 1/9·x₃² = 1. 
    ⎣     1/9⎦
```

Since the entries are unequal (and positive!) the sphere changes to an ellipsoid.

One solution is x = (2, 0, 0) along the first axis. Another is x = (0, 1, 0). The major axis has the farthest point x = (0, 0, 3). It is like a football or a rugby ball, but
not quite -- Those are closer to x₁² + x₂² + 1/2·x₃² = 1.  The two equal coefficients make them circular in the X₁-x₂ plane, and much easier to throw!

Now comes the final step, to allow nonzeros away from the diagonal of A.

**Example 3**:

```
A = ⎡5 4⎤ and  xᵀAx = 5u² + 8uv + 5v² = 1.   
    ⎣4 5⎦     
```

That ellipse is centered at u = v = 0, but the axes are not so clear. The off-diagonal 4s leave the matrix positive definite, but they rotate the ellipse -- its axes no longer line up with the coordinate axes.

![](../imgs/LA_F6.2.png)

> Figure 6.2  its principal axes.

To locate the ellipse we compute λ₁ = 1 and λ₂ = 9.  The unit eigenvectors are (1, -1)/√2 and (1, 1)/√2.  Those are at 45° angles with the u-v axes, and they are lined up with the axes of the ellipse. The way to see the ellipse properly is to rewrite xᵀAx = 1:

**New squares** 

![](../imgs/LA_new_squres_xTAx.png)

λ = 1 and λ = 9 are outside the squares. The eigenvectors are inside. This is different from completing the square to 5·(u + 4/5·v)² + 9/5·v², with the pivots outside.

The first square equals 1 at (1/√2, -1/√2 ) at the end of the major axis. The minor axis is one-third as long, since we need (1/3)² to cancel the 9.

Any ellipsoid xᵀAx = 1 can be simplified in the same way.  *The key step is to diagonalize A = QΛQᵀ* .  We straightened the picture by rotating the axes. Algebraically, the change to y = Qᵀx produces a sum of squares:

```
xᵀAx = (xᵀQ)Λ(Qᵀx) = yᵀΛy = λ₁y₁² + λ₂y₂² + ... + λnyn² = 1.  (5)
```

The major axis has y₁ = 1 / √λ₁ along the eigenvector with the smallest eigenvalue.

The other axes are along the other eigenvectors. Their lengths are 1 / √λ₂ , ... , 1 / √λn . Notice that the λ's must be positive -- the matrix must be positive definite -- or these square roots are in trouble. 

An indefinite equation y₁² - 9y₂² = 1 describes a hyperbola and not an ellipse. A hyperbola is a cross-section through a saddle, and an ellipse is a cross-section through a bowl.

![](../imgs/LA_hyperbola.png)

The change from x to y = Qᵀx rotates the axes of the space, to match the axes of the ellipsoid. In the y variables we can see that it is an ellipsoid, because the equation
becomes so manageable:

**6E**: Suppose A = QΛQᵀ with λᵢ > 0. Rotating y = Qᵀx simplifies xᵀAx = 1 :

```
    xᵀQΛQᵀx = 1 , yᵀΛy = 1 , and λ₁y₁² + ... + λnyn² = 1.
```

This is the equation of an ellipsoid. Its axes have lengths 1 / √λ₁,   ... , 1 / √λn  from the center. In the original x-space they point along the eigenvectors of A.


<h2 id="7d343fcdccb1d971e655a18f0ae0cb60"></h2>

### The Law of Inertia

For elimination and eigenvalues, matrices become simpler by elementary operations. The essential thing is to know which properties of the matrix stay unchanged. 

When a multiple of one row is subtracted from another, the row space, nullspace, rank, and determinant all remain the same.

For eigenvalues, the basic operation was a similarity transformation A → S⁻¹AS (or A → M⁻¹AM). The eigenvalues are unchanged (and also the Jordan form). 

Now we ask the same question for symmetric matrices: *What are the elementary operations and their invariants for xᵀAx* ?

The basic operation on a quadratic form is to change variables. A new vector y is related to x by some nonsingular matrix, x = Cy. The quadratic form becomes yᵀCᵀACy. This shows the fundamental operation on A:

```
Congruence transformation 同余转换

A → CᵀAC for some NONsingular C. (6)
```

The symmetry of A is preserved, since CᵀAC remains symmetric.  The real question is, What other properties are shared by A and CᵀAC ? 

The answer is given by Sylvester's ***law of inertia***.

**6F**: CᵀAC has the same number of positive eigenvahies, negative eigenvalues, and zero eigenvalues as A.

The *signs* of the eigenvalues (and not the eigenvalues themselves) are preserved by a congruence transformation.  In the proof, we will suppose that A is nonsingular. Then CᵀAC is also nonsingular, and there are no zero eigenvalues to worry about.  (Otherwise we can work with the nonsingular A + εI and A - εI, and at the end let ε → 0.)

Proof: skip...

**Example 4**: Suppose A = I. Then CᵀAC = CᵀC is positive definite. Both I and CᵀC haven positive eigenvalues, confirming the law of inertia.

**Example 5**: If A = [ 1 0 ; 0 -1 ] , then CᵀAC has a negative determinant :

```
    det( CᵀAC ) = (detCᵀ) (detA) (detC) = -(det C)² < 0 .
```

Then CᵀAC must have one positive and one negative eigenvalue, like A.

**Example 6**: This application is the important one:

**6G** For am symmetric matrix A,  ***the signs of the pivots agree with the signs of the eigenvalues***. The eigenvalue matrix Λ and the pivot matrix D have the same number of positive entries , negative entries, and zero entries.

We will assume that A allows the symmetric factorization A = LDLᵀ (without row exchanges). 

By the law of inertia, A has the same number of positive eigenvalues as D. But the eigenvalues of D are just its diagonal entries (the pivots). Thus the number of positive pivots matches the number of positive eigenvalues of A.

That is both beautiful and practical. 

It is beautiful because it brings together (for symmetric matrices) two parts of this book that were previously separate: *pivots* and *eigenvalues*. 
It is also practical, because the pivots can locate the eigenvalues:

**A has positive pivots, A- 2I has a negative pivot**

```
    ⎡ 3  3 0⎤        ⎡ 1 3 0⎤
A = ⎢ 3 10 7⎥  A-2I =⎢ 3 8 7⎥ 
    ⎣ 0  7 8⎦        ⎣ 0 7 6⎦
```

A has positive eigenvalues, by our test. But we know that λ<sub>min</sub> *is smaller than* 2, because subtracting 2 dropped it below zero. The next step looks at A - I, to see if λ<sub>min</sub> < 1. (It is, because A - I has a negative pivot.) That interval containing λ is cut in half at every
step by checking the signs of the pivots.

<h2 id="f2b49424030a50bcf8c0ca9cd03ed896"></h2>

### The Generalized Eigenvalue Problem (TODO)

Physics, engineering, and statistics are usually kind enough to produce symmetric matrices in their eigenvalue problems. 

***But sometimes Ax = λx is replaced by Ax = λMx.*** *There are two matrices rather than one*.

TODO


<h2 id="d8d1378d745dd94a25a4c239c7c6702b"></h2>

## 6.3 SINGULAR VALUE DECOMPOSITION

A great matrix factorization has been saved for the end of the basic course. 

UΣVᵀ joins with LU from elimination and QR from orthogonalization (Gauss and Gram-Schmidt).

> hint 1: 

行空间中找个典型向量 v₁， 然后变换到列空间的某个向量 u₁ : `u₁ = Av₁`.

目标是，找出 行空间中的一组标准正交基， 经过矩阵A变化后，得到 列空间中的一组标准正交基 : `AV=U∑` 

```
AV=U∑ => A = U∑V⁻¹ = U∑Vᵀ   (由目标可知，V标准正交，正交矩阵 逆等于转置换)
```


A = UΣVᵀ is known as the "SVD" or the ***singular value decomposition***. 

The SVD is closely associated with the eigenvalue-eigenvector factorization QΛQᵀ of a positive definite matrix. 
The eigenvalues are in the diagonal matrix Λ. 
The eigenvector matrix Q is orthogonal (QᵀQ = I) because eigenvectors of a symmetric matrix can be chosen to be orthonormal.

For most matrices that is not true, and for rectangular matrices it is ridiculous (eigenvalues undefined).  
But now we allow the Q on the left and the Qᵀ on the right to be *any two orthogonal matrices U and Vᵀ* -- not necessarily transposes of each other. Then every matrix will split into A = UΣVᵀ.

The diagonal (but rectangular) matrix Σ has eigenvalues from AᵀA, not from A!
Those positive entries (also called sigma) will be σ1, ... , σᵣ. They are the ***singular values*** of A.
They fill the first r places on the main diagonal of Σ--when A has rank r. The rest of Σ is zero.

With rectangular matrices, the key is almost always to consider AᵀA and AAᵀ. 

**Singular Value Decomposition**:

```
Any m by n matrix A can be factored into 
    A = UΣVᵀ = (orthogonal)(diagonal)(orthogonal)
```

The columns of U (m by m) are eigenvectors of AAᵀ, and the columns of V (n by n) are eigenvectors of AᵀA. 
The r singular values on the diagonal of Σ (m by n) are the square roots of the nonzero eigenvalues of both AAᵀ and AᵀA. 

Because U , V are both orthogonal , so UᵀU = I, VᵀV = I .

**Remark 1** For positive definite matrices, Σ is Λ and UΣVᵀ is identical to QΛQᵀ. For other symmetric matrices, any negative eigenvalues in Λ become positive in Σ.

**Remark 2** U and V give orthonormal bases for *all four fundamental subspaces*:

- first   r  columns of U:  column space of A
- first  m-r columns of U:  left nullspace of A
- first   r  columns of V:  row space of A
- first  n-r columns of V:  nullspace of A

**Remark 3** The SVD chooses those bases in an extremely special way. They are more than just orthonormal. *When A multiplies a column vⱼ of V, it produces σⱼ times a
column of U*. That comes directly from AV = UΣ, looked at a column at a time.

> hint 2

如何找出 U和V ?

**Remark 4** Eigenvectors of AAᵀ and AᵀA must go into the columns of U and V :

```
A = UΣVᵀ
AAᵀ = (UΣVᵀ)(VΣᵀUᵀ) = UΣΣᵀUᵀ  and, similarly,  AᵀA = VΣᵀΣVᵀ. (1)
```

∑ᵀ∑ 是对角矩阵 , 所以，V就是 AᵀA 的特征向量矩阵. U 同理。

*U must be the eigenvector matrix for* AAᵀ. The eigenvalue matrix in the middle is ΣΣᵀ -- which is m by m with σ₁²,...,σᵣ²  on the diagonal.

The V matrix must be the eigenvector matrix for AᵀA. The diagonal matrix ΣᵀΣ has the same σ₁²,...,σᵣ² , but it is n by n.

**Remark 5** There is the reason that Avⱼ = σⱼuⱼ. Start with AᵀAvⱼ = σⱼ²vⱼ:

```
Multiply by 
 
  AAᵀAvⱼ = σⱼ²Avⱼ    (2)
```

This says that Avⱼ is an eigenvector of AAᵀ.  We just moved parentheses to (AAᵀ)(Avⱼ). The length of this eigenvector Avⱼ is σⱼ, because 

```
vᵀAᵀAvⱼ = σⱼ²vⱼᵀvⱼ  gives ‖Avⱼ‖² = σⱼ².
```

So the unit eigenvector Avⱼ/σⱼ = uⱼ. ***In other words, AV = U∑***.

Example 1: This A has only one column: rank r = 1. Then ∑ has only σ₁ = 3:

![](../imgs/LA_svd_example_1.png)

AᵀA is 1 by 1, whereas AAᵀ is 3 by 3.  They both have eigenvalue 9 (whose square root is the 3 in ∑ ).  

The two zero eigenvalues of AAᵀ  leave some freedom for the eigenvectors in columns 2 and 3 of U.  We kept that matrix orthogonal.

```
> [U, S , V] = svd(a)
U =

  -0.33333   0.66667   0.66667
   0.66667   0.66667  -0.33333
   0.66667  -0.33333   0.66667

S =

Diagonal Matrix

   3
   0
   0

V =  1
```
---

Example 2: Now A has rank 2, and AAᵀ = [ 2 -1 ; -1 2 ] with λ = 3 and 1:

![](../imgs/LA_svd_example2.png)

Notice √3 and √1. The columns of U are *left* singular vectors (unit eigenvectors of AAᵀ).  The columns of V are *right* singular vectors (unit eigenvectors of AᵀA).

```
octave:5> a = [-1 1 0  ; 0 -1 1]
a =

  -1   1   0
   0  -1   1

octave:6> [U, S , V] = svd(a)
U =

  -0.70711   0.70711
   0.70711   0.70711

S =

Diagonal Matrix

   1.7321        0        0
        0   1.0000        0

V =

   4.0825e-01  -7.0711e-01   5.7735e-01
  -8.1650e-01  -2.7756e-16   5.7735e-01
   4.0825e-01   7.0711e-01   5.7735e-01

```


---

<h2 id="21c1532cf380b35ae96c0d9ac3e130b0"></h2>

### Applications of the SVD

The SVD is terrific for numerically stable computations, because U and V are orthogonal matrices. 

They never change the length of a vector. Since multiplication by U cannot destroy the scaling.

Of course ∑ could multiply by a large σ or (more commonly) divide by a small σ, and overflow the computer. But still ∑ is as good as possible.It reveals exactly what is large and what is small.  The ratio σ<sub>max</sub> / σ<sub>min</sub> is the ***condition number*** of an invertible n by n matrix. The availability of that information is another reason for the popularity of the SVD. We come back to this in the second application.

--- 
<h2 id="d16545b4b82233fb918b1cb0cb4c09d1"></h2>

#### 1. Image processing

Suppose a satellite takes a picture, and wants to send it to Earth. The picture may contain 1000 by 1000 "pixels"-a million little squares , each with a definite color. Do we must send back 1,000,000 numbers?

The key is in the singular values (in ∑). Typically, some σ's are significant and others are extremely small.  If we keep 20 and throw away 980, then we send only the corresponding 20 columns of U and V.  The other 980 columns are multiplied in UΣVᵀ by the small σ's that are being ignored. *We can do the matrix multiplication as columns times rows* :

```
A = UΣVᵀ = u₁σ₁v₁ᵀ + u₂σ₂v₂ᵀ + ... + uᵣσᵣvᵣᵀ.      (3)
```

Any matrix is the sum of *r* matrices of rank 1( mxn ).   If only 20 terms are kept, we send 20 time 2000 numbers instead of a million (25 to 1 compression).  (20 uᵢ , 20 vᵢ , 20 σᵢ).

The cost is in computing the SVD -- this has become much more efficient, but it is expensive for a big matrix.

多元统计分析中经典的主成分分析就是这样做的。 主成分分析就是对数据的协方差矩阵进行了类似的分解（特征值分解），但这种分解只适用于对称的矩阵，而 SVD 则是对任意大小和形状的矩阵都成立。

只是为了用图像压缩来介绍 SVD 的性质，实际使用中常见的图片格式（png，jpeg等）其压缩原理更复杂，且效果往往更好.


<h2 id="9cd2bf30f6aa7178d87488ff1960bc07"></h2>

#### 4. Least squares  TODO

For a rectangular system Ax = b, the least-squares solution comes from the normal equations AᵀAx̂ = Aᵀb. 

***If A has dependent columns then AᵀA is not invertible and x̂ is not determined*** . Any vector in the nullspace could be added to x̂. We can now complete Chapter 3, by choosing a "best" (shortest) x̂ for every Ax = b.

Ax = b has two possible difficulties: *Dependent rows or dependent columns*. 

With dependent rows, Ax = b may have no solution. That happens when b is outside the column space of A.Instead of Ax = b, we solve AᵀAx̂ = Aᵀb. 

But if A has dependent columns, this x̂  will not be unique. We have to choose a particular solution of AᵀAx̂ = Aᵀb, and we choose the shortest.

***The optimal solution of Ax = b is the minimum length solution of AᵀAx̂ = Aᵀb***. 


TODO


---

<h2 id="fff4369d5b0d5f3458ca8c052d7c2174"></h2>

## 6.4 MINIMUM PRINCIPLES  TODO

<h2 id="913394de1beecf34e858dc7068c2ee86"></h2>

## 6.5 THE FINITE ELEMENT METHOD  TODO


---














