
#numpy tips


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


## 数据过滤

- 返回第2列 值是1的 第1列数据

```python
pos = data[:, 1] == 1
Train_X[ pos , 0  ]
```

## 数据 拼接

- 在2维数组 第一列 ， 插入 1列 1
	- 注意，要确保 Train_X 是2维数据，如果不是，使用 reshape 转成2维数组

```python
np.insert( Train_X , 0, 1 , axis =1 )
```


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