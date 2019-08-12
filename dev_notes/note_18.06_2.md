
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

![](../imgs/la_1806_cramer_rule.gif)

What do I get in Cᵀb ? What's the first entry of Cᵀb ?  

Somehow I multiply cofactors by the entries of b, anytime I'm multiplying cofactors by numbers, I think, I'm getting the determinant of something. Let's call the matrix B , whose determinant comes out of Cᵀb .

So x₁ = detB₁/detA  , x₂ = detB₂/detA , ... 

**4C:** Cramer's rule: The jth component of x = A⁻¹b is the ratio

![](../imgs/LA_det_cramer_rule.png)

Actually, Cramer's Rule is a disastrous way to go, because compute these determinants takes like approximately forever.  

But having a formula allows you to do algebra instead of algorithms. They're nice formulas, but I just don't want you to use them. 


## |detA| = volume of box

---

# 21. 



