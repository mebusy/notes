...menustart

 - [numpy tips](#c2bfb8f194cb52abbd9cc9397dafc5d4)
     - [Combining Arrays](#84df0f6a0e96bb96e66fdba51a103ad5)
     - [Math Functions](#1f1ef887de84fa2b7f644b5878b4e6ce)
     - [Indexing / Slicing](#6b17874075ca37cc84a6c0d09e623e1c)
     - [Iterating Over Arrays](#f32b904edd83a21e8b374913f5631504)
     - [数据 slice](#1ae1043e3a38472916094e5c042464ed)
     - [数据过滤](#86260398567c0091b1c262ef98512bd6)
     - [数据 拼接](#6ab51568114b14d4784a1fa07f6717b5)
     - [数据转换](#3c30b3189b43008ec08418c0d6afc49f)

...menuend


<h2 id="c2bfb8f194cb52abbd9cc9397dafc5d4"></h2>


# numpy tips

 - Use the shape method to find the dimensions of the array. (rows, columns)
    - `m.shape   # (2, 3) `
 - `arange` returns evenly spaced values within a given interval.
    - `np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30`
    - `array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])`
 - `reshape` returns an array with the same data with a new shape.
    - `n.reshape(3, 5) # reshape array to be 3x5`
    - `array([[ 0,  2,  4,  6,  8], [10, 12, 14, 16, 18], [20, 22, 24, 26, 28]])`
 - `linspace` returns evenly spaced numbers over a specified interval.
    - `o = np.linspace(0, 4, 9)`
    - `array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ])`
 - `resize` changes the shape and size of array **in-place**.
    - `o.resize(3, 3)`
    - `array([[ 0. ,  0.5,  1. ], [ 1.5,  2. ,  2.5], [ 3. ,  3.5,  4. ]])`
 - `ones` returns a new array of given shape and type, filled with ones.
    - `np.ones((3, 2))`
    - `array([[ 1.,  1.], [ 1.,  1.], [ 1.,  1.]])`
 - `zeros` returns a new array of given shape and type, filled with zeros.
    - `np.zeros((2, 3))`
 - `eye` returns a 2-D array with ones on the diagonal and zeros elsewhere.
    - `np.eye(3)`

```python
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
```

 - `diag` extracts a diagonal or constructs a diagonal array.

```python
>>> y = np.array([4, 5, 6])
>>> y
>>> array([4, 5, 6])
>>>
>>> np.diag(y)
>>> array([[4, 0, 0],
           [0, 5, 0],
           [0, 0, 6]])
```

 - Create an array using repeating list (or see np.tile)
    - `np.array([1, 2, 3] * 3)`
    - `array([1, 2, 3, 1, 2, 3, 1, 2, 3])`
 - Repeat elements of an array using repeat.
    - `np.repeat([1, 2, 3], 4)`
    - `array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])`
 

<h2 id="84df0f6a0e96bb96e66fdba51a103ad5"></h2>


## Combining Arrays

```python
>>> p = np.ones([2, 3], int)
>>> p
>>> array([[1, 1, 1],
           [1, 1, 1]])
```

 - Use `vstack` to stack arrays in sequence vertically (row wise).

```python
>>> np.vstack([p, 2*p])
>>> array([[1, 1, 1],
           [1, 1, 1],
           [2, 2, 2],
           [2, 2, 2]])
```

 - Use hstack to stack arrays in sequence horizontally (column wise).

```python
>>> np.hstack([p, 2*p])
>>> array([[1, 1, 1, 2, 2, 2],
           [1, 1, 1, 2, 2, 2]])
```

 - Dot Product:
    - `x.dot(y)`
 - Use .T to get the transpose.
    - `z.T`
 - Use .dtype to see the data type of the elements in the array.
    - `z.dtype`
 - Use .astype to cast to a specific type.
    - `z = z.astype('f')`

<h2 id="1f1ef887de84fa2b7f644b5878b4e6ce"></h2>


## Math Functions

```python
a = np.array([-4, -2, 1, 3, 5])
a.mean()
0.59999999999999998
a.std()
3.2619012860600183

# argmax and argmin return the index of the maximum and minimum values in the array.
a.argmax()
4 
a.argmin()
0

# PS. also works on multidimensional array 
# but will flatten the array , then do operations
```

<h2 id="6b17874075ca37cc84a6c0d09e623e1c"></h2>


## Indexing / Slicing

```python
s = np.arange(13)**2
s
array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121, 144])

# 切片
s[-5::-2]
array([64, 36, 16,  4,  0])

# Let's look at a multidimensional array.
r = np.arange(36)
r.resize((6, 6))
r
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])

# Use bracket notation to slice: array[row, column]
r[2, 2]
14

# And use : to select a range of rows or columns
r[3, 3:6]
array([21, 22, 23])

# Here we are selecting all the rows up to (and not including) row 2,
# and all the columns up to (and not including) the last column.
r[:2, :-1]
array([[ 0,  1,  2,  3,  4],
       [ 6,  7,  8,  9, 10]])

# This is a slice of the last row, and only every other element.
r[-1, ::2]
array([30, 32, 34])

# We can also perform conditional indexing. 
# Here we are selecting values from the array that
# that are greater than 27. (Also see `np.where`)
r[r > 27]
array([28, 29, 30, 31, 32, 33, 34, 35])

# Here we are assigning all values in the array 
# that are greater than 30 to the value of 30.
r[r > 30] = 30
r
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 30, 30, 30, 30, 30]])
```


 - **Be careful with copying and modifying arrays in NumPy!**
 - use `r.copy` to create a copy that will not affect the original array
    - `r_copy = r.copy()`

<h2 id="f32b904edd83a21e8b374913f5631504"></h2>


## Iterating Over Arrays

 - Let's create a new 4 by 3 array of random numbers 0-9.

```python
test = np.random.randint(0, 10, (4,3))
test
array([[5, 2, 9],
       [6, 0, 1],
       [0, 4, 5],
       [3, 8, 0]])
```

 - Use zip to iterate over multiple iterables.

```python
test2 = test**2
test2
array([[25,  4, 81],
       [36,  0,  1],
       [ 0, 16, 25],
       [ 9, 64,  0]])

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)
[5 2 9] + [25  4 81] = [30  6 90]
[6 0 1] + [36  0  1] = [42  0  2]
[0 4 5] + [ 0 16 25] = [ 0 20 30]
[3 8 0] + [ 9 64  0] = [12 72  0]
```



<h2 id="1ae1043e3a38472916094e5c042464ed"></h2>


## 数据 slice


- 从2维度数据中 抽取第一列

```python
train_X = data[:,0]  
```

- 从2维度数据中 抽取第1,3列

```python
train_X = data[:,[0,2]]  
```

- 从2维度数据中 抽取第一列 ，返回一个 Nx1 的 2维度数组

```python
train_X = data[:, [0] ] 
```


<h2 id="86260398567c0091b1c262ef98512bd6"></h2>


## 数据过滤

- 返回第2列 值是1的 第1列数据

```python
pos = data[:, 1] == 1
Train_X[ pos , 0  ]
```

<h2 id="6ab51568114b14d4784a1fa07f6717b5"></h2>


## 数据 拼接

- 在2维数组 第一列 ， 插入 1列 1
    - 注意，要确保 Train_X 是2维数据，如果不是，使用 reshape 转成2维数组

```python
np.insert( Train_X , 0, 1 , axis =1 )
```


<h2 id="3c30b3189b43008ec08418c0d6afc49f"></h2>


## 数据转换

- bool 数据转 int 数组

```python
>>> y
array([False, False,  True,  True], dtype=bool)
>>> 1*y                      # Method 1
array([0, 0, 1, 1])
>>> y.astype(int)            # Method 2
array([0, 0, 1, 1]) 
```

- constant 转 2维数组

```python
np.array( 0.4 , ndmin=2  )
```

--------

# SciPy 2019

## Array Slicing

numpy 可以把多个维度的slicing 放在一个方括号内...

![](../imgs/np_array_slicing.png)

- single colon : everything





