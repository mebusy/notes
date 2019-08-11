
# 18.Determinants 

Up to now we paid a lot of attention to rectangular matrices. 

Now, concentrating on square matrices. Determinants and Eigen values are big, big chunk of 18.06.

## Determinants , det A = |A| 

Every square matrix has a number associated with , called its determinant. 

- det A = 0 , means A is singular.  
- det A !=0 , means A is invertible.

## Signed

Determinant is signed.

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


# 19. Formular for Determinant

## Formula for detA ( n! terms )

 - use property 3 to break down each row 
    - [a b c] = [a 0 0] + [0 b 0] + [0 0 c]
 - the determinant of A can be expanded into nⁿ terms 
 - a lot terms has 0 det,  they can be removed.
 - The nonzero terms have to come in different columns and rows. 
    - ![](../imgs/LA_det_3x3_6terms.png)
 - ![](../imgs/LA_det_bigFormula.png)
 
## Cofactor formula

Cofactor is a way of breaking up above big formula that connects the nxn determinant to a determinant one smaller. 

![](../imgs/LA_det_cofactor_filter.png)

- **The determinant of A is a combination of any row i times its cofactors**.
    - **det A by cofactors:** det A = aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢ<sub>𝑛</sub>Cᵢ<sub>𝑛</sub>. (10)
    - The cofactor is the determinant of Mᵢⱼ , with the correct sign:
        - **delete row i and column j:** Cᵢⱼ = (-1)ⁱ⁺ʲ detMᵢⱼ.   (11)


# 20. APPLICATIONS OF DETERMINANTS

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

## Cramers Rule for x=A⁻¹b

 

## |detA| = volume of box





