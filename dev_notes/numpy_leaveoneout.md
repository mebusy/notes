[](...menustart)

- [Numpy Leave One Out Array](#a1671d9686bccadf21021559cf428f7d)

[](...menuend)


<h2 id="a1671d9686bccadf21021559cf428f7d"></h2>

# Numpy Leave One Out Array

Goal: construct a leave-one-out matrix from a vecotr of length k.

In the matrix, each row is a vecotr of length k-1, with a different vector compeont dropped each time.

For example, suppose you have data points [(1,4), (2,7), (3,11), (4,9), (5,15)] that you want to perfrom for a simple regression model. 

For each cross-validation, you use one point for testing, and the remainign 4 points for training. In other words, you want the trainigng set to be:

```python
[(2,7), (3,11), (4,9), (5,15)]
[(1,4), (3,11), (4,9), (5,15)]
[(1,4), (2,7),  (4,9), (5,15)]
[(1,4), (2,7), (3,11), (5,15)]
[(1,4), (2,7), (3,11), (4,9)]
```

Use numpy


```python
N = 5
np.tri(N)
# array([[1., 0., 0., 0., 0.],
#        [1., 1., 0., 0., 0.],
#        [1., 1., 1., 0., 0.],
#        [1., 1., 1., 1., 0.],
#        [1., 1., 1., 1., 1.]])
np.tri(N, N-1)
# array([[1., 0., 0., 0.],
#        [1., 1., 0., 0.],
#        [1., 1., 1., 0.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.]])
np.tri(N, N-1, -1)
# array([[0., 0., 0., 0.],
#        [1., 0., 0., 0.],
#        [1., 1., 0., 0.],
#        [1., 1., 1., 0.],
#        [1., 1., 1., 1.]])
```


```python
np.arange(1, N)
# array([1, 2, 3, 4])
np.arange(1, N) - np.tri(N, N-1, -1)
# array([[1., 2., 3., 4.],
#        [0., 2., 3., 4.],
#        [0., 1., 3., 4.],
#        [0., 1., 2., 4.],
#        [0., 1., 2., 3.]])
idx = np.arange(1, N) - np.tri(N, N-1, -1).astype('int')
# array([[1, 2, 3, 4],
#        [0, 2, 3, 4],
#        [0, 1, 3, 4],
#        [0, 1, 2, 4],
#        [0, 1, 2, 3]])
```

```python
# raw data
data = np.array([(1,4), (2,7), (3,11), (4,9), (5,15)])
arr_leaveoneout = data[idx]
# array([[[ 2,  7],
#         [ 3, 11],
#         [ 4,  9],
#         [ 5, 15]],
# 
#        [[ 1,  4],
#         [ 3, 11],
#         [ 4,  9],
#         [ 5, 15]],
# 
#        [[ 1,  4],
#         [ 2,  7],
#         [ 4,  9],
#         [ 5, 15]],
# 
#        [[ 1,  4],
#         [ 2,  7],
#         [ 3, 11],
#         [ 5, 15]],
# 
#        [[ 1,  4],
#         [ 2,  7],
#         [ 3, 11],
#         [ 4,  9]]])
```




