http://web.mit.edu/18.06

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


