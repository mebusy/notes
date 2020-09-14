...menustart

- [Deep Learning](#6a68b6412b3d8a605c374d3c59e02694)
- [From Machine Learning to Deep Learning](#d41184f514356348f59aa91ad4f37c98)
    - [SOFTMAX](#1d993169621e0855bad00d71c005cf1b)
    - [CROSS-ENTROPY](#e227f3d7f7e740bb759f0066342ff799)
    - [Minimizing Cross Entropy](#0b3ff0c33c38d07fc732b5ec92ce1647)
    - [Numerical Stability](#6bd7e96f5a6e9231f7d947c5fc18e876)
        - [Images](#fff0d600f8a0b5e19e88bfb821dd1157)
        - [Weight initialization](#9457fbceb006e0a464b95be0ee804d83)
        - [Initialization of the lgistic classifier](#caa736eb798e357900ffcd35d1a78e99)
    - [The Kaggle Challenge](#0c4981f443dd7633e4286cbaa482c579)
- [Deep Neural Networks](#87b3239cbf57b3e46249505264571228)
    - [Linear Model Limited](#f880aa9c184596fc12ff27937ebaf8ca)
    - [Network of ReLUs](#9be412d16c60d2fa986ffc1f194643c0)
    - [The Chain Rule](#62568a512f5b51ee525d33114a235b26)
    - [Back prop](#d93c592036c29f14635824ddf09aab87)
    - [Training a Deep Learning Network](#3964943701fa3f4989658e59f88cc110)
    - [Regularization Intro](#949b893e589d45ecfe63894272b7b754)
    - [Regularization](#853cc01c0ad043a93a400b3b1dc15614)
    - [Dropout](#09bb9294aa4a843883a3f401aeaf8b5b)
- [Convolutional Neural Network](#02ed75b713cdaf7bbe2faae40ba76279)
    - [Statistical Inveriance](#78289659377fe0ce4edb6cc2c3e44939)
    - [Convolutional Networks , or CONVNETS](#4f15f700f5c4dc733c503ae470344017)
    - [Explore The Design Space](#3e6416a016525c87f33de8dad90df107)
    - [1x1 Convolutions](#557f2cb10e34586ed5a05c43c0c3d26a)

...menuend


<h2 id="6a68b6412b3d8a605c374d3c59e02694"></h2>


# Deep Learning 

<h2 id="d41184f514356348f59aa91ad4f37c98"></h2>


# From Machine Learning to Deep Learning

<h2 id="1d993169621e0855bad00d71c005cf1b"></h2>


## SOFTMAX

The way to turn scores into probabilities is to use **softmax** function , will be denoted by *S*. It can take any kind of scores and turn them into proper probabilities. 

![](../imgs/DL_softmax.png)

> scores -> probabilities

Proper probabilities , sum to 1.


```python
"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum( np.exp(x) , axis = 0 )


print(softmax(scores))
```

![](../imgs/DL_softmax_graph.png)


Caution:

 1. if we multiply scores by 10 , then probabilities get close to either 0.0 or 1.0
 2. if we divide scored by 10 , probabilities get close to the uniform distribution.



<h2 id="e227f3d7f7e740bb759f0066342ff799"></h2>


## CROSS-ENTROPY


```
D(S,L) = -Σ Lᵢ log(Sᵢ)
```

Cross-entropy is not symmetric :   D(S,L) != D(L,S)

![](../imgs/DL_cross_entropy.png)

 - We have an input , it's going to be turned into logits using a linear model
 - We're then going to feed the logits , which are scores , into a softmax to turn them into probobilities
 - Then we're going to compare those probabilities to the one hot encoded labels using the cross entropy function.

This entire setting is often called multinominal logistic classification.

---

<h2 id="0b3ff0c33c38d07fc732b5ec92ce1647"></h2>


## Minimizing Cross Entropy

The question of course is how we're going to find those weights w and biases b that will get our classifier to do what we want it to do.

That is , have low distance for the correct class D(A, a) , but have a high distance for the incorrect class D(A , b).

One thing you can do is measure that distance averaged over the entire training sets for all the inputs and all the labels that you have available.

```
traing loss : l = 1/N * Σ D( S(Wxᵢ + b) , Lᵢ )
```

Ways:

 1. Gradient Descent
     - Take the dirivative of your loss, with respect to your parameters , and follow that derivative by taking a step backwards and repeat , until you get to the buttom.



<h2 id="6bd7e96f5a6e9231f7d947c5fc18e876"></h2>


## Numerical Stability

In particular , adding very small values to a very large value can introduce a lot of errors.

```python
>>> a = 1000000000
>>> for i in xrange(1000000):
...     a = a + 0.000001
... 
>>> print a - 1000000000
0.953674316406    # Yes, it's not 1!
```



We're going to want the values involved in the calculation of this big loss function that we care about to never get too big or too small.

On good guiding principle is that we always want our variables to have zero mean and equal variance whenever possible.

```
MEAN :       Xᵢ = 0 
VARIANCE:      σ(Xᵢ) = σ(Xⱼ)
```

![](../imgs/DL_numerical_stability.png)

<h2 id="fff0d600f8a0b5e19e88bfb821dd1157"></h2>


### Images

If you dealing with images, you can take the pixel value of your image, they are typically between 0 and 255 , and simply subtract 128 and divide by128 `( C - 128) / 128 ` .

It doesn't change the content of your image, but it makes it much easier for the optimization to proceed numerically.

<h2 id="9457fbceb006e0a464b95be0ee804d83"></h2>


### Weight initialization

You also want your weights and biases to be initialized at a good enough starting point for the gradient descent to preceed. There are lots of fancy schemes to find good initialization values , but we're going to focus on a simple , general method.

Draw the weights randomly from a Gaussian distribution with mean zero and standard deviation sigma.

![](../imgs/DL_weights_initialization.png)

The sigma value determines the order of magnitude of you outputs at the initial point of your optimization.  Because of the softmax on top of it, the order of magnitude also determines the peakiness of your initial probability distribution.

 - A large sigma means that your distribution will have large peaks. It's going to be very opinionated.
 - A small sigma means that your distribution is very uncertain about things.

It's usually better to begin with an uncertain distribution and let the optimization become more confident as the train progress.

***So use a small sigma to begin with***.


<h2 id="caa736eb798e357900ffcd35d1a78e99"></h2>


### Initialization of the lgistic classifier

Now we actually have everythings we need to actually train this classifier.

 - We've got our training data `X` 
     - which is normalized to have zerom mean (pixels - 128)/128 , and unit variance.
 - We multiply `X` by a large matrix `W` 
     - `W` is intialized with random weights
 - We apply the softmax and then the cross entropy loss 
 - and we calculate the average of this loss over the entire traning data.

--- ASSIGNMENT

安装

```
brew install docker docker-machine
```

启动 docker-machine

建立並啟動一個 VM 作為 docker 的環境 , 這邊我使用的 driver 為 VirtualBox，名字設定為 default：

```
docker-machine create --driver virtualbox default
```

启动 VM

接下來為重點，我們執行 docker-machine env default，可以查看 default 所設定的參數，而這些參數用於指定 docker 的 client 所要連線的參數：

```
$ docker-machine env default
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/qibinyi/.docker/machine/machines/default"
export DOCKER_MACHINE_NAME="default"
# Run this command to configure your shell: 
# eval $(docker-machine env default)
```

照着上面说的，执行最后一句

```
$ NO_PROXY=`docker-machine ip default` docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

dock-machine 设置代理

```
docker-machine ssh default

# now the command prompt will say something like:
# docker@default:~$

# we need root access:
sudo -s

# now the command prompt will say something like:
# root@default:~$

# now configure the proxy
echo "export HTTP_PROXY=http://[uid]:[pw]@corporate.proxy.com:[port]" >> /var/lib/boot2docker/profile
echo "export HTTPS_PROXY=http://[uid]:[pw]@corporate.proxy.com:[port]" >> /var/lib/boot2docker/profile

# for verification
cat /var/lib/boot2docker/profile

# exit out of ssh session
exit
exit

# restart
docker-machine restart default

# now you should be able to proceed with installation steps
docker run hello-world
```

---

```
NO_PROXY=`` docker run -p 8888:8888 --name tensorflow-udacity -it gcr.io/tensorflow/udacity-assignments:0.6.0
```

 - docker-machine ip default :  docker host IP

访问:

```
open http://`docker-machine ip default`:8888
```


<h2 id="0c4981f443dd7633e4286cbaa482c579"></h2>


## The Kaggle Challenge

machine learning 竞赛网站

---

<h2 id="87b3239cbf57b3e46249505264571228"></h2>


# Deep Neural Networks

<h2 id="f880aa9c184596fc12ff27937ebaf8ca"></h2>


## Linear Model Limited

 - Linear operations are really nice 
     - Big matrix multiplies are exactly what GPUs were design for
 - The derivative of a linear function is nice too , it's a constant !


<h2 id="9be412d16c60d2fa986ffc1f194643c0"></h2>


## Network of ReLUs

We're going to construct our new function in the simplest way that we can think of.

Instead of having a single matrix multiplier as our classifier , we're going to insert a RELU right in the middle.

![](../imgs/DL_RELU.png)

We now have two matrices. 

 - one going from the inputs to the RELUs ,
 - and another one connecting the RELUs to the classifier.

Our function is now nonlinear thanks to the RELU in the middle , and we now have a new knob that we can tune , this number H ( in blue ) which corresponds to the number of RELU units that we have in the classifier. We can make it as big as we want.

<h2 id="62568a512f5b51ee525d33114a235b26"></h2>


## The Chain Rule

One reason to build this network by stacking simple operations is that it makes tha math very simple .

![](../imgs/DL_RELU_math.png)

The key mathematical insight is the chain rule : `[g( f(x ))]' = g'( f(x) ) * f'(x)  ` . 

 - if you have 2 functions that get composed , that is , one is applied to the output of the other , then the chain rule tells you that you can compute the derivatives of that function simply by taking the product of the derivatives of the components.

As long as you know how to write the derivatives of your individual functions , there is a simple graphical way to combine them together and compute the derivative for the whole function.

![](../imgs/DL_RELU_math2.png)

There's even better news for the compute scientist in you.  There is a way to write this chain rule that is very efficient computationally.

 - efficient data pipeline !
 - lots of data reuse !

<h2 id="d93c592036c29f14635824ddf09aab87"></h2>


## Back prop 

Here is an example.  Imagine your network is a stack of simple operations ( 1st line : x -> y  ) . 

Some have parameters like the matrix transforms ( ie. w1 , w2 ) , some don't like .  When you apply your data to some input x , you have data flowing through the stack up to your predictions y .

To compute the derivatives , you create another graph that looks like this. ( 2nd line:  <- ȳ )

The data in the new graph flows backwards through the network ,  get's combined using the chain rule and preduces gradients.

That graph can be derived completely automatically from the individual operations in your network. So most deep learning frameworks will just do it for you. This is called back-propagation, and it's a very powerful concept. It makes computing derivatives of complex function very efficient as long as the function is make up of simple blocks with simple derivatives.

Running the model up to the predictions is often called the forward prop, and the model that goes backwards is called the back prop.

So , to recap, to run stochastic gradient descent for every single little batch of your data in your training set,  you're going to run the forward prop, and then the back prop. And that will give you gradients for each of your weights in your model ( Δw₁, Δw₂ ).  Then you're going to apply those gradients with the learning rates ( α) to your original weights ( w₁, w₂ ) , and update them.

And you're going to repeat that all over again, many, many times. This is how your entire model gets optimized.

In particular each block of the back prop often takes about twice the memory that's needed forward prop and twice the compute.

![](../imgs/DL_BackProp.png)

---

<h2 id="3964943701fa3f4989658e59f88cc110"></h2>


## Training a Deep Learning Network 

2-layer Neural Network

![](../imgs/DL_RELU.png)


You can make it bigger , more complex , by increasing the size of that hidden layer in the middle.  But it turns out that increasing this H is not particularly efficient in general .  You need to make it very , very big , and then it gets really hard to train. This is where the central idea of deep learning comes into play.

Instead , you can also add more layers and make your model deeper.  There are lots of good reasons to do that.

 - one is parameter efficiency
     - You can typically get much more performance with fewer parameters by going deeper rather than wider.
 - another 1 is that a lot of natual phenomena that you might be interested in , tend to have a hierarchical structure which deep model naturally capture.


<h2 id="949b893e589d45ecfe63894272b7b754"></h2>


## Regularization Intro

Why did we not figure out earlier that deep-models were effective ?

Manu reasons, but mostly because deep-models only really shine if you have enough data to train them. It's only in recent years that large enough data sets have made their way to the academic world.  

We'll look at another reason now, we know better today how to train very very big models using better regularization techniques. There is a general issue when you're doing numerical optimization which I call the skinny jeans problem.  Skinny jeans look great, they fit perfectly , but they're really really hard to get into .  So most people end up waring jeans that are just a bit too big.  It's exactly the same with deep networks. The network that's just the right size for your data is very very hard to optimize .

So in practice , we always try networks that are way too big for our data and then we try our best to prevent them from overfitting.


<h2 id="853cc01c0ad043a93a400b3b1dc15614"></h2>


## Regularization

Regularizing means applying artificial constraints on your network that implicityly reduce the number of free parameters while not making it more difficult to optimize.

In the skinny jeans analogy , think stretch pants.  The fit just as well , but because they're flexible , they don't make things harder to fit in.

The stretch pants of deep learning are called L2 Regularization.  

The idea is to add another term to the loss ,which penalizes large weights.  It's typically achieved by adding the L2 norm of your weights to the loss , multiply by a small constant β.

![](../imgs/DL_regularization.png)


<h2 id="09bb9294aa4a843883a3f401aeaf8b5b"></h2>


## Dropout

There's another important technique for regularization that only emerged relatively recently and works amazingly well. It also looks insane the first time you see it , so bear with me . It's called dropout.

Dropout works likes this. 

![](../imgs/DL_dropout.png)

Imagine that you have one layer that connects to another layer. The values that go from one layer to the next are often called activations.  Now take those activations and randomly for every example you train your network on, set half of them to zero.  Completely randomly ,  you basically take half of the data that's flowing through your network and just destroy it. And then randomly again. If that doesn't sound crazy to you then you might qualify to become a student of Jeffery Hinto who pioneered the technique.

So what happens with dropout?

![](../imgs/DL_dropout2.png)

Your network can never rely on any given activation to be present , because they might be squashed at any given moment. So it is forced to learn a redundant representation for everything to make sure that at least some of the information remains.

It's like a game of whack-a-mole.  One activations gets smashed , but there's always one or more that do the same job and that don't get killed. So every thing remains fine at the end.

![](../imgs/DL_dropout3.png)

Forceing your network to learn redundant representations might sound very inefficient. But in practice , it makes things more rebust and prevents overfitting.  It also makes your network act as if taking the consensus over an ensemble of networks. Which is always a good way to improve performance. 

Dropout is one of the most important techniques to emerge in the last few years. It the dropout doesn't work for you, you should probably be using a bigger network.

---

When you evaluate the network that's been trained with drop out, you obvioulsy no longer want this randomness.

![](../imgs/DL_dropout_2.png)

You want something deterministic. Instead , you're going to want to take the consensus over these redundant models.  You get the consensus opinion by averaging the activations.

You want *Ye* here to be the average of all the *Yt*s that you got during training. 

Here's the trick to make sure this expectation holds. During training , not only do you use zero out so the activations that you drop out, but you also scale the remaining activations by a factor of 2.  This way, when it comes time to average them during evaluation, you just remove these dropouts and scaling operations from your neural net. And the result is an average of these activations that is properly scaled. 


---

<h2 id="02ed75b713cdaf7bbe2faae40ba76279"></h2>


# Convolutional Neural Network

<h2 id="78289659377fe0ce4edb6cc2c3e44939"></h2>


## Statistical Inveriance

![](../imgs/DL_cats.png)

You have an image and you want your network to say it's an image with a cat in it.  It doesn't really matter where the cat is , it's still an image with a cat.

If your network has to learn about cat in the left corner and about cat in the right corner independently , that's a lot of work that is has to do . 

How about you telling it instead , explicitly , that objects and images are largely the same whether they're on the left or on the right of the picture. That's what called translation invariance.  Different positions, same cat. 

Yet another example . Imagine you have a long text that talks about kittens. Does the meaning of kiten change depending on whether it's in the first sentence or in the second one ? Mostly not.  So if you're tring a network on text ,maybe you want the part of the network that learns what a kitten is to be reused every time you see the work kitten, and not have to relearn it every time.  

![](../imgs/DL_weight_shareing.png)

The way you achieve this in your own networks is using what is called **weight sharing**. When you know that two inputs can contain the same kind of information, then you share the weights and train the weights jointly for those inputs.

It is a very important idea. Statisitcal invariants , things that don't change on average across time or space , are every where. For images, the idea of weight sharing will get us to study convolutinal networks.  For text and sequences in general , it will lead us to embeddings and recurrent neural networks.


<h2 id="4f15f700f5c4dc733c503ae470344017"></h2>


## Convolutional Networks , or CONVNETS

Convnets are neural networks that share their parameters across space.

Imagine you have a image.

![](../imgs/DL_convent_1.png)

It can be represented as a flat pancake . It has width , height. And because you typically have red, green and blue channels , it also has a depth.  In this instance, depth is 3 ,  that's your input.

Now imagine taking a small patch of this image and running a tiny neural network on it , with say, K outputs.

Let's represent those outputs vertically, in a tiny column like this.


Now let's slide that little neural network across the image without changing the weights. Just slide across , and vertically like we're painting it with a brush. On the output, we've drawn another image. 

![](../imgs/DL_convent_2.png)

It's got a different witdh, a different height, and more importantly , it's got a different depth. Instead of RGB , now you have an output that's got many color channels , K of them. 

![](../imgs/DL_convent_3.png)

This operation is called a convolution.  

If your patch size were the size of the whole image, it would be no different than a regular layer of a neural network. But because we have this small patch instead, we have many fewer weights and they are shared across space.

A convent is going to basically be a deep network where instead of having stacks of matrix multiply layers. we're going to have stacks of convolutions. The general idea is that they will form from a pyramid. 

![](../imgs/DL_convolution_pyramid.png)

At the bottom you have this big image but very shallow, just RGB.  You're going to apply convolutions that are going to progressively squeeze the spatial dimensions while increasing the depth, which corresponds roughly to the semantic complexity of your representation.  An the top you can put your classifier . You have a representation where all the spatial information has been squeezed out and only parameters that map to contents of the image remain.

![](../imgs/DL_convolution_lingo.png)

So that is the general idea. If you're going to implement this , there are lots of little details to get right and a fair bit of lingo to get used to. 

you've met the concept of patch and depth.  Patches are sometimes called kernels.  Each pancake in your stack is called a feature map.  Here , you're mapping three feature maps to K feature maps.  Another term that you need to know is stride.  It's the number of pixels that you're shifting each time you move your filter.  A strider of 1 makes the output roughly the same size as the input. A strider is 2 means it's about half the size. 

---

That's it.  You can build a simple convnet with just this.  Stack up your convolutions , which thankfully you don't have to implement yourselves,  then use trieds to reduce the dimensional and increase the depth of your network, layer after layer. And once you have a deep and narrow representation, connect the whole thing to a few regular fully connected layers and you're ready to train your classifier.

You might wonder what happends to training , into the chain rule in particular , when you use shared weights like this.   Nothing really happens.

![](../imgs/DL_chain_rules_with_sharing.png)

The math just works. You just add up the derivatives from all of the possible locations on the image.

---

<h2 id="3e6416a016525c87f33de8dad90df107"></h2>


## Explore The Design Space

To improve a simple convnet

 - POOLING
 - 1x1 Convolutions
 - INCEPTION

The 1st improvement is a better way to reduce the spatial extent of your feature maps in the convolutional pyramid.  Until now, we've used striding to shift the filters by a few pixel each time and reduce the future map size.  This is a very aggressive way to downsample an image.  It removes a lot of information. 

What if instead of skipping one in every two convolutions, we still ran with a very small stride, say for example one. But then took all the convolutions in a neighborhood and combined them somehow. That operation is called **pooling**, and there are a few ways to go about it.

The most common is max pooling.  At every point in the feature map, look at a small neighborhood around that point and compute the maximum of all the responses around it.

![](../imgs/DL_max_pooling.png)

 - ADVANTAGE
     - **PARAMETER-FREE** , it doesn't add to your number of parameters. So you don't risk an increasing over fitting.
     - **OFTEN MORE ACCURATE**
 - DISADVANTAGE
     - MORE EXPENSIVE
     - MORE HYPER PARAMETERS
         - POOLING SIZE
         - POOLING STRIDE

A very typical architecture for a convnet is a few layers alternating convolutions and max pooling , followed by a few fully connnected layers at the top.

The 1st famouse model to use this architectuer was LENET-5 . Modern convolutional networkds such as ALEXNET.

Another notable form of pooling is average pooling. Instead of taking the max, just take an average over the window of pixels around a specific location. It's a little bit like providing a blurred low resolution view of the feature map below.  We're going to take advantage of that shortly.



<h2 id="557f2cb10e34586ed5a05c43c0c3d26a"></h2>


## 1x1 Convolutions

But first , I want to introduce you to another idea , it's the idea of one by one convolutions.



