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

*c step is no longer to subtract a multiple of one row from another*. Elimination changes the eigenvalues, which we don't want.

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














