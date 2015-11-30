
    机器学习分类
        监督学习 Supervised Learning
            回归问题 Regression
            分类 Classification
        非监督学习 UnSupervised Learning
            聚类 cluster
            密度估计
            降维
    线性回归 Linear Regression
        Linear Regression with One Variabl)
        Parameter learning
            1. 梯度下降算法 Gradient descent
            2. 最小二乘法
        多元线性回归 Multivariate Linear Regression
            多元梯度下降
        梯度下降中的实用方法
            1: 特征缩放 feature scale
            2. 均值归一化 Mean normalization
            3. 确保算法正确工作
            4. α的选择
        特征的选择
        多项式回归 Polynomial regression
        

# 机器学习分类

## 监督学习 `Supervised Learning`

'right answer' given

训练集 都有相应的正确答应，算法基于这些答案作预测。

机器学习可以处理 无数多个特征


### 回归问题 `Regression`

Predict continuous valued output(price)

### 分类  `Classification`

Discrete valued output ( example : 0 or 1  ...)


## 非监督学习 `UnSupervised Learning`

训练数据包含 `不带有目标值`的输入向量x。

### 聚类  cluster

根据数据发现样本中相似的群组——聚类

### 密度估计

在输入空间中判定数据的分布——密度估计

### 降维

把数据从高维空间转换到低维空间以用于可视化

---

# 线性回归 `Linear Regression`

## Linear Regression with One Variable

一些符号:

```
m  训练集 样本数量
x  input / feature
y  output / target 

(x,y) 表示一个训练样本
(xⁱ,yⁱ) 表示训练集合中的 第i个 训练样本
```


h 是 预测算法

对于线性回归, hypothesis公式:
```
h(xⁱ)=Θ₀ + Θ₁xⁱ
```
令：

```
J(Θ₀,Θ₁) = 1/(2*m) * ∑(h(xⁱ)-yⁱ)²
```

`J(Θ₀,Θ₁)` 称为代价函数 `cost function` ， 也称为平方误差函数 `square error function` 


 - 前面乘上的1/2是为了求导的时候，使常数系数消失
 - 回归算法的目标就变为了 调整θ使得代价函数 `J(θ)` 取得最小值
 - 方法有梯度下降法，最小二乘法等

## Parameter learning

几种使 使代价函数 `J(Θ₀,Θ₁)` 最小化的办法:


### 1. 梯度下降算法 Gradient descent

梯度下降算法 可以用来处理多个 输入 feature, 为了简便，下面只介绍 `Θ₀,Θ₁` 的情况

`算法描述`:

 - start with some `Θ₀,Θ₁`, 从某个初始值出发
 - keep changing `Θ₀,Θ₁` to reduce `J(Θ₀,Θ₁)`, 直到我们找到J的最小值，或许是局部最小值。

`解释`:

`J(Θ₀,Θ₁)` 的 图是一张3维图像，可以想象成是一座山。

算法的第一步，就是假设你在山上某个位置。

算法的第二步，你为了尽快下山，向下移动了一步。

重复，直到到达局部最低点。

    PS: 就像有不同的下山路线 和出口,
    不同的初始位置，梯度下降算法会得到不同的局部最优解

`代码`:

```
repeate until convergence  { //直到收敛
    Θⱼ = Θⱼ - α ( ∂/∂θ₀ )J(Θ₀,Θ₁)   (for j=0 and j=1)
}

//具体执行时，必须同步更新Θ：
repeate until convergence  { //直到收敛
    temp0 = Θ₀ - α ( ∂/∂θ₀ )J(Θ₀,Θ₁)
    temp1 = Θ₁ - α ( ∂/∂θ₁ )J(Θ₀,Θ₁)
    Θ₀ = temp0  // 同步计算完 所有Θ的新值后
    Θ₁ = temp1  // 才能更新Θ自身 
}
```

![](http://latex.codecogs.com/gif.latex?%5Ctheta_j%20%3A%3D%20%5Ctheta_j%20-%20%5Calpha%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5Ccdot%20x_%7Bj%7D%5E%7B%28i%29%7D)

![](http://latex.codecogs.com/gif.latex?%5Ctheta%3A%3D%5Ctheta-%5Calpha%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%5B%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5Ccdot%20x%5E%7B%28i%29%7D%20%5D)


说明：

 - α是学习速率 learning rate, 决定了我们下山的步子有多大
 - Θ必须同步更新，即分别计算出temp后,才能更新Θ,避免Θ₀先一步更新后，影响到Θ₁的计算
 - 梯度方向由`J(θ)`对θ 的偏导数决定, 也就是 学习速率`α` 后面的部分,    也就是J曲线在`Θᵢ`点的切线斜率
 - `J(θ)`的偏导数部分计算公式:
   `(∂/∂θⱼ)J(Θ₀,Θ₁)= 1/(m) * ∑[(h(xⁱ)-yⁱ) * xⁱ] ` ( j==0的情况, xⁱ = 1 )
 - 这里Θ每次更新，J 都要对所有的样本进行计算，这种也叫"批量"梯度下降
 - 这样的更新规则称为`LMS update rule`（least mean squares）
 - 每一次迭代都考察训练集的所有样本，而称为批量梯度下降`batch gradient descent`
 - 按照单个训练样本更新θ的值，称为随机梯度下降 `stochastic gradient descent`
   对于较大的数据集，一般采用效率较高的随机梯度下降法
 - TODO
 - TODO
 
### 2. 最小二乘法

令:

![](http://latex.codecogs.com/gif.latex?x%3D%5Cbegin%7Bbmatrix%7Dx_%7B0%7D%20%5C%5C%20x_%7B1%7D%20%5C%5C%20x_%7B2%7D%20%5C%5C%20...%20%5C%5C%20x_%7Bn%7D%20%5Cend%7Bbmatrix%7D%20%2C%20X%3D%5Cbegin%7Bbmatrix%7D-x%5E%7B1T%7D-%20%5C%5C%20-x%5E%7B2T%7D-%20%5C%5C%20...%20%5C%5C%20-x%5E%7BmT%7D-%20%5Cend%7Bbmatrix%7D%20%2C%20y%3D%5Cbegin%7Bbmatrix%7Dy%5E%7B1%7D%20%5C%5C%20y%5E%7B2%7D%20%5C%5C%20...%20%5C%5C%20y%5E%7Bm%7D%20%5Cend%7Bbmatrix%7D)

    m是训练样本的数量，每个x 包含了n个样本feature值，外加一个1,对应Θ₀, x转置后变为X中的行。
    

由解投影矩阵的公式:

```
ẋ = (AᵀA)⁻¹ Aᵀb
```

可得Θ解为:

```
Θ = (XᵀX)⁻¹ Xᵀy
```

`说明`:

 - 最小二乘法求解Θ, 不需要关心 变量归一化 feature scaling
 - 当n很大时, 比如n=10000，最小二乘法会很慢
 - 逻辑回归这类更复杂的算法，无法使用正规方程法

## 多元线性回归 Multivariate Linear Regression

符号改进:

```
n  feature 的数量
m  训练集 样本数量
x  input / feature
y  output / target 

xⁱ  表示训练集合中的 第i个 训练样本的 feature 向量
xⁱⱼ 第i个 训练样本的 第j个 feature 值 
```

hypothesis公式:

```
h(x)= Θ₀x₀ + Θ₁x₁ + Θ₂x₂ + ... + Θⱼxⱼ       (x₀=1)
```

令:

![](http://latex.codecogs.com/gif.latex?X%3D%5Cbegin%7Bbmatrix%7Dx_%7B0%7D%20%5C%5C%20x_%7B1%7D%20%5C%5C%20...%20%5C%5C%20x_%7Bn%7D%20%5Cend%7Bbmatrix%7D%20%5Ctheta%20%3D%20%5Cbegin%7Bbmatrix%7D%5Ctheta_%7B0%7D%20%5C%5C%20%5Ctheta_%7B1%7D%20%5C%5C%20...%20%5C%5C%20%5Ctheta_%7Bn%7D%20%5Cend%7Bbmatrix%7D)

h 就可以写成
```
h(x)= ΘᵀX   (行 x 列) 
```

### 多元梯度下降

```
Θ₀ = Θ₀ - α* 1/(m) * ∑(h(xⁱ)-yⁱ) * xⁱ₀
Θ₁ = Θ₁ - α* 1/(m) * ∑(h(xⁱ)-yⁱ) * xⁱ₁
Θ₂ = Θ₂ - α* 1/(m) * ∑(h(xⁱ)-yⁱ) * xⁱ₂
...
```

## 梯度下降中的实用方法 

### 1: 特征缩放 `feature scale`

`使每个特征feature的值都位于 [-1,1] 区间，以便梯度下降算法更快的收敛`

 `[-1,1] 并不是必须的，[-3,3],[-0.33,0.33]都是可以接受的，算法也能较快的收敛。`

以房屋价格为例:

现在有两个feature

 - x₁ = size ( 0-2000 feets )
 - x₂ = number of bedrooms (1-5)

由于 x₁, x₂取值范围相差太大，J 的轮廓图会以`狭长的椭圆形`呈现。

这会导致 梯度下降算法收敛的过慢。

如果我们把对 x₁, x₂ 做一下调整

 - x₁ = size/2000
 - x₂ = number of bedrooms /5

这样 x₁, x₂ 取值范围就在 0<= x <=1 之间。J 的轮廓图就是一个个`圆形`，

这种情况下，梯度下降算法 就会更快的收敛。


### 2. 均值归一化  Mean normalization

除了上面的 除以 最大值的做法, 也会采用 均值归一化的做法，使取值以0为均值

```
x = (feature-value - avg ) / range
```

这里, avg 是 feature的平均值 , range = max - min
 
对 x₁, x₂ 做调整:

 - x₁ = (size-1000)/2000
 - x₂ = (#bedrooms -2) /5

取值范围变为:

-0.5 <= x <= 0.5

    注意： 不要对 Θ₀ 做 feature scale 处理


### 3. 确保算法正确工作

画出 并观察 `x:迭代次数 , y:J(Θ)` 的 图像

如果算法工作不正确，可该用 较小的 `α` , 但注意不要过小

### 4. `α`的选择

尝试一系列值, ..., 0.001, 0.01, 0.1, 1 , ... , 找到一个合适的


## 特征的选择

还是房屋售价的例子, 假设有一组样本数据，记录的房屋的宽frontage 和深 depth

我们可以这样写 假设函数:

```
h(x)= Θ₀ + Θ₁ frontage + Θ₂ depth
```
因为 frontage x depth 正好是房屋的面积，所以我们也可以这样写 假设函数:
```
h(x)= Θ₀ + Θ₁ area
```

## 多项式回归 Polynomial regression

房屋size 和 price之间的关系，用 线性回归可能拟合的不是很好。

有时候，你希望使用 2次多项式来拟合:
```
h(x)= Θ₀ + Θ₁x + Θ₂x²
```

或者3次多项式：
```
h(x)= Θ₀ + Θ₁x + Θ₂x² + Θ₃x³
```

    注意：这里 x², x³ 是指 square 和 cube，不是第几个样本的意思


这种情况，我们可以令:

 - x1 = (size)
 - x2 = (size)²
 - x3 = (size)³

这样就可以用线性回归的算法来达到 多项式回归的效果

```
h(x)= Θ₀x₀ + Θ₁x₁ + Θ₂x₂ + Θ₃x₃  //这时，更要注意 均值归一化处理
```

2次多项式可以拟合出一条曲线，但是2次多项式有可能出现下降，

有时也可以考虑使用  开方
```
h(x)= Θ₀x₀ + Θ₁x₁ + Θ₂√x₂  // 不会出现下降
```

# 线性回归一般流程

```
%======================================
function plotData(x, y)
	plot(x, y, 'rx', 'MarkerSize', 10); % Plot the data 
	ylabel('Profit in $10,000s'); % Set the y−axis label 
	xlabel('Population of City in 10,000s'); % Set the x−axis label
end


function J = computeCost(X, y, theta)
	m = length(y); % number of training examples

	predictions = X*theta ;  % all h(x) 矩阵（向量）
	%sqrErrors = (predictions-y).^2 ;   
	%J= 1/(2*m) * sum( sqrErrors ) ; 
	
	%等价
	cost = (predictions-y)' * (predictions-y) ;   
	J= 1/(2*m) * cost ; 
end
```

---
梯度下降笨算法:
```
function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
	m = length(y); % number of training examples
	J_history = zeros(num_iters, 1);


	for iter = 1:num_iters

	    t1 = 0;
	    t2 = 0;
	    for i= 1:m
	        t1 = t1 + (X(i,:) * theta -y(i))*X(i,1);
	        t2 = t2 + (X(i,:) * theta -y(i))*X(i,2);
	    end
	    theta(1) = theta(1) - alpha* 1/m *t1;
	    theta(2) = theta(2) - alpha* 1/m *t2;
	
	    % Save the cost J in every iteration    
	    J_history(iter) = computeCost(X, y, theta);
	end

end
```

梯度下降 向量化算法1 :

```
function [theta, J_history] = gradientDescent1(X, y, theta, alpha, num_iters)
	m = length(y); % number of training examples
	J_history = zeros(num_iters, 1);


	for iter = 1:num_iters
	    % 注意：因为 A'*B 等价于 sum(A.*B), 所以这里不再需要 sum
	    theta = theta - alpha *1/m *( (X * theta - y )' * X  )';
	
	    % Save the cost J in every iteration    
	    J_history(iter) = computeCost(X, y, theta);
	end

end
```

梯度下降 向量化算法2 :

```
function [theta, J_history] = gradientDescent2(X, y, theta, alpha, num_iters)
	m = length(y); % number of training examples
	J_history = zeros(num_iters, 1);


	for iter = 1:num_iters
	    theta = theta - alpha *1/m *sum( (X * theta - y ) .* X  )';
	
	    % Save the cost J in every iteration    
	    J_history(iter) = computeCost(X, y, theta);
	end

end
```

---
```
%% =================== Part 2: Plotting ===================

data = load('ex1/ex1data1.txt'); % 装载训练集
X = data(:, 1); y = data(:, 2);  % 抽取 input / target
m = length(y); % number of training examples


% 可视化训练集
setenv("GNUTERM","qt")
plotData(X, y);

%% =================== Part 3: Gradient descent ===================

X = [ones(m, 1), data(:,1)]; % X 增加一列 1到左边，对应 x0
theta = zeros(2, 1); % initialize fitting parameters

% Some gradient descent settings
iterations = 1500;	% 梯度下降迭代步数
alpha = 0.01;  % alpha 初始值

computeCost(X, y, theta)  % 计算初始 J 值

% 执行梯度下降算法
theta = gradientDescent(X, y, theta, alpha, iterations);

%最小2乘法
% theta = pinv(X'*X)*X'*y      % 最小2乘法

% 画出拟合的曲线
hold on; % keep previous plot visible
plot(X(:,2), X*theta, '-')
legend('Training data', 'Linear regression')
hold off % don't overlay any more plots on this figure

```

---
debug:

```
%% ============= Part 4: Visualizing J(theta_0, theta_1) =============
% Grid over which we will calculate J
theta0_vals = linspace(-10, 10, 100);
theta1_vals = linspace(-1, 4, 100);

% initialize J_vals to a matrix of 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals));

% Fill out J_vals
for i = 1:length(theta0_vals)
    for j = 1:length(theta1_vals)
	  t = [theta0_vals(i); theta1_vals(j)];    
	  J_vals(i,j) = computeCost(X, y, t);
    end
end

% 画三维图
% Because of the way meshgrids work in the surf command, we need to 
% transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals';
% Surface plot
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0'); ylabel('\theta_1');


% 画轮廓线
figure;
% Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0'); ylabel('\theta_1');
% 画 theta 最终收敛的坐标
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);

```

##### feature normalize

```
function [X_norm, mu, sigma] = featureNormalize(X)

mu = mean( X )
sigma = std( X )
X_norm = (X_norm-mu)./sigma   % 注意，不是矩阵除法，是点除

end
```

