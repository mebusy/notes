...menustart

 - [Four special matrices](#523995f0bde7f6f864950a61566a59a5)
	 - [Sparse](#7407fb7e6a4df6392aaabd2368157312)
	 - [Invertible](#6279ece7c95ba205cea508f2082ab1c8)
	 - [Periodic](#cdcc32a064503184053bd2018d1c0e7e)

...menuend


<h2 id="523995f0bde7f6f864950a61566a59a5"></h2>

# Four special matrices

K = ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/toeplitz_matrix.gif)

图示矩阵K 的4个特点:

 1. K=Kᵀ , symmetric.  Symmetric matrix is the most important class of matrices.
 2. Sparse.   **nnz**(K) to calculate the number of none-zero of a matrix.
 3. constant diagonal. Toeplitz is a diagonal-constant matrix: K=**toeplitz**( [-2 -1 0 0] ) . Caution: diagonal-constant matrix is not diagonal matrix. Toeplitz may symmetric or not. eg: K=toeplitz( [2 -1 0 0] , [1 3 0 0 ] )
 4. K is invertible. Invertible means K·K⁻¹=I ,  **eye**(n) can create an identity matrix.

<h2 id="7407fb7e6a4df6392aaabd2368157312"></h2>

### Sparse

If a matrix is sparse , Sparse MATLAB is the way to improve the performance of computation. To create a sparse matrix: KS = **parse**(K).

```
  (1, 1) ->  2
  (2, 1) -> -1
  (1, 2) -> -1
  (2, 2) ->  2
  (3, 2) -> -1
  (2, 3) -> -1
  (3, 3) ->  2
  (4, 3) -> -1
  (3, 4) -> -1
  (4, 4) ->  2
```

<h2 id="6279ece7c95ba205cea508f2082ab1c8"></h2>

### Invertible

How to know if a matrix is invertible? We will not use determinant here. I would do row reduce, that's the default option in linear algebra. Row reduce aiming for a triangular matrix. If a matrix is triangular then I can see immediately everything. 

Elimination can convert a matrix into an upper triangular matrix. And this is how MATLAB would find the determinant. It would do elimination, and the determinant of a triangular matrix is just product down the diagonal, the product of the pivots.

```
# MATLAB may very clever when dealing with fractions
> [L,U,P] = lu(K)
> U = 
   2.00000  -1.00000   0.00000   0.00000
   0.00000   1.50000  -1.00000   0.00000
   0.00000   0.00000   1.33333  -1.00000
   0.00000   0.00000   0.00000   1.25000

> det(U)
ans =  5
```

When is an upper triangular matrix invertible? K is invertible because the diagonal is non-zero. It's got full non-zero pivots.

<h2 id="cdcc32a064503184053bd2018d1c0e7e"></h2>

### Periodic

C = ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/toeplitz_matrix_not_invertible.gif)

C is also a toeplitz matrix. But it is not invertible. We even can see that without computing determinants. We can see it without doing elimination, too.

It is not invertible is because it's circulant. The diagonal which only has three *-1* circled around to the 4th. The diagonal which has two *0* circled around to other two *0*. The diagonal are not only constant, they loop around. This is a periodic matrix. Periodic matrix can always find a *non-zero vector u* so that Cu=0 (Here is vector [1;1;1;1]) . 

Cu=0 definitely means C is not invertible. 

If C is invertbile , then C⁻¹·Cu = C⁻¹·0 => u=0 , the only solution to Cu=0 is u=0. But that is not true here , so we conclude C is not invertible.

The physical meaning of K and C:

K is like 4 mass (块) connected to each other by strings , but the two endpoint string are fixed to wall. ||~o~o~o~o~||

C is like 4 mass connected to each other by strings and circled around. 

---

T = ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/toeplitz_matrix_free_fixed.gif)

T is free-fixed , with the top-left *2* changed to *1* . ( ~o~o~o~o~|| ) . T is invertible because it still has a support in physics meaning. 

B = ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/toeplitz_matrix_free_free.gif) 

B is free-free. ( ~o~o~o~o~ )  B is not invertible because Bu=0 while u = [1;1;1;1] .

Both T and B are not toeplitz any more.  

> TODO 下面没明白

So fixed means the displacement is zero. Something was set to zero.  Free means that the fifth guy is the same as the fourth. The slope is zero. 

Fixed "is u is zero". Free is "slope is zero".

K , T are *positive definite*.  C,B are *positive semi-definite*, they hit zero somehow.

If I have a symmetric matrix and the pivots are all positive , the matrix is positive definite.  Positive definite matrix connectes to pivots, connects to eigenvalues, connects to least squares, Determinant too. It's all over the place.

