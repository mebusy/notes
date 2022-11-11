[](...menustart)

- [distance matrix](#85ce9fbdac706be2d7d0c1472b752b44)
    - [points in two sets](#8402d09645a7552c57b0679478c932ac)
    - [points in 1 set](#3ef2b1846a58f100a48f947755ef9b67)

[](...menuend)


<h2 id="85ce9fbdac706be2d7d0c1472b752b44"></h2>

# distance matrix

<h2 id="8402d09645a7552c57b0679478c932ac"></h2>

## points in two sets

compute the pairwise distance between two sets of points, *a* and *b*

The technique works for an arbitrary number of points, but for simplicity make them 2D.

Set a has m points giving it a shape of (m, 2), and b has n points giving it a shape of (n, 2).

```python
import numpy as np
a = np.arange(6).reshape(3,2)
# array([[0, 1],
#        [2, 3],
#        [4, 5]])

b = np.linspace(7, 14, num=8).reshape(4,-1)
# array([[ 7.,  8.],
#        [ 9., 10.],
#        [11., 12.],
#        [13., 14.]])
```

using scipy *distance_matrix*

```python
from scipy.spatial import distance_matrix
distance_matrix(a,b)
# array([[ 9.89949494, 12.72792206, 15.55634919, 18.38477631],
#        [ 7.07106781,  9.89949494, 12.72792206, 15.55634919],
#        [ 4.24264069,  7.07106781,  9.89949494, 12.72792206]])
```


using numpy's broadcasting rules

```python
np.linalg.norm(a[:, None, :] - b[None, :, :], axis=-1)
# array([[ 9.89949494, 12.72792206, 15.55634919, 18.38477631],
#        [ 7.07106781,  9.89949494, 12.72792206, 15.55634919],
#        [ 4.24264069,  7.07106781,  9.89949494, 12.72792206]])
```

Why does this work ?

Because NumPy applies element-wise calculations when axes **have the same dimension** or when one of the axes can be expanded to match. It checks for matching dimensions by **moving right to left through the axes**.

`a[:, None, :]` gives `(3, 1, 2)` view of a and `b[None, :, :]` gives  `(1, 4, 2)` view of b. 

The subtraction operation moves right(2) to left(3). Any 2D point can be subtracted from another 2D point.

The result is a `(3, 4, 2)` array with element-wise subtractions.

Then, we apply the L2 norm along the -1th axis (the last axis), This gives us the Euclidean distance between each pair of points.

numpy can also make it works with any operation that can do reductions. e.g. Manhattan distance 

```python
np.sum(np.abs(a[:, None, :] - b[None, :, :]), axis=-1)
# array([[14., 18., 22., 26.],
#        [10., 14., 18., 22.],
#        [ 6., 10., 14., 18.]])
```

Becoming comfortable with this type of vectorized operation is an important way to get better at scientific computing!


From the distance matrix, we can get the **closest pair**

```python
dist_m = np.linalg.norm(a[:, None, :] - b[None, :, :], axis=-1)
np.unravel_index( dist_m.argmin(), dist_m.shape  )
# (2, 0)
# that is, 3rd point from set a, and 1st point from set b
```

<h2 id="3ef2b1846a58f100a48f947755ef9b67"></h2>

## points in 1 set

```python
np.linalg.norm(a[:, None, :] - a[None, :, :], axis=-1)
# array([[0.        , 2.82842712, 5.65685425],
#        [2.82842712, 0.        , 2.82842712],
#        [5.65685425, 2.82842712, 0.        ]])
```




