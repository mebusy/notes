
# Maxq 


 
# 3. The MAXQ Value Function Decomposition
 
## 3.1 Taxi example

**subtasks** : Each of following subtasks is defined by a subgoal, and each subtask terminates when the subgoal is achieved.

 - Navigate(t)
    - the goal is to move the taxi from its current location to one of the four target locations,
    - which will be indicated by the formal parameter t.
 - Get
    - the goal is to move the taxi from its current location to the passenger’s current location and pick up the passenger.
 - Put
    - The goal of this subtask is to move the taxi from the current location to the passenger’s destination location and drop off the passenger.
 - Root
    - This is the whole taxi task.


After defining these subtasks, we must indicate for each subtask which other subtasks or primitive actions it should employ to reach its goal. 

 - the Navigate(t) subtask should use the four primitive actions North, South, East, and West
 - The Get subtask should use the Navigate subtask and the Pickup primitive action

All of this information can be summarized by a directed acyclic graph called the ***task graph***

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_taxi_task_graph.png)
 - each node corresponds to a subtask or a primitive action
    - each subtask will executes its policy by calling child subroutine 
 - each edge corresponds to a potential way in which one subtask can "call" one of its child tasks
 - this collection of policies is called *hierarchical policy* 
    - In a hierarchical policy, each subroutine executes until it enters a terminal state for its subtask.

## 3.2 Definitions

 - given MDP M 
 - decomposed M into a finite set of subtasks { M₀,M₁,...,M<sub>n</sub> }
    - with the convention that M₀ is the root task

**Definition 2** An unparameterized subtask is a *3-tuple* , < Tᵢ,Aᵢ,R̃ᵢ  > 

 - Tᵢ is a termination predicate *that partitions S into a set of active states, Sᵢ, and a set of terminal states, Tᵢ*
    - The policy for subtask Mᵢ can only be executed if current state *s* is in *Sᵢ*.
    - If , at any time Mᵢ is being executed, the MDP enters a state in Tᵢ , then Mᵢ terminates immediately , even if it is still executing a subtask
 - Aᵢ is a set of actions that can be performed to achieve subtask Mᵢ.
    - can either be primitive action from A
    - or can be other subtasks , which we will denote by their indexes i.
    - Aᵢ define a direct graph over subtasks
        - no subtask can invoke itself recursively either directly or indirectly.
    - If a child subtask Mⱼ has formal parameters, then this is interpreted as if the subtask occurred multiple times in Aᵢ 
    - Aᵢ may differ from one state to another , and from on set of actual parameter values to another 
        - so Aᵢ is a function of *s and actual parameters*. 
 - R̃ᵢ(s')  is the pseudo-reward function,which specifies a (deterministic) pseudo-reward for each transition to a terminal state s' ∈ Tᵢ 
    - This pseudo-reward tells how desirable each of the terminal states is for this subtask.
    - It is typically employed to give goal terminal states a pseudo-reward of 0 and any non-goal terminal states a negative reward.
    - By definition, the pseudo-reward R̃ᵢ(s) is also zero or all non-terminal states s. 
    - The pseudo-rewardis only used during learning, so it will not be mentioned further until Section 4.
    - primitive action is alwasy executable, it always terminates immediately after execution, and its pseudo-reward function is uniformly zero.


If a subtask has formal parameters, and b specifies the actual parameter values for task Mᵢ, Then we can define a parameterized termination predicate Tᵢ(s,b) and and a parameterized pseudo-reward function R̃ᵢ(s,b).

It should be noted that if a parameter of a subtask takes on a large number of possible values, this is equivalent to creating a large number of different subtasks, each of which will need to be learned. It will also create a large number of candidate actions for the parent task, which will make the learning problem more difficult for the parent task as well.


**Definition 3** A hierarchical policy ,π, is a set containing a policy for each of the subtasks in the problem: π = { π₀,π₁,...,π<sub>n</sub> }.

Each subtask policy πᵢ takes a state and returns the name of a primitive action to execute , or the name of a subroutine to invoke (and binding for its formal parameters). 




