
# Maxq 


 ![][1] 

 
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

```
s → πᵢ |→ primitive action
       |→ subroutine
```

A subtask policy is a deterministic "option" , and its probability of terminating in state *s* (denote by β(s) ) is 0 if s∈Sᵢ , and 1 if s∈Tᵢ.

In a parameterized task,

```
        s → πᵢ |→ chosen action a
parameter ↑    |→ parameter of a
```

```python
def EXECUTEHIERARCHICALPOLICY(pi):
    ...
```


It is sometimes useful to think of the contents of the stack as being an additional part of the state space for the problem. Hence, a hierarchical policy implicitly defines a mapping from the current state s<sub>t</sub> and current stack contents K<sub>t</sub> to a primitive action a.

This action is executed, and this yields a resulting state s<sub>t+1</sub> and a resulting stack contents K<sub>t+1</sub>. 

Because a hierarchical policy maps from states *s* and stack contents K to actions, the value function for a hierarchical policy must assign values to combinations of states *s* and stack contents K.


**Definition 4**  A hierarchical value function, V<sup>π</sup>( (s,K) ) , gives the expected cumulative reward of following the hierarchical policy π starting in state *s* with stack contents K . 

 - This hierarchical value function is exactly what is learned by HAMQ 
 - in this paper, we will focus on learning only the *projected value functions* of each of the subtasks M₀,M₁,...,M<sub>n</sub> in the hierarchy.

**Definition 5** The projected value function of hierarchical policy π on subtask Mᵢ , V<sup>π</sup>(i,s) , is the expected cumulative reward of executing πᵢ ( and the policies of all descendents of Mᵢ ) starting in state *s* until Mᵢ terminiates.

---

The purpose of the MAXQ value function decomposition is to decompose V(0,s) (the projected value function of the root task) in terms of the projected value function V(i,s) of all of the subtasks in the MAXQ decomposition.

## 3.3 Decomposition of the Projected Value Function

The decomposition is based on the following theorem:

**Theorem 1** Given a task graph over tasks M₀,M₁,...,M<sub>n</sub>  and a hierarchical policy π, each subtask Mᵢ defines a semi-MDP with state Sᵢ, actions Aᵢ, probability transition function P<sup>π</sup>ᵢ(s',N | s,a) , and expected reward function R̅(s,a) = V<sup>π</sup>(a,s) , where  V<sup>π</sup>(a,s) is the projected value function for child task Mₐ in state *s*. 

 - If a is a primitive action, V<sup>π</sup>(a,s) is defined as the expectedimmediate reward of executing a in s:
    - V<sup>π</sup>(a,s) = ∑<sub>s'</sub> P(s'|s,a)·R(s'|s,a).

**Proof**: 

Let's write out the value of V<sup>π</sup>(i,s): 

  V<sup>π</sup>(i,s) = E{ r<sub>t</sub> + γr<sub>t+1</sub> + γ²r<sub>t+2</sub> + ... | s<sub>t</sub> = s, π }   (5)

The sum continues until the subroutine for task Mᵢ enters a state in Tᵢ.

Now let us suppose that the first action chosen by πᵢ is a subroutine *a* . This subroutine is invoked, and it executes for a number of steps N and terminates in state s' according to P<sup>π</sup>ᵢ(s',N | s,a) . We can rewriet Equation (5) as : 

  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_eq_6.png)

 - the first part of equation 6  is the discounted sum of rewards for executing subroutine *a* in state *s* until it terminates
    - in other words, it is V<sup>π</sup>(a,s), the projected value function for the child task Mₐ.
 - the 2nd term of the equation is the value of s' for the current task i , V<sup>π</sup>(i,s') , discounted by γᴺ , where s' is the current state when subroutine *a* terminates.

We can write this in the form of a Bellman equation :

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_eq_7.png)

 - This has the same form as Equation (3)
 - the first term is the expected reward R̅(s,π(s)). Q.E.D.

---


To obtain a hierarchical decomposition of the projected value function, let us switch to the action-value (or Q) representation. 

Let Q<sup>π</sup>(i,s,a) be the expected cumulative reward for subtask Mᵢ of performing action *a* in state *s* , end then following hierarchical policy π until Mᵢ terminates.  We can re-state Equation (7) as follows:

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_eq_8.png)

 - difference from V<sup>π</sup>(i,s):
    - V: Mₐ is provided by πᵢ(s)
    - Q: Mₐ is chosen
 - then 2nd term is the expected discounted reward of *completing task* Mᵢ after executing action *a* in state *s*.
    - This term only depends on i, s, and a, because the summation marginalizes away the dependence on s' and N.
    - Let us define C<sup>π</sup>(i,s,a) to be equal to this term:

**Definition 6** The completion function, C<sup>π</sup>(i,s,a) , is the expected discounted cumulative reward of completing subtask Mᵢ after invoking the subroutine for subtask Mₐ in state *s*. The reward is discounted back to the point in time where a begins execution ( \* γᴺ ) .

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_eq_9.png)

With this definition, we can express the Q function recursively as

 Q<sup>π</sup>(i,s,a)  = V<sup>π</sup>(a,s) + C<sup>π</sup>(i,s,a)     (10)

 - 实际上，C<sup>π</sup> is related to *s'*


Finally, we can re-expressthe definition for  V<sup>π</sup>(i,s) as 

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_eq_11.png)

We will refer to equations (9), (10), and (11) as the *decomposition equation*  for the MAXQ hierarchy under a fixed hierarchical policy π. 

These equations recursively decompose the projected value function for the root,  V<sup>π</sup>(0,s) into the projected value functions for
the individual subtasks, M₁,...,M<sub>n</sub>  and the individual completion functions  C<sup>π</sup>(j,s,a) for j=1,...,n. 

Now just the C values for all non-primitive subtasks and the V values for all primitive actions must be stored to represent the value function decomposition.

---

To make it easier for programmers to design and debug MAXQ decompositions, we have developed a graphical representation that we call the MAX Q graph.

 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_taxi_maxq_graph.png)

 - The graph contains two kinds of nodes : Max nodes and Q nodes
 - The Max nodes correspond to the subtasks in the task decomposition
    - There is one Max node for each primitive action and one Max node for each subtask (including the Root) task.
    - Each primitive Max node i stores the value of V<sup>π</sup>(i,s) 
 - The Q nodes correspond to the actions that are available for each subtask
    - Each Q node for **parent** task i, state *s*,  and subtask *a* stores the value of C<sup>π</sup>(i,s,a).
    - eg. QGet shores C<sup>π</sup>(0,s,Get) ??? 
 - The children of any node are unordered ( nothing about the order in which they will be executed )
    - Indeed, a child action may be executed multiple times before its parent subtask is completed.
 - the Max nodes and Q nodes can be viewed as performing parts of the computation 
    - Specifically, each Max node i can be viewed as computing the projected value function V<sup>π</sup>(i,s)  for its subtask. 
    - For primitive Max nodes, this information is stored in the node.
 - Each Q node with parent task i and child task a can be viewed as computing the value of Q<sup>π</sup>(i,s,a) 

 - Q node 保存 C, 用于计算 Q value ; Max node 用来计算 V value (primtive Max node 保存V )

----

 ![][1] 

As an example , consider the situation shown in Figure 1, which we will denote by s₁.

Suppose that the passenger is at R and wishes to go to B. Let the hierarchical policy we are evaluating be an ***optimal*** policy denoted by π ( we will omit the superscript \* to reduce the clutter of the notation) . 

 - The value of this state under π is 10
 - π need 10 units action  (a reward of -10)
    - 1 unit to move the taxi to R
    - 1 unit to pickup the passenge
    - 7 units to move the taxi to B
    - 1 unit to putdown the passenger
 - When the passenger is delivered, the agent gets a reward of +20
 - so the net value is +10

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_taxi_fig4.png)

 - To compute the value V<sup>π</sup>(Root,s₁)  
    - MaxRoot consults its policy and finds that π<sub>root</sub>(s₁) is Get.
    - Hence, it "ask" the Q node , QGet to compute Q<sup>π</sup>(Root,s₁,Get) 
    - The completion cost for the Root task after performing a Get , C<sup>π</sup>(Root,s₁,Get)  , is 12
        - it will cost 8 units to deliver the customer after completing the Get subtask
    - then it must ask MaxGet to estimate the expected reward of performing the Get itself.
 - The policy for MaxGet dictates that in s₁, the Navigate subroutine should be invoked with *t* bound to R 
    - so MaxGet consults the Q node, QNavigateForGet to compute the expected reward.
    - QNavigateForGet knows that after completing the Navigate(R) task, one more action (the Pickup) will be required to complete the Get
        - so C<sup>π</sup>(MaxGet,s₁,Navigate(R)) = -1
    - it then ask MaxNavigate(R) to compute the expected reward of performing a Navigate to location R
 - The policy for MaxNavigate chooses the North action, so MaxNavigate asks QNorth to compute the value.
    - QNorth looks up its completion cost, and finds that C<sup>π</sup>( Navigate, s₁ , North) is 0
        - i.e., the Navigate task will be completed after performing the North action)
    - It consults MaxNorth to determine the expected cost of performing the North action itself.
        - Because MaxNorth is a primitive action, it looks up its expected reward, which is -1
 - Now this series of recursive computations can conclude as follows:  
    - Q<sup>π</sup>( Navigate(R), s₁ , North) = -1 + 0
    - V<sup>π</sup>( Navigate(R), s₁ ) = -1
    - Q<sup>π</sup>( Get, s₁ , Navigate(R) ) = -1 + -1
    - V<sup>π</sup>( Get, s₁ ) = -2
    - Q<sup>π</sup>( Root, s₁ ,Get) = -2 + 12
 - The end result of all of this is that the value of V<sup>π</sup>( Root,s₁ ) is decomposed into a sum of C terms plus the expected reward of the chosen primitive action:
    - V<sup>π</sup>( Root,s₁ ) = V<sup>π</sup>( North,s₁ ) + C<sup>π</sup>( Navigate(R), s₁ , North) + C<sup>π</sup>( Get, s₁ , Navigate(R) ) + C<sup>π</sup>( Root, s₁ ,Get) = -10












---

 [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/maxq_taxi_fig1.png
