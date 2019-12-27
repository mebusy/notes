...menustart

 - [RL David Silver , Part II](#642eadc816039c29a67ef129a6a090f6)
 - [Lecture 6:](#ecbcb5fe84f115baf7815f06a0042e1c)
     - [Value Function Approximation](#d9bb6b898523b2ea131950f5ec3fc308)
     - [Types of Value Function Approximation](#c6856fb88cde30004a30618776062a49)
     - [Value Function Approx. By Stochastic Gradient Descent](#2a8b356b7c497a4fa82537430889ff7c)
     - [TD(λ) with Value Function Approximation](#174cd9c9b503392d64f89edef582c758)
         - [Linear Action-Value Function Approximation](#ab0c9102c68d79422c93b60ef602d0bf)
         - [Stochastic Gradient Descent with Experience Replay](#40a1eb12575cfb9513a55cd7c8c874b5)
         - [Experience Replay in Deep Q-Networks (DQN)](#40a03e04054cc71abac6ad864a8b68e7)
 - [Lecture 7: Policy Gradient](#90ded6467b8ae95c15b518af0d6870af)
     - [1 Introduction](#8d2142fab6a831f4b2392206488d94a9)
         - [Policy Objective Functions](#96854aaa67c2cd550cb2242d152a3824)
         - [Softmax Policy](#db335bb35a59f97ddf493fcd1f74c079)
         - [Gaussian Policy](#c70cfd6d28c91d98dfd6410b3fbbeb44)
         - [One-Step MDPs](#51f43739235c39cdfa777a62f8648662)
         - [Policy Gradient Theorem](#a5656501eabca0acff7cb458bf0c1c13)
         - [Monte-Carlo Policy Gradient (REINFORCE)](#a1e378fb40906a1956a68710a611c1d6)
         - [Puck World Example](#3794e0fc1b829b0ff26b06e8f9a994d9)
         - [Reducing Variance Using a Critic](#fcb509fd5f5388d2b7ac9755d5ce7f17)
         - [Estimating the Action-Value Function](#95e4a74a003f412f4a8d513ef0448f11)
         - [Reducing Variance Using a Baseline](#3acf83ce7914d2b57f2c296114e396dd)
         - [Estimating the Advantage Function (1)](#0c31786a0e21f8d28470ba60afa42833)
         - [Estimating the Advantage Function (2)](#882835147fcacb1d7c0593c271657ca1)
         - [Alternative Policy Gradient Directions](#5d215218c32dde80c225cf454d518f0a)
     - [2 Finite Difference Policy Gradient](#c202e82b2a0d6070b8c852c124c7ea2e)
     - [3 Monte-Carlo Policy Gradient](#afbf6d2252accb977e4273ae3f55bcdd)
     - [4 Actor-Critic Policy Gradient](#3955f668aa01a331d669152fc2a66888)
 - [Lecture 8: Integrating Learning and Planning](#50d65004325941be417f9541f49a1314)
     - [1 Introduction](#8d2142fab6a831f4b2392206488d94a9)
     - [2 Model-Based Reinforcement Learning](#8bf761ff4e3ea4776a4789487933add1)
         - [Back to the AB Example](#12aa7b676bf938dcf88b1be11f69ecd7)
     - [3 Integrated Architectures](#e73c5eb2c33fbcafd857983c404349b8)
     - [4 Simulation-Based Search](#964b6e51181c427e77052ef724ce70e6)
 - [Lecture 9 :](#e296e754e887fb190b7ddbc5999e3ab8)
 - [Lecture 10: Classic Games](#9a7a5bf12ece7ccf9d2c7a3d596925ba)

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

<h2 id="ab0c9102c68d79422c93b60ef602d0bf"></h2>


### Linear Action-Value Function Approximation

we might have 1 feature ,x₁, say how far am I far from the wall if I moving forwards. And I have another feature , x₂ , says how far am I far from this wall if I'm moving backwards. 

<h2 id="40a1eb12575cfb9513a55cd7c8c874b5"></h2>


### Stochastic Gradient Descent with Experience Replay

我们保存所有的经验，而不是用过一次后就扔掉。

就像又回到了监督学习法。

打乱顺序，做一次随机梯度下降；再次打乱顺序，又一次地做随机地图下降。


<h2 id="40a03e04054cc71abac6ad864a8b68e7"></h2>


### Experience Replay in Deep Q-Networks (DQN)

之前说过，Sarsa，TD 这些方法 can not work in your network. However this method is stable in your networks. 

我们实际是在用两套神经网络运行。一般会freeze 老的神经网路。

<h2 id="90ded6467b8ae95c15b518af0d6870af"></h2>


# Lecture 7: Policy Gradient

idea : maximum policy objective function J(θ)

---

 - policy object function J(θ) : function of π<sub>θ</sub>(s,a)
    1. start value
    2. average value
    3. average reward per time step 
 - policy gradient
    - ∇<sub>θ</sub> J(θ) 
    - Δθ = α·∇<sub>θ</sub> J(θ)
 - compute policy gradient
    - score function :   d/dxf(x) / f(x)
        - ∇<sub>θ</sub>  π<sub>θ</sub>(s,a) = π<sub>θ</sub>(s,a) **∇<sub>θ</sub> log π<sub>θ</sub>(s,a)**
        - bold part is called : score function
        - what is exactly score function is ?
    - Softmax policy score function : 
        - ∇<sub>θ</sub> log π<sub>θ</sub>(s,a) =  ɸ(s,a) - 𝔼<sub>πθ</sub>[ ɸ(s,·) ]
        - the feature for the action we actually took , minus the average feature for all action might taken.
 - use score function to compute ∇<sub>θ</sub> J(θ) 
    - ∇<sub>θ</sub> J(θ)  = 𝔼<sub>πθ</sub> [ score_function· Q<sup>πθ</sup> (s, a) ]
    - to update θ : 
        - θ ← θ + α·score_function * Q<sup>πθ</sup> (s, a) 
        - using a Critic :  θ ← θ + α·score_function * Q<sub>w</sub> (s, a) 
            - w ← w + β·difference·φ(s, a)
        - use Advantage Function
            - ∇<sub>θ</sub> J(θ)  = 𝔼<sub>πθ</sub> [ score_function· (Q<sub>w</sub>(s, a) - V<sub>v</sub>(s) ) ]
            - In practice we can use an approximate TD error
                - ∇<sub>θ</sub> J(θ)  = 𝔼<sub>πθ</sub> [ score_function· difference_V<sub>v</sub>(s)  ) ]




<h2 id="8d2142fab6a831f4b2392206488d94a9"></h2>


## 1 Introduction

直接将 policy，而不是 value function, 参数化。

Wheneven a state aliasing occurs , a staochastic policy can do better than a deterministic policy.

<h2 id="96854aaa67c2cd550cb2242d152a3824"></h2>


### Policy Objective Functions 

 - start value
    - In episodic environments we can use the start value
    - This basically says, if I always start in some state s1, or have some distribution of start state  s1, what the total reward will I get from that start state almost. 
    - 比如说在atari游戏中，我一直打通关直到最后，然后获得得分。
 - average value
    - In continuing environments we can use the average value
    - Let consider the probability of any state , times the value from that state onwards. So we average over the value of all states. 
    - maybe in s1 ,we got 10 points from that point onwards, in s2 wo got 20 points from that point onwards. So we average those , say, well the objective rewards is 15.
 - Or the average reward per time-step
    - What we really care about is just , let's consider some continuing environments I'm going round round round , now I care about is make sure the per time step I gaining the most reward. So we're not summing there reward over time, we just saying we will take the average of my immediate rewards over the entire distribution of states I visited.
    - so this is basically saying, the objective is there is some probability I'm in some state , some probability I take an action from that state under my policy , and this is the immediate reward that I get at that step. What we care about is getting the most reward per time step. 

这三种方法殊途同归。


<h2 id="db335bb35a59f97ddf493fcd1f74c079"></h2>


### Softmax Policy

we use for discrete actions


The score fuction is just the feature for the action we actually took , minus the average feature for all action might taken. 

So this basically saying, how much more this feature do I have than usual , this is the score function.

When we start doing this kind of policy gradient algorithm , what are we actually doing is saying , if a feature occurs more than usual and gets reward , then we want to adjust the policy to do more 

  ∇<sub>θ</sub> log π<sub>θ</sub>(s,a) 

=  ∇<sub>θ</sub> log ( e<sup>ɸ(s,a)ᵀθ</sup> / ∑e<sup>ɸ(s,a')ᵀθ</sup> ) 

= ∇<sub>θ</sub> log e<sup>ɸ(s,a)ᵀθ</sup> - ∇<sub>θ</sub> log  ∑e<sup>ɸ(s,a')ᵀθ</sup> 

= ∇<sub>θ</sub> ɸ(s,a)ᵀθ - ∑ ∇<sub>θ</sub> ɸ(s,a')ᵀθ

= ɸ(s,a) - ∑ɸ(s,a') = ɸ(s,a) - 𝔼<sub>πθ</sub>[ ɸ(s,·)]

= ɸ(s,a) - ∑<sub>b</sub> π(b|s,θ)·ɸ(s,b)






<h2 id="c70cfd6d28c91d98dfd6410b3fbbeb44"></h2>


### Gaussian Policy

used in continuous actions space like AIBO.

score function 

 - a : action we actually took
 - μ(s) : mean action ?

<h2 id="51f43739235c39cdfa777a62f8648662"></h2>


### One-Step MDPs

最后一个期望𝔼 , 这是使用 likehood ratios 技巧的要点所在。We start with something which is an expectation, we take the gradient, and recover something which is still an expecation. So this thing is an expectation under a policy , so this is an expectation under start state, next expectation the action we pick is all the gradient to log policy multiply by reward -- the expectation of the score times reward. 

It shows us if we want to increase the objective function, want get more reward, we just need to move in the direction that determine by the score times the reward. 

Again this tell us how to adjust a  policy so that get more or less something , and this tell us what is good or bad. 

So if get a really big reward you want to move in the direction that get more reward. if you get a negative reward, you want to move in the opposite  direction. 

<h2 id="a5656501eabca0acff7cb458bf0c1c13"></h2>


### Policy Gradient Theorem

The policy gradient is basically given by this thing , which is  some expectation of score function , multiplied by the action value Q. So it basically tells you again  how to adjust the policy so to get more or less of that particular action , multiplied by , how good that particular action was. 

<h2 id="a1e378fb40906a1956a68710a611c1d6"></h2>


### Monte-Carlo Policy Gradient (REINFORCE)

利用随机梯度上升算法来优化参数。

 - sample Q
 - so we are gonna be in a state, we start by take the action , add see what return we got. we'd use that to estimate Q. We just plug that in our policy gradient to give us a estimate direction to move. 
 - so every single episode now , in each step , we just adjust parameters a little bit in the direction of the score multiplied by the return we got from that point onwards.

<h2 id="3794e0fc1b829b0ff26b06e8f9a994d9"></h2>


### Puck World Example

 - it's slow. MC policy gradient methods tend to be slow. They're very high varience. 
 - so the rest of this class is going to be about using similar ideas but making them more efficient.

So that's going to bring us to the final family of algorithms -- actor critic methods.

<h2 id="fcb509fd5f5388d2b7ac9755d5ce7f17"></h2>


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


<h2 id="95e4a74a003f412f4a8d513ef0448f11"></h2>


### Estimating the Action-Value Function

 - we can think of this is another form of generalized policy iteration
    - where we start off with a policy , we evaluate that policy using the critic , and then instead of doing greedy policy improvement we're moving a gradient step in some direction to get a better policy. 
    - to choose a first policy , you can pick an arbitrary policy , so you initialize your policy parameters θ however you want. 
    - there's no greedy anymore , no ε really, the policy itself determines how we move around to this environment. 

Now we have the basic idea of actor-critic algorithm. But what we want to do is to make these things better. So we consider now some tricks to make this thing better. 

<h2 id="3acf83ce7914d2b57f2c296114e396dd"></h2>


### Reducing Variance Using a Baseline

So the first trick and perpaps the easiest and best trick is to to reduce vairence using what's called a baseline. 

So the idea is to subtract some baseline function from the policy gradient. and this can actually be done in a way that doesn;t change the direction of ascent. In other words, it changes the variance of the estimator , we can reduce the variance of this thing without changing the expectation. So another way to say that is that what we're going to do is we're going to subtract off some term which looks like this (red at bottom) from our policy gradient. 

 - B(s) is not depend on actino
 - we can pull the gradient ∇ outside of the sum ∑ 

 - advantage function
    - it is something which  tells us how much better than usual is it to take action *a*.

<h2 id="0c31786a0e21f8d28470ba60afa42833"></h2>


### Estimating the Advantage Function (1)

There is an easier way and probably a better way.

<h2 id="882835147fcacb1d7c0593c271657ca1"></h2>


### Estimating the Advantage Function (2)

This is probably the most commonly used variant of the actor critic. 

It uses the following idea which is that the TD error is a sample of the advantage function. 


<h2 id="5d215218c32dde80c225cf454d518f0a"></h2>


### Alternative Policy Gradient Directions

Thereis a really important question in actor-critic algorithms , which is we've used this critic and we just kind of said let's replace the true critic value with some approximation. and we just plugged in that thing and hoped that the gradient that we follow is still correct. But how do we know that is valid? how do we know this is really pushing us in the corrent gradient direction.

The answer is that amazingly if you choose the value function approximation carefully that you use, it is possible to pick a value function approximator that doesn't introduce any bias at all. In other words despite the fact that we don't have a true value function , they were approximating the value function, we can still follow the true gradient , we can be guaranteed to follow the true gradient with our policy update. 


That approach is called compatible function approximation. The main idea is that the features that we use, to have a compatible function approximator , are themselves the score function. we basically build up features for our critic where the features are the score of our policy. 

And if we use that **particular type** of feature , and we use **linear combination** of those feature  then we actually guarantee we don't affect the policy direction , we actually still follow the true gradient direction if we follow there compatible features. 

One last idea this is a recent idea , and a useful idea to know about -- Natural Policy Gradient.





<h2 id="c202e82b2a0d6070b8c852c124c7ea2e"></h2>


## 2 Finite Difference Policy Gradient

<h2 id="afbf6d2252accb977e4273ae3f55bcdd"></h2>


## 3 Monte-Carlo Policy Gradient


<h2 id="3955f668aa01a331d669152fc2a66888"></h2>


## 4 Actor-Critic Policy Gradient

---

<h2 id="50d65004325941be417f9541f49a1314"></h2>


# Lecture 8: Integrating Learning and Planning

<h2 id="8d2142fab6a831f4b2392206488d94a9"></h2>


## 1 Introduction

<h2 id="8bf761ff4e3ea4776a4789487933add1"></h2>


## 2 Model-Based Reinforcement Learning

<h2 id="12aa7b676bf938dcf88b1be11f69ecd7"></h2>


### Back to the AB Example

我们从真实经验出发，建模，我们生成了一个模型，现在我们可以用这个模型 取样 sampled experience。

这种方法的优势是 即使我们只是看到这些 Real Experience，我们都可以在规定的计算量预算下，尽可能多的抽取轨迹样本。

有了模型就等于有了无穷的数据。

所以，我们真实经验出发，建模，sample experience，now let's start final step which is to learn from sampled experience. Apply , say MC learning , to these trajectory.








<h2 id="e73c5eb2c33fbcafd857983c404349b8"></h2>


## 3 Integrated Architectures

<h2 id="964b6e51181c427e77052ef724ce70e6"></h2>


## 4 Simulation-Based Search

---

<h2 id="e296e754e887fb190b7ddbc5999e3ab8"></h2>


# Lecture 9 : 

 - Information state space
    - I'm in the state where I've tried left 3 times and right 1 time.  and we can ask about how good is it to move in this state where the agent has cumulate information. 
    - so I might in a state I've never seen. 

---

<h2 id="9a7a5bf12ece7ccf9d2c7a3d596925ba"></h2>


# Lecture 10: Classic Games







