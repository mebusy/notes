
# MAXQ-OP

 - a novel online planning algorithm for large MDPs
    - that utilizes MAXQ hierarchical decomposition in online settings.
 - able to reach much more deeper states in the search tree with relatively less computation time
    - by exploiting MAXQ hierarchical decomposition online

# Introduce 

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


