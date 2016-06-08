...menustart

 * [Vector Spaces](#2f21953656c07a77cad97b71c89a69de)
	 * [2.1 VECTOR SPACES AND SUBSPACES](#972dab9e05beb3d5443db66ec0eabd2e)
		 * [The Column Space of A](#8181c20bb270d985c5745507fd8a273b)
		 * [The Nullspace of A](#3c94b747c25e8b676e5f7af1a67da8a5)
	 * [2.2 SOLVING Ax=0 and Ax=b](#1e0304a592cf2dccbcb3c7e858021d8d)
		 * [Echelon Form(梯形) *U* and Row Reduced Form *R*](#fb0727e770a06722aa7b9d64a9b6af91)
		 * [Pivot Variables and Free Variables](#1e32c695f24ac4d5108ba9cca53ac86a)
		 * [Solving Ax = b, Ux = c, and Rx = d](#0aa8bb162b1e64c4edd71e634be16382)

...menuend




<h2 id="2f21953656c07a77cad97b71c89a69de"></h2>
# Vector Spaces

<h2 id="972dab9e05beb3d5443db66ec0eabd2e"></h2>
## 2.1 VECTOR SPACES AND SUBSPACES

For the concept of a ***vector space***, we start immediately with the most important spaces. They are denoted by **R¹, R², R³**, ... ; the space **Rⁿ** consists of all column vectors with ***n*** components.

 - **We can add any two vectors, and we can multiply all vectors by scalars. In other words, we can take linear combinations.** 

Normally our vectors belong to one of the spaces **Rⁿ**; they are ordinary column vectors. The formal definition allows other things to be ***"vectors"*** - provided that addition and scalar multiplication are all right. We give three examples:

 1. *The infinite-dimensional space* **R°°**.
    - Its vectors have infinitely many components, as in x = (1, 2, 1, 2, ...). The laws for x + y and cx stay unchanged. 
 2. *The space of 3 by 2 matrices*. 
    - In this case the "vectors" are matrices! This space is almost the same as **R⁶**. Any choice of *m* and *n* would give the vector space of all m by n matrices.
 3. *The space of functions f (x)*.
    - Here we admit all functions f that are defined on a fixed interval, say 0 < x < 1. The space includes *f(x) = x², g(x) = sinx*, their sum *(f + g)(x) = x² + sinx*, and all multiples like *3x²* and *-sinx*. The vectors are functions, and the dimension is somehow a larger infinity than for **R°°**. 

---

**Definition: Subspace**

A ***subspace*** of a vector space is a nonempty subset that satisfies the requirements for a vector space: Linear combinations stay in the subspace.

 - (i) If we add any vectors x and y in the subspace, x + y is in the subspace.
 - (ii) If we multiply any vector x in the subspace by any scalar c, cx is in the subspace.

---

Notice in particular that ***the zero vector will belong to every subspace***. That comes from rule (ii): Choose the scalar to be c = 0. The smallest subspace **Z** contains only one vector, the zero vector.

 - Example:

Start from the vector space of 3 by 3 matrices. One possible subspace is the set of lower triangular matrices. Another is the set of symmetric matrices. A + B and cA are lower triangular if A and B are lower triangular, and they are symmetric if A and B are
symmetric. Of course, the zero matrix is in both subspaces.

<h2 id="8181c20bb270d985c5745507fd8a273b"></h2>
### The Column Space of A

We now come to the key examples, the **column space** and the **nullspace** of a matrix A.

***The column space contains all linear combinations of the columns of A***. It is a subspace of **Rⁿ**. We illustrate by a system of m = 3 equations in n = 2 unknowns:

```
|1  0| |u|   |b₁|
|5  4|·|v| = |b₂|
|2  4|       |b₃|
```

With m > n we have more equations than unknowns - and usually there will be no solution. The system will be solvable only for a very "thin" subset of all possible b's ( b in plane).

**2A:** The system Ax = b is solvable if and only if the vector b can be expressed as ***a combination of the columns of A***. Then b is in the column space.

We can describe all combinations of the two columns geometrically: *Ax = b* can be solved if and only if b lies in the **plane** that is spanned by the two column vectors. This is the *thin* set of attainable b. If b lies off the plane, then it is not a combination of the two columns. In that case Ax = b has no solution.

What is important is that this plane is not just a subset of R³; it is a **subspace**. It is the column space of A, consisting of all combinations of the columns. It is denoted by ***C(A)***.

Then C(A) can be somewhere between the zero space and the whole space **Rᵐ**. Together with its perpendicular space, it gives one of our two approaches to understanding Ax = b.

<h2 id="3c94b747c25e8b676e5f7af1a67da8a5"></h2>
### The Nullspace of A

The second approach to Ax = b is "dual" to the first. 

We are concerned not only with attainable right-hand sides b, but also with the solutions x that attain them. 

The right- hand side b = 0 always allows the solution x = 0, but there may be infinitely many other solutions. (There always are, if there are more unknowns than equations, n > m.) ***The solutions to Ax = O form a vector space - the nullspace of A***.

The ***nullspace*** of a matrix consists of all vectors x such that Ax = 0. It is denoted by It is a subspace of **Rⁿ**(n维子空间), just as the column space was a subspace of **Rᵐ**.

The nullspace is easy to find for the example given above; it is as small as possible:

```
|1  0| |u|   |0|
|5  4|·|v| = |0|
|2  4|       |0|
```

The first equation gives u = 0, and the second equation then forces v = 0. ***The nullspace contains only the vector (0, 0)***. This matrix has "independent columns" - a key idea that comes soon.

The situation is changed. when a third column is a combination of the first two:

```
    |1  0  1| 
B = |5  4  9| 
    |2  4  6|  
```

B has the same column space as A. The new column lies in the same plane ; it is the sum of the two column vectors we started with. But the nullspace of B contains the vector (1, 1, -1) and automatically contains,any multiple (c, c, -c):

```
|1  0  1| | c|   |0|
|5  4  9|·| c| = |0|  
|2  4  6| |-c|   |0|
```

The nullspace of B is the line of all points x = c, y = c, z = -c. (The line goes through the origin, as any subspace must.) 

We want to be able, for any system Ax = b, to find C(A) and N(A): all attainable right-hand sides b and all solutions to Ax = 0.

The vectors b are in the column space and the vectors x are in the nullspace. 

We hope to end up by understanding all four of the subspaces that are intimately related to each other and to A - the ***column space*** of A, the ***nullspace*** of A, and their two perpendicular spaces.

<h2 id="1e0304a592cf2dccbcb3c7e858021d8d"></h2>
## 2.2 SOLVING Ax=0 and Ax=b

Chapter 1 concentrated on square invertible matrices. There was one solution to Ax = b, and it was x = A⁻¹b. That solution was found by elimination (not by computing A⁻¹). 

A rectangular matrix brings new possibilities - U may not have a full set of pivots. 

This section goes onward from U to a reduced form *R* - **the simplest matrix that elimination can give**. R reveals all solutions immediately.

For an invertible matrix, the nullspace contains only x = 0 (multiply Ax = 0 by A⁻¹). The column space is the whole space (Ax = b has a solution for every b). The new questions appear when the nullspace contains more than the zero vector and/or the column space contains less than all vectors:

 1. Any vector x_n in the nullspace can be added to a particular solution x. The solutions to all linear equations have this form, x = x_p + x_n:
    - **Ax_p = b and Ax_n = 0 produce A(x_p + x_n) = b**.
    - x_p 可能有不同的选择，任选一个即可
    - 因为 Ax_n = 0, 加上它并不影响 Ax = b
 2. When the column space doesn't contain every b in Rᵐ, we need the conditions on b that make Ax = b solvable.

```
|1  1|
|2  2|
```

 - This matrix is not invertible: y + z = b₁, and 2y + 2z = b₂ usually have no solution.
 - There is no solution **unless** b₂ = 2b₁ . The column space of A contains only those b's: the multiples of (1, 2).
 - When b₂ = 2b₁, there are ***infinitely many solutions***. 
    - A particular solution to y + z = 2 and 2y + 2z = 4 is x_p (1, 1). The nullspace of A contains (-1, 1) and all its multiples x_n = (-c, c):

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_completeSolution.png)

<h2 id="fb0727e770a06722aa7b9d64a9b6af91"></h2>
### Echelon Form(梯形) *U* and Row Reduced Form *R*

We start by simplifying this 3 by 4 matrix, first to U and then further to R:

```
    | 1  3 3 2|
A = | 2  6 9 7|
    |-1 -3 3 4|
```

The pivot a₁₁ = 1 is nonzero. The usual elementary operations will produce zeros in the first column below this pivot. The bad news appears in column 2:

```
     | 1 3 3 2|
A -> | 0 0 3 3|
     | 0 0 6 6|
```

The candidate for the second pivot has become zero: *unacceptable*. 

We look below to carry out a row exchange. In this case the entry below it is also zero. If A were square, this would signal that the matrix was singular. 

With a rectangular matrix, we must expect trouble anyway, and there is no reason to stop. All we can do is to go on to the next column, where the pivot entry is 3. Eventually we arrive at Echelon matrix U:

```
     | 1 3 3 2|
U -> | 0 0 3 3|
     | 0 0 0 0|
```

Strictly speaking, we proceed to the fourth column. A zero is in the third pivot position, and nothing can be done. U is upper triangular, but its pivots are not on the main diagonal. The nonzero entries of U have a "staircase pattern," or echelon form. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_echelon_form.png)  
***Figure 2.3***

We can always reach this echelon form U, with zeros below the pivots:

 1. The pivots are the first nonzero entries in their rows.
 2. Below each pivot is a column of zeros, obtained by elimination.
 3. Each pivot lies to the right of the pivot in the row above. This produces the staircase pattern, and zero rows come last.
 
***A = LU*** is still available

```
    | 1 0 0 |
L = | 2 1 0 |
    |-1 2 1 |
```

The only operation not required by our example, but needed in general, is row exchange by a permutation matrix P.

Here is *PA = LU* for all matrices:

 - **2B:** For any m by n matrix A there is a permutation P, a lower triangular L with unit diagonal, and an m by n echelon matrix U, such that *PA = LU*

*Now comes* ***R***. We can go further than U, to make the matrix even simpler. Divide the second row by its pivot 3, so that ***all pivots are 1***. Then use the pivot row to produce ***zero above the pivot*** (This time we subtract a row from *a higher row*). The final result (the best form we can get) is the ***reduced row echelon form R*** :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_ReducedEchelon.png)

This matrix R is the final result of elimination on A. MATLAB would use the command **R = rref (A)**. Of course rref(R) would give R again!

If A is a square invertible matrix , in that case , rref(R) is *identity matrix*.  ***rref (A) = 1***, when A is invertible.

For a 5 by 8 matrix with four pivots, Figure 2.3 shows the reduced form R. **It still contains an identity matrix, in the four pivot rows and four pivot columns**. 

 - From R we will quickly find the nullspace of A. 
 - *Rx = 0* has the same solutions as *Ux = 0* and *Ax=0*

<h2 id="1e32c695f24ac4d5108ba9cca53ac86a"></h2>
### Pivot Variables and Free Variables

Our goal is to read off all the solutions to Rx = 0. The pivots are crucial:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_nullspaceOfR.png)

 - The unknowns u, v, w, y go into two groups.
 - One group contains the ***pivot variables***, those that correspond to ***columns with pivots***.
 - The other group is made up of the ***free variables***, corresponding to ***columns without pivots***.

To find the most general solution to Rx = 0 (or, equivalently, to Ax = 0) we may assign arbitrary values to the free variables. Suppose we call these values simply v and y. The pivot variables are completely determined in terms of v and y:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_R_free_solution.png)

There is a "double infinity" of solutions, with v and y free and independent. The complete solution is a combination of two **special solutions**:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_R_free_solution2png.png)

The special solution (-3, 1, 0, 0) has free variables v = 1, y = 0. The other special solution (1, 0, -1, 1) has v = 0 and y = 1. All solutions are *linear combinations of these two*. The best way to find all solutions to Ax = 0 is from the special solutions:

 1. After reaching Rx = 0, identify the pivot variables and free variables
 2. Give one free variable the value 1, set the other free variables to 0, and solve Rx = 0 for the pivot variables. This x is a special solution.
 3. Every free variable produces its own "special solution" by step 2. The combinations of special solutions form the nullspace-all solutions to Ax = 0.

Within the 4-dimensional space of all possible vectors x, the solutions to Ax = 0 form a 2-dimensional subspace-the nullspace of A. In the example, N(A) is generated by the special vectors (-3, 1, 0, 0) and (1, 0, -1, 1). The combinations of these two vectors produce the whole nullspace.

Here is a little trick. The special solutions are especially easy from R. The numbers 3 and 0 and -1 and 1 lie in the "nonpivot columns" of R. **Reverse their signs to find the pivot variables** (not free) **in the special solutions**. I will put the two special solutions from equation (2) into a nullspace matrix N, so you see this neat pattern:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_nullspace_matrix.png)

The free variables have values 1 and 0 (formed in identity). 
 
This is the place to recognize one extremely important theorem. Suppose a matrix has more columns than rows, n > m. Since m rows can hold at most m pivots, there must be at least n - m free variables. There will be even more free variables if some rows of R reduce to zero; but no matter what, at least one variable must be free. This free variable can be assigned any value, leading to the following conclusion:

 - **2C:** If Ax ***=0*** has more unknowns than equations (n > m), it has at least one special solution: There are more solutions than the trivial x=0.

There must be infinitely many solutions, since any multiple cx will also satisfy A(cx) = 0. *The nullspace has the same "dimension" as the number of free variables and special solutions.*

This central idea-the ***dimension*** of a subspace-is made precise in the next section. We count the free variables for the nullspace. We count the pivot variables for the column space!

<h2 id="0aa8bb162b1e64c4edd71e634be16382"></h2>
### Solving Ax = b, Ux = c, and Rx = d

The case b≠0 is quite different from b = 0. The row operations on A must act also on the right-hand side (on b). 

We begin with letters (b1, b2, b3) to find the solvability condition - for b to lie in the column space. Then we choose b = (1, 5, 5) and find all solutions x.

For the original example Ax = b = (b1, b2, b3), apply to both sides the operations that led from A to U. The result is an upper triangular system Ux = c:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_echelon_on_both_side.png)   (3)
 
Start now with Ux = c.   c is just L⁻¹b.

It is not clear that these equations have a solution. The third equation is very much in doubt, because its left-hand side is zero. The equations are inconsistent unless b3 - 2b2 + 5b1 = 0. Even though there are more unknowns than equations, there may be no solution. 

We know another way of answering the same question: Ax = b can be solved if and only if b lies in the column space of A. This subspace comes from the four columns of A (not of U!):

```
    | 1  3 3 2|
    | 2  6 9 7|
    |-1 -3 3 4|
```

Even though there are four vectors, their combinations only fill out a plane in three- dimensional space. Column 2 is three times column 1. The fourth column equals the third minus the first. *These dependent columns, the second and fourth, are exactly the ones without pivots.*

The column space C(A) can be described in two different ways. On the one hand, it is the plane generated by columns 1 and 3. The other columns lie in that plane, and contribute nothing new. Equivalently, it is the plane of all vectors b that satisfy b3 - 2b2 + 5b1 = 0; this is the constraint if the system is to be solvable. ***Every column satisfies this constraint, so it is forced on b!*** Geometrically, we shall see that the vector (5, -2, 1) is perpendicular to each column.
 
If b belongs to the column space, the solutions of Ax = b are easy to find. The last equation in Ux = c is 0 = 0. To the free variables v and y, we may assign any values, as before. The pivot variables u and w are still determined by back-substitution. For a specific example with b3 - 2b2 + 5b1 = 0, choose b = (1, 5, 5):

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_solve_uxc.png)  
(4)

***Every solution to Ax = b is the sum of one particular solution and a solution to Ax = 0:***

`X_complete = X_particular + X_nullspace`

The particular solution in equation (4) comes from solving the equation with *all free variables set to zero*. That is the only new part, since the nullspace is already computed. When you multiply the highlighted equation by A, you get Ax_complete = b + 0.

Geometrically, the solutions again fill a two-dimensional surface - but it is not a subspace. It does not contain x = 0. It is parallel to the nullspace we had before, shifted by the particular solution x_p as in Figure 2.2. Equation (4) is a good way to write the answer:

 1. Reduce Ax = b to Ux = c.
 2. With free variables = 0, find a particular solution to Ax_p = b and Ux_p = c.
 3. Find the special solutions to Ax = 0 (or Ux = 0 or Rx = 0). Each free variable, in turn, is 1. Then x = x_p + (any combination x_n of special solutions).
