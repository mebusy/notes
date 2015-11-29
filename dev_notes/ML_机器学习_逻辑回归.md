
[TOC]

# 逻辑回归  Logistic Regression

##### 逻辑回归其实是分类问题 Classification

##### 下面讨论都是`两类`问题，即目标值只有`0,1` 两种可能

## 模型 : h(x) = g(Θᵀx)

##### logistic回归实质上还是线性回归模型

我们在 线性回归的连续值 结果上加 一层函数映射 g, 将连续值映射到离散值0/1上

```
h(x) = g(Θᵀx)
```

其中,

![](http://latex.codecogs.com/gif.latex?g%28z%29=%5Cfrac%7B1%7D%7B1&plus;%20e%5E%7B-z%7D%7D)

完整的假设函数如下：

![][1]


g(z) 称为 S型函数 Sigmoid function 或 逻辑函数 Logistic function

g(z)的函数图像如下：

![](http://images.cnitblog.com/blog/392228/201410/311940295342017.jpg)

当z趋近于-∞，g(z)趋近于0，而z趋近于∞，g(z)趋近于1，从而达到分类的目的。

整条曲线呈S型, 这也是 "S型" 叫法的由来。


##### 逻辑回归的假设函数h(x)的输出，是 y=1的概率的估计值

```
h(x) = P( y=1|x;Θ )
P( y=1|x;Θ ) + P( y=0|x;Θ ) = 1
```

## 决策边界  decision boundary

决策边界 是假设函数的一个属性，它包含参数 Θ

## 代价函数 cost function J

##### 逻辑回归 J 应该是个`凸函数 convex` ， 线性回归的J 是`非凸函数`

```
J(Θ)= 1/m ∑ cost( h(x) , y )
```

![](http://latex.codecogs.com/gif.latex?cost%28%20h_%5Ctheta%28x%29%2Cy%29%3D%5Cbegin%7Bcases%7D%20-log%28h_%5Ctheta%28x%29%29%20%26%20%5Ctext%7B%20if%20%7D%20y%3D%201%5C%5C%20-log%281-h_%5Ctheta%28x%29%29%20%26%20%5Ctext%7B%20if%20%7D%20y%3D0%20%5Cend%7Bcases%7D)

`特点`:

 - 如果 h(x)=y, 那么 cost(h(x),y)=0  ( y=[0,1] )
 - 如果 y=0 ,  h(x)->1 ,  那么 cost(h(x),y) -> ∞
 - 如果 y=1 ,  h(x)->0 ,  那么 cost(h(x),y) -> ∞
 
拆成两个等式 非常不利于计算，利用 y 只能取0和1的特点，我们可以把cost function 简化为一个等式

```
cost(h(x),y) = -ylog( h(x) ) -(1-y)log( 1-h(x) )
```

最终我们获得完整的代价函数:

```
J(Θ)= -1/m [∑ ylog( h(x) ) + (1-y)log( 1-h(x) )]
```

![][1]


## 梯度下降

![](http://latex.codecogs.com/gif.latex?%5Ctheta_j%3A%3D%5Ctheta_j%20-%20%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%29-y%29x_j)


迭代公式和 线性回归基本一样，唯一区别就是 h(x) 不同。


---
---

  [1]: http://latex.codecogs.com/gif.latex?h_%5Ctheta%28x%29%3D%5Cfrac%7B1%7D%7B1&plus;%20e%5E%7B-%5Ctheta%5E%7BT%7Dx%7D%7D


