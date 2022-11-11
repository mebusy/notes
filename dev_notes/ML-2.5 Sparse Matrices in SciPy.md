[](...menustart)

- [2.5.1 sparse matrix 稀疏矩阵](#fca8e35517fe35e6d20e8d2e3bbc1bf5)
    - [2.5.1.3 稀疏矩阵典型应用](#9cadc88507c523d3dea5a4f476db725b)
    - [2.5.1.4](#15ddb90d4e7b762fddb46580bd9bcefb)
    - [2.5.1.5 稀疏结构可视化](#c360446bd3390522432da925eda08668)
- [2.5.2 存储方案](#579875f7240429c4dadfb8219bf0bcd6)
    - [2.5.2.1 通用方法](#2dc46803617f7ef534fcce33d32cdf39)
- [2.5.3 解线性系统](#d1ccdc928930ec7d6b9d66d9d154a6f1)
    - [2.5.3.1. Sparse Direct Solvers](#7b13e1c4fcfcdb6da049730df1b70967)
        - [2.5.3.1.1. Examples](#a4a00f0768812a252f71feaa5d5a55ac)
    - [2.5.3.2. 迭代解](#b9d0a750d313c7b2e876e9695bdb5268)
        - [2.5.3.2.1. 通用参数](#03433a82bafbd7224fd8702e88608a38)
        - [2.5.3.2.2. LinearOperator Class](#6cd19b9ed1714fc2c5bd241abb7b68b3)
    - [2.5.3.3. 特征向量 相关问题解法](#f1e287ba5f84969a417285aa500fdf34)
        - [2.5.3.3.1. eigen 模块](#2c38fb63669a60c4149b23eb29a35ceb)

[](...menuend)


[原文](http://scipy-lectures.github.io/index.html)
<h2 id="fca8e35517fe35e6d20e8d2e3bbc1bf5"></h2>

##2.5.1 sparse matrix 稀疏矩阵
为什么是稀疏矩阵，省内存，空间，计算更有效率

<h2 id="9cadc88507c523d3dea5a4f476db725b"></h2>

###2.5.1.3 稀疏矩阵典型应用
1 求解偏微分方程partial differential equations

* 有限元方法 the finite element method, 
* 机械工程，电子, 物理

2 图像理论

* nonzero at (i, j) means that node i is connected to node j

<h2 id="15ddb90d4e7b762fddb46580bd9bcefb"></h2>

###2.5.1.4 
```python
import numpy as np
import scipy.sparse
import scipy.sparse as sps
import matplotlib.pyplot as plt
```

<h2 id="c360446bd3390522432da925eda08668"></h2>

###2.5.1.5 稀疏结构可视化

* spy() from matplotlib
```python
plt.clf()
plt.spy(mtx, marker='.', markersize=2)
plt.show()
```

<h2 id="579875f7240429c4dadfb8219bf0bcd6"></h2>

##2.5.2 存储方案

* scipy.sparse中共有7种存储方式的稀疏矩阵，适合不同的场合。
csc_matrix: Compressed Sparse Column format
csr_matrix: Compressed Sparse Row format
bsr_matrix: Block Sparse Row format
lil_matrix: List of Lists format
dok_matrix: Dictionary of Keys format
coo_matrix: COOrdinate format (aka IJV, triplet format)
dia_matrix: DIAgonal format

* 注意 * 符号作为矩阵乘法，不是numpy的一部分，把稀疏矩阵传给numpy 不会起作用。

<h2 id="2dc46803617f7ef534fcce33d32cdf39"></h2>

###2.5.2.1 通用方法

所有scipy.sparse 类 都是 spmatrix的子类

* 默认算数操作的实现，总是会把矩阵转为CSR 压缩的稀疏行
* shape, data type set/get
* nonzero indices
* 格式转换，和NumPy 交互(toarray(), todense())
 

属性 attributes

* mtx.A - same as mtx.toarray()
* mtx.T - transpose (same as mtx.transpose())
* mtx.H - 厄米特矩阵 Hermitian (conjugate) transpose
* mtx.real - real part of complex matrix
* mtx.imag - imaginary part of complex matrix
* mtx.size - the number of nonzeros (same as self.getnnz())
* mtx.shape - the number of rows and columns (tuple)

数据经常 stored in NumPy arrays


<h2 id="d1ccdc928930ec7d6b9d66d9d154a6f1"></h2>

##2.5.3 解线性系统

* 稀疏 矩阵/特征值的解法，都在scipy.sparse.linalg
* the submodules:
dsolve: 直接因式分解
isolve: 迭代法解
eigen: 稀疏特征值问题求解

<h2 id="7b13e1c4fcfcdb6da049730df1b70967"></h2>

###2.5.3.1. Sparse Direct Solvers

* 默认解法: SuperLU 4.0
* 可选: umfpack , 效率推荐scikits.umfpack

<h2 id="a4a00f0768812a252f71feaa5d5a55ac"></h2>

####2.5.3.1.1. Examples

* import整个module, 看它的文档
```python
>>> from scipy.sparse.linalg import dsolve
>>> help(dsolve) 
```
* superlu 和 umfpack 都可以用

准备一个线性系统
```python
>>> import numpy as np
>>> from scipy import sparse
>>> mtx = sparse.spdiags([[1, 2, 3, 4, 5], [6, 5, 8, 9, 10]], [0, 1], 5, 5)
>>> mtx.todense()
matrix([[ 1,  5,  0,  0,  0],
        [ 0,  2,  8,  0,  0],
        [ 0,  0,  3,  9,  0],
        [ 0,  0,  0,  4, 10],
        [ 0,  0,  0,  0,  5]])
>>> rhs = np.array([1, 2, 3, 4, 5])
```

双精度实数解
```python
>>> mtx2 = mtx.astype(np.float64)
>>> x = dsolve.spsolve(mtx2, rhs, use_umfpack=True)
>>> print x
[ 106.   -21.     5.5   -1.5    1. ]
>>> print "Error: ", mtx2 * x - rhs
Error:  [ 0.  0.  0.  0.  0.]
```

<h2 id="b9d0a750d313c7b2e876e9695bdb5268"></h2>

###2.5.3.2. 迭代解

* isolve 模块包含以下解法:
bicg (BIConjugate Gradient)
bicgstab (BIConjugate Gradient STABilized)
cg (Conjugate Gradient) - symmetric positive definite matrices only
cgs (Conjugate Gradient Squared)
gmres (Generalized Minimal RESidual)
minres (MINimum RESidual)
qmr (Quasi-Minimal Residual)

<h2 id="03433a82bafbd7224fd8702e88608a38"></h2>

#### 2.5.3.2.1. 通用参数

<h2 id="6cd19b9ed1714fc2c5bd241abb7b68b3"></h2>

#### 2.5.3.2.2. LinearOperator Class
```python
from scipy.sparse.linalg.interface import LinearOperator
```

* 矩阵 向量 乘法的通用接口
* shape and matvec()  (+ some optional parameters)
* 例子

<h2 id="f1e287ba5f84969a417285aa500fdf34"></h2>

### 2.5.3.3. 特征向量 相关问题解法
<h2 id="2c38fb63669a60c4149b23eb29a35ceb"></h2>

####2.5.3.3.1. eigen 模块
* ARPACK 为解决大型特征值问题而设计的Fortran77的子程序的集合
* lobpcg（局部最优座预处理共轭梯度法）








