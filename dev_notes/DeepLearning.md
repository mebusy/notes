
# Deep Learning 

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



The sigma value determines the order of magnitude of you outputs at the initial point of your optimization.  Because of the softmax on top of it, the order of magnitude also determines the peakiness of your initial probability distribution.

 - A large sigma means that your distribution will have large peaks. It's going to be very opinionated.
 - A small sigma means that your distribution is very uncertain about things.

It's usually better to begin with an uncertain distribution and let the optimization become more confident as the train progress.

***So use a small sigma to begin with***.









