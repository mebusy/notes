...menustart

 - [Elgenvalues and Elgenvectors](#8358d3063f9f8db669067bc62cf5ea5e)
	 - [5.1 INTRODUCTION](#103445c268b50fae9bd814331a04faa4)

...menuend



<h2 id="8358d3063f9f8db669067bc62cf5ea5e"></h2>
# Elgenvalues and Elgenvectors


<h2 id="103445c268b50fae9bd814331a04faa4"></h2>
## 5.1 INTRODUCTION

This chapter begins the "second half" of linear algebra. 

The first half was about Ax = b. The new problem Ax = λx  will still be solved by simplifying a matrix -- making it diagonal if possible. 

The basic step is no longer to subtract a multiple of one row from another. Elimination changes the eigenvalues, which we don't want.

Determinants give a transition from Ax = b to Ax = λx. In both cases the determinant leads to a "formal solution": to Cramer's rule for x = A⁻¹b, and to the polynomial det (A - λI), whose roots will be the eigenvalues. (All matrices are now square; the eigenvalues of a rectangular matrix make no more sense than its determinant.) The determinant can actually be used if n = 2 or 3. For large n, computing λ, is more difficult than solving Ax = b.

