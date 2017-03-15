...menustart

 - [numpy tips](#c2bfb8f194cb52abbd9cc9397dafc5d4)
	 - [数据 slice](#1ae1043e3a38472916094e5c042464ed)
	 - [数据过滤](#86260398567c0091b1c262ef98512bd6)
	 - [数据 拼接](#6ab51568114b14d4784a1fa07f6717b5)
	 - [数据转换](#3c30b3189b43008ec08418c0d6afc49f)

...menuend


<h2 id="c2bfb8f194cb52abbd9cc9397dafc5d4"></h2>

#numpy tips


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




