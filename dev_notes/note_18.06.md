...menustart

 - [1](#c4ca4238a0b923820dcc509a6f75849b)
 - [2](#c81e728d9d4c2f636f067f89cc14862c)

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

## 3

 1. Matrix multiplcation (4 ways) :  A * B = C
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
        - sum( Cn*Rn ) 
 2. Inverse of A , AB, Aᵀ
    - 21:39
 3. Gauss-Jordan / find A⁻¹


 - note
    - 矩阵乘法规则， 适用于 单个数字元素， 也同样适用于 block 元素
