...menustart

- [Determinants](#44858f4401928ded6e165da37ea948a5)
    - [4.1 INTRODUCTION](#1cf6e82fd421ceda204af00707567518)
    - [4.2 PROPERTIES OF THE DETERMINANT](#14ed27a135e747655e17c482f074d582)
    - [4.3 FORMULAS FOR THE DETERMINANT](#f1652258e62063b8ce99a27a30fdb173)
        - [Expansion of detA in Cofactors](#bc04ae4273a1f4807770b5acb33f990b)
    - [4.4 APPLICATIONS OF DETERMINANTS](#2279c075e64bc81f35bb0751f9b2ea86)
        - [1. Computation of A⁻¹](#b105d89fa880f05d88cef65dec54a920)
        - [2. The Solution of Ax = b.](#ababd14c9c564481b2f47b6d96e29b0a)
        - [3. The Volume of a Box.](#fd7c0e5423c4bd8de8470b61d40e01e1)
        - [4. A Formula for the Pivots.](#6427117566de9225a3e174e57ee98198)

...menuend


<h2 id="44858f4401928ded6e165da37ea948a5"></h2>


# Determinants

<h2 id="1cf6e82fd421ceda204af00707567518"></h2>


## 4.1 INTRODUCTION

One viewpoint is this: The determinant provides an explicit "formula" for each entry of A⁻¹ and A⁻¹b. 

We can list four of the main uses of determinants:

 1. They test for invertibility. 
     - ***If the determinant of A is zero, then A is singular***. 
     - ***If det A ≠ 0, then A is invertible*** (and A⁻¹ involves 1/detA).
     - The most important application, and the reason this chapter is essential to the book, is to the family of matrices A - λI. The parameter λ is subtracted all along the main diagonal, and the problem is to find the eigenvalues for which A - λI is singular. The test is det(A - λI) = 0. This polynomial of degree n in X has exactly n roots. The matrix has n eigenvalues. This is a fact that follows from the determinant formula, and not from a computer.
 2. The determinant of A equals the ***volume*** of a box in n-dimensional space. 
     - The edges of the box come from the rows of A . The columns of A would give an entirely different box with the same volume.
     - ![](../imgs/LA_F4.1.png)
 3. The determinant gives a formula for each pivot. 
     - Theoretically, we could predict when a pivot entry will be zero, requiring a row exchange. 
     - From the formula ***determinant = ± (product of the pivots)***, it follows that *regardless of the order of elimination, the product of the pivots remains the same apart from sign*.
 4. The determinant measures the dependence of A⁻¹b on each element of b. 
     - If one parameter is changed in an experiment, or one observation is corrected, the "influence coefficient" in A⁻¹ is a ratio of determinants.

There is one more problem about the determinant. It is difficult not only to decide on its importance, and its proper place in the theory of linear algebra, but also to choose the best definition. Obviously, detA will not be some extremely simple function of n² variables; otherwise A⁻¹ would be much easier to find than it actually is.

***The simple things about the determinant are not the explicit formulas, but the properties it possesses***. This suggests the natural place to begin. The determinant can be (and will be) defined by its three most basic properties: 
- det I = 1, 
- **the sign is reversed by a row exchange**, 
- the determinant is linear in each row separately. 

The problem is then to show how the determinant can be computed , by systematically using these properties .  This will bring us back to the product of the pivots.

Here is a light-hearted question about permutations. ***How many exchanges does it take to change VISA into AVIS***? Is this permutation odd or even?

---

<h2 id="14ed27a135e747655e17c482f074d582"></h2>


## 4.2 PROPERTIES OF THE DETERMINANT

This will be a pretty long list. Fortunately each rule is easy to understand, and even easier to illustrate, for a 2 by 2 example. Therefore we shall verify that the familiar definition in the 2 by 2 case,

```
det ⎡a b⎤ = |a b| = ad - bc 
    ⎣c d⎦   |c d|
```

Notice the two accepted notations for the determinant, det A and |A|.

Properties 4-10 will be deduced from the previous ones. **Every property is a consequence of the first three**. 

We emphasize that the rules apply to *square matrices* of any size.

 1. **det I = 1**
     - The determinant of the identity matrix is 1.
 2. *The determinant changes sign when two rows are exchanged*.
 3. *The determinant depends linearly on one row*. 
     1. Add vectors in row

         ```
         |a+a' b+b'| =|a b| + |a' b'|
         |c    d   |  |c d|   |c  d |
         ```
     2. Multiply by *t* in row

         ```
        |ka kb| = k |a b|
        | c  d|     |c d|
        ```
         - det2A = 2ⁿ detA
 4. *If two rows of A are equal, then det A = 0.*
    - deduce from rule 2 ,  r = -r => r = 0 
 5. *Subtracting k x row i from row j , leaves the same determinant*.  
    - deduce from 3.1,3.2 : 消元不改变 determinant
    - 几何意义: 向量ab,cd, 向量ab不变，平行四边型的底不变; 向量cd 沿着 ab 方向发生切变，平行四边型的高不变，所以ab,cd 构成的面积不变。

 6. *If A has a row of zeros, then det A = 0*.
    - deduce from 3
    ```
    5|0 0| =|0 0| ,  5x =x -> x=0 
     |c d|  |c d|
    ```

 7. *If A is triangular, then det A is the product of the diagonal entries*. 
     - If the triangular A has 1s along the diagonal, then det A = 1.

     ```
     |a b|= ad, |a 0|= ad 
     |0 d|      |c d|
    ```
    - ***Proof:*** Suppose the diagonal entries are nonzero. Then elimination can remove all the off-diagonal entries (and keep the same pivot, 那些off-diagonal entries都是打酱油的), without changing the determinant (by rule 5)
    - *If a diagonal entry is 0 then elimination will produce a 0 row.* This is a key property: **All singular matrices have a zero determinant**.

 8. *If A is singular, then det A = 0. If A is invertible, then det A ≠ 0.*
     - If A is singular, elimination leads to a zero row in U. Then det A = det U = 0. 
     - If A is nonsingular, elimination puts the pivots d₁, ..., d𝑛, on the main diagonal. We have a "product of pivots" formula for det A! The sign depends on whether the number of row exchanges is even or odd:
         - **Product of pivots**:  detA = ± detU = ± d₁d₂ ... d𝑛 .  (also see 4A)

 9. *detAB = detA x detB*.
     - ![](../imgs/LA_Det_ProductRule.png)
     - This rule is the most surprising
     - A particular case of this rule gives the determinant of A⁻¹: `detA⁻¹ = 1 / detA`:
         - because (det A) (det A⁻¹) = det AA⁻¹ = det I = 1. 
     - **Proof:** 
         - If either A or B is singular , the AB is singular, detAB = detA x detB  = 0
         - otherwise, For a diagonal matrix, det DB = (det D) (det B), follows by factoring each dᵢ from its row. Reduce a general matrix A to D by elimination -- from A to U as usual, and from U to D by upward elimination (see rule 7). The determinant does not change, except for a sign reversal when rows are exchanged. The same steps reduce AB to DB, with precisely the same effect on the determinant. 

 10. *detAᵀ = detA*.
     - **Proof:** 
         - If A is singular, then detAᵀ = detA = 0 
         - otherwise, it allows the factorization ***PA = LDU*** , apply rule 9, we get 
             - `det P det A = det L det D det U.`
             - `det Aᵀ det Pᵀ = det Uᵀ det Dᵀ det Lᵀ.`
             - detL = detLᵀ = detU = detUᵀ = 1, detD = detDᵀ, detP = detPᵀ = ±1
         - We conclude that  det A = det Aᵀ.
     - 行列式，所有行的性质，对列同样有效

---

<h2 id="f1652258e62063b8ce99a27a30fdb173"></h2>


## 4.3 FORMULAS FOR THE DETERMINANT

The first formula has already appeared. Row operations produce the pivots in D:

**4A**: If A is invertible, then PA = LDU and det P = ±1. The product rule gives:

```
detA = ± detL detD detU = ±(Product of the pivots).  (1)
```

The sign ±1 depends on whether the number of row exchanges is even or odd. 

The triangular factors have detL = detU = 1 , and detD = d₁...d𝑛 .

In the 2 by 2 case, the standard LDU factorization is:

![](../imgs/LA_LDU_2x2.png)

The product of the pivots is ad - bc.

For n = 2, we will be proving that ad - bc is correct. For n = 3, the determinant formula is again pretty well known (it has six terms):

![](../imgs/LA_det_3x3.png)

Our goal is to derive these formulas directly from the defining properties 1-3 of det A. If we can handle n = 2 and n = 3 in an organized way, you will see the pattern.

To start, each row can be broken down into vectors in the coordinate directions:

```
[a b] = [a 0] + [0 b] and [c d] = [c 0] + [0 d].
```

Then we apply the property of linearity, first in row 1 and then in row 2:

![](../imgs/LA_det_2x2_factor.png)

Every row splits into n coordinate directions, so this expansion has nⁿ terms. 

Most of those terms (all but n! ) will be automatically zero. When two rows are inthe same coordinate direction, one will be a multiple of the other, and 

```
    |a 0|= 0,  |0 b|= 0 
    |c 0|      |0 d|
```

We pay attention *only when the rows point in different directions*. ***The nonzero terms have to come in different columns***. 

Suppose the first row has a nonzero term in column α, the second row is nonzero in column β , and finally the 𝑛th row in column v. The column numbers α, β, ... , v are all different. They are a reordering, or ***permutation***, of the numbers 1 , 2, ... , n. 

The 3 by 3 case produces 3! = 6 determinants:

![](../imgs/LA_det_3x3_6terms.png)

All but these n! determinants are zero, because a column is repeated.   In other words, ***there are n! ways to permute the numbers 1, 2, ... , n***. The column numbers give the permutations:

```
Column numbers (α, β, v) = (1, 2, 3), (2, 3, 1), (3, 1, 2), (1, 3, 2), (2, 1, 3), (3, 2, 1).
```

Those are the 3! = 6 permutations of (1, 2, 3); the first one is the identity.

The determinant of A is now reduced to six separate and much simpler determinants. Factoring out the aᵢⱼ, there is a term for every one of the six permutations:

![](../imgs/LA_det_3x3_6terms2.png)  (5)

![](../imgs/LA_det_bigFormula.png)   (6)

It remains to find the determinant of P. Row exchanges transform it to the identity matrix, and each exchange reverses the sign of the determinant:

- det P = +1 or - 1 , ***for an even or odd number of row exchanges***.

```
                    |1    |
(1,3,2) is odd so   |    1| = -1 ,
                    |  1  |  

                    |    1|
(3,1,2) is even so  |1    | = 1 .
                    |  1  |  
```

It is possible to see why it has properties 1-3. 

 1. For A = I, every product of the aᵢⱼ will be zero, except for the column sequence (1, 2, ... , n). This term gives det I = 1. 
 2. Property 2 will be checked in the next section, because here we are most interested in property 3: 
 3. The determinant should depend linearly on the first row a₁₁, a₁₂, ... , a₁<sub>𝑛</sub>.

Look at all the terms a₁ₐ, a₂ᵦ, ... ,  a<sub>𝑛</sub>ᵧ , involving a₁₁.  The first column is α = 1. This leaves some permutation (β, ... , γ) of the remaining columns (2, ... , n).  We collect all these terms together as a₁₁C₁₁  , where the coefficient of a₁₁ is a smaller determinant--with row 1 and column 1 removed:

![](../imgs/LA_det_cofactor.png)

Similarly, the entry a₁₂ is multiplied by some smaller determinant C₁₂. 

Grouping all the terms that start with the same a₁₁, formula (6) becomes

**Cofactors along row 1:** det A = a₁₁C₁₁ + a₁₂C₁₂ + ... + a₁<sub>𝑛</sub>C₁<sub>𝑛</sub>. (8)

This shows that detA depends linearly on the entries a₁₁, ... , a₁<sub>𝑛</sub> of the first row.

**Example 2** For a 3 by 3 matrix, this way of collecting terms gives

```
detA = a₁₁(a₂₂a₃₃ - a₂₃a₃₂) + a₁₂(a₂₃a₃₁ - a₂₁a₃₃) + a₁₃(a₂₁a₃₂ - a₂₂a₃₁) (9)
```

<h2 id="bc04ae4273a1f4807770b5acb33f990b"></h2>


#### Expansion of detA in Cofactors

We want one more formula for the determinant. If this meant starting again from scratch, it would be too much. But the formula is already discovered--it is (8), and the only point is to identify the cofactors C₁ⱼ that multiply a₁ⱼ.

We know that C₁ⱼ depends on rows 2, ... , n.  Row 1 is already accounted for by a₁ⱼ.  

What we are really doing is splitting the determinant into the following sum:

![](../imgs/LA_det_cofactor_filter.png)

For a determinant of order n, this splitting gives n smaller determinants ( ***minors***) of order n - 1;  The submatrix M₁ⱼ is formed by throwing away row 1 and column j.

There is a similar expansion on any other row, say row i :

**4B** The determinant of A is a combination of any row i times its cofactors:

&nbsp;&nbsp;&nbsp;&nbsp;**det A by cofactors:** det A = aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢ<sub>𝑛</sub>Cᵢ<sub>𝑛</sub>. (10)

The cofactor is the determinant of Mᵢⱼ , with the correct sign:

&nbsp;&nbsp;&nbsp;&nbsp;**delete row i and column j:** Cᵢⱼ = (-1)ⁱ⁺ʲ detMᵢⱼ.   (11)

---

<h2 id="2279c075e64bc81f35bb0751f9b2ea86"></h2>


## 4.4 APPLICATIONS OF DETERMINANTS

This section follows through on four major applications: 
    - *inverse of A*, 
    - *solving Ax = b*, 
    - *volumes of boxes*, 
    - and *pivots*. 


<h2 id="b105d89fa880f05d88cef65dec54a920"></h2>


#### 1. Computation of A⁻¹

The 2 by 2 case shows how cofactors go into A⁻¹:

![](../imgs/LA_det_apply_inverse.png)

We are dividing by the determinant, and A is invertible exactly when det A is nonzero.

That is the clue we need: **A⁻¹ divides the cofactors by det A**.

![](../imgs/LA_det_apply_inverse2.png)

**Cofactor matrix C is transposed !**.

Our goal is to verify this formu1 for A⁻¹. We have to see why ACᵀ = (detA) I:

![](../imgs/LA_det_apply_inverse3.png)  (2)

The critical question is: *Why do we get zeros off the diagonal*? If we combine the entries a₁ⱼ from row 1 with the cofactors C₂ⱼ for row 2, why is the result zero?

&nbsp;&nbsp;&nbsp;&nbsp; a₁₁C₂₁ + a₁₂C₂₂ + ... + a₁<sub>𝑛</sub>C₂<sub>𝑛</sub> = 0 . (3)

The answer is: We are computing the determinant of a new matrix B (indicate by C₂ⱼ), with a new row 2. The first row of A (a₁ⱼ) is copied into the second row of B . 

Then B has two equal rows, and det B = 0.

Dividing by the number detA (if it is not zero!) gives `A⁻¹ = Cᵀ / detA`.

**Example 1:**  The inverse of a sum matrix is a difference matrix:

![](../imgs/LA_det_inverse_of_sum_matrix.png)


<h2 id="ababd14c9c564481b2f47b6d96e29b0a"></h2>


#### 2. The Solution of Ax = b.


![](../imgs/la_1806_cramer_rule.gif)

**4C:** Cramer's rule: The jth component of x = A⁻¹b is the ratio

![](../imgs/LA_det_cramer_rule.png)

<h2 id="fd7c0e5423c4bd8de8470b61d40e01e1"></h2>


#### 3. The Volume of a Box.

The connection between the determinant and the volume is clearest when all angles are *right angles* -- the edges are perpendicular, and the box is rectangular. 

Then the volume is the product of the edge lengths: volume = *l₁l₂...l<sub>𝑛</sub>*.

We want to obtain the same *l₁l₂...l<sub>𝑛</sub>* from detA, *when the edges of that box are the rows of A*. With right angles, these rows are orthogonal and AAᵀ is diagonal (QQᵀ = I ):

![](../imgs/LA_det_right_angle_box.png)


&nbsp;&nbsp;&nbsp;&nbsp; Right-angle case:  *l₁²l₂²...l<sub>𝑛</sub>²* = det(AAᵀ) = (detA)(detAᵀ) = (detA)².

The square root of this equation says that ***the determinant equals the volume***.  The sign of detA will indicate whether the edges form a "right-handed" set of coordinates, as in the usual x-y-z system, or a left-handed system like y-x-z.

---

If the angles are not 90°, the volume is not the product of the lengths.

![](../imgs/LA_F4.2.png)

The "volume" of a parallelogram equals the base l times the height h. 

The key point is this: By rule 5, detA is unchanged when a multiple of row 1 is subtracted from row 2 (here is b-p).  *We can change the parallelogram to a rectangle*, where it is already proved that volume = determinant.

This completes the link between volumes and determinants, but it is worth coming back one more time to the simplest case. We know that

```
det ⎡1 0⎤ = 1 ,  det ⎡1 0⎤ = 1
    ⎣0 1⎦            ⎣c 1⎦
```

These determinants give the volumes-or areas, since we are in two dimensions-drawn in Figure 4.3. The parallelogram has unit base and unit height; its area is also 1.


<h2 id="6427117566de9225a3e174e57ee98198"></h2>


#### 4. A Formula for the Pivots.

We can finally discover when elimination is possible without row exchanges.

The key observation is that the first k pivots are completely determined by the submatrix A<sub>k</sub> in the upper left corner of A.

*The remaining rows and columns of A have no effect on this corner of the problem:*

![](../imgs/LA_det_matrix_corner.png)

Certainly the first pivot depended only on the first row and column. The second pivot (ad - bc)/a depends only on the 2 by 2 corner submatrix A₂. The rest of A does not enter until the third pivot. 

Actually it is not just the pivots, but the entire upper-left corners of L, D, and U, that are determined by the upper-left corner of A:

![](../imgs/LA_det_matrix_corner2.png)

What we see in the first two rows and columns is exactly the factorization of the corner submatrix A₂. This is a general rule if there are no row exchanges:

- **4D** If A is factored into LDU, the upper left corners satisfy A<sub>k</sub> = L<sub>k</sub>D<sub>k</sub>U<sub>k</sub> . For every k, the submatrix A<sub>k</sub> is going through a Gaussian elimination of its own.

The proof is to see that this corner can be settled first, before even looking at other eliminations. Or use the laws for ***block multiplication***:

![](../imgs/LA_det_block_multiple.png)

Comparing the last matrix with A, the corner L<sub>k</sub>D<sub>k</sub>U<sub>k</sub> coincides with A<sub>k</sub>. Then:

&nbsp;&nbsp;&nbsp;&nbsp; *detA<sub>k</sub> = detL<sub>k</sub>detD<sub>k</sub>detU<sub>k</sub> = detD<sub>k</sub> = d₁d₂...d<sub>k</sub>*.

*The product of the first k pivots is the determinant of A<sub>k</sub>*. 

We can isolate each pivot d<sub>k</sub> as ***a ratio of determinants***:

![](../imgs/LA_det_formular_for_pivots.png)

From equation (5) we can finally read off the answer to our original question:

***The pivot entries are all nonzero whenever the numbers det A<sub>k</sub> are all nonzero:***

- **4E** Elimination can be completed without row exchanges (so P = I and A= LU), if and only if the leading submatrice,, A₁, A₂, ... , A<sub>𝑛</sub>  are all nonsingular.


