...menustart

- [Orthogonality](#878bcbccb5d63db01d2193f2e15cae28)
    - [3.1 ORTHOGONAL VECTORS AND SUBSPACES](#70835fd4404a5ddec835801ba42ecfb0)
        - [Orthogonal Vectors](#5ef1a2d8f6384823a45b583b55b4eb4f)
        - [Orthogonal Subspaces](#1e3ebdd6bb6b76f4c2c83481ece42bac)
        - [3D Fundamental Theorem of Linear Algebra, Part II](#a59d22eb966cffaaaa70554ec8025d2a)
        - [The Matrix and the Subspaces](#5e674f75381627d3b48028a69ae47b43)
    - [3.2 COSINES PROJECTIONS ONTO LINES](#870df6062f5bb62d6f82187a8efebbe1)
        - [Inner Products and Cosines](#71c346793ba386be5a1d98cd2c34c105)
        - [Projection onto a Line](#20ccf5b7b420465ebecf5702c5d33297)
        - [Projection Matrix of Rank 1](#77cc1691c5dd2037118a1d11e100cad7)
        - [Transposes from Inner Products](#8cccc981ad8d934119049052d2aad585)
    - [3.3 PROJECTIONS LEAST SQUARES](#4a2df06c2d276ad56402eecaa894e5d5)
        - [Least-Squares Problems with Several Variables](#b764f194bfbd3ef0f3c068388cebeea7)
        - [The Cross-Product Matrix of AᵀA](#5757e6b48c83a9147f7bea89ff984a9c)
        - [Projection Matrices](#3922a817bfd16012568e8709192d410c)
        - [Least-Squares Fitting of Data](#52a7cbb3e182ed785dad8c7bc7a8e718)
    - [3.4 ORTHOGONAL BASES AND GRAM-SCHMIDT](#09bbcb83a58fddde91f52c847cd92d46)
        - [Rectangular Matrices with Orthonormal Columns](#30de4e2d90eb5352ce69b4782264cd6b)
        - [The Gram-Schmidt Process](#e8bd1a0d73391e5faccdebb17e16f305)
        - [The Factorization A = QR](#9abeff81b513ce7e5c2268c074e45858)
        - [Function Spaces and Fourier Series](#f7b94cc4db71bd4599e6e5dd3d560808)

...menuend


<h2 id="878bcbccb5d63db01d2193f2e15cae28"></h2>


# Orthogonality

<h2 id="70835fd4404a5ddec835801ba42ecfb0"></h2>


## 3.1 ORTHOGONAL VECTORS AND SUBSPACES

- In choosing a basis, we tend to choose an orthogonal basis , to make those calculations simple. 
- A further specialization makes the basis just about optimal: The vectors should have length 1. 
- For an orthonormal basis (orthogonal unit vectors), we will find:
     - 1. the length ‖x‖ of a vector
     - 2. the test xᵀy = 0 for perpendicular vectors;
     - 3. how to create perpendicular vectors from linearly independent vectors.

More than just vectors, subspaces can also be perpendicular. The 4 fundamental subspaces are perpendicular in pairs, 2 in Rᵐ and 2 in Rⁿ. That will complete the fundamental theorem of linear algebra.


The first step is to find the ***length of a vector***. 

- ***The length ‖x‖ in Rⁿ is the positive square root of xᵀx***


<h2 id="5ef1a2d8f6384823a45b583b55b4eb4f"></h2>


#### Orthogonal Vectors

```bash
Orthogonal vectors    xᵀy = 0 

proof:

    ‖x‖² + ‖y‖² = ‖x+y‖²   # 勾股定理
=>  xᵀx + yᵀy = (x+y)ᵀ(x+y)
=>  xᵀx + yᵀy = xᵀx + xᵀy + yᵀx + yᵀy
# vector inner product leads to scalar , so xᵀy == yᵀx
=>  xᵀx + yᵀy = xᵀx + 2xᵀy + yᵀy 
=>  xᵀy = 0 
```

![](../imgs/LA_inner_product_xTy.png)

> ***zero vector is orthogonal to any vector***.

Useful fact: **If nonzero vectors v₁, ... , vk are mutually orthogonal** (every vector is perpendicular to every other), **then those vectors are linearly independent**.

- The coordinate vectors e₁, ... , en in Rⁿ are the most important orthogonal vectors. 
- Those are the columns of the identity matrix. 
- They form the simplest basis for Rⁿ, and
- they are *unit vectors* - each has length ‖eᵢ‖ = 1. 
- They point along the coordinate axes. 
     - If these axes are rotated, the result is a new **orthonormal basis**: 
     - a new system of *mutually orthogonal unit vectors*. 
- In R² we have cos²θ + sin²θ = 1:
     - **Orthonormal vectors in R2** v₁ = ( cosθ, sinθ ) and v₂ = ( -sinθ, cosθ ).



<h2 id="1e3ebdd6bb6b76f4c2c83481ece42bac"></h2>


#### Orthogonal Subspaces

**Every vector** *in one subspace must be orthogonal to* **every vector** *in the other subspace*.

- Subspaces of ***R³*** can have dimension 0, 1, 2, or 3. 
- The subspaces are represented by lines or planes through the origin
     - and in the extreme cases, by the origin alone or the whole space. 
- The subspace {0} is orthogonal to all subspaces. 
- A line can be orthogonal to another line, or it can be orthogonal to a plane
- **but a plane cannot be orthogonal to a plane in R³**.
     - because 2 orthogonal plane has dimension 4 in total , they must intersect in a line in R³ 
     - 2 vectors in a same line are not orthogonal
     - **2 orthogonal subspace never intersect in any none zero vector**
     - I have to admit that the front wall and side wall of a room look like perpendicular planes in R³. But by our definition, that is not so!
     - 2 planes can be orthogonal in R⁴

**3B**: 

- Two subspaces V and W of the same space Rⁿ are *orthogonal* if every vector v in V is orthogonal to every vector w in W: 
     - vᵀw = 0 for all v and w.

**Example 2**: Suppose V is the plane spanned by v₁ = (1, 0, 0, 0) and v₂ = (1, 1, 0, 0). If W is the line spanned by w = (0, 0, 4, 5), then w is orthogonal to both v's. The line W will be orthogonal to the whole plane V.

In this case, with subspaces of dimension 2 and 1 in R4, there is room for a third subspace. The line L through z = (0, 0, 5, -4) is perpendicular to V and W. Then the dimensions add to 2 + 1 + 1 = 4. What space is perpendicular to all of V, W, and L ?


The important orthogonal subspaces don't come by accident, and they come two at a time. In fact orthogonal subspaces are unavoidable: ***They are the fundamental subspaces***! The first pair is the *nullspace and row space*. Those are subspaces of **Rⁿ** - the rows have n components and so does the vector x in Ax = 0. We have to show, using Ax = 0, that ***the rows of A are orthogonal to the nullspace vector x***.


**3C Fundamental theorem of orthogonality**:  

- The row space is orthogonal to the nullspace (in Rⁿ) , Ax = 0 
- The column space is orthogonal to the left nullspace (in Rᵐ)

***First proof***  Suppose x is a vector in the nullspace. Then Ax = 0 , and this system of *m* equations can be written out as rows of A multiplying x:

```
     | ... row 1 ... | |x₁|   |0|
     | ... row 2 ... |·|x₂| = |0|
Ax = |               | |  |   | |
     |               | |  |   | |
     | ... row m ... | |  |   |0|
                       |xn|
```

- The main point is already in the first equation: row 1 is orthogonal to x. 
     - Their inner product is zero; 
- Every right-hand side is zero, so x is orthogonal to every row. 
     - Therefore x is orthogonal to every combination of the rows. 
- Each x in the nullspace is orthogonal to each vector in the row space, so ***N(A) ⊥ C(Aᵀ)*** .


The other pair of orthogonal subspaces comes from Aᵀy = 0, or yᵀA = 0:

```
      |c       c|
      |o       o|
      |l       l|
yᵀA = |u  ...  u| = [0 ... 0]
      |m       m|
      |n       n|
      |         |
      |1       n|
```

- The equation says , from the zeros on the right-hand side , the vector y is orthogonal to every column.
     - Therefore y is orthogonal to every combination of the columns.
- y is orthogonal to the column space, and it is a typical vector in the left nullspace:
     - ***N(Aᵀ) ⊥ C(A)***



***Second proof***  If x is in the nullspace then Ax = 0. If v is in the row space, it is a combination of the rows: v = Aᵀz for some vector z. Now, in one line:

```
Nullspace ⊥ Row space :   
    vᵀx = (Aᵀz)ᵀx = zᵀAx = zᵀ0 = 0.    (8)
```


**DEFINITION** Given a subspace V of Rⁿ, the space of all vectors orthogonal to V is called the **orthogonal complement** of V. It is denoted by **V<sup>⊥</sup> = "V perp."**  

- the nullspace is the orthogonal complement of the row space
     - A vector z can't be orthogonal to the nullspace but outside the row space
- **Dimension formula**:  dim(row space) + dim(nullspace) = number of columns.
     - r + ( n -r ) = n 
 
<h2 id="a59d22eb966cffaaaa70554ec8025d2a"></h2>


#### 3D Fundamental Theorem of Linear Algebra, Part II

- The nullspace is the *orthogonal complement* of the row space in Rⁿ.
- The left nullspace is the *orthogonal complement* of the column space in Rᵐ.

**3E** Ax = b is solvable if and only if  yᵀb = 0  whenever yᵀA  = 0.

- Ax = b requires b to be in the column space. 
- Ax = b **requires b to be perpendicular to the left nullspace**.


---

<h2 id="5e674f75381627d3b48028a69ae47b43"></h2>


#### The Matrix and the Subspaces

- Splitting Rⁿ into orthogonal parts V and W , will split every vector into x = v + w. 
- The vector v is the projection onto the subspace V. 
- The orthogonal component w is the projection of x onto W. 

Figure 3.4 summarizes the fundamental theorem of linear algebra.

![](../imgs/LA_Figure_3.4.png)

- The nullspace is carried to the zero vector. 
- Every Ax is in the column space. 
- Nothing is carried to the left nullspace. 
- The real action is between the row space and column space, and you see it by looking at a typical vector ***x*** :
     - It has a "row space component" and a "nullspace component," with `x = xᵣ+ xn`,  When multiplied by A, this is `Ax = Axᵣ + Axn`:
     - The nullspace component goes to zero: Axn = 0.
     - The row space component goes to the column space: `Axᵣ = Ax`.

- 事实上, 任意 vector a 都可以拆分 两部分, 一部分是在某个子空间S 上的投影， 另一部分是在 S的正交补 S<sup>⊥</sup> 上的投影
     - *Ia = Pa + P<sup>⊥</sup>a*  =>  **I = P + P<sup>⊥</sup>**
     - S<sup>⊥</sup> 其实就是 法线空间,  **I = P + P<sub>N</sub>**
  
Of course everything goes to the column space - the matrix cannot do anything else. I tried to make the row and column spaces the same size, with equal dimension r.

**3F** From the row space to the column space. A is actually invertible. Every vector b in the column space comes from exactly one vector xᵣ , in the row space.

***Proof*** Every b in the column space is a combination Ax of the columns. In fact, b is Axᵣ with xᵣ in the row space, since the nullspace component gives Ax = 0. If another vector x, in the row space gives Ax'ᵣ = b, then A(xᵣ - x'ᵣ) = b - b = 0. This puts xᵣ - x'ᵣ in the nullspace and the row space, which makes it orthogonal to itself. Therefore it is zero, and xᵣ = x'ᵣ . Exactly one vector in the row space is carried to b.

> ***Every matrix transforms its row space onto its column space.***

On those r-dimensional spaces A is invertible (if x in row space ). On its nullspace A is zero. When A is diagonal, you see the invertible submatrix holding the r nonzeros.


Aᵀ goes in the opposite direction, from Rᵐ to Rⁿ and from C(A) back to C(Aᵀ). Of course the transpose is not the inverse! Aᵀ moves the spaces correctly, but not the individual vectors. That honor belongs to A⁻¹ if it exists - and it only exists if r = m = n. We cannot ask A⁻¹ to bring back a whole nullspace out of the zero vector.

When A⁻¹ fails to exist, the best substitute is the ***pseudoinverse*** A⁺. This inverts A where that is possible: A⁺Ax = x for x in the row space. On the left nullspace, nothing can be done: A⁺y = 0. Thus A⁺ inverts A where it is invertible, and has the same rank r. One formula for A⁺ depends on the ***singular value decomposition*** - for which we first need to know about eigenvalues.



<h2 id="870df6062f5bb62d6f82187a8efebbe1"></h2>


## 3.2 COSINES PROJECTIONS ONTO LINES


![](../imgs/LA_projection_onto_line.png)

**Figure 3.5** The projection p is the point ( on the line through a ) closest to b.

The situation is the same when we are given a plane (or any subspace S) instead of a line. Again the problem is to find the point p on that subspace that is closest to b. ***This point p is the projection of b onto the subspace***. Geometrically, that gives the distance between points b and subspaces S. But there are two questions that need to be asked:

 1. Does this projection actually arise in practical applications?
 2. If we have a basis for the subspace S, is there a formula for the projection p ?

The answers are certainly yes. This is exactly the problem of the ***least-squares*** solution to an overdetermined system. The vector b represents the data from experiments or questionnaires, and it contains too many errors to be found in the subspace S. The equations are inconsistent, and Ax = b has no solution.

The least-squares method selects p as the best choice to replace b. 

A formula for p is easy when the subspace is a line.   Projection onto a higher dimensional subspace is by far the most important case; it corresponds to a least-squares problem with several parameters. The formulas are even simpler when we produce an orthogonal basis for S.


<h2 id="71c346793ba386be5a1d98cd2c34c105"></h2>


#### Inner Products and Cosines

Relationship of inner products and angles.

![](../imgs/LA_innerProduct_and_angle.png)

Figure 3.6 The cosine of the angle θ = β - α using inner products.

- The length ‖a‖ is the hypotenuse 斜边 in the triangle OαQ. 
     - So the sine and cosine of a are : `sinα = a₂/‖a‖ , cosα = a₁/‖a‖` 
     - For the angle β , `sinα = b₂/‖b‖ , cosα = b₁/‖b‖` 
     - **cosθ = cos(β - α) = cosβcosα + sinβsinα = ( a₁b₁ + a₂b₂ ) / ‖a‖·‖b‖**  ,  (1)

The numerator in formula (1) is exactly the inner product of a and b. It gives the relationship between aᵀb and cos θ:

**3G** The cosine of the angle between any *nonzero vectors* a and b is :  

```
    cosθ = aᵀb / ‖a‖·‖b‖  (2)
```



<h2 id="20ccf5b7b420465ebecf5702c5d33297"></h2>


#### Projection onto a Line

![](../imgs/LA_projection_onto_line2.png)

- Now we want to find the projection point p. 
- This point must be some multiple p = x̂a of the given vector a 
     - every point on the line is a multiple of a. 
- The problem is to compute the coefficient `x̂`. 
- All we need is the geometrical fact that ***the line from b to the closest point p = x̂a is perpendicular to the vector a***:

```
      (b - x̂a) ⊥ a ,  
  or  aᵀ(b - x̂a) = 0 ,  
  or  x̂ = (aᵀb / aᵀa)   (4)
```

That gives the formula for the number x̂ and the projection p:

**3H** The projection of the vector b onto the line in the direction of a is p = x̂a:

![](../imgs/LA_projection_onto_a_line.png)

This leads to the **Schwarz inequality** in equation (6), which is the most important inequality in mathematics.  A special case is the fact that arithmetic means ½(x + y) ≥ geometric mean  √xy . 

```
Schwarz inequality:  |aᵀb| ≤ ‖a‖·‖b‖    (6)
```

All vectors a and b satisfy the ***Schwarz inequality***, which is |cosθ| ≤ 1 in Rⁿ.

One final observation about `|aᵀb| ≤ ‖a‖·‖b‖` . Equality holds *if and only if* b is a multiple of a. The angle is θ = 0° or θ = 180° and the cosine is 1 or -1. In this case b is identical with its projection p, and the distance between b and the line is zero.


<h2 id="77cc1691c5dd2037118a1d11e100cad7"></h2>


#### Projection Matrix of Rank 1

The projection of *b* onto the line through *a* lies at p = a(aᵀb/aᵀa). That is our formula p = x̂a, but the vector *a* is put before the number x̂ = aᵀb/aᵀa. Projection onto a line is carried out by a ***projection matrix P***, and written in this new order we can see what it is. 

P is the matrix that multiplies b and produces p:

```
    p = Pb ,  P = aaᵀ/aᵀa    (7)
```

That is a column times a row, **a square matrix**,  divided by the number aᵀa .  (aaᵀ 是一个秩1矩阵)

This matrix has two properties that we will see as typical of projections:

 1. **P is a symmetric matrix**.    ( aaᵀ 对称)
 2. **Its square is itself: P²= P**.


Every column is a multiple of a, and so is Pb = x̂a. The vectors that project to p = 0 are especially important. They satisfy aᵀb = 0 -- they are perpendicular to a and their component along the line is zero. They lie in the nullspace , the perpendicular plane.

Actually that example is too perfect. It has the nullspace orthogonal to the column space, which is haywire. The nullspace should be orthogonal to the row space. But because P is symmetric, its row and column spaces are the same.

**Remark on scaling**: The projection matrix aaᵀ/aᵀa  is the same if a is doubled:

- if a = [1 1 1]ᵀ , P 的所有元素 = 1/3 
- if a = [2 2 2]ᵀ , P 的所有元素仍然 = 1/3 


The line through a is the same, and that's all the projection matrix cares about. If a has unit length, the denominator is aᵀa = 1 and the matrix is just P = aaᵀ .

Example 3: Project onto the "θ-direction" in the x-y plane. The line goes through *a = (cosθ, sinθ)* and the matrix is symmetric with P² = P:

![](../imgs/LA_3.2_example3.png)

Here c is cosθ, s is sinθ, and c2 + s2 = 1 in the denominator. This matrix P was discovered in Section 2.6 on linear transformations. Now we know P in any number of dimensions. We emphasize that it produces the projection p:


***To project b onto a, multiply by the projection matrix P:  p = Pb***

---

<h2 id="8cccc981ad8d934119049052d2aad585"></h2>


#### Transposes from Inner Products

Finally we connect inner products to Aᵀ. Up to now, Aᵀ is simply the reflection of A across its main diagonal; the rows of A become the columns of Aᵀ, and vice versa. The entry in row i, column j of Aᵀ is the (j, i) entry of A:

 **Transpose by reflection**: (Aᵀ)ᵢⱼ = (A)ⱼᵢ

There is a deeper significance to Aᵀ. Its close connection to inner products gives a new and much more "abstract" definition of the transpose:

**3J** The transpose Aᵀ can be defined by the following property:  

- The inner product of Ax with y equals the inner product Of x with Aᵀy. Formally, this simply means:

```
    (Ax)ᵀy = xᵀAᵀy = xᵀ(Aᵀy)     (8)
```

This definition gives us another (better) way to verify the formula (AB)ᵀ = BᵀAᵀ. Use equation (8) twice:

```
Move A then move B: 
    (ABx)ᵀy = (Bx)ᵀ(Aᵀy) = xᵀ(BᵀAᵀy)
```

The transposes turn up in reverse order on the right side, just as the inverses do in the formula (AB)⁻¹ = B⁻¹ A⁻¹. We mention again that these two formulas meet to give the remarkable combination (A⁻¹)ᵀ = (Aᵀ)⁻¹ .


<h2 id="4a2df06c2d276ad56402eecaa894e5d5"></h2>


## 3.3 PROJECTIONS LEAST SQUARES

Up to this point, Ax = b either has a solution or not. If b is not in the column space C(A), the system is inconsistent and Gaussian elimination fails. This failure is almost certain when there are several equations and only one unknown:

```
    More equations     2x = b₁
    than unknowns-    3x = b₂
    no solution?    4x = b₃
```

This is solvable when b1, b2, b3 are in the ratio 2:3:4. The solution x will exist only if b is on the same line as the column a = (2, 3, 4).

In spite of their unsolvability, inconsistent equations arise all the time in practice. They have to be solved!  Rather than expecting no error in some equations and large errors in the others, it is much better to *choose the x that minimizes an average error E in the m equations*.

The most convenient "average" comes from the *sum of squares*:

```
Squared error  
    E² = (2x-b₁)² + (3x-b₂)² + (4x-b₃)² .
```

- If there is an exact solution, the minimum error is E = 0. 
- In the more likely case that b is not proportional to a, the graph of E² will be a parabola ( para 'beside' + bolē 'a throw' -> 抛物线). The minimum error is at the lowest point, where the derivative is zero:

```
dE²/dx = 2[(2x-b₁)2 +(3x-b₂)3 +(4x-b₃)4] = 0. 
```

Solving for x, the least-squares solution of this model system ax = b is denoted by x̂ :  (you need some calculus)

![](../imgs/LA_least_square_solution_example.png)  

**3K**:  The least-squares solution to a problem ax = b  in one unknon is x̂ = aaᵀ/aᵀa .

<h2 id="b764f194bfbd3ef0f3c068388cebeea7"></h2>


#### Least-Squares Problems with Several Variables

Now we are ready for the serious step, to ***project b onto a subspace*** . This problem arises from Ax = b when A is an m by n matrix.   The number m of observations is still larger than the number n of unknowns, so it must be expected that Ax = b will be inconsistent. *Probably, there will not exist a choice of x that perfectly fits the data b*. In other words, the vector b probably will not be a combination of the columns of A; it will be outside the column space.

Again the problem is to choose x̂ so as to minimize the error, and again this minimization will be done in the least-squares sense. The error is E = ‖Ax - b‖, and ***this is exactly the distance from b to the point Ax in the column space***. Searching for the least-squares solution x̂ , which minimizes E, is the same as locating the point p = Ax̂ that is closer to b than any other point in the column space.

We may use geometry or calculus to determine x̂ . In n dimensions, we prefer the appeal of geometry; p must be the "projection of b onto the column space." The error vector e = b - Ax̂ must be perpendicular to that space (Figure 3.8). Finding x̂ and the projection p = Ax̂ is so fundamental that we do it in two ways:

![](../imgs/LA_F3.8.png)

 1. All vectors perpendicular to the column space lie in the left nullspace. Thus the error vector e = b - Ax̂ must be in the nullspace of Aᵀ:
     - `Aᵀ(b-Ax̂) = 0  , or AᵀAx̂ = Aᵀb`
     - 在坏方程左右乘上 Aᵀ ,就是好方程。 AᵀA 是本章的核心
 2. The error vector must be perpendicular to each column a₁ , ... , an of A:
     - ![](../imgs/LA_errorVector_perpend_t_column.png)
     - This is agin `Aᵀ(b-Ax̂) = 0  , or AᵀAx̂ = Aᵀb`.

The fastest way is just to multiply the unsolvable equation Ax = b by Aᵀ. All these equivalent methods produce a square coefficient matrix AᵀA. It is symmetric (its transpose is not AAᵀ!) and it is the fundamental matrix of this chapter.

The equations AᵀAx̂ = Aᵀb are known in statistics as the **normal equations**.


**3L**:  

- When Ax b is inconsistent, its least-squares solution minimizes ‖Ax - b‖²  
     - **normal equations** :  `AᵀAx̂ = Aᵀb`     (1)
- AᵀA is invertible exactly when the columns of A are linearly independent! Then,
     - **Best estimate x̂**:  `x̂ = (AᵀA)⁻¹Aᵀb`        (2)
- The projection of b onto the column space is the nearest point Ax̂:
     - **Projection**:  `p = Ax̂ = A·(AᵀA)⁻¹Aᵀb`     (3)
     - `also:  p = Pb = A(AᵀA)⁻¹Aᵀ·b`


Remark:

 1. Suppose b is actually in the column space of A. Then the projection of b is still b:
     - **b in column space**:  *p = A(AᵀA)⁻¹Aᵀ·Ax = Ax = b* .
     - The closest point p is just b itself.
 2. At the other extreme, suppose b is perpendicular to every column, so Aᵀb = 0. In this case b projects to the zero vector
     - **b in left nullspace**:  *p = A(AᵀA)⁻¹Aᵀ·b = A(AᵀA)⁻¹ 0 = 0*.
 3. When A is square and invertible, the column space is the whole space. Every vector projects to itself, p equals b, and x = x̂:
     - **If A is invertible**:  *p = A(AᵀA)⁻¹Aᵀ·b = AA⁻¹(Aᵀ)⁻¹Aᵀ b = b*.
 4. Suppose A has only one column, containing a. Then the matrix AᵀA is the number aᵀa and x̂ is aᵀb/aᵀa. We return to the earlier formula.


<h2 id="5757e6b48c83a9147f7bea89ff984a9c"></h2>


#### The Cross-Product Matrix of AᵀA

The matrix AᵀA is certainly symmetric. Its transpose is (AᵀA)ᵀ = AᵀAᵀᵀ, which is AᵀA again. Its i, j entry (and j, i entry) is the inner product of column i of A with column j of A. The key question is the invertibility of AᵀA, and fortunately：

>**AᵀA has the same nullspace as A.**

Certainly if Ax = 0 then AᵀAx = 0. Vectors x in the nullspace of A are also in the nullspace of AᵀA. 

To go in the other direction, start by supposing that AᵀAx = 0, and take the inner product with x to show that Ax = 0:

```
  xᵀAᵀAx = 0,  or ‖Ax‖² = 0 ,  or Ax = 0.
```

The two nullspaces are identical. In particular, if A has independent columns (and only x = 0 is in its nullspace), then the same is true for AᵀA:

**3M** If A has independent columns, then AᵀA is square, symmetric, and invertible.

We show later that AᵀA is also positive definite (all pivots and eigenvalues are positive). This case is by far the most common and most important. Independence is not so hard in m-dimensional space if m > n. We assume it in what follows.

---

<h2 id="3922a817bfd16012568e8709192d410c"></h2>


#### Projection Matrices

We have shown that the closest point to b is p = A(AᵀA)⁻¹Aᵀb. This formula expresses in matrix terms the construction of a perpendicular line from b to the column space of A. The matrix that gives p is a projection matrix, denoted by P:

```
  Projection Matrix:  P = A(AᵀA)⁻¹Aᵀ    (4)
```

- This matrix projects any vector b onto the column space of A.  
    - In other words, p = Pb is the component of b in the column space, 
    - and the error e = b - Pb is the component in the orthogonal complement. 
- I - P is also a projection matrix! 
     - It projects b onto the orthogonal complement, 
     - and the projection is b - Pb (e).

In short, we have a matrix formula for splitting any b into two perpendicular components. Pb is in the column space C(A), and the other component (I - P)b is in the left nullspace N(AT) - which is orthogonal to the column space.

These projection matrices can be understood geometrically and algebraically.

**3N** The projection matrix P = A(AᵀA)⁻¹Aᵀ has two basic properties:

 1. It equals its square: P² = P.
 2. It equals its transpose: Pᵀ = P

Conversely, any symmetric matrix with P² = P represents projection.

***Proof*** It is easy to see why P² = P. 

To prove that *P* is also symmetric, take its transpose. Multiply the transposes in reverse order, and use symmetry of (AᵀA)⁻¹, to come back to P:

```
    Pᵀ = (Aᵀ)ᵀ((AᵀA)⁻¹)ᵀAᵀ 
       = A((AᵀA)ᵀ)⁻¹Aᵀ 
       = A(AᵀA)⁻¹Aᵀ = P.
```

For the converse, we have to deduce from P² = P and Pᵀ = P that Pb ***is the projection of b onto the column space of P***. The error vector b - Pb is orthogonal to the space. For any vector Pc in the space, the inner product is zero:

```
    // PS: (I-P)ᵀ = (I-P)
    (b-Pb)ᵀPc = bᵀ(I-P)ᵀPc=bᵀ(P-P²)c = 0.  

```

Thus b - Pb is orthogonal to the space, and Pb is the projection onto the column space.

Suppose A is actually invertible. If it is 4 x 4, then its four columns are independent and its column space is all of R⁴. What is the projection onto the whole space? It is the identity matrix.

```
  P = A(AᵀA)⁻¹Aᵀ = AA⁻¹(Aᵀ)⁻¹Aᵀ = I.  (5)
```

The identity matrix is symmetric, I² = I, and the error b - Ib is zero.

To repeat: We cannot invert the separate parts Aᵀ and A when those matrices are rectangular. It is the square matrix AᵀA that is invertible , not Aᵀ and A.

---

<h2 id="52a7cbb3e182ed785dad8c7bc7a8e718"></h2>


#### Least-Squares Fitting of Data

Suppose we do a series of experiments, and expect the output b to be a linear function of the input t. We look for a ***straight line*** b = C + Dt. 

```
    C + Dt₁ = b₁
    C + Dt₂ = b₂
        ...
    C + Dtm = bm
```

This is an *overdetermined* system, with m equations and only two unknowns. If errors are present, it will have no solution. A has two columns, and x = (C, D) : 

```
|1 t₁|        |b₁|
|1 t₂| |C|  = |b₂|   , or Ax = b.   (7)
| .  | |D|    |. |
|1 tm|        |bm|
```

The best solution (Ĉ, D̂) is the x̂ that minimizes the squared error E².

![](../imgs/LA_F3.9.png)

The vector p = Ax̂ is as close as possible to b. (Figure 3.9). On the graph, the errors are the ***vertical distances*** `b - C - Dt` to the straight line (not perpendicular distances!). It is the vertical distances that are squared, summed, and minimized.

```
    |1 -1| |C|  |1|
    |1  1|·|D| =|1|.
    |1  2|      |3|
```

If those equations Ax = b could be solved, there would be no errors. They can't be solved because the points are not on a line. Therefore they are solved by least squares:

```bash
AᵀAx̂ = Aᵀb  is :  |3 2|·|Ĉ|= |5|
                  |2 6| |D̂|  |6|
```

The best solution is Ĉ = 9/7, D̂ = 4/7 and the best line is `9/7 + 4/7·t`.

Note the beautiful connections between the two figures. The problem is the same but the art shows it differently. In Figure 3.9b, b is not a combination of the columns (1, 1, 1) and (-1, 1, 2). In Figure 3.9, the three points are not on a line. Least squares replaces points b that are not on a line by points p that are! ***Unable to solve Ax = b, we solve Ax̂ = p***.

- Figure 3.9b is in three dimensions (or m dimensions if there are m points) 
- and Figure 3.9a is in two dimensions (or n dimensions if there are n parameters).

**3O**  The measurements b₁, ..., bm are given at distinct points t₁ , ..., tm. Then the straight line C + Dt which minimizes E² comes from least squares:

![](../imgs/LA_3O.png)

---

Normal equation 也可以用来拟合2次曲线. eg. 过原点的2次曲线 Ct + Dt² = y. 

eg.  (1,1) , (2,5) , (-1,-2)

```
    ⎡ 1  1⎤         ⎡ 1⎤
A = ⎢ 2  4⎥ ,   b = ⎢ 5⎥
    ⎣-1  1⎦         ⎣-2⎦
```

A 第1列是 t, 第2列是 t².

--- 

TODO **Weighted Least Squares**

---

<h2 id="09bbcb83a58fddde91f52c847cd92d46"></h2>


## 3.4 ORTHOGONAL BASES AND GRAM-SCHMIDT

In an orthogonal basis, every vector is perpendicular to every other vector. The coordinate axes are mutually orthogonal. That is just about optimal, and the one possible improvement is easy: Divide each vector by its length, to make it a unit vector. That changes an ***orthogonal*** basis into an ***orthonormal*** basis of q's:

**3P** The vectors q₁, ..., qn are ***orthonormal*** if 

```
qᵢᵀqⱼ = ⎰ 0 whenever i ≠ j, giving the orthogonality; 
        ⎱ 1 whenever i = j, giving the normalization.
```

***A matrix with orthonormal columns will be called Q***. ( square or rectangular )
 
The most important example is the *standard basis*. For the x-y plane, the bestknown axes e₁ = (1, 0) and e₂ = (0, 1) are not only perpendicular but horizontal and vertical. Q is the 2 x 2 identity matrix. In n dimensions the standard basis e₁, ... , en again consists of *the columns of Q = I*:

```
               |1|       |0|             |0|
Standard       |0|       |1|             |0|
 basis    e₁ = |0|, e₂ = |0|, ... , en = |0|
               |.|       |.|             |.|
               |0|       |0|             |1|
```

That is not the only orthonormal basis! We can rotate the axes without changing the right angles at which they meet. These rotation matrices will be examples of Q.

If we have a subspace of Rⁿ, the standard vectors eᵢ might not lie in that subspace. But the subspace always has an orthonormal basis, and it can be constructed in a simple way out of any basis whatsoever. This construction, which converts a skewed set of axes into a perpendicular set, is known as ***Gram-Schmidt orthogonalization***.

To summarize, the three topics basic to this section are:

 1. The definition and properties of orthogonal matrices Q.
 2. The solution of Qx = b, either n x n or rectangular (least squares).
 3. The Gram-Schmidt process and its interpretation as a new factorization A = QR.

**3Q**  If Q (square or rectangular) has orthonormal columns, then QᵀQ = I:

```
Orthonormal columns:
    ⎡-- q₁ᵀ --⎤ ⎡|  |  | ⎤   ⎡1 0 · 0⎤  
    ⎢-- q₂ᵀ --⎥·⎢q₁ q₂ qn⎥ = ⎢0 1 · 0⎥ = I.    (1)
    ⎢         ⎥ ⎢|  |  | ⎥   ⎢· · · ·⎥
    ⎣-- qnᵀ --⎦ ⎣|  |  | ⎦   ⎣0 0 · 1⎦
```

- ***An orthogonal matrix is a square matrix with orthonormal columns.***  Then **Qᵀ is Q⁻¹** , ***the transpose is the inverse***.
     -  *Orthonormal matrix* would have been a better name, but it is too late to change. 
     - Also, there is no accepted word for a rectangular matrix with orthonormal columns. We still write Q, but we won't call it an "orthogonal matrix" unless it is square.
     - 只有Q是方阵的情况下，我们才称之为: 正交矩阵
     - orthonormal 是 QᵀQ = I, Qᵀ = Q⁻¹ 的前提之一 !
- Note that QᵀQ = I even if Q is rectangular. But then Qᵀ is only a left-inverse.

**3R** Multiplication by any Q preserves lengths:

```
Lengths unchanged: 
    ‖Qx‖ = ‖x‖  for ever vector x.  (2)
```

- eg. rotations and reflection matrix.

It also preserves innerproducts and angles, since (Qx)ᵀ(Qy) = `xᵀQᵀQy = xᵀy`.

The preservation of lengths comes directly from QᵀQ = I:

```
         ‖Qx‖² = ‖x‖²  
because  (Qx)ᵀ(Qx) = xᵀQᵀQx = xᵀx.  (3)
```

We come now to the calculation that uses the special property Qᵀ is Q⁻¹. If we have a basis, then any vector is a combination of the basis vectors. This is exceptionally simple for an orthonormal basis, which will be a key idea behind Fourier series. The problem is to *find the coefficients of the basis vectors*:

&nbsp;&nbsp; ***Write b as a combination b = x₁q₁ + x₂q₂ + ... + x<sub>n</sub>q<sub>n</sub>***

To compute x₁ there is a neat trick. *Multiply both sides of the equation by q₁ᵀ*.  We are left with q₁ᵀb = x₁q₁ᵀq₁. Since q₁ᵀq₁ = 1, we have found x₁ = q₁ᵀb. 

Each piece of b has a simple formula, and recombining the pieces gives back b:

&nbsp;&nbsp;&nbsp;&nbsp; ***Every vector b is equal to (q₁ᵀb)q₁ + (q₂ᵀb)q₂ + ... + (q<sub>n</sub>ᵀb)q<sub>n</sub> .  &nbsp;&nbsp;&nbsp;&nbsp;(4)***

I can't resist putting this orthonormal basis into a square matrix Q. The vector equation x₁q₁ + ... + x<sub>n</sub>q<sub>n</sub>= b is identical to Qx = b.  Its solution is x = Q⁻¹b. But since Q⁻¹ = Qᵀ -- this is where orthonormality enters -- the solution is also x = Qᵀb:

```
          ⎡-- q₁ᵀ --⎤⎡ ⎤   ⎡q₁ᵀb⎤
x = Qᵀb = ⎢         ⎥⎢b⎥ = ⎢    ⎥    (5)
          ⎣-- qnᵀ --⎦⎣ ⎦   ⎣qnᵀb⎦
```

***The components of x are the inner products*** **qᵢᵀb** , as in equation (4) . 

**Remark 1**: The ratio aᵀb/aᵀa appeared earlier, when we projected b onto a line. Here a is q₁, the denominator is 1, and the projection is (q₁ᵀb)q₁. Thus we have a new interpretation for formula (4): *Every vector b is the sum of its one-dimensional projections onto the lines through the q's*.

- b 等于 b 在各个基向量上投影的和。

**Remark 2**: ***The rows of a square matrix are orthonormal whenever the columns are***.

```
        ⎡1/√3   1/√2   1/√6⎤
    Q = ⎢1/√3    0    -2/√6⎥
        ⎣1/√3  -1/√2   1/√6⎦  
```


---

<h2 id="30de4e2d90eb5352ce69b4782264cd6b"></h2>


#### Rectangular Matrices with Orthonormal Columns

This chapter is about Ax = b, when A is not necessarily square.

For Qx = b we now admit the same possibility -- there may be more rows than columns. The n orthonormal vectors qᵢ in the columns of Q have m > n components. Then Q is an m x n matrix and we cannot expect to solve Qx = b exactly. *We solve it by least squares*.

If there is any justice, orthonormal columns should make the problem simple. It worked for square matrices, and now it will work for rectangular matrices. The key is to notice that we still have QᵀQ = I. So Qᵀ is still the ***left-inverse*** of Q.

For least squares that is all we need. Now the normal equations are QᵀQx̂ = Qᵀb. But QᵀQ is the identity matrix!  Therefore x̂ = Qᵀb, whether Q is square and x̂ is an exact solution, or Q is rectangular and we need least squares.

**3S** If Q has orthonormal columns, the least-squares problem becomes easy:

```
  Qx = b   , rectangular system with no solution for most b.
QᵀQx̂ = Qᵀb , normal equation for the best x̂ -- in which QᵀQ = I.
   x̂ = Qᵀb , x̂ᵢ = qᵢᵀb 
   p = Qx̂  , the projection of b is (q₁ᵀb)q₁ + ... + (qnᵀb)qn.
   p = QQᵀb, the projection matrix is P = QQᵀ ( here QQᵀ ≠ I )
```

PS. For rectangular matrics , QQᵀ ≠ I :

```octave
octave:11> Q = [1 0 ; 0 1 ; 0 0 ]
Q =

   1   0
   0   1
   0   0

octave:12> Q'*Q
ans =

   1   0
   0   1

octave:13> Q*Q'
ans =

   1   0   0
   0   1   0
   0   0   0
```

```
The projection matrix: 
    P = Q(QᵀQ)⁻¹Qᵀ ,  or P = QQᵀ     (7)
```

QQᵀ is the zero matrix on the othogonal complement ( the nullspace of Qᵀ ).  -- 不理解

**Example 3** The following case is simple but typical. Suppose we project a point b = (x,y,z) onto the x-y plane. It's projection is p = (x,y,0), and this is the sum of the separate projections on the x- and y-axes:

```
         ⎡1⎤                  ⎡x⎤
    q₁ = ⎢0⎥  and  (q₁ᵀb)q₁ = ⎢0⎥;
         ⎣0⎦                  ⎣0⎦  

         ⎡0⎤                  ⎡0⎤
    q₂ = ⎢1⎥  and  (q₂ᵀb)q₂ = ⎢y⎥.
         ⎣0⎦                  ⎣0⎦  
```

The overall projection matrix is :

```
                    ⎡1 0 0⎤         ⎡x⎤   ⎡x⎤
P = q₁q₁ᵀ + q₂q₂ᵀ = ⎢0 1 0⎥,  and  P⎢y⎥ = ⎢y⎥ 
                    ⎣0 0 0⎦         ⎣z⎦   ⎣0⎦  
```

***Projection onto a plane = sum of projections onto orthonormal q₁ and q₂***.

Orthogonal columns are so much better that it is worth changing to that case. And it leads to a factorization A = QR that is nearly as famous as A = LU.

---

<h2 id="e8bd1a0d73391e5faccdebb17e16f305"></h2>


#### The Gram-Schmidt Process

Now we propose to find a way to ***make*** them orthogonal.

The method is simple. We are given a,b,c and we want q₁,q₂,q₃. There is no problem with q₁: it can go in the direction of a. We divide by the length , so that q₁ = a/‖a‖ is a unit vector. The real problem begins with q₂ -- which has to be orthogonal to q₁. If the second vector b has any component in the direction of q₁ (or a) , ***that component has to be subtracted***:

```
Second Vector      
    B = b - (q₁ᵀb)q₁ , and q₂ = B/‖B‖.     (9)
```

B is orthogonal to q₁. It is the part of b that goes in a new direction , and not in the direction of a.

![](../imgs/LA_F3.10.png)

At this point q₁ and q₂ are set. The third orthogonal direction starts with c. It will not be in the plance of q₁ and q₂, which is the plane of a and b. However, it may have a component in that plane, and that has to be substracted. What is left is the component C we want, the part that is in a new direction perpendicular to the plane:

```
Third Vector     
C = c -(q₁ᵀc)q₁ -(q₂ᵀc)q₂ , and q₃ = C/‖C‖.  (10)
```

This is the one idea of the whole Gram-Schmidt process, ***to subtract from every new vector  its components in the directions that are already settled***. That idea is used over and over again. When there is a 4th vector, we subtract away its components in the direction of q₁,
q₂,q₃.


**Example 5 Gram-Schmidt** Suppose the independent vectors are a, b, c:

```
    ⎡1⎤      ⎡1⎤      ⎡2⎤         
a = ⎢0⎥, b = ⎢0⎥, c = ⎢1⎥.
    ⎣1⎦      ⎣0⎦      ⎣0⎦         

     ⎡1/√2⎤
q₁ = ⎢ 0  ⎥.
     ⎣1/√2⎦
```

```
    ⎡1⎤       ⎡1/√2⎤       ⎡ 1⎤
B = ⎢0⎥ - 1/√2⎢ 0  ⎥  = 1/2⎢ 0⎥.
    ⎣0⎦       ⎣1/√2⎦       ⎣-1⎦

     ⎡ 1/√2⎤
q₂ = ⎢  0  ⎥.
     ⎣-1/√2⎦
```

```
    ⎡2⎤     ⎡1/√2⎤     ⎡ 1/√2⎤    ⎡0⎤
C = ⎢1⎥ - √2⎢ 0  ⎥ - √2⎢  0  ⎥  = ⎢1⎥.
    ⎣0⎦     ⎣1/√2⎦     ⎣-1/√2⎦    ⎣0⎦   
```


**3T** The Gram-Schmidt process starts with independent vectors a₁, ... , a<sub>n</sub>    and end with orthogonal vectors q₁, ... , q<sub>n</sub>. At step j it substracts from aⱼ its components in the directions q₁, ... , qⱼ₋₁ that are already settled:

```
Aⱼ = aⱼ -(q₁ᵀaⱼ)q₁ - ... -(qⱼ₋₁ᵀaⱼ)qⱼ₋₁.  (11)
```

*Remark on the calculations*  I think it is easier to compute the orthogonal a, B, C, without forcing their lengths to equal one. Then square roots enter only at the end, when dividing by those lengths. The example above would have the same B and C, without using square roots.

*Notice the 1/2 from aᵀb/aᵀa instead of 1/√2 from qᵀb*.

```
    ⎡1⎤      ⎡1⎤    ⎡ 1/2⎤
B = ⎢0⎥ - 1/2⎢0⎥  = ⎢  0 ⎥,
    ⎣0⎦      ⎣1⎦    ⎣-1/2⎦

    ⎡2⎤   ⎡1⎤    ⎡ 1/2⎤    ⎡0⎤
C = ⎢1⎥ - ⎢0⎥ - 2⎢  0 ⎥  = ⎢1⎥.
    ⎣0⎦   ⎣1⎦    ⎣-1/2⎦    ⎣0⎦   
```



---

<h2 id="9abeff81b513ce7e5c2268c074e45858"></h2>


#### The Factorization A = QR

We started with a matrix A, whose columns were a, b, c. We ended with a matrix Q, whose columns are q₁,q₂,q₃. What is the relation between those matrices? The matrices A and Q are m x n when the n vectors are in m-dimensional space, and there has to be a third matrix that connects them.

The idea is to write the a's as combinations of the q's. The vector b in Figure 3.10 is a combination of the orthonormal q₁ and q₂, and we know what combination it is:

```
    b = (q₁ᵀb)q₁ + (q₂ᵀb)q₂.
```

Every vector in the plane is the sum of its q₁ and q₂ components. Similarly c is the sum of its q₁,q₂,q₃ components: 

`c = (q₁ᵀc)q₁ + (q₂ᵀc)q₂ + (q₃ᵀc)q₃`. 

If we express that in matrix form we have ***the new factorization A = QR***:

```
QR factors :

    ⎡     ⎤   ⎡        ⎤⎡q₁ᵀa q₁ᵀb q₁ᵀc⎤
A = ⎢a b c⎥ = ⎢q₁ q₂ q₃⎥⎢     q₂ᵀb q₂ᵀc⎥ = QR.    (12)
    ⎣     ⎦   ⎣        ⎦⎣          q₃ᵀc⎦
```

R is upper triangular because of the way Gram-Schmidt was done. The first vectors a and q₁ fell on the same line. Then q₁, q₂ were in the same plane as a, b. The third vectors c and q₃ were not involved until step 3.

The QR factorization is like A = LU, except that the first factor Q has orthonormal columns. The second factor is called R, because the nonzeros are to the *right* of the diagonal (and the letter U is already taken). 

```
    ⎡1 1 2⎤   ⎡1/√2  1/√2  0 ⎤⎡√2  1/√2  √2⎤
A = ⎢0 0 1⎥ = ⎢  0    0    1 ⎥⎢    1/√2  √2⎥ = QR.
    ⎣1 0 0⎦   ⎣1/√2 -1/√2  0 ⎦⎣          1 ⎦
```

*You see the lengths of a, B, C on the diagonal of R*. The orthonormal vectors q₁,q₂,q₃, which are the whole object of orthogonalization, are in the first factor Q. 

The entries rᵢⱼ = qᵢᵀaⱼ.

PS. if j>i , aⱼ is always perpendent to the previous settled qᵢ. 这点确保了 R is upper triangular.

**3U** Every m x n matrix with independent columns canbe factored into A = QR. The columns of Q are orthonormal, and R is upper triangular and invertible. When m = n and all matrices are square, Q becomes an orthogonal matrix.

I must not forget the main point of orthogonalization. It simplifies the least-squares problem Ax = b. The normal equations are still correct, but AᵀA becomes easier:

```
AᵀA = RᵀQᵀQR = RᵀR.     (14)
```

The fundamental equation AᵀAx̂ = Aᵀb simplifies to a triangular system:

```
RᵀRx̂ = RᵀQᵀb ,   or  Rx̂ = Qᵀb.     (15)
```
Instead of solving QRx = b, which can't be done, we solve Rx̂ = Qᵀb, which is just back-substitution because R is triangular. The real cost is the mn² operations of Gram-Schmidt, which are needed to find Q and R in the first place.

The same idea of orthogonality applies to functions. The sines and cosines are orthogonal; the powers 1, x, x² are not. When f(x) is written as a combination of sines and cosines, that is a ***Fourier series***. Each term is a projection onto a line -- the line in function space containing multiples of cosnx or sinnx. It is completely parallel to the vector case, and very important. And finally we have a job for Schmidt: To orthogonalize the powers of x and produce the Legendre polynomials.

---

<h2 id="f7b94cc4db71bd4599e6e5dd3d560808"></h2>


#### Function Spaces and Fourier Series

This is a brief and optional section, but it has a number of good intentions:

 1. to introduce the most famous infinite-dimensional vector space (Hilbert space);
 2. to extend the ideas of length and inner product from vectors v to functions f(x);
 3. to recoginze the Fourier series as a sum of one-dimensional projections ( the orthogonal "columns" are the sines and cosines);
 4. to apply Gram-Schmidt orthogonalization to the polynomials 1, x, x², ... ; and
 5. to find the best approximation to f(x) by a straight line.

We will try to follow this outline, which opens up a range of new-applications for linear algebra, in a systematic way.

 1. Hilbert space
     - After studying Rⁿ, it is natural to think of the space R<sup>∞</sup>. The infinite series must converge to a finite sum. This leaves (1, 1/2, 1/3, ...) but not (1, 1, 1, ...).  
     - Hilbert space is the natural way to let the number of dimensions become infinite, and at the same time to keep the geometry of ordinary Euclidean space. Ellipses "..." become infinite-dimensional ellipsoids, and perpendicular lines are recognized exactly as before. The vectors v and w are orthogonal when their inner product is zero: 
     - `vᵀw = v₁w₁ + v₂w₂ + v₃w₃ + ... = 0`.
     - This snm is guaranteed to converge, and for any two vectors it still obeys the Schwarz inequality `‖vᵀw‖ < ‖v‖‖w‖` . The cosine, even in Hilbert space, is never larger than 1.
     - There is another remarkable thing about this space: It is found under a great many different disguises. Its "vectors" can turn into functions, which is the second point.

 2. Lengths and Inner Products.
     - Suppose f(x) = sin x on the interval 0 < x < 2π.




TODO


---





















