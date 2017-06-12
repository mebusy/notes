...menustart

 - [RL David Silver , Part II](#642eadc816039c29a67ef129a6a090f6)
 - [Lecture 6:](#ecbcb5fe84f115baf7815f06a0042e1c)
	 - [Value Function Approximation](#d9bb6b898523b2ea131950f5ec3fc308)
	 - [Types of Value Function Approximation](#c6856fb88cde30004a30618776062a49)
	 - [Value Function Approx. By Stochastic Gradient Descent](#2a8b356b7c497a4fa82537430889ff7c)
	 - [TD(λ) with Value Function Approximation](#174cd9c9b503392d64f89edef582c758)

...menuend


<h2 id="642eadc816039c29a67ef129a6a090f6"></h2>

# RL David Silver , Part II

<h2 id="ecbcb5fe84f115baf7815f06a0042e1c"></h2>

# Lecture 6: 

<h2 id="d9bb6b898523b2ea131950f5ec3fc308"></h2>

## Value Function Approximation


<h2 id="c6856fb88cde30004a30618776062a49"></h2>

## Types of Value Function Approximation


 - for q(s,a,w) , you feature should be extracted from both state , action
    - eg. self.featExtractor.getFeatures(state, action )

 - 第二张图 action-in
 - 第三张图 action-out
    - Atari game ?

<h2 id="2a8b356b7c497a4fa82537430889ff7c"></h2>

## Value Function Approx. By Stochastic Gradient Descent

<h2 id="174cd9c9b503392d64f89edef582c758"></h2>

## TD(λ) with Value Function Approximation

 - When you useing Function Approximation , the size of eligibility traces is on the size of you parameters ?
    - it record all the features you have seen so far.

### Linear Action-Value Function Approximation

we might have 1 feature ,x₁, say how far am I far from the wall if I moving forwards. And I have another feature , x₂ , says how far am I far from this wall if I'm moving backwards. 

### Stochastic Gradient Descent with Experience Replay

我们保存所有的经验，而不是用过一次后就扔掉。

就像又回到了监督学习法。

打乱顺序，做一次随机梯度下降；再次打乱顺序，又一次地做随机地图下降。


### Experience Replay in Deep Q-Networks (DQN)

之前说过，Sarsa，TD 这些方法 can not work in your network. However this method is stable in your networks. 

我们实际是在用两套神经网络运行。一般会freeze 老的神经网路。

# Lecture 7: Policy Gradient

## 1 Introduction

直接将 policy，而不是 value function, 参数化。



## 2 Finite Difference Policy Gradient

## 3 Monte-Carlo Policy Gradient


## 4 Actor-Critic Policy Gradient



