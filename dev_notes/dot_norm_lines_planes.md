...menustart

- [Dot Product and Normals to Lines and Planes](#8c74fbe5491cc80df8a6aeac75b11cb7)
    - [Normal Vector A](#26d5cd5f94257c59f16c4137aae7cd7c)

...menuend


<h2 id="8c74fbe5491cc80df8a6aeac75b11cb7"></h2>


# Dot Product and Normals to Lines and Planes


The equation of a line in the form ax + by = c can be written as a dot product:

 `(a,b)·(x,y) = c, or A·X = c,`

where A = (a, b) and X = (x,y).

The equation of a line in the form ax + by + cz = d can be written as a dot product:

 `(a,b, c) · (x,y, z) = d, or A · X = d,`

where A = (a, b, c) and X = (x,y, z). 


<h2 id="26d5cd5f94257c59f16c4137aae7cd7c"></h2>


## Normal Vector A

If point P and Q are in the plane with equation A·X = d, then A·P = d and A·Q = d, so

 `A · (Q - P) = d - d = 0.`

This means that the vector A is orthogonal to any vector PQ between points P and Q of the plane.

But the vector PQ can be thought of as a tangent vector or direction vector of the plane. This means that vector A is orthogonal to the plane, meaning A is orthogonal to every direction vector of the plane.

A nonzero vector that is orthogonal to direction vectors of the plane is called a **normal vector to the plane**.

Thus the **coefficient vector A is a normal vector** to the plane.

**Careful**: It is NOT true that for any point P in the plane, A is orthogonal to P (unless d = 0).


**Example**: Finding a plane when the normal is known. Suppose that A = (1, 2, 3). Find the equation of the plane through P = (1, -1, 4) with normal vector A.

**Solution**: The equation must be (1, 2, 3) · X = d for some constant d. But since P is on the plane, if we set X = P, we must get the correct value of d. Thus d = (1, 2, 3) · (1, -1, 4) = 1 -2 + 12 = 11. The equation is A · X = 11.







