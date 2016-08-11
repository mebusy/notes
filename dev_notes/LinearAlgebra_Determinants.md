...menustart

 - [Determinants](#44858f4401928ded6e165da37ea948a5)

...menuend



<h2 id="44858f4401928ded6e165da37ea948a5"></h2>
# Determinants

One viewpoint is this: The determinant provides an explicit "formula" for each entry of A⁻¹ and A⁻¹b. 

We can list four of the main uses of determinants:

 1. They test for invertibility. 
 	- ***If the determinant of A is zero, then A is singular***. 
 	- ***If det A ≠ 0, then A is invertible*** (and A⁻¹ involves 1/detA).
 	- 
 	- The most important application, and the reason this chapter is essential to the book, is to the family of matrices A - λI. The parameter λ is subtracted all along the main diagonal, and the problem is to find the eigenvalues for which A - λI is singular. The test is det(A - λI) = 0. This polynomial of degree n in X has exactly n roots. The matrix has n eigenvalues. This is a fact that follows from the determinant formula, and not from a computer.
 2. The determinant of A equals the ***volume*** of a box in n-dimensional space. 
 	- The edges of the box come from the rows of A . The columns of A would give an entirely different box with the same volume