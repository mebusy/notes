...menustart

- [线性回归 梯度下降 数学推导](#e28d21841f0baf693d9bd91107d5dfd9)
    - [梯度下降](#b1f126ef3b67138c7e19176b361e6857)
    - [批量梯度下降法](#94dde0a8dbe1f4313139f9952c5c55f5)

...menuend


<h2 id="e28d21841f0baf693d9bd91107d5dfd9"></h2>


# 线性回归 梯度下降 数学推导

<h2 id="b1f126ef3b67138c7e19176b361e6857"></h2>


## 梯度下降

- ![](https://juejin.cn/equation?tex=f(%5Cboldsymbol%7Bx_i%7D)%20%3D%20%5Cboldsymbol%7Bw%7D%5ET%20%5Cboldsymbol%7Bx_i%7D)

梯度下降法: 是从某一个权重 w 的初始值开始，逐渐对权重进行更新, 每次用新计算的值覆盖原来的值： 

- ![](https://juejin.cn/equation?tex=w_j%20%3A%3D%20w_j%20-%20%5Calpha%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%7Bw_j%7D%7DJ(%5Cboldsymbol%7Bw%7D))

- 这里
    - α is learning rate
    - ![](https://juejin.cn/equation?tex=%5Cfrac%20%5Cpartial%20%7B%5Cpartial%7Bw_j%7D%7DJ(%5Cboldsymbol%7Bw%7D)) is Gradient
        - 在某个点，函数沿着梯度方向的变化速度最快。

w 是一个向量, 更新w的时候，我们是要同时对 n 维所有w值进行更新，

接下来我们简单推导一下梯度公式.

首先考虑只有一条训练样本 ![](https://juejin.cn/equation?tex=(%5Cboldsymbol%7Bx_i%7D%2C%20y_j))  的情况, ![](https://juejin.cn/equation?tex=J(w)%3D%5Cfrac%7B1%7D%7B2%7D(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%5E2).

可以得到:

- ![eq1][1]


对单个训练样本，每次对梯度的更新:

- ![](https://juejin.cn/equation?tex=w_j%20%3A%3D%20w_j%20-%20%5Calpha%20(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%20x_%7Bi%2Cj%7D)


<h2 id="94dde0a8dbe1f4313139f9952c5c55f5"></h2>


## 批量梯度下降法

当有 m个训练样本的时候 , cost function 为 ![](https://juejin.cn/equation?tex=J(%5Cboldsymbol%7Bw%7D)%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5Em(f(%5Cboldsymbol%7Bx_i%7D)%20-%20y_i)%5E2)。 

求导时，只需要对多条训练样本的数据求和。

- ![](https://juejin.cn/equation?tex=J(%5Cboldsymbol%7Bw%7D)%20%3D%20%5Cfrac%7B1%7D%7B2%7D%20%5Clbrace%20(f(%5Cboldsymbol%7Bx_1%7D)%20-%20y_i)%5E2%20%2B%20%5Ccdots%20%2B%20(f(%5Cboldsymbol%7Bx_m%7D)%20-%20y_m)%5E2%20%5Crbrace)


- ![eq2][2]

由此，可以得出每个 wⱼ 的导数:

- ![](https://juejin.cn/equation?tex=w_j%20%3A%3D%20w_j%20-%20%5Calpha%20%5Csum%5Em_%7Bi%3D1%7D(f(%5Cboldsymbol%7Bx_%7Bi%7D%7D)-y_i)x_%7Bi%2Cj%7D)
    - 多个样本的梯度求和




[1]: https://juejin.cn/equation?tex=%5Cbegin%7Baligned%7D%0A%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7DJ(%5Cboldsymbol%7Bw%7D)%20%26%20%3D%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D%20%5Cfrac%20%2012(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%5E2%5C%5C%0A%26%20%3D%202%20%5Ccdot%5Cfrac%2012(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%5Ccdot%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D%20%20(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%20%5C%5C%0A%26%20%3D%20(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%5Ccdot%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D(%5Csum%5En_%7Bj%3D0%7D%20w_jx_%7Bi%2Cj%7D-y_i)%20%5C%5C%0A%26%20%3D%20(f(%5Cboldsymbol%7Bx_i%7D)-y_i)%20x_%7Bi%2Cj%7D%0A%5Cend%7Baligned%7D

[2]: https://juejin.cn/equation?tex=%5Cbegin%7Baligned%7D%0A%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7DJ(w)%20%26%20%3D%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D%20%5Cfrac%20%2012%5Clbrace%20(f(%5Cboldsymbol%7Bx_1%7D)%20-%20y_i)%5E2%20%2B%20%5Ccdots%20%2B%20(f(%5Cboldsymbol%7Bx_m%7D)%20-%20y_m)%5E2%20%5Crbrace%5C%5C%0A%26%20%3D%202%20%5Ccdot%5Cfrac%2012(f(%5Cboldsymbol%7Bx_1%7D)-y_1)%5Ccdot%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D%20%20(f(%5Cboldsymbol%7Bx_1%7D)-y_1)%20%2B%20%5Ccdots%5C%5C%0A%26%20%3D%20(f(%5Cboldsymbol%7Bx_1%7D)-y_1)%5Ccdot%20%5Cfrac%20%5Cpartial%20%7B%5Cpartial%20w_j%7D(%5Csum%5En_%7Bj%3D0%7D%20w_jx_%7B1%2Cj%7D-y_1)%20%2B%20%5Ccdots%20%5C%5C%0A%26%20%3D%20(f(%5Cboldsymbol%7Bx_1%7D)-y_1)%20x_%7B1%2Cj%7D%20%2B%20%5Ccdots%20%5C%5C%0A%26%20%3D%20%5Csum_%7Bi%3D1%7D%5Em(f(%5Cboldsymbol%7Bx_i%7D)%20-%20y_i)x_%7Bi%2Cj%7D%0A%5Cend%7Baligned%7D

