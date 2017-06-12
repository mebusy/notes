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

Wheneven a state aliasing occurs , a staochastic policy can do better than a deterministic policy.

### Policy Objective Functions 

 - start value
    - In episodic environments we can use the start value
    - This basically says, if I always start in some state s1, or have some distribution of start state  s1, what the total reward will I get from that start state almost. 
    - 比如说在atari游戏中，我一直打通关知道最后，然后获得得分。
 - average value
    - In continuing environments we can use the average value
    - Let consider the probability of any state , times the value from that state onwards. So we average over the value of all states. 
    - maybe in s1 ,we got 10 points from that point onwards, in s2 wo got 20 points from that point onwards. So we average those , say, well the objective rewards is 15.
 - Or the average reward per time-step
    - What we really care about is just , let's consider some continuing environments I'm going round round round , now I care about is make sure the per time step I gaining the most reward. So we're not summing there reward over time, we just saying we will take the average of my immediate rewards over the entire distribution of states I visited.
    - so this is basically saying, the objective is there is some probability I'm in some state , some probability I take an action from that state under my policy , and this is the immediate reward that I get at that step. What we care about is getting the most reward per time step. 

这三种方法殊途同归。


### Softmax Policy

The score fuction is just the feature for the action we actually took , minus the average feature for all action might taken. 

So this basically saying, how much more this feature do I have than usual , this is the score function.

When we start doing this kind of policy gradient algorithm , what are we actually doing is saying , if a feature occurs more than usual and gets reward , then we want to adjust the policy to do more 


### Gaussian Policy

score function 

 - a : action we actually took
 - μ(s) : mean action ?

### One-Step MDPs

最后一个期望𝔼 , 这是使用 likehood ratios 技巧的要点所在。We start with something which is an expectation, we take the gradient, and recover something which is still an expecation. So this thing is an expectation under a policy , so this is an expectation under start state, next expectation the action we pick is all the gradient to log policy multiply by reward -- the expectation of the score times reward. 

It shows us if we want to increase the objective function, want get more reward, we just need to move in the direction that determine by the score times the reward. 

Again this tell us how to adjust a  policy so that get more or less something , and this tell us what is good or bad. 

So if get a really big reward you want to move in the direction that get more reward. if you get a negative reward, you want to move in the opposite  direction. 






## 2 Finite Difference Policy Gradient

## 3 Monte-Carlo Policy Gradient


## 4 Actor-Critic Policy Gradient



