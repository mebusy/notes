...menustart

 - [18.Determinants](#ae8178b3d3c78ee97adfcc298fe0b11e)
     - [Determinants , det A = |A|](#fc7bcc02eaa53ccf05c2b3f48461de47)
     - [Signed](#71fed0c3428bf1a2e19af257c4bac379)
     - [Properties](#9fc2d28c05ed9eb1d75ba4465abf15a9)
 - [19. Formular for Determinant](#077014dde3a16154d48a5807d1c351bb)
     - [Formula for detA ( n! terms )](#a4ea43d88bcd4db4f7d7fe3abe7052b4)
     - [Cofactor formula](#d02910574d79a0726db429910342d33e)
 - [20. APPLICATIONS OF DETERMINANTS](#d32bea3e6901eaca807e7ff0a03afc52)
     - [Formula for A⁻¹](#23d31b234b8839bc2675b16fff1de2da)
     - [Cramers Rule for x=A⁻¹b](#8d1f376d9179ba4326b17606a2f64136)
     - [| detA | = volume of box](#b99ff4a9543c3ccbfac05190cc07dd68)
 - [21. EigenValues - EigenVectors](#2a051e916e56ff2ad1a6b47745f85a6b)
     - [det\[A-λI\] = 0](#9e08a229f7feafd17be0f57fed7d544d)
     - [Trace = λ₁+λ₂+ ... + λ<sub>n</sub>](#95946abeb88b298e53a6c970166fb7aa)

...menuend


<h2 id="ae8178b3d3c78ee97adfcc298fe0b11e"></h2>

-----
-----

# 18.Determinants 

Up to now we paid a lot of attention to rectangular matrices. 

Now, concentrating on square matrices. Determinants and Eigen values are big, big chunk of 18.06.

<h2 id="fc7bcc02eaa53ccf05c2b3f48461de47"></h2>

-----

## Determinants , det A = |A| 

Every square matrix has a number associated with , called its determinant. 

- det A = 0 , means A is singular.  
- det A !=0 , means A is invertible.

<h2 id="71fed0c3428bf1a2e19af257c4bac379"></h2>

-----

## Signed

Determinant is signed.

<h2 id="9fc2d28c05ed9eb1d75ba4465abf15a9"></h2>

-----

## Properties 

3 base properties:

1. det I = 1.
2. Exchanging rows reverse sign of det.  
3. The determinant depends linearly on **one** row. (single row linearity)
    - 3a: Add vectors in a row
        - 
        ```
        |a+a' b+b'| =|a b| + |a' b'|
        |c    d   |  |c d|   |c  d |
        ```
    
    - 3b: Multiply by t in row
        - 
        ```
        |ka kb| = k |a b|
        | c  d|     |c d|
        ```
        - det2A = 2ⁿ detA
        - det(A+B) ≠ detA + detB

---

<details>
<summary>
p4 ~ p10
</summary>

 - p4: property 2 also said , dup rows => det=0 
 - p5: elimination ( - k rowi from rowj ) doesn't change det.
    - 数学上，减去的这部分 使用p3 可以分离出去，这部分的det 为0.
    - 集合上，平行四边形,底不变发生切变，面积不变
 - p6: zero row => det=0.
    - p3b, in case a=0,b=0 , K·det=det => det=0.
 - p7: triangular matrix, det = product of pivots
 - p8: If A is singular, then det A = 0. If A is invertible, then det A ≠ 0.
 - p9: det AB = detA * detB  (very valuable property)
    - detA⁻¹
 - p10: detAᵀ = detA 
    - 行列式，所有行的性质，对列同样有效

</details>



<h2 id="077014dde3a16154d48a5807d1c351bb"></h2>

-----
-----

# 19. Formular for Determinant

<h2 id="a4ea43d88bcd4db4f7d7fe3abe7052b4"></h2>

-----

## Formula for detA ( n! terms )

 - use property 3 to break down each row 
    - [a b c] = [a 0 0] + [0 b 0] + [0 0 c]
 - the determinant of A can be expanded into nⁿ terms 
 - a lot terms has 0 det,  they can be removed.
 - The nonzero terms have to come in different columns and rows. 
    - ![](../imgs/LA_det_3x3_6terms.png)
 - ![](../imgs/LA_det_bigFormula.png)
 
<h2 id="d02910574d79a0726db429910342d33e"></h2>

-----

## Cofactor formula

Cofactor is a way of breaking up above big formula that connects the nxn determinant to a determinant one smaller. 

![](../imgs/LA_det_cofactor_filter.png)

- **The determinant of A is a combination of any row i times its cofactors**.
    - **det A by cofactors:** det A = aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢ<sub>𝑛</sub>Cᵢ<sub>𝑛</sub>. (10)
    - The cofactor is the determinant of Mᵢⱼ , with the correct sign:
        - **delete row i and column j:** Cᵢⱼ = (-1)ⁱ⁺ʲ detMᵢⱼ.   (11)


<h2 id="d32bea3e6901eaca807e7ff0a03afc52"></h2>

-----
-----

# 20. APPLICATIONS OF DETERMINANTS

<h2 id="23d31b234b8839bc2675b16fff1de2da"></h2>

-----

## Formula for A⁻¹

![](../imgs/la_det_ap_inverse.gif)

<details>
<summary>
ACᵀ = (detA) I
</summary>

![](../imgs/LA_det_apply_inverse3.png)

The critical question is: Why do we get zeros off the diagonal? 

The answer is: we are actually computing the determinant of a new matrix which has equal rows. 

</details>

<h2 id="8d1f376d9179ba4326b17606a2f64136"></h2>

-----

## Cramers Rule for x=A⁻¹b

![](../imgs/la_1806_cramer_rule.gif)

What do I get in Cᵀb ? What's the first entry of Cᵀb ?  

Somehow I multiply cofactors by the entries of b, anytime I'm multiplying cofactors by numbers, I think, I'm getting the determinant of something. Let's call the matrix B , whose determinant comes out of Cᵀb .

So x₁ = detB₁/detA  , x₂ = detB₂/detA , ... 

**4C:** Cramer's rule: The jth component of x = A⁻¹b is the ratio

![](../imgs/LA_det_cramer_rule.png)

Actually, Cramer's Rule is a disastrous way to go, because compute these determinants takes like approximately forever.  

But having a formula allows you to do algebra instead of algorithms. They're nice formulas, but I just don't want you to use them. 


<h2 id="b99ff4a9543c3ccbfac05190cc07dd68"></h2>

-----

## | detA | = volume of box


```
    已知三角形的三个顶点：
    (x1,y1),(x2,y2),(x3,y3),求面积:
    解：
                |x1 y1 1|
    S= 1/2 det  |x2 y2 1|
                |x3 y3 1|
    
    
    如果有个顶点是原点,比如(x1,y1)=(0,0)
    
    S =  1/2 det|x2,y2|
                |x3,y3|
```

---

<h2 id="2a051e916e56ff2ad1a6b47745f85a6b"></h2>

-----
-----

# 21. EigenValues - EigenVectors 

There are certain vectors where Ax comes out parallel to x. And those are the eigenvectors.  **Ax=λx**.

If A is singular, λ=0 is an eigenvalue.

Now the question is how do we find these x-s and λ.

<details>
<summary>
Projection Matrix
</summary>

Any x in projection plane  Ax=x , λ=1

Any x ⟂ plane,  Ax=0 , λ=0.

</details>

<details>
<summary>
Permutation Matrix
</summary>

```
A =

   0   1
   1   0
```

x = [1;1] , λ=1

x = [-1;1] , λ=-1. In fact, the trace tells you right away what the other eigenvalue is.

</details>

How to solve Ax=λx ?

(A-Iλ)x = 0.    A-Iλ has to be singular.


<h2 id="9e08a229f7feafd17be0f57fed7d544d"></h2>

-----

## det[A-λI] = 0 

The idea will be to find λ first. I'll find n λ's.  A λ could be repeated, A repeated λ is source of all trouble in 18.06.

<h2 id="95946abeb88b298e53a6c970166fb7aa"></h2>

-----

## Trace = λ₁+λ₂+ ... + λ<sub>n</sub>

Fact: sum of λ's = a₁₁+a₂₂+ ... + a<sub>nn</sub>.


<details>
<summary>
Symmetric Matrix Example 
</summary>

```
A =

   3   1
   1   3
```
</details>








