
# RL David Silver

https://search.bilibili.com/all?keyword=David%20Silver%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0&page=1&order=totalrank&tids_1=36


http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html



# Lecture Introduction 

## Agent and Environment

所有 agent 都有两个输入： observation and reward. 这些输入共同决定 下一步措施。


## History and State

Histroy is huge. It is normally not useful. 

State is the information used to determine what happens next

Formally, **state is a function of the history**:  s<sub>t</sub> = f(H<sub>t</sub>)

### Environment State

Sᵉ<sub>t</sub>

 - The environment state is not usually visible to the agent
 - Even if it is visible, it may contain irrelevant information


something about multi-agents

 - for each agent, it can consider all other agents and their interacting with environment to be a part of environment. 


### Agent State 

sª<sub>t</sub> = f(H<sub>t</sub>) 


### Information State

information state , a.k.a Markov state

 - The environment state is Markov
 - The history H<sub>t</sub> is Markov

## Fully Observable Environments

 - Full observability: agent **directly** observes environment state
    - O<sub>t</sub> = Sª<sub>t</sub> = Sᵉ<sub>t</sub>
 - Agent state = environment state = information state
 - Formally, this is a Markov decision process (MDP)

## Partially Observable Environments

 - Partial observability: agent **indirectly** observes environment:
    - A robot with camera vision isn’t told its absolute location
    - A trading agent only observes current prices
    - A poker playing agent only observes public cards
 - Now agent state != environment state
 - Formally this is a **partially observable Markov decision process**  (POMDP)
 - Agent must construct its own state representation Sª<sub>t</sub> , how to do that ? We have many ways :
    - Complete history: Sª<sub>t</sub> = H<sub>t</sub>
    - **Beliefs** of environment state: 
    - Recurrent neural network

## Policy

 - Deterministic policy: a = π(s)
 - Stochastic policy: π(a|s) = P(A<sub>t</sub>=a | s<sub>t</sub>=s)

## Value Function

 - Value function is a prediction of future reward

## Model
 
 - A model predicts what the environment will do next
 - Transitions:  P predicts the next state
 - Rewards: R predicts the next (immediate) reward, e.g.
 - Model is not necessary.

## Categorizing RL agents 1

 - Value Based
    - ~~No Policy (Implicit)~~  (can get the optimal action by do 1-step expectimax search)
    - Value Function
 - Policy Based
    - Policy
    - ~~No Value Function~~ 
 - Actor Critic
    - Policy
    - Value Function


## Categorizing RL agents 2

 - Model Free
    - Policy and/or Value Function
    - ~~No Model~~
 - Model Base
    - Policy and/or Value Function
    - Model

---

## Learning and Planning

Two fundamental problems in sequential decision making

 - Reinforcement Learning:
    - The environment is initially unknown
    - The agent interacts with the environment
    - The agent improves its policy
 - Planning:
    - A model of the environment is known
    - The agent performs computations with its model (without any external interaction)
    - The agent improves its policy
    - a.k.a. deliberation, reasoning, introspection, pondering, thought, search

## Prediction and Control

 - Prediction: evaluate the future
    - Given a policy
 - Control: optimise the future
    - Find the best policy

---

# Lecture 2 : MDP

## Introduction to MDPs

 - MDP formally describe an environment for reinforcement learning 
    - Where the environment is fully observable
    - i.e. The current state completely characterises the process
        - state 特征化了 我们所需要知道的一切
 - Almost all RL problems can be formalised as MDPs, e.g
    - Optimal control primarily deals with continuous MDPs
    - Partially observable problems can be converted into MDPs
    - Bandits are MDPs with one state

## Markov Process

 - A Markov process is a memoryless random process,
 - A Markov Process (or Markov Chain) is a tuple ( S,P )
    - S is a (finite) set of states
    - P is a state transition probability matrix

## Markov Reward Process

 - A Markov Reward Process is a tuple ( S ,P , R , γ )
    - R is a reward function , R<sub>s</sub> = 𝔼( R<sub>t+1</sub> | S<sub>t</sub>=s )
    - γ is a discount factor, γ ∈ [0, 1]

### Return

 - the return G<sub>t</sub> t is the total discounted reward from time-step t
    - G<sub>t</sub> = R<sub>t+1</sub> + γR<sub>t+2</sub> + ... 
    - why here is no expectation ?
        - because here G is just one sample from our MRP , later we will talk about expectation.
    - The value of receiving reward R afte k + 1 time-steps is γᵏR.
    - This values immediate reward above delayed reward.
        - γ close to 0 leads to ”myopic” evaluation
        - γ close to 1 leads to ”far-sighted” evaluation

 - Most Markov reward and decision processes are discounted
 - It is sometimes possible to use undiscounted Markov reward processes
    - if all sequences terminate


## MRP Value Function

 - state-value function  v(s)
 - action-value function  q(s,a)

value is expectation because the environment is stochastic.


## Bellman Equation for MRPs

The value function can be decomposed into two parts:

 - immediate reward R<sub>t+1</sub>
 - discounted value of successor state γ·v(S<sub>t+1</sub>)

## Bellman Equation in Matrix Form

Bellman Equation for MRPs has no concept of maximum. So t can be expressed concisely using matrices. And here the bellman exuation is a linear equation , as a result it can be solved directly. It is not true when we meet MDP.

 - Direct solution only possible for small MRPs
 - There are many iterative methods for large MRPs, e.g.
    - Dynamic programming
    - Monte-Carlo evaluation
    - Temporal-Difference learning

## Markov Decision Process

 - A Markov decision process (MDP) is a Markov reward process with decisions. 
 - It is an environment in which all states are Markov
 - ( S , **A**,  P , R , γ )

 - Given an MDP M= ( S , A,  P , R , γ ) , and a policy π 
    - The state sequence S1, S2, ... is a Markov process (S,P<sup>π</sup>)
    - The state and reward sequence S1,R2,S2, ... is is a Markov reward process ( S,P<sup>π</sup>, R<sup>π</sup>, γ  )

### MDP Value Function

you can get different rewards. It is not one expectation any more , there are different expectations depending how we act

### MDP Bellman Expectation Equation

 - The state-value function can again be decomposed into immediate reward plus discounted value of successor state,
 - The action-value function can similarly be decomposed

With a fixed policy π,  MDP Bellman Expectation Equation can also be expressed concisely using matrices.

## Optimal Value Function

v<sup>\*</sup> is the maximum value function over all policies.


v<sup>\*</sup> is the maximum, q<sup>\*</sup> is the average (expectation).

## Solving the Bellman Optimality Equation

 - Value Iteration
 - Policy Iteration
 - Q-learning
 - Sarsa

---


# Lecture 3:  Planning by Dynamic Programming



