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

![][1]


右边的求和项，就是正则化项，参数λ 称为正则化参数, λ作用是在两个'求和'目标之间控制一个平衡关系。

注意，正则化项的j 是从1开始的，正则化并不处理Θ₀ .

但是如果 λ的值过大, 比如10¹⁰, 会导致大部分的Θⱼ接近0, 假设函数就近似h(x)=Θ₀, 从而导致欠拟合 `underfitting`.


# 正则化线性回归

### 代价函数:

![][1]

### 梯度下降算法:

我们把 梯度下降算法拆成两部分

  1. 对于 Θ₀ , 迭代算法和 梯度下降算法一样
  2. 对于有 正则化项 参数 , Θ [1,n]  

我们在 线性梯度下降基础上右边加上一项

![][3]

化简一下:

![][2]

可以看到，跟 最新的线性回归算法相比， 正则化迭代算法 只是每次迭代，Θⱼ 会略微变小

### 正规方程组解法

if λ > 0 ,

![](http://latex.codecogs.com/gif.latex?%5Ctheta%3D%5Cleft%20%28%20X%5ETX&plus;%5Clambda%5Cbegin%7Bbmatrix%7D%200%20%26%20%26%20%26%20%5C%5C%20%26%201%20%26%20%26%20%5C%5C%20%26%20%26%20...%20%26%20%5C%5C%20%26%20%26%20%26%201%20%5Cend%7Bbmatrix%7D%20%5Cright%20%29%5E%7B-1%7DX%5ETy)



# 正则化 逻辑回归

### 代价函数

和 正则化线性回归 代价函数的处理一样，

正则化逻辑回归代价函数, 也是在 逻辑回归代价函数基础上，加上 正则化项:

![](http://latex.codecogs.com/gif.latex?&plus;%20%5Cfrac%7B%5Clambda%7D%7B2m%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Ctheta_j%5E2)


### 梯度下降算法

和 正则化线性回归梯度下降算法一致，仅仅是 假设函数h(x) 的不同

Θ₀ 无正则化处理

Θ [1,n]  :

![][3]

![][2]

# 正则化处理流程

##### 特征映射 feature mapping

```
function out = mapFeature(X1, X2)
	% MAPFEATURE Feature mapping function to polynomial features
	%
	%   MAPFEATURE(X1, X2) maps the two input features
	%   to quadratic features used in the regularization exercise.
	%
	%   Returns a new feature array with more features, comprising of 
	%   X1, X2, X1.^2, X2.^2, X1*X2, X1*X2.^2, etc..
	%
	%   Inputs X1, X2 must be the same size
	%

	% 当 x1 幂为0时, x2 幂可以为 0-6 ，7 种组合， 其中 (0,0) 组合就是 x0
	% 当 x1 幂为1时, x2 幂可以为 0-5 ，6 种组合
	% 当 x1 幂为6时, x2 幂可以为 0   ，1 种组合

	% 所以，最终有 1＋2+3+4+5+6+7 ＝ 28 个 feature 

	degree = 6;  % 最高 6 次方项
	out = ones(size(X1(:,1)));  % 没必要吧，ones(size(X1)) 也一样
	for i = 1:degree
	    for j = 0:i
	        out(:, end+1) = (X1.^(i-j)).*(X2.^j);   % 这里，end是什么用法？
	    end
	end

end
```

##### 代价函数，和梯度

```
```

##### 一般流程
```
data = load('ex2data2.txt');
X = data(:, [1, 2]); y = data(:, 3);

% Note that mapFeature also adds a column of ones for us
X = mapFeature(X(:,1), X(:,2));
```

---
---

  [1]: http://latex.codecogs.com/gif.latex?J%28%5Ctheta%29%3D%5Cfrac%7B1%7D%7B2m%7D%5Cleft%20%5B%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5E2&plus;%5Clambda%20%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Ctheta_%7Bj%7D%5E%7B2%7D%20%5Cright%20%5D
  
  
  [2]: http://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3A%3D%20%5Ctheta_j%281-%5Calpha%5Cfrac%7B%5Clambda%7D%7Bm%7D%29%20-%20%5Calpha%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29x%5E%7B%28i%29%7D_j
  
  [3]: http://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3A%3D%20%5Ctheta_j%20-%20%5Calpha%5Cleft%20%5B%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29x%5E%7B%28i%29%7D_j%20&plus;%5Cfrac%7B%5Clambda%20%7D%7Bm%7D%5Ctheta_j%20%5Cright%20%5D
  
