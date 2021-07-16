...menustart


...menuend


```python
>>> a = [2,1]
>>> b = [1,2]
>>> np.cross(a,b)
array(3)
>>> a = [2,1,0]
>>> b = [1,2,0]
>>> np.cross(a,b)
array([0, 0, 3])
>>>
```

AI

BFS 

bᵐ, 没有权重


+ 权重 UCS

A*  UCS +  Heuristics (Greedy)


8 Puzzle



CSP

N-Queens


Adv

mini-max , act as a ghost? 

Expectimax Search -> MDP


==========

Dot Product


- Measuring direction

cosθ = x·y/‖x‖‖y‖

负点积 意味着向量指向不同的方向。
如果点积为零，则两个向量正交（垂直）。

can I see it？


- Projecting Vectors

当至少一个向量是单位长度时，点积是 非单位长度向量在归一化向量轴上的投影长度
（当它们都是单位长度时，它们都在方向上移动相同的量 彼此的）。

点到直线的距离问题


- Planes (aka walls/slopes/triangles)

v<sub>out</sub> = v<sub>in</sub> - 2( v<sub>in</sub> · n ) n




向量运算在游戏开发中的应用和思考

https://wuzhiwei.net/vector_in_games/?hmsr=toutiao.io&utm_campaign=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io

Applications of the Vector Dot Product for Game Programming

https://hackernoon.com/applications-of-the-vector-dot-product-for-game-programming-12443ac91f16




[Cross Product Application](https://amirazmi.net/cross-products-in-game-development-and-their-use-cases/)


-- compute projection vector

method 1

```python
>>> import numpy as np
>>> v = np.array( [4,1]   )
>>> w = np.array( [2,-1] )
>>> # v projects onto w
>>> w_u = w / np.sqrt( w.dot(w) )
>>> w_u
array([ 0.89442719, -0.4472136 ])
>>> # calculate lengh of projection vector
>>> v.dot(w_u)
3.1304951684997055
>>> # projection vector
>>> v.dot(w_u) * w_u
array([ 2.8, -1.4])
```

```python
>>> v.dot( w ) / np.sqrt( w.dot(w) ) * w /  np.sqrt( w.dot(w) )
array([ 2.8, -1.4])
>>> v.dot( w ) /  w.dot(w) * w
array([ 2.8, -1.4])
```

```octave
octave:8> w*w' / (w'*w)  * v
ans =

   2.8000
  -1.4000
```







