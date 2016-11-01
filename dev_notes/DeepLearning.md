
# Deep Learning 

# From Machine Learning to Deep Learning

## SOFTMAX

The way to turn scores into probabilities is to use **softmax** function , will be denoted by *S*. It can take any kind of scores and turn them into proper probabilities. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_softmax.png)

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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_softmax_graph.png)


Caution:

 1. if we multiply scores by 10 , then probabilities get close to either 0.0 or 1.0
 2. if we divide scored by 10 , probabilities get close to the uniform distribution.



## CROSS-ENTROPY


```
D(S,L) = -Σ Lᵢ log(Sᵢ)
```

Cross-entropy is not symmetric :   D(S,L) != D(L,S)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_cross_entropy.png)

 - We have an input , it's going to be turned into logits using a linear model
 - We're then going to feed the logits , which are scores , into a softmax to turn them into probobilities
 - Then we're going to compare those probabilities to the one hot encoded labels using the cross entropy function.

This entire setting is often called multinominal logistic classification.

---

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
MEAN :   	Xᵢ = 0 
VARIANCE:  	σ(Xᵢ) = σ(Xⱼ)
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_numerical_stability.png)

### Images

If you dealing with images, you can take the pixel value of your image, they are typically between 0 and 255 , and simply subtract 128 and divide by128 `( C - 128) / 128 ` .

It doesn't change the content of your image, but it makes it much easier for the optimization to proceed numerically.

### Weight initialization

You also want your weights and biases to be initialized at a good enough starting point for the gradient descent to preceed. There are lots of fancy schemes to find good initialization values , but we're going to focus on a simple , general method.

Draw the weights randomly from a Gaussian distribution with mean zero and standard deviation sigma.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_weights_initialization.png)

The sigma value determines the order of magnitude of you outputs at the initial point of your optimization.  Because of the softmax on top of it, the order of magnitude also determines the peakiness of your initial probability distribution.

 - A large sigma means that your distribution will have large peaks. It's going to be very opinionated.
 - A small sigma means that your distribution is very uncertain about things.

It's usually better to begin with an uncertain distribution and let the optimization become more confident as the train progress.

***So use a small sigma to begin with***.


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


## The Kaggle Challenge

machine learning 竞赛网站

---

# Deep Neural Networks

## Linear Model Limited

 - Linear operations are really nice 
 	- Big matrix multiplies are exactly what GPUs were design for
 - The derivative of a linear function is nice too , it's a constant !


## Network of ReLUs

We're going to construct our new function in the simplest way that we can think of.

Instead of having a single matrix multiplier as our classifier , we're going to insert a RELU right in the middle.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_RELU.png)

We now have two matrices. 

 - one going from the inputs to the RELUs ,
 - and another one connecting the RELUs to the classifier.

Our function is now nonlinear thanks to the RELU in the middle , and we now have a new knob that we can tune , this number H ( in blue ) which corresponds to the number of RELU units that we have in the classifier. We can make it as big as we want.

## The Chain Rule

One reason to build this network by stacking simple operations is that it makes tha math very simple .

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_RELU_math.png)

The key mathematical insight is the chain rule : `[g( f(x ))]' = g'( f(x) ) * f'(x)  ` . 

 - if you have 2 functions that get composed , that is , one is applied to the output of the other , then the chain rule tells you that you can compute the derivatives of that function simply by taking the product of the derivatives of the components.

As long as you know how to write the derivatives of your individual functions , there is a simple graphical way to combine them together and compute the derivative for the whole function.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_RELU_math2.png)

There's even better news for the compute scientist in you.  There is a way to write this chain rule that is very efficient computationally.

 - efficient data pipeline !
 - lots of data reuse !

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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_BackProp.png)


