
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

 - Subspaces of R³ can have dimension 0, 1, 2, or 3. 
 - The subspaces are represented by lines or planes through the origin
 	- and in the extreme cases, by the origin alone or the whole space. 
 - The subspace {0} is orthogonal to all subspaces. 
 - A line can be orthogonal to another line, or it can be orthogonal to a plane
 - **but a plane cannot be orthogonal to a plane**.
 	- I have to admit that the front wall and side wall of a room look like perpendicular planes in R³. But by our definition, that is not so!

**3B**: 

 - Two subspaces V and W of the same space Rⁿ are *orthogonal* if every vector v in V is orthogonal to every vector w in W: 
 	- vᵀw = 0 for all v and w.











