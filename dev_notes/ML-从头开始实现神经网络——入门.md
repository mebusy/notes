...menustart

 * [从头开始实现神经网络——入门](#a8e5e4ff9eab1384c83defd779a4b42a)
   * [产生数据集](#0c441b14781795af30c7ef9735a71b26)
 * [Package imports](#a5a2c9865655969a15f7320480aec481)
 * [Display plots inline and change default figure size](#8c0e9796e71090b880a14b3df2d6ef71)
 * [used for ipython](#47e07eed97ae9cf07d261e6a257995f1)
 * [%matplotlib inline](#05f65ed01981987163a8125a0283a7ab)
 * [Generate a dataset and plot it](#72dcd42ec73308334057a9fb6dd8084c)
   * [Logistic回归](#41b46dfc0b86b27a24f2fd0859601f9f)
 * [Helper function to plot a decision boundary.](#7c7c86a227a26b95d19624da9530d86f)
 * [If you don't fully understand this function don't worry, it just generates the contour plot below.](#5a3c539b11b0de8bde1d2c664f561fd1)
 * [Plot the decision boundary](#fa8b9079f938129811351dc2da540938)
   * [训练神经网络](#67fd927dbbde24e0a4e33a49821346bd)
   * [神经网络如何预测](#6a77b6aadd74cd5dfaed1b5a42d06268)
       * [学习参数](#8a98c75bcbb92feb6675bfa9f7554e68)
       * [实现](#38164c8be942882c3e6c233dfc8087ab)
 * [Gradient descent parameters (I picked these by hand)](#8918c18069d3e2d37825c7a0aa9b8ad7)
 * [Helper function to evaluate the total loss on the dataset](#24dadccd15c89a6bcae3ea31e48b04e1)
 * [Helper function to predict an output (0 or 1)](#3d9b2c51cec46ad99f068f3509c50516)
 * [This function learns parameters for the neural network and returns the model.](#f16f2ee97812ff64f3412a39df93472f)
 * [- nn_hdim: Number of nodes in the hidden layer](#64c89f28e85aa9c9b9cd26d7b2c64037)
 * [- num_passes: Number of passes through the training data for gradient descent](#0413112b5c54316c374670810c17b0ec)
 * [- print_loss: If True, print the loss every 1000 iterations](#52985252a6929bd0b68f7ab8faaa60b7)
   * [隐藏层规模为3的神经网络](#9a19b3c2ae83b808232d7a6d84bd9643)
 * [Build a model with a 3-dimensional hidden layer](#ee776fa8de8791678d3bf348c3d72738)
 * [Plot the decision boundary](#fa8b9079f938129811351dc2da540938)
   * [变换隐藏层的规模](#8f3bd9e9a60d3826fd71b039c4861df3)

...menuend


<h2 id="a8e5e4ff9eab1384c83defd779a4b42a"></h2>
#从头开始实现神经网络——入门

在接下来的文章中，我会探索如何使用Theano写一个高效的神经网络实现。 

<h2 id="0c441b14781795af30c7ef9735a71b26"></h2>
## 产生数据集
scikit-learn提供了一些很有用的数据集产生器，所以我们不需要自己写代码了。 
我们将从make_moons 函数开始。 

    sklearn.datasets.make_moons(n_samples=100, shuffle=True, noise=None, random_state=None) 

    Parameters:	
        n_samples : int, optional (default=100)		
                    The total number of points generated.
        shuffle : bool, optional (default=True)		
                    Whether to shuffle the samples.
        noise : double or None (default=None)		
                Standard deviation of Gaussian noise added to the data.
    Returns:	
        X : array of shape [n_samples, 2]		
            The generated samples.
        y : array of shape [n_samples]			
            The integer labels (0 or 1) for class membership of each sample.

代码:
```python
<h2 id="a5a2c9865655969a15f7320480aec481"></h2>
# Package imports
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib

<h2 id="8c0e9796e71090b880a14b3df2d6ef71"></h2>
# Display plots inline and change default figure size
<h2 id="47e07eed97ae9cf07d261e6a257995f1"></h2>
# used for ipython
<h2 id="05f65ed01981987163a8125a0283a7ab"></h2>
#%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)
<h2 id="72dcd42ec73308334057a9fb6dd8084c"></h2>
# Generate a dataset and plot it
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)

"""
s   : point size ^2
c   : color 
cmap: A Colormap instance or registered name. cmap is only used if c is an array of floats. 
      If None, defaults to rc image.cmap.
"""
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)

plt.show()
```

![](http://ww1.sinaimg.cn/mw690/6941baebgw1ew6gz74sg6j20gu0dbt9v.jpg)

产生的数据集中有两类数据，分别以红点和蓝点表示。你可以把蓝点看作是男性病人，红点看作是女性病人，x和y轴表示药物治疗。
我们的目标是，在给定x和y轴的情况下训练机器学习分类器以预测正确的分类（男女分类）
注意，数据并不是线性可分的，我们不能直接画一条直线以区分这两类数据。
这意味着线性分类器，比如Logistic回归，将不适用于这个数据集，除非手动构建在给定数据集表现很好的非线性特征（比如多项式）。   

事实上，这也是神经网络的主要优势。你不用担心特征构建，神经网络的隐藏层会为你学习特征。 
  
<h2 id="41b46dfc0b86b27a24f2fd0859601f9f"></h2>
##Logistic回归

为了证明这个观点，我们来训练一个Logistic回归分类器。它的输入是x和y轴的值，输出预测的分类（0或1）。 
为了简单，我们使用scikit-learn库里的Logistic回归类。 

```python
<h2 id="7c7c86a227a26b95d19624da9530d86f"></h2>
# Helper function to plot a decision boundary.
<h2 id="5a3c539b11b0de8bde1d2c664f561fd1"></h2>
# If you don't fully understand this function don't worry, it just generates the contour plot below.
def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    
<h2 id="fa8b9079f938129811351dc2da540938"></h2>
# Plot the decision boundary
plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")
plt.show()
```

![](http://ww1.sinaimg.cn/mw690/6941baebjw1ew6gxgqoncj20gm0dlgmy.jpg)

上图展示了Logistic回归分类器学习到的决策边界。  
使用一条直线尽量将数据分离开来，但它并不能捕捉到数据的“月形”特征。 

<h2 id="67fd927dbbde24e0a4e33a49821346bd"></h2>
##训练神经网络
让我们来建立具有一个输入层、一个隐藏层、一个输出层的三层神经网络。
输入层的结点数由数据维度决定，这里是2维。类似地，输出层的结点数由类别数决定，也是2。
（因为我们只有两类输出，实际中我们会避免只使用一个输出结点预测0和1，而是使用两个输出结点以使网络以后能很容易地扩展到更多类别）。
网络的输入是x和y坐标，输出是概率，一个是0（女性）的概率，一个是1（男性）的概率。它看起来像下面这样：

![](http://ww2.sinaimg.cn/mw690/6941baebjw1ew6gxgflxhj20sg0j9416.jpg)

我们可以为隐藏层选择维度（结点数）。
放入隐藏层的结点越多，我们能训练的函数就越复杂。但是维度过高也是有代价的。
首先，预测和学习网络的参数就需要更多的计算。参数越多就意味着我们可能会过度拟合数据。 

如何选择隐藏层的规模？  
尽管有一些通用的指导和建议，但还是依赖于具体问题具体分析，与其说它是一门科学不如说是一门艺术。我们稍后会在隐藏层的结点数上多做一点事情，然后看看它会对输出有什么影响。

我们还需要为隐藏层挑选一个激活函数。 
激活函数将该层的输入转换为输出。一个非线性激活函数允许我们拟合非线性假设。 
常用的激活函数有tanh、the sigmoid函数或者是ReLUs。 
这里我们选择使用在很多场景下都能表现很好的tanh函数。 
这些函数的一个优点是它们的导数可以使用原函数值计算出来。 
例如，tanh x的导数是1-tanh^2 x。这个特性是很有用的，它使得我们只需要计算一次tanh x值，之后只需要重复使用这个值就可以得到导数值。

因为我们想要得到神经网络输出概率，所以输出层的激活函数就要是softmax。 
这是一种将原始分数转换为概率的方法。如果你很熟悉logistic回归，可以把softmax看作是它在多类别上的一般化。 
    softmax: 1.用于分类   2.待分类的数量类别数量大于2（等于2也适用）

<h2 id="6a77b6aadd74cd5dfaed1b5a42d06268"></h2>
##神经网络如何预测
神经网络使用前向传播进行预测。 
前向传播只不过是一堆矩阵相乘并使用我们上面定义的激活函数了。 
假如x是该网络的2维输入，我们将按如下计算预测值（也是二维的）:

![](http://ww4.sinaimg.cn/mw690/6941baebjw1ew6gxg04dkj204502f746.jpg)

zi是输入层、ai是输出层。W1,b1,W2,b2是需要从训练数据中学习的网络参数。 
你可以把它们看作是神经网络各层之间数据转换矩阵。看着上文的矩阵相乘，我们可以计算出这些矩阵的维度。如果我们的隐藏层中使用500个结点，那么有

![](http://ww1.sinaimg.cn/mw690/6941baebgw1ew6h1psaxkj208q00lq2s.jpg)

现在你明白了为什么增大隐藏层的规模会导致需要训练更多参数。 

<h2 id="8a98c75bcbb92feb6675bfa9f7554e68"></h2>
####学习参数
学习该网络的参数意味着要找到使训练集上错误率最小化的参数(W1,b1,W2,b2)。
但是如何定义错误率呢？ 
我们把衡量错误率的函数叫做损失函数（loss function）。 
输出层为softmax时多会选择交叉熵损失（cross-entropy loss）。 
假如我们有N个训练例子和C个分类，那么预测值（hat{y}）相对真实标签值的损失就由下列公式给出：

![](http://ww4.sinaimg.cn/mw690/6941baebjw1ew6gxfmjqgj206e018a9w.jpg)

这个公式看起来很复杂，但实际上它所做的事情不过是把所有训练例子求和，然后加上预测值错误的损失。 
所以，hat{y}（预测值）距离 hat{y}（真实标签值）越远，损失值就越大。 

要记住，我们的目标是找到能最小化损失函数的参数值。 
我们可以使用梯度下降方法找到最小值。我会实现梯度下降的一种最普通的版本，也叫做有固定学习速率的批量梯度下降法。诸如SGD（随机梯度下降）或minibatch梯度下降通常在实践中有更好的表现。 
所以，如果你是认真的，这些可能才是你的选择，最好还能逐步衰减学习率。

作为输入，梯度下降需要一个与参数相关的损失函数的梯度（导数矢量）：

![](http://ww3.sinaimg.cn/mw690/6941baebjw1ew6h76af2rj202x00umwy.jpg)

为了计算这些梯度，我们使用了著名的后向传播算法。这个算法是从输出计算梯度的一种很高效的方法。 
应用后向传播公式我们发现以下内容:

![](http://ww2.sinaimg.cn/mw690/6941baebjw1ew6gxfhs9aj205805y0sp.jpg)


<h2 id="38164c8be942882c3e6c233dfc8087ab"></h2>
####实现
现在我们要准备开始实现网络了。我们从定义梯度下降一些有用的变量和参数开始：
```python
num_examples = len(X) # training set size
nn_input_dim = 2 # input layer dimensionality
nn_output_dim = 2 # output layer dimensionality
 
<h2 id="8918c18069d3e2d37825c7a0aa9b8ad7"></h2>
# Gradient descent parameters (I picked these by hand)
epsilon = 0.01 # learning rate for gradient descent
reg_lambda = 0.01 # regularization strength
```

首先要实现我们上面定义的损失函数。以此来衡量我们的模型工作得如何：

```python
<h2 id="24dadccd15c89a6bcae3ea31e48b04e1"></h2>
# Helper function to evaluate the total loss on the dataset
def calculate_loss(model):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation to calculate our predictions
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    # Calculating the loss
    corect_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(corect_logprobs)
    # Add regulatization term to loss (optional)
    data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1./num_examples * data_loss
```

还要实现一个辅助函数来计算网络的输出。它的工作就是传递前面定义的前向传播并返回概率最高的类别。

```python
<h2 id="3d9b2c51cec46ad99f068f3509c50516"></h2>
# Helper function to predict an output (0 or 1)
def predict(model, x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)
```

最后是训练神经网络的函数。它使用上文中发现的后向传播导数实现批量梯度下降。

```python
<h2 id="f16f2ee97812ff64f3412a39df93472f"></h2>
# This function learns parameters for the neural network and returns the model.
<h2 id="64c89f28e85aa9c9b9cd26d7b2c64037"></h2>
# - nn_hdim: Number of nodes in the hidden layer
<h2 id="0413112b5c54316c374670810c17b0ec"></h2>
# - num_passes: Number of passes through the training data for gradient descent
<h2 id="52985252a6929bd0b68f7ab8faaa60b7"></h2>
# - print_loss: If True, print the loss every 1000 iterations
def build_model(nn_hdim, num_passes=20000, print_loss=False):
 
    # Initialize the parameters to random values. We need to learn these.
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, nn_output_dim))
 
    # This is what we return at the end
    model = {}
 
    # Gradient descent. For each batch...
    for i in xrange(0, num_passes):
 
        # Forward propagation
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
 
        # Backpropagation
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)
 
        # Add regularization terms (b1 and b2 don't have regularization terms)
        dW2 += reg_lambda * W2
        dW1 += reg_lambda * W1
 
        # Gradient descent parameter update
        W1 += -epsilon * dW1
        b1 += -epsilon * db1
        W2 += -epsilon * dW2
        b2 += -epsilon * db2
 
        # Assign new parameters to the model
        model = { 'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
 
        # Optionally print the loss.
        # This is expensive because it uses the whole dataset, so we don't want to do it too often.
        if print_loss and i % 1000 == 0:
          print "Loss after iteration %i: %f" %(i, calculate_loss(model))
 
    return model
```

<h2 id="9a19b3c2ae83b808232d7a6d84bd9643"></h2>
##隐藏层规模为3的神经网络
一起来看看假如我们训练了一个隐藏层规模为3的神经网络会发生什么。

```python
<h2 id="ee776fa8de8791678d3bf348c3d72738"></h2>
# Build a model with a 3-dimensional hidden layer
model = build_model(3, print_loss=True)
 
<h2 id="fa8b9079f938129811351dc2da540938"></h2>
# Plot the decision boundary
plot_decision_boundary(lambda x: predict(model, x))
plt.title("Decision Boundary for hidden layer size 3")
plt.show()
```

![](http://ww2.sinaimg.cn/mw690/6941baebjw1ew6gxf6v1qj20gm0dlta6.jpg)
耶！这看起来结果相当不错。我们的神经网络能够找到成功区分类别的决策边界。

<h2 id="8f3bd9e9a60d3826fd71b039c4861df3"></h2>
##变换隐藏层的规模
```python
plt.figure(figsize=(16, 32))
hidden_layer_dimensions = [1, 2, 3, 4, 5, 20, 50]
for i, nn_hdim in enumerate(hidden_layer_dimensions):
    plt.subplot(5, 2, i+1)
    plt.title('Hidden Layer size %d' % nn_hdim)
    model = build_model(nn_hdim)
    plot_decision_boundary(lambda x: predict(model, x))
plt.show()
```

低维隐藏层能够很好地捕捉到数据的总体趋势。更高的维度则更倾向于过拟合。 


