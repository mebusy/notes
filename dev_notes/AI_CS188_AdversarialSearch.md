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
    - recursive call

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_func_max_value.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_func_min_value.png)


## Minimax Example

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimax_example.png)



Pacman game sample:

you get points when you win , you get points when you get a dot , you lost a point every step. 

If you play against a perfect player  you want to use minimax but if you are not playing against a player move random  then minimax is going to be overly pessimistic. 



Resource Limits

For a chess game, we can't possibly search the whole game tree. Essentially we've got resource limits in this case time. That tell us we can only look forward so far into the tree before the exponential growth of the tree gets this.

So we can only search just some limited depth from the tree. Now the problem is we get to the end of our search we don't have terminal utilities because we are not actually at the end of the game. 

So we need to replace the terminal utilities in the minimax algorithm with what's called evaluation function, which takes a non-terminal position and gives us some estimate of what the terminal utility under that tree would be under minimax plan.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_resource_limitation_pacman_example2.png)

For this example , if we look forward just a couple steps , we're going to need know it won't be able to see actually eating of the dot or any future collisions with the ghost.  We can not see whether or not we can be closer or farther from the dot. But we have to have an evaluation function that says that. 

If we can see all the way into the future , we can see the whole game play out on this board. The critical thing is that the blue ghost is going to go somewhere and once it goes somewhere it's committed. So what we should do now is moving towards the orange ghost because we are still not in any danger.  If you look deeply enough into the tree you see that what this allows you to do is force the blue ghost to make a decision before you have to.


Evaluation Functions

a function takes a non-terminal state and return some number. Just like the heuristic value in Astar search , in this case we want that number to return the actual minimax value of that position. That is not going to happen. In practice what peaple do is they try to come up with some function which on average is positive when the minimax value is positive , is negative when the minimax value is negative. 


pacman example : starve ( loop in a range  )

danger of replanning agents

the plan they have in their head does not really have to be consistent. Every step you do a new plan. 

10 points for a dot.

The problem is if we take the right branch , look at that state ( right,  2nd level ) , it's just like the state of the root . (1 is a bit left, another is a bit of right) 

so we trash.  

solution: closer to a dot  score point as well.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_adversarial_search_pacman_example2.png)

What's going on here each agent is separately doing their own searches. But they see that the other one constrols , they treat it like min node (???). So even though each agent is actually doing its own search because they are both assuming the other one shares its evaluation function that is also minimax agent. We're goint to see cooperation emerge.

This shows you how you can get cooperation without programming it in, simply they're both trying to achieve the same goal. 


Alpha-Beta Pruning properties

you must apply it after doing some actions.






