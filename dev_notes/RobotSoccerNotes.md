
# MAXQ-OP

 - a novel online planning algorithm for large MDPs
    - that utilizes MAXQ hierarchical decomposition in online settings.
 - able to reach much more deeper states in the search tree with relatively less computation time
    - by exploiting MAXQ hierarchical decomposition online

# 1. Introduce 

 - offline MDP not works for soccer 
    - state space is too large
        - even ignoring some less important state variables  
            - e.g., stamina and view width for each player
        - the ball state takes four variables x, y, ẋ, ẏ
        - each player state takes six variables, (x, y, ẋ, ẏ, α, β), 
            - where (x, y), (ẋ, ẏ), α, and β are position, velocity, body angle, and neck angle, respectively. 
    - the *dimensionality* of the resulting state space is 22 × 6 + 4 = 136
    - All state variables are continuous
    - we obtain a state space containing 10⁴⁰⁸ states, if we discretize each state variable into only 10³ values
    - even worse, the transition model of the problem is subject to change given different opponent teams. 
 - online algorithms alleviate this difficulty
    - by focusing on computing a near-optimal action merely for the current state. 
    - The key observation is that an agent can only encounter a fraction of the overall states when interacting with the environment
        - eg. the total number of timesteps for a match is normally 6000
        - the agent has to make decisions only for those encountered states
        - Online algorithms evaluate all available actions for the current state and select the seemingly best one by recursively performing forward search over reachable state space.
            - 值得指出的是，在搜索过程中采用启发式技术以减少时间和内存使用并不常见，就像依赖前向搜索的许多算法一样，如实时动态规划和UCT
    - online algorithms can easily handle unpredictable changes of system dynamics
        - because in online settings, we only need to tune the decision making for a single timestep instead of the entire state space
    - However, the agent must come up with a plan for the current state in almost real time 
        - because computation time is usually very limited for online decision making 
        - (e.g., only 100ms in RoboCup 2D). 
 - Hierarchical decomposition scale MDP algorithms to large problems
    - decomposes the value function of the original MDP into an additive combination of value functions for sub-MDPs arranged over a task hierarchy
    - MAXQ advantages
        - temporal abstraction
            - temporally extended actions 时间上延伸的动作 (also known as options, skill, or macroactions) are treated as primitive actions by higher-level subtasks. 
        - state abstraction
            - aggregates the underlying system states into macrostates by eliminating irrelevant state variables for subtasks. 
            - 通过消除子任务的不相关状态变量将基础系统状态聚合成宏状态。
        - subtask sharing
            - 子任务计算策略 重用
        - For example, in RoboCup 2D, attacking behaviors generally include passing, dribbling, shooting, intercepting, and positioning. Passing, dribbling, and shooting share the same kicking skill, whereas intercepting and positioning utilize the identical moving skill. 
 - MAXQ-OP MAXQ value function decomposition for online planning
    - performs online planning to find the near-optimal action for the current state
    - while exploiting the hierarchical structure of the underlying problem. 

---

 - online algorithms find a near-optimal action for current state via forward search incrementally in depth
 - However, it is difficult to reach deeper nodes in the search tree within domains with large action space , while keeping the appropriate branching factor to a manageable size.  
    - 比如： 球员们需要很长时间才能收获一个进球
 - Hierarchical decomposition enables the search process to reach deeper states using temporally abstracted subtasks -- a sequence of actions that lasts for multiple timesteps
    - For example, when given a subtask called *moving-to-target* , the agent can continue the search process starting from the target state ,without considering the detailed plan on specifically moving toward the target , just assuming that *moving-to-target* can take care of this.
 - One advantage of MAXQ-OP 
    -  do not need to manually write down complete local policy for each subtask 
    - Instead, build a MAXQ task hierarchy by defining well the active states, the goal states, and optionally the local-reward functions for all subtasks.
    - Local-reward functions are artificially introduced by the programmer to enable more efficient search processes,as the original rewards defined by the problem
    may be too sparse to be exploited.
 - Given the task hierarchy, MAXQ-OP automatically finds the near-optimal action for the current state by simultaneously searching over the task hierarchy and building a forward search tree.
 - a *completion function* for a task gives the expected cumulative reward obtained , after finishing a subtask but before completing the task itself following a hierarchical policy.
 - Directly applying MAXQ to online planning requires knowing in advance the completion function for each task, following the recursively optimal policy.
 - Thus, obtaining the completion function is equivalent to solving the entire task which is not applicable in online settings.
    - This poses the major challenge of utilizing MAXQ online.

--- 

 - 2 major work
    - exploit the MAXQ hierarchical structure online
    - approximation method made for computing the completion function online.

---

# 2. RELATED WORK

 - online planning for MDPs
    - RTDP : real-time dynamic programming
        - tries to find a near-optimal action for the current state by conducting a trial-based search process
        - with greedy action selection and an admissible heuristic
    - AO\*
        - 与或图的启发式搜索算法
    - Monte Carlo tree search (MCTS)
        - combining tree search methods with Monte Carlo sampling techniques
    -  trial-based heuristic tree search (THTS)
 - they do not exploit the underlying hierarchical structure of the problem

---

 -  hierarchical reinforcement learning (HRL)
    - HRL aims to learn a policy for an MDP efficiently by exploiting the underlying structure while interacting with the environment.
    - One common approach is using state abstraction to partition the state space into a set of subspaces, namely ***macrostates***, by eliminating irrelevant state variables
    - In particular, Sutton model HRL as a semi-Markov decision process (SMDP) by introducing temporally extended actions, namely ***options***
        - Each option is associated with an inner policy that can be either manually specified or learned by the agent
    - MAXQ-based HRL methods convert the original MDP into a hierarchy of SMDPs and learn the solutions simultaneously 
 - challenge of hierarchical decomposition
    - when searching with high-level actions (tasks), it is critical to know how they can be fulfilled by low-level actions (subtasks or primitive actions).
        - For example, if a player wants to shoot the goal (high-level action), it must first know how to adjust its position and kick the ball toward a specified position (low-level actions).  
        - Unfortunately, this information is not available in advance during online planning
        - we address this challenge by introducing a termination distribution for each subtask over its terminal states and assuming that subtasks will take care of the local policies to achieve the termination distributions. 


# 3. Background

## 3.1 MDP

 - we assume that there exists a set of goal states G ⊆ S
    - for all g ∈ G and a ∈ A, we have T(g | g, a) = 1 and R(g, a) = 0
 - If the discount factor γ = 1 , the resulting MDP is then called *undiscounted goal-directed* MDP
 - It has been proved that any MDP can be transformed into an equivalent undiscounted negative-reward goal-directed MDP where the reward for nongoal states is strictly negative

## 3.2. MAXQ Hierarchical Decomposition

 - decomposes the original MDP M into a set of sub-MDPs arranged over a hierarchical structure
 - Each sub-MDP is treated as an macroaction for high-level MDPs
 - Specifically, let the decomposed MDPs be {M₀, M₁,..., Mn}, then M₀ is the root subtask such that solving M0 solves the original MDP M
 - Each subtask Mᵢ is defined as a tuple < τᵢ, Aᵢ, R̃ᵢ >
    - τᵢ: *termination predicate*  
        - partitions the state space into a set of active states Sᵢ, and a set of terminal states Gᵢ ( also known as subgoals )
    - Aᵢ: is a set of (macro)actions that can be selected by Mᵢ 
        - which can either be ***primitive actions*** of the original MDP M or ***low-level subtasks***  .
    - R̃ᵢ: (optional) *local-reward* function
        - specifies the rewards for transitions from active states Sᵢ to terminal states Gᵢ
 - A subtask can also take parameters
    -  different bindings of parameters specify different instances of a subtask
 - 












