...menustart

 - [Adversarial Search](#6778eced7db02d1b66c03c39306bc708)

...menuend



<h2 id="6778eced7db02d1b66c03c39306bc708"></h2>
# Adversarial Search

## Types of Games

 - Axes
    - Deterministic or stochastic?
    - One, two, or more players?
    - Zero sum?
    - Perfect information (can you see the state)?

 
 We will talk about zero sum and deterministic games. They are games of perfect information.

Think about how this is different from search. 

In search I gave you the search problem , and what you gave me back is a plan or path it is a sequences of actions that executed and it was guaranteed to succeed.

That's not going to work here because we don't control our opponent. So we can't just give a plan that guarantes to succeed. What we need to do is we need a function which tells us in any given state what to do . That is the **policy** in the game case it's often called strategy. 


## Deterministic Games

 - Many possible formalizations, one is:
    - States: S (start at s₀)
    - Players: P={1...N} (usually take turns)
    - Actions: A (may depend on player / state)
    - Transition Function: SxA →S
    - Terminal Test: S →{t,f}
    - Terminal Utilities: SxP →R
        - Terminal Utilities:  this tell us for an end-state how much it is worth to each of the players.
 - Solution for a player is a ***policy***: S → A
    - the solution to a game like this is a policy which map states to actions.


## Zero-Sum Games

 Zero-Sum Games | General Games
 --- | --- 
 Agents have opposite utilities (values on outcomes) | Agents have independent utilities (values on outcomes)
 Lets us think of a single value that one maximizes and the other minimizes | Cooperation, indifference, competition, and more are all possible
 Adversarial, pure competition | More later on non-zero-sum games



## Adversarial Search

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_adversarial_search_illustration.png)

we're going to have an agent is trying to figure out what to do. Just like a regular single-agent search. 

Before the way you're going to decide what to do is we're going to think about consquences of our actions. 

The differences rather than thinking about sequence of actions that I can perform , I need think about my opponent. 

So I imagine taking an action and then I imagine my opponent will then be in the situation of thinking about the "opponent" should do.  And they're going to imagine that they're taking an action which I will respond. It will get this enbedded interleaving of our future states. 


---

## Single-Agent Trees

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_single_agent_trees.png)

some of there paths go forever , some of these paths end because it meet the last of the game terminates. 

And what we actually do ? 

We image there is  associated values with this. Let's say this is the best possible outcome where I go straight to the dot ate it. And there are various other outcomes buried further in the other trees and I can associate numbers with them.

In the case of single-agent , I get to pick any outcome I like.  In this  actual search case , showed as the pic , we should make that value-8 outcome happen.


For terminal state the value is known. What about the other ones?  

well in this state I have a choice I can get 8 or I can get whatever is down below the left path (4-n-6). So I can write the value of the state is defined to be the maximum over the values of its children. 

In single-agent case, we choose maximum value.

 - Value of a state: The best achievable outcome (utility) from that state
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_value_of_a_state.png)


---

## Adversarial Game Trees

Let's think about the case where we have an adversary . 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_game_trees.png)

In the state of root , we can still do the same thought : move left or move right. 

The difference now is in each of these possible futures the ghost can move left or right. So there's still the tree of of possible futures. 

So we need to think about now what a value is in the case of an adversary. This is going to give us the idea of a ***minimax*** value. 


## Minimax Values

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimaxValues.png)

8 is still gonna be the best outcome we can achieve under perfect play against an optimal adversary. 

We still know the value of Terminal States. For a state that is under my opponents control I imagine that this ghost is out there to minimize my value , so it will be -10.

---


##  Tic-Tac-Toe Game Tree

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_ticTac_game_tree.png)

Blue one moves first. 

The value of root will be one of { -1,1,0 }.


## Adversarial Search (Minimax)

 - Deterministic, zero-sum games:
    - Tic-tac-toe, chess, checkers
    - One player maximizes result
    - The other minimizes result

 - Minimax search:
    - A state-space search tree
    - Players alternate turns
    - Compute each node’s minimax value: the best achievable utility against a rational (optimal) adversary

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimax.png)

## Minimax Implementation

 - Dispatch

```python
def value(state):
    if the state is a terminal state: return the state’s utility
    if the next agent is MAX: return max-value(state)
    if the next agent is MIN: return min-value(state)
```

 - Minimax Implementation  

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_func_max_value.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_func_min_value.png)



## Minimax Efficiency

 - How efficient is minimax?
    - Just like (exhaustive) DFS
    - Time: O(bᵐ)
    - Space: O(bm)
 - Pacma mple: For chess, b ≈35, m ≈100
    - Exact solution is completely infeasible
    - But, do we need to explore the whole tree?


## Minimax Properties

game sample:

you get points when you win , you get points when you get a dot , you lost a point every step. 

If you play against a perfect player  you want to use minimax but if you are not playing against a player move random  then minimax is going to be overly pessimistic. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_minimax_properties.png)


## Resource Limits

 - Problem: In realistic games, cannot search to leaves!
 - Solution: Depth-limited search
    - Instead, search only to a limited depth in the tree
    - Replace terminal utilities with an evaluation function for non-terminal positions
 - Example:
    - Suppose we have 100 seconds, can explore 10K nodes / sec
    - So can check 1M nodes per move
    - α-β reaches about depth 8 – decent chess program
 - Guarantee of optimal play is ***gone***
 - More plies makes a BIG difference
 - Use iterative deepening for an anytime algorithm

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_resource_limits.png)


For a chess game, we can't possibly search the whole game tree. Essentially we've got resource limits in this case time. That tell us we can only look forward so far into the tree before the exponential growth of the tree gets this.

So we can only search just some limited depth from the tree. Now the problem is we get to the end of our search we don't have terminal utilities because we are not actually at the end of the game. 

So we need to replace the terminal utilities in the minimax algorithm with what's called evaluation function, which takes a non-terminal position and gives us some estimate of what the terminal utility under that tree would be under minimax plan.


## Depth Matters

 - Evaluation functions are always imperfect
 - The deeper in the tree the evaluation function is buried, the less the quality of the evaluation function matters
 - An important example of the tradeoff between complexity of features and complexity of computation


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_depth_matters.png)


----

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_resource_limitation_pacman_example2.png)

For this example , if we look forward just a couple steps , we're going to need know it won't be able to see actually eating of the dot or any future collisions with the ghost.  We can not see whether or not we can be closer or farther from the dot. But we have to have an evaluation function that says that. 

If we can see all the way into the future , we can see the whole game play out on this board. The critical thing is that the blue ghost is going to go somewhere and once it goes somewhere it's committed. So what we should do now is moving towards the orange ghost because we are still not in any danger.  If you look deeply enough into the tree you see that what this allows you to do is force the blue ghost to make a decision before you have to.


## Evaluation Functions

A function takes a non-terminal state and return some number,just like the heuristic value in Astar search . 

In this case we want that number to return the actual minimax value of that position. That is not going to happen. In practice what peaple do is they try to come up with some function which on average is positive when the minimax value is positive , is negative when the minimax value is negative. 

 - Evaluation functions score non-terminals in depth-limited search
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_eval_func_chess.png)
 - Ideal function: returns the actual minimax value of the position
 - In practice: typically weighted linear sum of features:
    - Eval(s)=w₁f₁(s) + w₂f₂(s) + ... + w<sub>n</sub>f<sub>n</sub>(s)
    - eg. f₁(s)=(num white queens – num black queens), etc.


---

## Why Pacman Starves

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_why_pacman_starves.png)

issue  : starve ( loop in a range  )

danger of replanning agents

the plan they have in their head does not really have to be consistent. Every step you do a new plan. 

10 points for a dot.

The problem is if we take the right branch , look at that state ( right,  2nd level ) , it's just like the state of the root . (1 is a bit left, another is a bit of right) 

so we trash.  


 - A danger of replanning agents!
    - He knows his score will go up by eating the dot now (west, east)
    - He knows his score will go up just as much by eating the dot later (east, west)
    - There are no point-scoring opportunities after eating the dot (within the horizon, two here)
    - Therefore, waiting seems just as good as eating: he may go east, then back west in the next round of replanning!



solution: closer to a dot  score point as well.




---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_adversarial_search_pacman_example2.png)

What's going on here each agent is separately doing their own searches. But they see that the other one constrols , they treat it like min node (???). So even though each agent is actually doing its own search because they are both assuming the other one shares its evaluation function that is also minimax agent. We're goint to see cooperation emerge.

This shows you how you can get cooperation without programming it in, simply they're both trying to achieve the same goal. 


---


## Game Tree Pruning 



### Alpha-Beta Pruning

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_alpha_beta_pruning.png)

 - General configuration (MIN version)
    - We’re computing the MIN-VALUE at some node n
    - We’re looping over n’s children
    - n’s estimate of the childrens’ min is dropping
    - Who cares about n’s value?  MAX
    - Let α be the best value that MAX can get at any choice point along the current path from the root
    - If n becomes worse than α, MAX will avoid it, so we can stop considering n’s other children (it’s already bad enough that it won’t be played)
 - MAX version is symmetric

### Pruning Exampe


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimax_example.png)

 - 第2层
    - 最左节点, min-value 计算的 3
    - 中间节点
        - 1st successor is 2 , than means the min value of parent is ≤ 2. 
        - so the value of rest successor is not important now, because they will not influence the choice of max-value ,calculated by the first level node
        - computation break

### Alpha-Beta Implementation

 - α: MAX’s best option on path to root
 - β: MIN’s best option on path to root

```python
def max-value(state, α, β):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor, α, β))
        # top min-value not care what remains, if v ≥ β
        if v ≥ β return v
        # update global max value
        α = max(α, v)
    return v
```

```python
def min-value(state , α, β):
    initialize v = +∞
    for each successor of state:
        v = min(v, value(successor, α, β))
        # top max-value not care what remains, if v ≤ α
        if v ≤ α return v
        # update global min value
        β = min(β, v)
    return v
```

### Alpha-Beta Pruning Properties

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_alpha-beta-properties.png)

 - This pruning has ***no effect*** on minimax value computed for the root!

 - Values of intermediate nodes might be wrong
    - Important: children of the root may have the wrong value
    - So the most naive version won’t let you do action selection

 - Good child ordering improves effectiveness of pruning

 - With “perfect ordering”:
    - Time complexity drops to O(b<sup>m/2</sup>)
    - Doubles solvable depth!
    - Full search of, e.g. chess, is still hopeless…


***You must apply it after doing some actions***.

---

## Iterative Deepening

 - Iterative deepening uses DFS as a subroutine:
    1. Do a DFS which only searches for paths of length 1 or less.  i
        - (DFS gives up on any path of length 2)
    2. If “1” failed, do a DFS which only searches paths of length 2 or less.
    3. If “2” failed, do a DFS which only searches paths of length 3 or less.
        - ... and so on.











