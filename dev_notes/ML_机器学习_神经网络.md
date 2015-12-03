

[TOC]

# Neural Networks 

神经网络可以处理feature数量很大的非线性回归

## 模型表示

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural1.png)

 - 左边的x , 是 input layer
 - 最右边的 单个圈， 是 output layer
 - 中间的a， hidden layer
 - `aᵢ⁽ʲ⁾`  代表 j层的 第i个单元
 - Θ`⁽ʲ⁾` 第j层 映射到下一层的函数的参数`矩阵`
 - `x₀` 可以不用明写出来
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2.png)

 - 如图,Θ`⁽¹⁾` 是个 3x4 矩阵: `S₍ⱼ₊₁₎ x （Sⱼ+1）=3x4`  ; `Sⱼ= j`层的单元数,不包括0单元  


我们把激活函数表示为:

![](http://latex.codecogs.com/gif.latex?a_1%5E%7B%282%29%7D%20%3D%20g%28z_1%5E%7B%282%29%7D%20%29)

所以有:

![](http://latex.codecogs.com/gif.latex?z_1%5E%7B%282%29%7D%3D%20%5CTheta_%7B10%7D%5E%7B%281%29%7Dx_0&plus;%5CTheta_%7B11%7D%5E%7B%281%29%7Dx_1&plus;%5CTheta_%7B12%7D%5E%7B%281%29%7Dx_2&plus;%5CTheta_%7B13%7D%5E%7B%281%29%7Dx_3)

## Forward Propagation 前向传播

### 向量化实现

我可以看到，某一层单元的 z ，可以向量化表示

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural_vec.png)

为了纪录方便，我们使用 `a⁽¹⁾` 来表示第一层的 x , 

这样

`z⁽ʲ⁺¹⁾=`Θ`⁽ʲ⁾a⁽ʲ⁾ ` , 这里a是一个4维的向量

![](http://latex.codecogs.com/gif.latex?z%5E%7B%283%29%7D%3D%5CTheta%5E%7B%282%29%7Da%5E%7B%282%29%7D%20%5C%5C%20h_%5Ctheta%28x%29%3Da%5E%7B%283%29%7D%3Dg%28z%5E%7B%283%29%7D%29)

这个计算 h(x)的过程，称为 `前向传播` , 计算顺序:  输入层->隐藏层->输出层

---

我们尝试去掉输入层，发现剩下的部分 和逻辑回归单元非常像。 

只是神经网络不是使用 x,而是使用 `a⁽ʲ⁾`, 


# 应用

##### 简单的例子: 逻辑与 AND

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural_AND.png)

如果把权重(Θ参数) 改为 [-10,20,20] , 就能模拟 逻辑或 OR 运算。


