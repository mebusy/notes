
[TOC]

# 逻辑回归  Logistic Regression

##### 逻辑回归其实是分类问题 Classification

##### 下面讨论都是`二元分类`问题，即目标值只有`0,1` 两种可能

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

我们观察 g(z)的函数图 , 可以看到

  - 当 z>=0, 也即 Θᵀx >= 0 时， 函数值 >= 0.5
  - 当 z< 0, 也即 Θᵀx <  0 时， 函数值 < 0.5
  - 当 Θ 确定后, Θᵀx 的图像就是 决策边界

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
J(Θ)= -1/m ∑[ ylog( h(x) ) + (1-y)log( 1-h(x) ) ]
```

![][1]


## 梯度下降


迭代公式和 线性回归基本一样，唯一区别就是 h(x) 不同。

？为什么公式基本一样？ 因为这只是 h(x) 和 y 之间的比较？

![](http://latex.codecogs.com/gif.latex?%5Ctheta%3A%3D%5Ctheta-%5Calpha%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%5B%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5Ccdot%20x%5E%7B%28i%29%7D%20%5D)


## 高级优化

##### 优点
  - 不需要手动选择𝛼
  - 一般比梯度下降算法快

##### 缺点
  - 更加复杂

### 用法

```
% 假设 有两个Θ₀ Θ₁ 参数

% 首先定义一个costFunction, 返回J 和 一个梯度值
function [jVal , gradient] = costFunction( theta )
    jval = % 计算代价函数 J(Θ)
    
    gradient = zeroes(2,1) ;
    gradient[1] = % J(Θ) 对 Θ₀ 的偏导数
    gradient[2] = % J(Θ) 对 Θ₁ 的偏导数
end

% 有了这个 costFunction之后，就可以

options = optimset( 'GradObj' , 'on' , 'MaxIter' , '100' );
initialTheta = zeros( 2,1 );  % Θ 初始值
[optTheta, functionVal, exitFlag] ...
    = fminunc(@costFunction , initialTheta , options );
```

# 多类分类

## 1-vs-all 分类思想

例子：

假设我们有一个训练集，有三个类别。

我们要做的，就是将其分成3个二元分类问题。

```
hⁱ(x) = P( y=i | x; Θ )   (i=1,2,3)
```

TODO:  不是很明白，3个0,1, 怎么合成一个 1,2,3

# review :

##### 和线性回归一样，拟合曲线，需要多项式

##### h(x) = g( θᵀx ) , θᵀx 图像可以看到决策边界

##### 逻辑回归的 代价函数 J 总是个凸函数


---
---

  [1]: http://latex.codecogs.com/gif.latex?h_%5Ctheta%28x%29%3D%5Cfrac%7B1%7D%7B1&plus;%20e%5E%7B-%5Ctheta%5E%7BT%7Dx%7D%7D


