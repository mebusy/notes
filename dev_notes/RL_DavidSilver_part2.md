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

idea : maximum policy objective function J(θ)


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

  ∇<sub>θ</sub> log π<sub>θ</sub>(s,a) 

=  ∇<sub>θ</sub> log ( e<sup>ɸ(s,a)ᵀθ</sup> / ∑e<sup>ɸ(s,a')ᵀθ</sup> ) 

= ∇<sub>θ</sub> log e<sup>ɸ(s,a)ᵀθ</sup> - ∇<sub>θ</sub> log  ∑e<sup>ɸ(s,a')ᵀθ</sup> 

= ∇<sub>θ</sub> ɸ(s,a)ᵀθ - ∑ ∇<sub>θ</sub> ɸ(s,a')ᵀθ

= ɸ(s,a) - ∑ɸ(s,a') = ɸ(s,a) - 𝔼<sub>πθ</sub>[ ɸ(s,·)]



### Gaussian Policy

score function 

 - a : action we actually took
 - μ(s) : mean action ?

### One-Step MDPs

最后一个期望𝔼 , 这是使用 likehood ratios 技巧的要点所在。We start with something which is an expectation, we take the gradient, and recover something which is still an expecation. So this thing is an expectation under a policy , so this is an expectation under start state, next expectation the action we pick is all the gradient to log policy multiply by reward -- the expectation of the score times reward. 

It shows us if we want to increase the objective function, want get more reward, we just need to move in the direction that determine by the score times the reward. 

Again this tell us how to adjust a  policy so that get more or less something , and this tell us what is good or bad. 

So if get a really big reward you want to move in the direction that get more reward. if you get a negative reward, you want to move in the opposite  direction. 

### Policy Gradient Theorem

The policy gradient is basically given by this thing , which is  some expectation of score function , multiplied by the action value Q. So it basically tells you again  how to adjust the policy so to get more or less of that particular action , multiplied by , how good that particular action was. 

### Monte-Carlo Policy Gradient (REINFORCE)

利用随机梯度上升算法来优化参数。

 - sample Q
 - so we are gonna be in a state, we start by take the action , add see what return we got. we'd use that to estimate Q. We just plug that in our policy gradient to give us a estimate direction to move. 
 - so every single episode now , in each step , we just adjust parameters a little bit in the direction of the score multiplied by the return we got from that point onwards.

### Puck World Example

 - it's slow. MC policy gradient methods tend to be slow. They're very high varience. 
 - so the rest of this class is going to be about using similar ideas but making them more efficient.

So that's going to bring us to the final family of algorithms -- actor critic methods.

### Reducing Variance Using a Critic

 - I'm playing a Atari game, one 1 particular episode I might get a score of 1000, and next episode I might get a score of 0. And that's just in the randomness of what happens. because over the course of 10000 steps there are many many different random event which might occur. This thing is very noisy. 
 - And the main idea of the critic methods is that indead of using the return to estimate the action value function we're going to explicitly estimate the action value function using a critic , using a value function approximator. 
 - combine value function approximation with our policy methods. 
 - plug Q<sub>w</sub> into our policy gradient as a substitute for Q<sup>π</sup>.
 - actor: actor is the thing which is doing things in the world and it contains the policy ,it's picking actions , it's actually making the decisions of what to do in the world
 - critic: critic doesn't actually take any decisions it's just watching what the actor does , and seeing what that's good or bad , evaluating that thing saying those decisions were good they got a score of 1000 or they got a score of -1000. 
 - the main idea is now to use an approximate policy gradient instead of the true policy gradient
    - we're going to adjust the actor , we can adjust the policy in the direction which according to the critic will get more reward. 
    - so the critics gonna say hey I think if you go in this direction you can actually do better. and then the actor is going to move in the direction of that gradient. 
 - so the way we're going to do that if we're going to take our original policy gradient algorithm , replace the true action value function with this estimated approximate value function -- where we got our neural network or whatever to estimate this thing. 
 - we're going to do then is that each step we're just going to move a little bit using stochastic gradient ascent , every step we're going to move a little bit in the direction of the score multiplied by a sample from our own function approximator.  So the critic is saying hey I think this thing is good or I think this thing is bad and then we move a little bit in the direction that gets more or less of the things that the critic says are good or bad. 

So how do we estimate the action value function ?


### Estimating the Action-Value Function

 - we can think of this is another form of generalized policy iteration
    - where we start off with a policy , we evaluate that policy using the critic , and then instead of doing greedy policy improvement we're moving a gradient step in some direction to get a better policy. 
    - to choose a first policy , you can pick an arbitrary policy , so you initialize your policy parameters θ however you want. 
    - there's no greedy anymore , no ε really, the policy itself determines how we move around to this environment. 

Now we have the basic idea of actor-critic algorithm. But what we want to do is to make these things better. So we consider now some tricks to make this thing better. 

### Reducing Variance Using a Baseline

So the first trick and perpaps the easiest and best trick is to to reduce vairence using what's called a baseline. 

So the idea is to subtract some baseline function from the policy gradient. and this can actually be done in a way that doesn;t change the direction of ascent. In other words, it changes the variance of the estimator , we can reduce the variance of this thing without changing the expectation. So another way to say that is that what we're going to do is we're going to subtract off some term which looks like this (red at bottom) from our policy gradient. 

 - B(s) is not depend on actino
 - we can pull the gradient ∇ outside of the sum ∑ 

 - advantage function
    - it is something which  tells us how much better than usual is it to take action *a*.

### Estimating the Advantage Function (1)

There is an easier way and probably a better way.

### Estimating the Advantage Function (2)

This is probably the most commonly used variant of the actor critic. 

It uses the following idea which is that the TD error is a sample of the advantage function. 


### Alternative Policy Gradient Directions

Thereis a really important question in actor-critic algorithms , which is we've used this critic and we just kind of said let's replace the true critic value with some approximation. and we just plugged in that thing and hoped that the gradient that we follow is still correct. But how do we know that is valid? how do we know this is really pushing us in the corrent gradient direction.

The answer is that amazingly if you choose the value function approximation carefully that you use, it is possible to pick a value function approximator that doesn't introduce any bias at all. In other words despite the fact that we don't have a true value function , they were approximating the value function, we can still follow the true gradient , we can be guaranteed to follow the true gradient with our policy update. 


That approach is called compatible function approximation. The main idea is that the features that we use, to have a compatible function approximator , are themselves the score function. we basically build up features for our critic where the features are the score of our policy. 

And if we use that **particular type** of feature , and we use **linear combination** of those feature  then we actually guarantee we don't affect the policy direction , we actually still follow the true gradient direction if we follow there compatible features. 

One last idea this is a recent idea , and a useful idea to know about -- Natural Policy Gradient.





## 2 Finite Difference Policy Gradient

## 3 Monte-Carlo Policy Gradient


## 4 Actor-Critic Policy Gradient

---

# Lecture 8: Integrating Learning and Planning



