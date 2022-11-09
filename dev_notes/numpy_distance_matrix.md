# distance matrix

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

b = np.arange(8).reshape([4,2])
# array([[0, 1],
#       [2, 3],
#       [4, 5],
#       [6, 7]])
```

using scipy *distance_matrix*

```python
from scipy.spatial import distance_matrix
distance_matrix(a,b)
# array([[0.        , 2.82842712, 5.65685425, 8.48528137],
#       [2.82842712, 0.        , 2.82842712, 5.65685425],
#       [5.65685425, 2.82842712, 0.        , 2.82842712]])
```


using numpy's broadcasting rules

```python
np.linalg.norm(a[:, None, :] - b[None, :, :], axis=-1)
# array([[0.        , 2.82842712, 5.65685425, 8.48528137],
#       [2.82842712, 0.        , 2.82842712, 5.65685425],
#       [5.65685425, 2.82842712, 0.
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
# array([[ 0,  4,  8, 12],
#       [ 4,  0,  4,  8],
#       [ 8,  4,  0,  4]])
```

Becoming comfortable with this type of vectorized operation is an important way to get better at scientific computing!


From the distance matrix, we can get the **closest pair**

```python
np.unravel_index( dist_m.argmin(), dist_m.shape  )
# (0, 0)
# that is, 1st point from set a, and 1st point from set b
```

## points in 1 set

```python
np.linalg.norm(a[:, None, :] - a[None, :, :], axis=-1)
```







