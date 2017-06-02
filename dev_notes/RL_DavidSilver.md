
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





