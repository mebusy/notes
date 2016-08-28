...menustart

 - [Elgenvalues and Elgenvectors](#8358d3063f9f8db669067bc62cf5ea5e)
	 - [5.1 INTRODUCTION](#103445c268b50fae9bd814331a04faa4)

...menuend



<h2 id="8358d3063f9f8db669067bc62cf5ea5e"></h2>
# Elgenvalues and Elgenvectors


<h2 id="103445c268b50fae9bd814331a04faa4"></h2>
## 5.1 INTRODUCTION

This chapter begins the "second half" of linear algebra. 

The first half was about Ax = b. The new problem Ax = λx  will still be solved by simplifying a matrix -- making it diagonal if possible. 

*The basic step is no longer to subtract a multiple of one row from another*. Elimination changes the eigenvalues, which we don't want.

Determinants give a transition from Ax = b to Ax = λx. In both cases the determinant leads to a "formal solution": to Cramer's rule for x = A⁻¹b, and to the polynomial det (A - λI), whose roots will be the eigenvalues. (All matrices are now square; the eigenvalues of a rectangular matrix make no more sense than its determinant.) The determinant can actually be used if n = 2 or 3. For large n, computing λ, is more difficult than solving Ax = b.

The first step is to understand how eigenvalues can be useful. One of their applications is to ordinary differential equations. We shall not assume that the reader is an expert on differential equations ! If you can differentiate xⁿ, sin x, and eˣ, you know enough. As a specific example, consider the coupled pair of equations

```
dv/dt = 4v - 5w,  v = 8 at t=0,
dw/dt = 2v - 3w,  w = 5 at t=0.		(1)
```

This is an ***initial-value problem***. The unknown is specified at time t = 0 by the given initial values 8 and 5. The problem is to find v(t) and w(t) for later times t > 0. 

It is easy to write the system in matrix form. Let the unknown vector be u(t), with initial value u(0). The coefficient matrix is A:

```
Vector unknown :

u(t) = ⎡v(t)⎤, u(0) = ⎡8⎤,  A = ⎡4 -5⎤
	   ⎣w(t)⎦		  ⎣5⎦		⎣2 -3⎦
```

The two coupled equations become the vector equation we want:

```
Matrix form :

du/dt = Au    with u = u(0) at t=0  (2)
```

This is the basic statement of the problem. Note that it is a first-order equation -- no higher derivatives appear -- and it is *linear* in the unknowns. It also has *constant coefficients*; the matrix A is independent of time.

How do we find u(t)? If there were only one unknown instead of two, that question
would be easy to answer. We would have a scalar instead of a vector equation:

```
Single equation :

du/dt = au   with  u = u(0) at t=0	(3)
```

The solution to this equation is the one thing you need to know:

```
Pure exponential 	u(t) = eᵅᵗu(0)	(4)
```

At the initial time t = 0, u equals u(0) because e⁰ = 1. The derivative of eᵅᵗ has the required factor *a*, so that du/dt = au. Thus the initial condition and the equation are both satisfied.

We shall take a direct approach to systems, and look for solutions with the *same exponential dependence* on *t* just found in the scalar case:

 - v(t) = e<sup>λ</sup>ᵗy

 - w(t) = e<sup>λ</sup>ᵗz &nbsp;&nbsp;&nbsp;&nbsp;(5)

or in vector notation:

 - u(t) = e<sup>λ</sup>ᵗx. &nbsp;&nbsp;&nbsp;&nbsp;(6)

This is the whole key to differential equations du/dt = Au:  ***Look for pure exponential solutions***. Substituting v = e<sup>λ</sup>ᵗy and w = e<sup>λ</sup>ᵗz into the equation, we find

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_dif_equation.png)

he factor e<sup>λ</sup>ᵗ is common to every term, and can be removed. This cancellation is the reason for assuming the same exponent λ for both unknowns; it leaves

```
Eigenvalue problem :

4y - 5z = λy
2y - 3z = λz.	  (7)
```

That is the eigenvalue equation. 

In matrix form it is Ax = λx. You can see it again if we use u = e<sup>λ</sup>ᵗx -- a number e<sup>λ</sup>ᵗ that grows or decays times a fixed vector x. ***Substituting into du/dt = Au gives λe<sup>λ</sup>ᵗx = Ae<sup>λ</sup>ᵗx. The cancellation of eat produces***

```
Eigenvalue equation :

Ax = λx.	(8)
```

Now we have the fundamental equation of this chapter. It involves two unknowns λ and x. It is an algebra problem, and differential equations can be forgotten! The number λ (lambda) is an ***eigenvalue*** of the matrix A, and the vector x is the associated ***eigenvector***.
Our goal is to find the eigenvalues and eigenvectors, λ's and x's, and to use them.

---

**The Solutions of Ax = λx**

Notice that Ax = λx is a nonlinear equation; λ multiplies x. If we could discover λ., then the equation for x would be linear. In fact we could write λIx in place of λx, and bring this term over to the left side:

```
(A - λI)x = 0.		(9)
```

The identity matrix keeps matrices and vectors straight; the equation (A - λ)x = 0 is
shorter, but mixed up. This is the key to the problem:

 - ***The vector x is in the nullspace of A - λI***.
 - ***The number λ, is chosen so that A - λI has a nullspace***.

Of course every matrix has a nullspace. We want a *nonzero* eigenvector x.  The goal is to build u(t) out of exponentials e<sup>λ</sup>ᵗx , and *we are interested only in those particular values λ for which there is a nonzero eigenvector x.  To be of any use, the nullspace of A - λI must contain vectors other than zero. In short, A - λI ***must be singular***.

For this, the determinant gives a conclusive test.

**5A**: The number λ is an eigenvalue of A if and only if A - λI is singular:

```
det( A - λI ) = 0.		(10)
```

This is the characteristic equation. Each λ is associated with eigenvectors x:

```
(A - λI)x = 0	or 	 Ax = λx.	(11)
```

In our example, we shift A by λI to make it singular:

```
Subtract λI :

A - λI = ⎡4-λ   -5 ⎤.
		 ⎣ 2   -3-λ⎦
```

Note that λ is subtracted only from the main diagonal (because it multiplies I).


```
Determinant :

|A - λI| = (4 - λ)(-3 - λ) + 10   or   λ² - λ - 2.
```

This is the *characteristic polynomial*. Its roots, where the determinant is zero, are the eigenvalues. They come from the general formula for the roots of a quadratic, or from factoring into λ² - λ - 2 = (λ + 1) (λ - 2).  That is zero if λ = -1 or λ = 2, as the general formula confirms:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple.png)

**There are two eigenvalues, because a quadratic has two roots.** Every 2 by 2 matrix A - λI has λ² (and no higher power of λ²) in its determinant.

The values λ = -1 and λ = 2 lead to a solution of Ax = λx or (A - λI )x = 0. A matrix with zero determinant is singular, so there must be nonzero vectors x in its nullspace. In fact the nullspace contains a whole line of eigenvectors; it is a subspace!

```
λ₁ = -1: (A - λ₁I)x = ⎡5  -5⎤⎡y⎤ = ⎡0⎤.
					  ⎣2  -2⎦⎣z⎦   ⎣0⎦
```

The solution (the first eigenvector) is any nonzero multiple of x₁:

```
Eigenvector for λ₁ :

x₁ = ⎡1⎤.
	 ⎣1⎦
```

The computation for λ₂ is done separately:

```
λ₂ = 2: (A - λ₂I)x = ⎡2  -5⎤⎡y⎤ = ⎡0⎤.
					 ⎣2  -5⎦⎣z⎦   ⎣0⎦
```

The second eigenvector is any nonzero multiple of x₂:

```
Eigenvector for λ₂ :

x₂ = ⎡5⎤.
	 ⎣2⎦
```

You might notice that the columns of A - λ₁I give x₂, and the columns of A - λ₂I are multiples of x₁. *This is special (and useful) for 2 by 2 matrices*.

In the 3 by 3 case, I often set a component of x equal to 1 and solve (A - λI)x = 0 for the other components(因为满足条件的x很多). Of course if x is an eigenvector then so is 7x and so is -x. All vectors in the nullspace of A - λI (which we call the *eigenspace*) will satisfy Ax = λx. In our example the eigenspaces are the lines through x₁ = (1, 1) and x₂ = (5, 2).

Before going back to the application (the differential equation), we emphasize the steps in solving Ax = λx:

 1. ***Compute the determinant of A - λI***. 
 	- With λ, subtracted along the diagonal, this determinant is a polynomial of degree n. It starts with (-λ)ⁿ.
 2. ***Find the roots of this polynomial***. 
 	- The n roots are the eigenvalues of A.
 3. ***For each eigenvalue solve the equation (A - λI)x = 0***. 
 	- Since the determinant is zero, there are solutions other than x = 0. Those are the eigenvectors.


In the differential equation, this produces the special solutions u = e<sup>λ</sup>ᵗx . They are the *pure exponential solutions* to du/dt = Au. Notice e⁻ᵗ and e²ᵗ:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple_001.png)

There two special solutions give the complete solution. They can be multiplied by any numbers c₁ and c₂, and they can be added together. When u₁ and u₂ satisfy the linear equation du/dt = Au, so does their sum u₁ + u₂.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple_012.png)

This is ***superposition***, and it applies to differential equations (homogeneous and linear) just as it applied to matrix equations Ax = 0. The nullspace is always a subspace, and combinations of solutions are still solutions.

Now we have two free parameters c₁ and c₂, and it is reasonable to hope that they can be chosen to satisfy the initial condition u = u(0) at t = 0:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple_013.png)

The constants are c₁ = 3 and c₂ = 1, and the solution to the original equation is

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple_014.png)

Writing the two components separately, we have v (0) = 8 and w (0) = 5:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_eigenvalues_4_exmaple_014.1.png)

The key was in the eigenvalues λ and eigenvectors x. Eigenvalues are important in themselves, and not just part of a trick for finding *u*. 

Probably the homeliest example is that of soldiers going over a bridge.  Traditionally, they stop marching and just walk across. If they happen to march at a frequency equal to one of the eigenvalues of the bridge, it would begin to oscillate. (Just as a child's swing does; you soon notice the natural frequency of a swing, and by matching it you make the swing go higher.) An engineer tries to keep the natural frequencies of his bridge or rocket away from those of the wind or the sloshing of fuel. And at the other extreme, a stockbroker spends his life trying to get in line with the natural frequencies of the market. The eigenvalues are the most important feature of practically any dynamical system.


**Summary and Examples**

To summarize, this introduction has shown how λ and x appear naturally and automatically when solving du/dt = Au. Such an equation has pure exponential solutions u = e<sup>λ</sup>ᵗx ; the eigenvalue gives the rate of growth or decay, and the eigenvector x develops at this rate. The other solutions will be mixtures of these pure solutions, and the mixture is adjusted to fit the initial conditions.

The key equation was Ax = λx. Most vectors x will not satisfy such an equation. They change direction when multiplied by A, so that Ax is not a multiple of x. This means that ***only certain special numbers λ are eigenvalues, and only certain special vectors x are eigenvectors***. We can watch the behavior of each eigenvector, and then combine these "normal modes" to find the solution. To say the same thing in another way, the underlying matrix can be diagonalized.

The diagonalization in Section 5.2 will be applied to difference equations, Fibonacci numbers, and Markov processes, and also to differential equations. In every example, we start by computing the eigenvalues and eigenvectors; there is no shortcut to avoid that. Symmetric matrices are especially easy. "Defective matrices" lack a full set of eigenvectors, so they are not diagonalizable. Certainly they have to be discussed, but we will not allow them to take over the book. We start with examples of particularly good matrices.

Example 1: Everything is clear when A is a ***diagonal matrix***:

```
A = ⎡3 0⎤ has λ₁ = 3 with x₁ = ⎡1⎤,  λ₂ = 2 with x₂ = ⎡0⎤.
	⎣0 2⎦  					   ⎣0⎦					  ⎣1⎦
```

On each eigenvector A acts like a multiple of the identity: Ax₁ = 3x₁ and Ax₂ = 2x₂. Other vectors like x = (1, 5) are mixtures x₁ + 5x₂ of the two eigenvectors, and when A multiplies x₁ and x₂ it produces the eigenvalues  λ₁ = 3 and x₂ = 2:

```
A  times  x₁+5x₂  is 3x₁+10x₂ = ⎡ 3⎤.  
								⎣10⎦
```

This is Ax for a typical vector x -- not an eigenvector. But the action of A is determined by its eigenvectors and eigenvalues.



Example 2: The eigenvalues of a ***projection matrix*** are 1 or 0!

```
P = ⎡1/2 1/2⎤ has λ₁ = 1 with x₁ = ⎡1⎤,  λ₂ = 0 with x₂ = ⎡ 1⎤.
	⎣1/2 1/2⎦  					   ⎣1⎦					  ⎣-1⎦
```

We have λ = 1 when x projects to itself, and λ = 0 when x projects to the zero vector. The column space of P is filled with eigenvectors, and so is the nullspace. If those spaces have dimension r and n - r, then k = 1 is repeated r times and A = 0 is repeated n - r times (always n λ's):

```
Four eigenvalues allowing repeats:

	⎡1 0 0 0⎤
P = ⎢0 0 0 0⎥ 	has λ = 1,1,0,0
 	⎢0 0 0 0⎥   
	⎣0 0 0 1⎦ 
```

***There is nothing exceptional about λ = 0***. Like every other number, zero might be an eigenvalue and it might not. If it is, then its eigenvectors satisfy Ax = Ox. Thus x is in the nullspace of A. A zero eigenvalue signals that A is singular (not invertible); its determinant is zero. Invertible matrices have all λ ≠ 0.

Example 3: The eigenvalues are on the main diagonal when A is ***triangular***:

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigen_example_3.png)

The determinant is just the product of the diagonal entries. It is zero if λ=1, λ=3/4, or λ=1/2; the eigenvalues were already sitting along the main diagonal.

This example , in which the eigenvalues can be found by inspection, points to one main theme of the chapter: *To transform A into a diagonal or triangular matrix* ***without changing its eigenvalues***. We emphasize once more that the Gaussian factorization A = LU is not suited to this purpose. The eigenvalues of *U* may be visible on the diagonal, but they are ***not*** the eigenvalues of A.

For most matrices, there is no doubt that the eigenvalue problem is computationally more difficult that Ax = b.

With linear systems, a finite number of elimination steps produced the exact answer in a finite time. (Or equivalently, Cramer's rule gave an exact formula for the solution.) No such formula can give the eigenvalues, or Galois would turn in his grave. For a 5 by 5 matrix, det (A - λI) involves λ⁵. Galois and Abel proved that there can be no algebraic formula for the roots of a fifth-degree polynomial.

All they will allow is a few simple checks on the eigenvalues, *after* they have been computed, and we mention two good ***sum and product***.

**5B**: The ***sum*** of the n eigenvalues equals the sum of the n diagonal entries.

```
Trace of A = λ₁ + ... + λn = a₁₁ + ... + ann   (15)
```

Furthermore, the ***product*** of the n eigenvalues equals the ***determinant*** of A.

---

The projection matrix *P* had diagonal entries 1/2, 1/2 and eigenvalues 1, 0.  Then 1/2 + 1/2
agrees with 1 + 0 as it should. So does the determinant, which is 0·1 = 0. *A singular matrix, with zero determinant, has one or more of its eigenvalues equal to zero*.

There should be no confusion between the diagonal entries and the eigenvalues. For a triangular matrix they are the same -- but that is exceptional. Normally the pivots, diagonal entries, and eigenvalues are completely different. And for a 2 by 2 matrix, the trace and determinant tell us everything:

```
⎡a b⎤ has trace a+d , and determinant ad-bc
⎣c d⎦
```

```
det(A-λI) = det |a-λ   b | = λ² - (trace)λ + determinat 
				| c   d-λ|
```

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigenvalue_formular_for_2x2.png)


**Eigshow**

There is a MATLAB demo (just type eigshow), displaying the eigenvalue problem for a 2 by 2 matrix. 

It starts with the unit vector x = (1, 0). *The mouse makes this vector move around the unit circle*. At the same time the screen shows Ax, in color and also moving. Possibly Ax is ahead of x. Possibly Ax is behind x. Sometimes Ax is parallel to x. At that parallel moment, Ax = λx (twice in the second figure).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_eigenshow.png)

The eigenvalue λ is the length of Ax, when the ***unit*** eigenvector x is parallel. The built-in choices for A illustrate three possibilities: 0, 1, or 2 real eigenvectors.

 1. There are *no real eigenvectors*. Ax *stays behind or ahead of* x. 
 	This means the eigenvalues and eigenvectors are complex, as they are for the rotation Q.
 2. There is only one line of eigenvectors (unusual).  The moving directions Ax and x meet but don't cross. 
 	- This happens for the last 2 by 2 matrix below.
 3. There are eigenvectors in two independent directions. This is typical! 
 	- Ax crosses x at the first eigenvector x₁, and it crosses back at the second eigenvector x₂.

Suppose A is singular (rank 1). Its column space is a line. The vector Ax has to stay on that line while x circles around. 

One eigenvector x is along the line. Another eigenvector appears when Ax₂ = 0. Zero is an eigenvalue of a singular matrix.

You can mentally follow x and Ax for these six matrices. How many eigenvectors and where? When does Ax go clockwise, instead of counterclockwise with x ?

```
A = ⎡2 0⎤ ⎡2  0⎤ ⎡0 1⎤ ⎡ 0 1⎤ ⎡1 1⎤ ⎡1 1⎤ 
	⎣0 1⎦ ⎣0 -1⎦ ⎣1 0⎦ ⎣-1 0⎦ ⎣1 1⎦ ⎣0 1⎦ 
```


---

## 5.2 DIAGONALIZATION OF A MATRIX

We start right off with the one essential computation. It is perfectly simple and will be used in every section of this chapter. ***The eigenvectors diagonalize a matrix***:

**5C** Suppose the n by n matrix A has n linearly independent eigenvectors.If these eigenvectors are the columns of a matrix S. then S⁻¹AS is a diagonal matrix Λ. The eigenvalues of A are on the diagonal of Λ:

```
Diagonalization:

				⎡λ₁       ⎤
   S⁻¹AS = Λ =  ⎢  λ₂ 	  ⎥.	(1)
   				⎢    ...  ⎥
  				⎣       λn⎦
```

We call S the "eigenvector matrix" and Λ the "eigenvalue matrix".

***Proof*** Put the eigenvectors xᵢ in the columns of S, and compute AS by columns:

```
     ⎡ |  |      |  ⎤   ⎡ |    |        |   ⎤
AS = ⎢ x₁ x₂ ... xn ⎥ = ⎢λ₁x₁ λ₂x₂ ... λnxn ⎥.
     ⎢ |  |      |  ⎥   ⎢ |    |	|   ⎥
     ⎣ |  |      |  ⎦   ⎣ |    |        |   ⎦
```

> A * eigenvector x, 就会 引出 eigenvalue.

Then the trick is to split this last matrix into a quite different product SA:

```
     ⎡                  ⎤   ⎡              ⎤ ⎡λ₁       ⎤
AS = ⎢λ₁x₁ λ₂x₂ ... λnxn⎥ = ⎢ x₁ x₂ ... xn ⎥ ⎢  λ₂     ⎥.
     ⎢                  ⎥   ⎢              ⎥ ⎢    ...  ⎥
     ⎣                  ⎦   ⎣              ⎦ ⎣       λn⎦
```

```
AS = SΛ , or S⁻¹AS = Λ , or A = SΛS⁻¹	(2)
```

S is invertible, because its columns (the eigenvectors) were assumed to be independent. 

We add four remarks before giving any examples or applications.

***Remark 1*** If the matrix A has no repeated eigenvalues -- the numbers λ₁,...,λn are distinct -- then its n eigenvectors are automatically independent (see 5D below). Therefore ***any matrix with distinct eigenvalues can be diagonalized***.

> TODO: [1 0 ; 0 1] has 2 same eigenvalue.

***Remark 2*** The diagonalizing matrix S is *not unique*. An eigenvector x can be multiplied by a constant, and remains an eigenvector. We can multiply the columns of S by any nonzero constants, and produce a new diagonalizing S. 

Repeated eigenvalues leave even more freedom in S. For the trivial example A = I, any invertible S will do: SIS⁻¹ is always diagonal (Λ is just I). All vectors are eigenvectors of the identity.


***Remark 3*** *Other matrices S will not produce a diagonal Λ*. Suppose the first column of S is y. Then the first column of SΛ is λ₁y. If this is to agree with the first column of AS, which by matrix multiplication is Ay, then y must be an eigenvector: Ay = λ₁y. The *order* of the eigenvectors in S and the eigenvalues in Λ is automatically the same.


***Remark 4*** Not all matrices possess n linearly independent eigenvectors, so not all matrices are diagonalizable.  The standard example of a "defective matrix" is

```
A = ⎡0 1⎤. 
	⎣0 0⎦ 
```

Its eigenvalues are λ₁ = λ₂ = 0, since it is triangular with zeros on the diagonal:

```
det( A-λI ) = det⎡-λ  1⎤ = λ² . 
				 ⎣ 0 -λ⎦ 
```

All eigenvectors of this A are multiples of the vector (1, 0):

```
  ⎡0 1⎤x = ⎡0⎤,  or x = ⎡c⎤. 
  ⎣0 0⎦    ⎣0⎦ 			⎣0⎦ 
```

λ = 0 is a double eigenvalue -- its *algebraic multiplicity* (代数重数) is 2. But the *geometric multiplicity* is 1 -- there is only one independent eigenvector. We can't construct S.

Here is a more direct proof that this A is not diagonalizable. Since λ₁ = λ₂ = 0, Λ would have to be the zero matrix. But if Λ = S⁻¹AS = 0, then we premultiply by S and postmultiply by S⁻¹, to deduce falsely that A = 0. There is no invertible S.

That failure of diagonalization was ***not*** a result of λ = 0. It came from λ₁ = λ₂ :

```
Repeated eigenvalues:

A = ⎡3 1⎤  and A = ⎡2 -1⎤. 
    ⎣0 3⎦    	   ⎣1  0⎦ 
```

Their eigenvalues are 3, 3 and 1, 1. They are not singular! The problem is the shortage of eigenvectors -- which are needed for S. That needs to be emphasized:

 - ***Diagonalizability of A depends on enough eigenvectors***. 
 - ***Invertibility of A depends on nonzero eigenvalues***.

There is no connection between diagonalizability (n independent eigenvectors) and invertibility (no zero eigenvalues). 

The only indication given by the eigenvalues is this: *Diagonalization can fail only if there are repeated eigenvalues*. (注意是 ***can***) Even then, it does not always fail. A = I has repeated eigenvalues 1 , 1, ... , 1 but it is already diagonal! There is no shortage of eigenvectors in that case.

The test is to check, for an eigenvalue that is repeated *p* times, whether there are *p* independent eigenvectors -- in other words, whether A - λI has rank n - *p*. To complete that circle of ideas, we have to show that *distinct* eigenvalues present no problem.

**5D** If eigenvectors x₁, ..., x<sub>k</sub> correspond to *different* eigenvalue λ₁,...,λ<sub>k</sub>  then those eigenvectors are linearly independent.

Suppose first that k = 2, and that some combination of x₁ and x₂ produces zero: c₁x₁ + c₂x₂ = 0. Multiplying by A, we find c₁λ₁x₁ + c₂λ₂x₂ = 0. Subtracting λ₂ times the previous equation, the vector x₂ disappears:

```
  c₁(λ₁-λ₂)x₁ = 0.
```






