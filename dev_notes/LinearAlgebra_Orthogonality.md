
# Orthogonality

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

***zero vector is orthogonal to any vector***.

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
 	- because 2 orthogonal plane has deminsion 4 in total , they must intersect in a line in R³ 
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

```
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
 - Each x in the nullspace is orthogonal to each vector in the row space, so ***N(A) ⟂ C(Aᵀ)***.


The other pair of orthogonal subspaces comes from Aᵀy = 0, or yᵀA = 0:

```
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
 	- ***N(Aᵀ) ⟂ C(A)***



***Second proof***  If x is in the nullspace then Ax = 0. If v is in the row space, it is a combination of the rows: v = Aᵀz for some vector z. Now, in one line:

```
Nullspace ⟂ Row space :   vᵀx = (Aᵀz)ᵀx = zᵀAx = zᵀ0 = 0.    (8)
```


**DEFINITION** Given a subspace V of Rⁿ, the space of all vectors orthogonal to V is called the **orthogonal complement** of V. It is denoted by **V⟂ = "V perp."**  (⟂ 在右上角)

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





