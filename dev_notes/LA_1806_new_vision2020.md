
# Part 1: The Column Space of a Matrix


```
A =

   1   4   5
   3   2   5
   2   1   3
```

- A = CR
    - 
    ```
    C = 
       1   4
       3   2
       2   1
    ```
    - 
    ```
    R =
       1   0   1
       0   1   1
    ```
- **Key facts**
    - The r columns of C are a **basis** for the column space of A: **dimension** r
    - The r rows of R are a **basis** for the row space of A
- **Counting Theorem**
    - Ax = 0 has one solution x = [1,1,-1]
    - **There are n-r independent solutions to Ax=0.**

- A = CR  desirable
    - C has columns directly from A: meaningful
    - R turns out to be the **row reduced echelon form of A**
- A = CR undesirable
    - C and R could be very ill-conditioned
        - ill-conditioned means it is difficult to deal with
        - e.g. C and R are not great for avoiding round off or being good in large computations 
    - if A is invertible, then C = A, R = I


# Part 2: The Big Picture of Linear Algebra

- If Ax = 0 then x is orthogonal to every row of A
- 2 pairs of **orthogonal subspace**
    - **N(A)  ⟂ C(Aᵀ)**
    - **N(Aᵀ) ⟂  C(A)**
- **Big Picture**
    - ![](../imgs/LA_Figure_3.4.png)

- **Multiplying Columns time Rows / Six Factorizations**
    - ![](../imgs/LA_1806_2020_multiply.png)
    - LU : elimination


# Part 3: Orthogonal Vectors

- if Q is square,  Qᵀ = Q⁻¹
- if Q1,Q2 are square, Q1Q2 = Q2Q1
- Qx , it won't change the length of x
- Least Squares:  Major application of A = QR 
    - normal equation for the best x̂:  Aᵀe = 0  or AᵀAx̂ = Aᵀb
    - if A = QR, Rx̂ = Qᵀx
    - ![](../imgs/LA_F3.8.png)


# Part 4: Eigenvalues and Eigenvectors

- **S = Sᵀ  Real Eigenvalues and Orthogonal Eigenvectors**
- S = QAQᵀ




