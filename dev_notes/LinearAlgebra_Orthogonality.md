...menustart

 - [Orthogonality](#878bcbccb5d63db01d2193f2e15cae28)
	 - [3.1 ORTHOGONAL VECTORS AND SUBSPACES](#70835fd4404a5ddec835801ba42ecfb0)
	 - [3.2 COSINES PROJECTIONS ONTO LINES](#870df6062f5bb62d6f82187a8efebbe1)
	 - [3.3 PROJECTIONS LEAST SQUARES](#4a2df06c2d276ad56402eecaa894e5d5)

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


**Orthogonal Vectors**

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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_inner_product_xTy.png)

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



**Orthogonal Subspaces**

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

In this case, with subspaces of dimension 2 and *l* in R4, there is room for a third subspace. The line L through z = (0, 0, 5, -4) is perpendicular to V and W. Then the dimensions add to 2 + 1 + 1 = 4. What space is perpendicular to all of V, W, and L ?


The important orthogonal subspaces don't come by accident, and they come two at a time. In fact orthogonal subspaces are unavoidable: ***They are the fundamental subspaces***! The first pair is the *nullspace and row space*. Those are subspaces of **Rⁿ** - the rows have n components and so does the vector x in Ax = 0. We have to show, using Ax = 0, that ***the rows of A are orthogonal to the nullspace vector x***.


**3C Fundamental theorem of orthogonality**:  

 - The row space is orthogonal to the nullspace (in Rⁿ) , Ax = 0 
 - The column space is orthogonal to the left nullspace (in Rᵐ)

***First proof***  Suppose x is a vector in the nullspace. Then Ax = 0 , and this system of *m* equations can be written out as rows of A multiplying x:

```octave
	 | ... row 1 ... | |x₁|   |0|
	 | ... row 2 ... |·|x₂| = |0|
Ax = | 				 | |  |	  | |
	 | 				 | |  |	  | |
	 | ... row m ... | |  |	  |0|
	 				   |xn|
```

 - The main point is already in the first equation: row 1 is orthogonal to x. 
 	- Their inner product is zero; 
 - Every right-hand side is zero, so x is orthogonal to every row. 
 	- Therefore x is orthogonal to every combination of the rows. 
 - Each x in the nullspace is orthogonal to each vector in the row space, so ***N(A) ⊥ C(Aᵀ)*** .


The other pair of orthogonal subspaces comes from Aᵀy = 0, or yᵀA = 0:

```octave
	  |c 	   c|
	  |o 	   o|
	  |l 	   l|
yᵀA = |u  ...  u| = [0 ... 0]
	  |m 	   m|
	  |n 	   n|
	  |		    |
	  |1 	   n|
```

 - The equation says , from the zeros on the right-hand side , the vector y is orthogonal to every column.
 	- Therefore y is orthogonal to every combination of the columns.
 - y is orthogonal to the column space, and it is a typical vector in the left nullspace:
 	- ***N(Aᵀ) ⊥ C(A)***



***Second proof***  If x is in the nullspace then Ax = 0. If v is in the row space, it is a combination of the rows: v = Aᵀz for some vector z. Now, in one line:

```octave
	Nullspace ⊥ Row space :   vᵀx = (Aᵀz)ᵀx = zᵀAx = zᵀ0 = 0.    (8)
```


**DEFINITION** Given a subspace V of Rⁿ, the space of all vectors orthogonal to V is called the **orthogonal complement** of V. It is denoted by **V⊥ = "V perp."**  (⊥ 在右上角)

 - the nullspace is the orthogonal complement of the row space
 	- A vector z can't be orthogonal to the nullspace but outside the row space
 - **Dimension formula**:  dim(row space) + dim(nullspace) = number of columns.
 	- r + ( n -r ) = n 
 
**3D Fundamental Theorem of Linear Algebra, Part II**

 - The nullspace is the *orthogonal complement* of the row space in Rⁿ.
 - The left nullspace is the *orthogonal complement* of the column space in Rᵐ.

**3E** Ax = b is solvable if and only if  yᵀb = 0  whenever yᵀA  = 0.

 - Ax = b requires b to be in the column space. 
 - Ax = b **requires b to be perpendicular to the left nullspace**.


---

**The Matrix and the Subspaces**

 - Splitting Rⁿ into orthogonal parts V and W , will split every vector into x = v + w. 
 - The vector v is the projection onto the subspace V. 
 - The orthogonal component w is the projection of x onto W. 

Figure 3.4 summarizes the fundamental theorem of linear algebra.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Figure_3.4.png)

 - The nullspace is carried to the zero vector. 
 - Every Ax is in the column space. 
 - Nothing is carried to the left nullspace. 
 - The real action is between the row space and column space, and you see it by looking at a typical vector ***x*** :
 	- It has a "row space component" and a "nullspace component," with `x = xᵣ+ xn`,  When multiplied by A, this is `Ax = Axᵣ + Axn`:
 	- The nullspace component goes to zero: Axn = 0.
 	- The row space component goes to the column space: `Axᵣ = Ax`.

Of course everything goes to the column space - the matrix cannot do anything else. I tried to make the row and column spaces the same size, with equal dimension r.

**3F** From the row space to the column space. A is actually invertible. Every vector b in the column space comes from exactly one vector xᵣ , in the row space.

***Proof*** Every b in the column space is a combination Ax of the columns. In fact, b is Axᵣ with xᵣ in the row space, since the nullspace component gives Ax = 0. If another vector x, in the row space gives Ax'ᵣ = b, then A(xᵣ - x'ᵣ) = b - b = 0. This puts xᵣ - x'ᵣ in the nullspace and the row space, which makes it orthogonal to itself. Therefore it is zero, and xᵣ = x'ᵣ . Exactly one vector in the row space is carried to b.

> ***Every matrix transforms its row space onto its column space.***

On those r-dimensional spaces A is invertible (if x in row space ). On its nullspace A is zero. When A is diagonal, you see the invertible submatrix holding the r nonzeros.


Aᵀ goes in the opposite direction, from Rᵐ to Rⁿ and from C(A) back to C(Aᵀ). Of course the transpose is not the inverse! Aᵀ moves the spaces correctly, but not the individual vectors. That honor belongs to A⁻¹ if it exists - and it only exists if r = m = n. We cannot ask A⁻¹ to bring back a whole nullspace out of the zero vector.

When A⁻¹ fails to exist, the best substitute is the ***pseudoinverse*** A⁺. This inverts A where that is possible: A⁺Ax = x for x in the row space. On the left nullspace, nothing can be done: A⁺y = 0. Thus A⁺ inverts A where it is invertible, and has the same rank r. One formula for A⁺ depends on the ***singular value decomposition*** - for which we first need to know about eigenvalues.



<h2 id="870df6062f5bb62d6f82187a8efebbe1"></h2>
## 3.2 COSINES PROJECTIONS ONTO LINES


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_projection_onto_line.png)

**Figure 3.5** The projection p is the point ( on the line through a ) closest to b.

The situation is the same when we are given a plane (or any subspace S) instead of a line. Again the problem is to find the point p on that subspace that is closest to b. ***This point p is the projection of b onto the subspace***. Geometrically, that gives the distance between points b and subspaces S. But there are two questions that need to be asked:

 1. Does this projection actually arise in practical applications?
 2. If we have a basis for the subspace S, is there a formula for the projection p ?

The answers are certainly yes. This is exactly the problem of the ***least-squares*** solution to an overdetermined system. The vector b represents the data from experiments or questionnaires, and it contains too many errors to be found in the subspace S. The equations are inconsistent, and Ax = b has no solution.

The least-squares method selects p as the best choice to replace b. 

A formula for p is easy when the subspace is a line.   Projection onto a higher dimensional subspace is by far the most important case; it corresponds to a least-squares problem with several parameters. The formulas are even simpler when we produce an orthogonal basis for S.


**Inner Products and Cosines**

Relationship of inner products and angles.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_innerProduct_and_angle.png)

Figure 3.6 The cosine of the angle θ = β - α using inner products.

 - The length ‖a‖ is the hypotenuse 斜边 in the triangle OαQ. 
 	- So the sine and cosine of a are : `sinα = a₂/‖a‖ , cosα = a₁/‖a‖` 
 	- For the angle β , `sinα = b₂/‖b‖ , cosα = b₁/‖b‖` 
 	- **cosθ = cos(β - α) = cosβcosα + sinβsinα = ( a₁b₁ + a₂b₂ ) / ‖a‖·‖b‖**  ,  (1)

The numerator in formula (1) is exactly the inner product of a and b. It gives the relationship between aᵀb and cos θ:

**3G** The cosine of the angle between any *nonzero vectors* a and b is :  

```octave
	cosθ = aᵀb / ‖a‖·‖b‖  (2)
```



**Projection onto a Line**

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_projection_onto_line2.png)

 - Now we want to find the projection point p. 
 - This point must be some multiple p = x̂a of the given vector a 
 	- every point on the line is a multiple of a. 
 - The problem is to compute the coefficient `x̂`. 
 - All we need is the geometrical fact that ***the line from b to the closest point p = x̂a is perpendicular to the vector a***:

```octave
	(b - x̂a) ⊥ a ,  or  aᵀ(b - x̂a) = 0 ,  or  x̂ = (aᵀb / aᵀa)   (4)
```

That gives the formula for the number x̂ and the projection p:

**3H** The projection of the vector b onto the line in the direction of a is p = x̂a:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_projection_onto_a_line.png)

This leads to the **Schwarz inequality** in equation (6), which is the most important inequality in mathematics.  A special case is the fact that arithmetic means ½(x + y) ≥ geometric mean  √xy . 

```octave
	Schwarz inequality:  |aᵀb| ≤ ‖a‖·‖b‖    (6)
```

All vectors a and b satisfy the ***Schwarz inequality***, which is |cosθ| ≤ 1 in Rⁿ.

One final observation about `|aᵀb| ≤ ‖a‖·‖b‖` . Equality holds *if and only if* b is a multiple of a. The angle is θ = 0° or θ = 180° and the cosine is 1 or -1. In this case b is identical with its projection p, and the distance between b and the line is zero.


**Projection Matrix of Rank 1**

The projection of *b* onto the line through *a* lies at p = a(aᵀb/aᵀa). That is our formula p = x̂a, but the vector *a* is put before the number x̂ = aᵀb/aᵀa. Projection onto a line is carried out by a ***projection matrix P***, and written in this new order we can see what it is. 

P is the matrix that multiplies b and produces p:

```octave
	p = Pb ,  P = aaᵀ/aᵀa    (7)
```

That is a column times a row -a square matrix- divided by the number aᵀa .  (aaᵀ 是一个秩1矩阵)

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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_3.2_example3.png)

Here c is cosθ, s is sinθ, and c2 + s2 = 1 in the denominator. This matrix P was discovered in Section 2.6 on linear transformations. Now we know P in any number of dimensions. We emphasize that it produces the projection p:


***To project b onto a, multiply by the projection matrix P:  p = Pb***

---

**Transposes from Inner Products**

Finally we connect inner products to Aᵀ. Up to now, Aᵀ is simply the reflection of A across its main diagonal; the rows of A become the columns of Aᵀ, and vice versa. The entry in row i, column j of Aᵀ is the (j, i) entry of A:

 **Transpose by reflection**: (Aᵀ)ᵢⱼ = (A)ⱼᵢ

There is a deeper significance to Aᵀ. Its close connection to inner products gives a new and much more "abstract" definition of the transpose:

**3J** The transpose Aᵀ can be defined by the following property:  

 - The inner product of Ax with y equals the inner product Of x with Aᵀy. Formally, this simply means:

```octave
	(Ax)ᵀy = xᵀAᵀy = xᵀ(Aᵀy)     (8)
```

This definition gives us another (better) way to verify the formula (AB)ᵀ = BᵀAᵀ. Use equation (8) twice:

```octave
	Move A then move B:  (ABx)ᵀy = (Bx)ᵀ(Aᵀy) = xᵀ(BᵀAᵀy)
```

The transposes turn up in reverse order on the right side, just as the inverses do in the formula (AB)⁻¹ = B⁻¹ A⁻¹. We mention again that these two formulas meet to give the remarkable combination (A⁻¹)ᵀ = (Aᵀ)⁻¹ .


<h2 id="4a2df06c2d276ad56402eecaa894e5d5"></h2>
## 3.3 PROJECTIONS LEAST SQUARES

Up to this point, Ax = b either has a solution or not. If b is not in the column space C(A), the system is inconsistent and Gaussian elimination fails. This failure is almost certain when there are several equations and only one unknown:

```octave
	More equations 	2x = b₁
	than unknowns-	3x = b₂
	no solution?	4x = b₃
```

This is solvable when b1, b2, b3 are in the ratio 2:3:4. The solution x will exist only if b is on the same line as the column a = (2, 3, 4).

In spite of their unsolvability, inconsistent equations arise all the time in practice. They have to be solved!  Rather than expecting no error in some equations and large errors in the others, it is much better to *choose the x that minimizes an average error E in the m equations*.

The most convenient "average" comes from the *sum of squares*:

```octave
	Squared error  E² = (2x - b₁)² + (3x - b₂)² + (4x - b₃)² .
```

 - If there is an exact solution, the minimum error is E = 0. 
 - In the more likely case that b is not proportional to a, the graph of E² will be a parabola ( para 'beside' + bolē 'a throw' -> 抛物线). The minimum error is at the lowest point, where the derivative is zero:

```octave
	dE²/dx = 2[(2x - b₁)2 + (3x - b₂)3 + (4x - b₃)4] = 0. 
```

Solving for x, the least-squares solution of this model system ax = b is denoted by x̂ :  (you need some calculus)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_least_square_solution_example.png)  

**3K**:  The least-squares solution to a problem ax = b  in one unknon is x̂ = aaᵀ/aᵀa .

**Least-Squares Problems with Several Variables**

Now we are ready for the serious step, to ***project b onto a subspace*** . This problem arises from Ax = b when A is an m by n matrix.   The number m of observations is still larger than the number n of unknowns, so it must be expected that Ax = b will be inconsistent. *Probably, there will not exist a choice of x that perfectly fits the data b*. In other words, the vector b probably will not be a combination of the columns of A; it will be outside the column space.

Again the problem is to choose x̂ so as to minimize the error, and again this minimization will be done in the least-squares sense. The error is E = ‖Ax - b‖, and ***this is exactly the distance from b to the point Ax in the column space***. Searching for the least-squares solution x̂ , which minimizes E, is the same as locating the point p = Ax̂ that is closer to b than any other point in the column space.

We may use geometry or calculus to determine x̂ . In n dimensions, we prefer the appeal of geometry; p must be the "projection of b onto the column space." The error vector e = b - Ax̂ must be perpendicular to that space (Figure 3.8). Finding x̂ and the projection p = Ax̂ is so fundamental that we do it in two ways:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F3.8.png)

 1. All vectors perpendicular to the column space lie in the left nullspace. Thus the error vector e = b - Ax̂ must be in the nullspace of Aᵀ:
 	- `Aᵀ(b-Ax̂) = 0  , or AᵀAx̂ = Aᵀb`
 	- 在坏方程左右乘上 Aᵀ ,就是好方程。 AᵀA 是本章的核心
 2. The error vector must be perpendicular to each column a₁ , ... , an of A:
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_errorVector_perpend_t_column.png)
 	- This is agin `Aᵀ(b-Ax̂) = 0  , or AᵀAx̂ = Aᵀb`.

The fastest way is just to multiply the unsolvable equation Ax = b by Aᵀ. All these equivalent methods produce a square coefficient matrix AᵀA. It is symmetric (its transpose is not AAᵀ!) and it is the fundamental matrix of this chapter.

The equations AᵀAx̂ = Aᵀb are known in statistics as the **normal equations**.


**3L**:  

 - When Ax b is inconsistent, its least-squares solution minimizes ‖Ax - b‖²  
 	- **normal equations** :  `AᵀAx̂ = Aᵀb`     (1)
 - AᵀA is invertible exactly when the columns of A are linearly independent! Then,
 	- **Best estimate x̂**:  `x̂ = (AᵀA)⁻¹Aᵀb`		(2)
 - The projection of b onto the column space is the nearest point Ax̂:
 	- **Projection**:  `p = Ax̂ = A·(AᵀA)⁻¹Aᵀb` 	(3)
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


**The Cross-Product Matrix of AᵀA**

The matrix AᵀA is certainly symmetric. Its transpose is (AᵀA)ᵀ = AᵀAᵀᵀ, which is AᵀA again. Its i, j entry (and j, i entry) is the inner product of column i of A with column j of A. The key question is the invertibility of AᵀA, and fortunately：

>**AᵀA has the same nullspace as A.**

Certainly if Ax = 0 then AᵀAx = 0. Vectors x in the nullspace of A are also in the nullspace of AᵀA. 

To go in the other direction, start by supposing that AᵀAx = 0, and take the inner product with x to show that Ax = 0:

```octave
	xᵀAᵀAx = 0,  or ‖Ax‖² = 0 ,  or Ax = 0.
```

The two nullspaces are identical. In particular, if A has independent columns (and only x = 0 is in its nullspace), then the same is true for AᵀA:

**3M** If A has independent columns, then AᵀA is square, symmetric, and invertible.

We show later that AᵀA is also positive definite (all pivots and eigenvalues are positive). This case is by far the most common and most important. Independence is not so hard in m-dimensional space if m > n. We assume it in what follows.

---

**Projection Matrices**

We have shown that the closest point to b is p = A(AᵀA)⁻¹Aᵀb. This formula expresses in matrix terms the construction of a perpendicular line from b to the column space of A. The matrix that gives p is a projection matrix, denoted by P:

```octave
	Projection Matrix:  P = A(AᵀA)⁻¹Aᵀ      (4)
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

```octave
	Pᵀ = (Aᵀ)ᵀ((AᵀA)⁻¹)ᵀAᵀ = A((AᵀA)ᵀ)⁻¹Aᵀ = A(AᵀA)⁻¹Aᵀ = P.
```

For the converse, we have to deduce from P² = P and Pᵀ = P that Pb ***is the projection of b onto the column space of P***. The error vector b - Pb is orthogonal to the space. For any vector Pc in the space, the inner product is zero:

```octave
	(b-Pb)ᵀPc = bᵀ(I-P)ᵀPc=bᵀ(P-P²)c = 0.  # PS: (I-P)ᵀ = (I-P)
```

Thus b - Pb is orthogonal to the space, and Pb is the projection onto the column space.

Suppose A is actually invertible. If it is 4 x 4, then its four columns are independent and its column space is all of R⁴. What is the projection onto the whole space? It is the identity matrix.

```octave
	P = A(AᵀA)⁻¹Aᵀ = AA⁻¹(Aᵀ)⁻¹Aᵀ = I.		(5)
```

The identity matrix is symmetric, I² = I, and the error b - Ib is zero.

To repeat: We cannot invert the separate parts Aᵀ and A when those matrices are rectangular. It is the square matrix AᵀA that is invertible , not Aᵀ and A.

---

**Least-Squares Fitting of Data**

Suppose we do a series of experiments, and expect the output b to be a linear function of the input t. We look for a ***straight line*** b = C + Dt. 

```octave
	C + Dt₁ = b₁
	C + Dt₂ = b₂
		...
	C + Dtm = bm
```

This is an *overdetermined* system, with m equations and only two unknowns. If errors are present, it will have no solution. A has two columns, and x = (C, D) : 

```octave
	|1 t₁|		  |b₁|
	|1 t₂|		  |b₂|
	| .  | |C|  = |. |   , or Ax = b.   (7)
	| .  | |D|	  |. |
	| .  |		  |. |
	|1 tm|		  |bm|
```

The best solution (Ĉ, D̂) is the x̂ that minimizes the squared error E²:





