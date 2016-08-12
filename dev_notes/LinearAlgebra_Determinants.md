...menustart

 - [Determinants](#44858f4401928ded6e165da37ea948a5)

...menuend



<h2 id="44858f4401928ded6e165da37ea948a5"></h2>
# Determinants

## 4.1 INTRODUCTION

One viewpoint is this: The determinant provides an explicit "formula" for each entry of A⁻¹ and A⁻¹b. 

We can list four of the main uses of determinants:

 1. They test for invertibility. 
 	- ***If the determinant of A is zero, then A is singular***. 
 	- ***If det A ≠ 0, then A is invertible*** (and A⁻¹ involves 1/detA).
 	- 
 	- The most important application, and the reason this chapter is essential to the book, is to the family of matrices A - λI. The parameter λ is subtracted all along the main diagonal, and the problem is to find the eigenvalues for which A - λI is singular. The test is det(A - λI) = 0. This polynomial of degree n in X has exactly n roots. The matrix has n eigenvalues. This is a fact that follows from the determinant formula, and not from a computer.
 2. The determinant of A equals the ***volume*** of a box in n-dimensional space. 
 	- The edges of the box come from the rows of A . The columns of A would give an entirely different box with the same volume.
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F4.1.png)
 3. The determinant gives a formula for each pivot. 
 	- Theoretically, we could predict when a pivot entry will be zero, requiring a row exchange. 
 	- From the formula ***determinant = ± (product of the pivots)***, it follows that *regardless of the order of elimination, the product of the pivots remains the same apart from sign*.
 4. The determinant measures the dependence of A⁻¹b on each element of b. 
 	- If one parameter is changed in an experiment, or one observation is corrected, the "influence coefficient" in A⁻¹ is a ratio of determinants.

There is one more problem about the determinant. It is difficult not only to decide on its importance, and its proper place in the theory of linear algebra, but also to choose the best definition. Obviously, detA will not be some extremely simple function of n² variables; otherwise A⁻¹ would be much easier to find than it actually is.

***The simple things about the determinant are not the explicit formulas, but the properties it possesses***. This suggests the natural place to begin. The determinant can be (and will be) defined by its three most basic properties: 
 - det I = 1, 
 - **the sign is reversed by a row exchange**, 
 - the determinant is linear in each row separately. 

The problem is then to show how the determinant can be computed , by systematically using these properties .  This will bring us back to the product of the pivots.

Here is a light-hearted question about permutations. ***How many exchanges does it take to change VISA into AVIS***? Is this permutation odd or even?

---

## 4.2 PROPERTIES OF THE DETERMINANT

This will be a pretty long list. Fortunately each rule is easy to understand, and even easier to illustrate, for a 2 by 2 example. Therefore we shall verify that the familiar definition in the 2 by 2 case,

```
det ⎡a b⎤ = |a b| = bc - ad 
	⎣c d⎦  	|c d|
```

Notice the two accepted notations for the determinant, det A and |A|.

Properties 4-10 will be deduced from the previous ones. **Every property is a consequence of the first three**. 

We emphasize that the rules apply to *square matrices* of any size.

 1. **det I = 1**
 	- The determinant of the identity matrix is 1.
 2. *The determinant changes sign when two rows are exchanged*.
 3. *The determinant depends linearly on one row*. 
 	1. Add vectors in row
 		- 
 		```
 		|a+a' b+b'| =|a b| + |a' b'|
      	|c    d   |  |c d|   |c  d |
 		```
 		- det2A = 2ⁿ detA
 	2. Multiply by *t* in row
 		- 
 		```
		|ka kb| = k |a b|
    	| c  d|     |c d|
    	```
 4. *If two rows of A are equal, then det A = 0.*
 	- deduce from rule 2 ,  r = -r => r = 0 
 5. *Subtracting k*row i from row j , leaves the same determinant.*
 	- deduce from 3.1,3.2
 	- 几何意义: 向量ab,cd, 向量ab不变，平行四边型的底不变; 向量cd 沿着 ab 方向发生切变，平行四边型的高不变，所以ab,cd 构成的面积不变。
 6. *If A has a row of zeros, then det A = 0*.
 	- deduce from 3
 	- 
 	```
    5|0 0| =|0 0| ,  5x =x -> x=0 
     |c d|  |c d|
    ```
 7. *If A is triangular, then det A is the product of the diagonal entries*. 
 	- If the triangular A has 1s along the diagonal, then det A = 1.
 	- 
 	```
     |a b|= ad, |a 0|= ad 
     |0 d|      |c d|
    ```
    - ***Proof:*** Suppose the diagonal entries are nonzero. Then elimination can remove all the off-diagonal entries (and keep the same pivot, 那些off-diagonal entries都是打酱油的), without changing the determinant (by rule 5)
    - *If a diagonal entry is 0 then elimination will produce a 0 row.* This is a key property: **All singular matrices have a zero determinant**.
 8. *If A is singular, then det A = 0. If A is invertible, then det A ≠ 0.*
 	- If A is singular, elimination leads to a zero row in U. Then det A = det U = 0. 
 	- If A is nonsingular, elimination puts the pivots d₁, ..., d𝑛, on the main diagonal. We have a "product of pivots" formula for det A! The sign depends on whether the number of row exchanges is even or odd:
 		- 









