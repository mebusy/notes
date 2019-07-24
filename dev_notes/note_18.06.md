...menustart

 - [1](#c4ca4238a0b923820dcc509a6f75849b)
 - [2](#c81e728d9d4c2f636f067f89cc14862c)
 - [3](#eccbc87e4b5ce2fe28308fd9f2a7baf3)
     - [Matrix multiplcation (4 ways) :  A * B = C](#99f80b726498ad866ed76cec68ca859e)
     - [Inverse of A , AB, Aᵀ](#785ba5483d4595815b81a1ab57fa7d38)
     - [Gauss-Jordan / find A⁻¹](#4e2c98c06f8cb4b5e5fda933f2d08ba2)
 - [4 (10)](#515dfcd954f57355545174f22e938c1f)
     - [Product of elimination matrices](#214181c5442239e64cc8d942b8b189e3)
     - [A=LU (no row exchange)](#f1248609fe6c8d2d55ee97b5d1a231d7)
     - [Permutations](#687883d0478f7377a01db0003294c174)
 - [5](#e4da3b7fbbce2345d7772b0674a318d5)
     - [Section 2.7 PA=LU](#0fa27231d37120418da2892cbb00e7cf)
     - [Section 3.1 Vector Spaces and Subspaces](#9d1fa1d7cb8b7fb75f4ac91338858795)

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
    - augmented matrix [A |b] ==elim=> [U |c] => Ux=c
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

<h2 id="99f80b726498ad866ed76cec68ca859e"></h2>

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
    
<h2 id="785ba5483d4595815b81a1ab57fa7d38"></h2>

### Inverse of A , AB, Aᵀ
    
 - A is not invertible if you can find a non-zero vector that Ax = 0
    - Ax = 0 means some combination of columns gives 0, they contribute nothing. 
 - (AB)⁻¹ = B⁻¹A⁻¹
 - AA⁻¹ = I 
    - => (A⁻¹)ᵀAᵀ = I 
    - = (Aᵀ)⁻¹ = (A⁻¹)ᵀ

<h2 id="4e2c98c06f8cb4b5e5fda933f2d08ba2"></h2>

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

<h2 id="515dfcd954f57355545174f22e938c1f"></h2>

## 4 (10)


<h2 id="214181c5442239e64cc8d942b8b189e3"></h2>

### Product of elimination matrices 

 - E₃E₂E₁A = U 
 - U 的最后一个 pivot 可以不为0

<h2 id="f1248609fe6c8d2d55ee97b5d1a231d7"></h2>

### A=LU (no row exchange)

 - EA=U , A=LU , E⁻¹=L

<h2 id="687883d0478f7377a01db0003294c174"></h2>

### Permutations 

 - elimination may introduce row exchanges. 
 - permutation matrix performs row exchange. 
 - The inverse of permuation matrix P is P's transpose.
    - P⁻¹ = Pᵀ  =>  PᵀP = I

<h2 id="e4da3b7fbbce2345d7772b0674a318d5"></h2>

## 5

<h2 id="0fa27231d37120418da2892cbb00e7cf"></h2>

### Section 2.7 PA=LU

 - Transpose 
    - RᵀR is always symmetric
    - (RᵀR)ᵀ = RᵀRᵀᵀ = RᵀR

<h2 id="9d1fa1d7cb8b7fb75f4ac91338858795"></h2>

### Section 3.1 Vector Spaces and Subspaces

 - The begining of Linear Algebra
 - All vector subspace have to go through the origin.
 - if S and T are both subspace, S∩T is a subspace.
    - why? 
    - Suppose I take a couple of vectors that are in the intersections, why is the sum also in the intersection? 
        - if V and W are 2 vectors in both S and T , then 
        - V+W is in S , and V+W is in T.   that is  , V+W is in both S and T as well. 
        - so that , V+W must in S∩T. 
    - 乘法的封闭性证明？ 等价若干加法所以不需要？
 - C(A)  column space


## 6 

### Column Space of A
 
 - column的长度j  决定了 A的column space 是 Rʲ 下的一个 subspace.
 - Does Ax=b has a solution for every b ? 
    - yes only if b is a combination of the colunmn, that is, b is a vector in the column space.

### Null Space of A 

 - Totally different space. it contains all solutions **x** to Ax = 0.
 - The dimension of N(A) is determined by number of columns. 
 - Why solutions to Ax=0 always give a subspace ?
    - That is , if Av=0 and Aw=0,  A(v+w) must be 0.
    - A(v+w) = Av + Aw = 0 
 - Q: Ax = b ,  is the solutions of x give a subspace ?
    - A: No. it doesn't go through the origin.


## 7

### Computing the nullspace (Ax=0)

The algorithm is elimination, but extended to the rectangular case (and won't carray b), where we have to continue even if there's zeros in the pivot position, we go on.

The result, let's call it U,  is a echelon matrix.

**Rank** of A = number of pivots

To solve Ax=0, really I'm solving Ux=0.

PS: The only operation not required by our example, but needed in general, is row exchange.

### Pivot variables -- free variables

when you get the echelon matrix, for free variables, you can assign any value, and then you just to compute the value of pivot variables,  so that you get a vector, a special solution for Ux=0.

if it have n free variables, you can find n vectors, n special solutions, those vectors span the null space.

That is , the null space contains exactly all the combinations of the special solutions. And how many special solutiosn there ? There's one for every free variable.  How many free variables ?  n-Rank !  (here, n means number of xᵢ in solution).



### Special Solutions -- rref(A) = R

Take a more step from U ,  making 0 above and below pivots, and making pivots = 1. (PS. zero above the pivot column , not needed for free column)

Then you get reduced row echelon form R.  Matlab will do it immediately with `rref(A)`. 

R got all the information as clear as can be.  

The solution to Rx=0  is as same as the solution to Ax=0 , or Ux=0.

PS. if A is invertible, then rref(A) = I.

```
octave:2> A
A =

    1    2    2    2
    2    4    6    8
    3    6    8   10

octave:3> rref(A)
ans =

   1.00000   2.00000   0.00000  -2.00000
   0.00000   0.00000   1.00000   2.00000
   0.00000   0.00000   0.00000   0.00000
```

But how can we get solution directly from the R form ?

From the pivot column, we get a identity matrix, form the free columns we get the free matrix.

```
octave:4> I = [1 0 ; 0 1]
I =

   1   0
   0   1

octave:5> F = [2 -2 ; 0 2 ]
F =

   2  -2
   0   2
```


The typical R form is

```
⎡ I F⎤
⎣ 0 0⎦
```

Now we gonna to create a 'nullspace matrix' N , which columns are the special solution, so that RN=0.

So what N will do the job ?

```
⎡ -F⎤
⎣  I⎦
```

That is ,

```
Rx = 0  

=>

[I F]·⎡ x_pivot⎤ = 0
      ⎣ x_free ⎦

=>

x_pivot = -F * free_variables

    P P     -2  2    -2  2
N = F F =>   F  F =>  1  0
    P P      0 -2     0 -2
    F F      F  F     0  1
```



---

```
R =

   1   0   1
   0   1   1
   0   0   0
   0   0   0
```

What's the x?  The x has a identify, it's only a single number 1, bt its the identify matix in free part. And what does it have in the pivot variables ?  [-1;-1]
 
x = c·[ -1;-1;1 ]
 

## 8

### Complete solution of Ax=b

To solve Ax=b,  we create an augmented matrix [A |b].

Solvability condition on b: b had to be in the column space C(A).

To find complete solution to Ax=b.

1. one particular solution 
    - set all free variables to 0, and then solve Ax=b for the pivot variables.
2. add on any x in the nullspace.

x = x<sub>p</sub> + x<sub>n</sub> , this pattern through all of mathematics, because it shows up everywhere.

x<sub>n</sub> is a subspace, but x<sub>complete</sub> is not.  x<sub>complete</sub> is like a subspace, but it's been shifted, away from the origin, it doesn't contain 0, since it must go through x<sub>p</sub> .

## 9

### Linear independence

indenpendent if N(A) = 0

### Spanning a space

The space consists of all combinations of those vectors.

### BASIS and dimension

BASIS for a space is a sequence of vectors with 2 properties.

1. they are independent
2. they span the space.

Dimension of a space is the  number of space basis.

Subspace also have basis.

rank(A) = #pivot columns = dimension of C(A) (PS. NOT the dimension of matrix) .

dim(C(A)) = r
dim(N(A)) = #free variables = n-r

A 和 Aᵀ 的 r 相等。


## 10

### Four Fundamental Subspace 

A is mxn

 - C(A) , ( in Rᵐ )                       ,dim=r
 - N(A) , dim=n-r
 - `---------`
 - Row Space C(Aᵀ) ,              ,dim=r
 - Left Null Space N(Cᵀ)  , ( in Rᵐ ),  dim=m-r

why we call N(Cᵀ) left null space ?

 - Aᵀy = 0  ==>  yᵀA = 0ᵀ 

About elimination:

Elimination preserve the row space. so R and A have different colum space, but same row space.

-----

```
A =

   1   2   3
   1   2   3
   2   5   8
```

it looks like the collmns are independent , does it ?

Actually, the rows are not inpendent ,so A is not invertible, so that the columns must be dependent. 

`A*[-1;2;-1 ] = 0` 

---

### New vector space !

All 3x3 matrices !!  we called M. 

Every 3x3 matrix is one of my "vectors". They are vectors in my vectors space because they obey the rules. 

Subspaces of M :

 - upper triangulars
 - symmetric matrices
 - diagonal matrices  D 

now D is a subspace. The dimension of D is 3. for example, you can shoose such 3 basis:

```
   1   0   0
   0   0   0
   0   0   0

   0   0   0
   0   3   0
   0   0   0

   0   0   0
   0   0   0
   0   0   7
```
  
## 11 













