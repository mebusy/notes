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


<h2 id="19c0e5b53cd312dea89ed35c4445ca18"></h2>
### 消元矩阵

One Elimination Step:

```
      | 1  0  0|               |  b₁  |
E₃₁ = | 0  1  0|   has E₃₁·b = |  b₂  |
      |-l  0  1|               |b₃-lb₁|
```

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







