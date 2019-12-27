...menustart

 - [7 Computations with Matrices](#a11f9fe43dfed0d30be3a8fbf4d57420)
     - [7.1 INTRODUCTION](#f3fd8c325ad2bd72e12ccb6f8f17afc4)

...menuend


<h2 id="a11f9fe43dfed0d30be3a8fbf4d57420"></h2>


# 7 Computations with Matrices

<h2 id="f3fd8c325ad2bd72e12ccb6f8f17afc4"></h2>


## 7.1 INTRODUCTION

 - 1. Techniques for Solving Ax = b.
    - Elimination is a perfect algorithm, except when the particular problem has special properties-as almost every problem has. 
    - Section 7.4 will concentrate on the property of *sparseness*, when most of the entries in A are zero. 
    - We develop ***iterative rather than direct methods*** for solving Ax = b. 
        - An iterative method is "self-correcting," and never reaches the exact answer. 
        - The object is to get close more quickly than elimination. 
        - In some problems, that can be done; in many others, elimination is safer and faster if it takes advantage of the zeros.  
    - The competition is far from over, and we will identify the *spectral radius* that controls the speed of convergence to x = A⁻¹b.
 - 2. Techniques for Solving Ax = λx.
    - The eigenvalue problem is one of the outstanding successes of numerical analysis. 
    - We have chosen two or three ideas:
        - the QR algorithm
        - the family of "power methods,"
        - the preprocessing of a symmetric matrix to make it tridiagonal.
 - 3. The Condition Number of a Matrix.
    - Section 7.2 attempts to measure the "sensitivity" of a problem: If A and b are slightly changed, how great is the effect on x = A⁻¹b?
    - Before starting on that question, we need a way to measure A and the change ΔA. 
    - The length of a vector is already defined, and now we need the ***norm of a matrix***.
    - Then the ***condition number***, and the sensitivity of A will follow from multiplying the norms of A and A⁻¹. 
    
*The matrices in this chapter are square*. 

page360
