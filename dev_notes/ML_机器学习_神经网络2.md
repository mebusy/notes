
# 神经网络2

##### 代价函数 和 反向传播 Backpropagation

一些标记:

 - L 标记 神经网络的总层数
 - S₄ 表示第4层的单元数，不包括偏差单元 `bias unit`
 - k 表示第几个输出单元

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural_costFunc.png)

 - k 代表第几个输出单元
 - 神经网络的代价函数，左侧部分是对K个输出单元的代价函数的求和
 - 右侧的正则化项

为了 min J(Θ)我们需要计算:

![](http://latex.codecogs.com/gif.latex?%5C%5CJ%28%5CTheta%29%5C%5C%5C%5C%20%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20%5CTheta_%7Bij%7D%5E%7B%28l%29%7D%7DJ%28%5CTheta%29)

记住:

这项是一个实数

![](http://latex.codecogs.com/gif.latex?%5CTheta_%7Bij%7D%5E%7B%28l%29%7D%20%5C%2C%20%5Cepsilon%5C%2C%20%5Cmathbb%7BR%7D)

我们使用前向传播计算激励值。

为了计算导数项，我们采用反向传播算法`Backpropagation`

