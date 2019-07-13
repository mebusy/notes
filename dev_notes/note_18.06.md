...menustart

 - [1](#c4ca4238a0b923820dcc509a6f75849b)
 - [2](#c81e728d9d4c2f636f067f89cc14862c)
 - [3](#eccbc87e4b5ce2fe28308fd9f2a7baf3)

...menuend


http://web.mit.edu/18.06

<h2 id="c4ca4238a0b923820dcc509a6f75849b"></h2>

## 1

 1. n linear equations, n unknowns
 2. Row picture  
    - line meet
 3. `*` Column picture
    - linear combination of columns
 4.  Maxtrix form
    - Ax = b

--- 
 - Q: how to compute Ax 
    1. each row dot product x 
    2. combination of columns

 - Q: can I solve Ax=b for every b?
    - That is , do the linear combination of columns fill the whole space (i.e. 3D).
    - It depends on columns of A.

 - solve Ax=b
    - ax=b, x=b/a=a⁻¹b
    - same idea: Ax=b => x=A⁻¹b


<h2 id="c81e728d9d4c2f636f067f89cc14862c"></h2>

## 2

 1. Elimination   
    - Success
    - Failure  0 in pivot position , row exchange
 2. Back-Substitution 
    - augmented matrix [Ab] ==elim=> [Uc] => Ux=c
 3. Elimination  Matrices
    - EA = U
    - 向量在 矩阵右侧，列组合；向量在矩阵左侧，行组合
    - Matrix x column => column
    - row x Marix => row 
    - subtract 3 x column1 from column2 is : (elementary matrix E₂₁)
 4. Matrix multiplication

----

 - E₂₁

```
⎡  1 0 0⎤
⎢ -3 1 0⎥
⎣  0 0 1⎦
```

 - permutation matrix: suppose to exchange row1 and row2

```
⎡ 0 1⎤
⎣ 1 0⎦
```

<h2 id="eccbc87e4b5ce2fe28308fd9f2a7baf3"></h2>

## 3

### Matrix multiplcation (4 ways) :  A * B = C

1. regular way
    - row·column, dot product
2. column way 
    -  columns in C , are combinations of columns of A 
    - that is , A * column of B ,  generates  a column in C 
3. row way
    - rows of C , are combinations of rows of B
    - that is , row of A * B , generates a row in C
4. 4th way
    - sum of (columns of A) * (rows of B) 
    - column * row , generates a big matrix 
    - `sum( Cn*Rn )` 
    
### Inverse of A , AB, Aᵀ
    
 - A is not invertible if you can find a non-zero vector that Ax = 0
    - Ax = 0 means some combination of columns gives 0, they contribute nothing. 
 - (AB)⁻¹ = B⁻¹A⁻¹
 - AA⁻¹ = I 
    - => (A⁻¹)ᵀAᵀ = I 
    - = (Aᵀ)⁻¹ = (A⁻¹)ᵀ

###  Gauss-Jordan / find A⁻¹

- how to find A⁻¹?
    - A * column j of A⁻¹ = column j of I 
    - 每次通过解一组方程组 就能得到 A⁻¹的一列
- Gauss-Jordan
    - slove n equations at once.
    - eliminate on long matrix [AI] , and get [IA⁻¹]
    - 为什么 经过消元法后(矩阵E)，就能得到A⁻¹嗯 ?
        - E*[AI] = [I?]
        - E*A = I => E = A⁻¹ => E*[AI] = [IA⁻¹]

 - note
    - 矩阵乘法规则， 适用于 单个数字元素， 也同样适用于 block 元素

## 4 (10)


### Product of elimination matrices 

 - E₃E₂E₁A = U 
 - U 的最后一个 pivot 可以不为0

### A=LU (no row exchange)

 - EA=U , A=LU , E⁻¹=L

### Permutations 

 - elimination may introduce row exchanges. 
 - permutation matrix performs row exchange. 
 - The inverse of permuation matrix P is P's transpose.
    - P⁻¹ = Pᵀ  =>  PᵀP = I

## 5

### Section 2.7 PA=LU

 - Transpose 
    - RᵀR is always symmetric
    - (RᵀR)ᵀ = RᵀRᵀᵀ = RᵀR

### Section 3.1 Vector Spaces and Subspaces

 - The begining of Linear Algebra

