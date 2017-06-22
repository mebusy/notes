
# 1. RL and MDP

## 1.2 Learning Sequential Decision Making


### Approaching Sequential Decision Making

 - algorithms that deal with the problem of sequential decision making
    1. programming , eg. hard code
    2. search and planning , eg. Deep Blue
    3. **learning**

### Online versus Off-line Learning

 - Online learning performs learning directly on the problem instance
 - Off-line learning uses a **simulator** of the environment as a cheap way to get many training examples for **safe** and **fast** learning.

### Credit Assignment

Is an action  ”good” or ”bad” ? The real problem is that the effect of actions with respect to the goal can be much **delayed**. For example, the opening moves in chess have a large influence on winning the game.

 - **temporal credit assignment** problem
    - Deciding how to give *credit* to the first moves , -- which did not get the immediate reward -- , is a difficult problem called the temporal credit assignment problem.
    - A related problem is the *structural credit assignment* problem
 - **structural credit assignment** problem
    - to distribute feedback over the *structure* representing the agent’s policy.
    - For example, the policy can be represented by a structure containing parameters (e.g. a neural network). Deciding which parameters have to be updated forms the structural credit assignment problem.


## 1.5 Solving MDP

 - model-based
    - DP 
 - model-free 
    1. indirect or model-based RL 
        - to learn the transition and reward model
    2. direct RL
        - temporal credit assignment problem
            - One possibility is to wait until the ”end” and punish or reward specific actions along the path taken. 
            - Instead , **temporal difference learning** 


## 1.7 Reinforcement Learning: Model-Free Solution Techniques

### 1.7.1 Temporal Difference Learning

TD methods learn their value estimates based on estimates of other values, which is called *bootstrapping*.

#### TD(0)

estimates V<sup>π</sup> for some policy π.

#### Q-learning

estimate Q-value functions.

Q-learning is an *off-policy* learning algorithm, which means that while following some exploration policy π, it aims at estimating the optimal policy π<sup>∗</sup>.

Q-learning is exploration-insensitive.  It means that it will converge to the optimal policy regardless of the exploration policy being followed, under the assumption that each state-action pair is visited an infinite number of times, and the learning parameter α is decreased appropriately.

#### SARSA

estimate Q-value functions.  But a *on-policy* algorithm. 

 - This learning algorithm will still converge in the limit to the optimal value function (and policy)
    - under the condition that all states and actions are tried infinitely often and
    - the policy converges in the limit to the greedy policy, i.e. such that exploration does not occur anymore.
 - SARSA is especially useful in non-stationary environments. 
    - In these situations one will never reach an optimal policy. It is also useful if function approximation is used, because off-policy methods can diverge when this is used.

#### Actor-Critic Learning

 - learn on-policy
 - keeps a separate policy independent of the value function
    - The policy is called the actor and the value function the critic. 
 - advantage
    - An advantage of having a separate policy representation is that if there are many actions, or when the action space is continuous, there is no need to consider all actions’ Q-values in order to select one of them. 
    - A second advantage is that they can learn *stochastic* policies naturally. Furthermore, a priori knowledge about policy constraints can be used.

#### Average Reward Temporal Difference Learning

Q-learning can also be adapted to the average-reward framework.  for example in the R-learning algorithm Schwartz.

### 1.7.2 Monte Carlo Methods

 - keep frequency counts on state-action pairs and future reward-sums (returns) and base their values on these estimates.
 - MC methods only require samples to estimate average sample returns.
    - Especially for episodic tasks this can be very useful, because samples from complete returns can be obtained. 
    - exploration is of key importance here, just as in other model-free methods.

---

# 2. Batch Reinforcement Learning

Whereas basic algorithms like Q-learning usually need many interactions until convergence to good policies, thus often rendering a direct application to real applications impos- sible, methods including ideas from batch reinforcement learning usually converge in a fraction of the time

# 7. Reinforcement Learning in Continuous State and Action Spaces

Analytically computing a good policy from a continuous model can be infeasible. 
 
The full problem requires an algorithm to learn how to choose actions from an infinitely large action space to optimize a noisy delayed cumulative reward signal in an infinitely large state space, where even the outcome of a single action can be stochastic. 

## 7.1 Introduction

### 7.1.1 Markov Decision Processes in Continuous Spaces

 - Transition function specifies a probability density function (PDF)
    - ∫<sub>S'</sub> T(s,a,s')ds' = P(s<sub>t+1</sub> ∈ S' | s<sub>t</sub>=s,a<sub>t</sub>=a )
 - It is often more intuitive to describe the transitions through a function that describes the system dynamics
    - s<sub>t+1</sub> = T(s<sub>t</sub>, a<sub>t</sub>) + ω<sub>T</sub>(s<sub>t</sub>, a<sub>t</sub>)
    - where T:SxA → S is a deterministic transition function that returns the expected next state for a given state-action pair
        - and ω<sub>T</sub>(s<sub>t</sub>, a<sub>t</sub>) is a zero-mean noise vector with the same size as the state vector.
    - For example, s<sub>t+1</sub> could be sampled from a Gaus- sian distribution centered at  T(s<sub>t</sub>, a<sub>t</sub>)
  
---

 - The reward function gives the expected reward for any two states and an action. 
    - The actual reward can contain noise:
    - r<sub>t+1</sub> = R( s<sub>t</sub>, a<sub>t</sub>,s<sub>t+1</sub> ) + ω<sub>R</sub>( s<sub>t</sub>, a<sub>t</sub>,s<sub>t+1</sub> ) 

---

 - action-selection policy
    - when action space is discrete :  state dependent probability mass function π : S × A → [0,1], such that :
        - π(s,a) = P(a<sub>t</sub>=a | s<sub>t</sub>=s) and ∑<sub>a∈A</sub> π(s,a) =1 
    - when the action space is also continuous , π(s) represents a PDF on the action space.

### 7.1.2 Methodologies to Solve a Continuous MDP

## 7.2 Function Approximation

### 7.2.1 Linear Function Approximation

#### 7.2.1.1 Discretizing the State Space: Tile Coding

#### 7.2.1.2 Issues with Discretization

 - the resulting function that maps states into features is not injective. 
 - In other words, φ(s) = φ(s′) does not imply that s = s′. 

--- 

 - Example : Consider a state space S = ℝ that is discretized such that 
    - ɸ(s) = (1,0,0)ᵀ , if s ≤ -2
    - ɸ(s) = (0,1,0)ᵀ , if -2 ≤ s ≤ 2
    - ɸ(s) = (0,0,1)ᵀ , if s ≥ -2
 - The action space is A = {-2,2}
 - the transition function is s<sub>t+1</sub> = s<sub>t</sub> + a<sub>t</sub> and the initial state is s₀ = 1.
 - The reward is defined by
    - r<sub>t+1</sub> =1 , if s<sub>t</sub> ∈ (-2.2)
    - r<sub>t+1</sub> =-1 , otherwise. 
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_f7.2.png)
 - In this MDP, it is optimal to jump back and forth between the states s = −1 and s = 1
    - However, if we observe the feature vector (0,1,0)ᵀ , 
    - we can not know if we are in s = −1 or s = 1 and we cannot determine the optimal action.

---

## TODO

---

# 9 Hierarchical Approaches

## 9.1 Introduction

### Four-Room Task

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_4_room_task.png)

 - the actions are stochastic
    - a 20% chance that it will stay in place
    - If the agent moves into a wall it will remain where it is.
 - If we can find a policy to leave a room, say by the North doorway, then we could reuse this policy in any of the rooms because they are identical.
 - We proceed to solve two smaller reinforcement learning problems
    - one to find a room-leaving policy to the North
    - another to leave a room through the West doorway.
 - also formulate and solve a higher-level reinforcement learning problem 
    - use only the 4 room-states. In each room-state we allow a choice of executing one of the previously learnt room-leaving policies : West or North leaving.
    - these policies are viewed as *temporally extended* actions because once they are invoked they will usually persist for multiple time-steps until the agent exits a room.
    - At this stage we simply specify a reward of -1 per room-leaving action 
 - The above example hides many issues that HRL needs to address, including: 
    - safe state abstraction
    - appropriately accounting for accumulated sub-task reward
    - optimality of the solution
    - specifying or even learning of the hierarchical structure itself

## 9.2 Background

### 9.2.1 Abstract Actions

 - Abstract actions may execute a policy for a smaller Markov Decision Problem
 - When executing an abstract action a stochastic transition function will make the sequence of states visited non-deterministic
 - The sequence of rewards may also vary , even if the reward function itself is deterministic. 
 - Finally, the time taken to complete an abstract action may vary.
 - Special case abstract actions that terminate in one time-step are just ordinary actions and we refer to them as **primitive** actions.

### 9.2.2 Semi-Markov Decision Problems

 - MDPs that include abstract actions are called **SMDPs**
 - We denote the random variable N ≥ 1 to be the number of time steps that an abstract action *a* takes to complete,starting in state s and terminating in state s′.
    - The model of the SMDP now includes the random variable N.
 - Transition function T : S × A × S × N → [0,1] gives the probability of the abstract action *a* terminating in state s′ after N steps, having been initiated in state s.
    - T(s,a,s',N) = Pr{ s<sub>t+N</sub>=s' | s<sub>t</sub>=s,a<sub>t</sub>=a }
 - The reward function R : S × A × S × N → R that gives the expected discounted sum of rewards when an abstract action *a* is started in state s and terminates in state s′ after N steps is: 
    - R(s,a,s',N) = E{ ∑<sub>n=</sub><sup>N-1</sup>₀ γⁿ·r<sub>t+n</sub> | s<sub>t</sub>=s,a<sub>t</sub>=a ,s<sub>t+N</sub>=s' }
    - The reward function for an abstract action accumulates single step rewards as it executes.
 - The value functions and Bellman “backup” equations for MDPs can also be generalized for SMDPs. 
    - If the abstract action executed in state s is π(s), persists for N steps and terminates we can write the value function as two series - the sum of 
        - the rewards accumulated for the first N steps 
        - and the remainder of the series of rewards.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_r_2_parts.png)
    - the second series is just the value function starting in s′ discounted by N steps, we can write 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_r_2_parts2.png)
 - other value function are also similar :
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_v_optimal.png)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_q_pi.png)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_q_optimal.png)
 - For problems that are guaranteed to terminate, the discount factor γ can be set to 1. ( abstract action ?)
    - In this case the number of steps N can be marginalised out in the above equations and the sum taken with respect to s alone.
    - The equations are then similar to the ones for MDPs with the expected primitive reward replaced with the expected sum of rewards to termination of the abstract action.
    - All the methods developed for solving MDP for reinforcement learning using primitive actions work equally well for problems using abstract actions. 
        - As primitive actions are just a special case of abstract actions

### 9.2.3 Structure

**Task Hierarchies** 

 - The root-node is a top-level SMPD, that can invoke its child-node SMDP policies as abstract actions
 - Child-node policies can recursively invoke other child subtasks
 - right down to sub-tasks that only invoke primitive actions

Task Hierarchies 只是一个限制调用关系的结构。 和 subtask并没有直接对应关系。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_4room_TH.png)

> Fig 9.2

### 9.2.4 State Abstraction

 - There are broadly two kinds of conditions under which state-abstractions can be introduced
     - we can eliminate irrelevant variables, and
     - where abstract actions “funnel” the agent to a small subset of states.

  
**Eliminating Irrelevant Variables**

 - algorithms will learn the same value-function or policy for all the redundant states.
    - eg. navigating through a red coloured room may be the same as for a blue coloured room
    - but a value function and policy treats each (position-in-room,colour) as a different state.
    - it would simplify the problem by eliminating the colour variable from consideration.


**Funnelling**

 - Funnelling allows the four-room task to be state-abstracted at the root node to just 4 states because
 - the abstract actions have the property of moving the agent to another room state,  irrespective of the starting position in each room

### 9.2.5 Value-Function Decomposition

 - The task-hierarchy for the four-room task  has 2 successful higher- level policies that will solve that whole problem.
     1. North-West-North
     2. West-North-North
 - The 2nd one is the shorter path,  but the simple hierarchical RL in section 9.1 can not make this distinction.
    - -1 for abstract action in section 9.1
 - What is needed is a way to decompose the value function for the whole problem over the task-hierarchy.
 - For four-room task , We need both the room- state and the position-in-room state to decide on the best action.
 - The question now arises as to how to decompose the original value function given the task-hierarchy so that the optimal action can be determined in each state.
    - MAXQ approach use a two part decomposition of the value function
        1. the value to termination of the abstract action
        2. the value to termination of the subtask

### 9.2.6 Optimality

 - Hierarchically Optimal
    - maximise the overall value function consistent with the constraints imposed by the task-hierarchy
    - eg. In 4-room task , assume that the agent moves with a 70% probabil- ity in the intended direction, but slips with a 10% probability each of the other three directions. 
    - Executing the hierarchical optimal policy for the task-hierarchy shown in Figure 9.2 may not be optimal. 
        - The top level policy will choose the West room- leaving action to leave the room by the nearest doorway.
        - If the agent should find itself near the North doorway due to stochastic drift, it will nevertheless stubbornly persist to leave by the West doorway , as dictated by the policy of the West room-leaving abstract action. 
    - The task-hierarchy could once again be made to yield the optimal solution if we included an abstract action that was tasked to leave the room by either the West or North doorway.

 - Recursively Optimal
    - sub-task policies to reach goal terminal states are *context free* ignoring the needs of their parent tasks.
    - This formulation has the advantage that sub-tasks can be re-used in various contexts, but they may not therefore be optimal **in each situation**.
    - globally Optimal > Hierarchically Optimal  > Recursively Optimal


## 9.3 Approaches to Hierarchical Reinforcement Learning (HRL)

 
### 9.3.3 MAXQ

 - MAXQ is an approach to HRL where the value function is decomposed over the task hierarchy
 - It can lead to a compact representation of the value function and makes sub-tasks *context-free* or portable.

---

 - abstract actions
    - are crafted by classifying subtask terminal states as either goal states or non-goal states.
    - Using disincentives for non-goal states, policies are learnt to encourage termination in goal states.
 - state value
    - represents the value of a state as a decomposed sum of sub-task completion values plus the expected reward for the immediate primitive action. 
        - completion value: the expected (discounted) cumulative reward to complete the sub-task after taking the next abstract action.
 

---

 - recall Q<sup>π</sup> for SMDP:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_q_pi.png)
 - for a particular sub-task *m*: 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_q_pi_subtask.png)
 - Abstract action *a* for subtask *m*  ( subtask is a path, eg. root 4-room problem has an abstract action which policy is EAST-NORTH-NORTH,so it contain 3 subtask ) invokes a child subtask *mₐ*.
    - expected value of completing subtask *mₐ* ：V<sup>π</sup>(mₐ,s) ,The *hierarchical policy*, π , is a **set of policies**, one for each subtask. 
        - 完成第一个subtask的value, 理解成一个 small MDP的 immediate reward
    - *completion function* C<sup>π</sup>(m,s,a) : expected discounted cumulative reward  
        - after completing abstract action *a* , in state *s* in subtask *m* , to the end of subtask *m*.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_cv_subtask.png)
        - 完成剩余subtask的 value , 理解成一个small MDP 的discounted 部分
 - now the Q function for *m* can be expressed recursively as **the value for completing mₐ** , plus the **completion value to the end of subtask m**.
    - Q<sup>π</sup>(m,s,a) = V<sup>π</sup>(mₐ,s) + C<sup>π</sup>(m,s,a)
 - V<sup>π</sup>(mₐ,s) depends on wheter it is primitive or not 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_vpi_ma.png)
 - If the path of activated subtasks from root subtask m₀ to primitive action m<sub>k</sub> is m₀,m₁,...,m<sub>k</sub>  , and the hierarchical policy specifies that in subtask mᵢ, π(s) =aᵢ, then 
    - Q<sup>π</sup>(m₀,s,π(s)) = V<sup>π</sup>(m₁,s) + C<sup>π</sup>(m₀,s,a₀)
    - = V<sup>π</sup>(m₂,s) + C<sup>π</sup>(m₁,s,a₁) + C<sup>π</sup>(m₀,s,a₀)
    - = ...
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_q_pi_02k.png)
 - optimal greedy policy
    - V<sup>\*</sup>(mₐ,s) = max<sub>a'</sub> Q<sup>\*</sup>(mₐ,s,a')

---

Algorithm 18 performs  a depth-first search and returns both the value and best action for subtask m in state s.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/RL_AOS_SMDP_Algorithm18.png)

> Algorithm 18. Evaluate(m,s)

 - As the depth of the task-hierarchy increases, this exhaustive search can become prohibitive.
 - Limiting the depth of the search is one way to control its complexity
 - For example, to plan an international trip,the flight and airport- transfer methods need to be considered, but ignore which side of the bed to get out of on the way to the bathroom on the day of departure, for higher level planning.














 

 





