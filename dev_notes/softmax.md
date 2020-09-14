...menustart

- [Softmax](#31d953b9d49a6b4378f45097047976d0)
    - [Practical issues: Numeric stability](#40eb18ef5b1bf8f66fcdf418e2cef2cd)
    - [Softmax & Sigmoid](#72db2e1699f3b38e8823c7cd58ff5821)
    - [Derivative](#70ae6e285cc14c8486e3cf5bec39d1fd)

...menuend


<h2 id="31d953b9d49a6b4378f45097047976d0"></h2>


# Softmax

![](../imgs/softmax3.gif)  is called the **softmax function**.


<h2 id="40eb18ef5b1bf8f66fcdf418e2cef2cd"></h2>


## Practical issues: Numeric stability

When you’re writing code for computing the Softmax function in practice, the intermediate terms e<sup>f</sup>  may be very large due to the exponentials.

```python
def softmax( f ):
    # Bad: Numeric problem, potential blowup
    return np.exp(f) / np.sum(np.exp(f))
    
>>>
>>> softmax( np.array([123, 456, 789])  )
__main__:3: RuntimeWarning: overflow encountered in exp
__main__:3: RuntimeWarning: invalid value encountered in divide
```

Notice that if we multiply the top and bottom of the fraction by a constant C and push it into the sum, we get the following (mathematically equivalent) expression:

![](../imgs/softmax4.gif) 

We are free to choose the value of C. This will not change any of the results. That is , only the relative difference of one action over another is important.

```python
>>> softmax( np.array([12,25,44]) )
array([  1.26641655e-14,   5.60279641e-09,   9.99999994e-01])
>>> # add 100 to all entries , it keeps the same result
>>> softmax(  np.array([12+100,25+100,44+100]) )
array([  1.26641655e-14,   5.60279641e-09,   9.99999994e-01])
```

A common choice for C is to set logC=−max(f). This simply states that we should shift the values inside the vector f so that the highest value is zero.


```python
def softmax( f ):
    # instead: first shift the values of f so that the highest number is 0:
    f -= np.max(f) # f becomes [-666, -333, 0]
    return np.exp(f) / np.sum(np.exp(f))  # safe to do, gives the correct answer

>>> softmax( np.array([12,25,44]) )
array([  1.26641655e-14,   5.60279641e-09,   9.99999994e-01])
```


[cs231n softmax notes](http://cs231n.github.io/linear-classify/#softmax)


<h2 id="72db2e1699f3b38e8823c7cd58ff5821"></h2>


## Softmax & Sigmoid 

Sigmoid function:

![](../imgs/sigmoid.gif)


```python
def sigmoid(X):
   return 1/(1+np.exp(-X))
```

What is the softmax distribution in case of 2 weights [a,b] ?

Suppose a≥b, Then:

![](../imgs/softmax-sigmoid.gif)

Yes, the soft-max distribution is the same as that given by the sigmoid.

```python
>>> softmax( np.array([14,12]) )
array([ 0.88079708,  0.11920292])
>>> sigmoid( 12-14 )
0.11920292202211755
```


<h2 id="70ae6e285cc14c8486e3cf5bec39d1fd"></h2>


## Derivative

Softmax is fundamentally a vector function. It takes a vector as input and produces a vector as output; in other words, it has multiple inputs and multiple outputs.

Therefore, we cannot just ask for "the derivative of softmax"; We should instead specify:

1. Which component (output element) of softmax we're seeking to find the derivative of.
2. Since softmax has multiple inputs, with respect to which input element the partial derivative is computed.


Take the derivative in multiple direction in space is very complicated if you think about it in the mathematical way. 


[求导&证明](https://zhuanlan.zhihu.com/p/25723112)



