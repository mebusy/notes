...menustart

 - [Elgenvalues and Elgenvectors](#8358d3063f9f8db669067bc62cf5ea5e)
	 - [5.1 INTRODUCTION](#103445c268b50fae9bd814331a04faa4)
	 - [5.2 DIAGONALIZATION OF A MATRIX](#a208ce5ccf9b8c57cd42ced0c19eca2e)
	 - [5.3 DIFFERENCE EQUATIONS AND POWERS Aᵏ](#b7b97b347a818a45c3aa318285ba99b7)
		 - [Fibonacci Numbers](#fdd5b4c8c15384ed3cceda4fe4cc38d6)
		 - [Markov Matrices](#bdfe38b6c05d238d6cb0df431aea8cb7)
		 - [Stability of u<sub>k+1</sub> = Au<sub>k</sub>](#ececb2267f15a71d7ecad9272b25ab4a)
		 - [Positive Matrices and Applications in Economics](#ee24aae762a9409f153f67ec07bbee34)
	 - [5.4 DIFFERENTIAL EQUATIONS AND eᴬᵗ  (TODO)](#6949286af35bec96be99401b85d929c5)
	 - [5.5 COMPLEX MATRICES](#8790e803d7a4cc615fb758ad25c12f30)
	 - [5.6 SIMILARITY TRANSFORMATIONS](#752452230e3a6aebda46452d7a021688)
		 - [Change of Basis = Similarity Transformation](#5f520f3a47da08c25d74016f54696110)

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

<h2 id="a208ce5ccf9b8c57cd42ced0c19eca2e"></h2>
## 5.2 DIAGONALIZATION OF A MATRIX

We start right off with the one essential computation. It is perfectly simple and will be used in every section of this chapter. ***The eigenvectors diagonalize a matrix***:

**5C** Suppose the n by n matrix A has n linearly independent eigenvectors.If these eigenvectors are the columns of a matrix S. then S⁻¹AS is a diagonal matrix Λ. The eigenvalues of A are on the diagonal of Λ:

```
Diagonalization:

              ⎡λ₁       ⎤
  S⁻¹AS = Λ = ⎢  λ₂     ⎥.	(1)
              ⎢    ...  ⎥
              ⎣       λn⎦
```

We call S the "eigenvector matrix" and Λ the "eigenvalue matrix".

***Proof*** Put the eigenvectors xᵢ in the columns of S, and compute AS by columns:

```
     ⎡ |  |      |  ⎤   ⎡ |    |        |   ⎤
AS = ⎢ x₁ x₂ ... xn ⎥ = ⎢λ₁x₁ λ₂x₂ ... λnxn ⎥.
     ⎢ |  |      |  ⎥   ⎢ |    |        |   ⎥
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

Since λ₁ ≠ λ₂ and x₁ ≠ 0, we are forced into c₁ = 0. Similarly c2 = 0, and the two vectors are independent; only the trivial combination gives zero.

This same argument extends to any number of eigenvectors. Therefore eigenvectors that come from distinct eigenvalues are automatically independent.

A matrix with n distinct eigenvalues can be diagonalized. This is the typical case.

**Examples of Diagoinalization**

The main point of this section is S⁻¹AS = Λ. The egenvector matrix S converts A into its eigenvalue matrix Λ (diagonal). We see this for projections and rotations.

Example 1: The projection A = [0.5 0.5 ; 0.5 0.5] has eigenvalue matrix [1 0 ; 0 0]. The eigenvectors go into the the columens of S:

```
A = ⎡1  1⎤  and AS = SΛ = ⎡1 0⎤. 
    ⎣1 -1⎦    	   		  ⎣1 0⎦ 
```

The last equation can be verified at a glance. Therefore S⁻¹AS = Λ.

Example 2: The eigenvalues themselves are not so clear for a ***rotation***:

```
90° rotation 		K = ⎡0 -1⎤  has   det(K - λI)=λ² + 1 
            		    ⎣1  0⎦  
```

***How can a vector be rotated and still have its direction unchanged?*** Apparently it can't -- except for the zero vector, which is useless. But there must be eigenvalues, and we must be able to solve du/dt = Ku. The characteristic polynomial A² + 1 should still have two roots  -- but those roots are *not real*.

The eigenvalues of K are *imaginary numbers*, A₁ = i and A₂ = -i. The eigenvectors are also not real. Somehow, in turning through 90°, they are multiplied by i or -i:

```
(K-λ₁I)x₁ = ⎡-i -1⎤⎡y⎤ = ⎡0⎤  and  x₁ = ⎡ 1⎤
    		⎣ 1 -i⎦⎣z⎦   ⎣0⎦ 			⎣-i⎦ 

(K-λ₂I)x₂ = ⎡ i -1⎤⎡y⎤ = ⎡0⎤  and  x₂ = ⎡ 1⎤. 
    		⎣ 1  i⎦⎣z⎦   ⎣0⎦ 			⎣-i⎦ 
```

The eigenvalues are distinct, even if imaginary, and the eigenvectors are independent. They go into the columns of S:

```
S = ⎡ 1 1⎤  and   S⁻¹KS = ⎡i  0⎤. 
    ⎣-i i⎦    	   		  ⎣0 -i⎦ 
```

We are faced with an inescapable fact, that ***complex numbers are needed even for real matrices***. If there are too few real eigenvalues, there are always n complex eigenvalues. (Complex includes real, when the imaginary part is zero.) If there are too few eigenvectors in the real world R³, or in Rⁿ, we look in C³ or Cⁿ. The space Cⁿ contains all column vectors with complex components, and it has new definitions of length and inner product and orthogonality. But it is not more difficult than Rⁿ , and in Section 5.5 we make an easy conversion to the complex case.

**Powers and Products: Aᵏ and AB**

There is one more situation in which the calculations are easy. ***The eigenvalues of A² are exactly λ₁², ... , λn² , and every eigenvector of A is also an eigenvector of A²***. We start from Ax = λx, and multiply again by A:

```
A²x = Aλx = λAx = λ²x.		(3)
```

Thus λ² is an eigenvalue of A², with the same eigenvector x.  If the first multiplication by A leaves the direction of x unchanged, then so does the second.

The same result comes from diagonalization, by squaring S⁻¹AS = Λ:

```
Eigenvalues of A²

(S⁻¹AS)(S⁻¹AS) = Λ²   or  S⁻¹A²S = Λ²
```

The matrix A² is diagonalized by the same S, *so the eigenvectors are unchanged*. The eigenvalues are squared. This continues to hold for any power of A:

**5E** The eigenvalues of Aᵏ are λ₁ᵏ, ... , λnᵏ, and each eigenvector of A is still an eigenvector of Aᵏ. When S diagonalizes A. it also diagonalizes Aᵏ:

```
Λᵏ = (S⁻¹AS)(S⁻¹AS)...(S⁻¹AS) = S⁻¹AᵏS.		(4)
```

If A is invertible this rule also applies to its inverse (the power k = -1). ***The eigenvalues of A⁻¹ are 1/λᵢ***. That can be seen even without diagonalizing:

```
if Ax = λx  then  x = λA⁻¹x  and  (1/λ)x = A⁻¹x.
```

Example 3: If K is rotation through 90°, then K² is rotation through 180° (which means -I) and K⁻¹ is rotation through -90°:

```
K = ⎡0 -1⎤,  K² = ⎡-1  0⎤,  and  K⁻¹ = ⎡ 0  1⎤.
    ⎣1  0⎦ 		  ⎣0  -1⎦ 			   ⎣-1  0⎦ 
```

The eigenvalues of K are i and -i; their squares are -1 and -1; their reciprocals 倒数 are 1/i = -i and 1/(-i) = i. Then K⁴ is a complete rotation through 360°:

```
K⁴ = ⎡1 0⎤  and also  Λ⁴ = ⎡i⁴   0  ⎤ = ⎡1 0⎤.
     ⎣0 1⎦                 ⎣0  (-i)⁴⎦   ⎣0 1⎦ 
```

For a ***product of two matrices***, we can ask about the eigenvalues of AB -- but we won't get a good answer. It is very tempting to try the same reasoning, hoping to prove what is *not in general true*. If λ is an eigenvalue of A and μ is an eigenvalue of B, here is the false proof that AB has the eigenvalue μλ:

```
False proof: ABx = μλx.
```

The mistake lies in assuming that A and B share the *same* eigenvector x. In general, they do not. We could have two matrices with zero eigenvalues, while AB has λ = 1:

```
AB = ⎡0 1⎤ ⎡0 0⎤ = ⎡1 0⎤.
     ⎣0 0⎦ ⎣1 0⎦   ⎣0 0⎦ 
```

The eigenvectors of this A and B are completely different, which is typical. For the same reason, the eigenvalues of A + B generally have nothing to do with λ + μ.

If the eigenvector is the same for A and B, then the eigenvalues multiply and AB has the eigenvalue μλ. But there is something more important. There is an easy way to recognize when A and B share a full set of eigenvectors, and that is a key question in quantum mechanics:

**5F** Diagonalizable matrices share the same eigenvectormatrix S if and only if AB = BA.

***Proof*** If the same S diagonalizes both A = SΛ₁S⁻¹ and B = SΛ₂S⁻¹, we can multiply in either order:

```
AB = SΛ₁S⁻¹ SΛ₂S⁻¹ = SΛ₁Λ₂S⁻¹ and  BA = SΛ₂S⁻¹ SΛ₁S⁻¹ = SΛ₂Λ₁S⁻¹.
```

Since Λ₁Λ₂ = Λ₂Λ₁ (diagonal matrices always commute) we have AB = BA. (this is what means commute)

In the opposite direction, suppose AB = BA. Starting from Ax = λx, we have

```
ABx = BAx = Bλx = λBx.
```

Thus x and Bx are both eigenvectors of A, sharing the same λ, (or else Bx = 0). If we assume for convenience that the eigenvalues of A are distinct -- the eigenspaces are all one-dimensional -- then Bx must be a multiple of x. In other words x is an eigenvector of B as well as A. The proof with repeated eigenvalues is a little longer.  _



***Heisenberg's uncertainty principle*** comes from noncommuting matrices, like position P and momentum Q. Position is symmetric, momentum is skew-symmetric, and together they satisfy QP - PQ = I. The uncertainty principle follows directly from the Schwarz inequality (Qx)ᵀ(Px) ≤ ‖Qx‖ ‖Px‖ of Section 3.2:

```
‖x‖² = xᵀx = xᵀ(QP - PQ)x ≤ 2 ‖Qx‖ ‖Px‖ .
```

The product of ‖Qx‖/‖x‖ and ‖Px‖/‖x‖ -- momentum and position errors, when the wave function is x -- is at least 1/2. It is impossible to get both errors small, because when you try to measure the position of a particle you change its momentum.

At the end we come back to A = SΛS⁻¹. ***That factorization is particularly suited to take powers of A***, and the simplest case A² makes the point. The LU factorization is hopeless when squared, but SΛS⁻¹ is perfect. The square is SΛ²S⁻¹, and the eigenvectors are unchanged. By following those eigenvectors we will solve difference equations and differential equations.

---

<h2 id="b7b97b347a818a45c3aa318285ba99b7"></h2>
## 5.3 DIFFERENCE EQUATIONS AND POWERS Aᵏ

Difference equations u<sub>k</sub>₊₁ = Au<sub>k</sub> move forward in a finite number of finite steps. 

A differential equation takes an infinite number of infinitesimal (无穷小) steps, but the two theories stay absolutely in parallel. 

It is the same analogy between the discrete and the continuous that appears over and over in mathematics. A good illustration is compound interest, when the time step gets shorter.

Suppose you invest $1000 at 6% interest. Compounded once a year, the principal P is multiplied by 1.06. *This is a difference equation P<sub>k</sub>₊₁ = AP<sub>k</sub> = 1.06 P<sub>k</sub> with a time step of one year*. After 5 years, the original P₀ = 1000 has been multiplied 5 times:

```
Yearly P₅ = (1.06)⁵P₀   which is   (1.06)⁵ 1000 = $1338.
```


Now suppose the time step is reduced to a month. The new difference equation is P<sub>k</sub>₊₁ = (1 + .06/12)P<sub>k</sub>  . After 5 years, or 60 months, you have $11 more:

```
Monthly P₆₀ = (1 + .06/12)⁶⁰P₀   which is   (1.005)⁶⁰ 1000 = $1349.
```


The next step is to compound every day, on 5(365) days. This only helps a little:

```
Daily compounding   (1 + .06/365)⁵ˣ³⁶⁵ 1000  = $1349.83.
```

Finally, to keep their employees really moving, banks offer *continuous compounding*. The interest is added on at every instant, and the difference equation breaks down. You can hope that the treasurer does not know calculus (which is all about limits as Δt → 0). The bank could compound the interest N times a year, so Δt = 1/N:

```
Continuously   (1 + .06/N)⁵ˣᴺ 1000  → e·³⁰ 1000 = $1349.87.
```

Or the bank can switch to a differential equation - the limit of the difference equation P<sub>k</sub>₊₁ = (1 + .06 Δt)P<sub>k</sub>  . Moving P<sub>k</sub> to the left side and dividing by Δt,


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Discrete_continuous.png)


*The solution is p(t) = e·⁰⁶ᵗ p₀*.   After t = 5 years, this again amounts to $1349.87. The principal stays finite, even when it is compounded every instant and the improvement over compounding every day is only four cents.


<h2 id="fdd5b4c8c15384ed3cceda4fe4cc38d6"></h2>
### Fibonacci Numbers

The main object of this section is to solve u<sub>k</sub>₊₁ = Au<sub>k</sub>. That leads us to Aᵏ and **powers of matrices**. Our second example is the famous ***Fibonacci sequence***:

```
Fibonacci numbers:  0, 1, 1, 2, 3, 5, 8, 13, ... 
```

**Fibonacci equation**: F<sub>k</sub>₊₂ = F<sub>k</sub>₊₁ + F<sub>k</sub>.   (2)

That is the difference equation. It turns up in a most fantastic variety of applications, and deserves a book of its own. Leaves grow in a spiral pattern, and on the apple or oak you find five growths for every two turns around the stem. The pear tree has eight for every three turns, and the willow is 13:5. The champion seems to be a sunflower whose seeds chose an almost unbelievable ratio of F₁₂/F₁₃ = 144/233.

How could we find the 1000th Fibonacci number, without starting at F₀ = 0 and F₁ = 1, and working all the way out to F₁₀₀₀? The goal is to solve the difference equation F<sub>k</sub>₊₂ = F<sub>k</sub>₊₁ + F<sub>k</sub>. **This can be reduced to a one-step equation u<sub>k</sub>₊₁ = Au<sub>k</sub>. Every step multiplies u<sub>k</sub> = (F<sub>k</sub>₊₁ , F<sub>k</sub>) by a matrix A**:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Fibonacci_equation.png)

The one-step system u<sub>k</sub>₊₁ = Au<sub>k</sub> is easy to solve. It starts from u₀. After one step it produces u₁ = Au₀. Then u₂ is Au₁, which is A²u₀. *Every step brings a multiplication by A*, and after k steps there are k multiplications:

***The solution to a difference equation u<sub>k</sub>₊₁ = Au<sub>k</sub> is u<sub>k</sub> = Aᵏu₀.***

The real problem is to find some quick way to compute the powers Aᵏ, and thereby find the 1000th Fibonacci number. The key lies in the eigenvalues and eigenvectors:

**5G** If A can be diagonalized, A = SΛS⁻¹, then Aᵏ comes from Λᵏ:

&nbsp;&nbsp;&nbsp;&nbsp; u<sub>k</sub> = Aᵏu₀ = (SΛS⁻¹)(SΛS⁻¹)...(SΛS⁻¹)u₀ = SΛᵏS⁻¹u₀.		&nbsp;&nbsp;&nbsp;&nbsp;(4)


The columns of S are the eigenvectors of A. Writing S⁻¹u₀ = c, the solution becomes:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_5g.png)

After k steps, u<sub>k</sub> is a combination of the n "pure solutions" λᵏx.

These formulas give two different approaches to the same solution u<sub>k</sub> = SΛᵏS⁻¹u₀. The first formula recognized that Aᵏ is identical with SΛᵏS⁻¹, and we could stop there.
But the second approach brings out the analogy with a differential equation: ***The pure exponential solutions e<sup>λit</sup>xᵢ are now the pure powers λᵢᵏxᵢ***. ? The eigenvectors xᵢ are amplified by the eigenvalues λᵢ. By combining these special solutions to match u₀ - that is where *c* came from - we recover the correct solution u<sub>k</sub> = SΛᵏS⁻¹u₀.

In any specific example like Fibonacci's, the first step is to find the eigenvalues:

```
A - λI = ⎡1-λ   1 ⎤  has det(A - λI) = λ² - λ - 1
		 ⎣ 1   -λ ⎦

Two eigenvalues: λ₁ = ( 1 + √5 ) / 2 m
				 λ₂ = ( 1 + √5 ) / 2 .
```

The second row of A - λI is (1, -λ). To get (A - λI )x = O, the eigen vector is x = (λ, 1). The first Fibonacci numbers F₀ = 0 and F₁ = 1 go into u₀, and S⁻¹u₀ = c:

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Fib1.png)

Those are the constants in u<sub>k</sub> = c₁λ₁ᵏx₁ + c₂λ₂ᵏx₂. Both eigenvectors x₁ and x₂ have second component 1. That leaves F<sub>k</sub> = c₁λ₁ᵏ + c₂λ₂ᵏ  in the second component of u<sub>k</sub>:

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Fib2.png)

This is the answer we wanted.

The fractions and square roots look surprising because Fibonacci's rule F<sub>k</sub>₊₂ = F<sub>k</sub>₊₁ + F<sub>k</sub> must produce whole numbers. Somehow that formula for F<sub>k</sub> must give an integer. In fact, since the second term [ ( 1-√5 ) /2 ] / √5  is always less than 2, it must just move the first term to the nearest integer:

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Fib3.png)

This is an enormous number, and F₁₀₀₁ will be even bigger. The fractions are becoming insignificant, and the ratio F₁₀₀₁ /F₁₀₀₀ must be very close to (1 + √5 )/2 ≈ 1.618. Since λ₂ᵏ is insignificant compared to λ₁ᵏ, the ratio F<sub>k</sub>₊₁ / F<sub>k</sub> approaches λ₁.

That is a typical difference equation, leading to the powers of 

```
A = ⎡1 1⎤ .
    ⎣1 0⎦
```

It involved √5 because the eigenvalues did. If we choose a matrix with λ₁ = 1 and λ₂ = 6, we can focus on the simplicity of the computation -- after A has been diagonalized:

```
A = ⎡-4 -5⎤  has λ 1 and 6,  with x₁ = ⎡ 1⎤, and x₂ = ⎡-1⎤.
    ⎣10 11⎦                            ⎣-1⎦           ⎣ 2⎦
```

```
Aᵏ = SΛᵏS⁻¹ is ⎡ 1 -1⎤⎡1ᵏ 0 ⎤⎡2 1⎤ = ⎡  2-6ᵏ    1-6ᵏ ⎤.
               ⎣-1  2⎦⎣0  6ᵏ⎦⎣1 1⎦   ⎣-2+2·6ᵏ -1+2·6ᵏ⎦
```

The powers 6ᵏ and 1ᵏ appear in that last matrix Aᵏ, mixed in by the eigenvectors.

For the difference equation u<sub>k</sub>₊₁ = Au<sub>k</sub>, we emphasize the main point. Every eigenvector x produces a "pure solution" with powers of λ:

```
One solution is   u₀ = x, u₁ = λx, u₂ = λ²x, ...
```

When the initial u₀ is an eigenvector x, this is the solution: u<sub>k</sub> = λᵏx. In general u₀ is not an eigenvector. But if u₀ is a combination of eigenvectors, the solution u<sub>k</sub> is the same combination of these special solutions.

**5H** If u₀ = c₁x₁ + ... + cnxn, then after k steps u<sub>k</sub> = c₁ᵏx₁ + ... + cnᵏxn. Choose the c's to match the starting vector u₀ :

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Fib6.png)



<h2 id="bdfe38b6c05d238d6cb0df431aea8cb7"></h2>
### Markov Matrices

*Each year 1/10 of the people outside California move in, and 2/10 of the people inside California move out*. We start with y₀ people outside and z₀ inside.

At the end of the first year the numbers outside and inside are y₁ and z₁:

```
Difference    y₁ = .9y₀ + .2z₀   or  ⎡y₁⎤ = ⎡.9 .2⎤⎡y₀⎤.
 equation     z₁ = .1y₀ + .8z₀       ⎣z₁⎦   ⎣.1 .8⎦⎣z₀⎦
```

This problem and its matrix have the two essential properties of a ***Markov process***:

 1. The total number of people stays fixed: ***Each column of the Markov matrix adds up to 1***. Nobody is gained or lost.
 2. The numbers outside and inside can never become negative: ***The matrix has no negative entries***. The powers Aᵏ are all nonnegative.*

We solve this Markov difference equation using **u<sub>k</sub> = SΛᵏS⁻¹u₀** . Then we show that the population approaches a "steady state." First A has to be diagonalized:

```
A - λI = ⎡.9-λ  .2  ⎤  has det(A - λI) = λ² - 1.7λ + .7
         ⎣ .1  .8-λ ⎦

λ₁ = 1 and λ₂ = .7:   A = SΛS⁻¹ = ⎡2/3  1/3⎤ ⎡1    ⎤ ⎡1   1⎤.
                                  ⎣1/3 -1/3⎦ ⎣   .7⎦ ⎣1  -2⎦
```

To find Aᵏ, and the distribution after k years, change SΛS⁻¹ to SΛᵏS⁻¹:

```
⎡yᵏ⎤ = Aᵏ⎡y₀⎤ = ⎡2/3  1/3⎤ ⎡1ᵏ    ⎤ ⎡1   1⎤ ⎡y₀⎤
⎣zᵏ⎦     ⎣z₀⎦   ⎣1/3 -1/3⎦ ⎣   .7ᵏ⎦ ⎣1  -2⎦ ⎣z₀⎦ 

     = (y₀ + z₀)⎡2/3⎤ + (y₀ - 2z₀)(.7)ᵏ⎡ 1/3⎤.
                ⎣1/3⎦                  ⎣-1/3⎦
```

Those two terms are c₁λ₁ᵏx₁ + c₂λ₂ᵏx₂.  In the long run, the other factor (.7)ᵏ becomes extremely small.  ***The solution approaches a limiting state*** u<sub>∞</sub> = (y<sub>∞</sub>, z<sub>∞</sub>):

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_Markov_Steady_status.png)

The total population is still y₀ + z₀, but in the limit 2/3 of this population is outside California and 1/3 inside.  This is true no matter what the initial distribution may have been !   If the year start with 2/3 outside and 1/3 inside , then it ends the same way : 

```
⎡.9  .2 ⎤ ⎡2/3⎤ = ⎡2/3⎤ .  or   Au∞ = u∞ .
⎣.1  .8 ⎦ ⎣1/3⎦   ⎣1/3⎦
```

***The steady state is the eigenvector of A corresponding to λ = 1. ***  Multiplication by A, from one time step to the next, leaves u<sub>∞</sub> unchanged.

The theory of Markov processes is illustrated by that California example:

**5I** A Markov matrix A has all aᵢⱼ ≥  0, with each column adding to 1.

 - (a) λ₁ = 1 is an eigenvalue of A.
 - (b) Its eigenvector x₁ is nonnegative -- and it is a steady state, since Ax₁ = x₁.
 - (c) The other eigenvalues satisfy λᵢ ≤ 1.
 - (d) If A or any power of A has all positive entries, these other |λᵢ| are below 1.  The solution Aᵏu₀ approaches a multiple of x₁ -- which is the steady state u<sub>∞</sub> .

To find the right multiple of x₁, use the fact that the total population stays the same. If California started with all 90 million people out, it ended with 60 million out and 30 million in. It ends the same way if all 90 million were originally inside.

We note that many authors transpose the matrix so its *rows* add to 1.

***Remark*** Our description of a Markov process was deterministic; populations moved in fixed proportions. But if we look at a single individual, the fractions that move become probabilities. With probability 1/10, an individual outside California moves in. If inside, the probability of moving out is 2/10. The movement becomes a *random process*, and A is called a ***transition matrix***.

The components of u<sub>k</sub> = Aᵏu₀ specify the probability that the individual is outside or inside the state. These probabilities are never negative, and add to 1 -- everybody has to be somewhere. That brings us back to the two fundamental properties of a Markov matrix:  Each column adds to 1, and no entry is negative.

Why is λ = 1 always an eigenvalue ?   Each column of *A - I* adds up to 1 - 1 = 0.  Therefore the rows of A - I add up to the zero row, they are linearly dependent, and det(A-I)=0.

Except for very special cases, u<sub>k</sub> will approach the corresponding eigenvector. (If everybody outside moves in and everybody inside moves out, then the populations are reversed every year and there is no steady state.)

In the formula u<sub>k</sub> = c₁λ₁ᵏx₁ + ... + cnλnᵏxn , no eigenvalue can be larger than 1. (Otherwise the probabilities u<sub>k</sub> would blow up.)  If all other eigenvalues are strictly smaller than λ₁ = 1, then the first term in the formula will be dominant.  The other λᵢᵏ go to zero, and
u<sub>k</sub> → c₁x₁ = u<sub>∞</sub> = steady state.

This is an example of one of the central themes of this chapter: Given information about A, find information about its eigenvalues. Here we found λ<sub>max</sub> = 1.

<h2 id="ececb2267f15a71d7ecad9272b25ab4a"></h2>
### Stability of u<sub>k+1</sub> = Au<sub>k</sub>

There is an obvious difference between Fibonacci numbers and Markov processes.  The numbers F<sub>k</sub> become larger and larger, while by definition any "probability" is between 0 and 1. The Fibonacci equation is *unstable*.  So is the compound interest equation P<sub>k+1</sub> = 1.06P<sub>k</sub>; the principal keeps growing forever.  If the Markov probabilities decreased to zero, that equation would be stable; but they do not, since at every stage they must add to 1. Therefore a Markov process is *neutrally stable*.

We want to study the behavior of u<sub>k+1</sub> = Au<sub>k</sub> as k → ∞. Assuming that A can be diagonalized, u<sub>k</sub> will be a combination of pure solutions:

&nbsp;&nbsp;&nbsp;&nbsp; **Solution at time k:**  u<sub>k</sub> = SΛᵏS⁻¹u₀ = c₁λ₁ᵏx₁ + ... + cnλnᵏxn .

The growth of u<sub>k</sub> is governed by the λᵢᵏ. ***Stability depends on the eigenvalues***:

**5J:** The difference equation u<sub>k+1</sub> = Au<sub>k</sub> is 

 - ***stable*** if all eigenvalues satisfy |λᵢ| < 1;
 - ***neutrally stable*** if some |λᵢ| = 1 and all the other |λᵢ| < 1; and
 - ***unstable*** if at least one eigenvalue has |λᵢ| > 1.

In the stable case, the powers Aᵏ approach zero and so does u<sub>k</sub> = Aᵏu₀.

Example 1 : This matrix A is certainly stable:

```
    A = ⎡0  4 ⎤  has eigenvalues  0 and 1/2.
        ⎣0 1/2⎦
```

<h2 id="ee24aae762a9409f153f67ec07bbee34"></h2>
### Positive Matrices and Applications in Economics

By developing the Markov ideas we can find a small gold mine (entirely optional) of matrix applications in economics.


**Example 2: Leontief's input-output matrix**

This is one of the first great successes of mathematical economics. To illustrate it, we construct a *consumption matrix* -- in which aᵢⱼ gives the amount of product *j* that is needed to create one unit of product *i* :

```
    ⎡.4  0 .1⎤     (steel)
A = ⎢ 0 .1 .8⎥.    (food)
    ⎣.5 .7 .1⎦     (labor)
```

The first question is: Can we produce y₁ units of steel, y₂ units of food, and y₃ units of labor? We must start with larger amounts p₁, p₂, p₃, because some part is consumed by the production itself. The amount consumed is Ap, and it leaves a net production of p - Ap.

```
  Problem:  To find a vector p such that p - Ap = y, or p = (I - A)⁻¹y.
```

On the surface, we are only asking if I - A is invertible. But there is a nonnegative twist to the problem.  Demand and production, y and p, are nonnegative. Since p is (I - A)⁻¹y , the real question is about the matrix that multiplies y:

***&nbsp;&nbsp;&nbsp;&nbsp;  When is (I - A)⁻¹ a nonnegative matrix?***

Roughly speaking, A cannot be too large. If production consumes too much, nothing is left as output. The key is in the largest eigenvalue λ₁ of A, which must be below 1: 

 - If λ₁ > 1, (I - A)⁻¹ fails to be nonnegative.
 - If λ₁ = 1, (I - A)⁻¹ fails to exist.
 - If λ₁ < 1, (I - A)⁻¹ is a converging sum of nonnegative matrices:
 	- **Geometric series:**   (I - A)⁻¹ = I + A + A² + A³ + ...  (7)

The 3 by 3 example has λ₁ = .9, and output exceeds input. Production can go on.

Those are easy to prove, once we know the main fact about a nonnegative matrix like A: ***Not only is the largest eigenvalue λ₁ positive, but so is the eigenvector x₁.***  Then (I - A)⁻¹ has the same eigenvector (why?), with eigenvalue 1/(1 - λ₁).  

If λ₁ exceeds 1, that last number is negative. The matrix (I - A)⁻¹ will take the positive vector x₁ to a negative vector x₁/(1 - λ₁). In that case (I - A)⁻¹ is definitely not nonnegative. If λ₁ = 1, then I - A is singular. The productive case is λ₁ < 1, when the powers of A go to zero (stability) and the infinite series I + A + A² + ...  converges.  Multiplying this series by *I - A* leaves the identity matrix -- all higher powers cancel -- so (I - A)⁻¹ is a sum of nonnegative matrices. We give two examples:

```
A = ⎡0  2⎤ has λ₁=2  and the economy is lost 
    ⎣2  0⎦

A = ⎡.5 2⎤ has λ₁=0.5  and we can produce anything.
    ⎣0 .5⎦
```

The matrices (I - A)⁻¹ in those two cases are 

```
-1/3 ⎡1  2⎤  and  ⎡2  8⎤. 
     ⎣2  1⎦       ⎣0  2⎦
```

Leontief's inspiration was to find a model that uses genuine data from the real economy. The table for 1958 contained 83 industries in the United States, with a "transactions table" of consumption and production for each one. The theory also reaches beyond (I - A)⁻¹, to decide natural prices and questions of optimization. Normally labor is in limited supply and ought to be minimized. And, of course, the economy is not always linear.

**Example 3: The prices in a closed input-output model**

The model is called "closed" when everything produced is also consumed.  Nothing goes outside the system. In that case A goes back to a *Markov matrix*. ***The columns add up to 1***.  We might be talking about the *value* of steel and food and labor, instead of the number of units. The vector p represents prices instead of production levels. 

Suppose p₀ is a vector of prices. Then Ap₀ multiplies prices by amounts to give the value of each product. That is a new set of prices which the system uses for the next set of values A²p₀. The question is whether the prices approach equilibrium (均衡). Are there prices such that p = Ap, and does the system take us there ?

You recognize p as the (nonnegative) eigenvector of the Markov matrix A, with λ = 1. It is the steady state p<sub>∞</sub>, and it is approached from any starting point p₀. By repeating a transaction over and over, the price tends to equilibrium.

The "Perron-Frobenius theorem" gives the key properties of a ***positive matrix*** -- not to be confused with a *positive definite* matrix, which is symmetric and has all its eigenvalues positive. Here all the entries aᵢⱼ are positive.

**5K:** If A is a positive matrix, so is its largest eigenvalue: λ₁ > all other |λᵢ| . Every component of the corresponding eigenvector x₁ is also positive.

***Proof: *** 

Suppose A > 0. The key idea is to look at all numbers *t* such that Ax ≥ tx for some nonnegative vector x (other than x = 0). We are allowing inequality in Ax ≥ tx in order to have many positive candidates t. For the largest value t<sub>max</sub> (which is attained), we will show that ***equality holds***: Ax = t<sub>max</sub>x.

Otherwise, if Ax ≥ t<sub>max</sub>x is not an equality, multiply by A. Because A is positive, that produces a strict inequality A²x > t<sub>max</sub>Ax. Therefore the positive vector y = Ax satisfies Ay > t<sub>max</sub>y, and t<sub>max</sub> could have been larger. This contradiction forces the equality Ax = t<sub>max</sub>x, and we have an eigenvalue. Its eigenvector x is positive (not just nonnegative) because on the left-hand side of that equality Ax is sure to be positive.

To see that no eigenvalue can be larger than t<sub>max</sub>, suppose Az = λz. Since λ and z may involve negative or complex numbers, we take absolute values:|λ||z|= |Az| ≤ A|z| by the "triangle inequality." This |z| is a nonnegative vector, so |λ| is one of the possible candidates *t*. Therefore |λ| cannot exceed λ₁, which was t<sub>max</sub>.

***Example4: Von Neumann'c model of an expanding economy***

We go back to the 3 by 3 matrix A that gave the consumption of steel, food, and labor. If the outputs are s₁, f₁, l₁, then the required inputs are

```
     ⎡.4  0 .1⎤ ⎡s₁⎤
u₀ = ⎢ 0 .1 .8⎥ ⎢f₁⎥ = Au₁
     ⎣.5 .7 .1⎦ ⎣l₁⎦
```

In economics the difference equation is backward! Instead of u₁ = Au₀ we have u₀ = Au₁.  If A is small (as it is), then production does not consume everything -- and the economy can grow. The eigenvalues of A⁻¹ will govern this growth.  But again there is a nonnegative twist, since steel, food, and labor cannot come in negative amounts. Von Neumann asked for the maximum rate *t* at which the economy can expand and still stay nonnegative, meaning that u₁ ≥ tu₀ ≥ 0.

Thus the problem requires u₁ > tAu₁. It is like the Perron-Frobenius theorem, with A on the other side. As before, equality holds when t reaches t<sub>max</sub> -- which is the eigenvalue associated with the positive eigenvector of A⁻¹. In this example the expansion factor is s :

```
     ⎡.4  0 .1⎤ ⎡1⎤   ⎡0.9⎤
Ax = ⎢ 0 .1 .8⎥ ⎢5⎥ = ⎢4.5⎥ = (9/10)x .
     ⎣.5 .7 .1⎦ ⎣5⎦   ⎣4.5⎦
```
With steel-food-labor in the ratio 1-5-5, the economy grows as quickly as possible:  ***The maximum growth rate is 1/λ₁***.

--- 

<h2 id="6949286af35bec96be99401b85d929c5"></h2>
## 5.4 DIFFERENTIAL EQUATIONS AND eᴬᵗ  (TODO)

--- 

<h2 id="8790e803d7a4cc615fb758ad25c12f30"></h2>
## 5.5 COMPLEX MATRICES

--- 

<h2 id="752452230e3a6aebda46452d7a021688"></h2>
## 5.6 SIMILARITY TRANSFORMATIONS

Virtually every step in this chapter has involved the combination S⁻¹AS.  The eigenvectors of A went into the columns of S , and that made S⁻¹AS a diagonal matrix (called Λ).

When A was symmetric (对称矩阵A的不同特征值所对应的特征向量是正交的), we wrote Q instead of S, choosing the eigenvectors to be orthonormal.

Now we look at all combinations M⁻¹AM -- *formed with any invertible M on the right and its inverse on the left*.  The invertible eigenvector matrix S may fail to exist (the defective case), or we may not know it, or we may not want to use it.

First a new word: ***The matrices A and M⁻¹AM are "similar."***   Going from one to the other is a ***similarity transformation***. It is the natural step for differential equations or matrix powers or eigenvalues -- just as elimination steps were natural for Ax = b. Elimination multiplied A on the left by L⁻¹, but not on the right by L. So U is not similar to A, and the pivots are not the eigenvalues.   So U is not similar to A, and the pivots are not the eigenvalues.

A whole family of matrices M⁻¹AM is similar to A, and there are two questions:

 1. What do these similar matrices M⁻¹AM have in common?
 2. With a special choice of M, what special form can be achieved by M⁻¹AM ?

The final answer is given by the ***Jordan form***, with which the chapter ends.

These combinations M⁻¹AM arise in a differential or difference equation, when a "change of variables" u = Mv introduces the new unknown v:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_MAM_diff.png)

The new matrix in the equation is M⁻¹AM. In the special case M = S, the system is uncoupled because Λ = S⁻¹AS is diagonal. The eigenvectors evolve independently. This is the maximum simplification, but other M's are also useful. We try to make M⁻¹AM easier to work with than A .

The family of matrices M⁻¹AM includes A itself, by choosing M = I. Any of these similar matrices can appear in the differential and difference equations, by the change u = Mv, so they ought to have something in common, and they do: ***Similar matrices share the same eigenvalues***.

**5P** Suppose that B = M⁻¹AM. Then A and B have the **same eigenvalues. Every eigenvector x of A corresponds to an eigenvector M⁻¹x of B**.

Start from Ax = λx and substitute A = MBM⁻¹:

```
  Same eigenvalue:  MBM⁻¹x = λx   which is B(M⁻¹x) = λ(M⁻¹x). 		(1)
```

The eigenvalue of B is still λ. The eigenvector has changed from x to M⁻¹x.

We can also check that A - λI and B - λI have the same determinant:

```
Product of matrices      B - λI =  M⁻¹AM - λI = M⁻¹(A - λI)M
Product rule        det(B - λI) = detM⁻¹ det(A - λI) detM = det(A - λI). 
```

The polynomials det(A - λI) and det(B - λI) are equal. Their roots -- the eigenvalues of A and B -- are the same. Here are matrices B similar to A.

Example 1:

```
A = ⎡1 0⎤ has eigenvalues 1 and 0. Each B is M⁻¹AM:
    ⎣0 0⎦


  if M = ⎡1 b⎤ , then B = ⎡1 b⎤ : triangular with λ = 1 and 0.
         ⎣0 1⎦            ⎣0 0⎦
  if M = ⎡ 1 1⎤ , then B = ⎡1/2 1/2⎤ : projection with λ = 1 and 0.
         ⎣-1 1⎦            ⎣1/2 1/2⎦
  if M = ⎡a b⎤ , then B = an arbitrary matrix with λ = 1 and 0.
         ⎣c d⎦            
```

In this case we can produce any B that has the correct eigenvalues. It is an easy case, because the eigenvalues 1 and 0 are distinct. The diagonal A was actually Λ, the outstanding member of this family of similar matrices (the capo). The Jordan form will worry about repeated eigenvalues and a possible shortage of eigenvectors. All we say now is that every M⁻¹AM has the same number of independent eigenvectors as A (each eigenvector is multiplied by M⁻¹).

The first step is to look at the linear transformations that lie behind the matrices.  Rotations, reflections, and projections act on n-dimensional space. The transformation can happen without linear algebra, but linear algebra turns it into matrix multiplication.

---

<h2 id="5f520f3a47da08c25d74016f54696110"></h2>
### Change of Basis = Similarity Transformation

The similar matrix B = M⁻¹AM is closely connected to A, if we go back to linear transformations. 

Remember the key idea: ***Every linear transformation is represented by a matrix***. The matrix depends on the choice of basis! If we change the basis by M we change the matrix A to a similar matrix B.

***Similar matrices represent the same transformation T with respect to different bases.***  The algebra is almost straightforward. Suppose we have a basis v₁, ... , vn. The jth column of A comes from applying T to vⱼ:

```
Tvⱼ = combination of the basis vectors = a₁ⱼv₁ + ... + anⱼvn.   (2)
```

For a new basis V₁, ... , Vn, the new matrix B is constructed in the same way: TVⱼ = combination of the basis vectors = b₁ⱼV₁ + ... + bnⱼVn .   But also each V must be a combination of the old basis vectors: Vⱼ = Σ mᵢⱼvᵢ . 

That matrix *M* is really representing the *identity transformation* (!) when the only thing happening is the change of basis (T is I). The inverse matrix M⁻¹ also represents the identity transformation, when the basis is changed from the v's back to the V's. 

Now the product rule gives the result we want:

**5Q** The matrices A and B that represent the same linear transformation T with respect to two different bases (the u's and the V's) are similar:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_similarity3.png)

I think an example is the best way to explain B = M⁻¹AM. Suppose T is projection onto the line L at angle θ. This linear transformation is completely described without the help of a basis. But to represent T by a matrix, we do need a basis.

Figure 5.5 offers two choices, the standard basis v₁ = (1, 0), v₂ = (0, 1) and a basis V₁, V₂ chosen especially for T.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F5.5.png)

In fact TV₁ = V₁ (since V₁ is already on the line L) and TV₂ = 0 (since V₂ is perpendicular to the line). In that eigenvector basis, the matrix is diagonal:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F5.5_example_01.png)

The other thing is the change of basis matrix M. For that we express V₁ as a combination v₁ cosθ + v₂ sinθ and put those coefficients into column 1. Similarly V₂ (or I V₂, the transformation is the identity) is -v₁ sinθ + v₂ cosθ, producing column 2:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F5.5_example_02.png)

The inverse matrix M⁻¹ (which is here the transpose) goes from v to V. Combined with B and M, it gives the projection matrix in the standard basis of v's:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_F5.5_example_03.png)

We can summarize the main point. The way to simplify that matrix A -- in fact to diagonalize it -- is to find its eigenvectors. 

They go into the columns of M (or S) and M⁻¹AM is diagonal. The algebraist says the same thing in the language of linear transformations: *Choose a basis consisting of eigenvectors*. The standard basis led to A, which was not simple. The right basis led to B, which was diagonal.

We emphasize again that M⁻¹AM does not arise in solving Ax = b. There the basic operation was to multiply A (on the left side only!) by a matrix that subtracts a multiple of one row from another. Such a transformation preserved the nullspace and row space of A; it normally changes the eigenvalues.

***Eigenvalues are actually calculated by a sequence of simple similarities.*** The matrix goes gradually toward a triangular form, and the eigenvalues gradually appear on the main diagonal. (Such a sequence is described in Chapter 7.) This is much better than trying to compute det(A- λI), whose roots should be the eigenvalues. For a large matrix, it is numerically impossible to concentrate all that information into the polynomial and then get it out again.

---

### Triangular Forms with a Unitary M

Our first move beyond the eigenvector matrix M = S is a little bit crazy: Instead of a more general M, we go the other way and restrict M to be unitary. M⁻¹AM can achieve a triangular form T under this restriction.  The columns of M = U are orthonormal (in the real case, we would write M = Q). Unless the eigenvectors of A are orthogonal, a diagonal U⁻¹AU is impossible. But "Schur's lemma" in **5R** is very useful -- at least to the theory. (The rest of this chapter is devoted more to theory than to applications. The Jordan form is independent of this triangular form.)

**5R** There is a unitary matrix M = U such that U⁻¹AU = T is triangular. The eigenvalues Of A appear along the diagonal of this similar matrix T.













