[TOC]

# 过度拟合 overfitting

如果有太多的feature，假设函数可能会很好的拟合训练集数据，
却无法正确的预测新的数据。

解决过拟合的办法:

 - 减少feature数量: 手动或使用模型选择算法 来选择保留的feature, 但是这样有可能丢失一些信息
 - 正则化 Regularization: 保留所有feature, 但是降低某些feature(和最终预测关联度比较小的) Θⱼ参数的重要性/值 ( 适合有很多feature,每个feature都对预测起一点作用的场合)。



# 正则化 Regularization

通过降低某些feature Θⱼ参数的值 ，正则化可以得到更简单的假设图像，不容易出现过拟合。

## 正则化 代价函数  Regularization Cost Function

![](http://latex.codecogs.com/gif.latex?J%28%5Ctheta%29%3D%5Cfrac%7B1%7D%7B2m%7D%5Cleft%20%5B%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5E2&plus;%5Clambda%20%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Ctheta_%7Bj%7D%5E%7B2%7D%20%5Cright%20%5D)


