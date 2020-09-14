...menustart

- [过度拟合 overfitting](#6129858f4f4ae385452b94ae0589e3c2)
- [正则化 Regularization](#36360bac2874c6fa4fbebdc1731c80f6)
    - [线性回归的例子:](#60a340b4fe60aaefadfb4199d44edda3)
- [正则化线性回归](#ec1dbd4eccae79c7bc2091316de35224)
    - [代价函数:](#73db361f556832cf91d56357c8203949)
    - [梯度下降算法:](#21acf0b2bd3a8d644af69fb6d0f63733)
    - [正规方程组解法](#62dc9889b8e1aeda5b4dc46f7665acf6)
- [正则化 逻辑回归](#d79c5efa3a07a2273edafc98c34fb708)
    - [代价函数](#287340d512ad4b09754b4574719e412f)
    - [梯度下降算法](#f072832c961b0762dbec1d78e5504442)
- [正则化处理流程](#c87d57915b8ec0bd3094315644b4794f)
    - [特征映射 feature mapping](#da4ad33e42cddccf3cc687f937bdfc06)
    - [代价函数，和梯度](#d4bb0a33bce7e76d7df296d1f45f3a3d)
    - [一般流程](#869492f5afdb7e6bc022701f149b2c48)

...menuend


<h2 id="6129858f4f4ae385452b94ae0589e3c2"></h2>


# 过度拟合 overfitting

如果有太多的feature，假设函数可能会很好的拟合训练集数据，
却无法正确的预测新的数据。

解决过拟合的办法:

 - 减少feature数量: 手动或使用模型选择算法 来选择保留的feature, 但是这样有可能丢失一些信息
 - 正则化 Regularization: 保留所有feature, 但是降低某些feature(和最终预测关联度比较小的) θⱼ参数的重要性/值 ( 适合有很多feature,每个feature都对预测起一点作用的场合)。



<h2 id="36360bac2874c6fa4fbebdc1731c80f6"></h2>


# 正则化 Regularization

通过降低某些feature θⱼ参数的值 ，正则化可以得到更简单的假设图像，不容易出现过拟合。

<h2 id="60a340b4fe60aaefadfb4199d44edda3"></h2>


## 线性回归的例子:

![][1]


右边的求和项，就是正则化项，参数λ 称为正则化参数, λ作用是在两个'求和'目标之间控制一个平衡关系。

注意，正则化项的j 是从1开始的，正则化并不处理θ₀ .

但是如果 λ的值过大, 比如10¹⁰, 会导致大部分的θⱼ接近0, 假设函数就近似h(x)=θ₀, 从而导致欠拟合 `underfitting`.


<h2 id="ec1dbd4eccae79c7bc2091316de35224"></h2>


# 正则化线性回归

<h2 id="73db361f556832cf91d56357c8203949"></h2>


### 代价函数:

![][1]

<h2 id="21acf0b2bd3a8d644af69fb6d0f63733"></h2>


### 梯度下降算法:

我们把 梯度下降算法拆成两部分

  1. 对于 θ₀ , 迭代算法和 梯度下降算法一样
  2. 对于有 正则化项 参数 , θ [1,n]  

我们在 线性梯度下降基础上右边加上一项

![][3]

化简一下:

![][2]

可以看到，跟 最新的线性回归算法相比， 正则化迭代算法 只是每次迭代，θⱼ 会略微变小

<h2 id="62dc9889b8e1aeda5b4dc46f7665acf6"></h2>


### 正规方程组解法

if λ > 0 ,

![](http://latex.codecogs.com/gif.latex?%5Ctheta%3D%5Cleft%20%28%20X%5ETX&plus;%5Clambda%5Cbegin%7Bbmatrix%7D%200%20%26%20%26%20%26%20%5C%5C%20%26%201%20%26%20%26%20%5C%5C%20%26%20%26%20...%20%26%20%5C%5C%20%26%20%26%20%26%201%20%5Cend%7Bbmatrix%7D%20%5Cright%20%29%5E%7B-1%7DX%5ETy)



<h2 id="d79c5efa3a07a2273edafc98c34fb708"></h2>


# 正则化 逻辑回归

<h2 id="287340d512ad4b09754b4574719e412f"></h2>


### 代价函数

和 正则化线性回归 代价函数的处理一样，

正则化逻辑回归代价函数, 也是在 逻辑回归代价函数基础上，加上 正则化项:

![](http://latex.codecogs.com/gif.latex?&plus;%20%5Cfrac%7B%5Clambda%7D%7B2m%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Ctheta_j%5E2)

![](../imgs/logistical_regression_cost.png)

<h2 id="f072832c961b0762dbec1d78e5504442"></h2>


### 梯度下降算法

和 正则化线性回归梯度下降算法一致，仅仅是 假设函数h(x) 的不同

θ₀ 无正则化处理

θ [1,n]  :

![][3]

![][2]

<h2 id="c87d57915b8ec0bd3094315644b4794f"></h2>


# 正则化处理流程

<h2 id="da4ad33e42cddccf3cc687f937bdfc06"></h2>


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

<h2 id="d4bb0a33bce7e76d7df296d1f45f3a3d"></h2>


##### 代价函数，和梯度

```
function [J, grad] = costFunctionReg(theta, X, y, lambda)
    % Initialize some useful values
    m = length(y); % number of training examples

    % You need to return the following variables correctly 
    J = 0;
    grad = zeros(size(theta));


    hx = sigmoid( X * theta );
    % 添加了 正则化部分
    J= 1/m * sum(  -y .* log( hx )  - ( 1-y ) .* log( 1- hx ) )  + lambda/(2*m )* ( theta' * theta ) ;      
    % 处理 feature 0 case
    J -= lambda/(2*m )* ( theta(1)^2 ) ;

    % 另一种处理 feature 0 case 的做法
    % 必须先计算出 grad0 并保存， 因为需要同步更新
    grad0   = 1/m *sum( ( hx - y ) .* X(:,1)  )'  ; % grad0 不正则化

    grad    = 1/m *sum( ( hx - y ) .* X  )' +  lambda/(m )*  theta ;     % 添加了 正则化部分
    grad(1) = grad0 ;

    % =============================================================
end
```

<h2 id="869492f5afdb7e6bc022701f149b2c48"></h2>


##### 一般流程

`注意: λ取值过大,对参数惩罚过大,会导致欠拟合, 取值过小, 会过拟合`

```
data = load('ex2data2.txt');
X = data(:, [1, 2]); y = data(:, 3);

% Note that mapFeature also adds a column of ones for us
X = mapFeature(X(:,1), X(:,2));

% Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1);

% Set regularization parameter lambda to 1
lambda = 1;

[cost, grad] = costFunctionReg(initial_theta, X, y, lambda);


%% ============= Part 2: Regularization and Accuracies =============

% Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1);

% Set regularization parameter lambda to 1 (you should vary this)
lambda = 1;


% Set Options
options = optimset('GradObj', 'on', 'MaxIter', 400);

% Optimize
[theta, J, exit_flag] = ...
    fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);


% 预测
% Compute accuracy on our training set
p = predict(theta, X);
```

---
---

  [1]: http://latex.codecogs.com/gif.latex?J%28%5Ctheta%29%3D%5Cfrac%7B1%7D%7B2m%7D%5Cleft%20%5B%20%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5E2&plus;%5Clambda%20%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Ctheta_%7Bj%7D%5E%7B2%7D%20%5Cright%20%5D
  
  
  [2]: http://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3A%3D%20%5Ctheta_j%281-%5Calpha%5Cfrac%7B%5Clambda%7D%7Bm%7D%29%20-%20%5Calpha%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29x%5E%7B%28i%29%7D_j
  
  [3]: http://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3A%3D%20%5Ctheta_j%20-%20%5Calpha%5Cleft%20%5B%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5Em%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29x%5E%7B%28i%29%7D_j%20&plus;%5Cfrac%7B%5Clambda%20%7D%7Bm%7D%5Ctheta_j%20%5Cright%20%5D
  
