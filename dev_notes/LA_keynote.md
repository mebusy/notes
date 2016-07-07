...menustart

 - [Preface](#5cf06822087ff10dec2ac74cf1e20d30)
 - [Elimination](#37ce2a99728857da54756961009fe633)
   - [Row Picture , Column Picture](#e3b14c3d3017ac3bb230a442e7e757ef)
   - [消元矩阵](#19c0e5b53cd312dea89ed35c4445ca18)
   - [矩阵乘法](#12127f40ff36ed84744a1af8c6e336be)
   - [LU 分解](#9ef9abc9eda686571cb1d8e4e47c3d10)
   - [置换矩阵](#2f79a6b54ab5e88029090d5fe24a83bf)
   - [INVERSES AND TRANSPOSE](#3a9e344c1e6d675b13d40464c481227f)
   - [Symmetric Matrices](#b899f85c23e42aea33f7684a076389ca)
   - [partial pivoting](#4c6c909215a7371958d82af08be17233)
 - [Vector Spaces](#2f21953656c07a77cad97b71c89a69de)
   - [subspace](#50d531aa756e5c11625170cc1c9cfbda)
   - [Column Space  C(A)](#684f816b438089969d265be5216aa435)
   - [Nullspace N(A)](#23705503ad60700b867022f40a8543dc)
   - [SOLVING Ax=0 and Ax=b](#9405663c8d12328a80ae3457c45d5995)
     - [Echelon Form(梯形) U ,  and Row Reduced Form R](#bee5654627ea92bad93731a29fd8d7bc)
   - [Basis for Vector Space](#7d21299ec6409c5d95f4c4c2dde8468c)
   - [Dimension of a Vector Space](#277acc5b1627dc1a1e613976782c994b)
   - [4 FUNDAMENTAL SUBSPACES](#ab80affa0ab7ca1586b19dd67f41f505)

...menuend



<h2 id="5cf06822087ff10dec2ac74cf1e20d30"></h2>
## Preface

 - n vectors in m - dimensional space
 - 2 fundamental problems  
 	- Ax=b 
 	- Ax=λx 
 - **Elimination** is the  way to understand a matrix by producing a lot of zero entries
 - a key goal, to see whole spaces of vectors: the **row space** and the **column space** and the **nullspace**
 - When A multiplies x
 	- it produces the new vector Ax
 	- The whole space of vectors moves--it is "transformed" by A (eg. 2D vector -> 3D)


<h2 id="37ce2a99728857da54756961009fe633"></h2>
## Elimination

 - 消元法基本运算
 - 1. 交换两行
 - 2. 一行减去另一行的k倍
 - 对于方程组来说，这两种操作不会影响解

<h2 id="e3b14c3d3017ac3bb230a442e7e757ef"></h2>
### Row Picture , Column Picture

 - 矩阵的行 => 线性方程 => 几何平面
 	- 1个 n 元的方程, 产生一个 n-1 维的平面
 		- 2个(独立的) n元方程, 产生一个 n-2 维的平面
 		- n个(独立的) n元方程, 产生 0 维平面 - 点 
 	- eg. 2个二元一次方程 组成方程组
 		- 直线相交, 唯一解
 		- 直线平行, 无解
 		- 直线重合, 无数解
 - 矩阵的列 => 列空间
 	- combination of the column vectors 
 - The Breakdown of Elimination
 	- 只有 non-singular 的情况, 才能得到a full set of pivots (全部非0主元)，
 	- 但是即便non-singular，消元也可能breakdown, 
 		- 这种情况可以通过 row exchanges 来解决。
 		- 这也是为什么 matlab进行LU分解，返回值包含一个 转置矩阵。
 - rank = r means *r pivot rows* and *r pivot columns*



<h2 id="19c0e5b53cd312dea89ed35c4445ca18"></h2>
### 消元矩阵

One Elimination Step:

```
      | 1  0  0|               |  b₁  |
E₃₁ = | 0  1  0|   has E₃₁·b = |  b₂  |
      |-l  0  1|               |b₃-lb₁|
```

 - 表示一个变换，  第***1***行乘以-3, 加到第***3***行

<h2 id="12127f40ff36ed84744a1af8c6e336be"></h2>
### 矩阵乘法

 - 矩阵乘法
 	- **Every column of AB is a combination of the columns of A**
 	- associative
 		- **(AB)C = A(BC)**
 	- distributive
 		- **A(B+C) =AB+AC and (B+C)D=BD+CD**

<h2 id="9ef9abc9eda686571cb1d8e4e47c3d10"></h2>
### LU 分解

 - **Triangular factorization A = LU with no exchanges of rows**
 	- L is lower triangular, with 1 on the diagonal
 	- U is the upper triangular matrix which appears after forward elimination.
 	- The diagonal entries of U are the pivots.
 	- The triangular factorization can be written A = LDU
 		- where L and U have 1 on the diagonal and D is the diagonal matrix of pivots.
 - For any m by n matrix A there is a permutation P, a lower triangular L with unit diagonal, and an m by n echelon matrix U, such that PA = LU     

 - LU分解不借助 行交换的关键是是 中间不能出现 0 pivot
   - 但是对最后一个 pivot 没有 非0的要求
   - 因为奇异矩阵也有LU分解

<h2 id="2f79a6b54ab5e88029090d5fe24a83bf"></h2>
### 置换矩阵

 - Permutation Matrices

```
A =
   1   2
   3   4

P =
   0   1
   1   0

P*A = // row exchange
   3   4
   1   2

A*P = // column exchange
   2   1
   4   3
```

 - 置换矩阵有个奇特的性质: 
   - **置换矩阵的转置  = 置换矩阵的逆 **
   - **P⁻¹=Pᵀ**
   - 因为置换矩阵是 正交矩阵

<h2 id="3a9e344c1e6d675b13d40464c481227f"></h2>
### INVERSES AND TRANSPOSE

 - INVERSES 
 	- **A⁻¹A = I , AA⁻¹ = I**
 	- **(AB)⁻¹ = B⁻¹A⁻¹**
 	- **(ABC)⁻¹ = C⁻¹B⁻¹A⁻¹**
 - TRANSPOSE
 	- **(A+B)ᵀ = Aᵀ+Bᵀ**
	- **(AB)ᵀ = BᵀAᵀ**
	- **(A⁻¹)ᵀ = (Aᵀ)⁻¹** #转置的逆,等于 逆的转置

<h2 id="b899f85c23e42aea33f7684a076389ca"></h2>
### Symmetric Matrices

 - **Aᵀ = A**
 - **R x Rᵀ gives a symmetric matrix**
 	- `(RᵀR)ᵀ = Rᵀ(Rᵀ)ᵀ = RᵀR`
 	- Symmetric Products RᵀR, RRᵀ, and LDLᵀ
 		- LU misses the symmetry, but LDLᵀ captures it perfectly.
 		- 不是所有的对称矩阵都有LDLᵀ 分解

<h2 id="4c6c909215a7371958d82af08be17233"></h2>
### partial pivoting

 - Roundoff Error
 	- Even a well-conditioned matrix like B can be ruined by a poor algorithm.
 - Exchanging rows to obtain the largest possible pivot is called **partial pivoting**.
 	- fundamental algorithm of numerical linear algebra: elimination with **partial pivoting**.



<h2 id="2f21953656c07a77cad97b71c89a69de"></h2>
## Vector Spaces

<h2 id="50d531aa756e5c11625170cc1c9cfbda"></h2>
### subspace

 - a nonempty subset that satisfies **Linear combinations**
   - the zero vector will belong to every subspace

```
    |1 3|
A = |2 3| 构成的是一个过原点的 平面子空间
    |4 1|
```   

<h2 id="684f816b438089969d265be5216aa435"></h2>
### Column Space  C(A)

 - a subspace of **Rᵐ**
 - Ax=b , 如果b 在 C(A) 中, 则有解

<h2 id="23705503ad60700b867022f40a8543dc"></h2>
### Nullspace N(A)

 - a subspace of **Rⁿ**
 - The solutions to Ax = O ,  are from N(A)

<h2 id="9405663c8d12328a80ae3457c45d5995"></h2>
### SOLVING Ax=0 and Ax=b

 - 如果方程组 多余 未知数, 可能无解
 - 如果方程组 少于 未知数, 至少有一个特解
 - 矩阵中, 非独立的行/列, 对于解 Ax = 0 无影响

 - Any vector x_n in the nullspace can be added to a particular solution x. 
   - 因为 Ax_n = 0, 加上它并不影响 Ax = b
   - **Ax_p = b and Ax_n = 0 produce A(x_p + x_n) = b**.
   - x_p 可能有不同的选择，任选一个即可
      - 比如解集是一条直线，选择直线上任意一点即可
      - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_completeSolution.png)

 - Spanning involves the column space, and independence involves the nullspace.
   - To decide if b is a combination of the columns, we try to solve Ax = b.
   - To decide if the columns are independent, we solve Ax = 0.

<h2 id="bee5654627ea92bad93731a29fd8d7bc"></h2>
#### Echelon Form(梯形) U ,  and Row Reduced Form R
 - Echelon U
   - 消元法 即使主元不能避免的变0 也继续下去

 - R
   - divide by pivot on each row, to make pivot "1"
   - the simplest matrix that elimination can give
   - MATLAB command R = **rref (A)**.
   - From R we will quickly find the nullspace of A.
   - Rx = 0 has the same solutions as Ux = 0 and Ax=0


<h2 id="7d21299ec6409c5d95f4c4c2dde8468c"></h2>
### Basis for Vector Space

 - 不同基组合可以得到相同的结果，但是只要确定了基，某一结果的组合就是唯一的
 - The columns of any matrix span its column space.
 - If they are independent, they are a basis for the column space
   - whether the matrix is square or rectangular.
 - If we are asking the columns to be a basis for the whole space Rⁿ, then the matrix must be square and invertible.


<h2 id="277acc5b1627dc1a1e613976782c994b"></h2>
### Dimension of a Vector Space
 
 - 矩阵不同的字空间拥有不同的维度
 - dimension of the column space = Rank

You must notice that the word "dimensional" is used in two different ways.

 - We speak about a four-dimensional vector, meaning a vector in R⁴.
 - Now we have defined a 4D subspace;
   - an example is the set of vectors in R⁶ whose first and last components are zero.
   - The members of this 4D subspace are 6D vectors like (0, 5, 1, 3, 4, 0).
 - We never use the terms "basis of a matrix" or "rank of a space" or "dimension of a basis." 
   - These phrases have no meaning. 
 - It is the **dimension of the column space** that equals the **rank of the matrix**, as we prove in the coming section.


<h2 id="ab80affa0ab7ca1586b19dd67f41f505"></h2>
### 4 FUNDAMENTAL SUBSPACES

4 subspaces in full rank:

 - C(A) , rank = r
 - N(A) , dimension = n-r
 - C(Aᵀ), **row space** ,  dimension = r
 - N(Aᵀ) , **left nullspace** , 

If A is an m by n matrix:

 - The nullspace N(A) and row space C(Aᵀ) are subspaces of **Rⁿ**.
 - The left nullspace N(Aᵀ) and column space C(A) are subspaces of **Rᵐ**.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LA_4subspaces.png)




