...menustart

 - [Adversarial Search](#6778eced7db02d1b66c03c39306bc708)
	 - [Types of Games](#82c396e55e8a69361a547039258d0479)
	 - [Deterministic Games](#cc82ac9a2727eb1d5950b8affab7d93b)
	 - [Zero-Sum Games](#d821b153288450f3f70a8b5429bd79e7)
	 - [Adversarial Search](#6778eced7db02d1b66c03c39306bc708)
	 - [Single-Agent Trees](#06c1352495eca3c370be92255d91cc6e)
	 - [Adversarial Game Trees](#d21873e6049038af1b9127a1c8220791)
	 - [Minimax Values](#a4d1f6cf51517d66b29531f7e039ffb0)
	 - [Tic-Tac-Toe Game Tree](#0a6312d7d59a7975900e968c851dadd1)
	 - [Adversarial Search (Minimax)](#dcf0514b6a79cf87fcd3bd43487c2421)
	 - [Minimax Implementation](#a58343ec090ddd8a61a686ba6cb80359)
	 - [Minimax Efficiency](#86563aad0e1c5702c26fc95c039b8f5d)
	 - [Minimax Properties](#41f6acef7d955252a54191e4a588c49d)
	 - [Resource Limits](#febe674abc9aa524c322edbbd8ec668c)
	 - [Depth Matters](#1d6bb0121e05033d0b24687e099f1cd7)
	 - [Evaluation Functions](#374868e68849b0b659b2677c21e7e73d)
	 - [Why Pacman Starves](#60f84bbd0786516b9c113184771ff9ad)
	 - [Game Tree Pruning](#89d4e1dda46082b0db4e378df9ea47fa)
		 - [Alpha-Beta Pruning](#358c18c4263b1fc77ce96e4af26835e5)
		 - [Pruning Exampe](#c19957d4c3956796b41234017dc153e6)
		 - [Alpha-Beta Implementation](#e846bcc2e55ec4d7cfa03d4713218f5b)
		 - [Alpha-Beta Pruning Properties](#ec4a6665d642ea66a394cbde7e464a8d)
	 - [Iterative Deepening](#fcbd892c255445e0e3c99ceeb0dbc2e9)
 - [Expectimax and Utilities](#a45c912b3f29a85dfaf265df7e679a37)
	 - [Expectimax Search](#6ecc2099b9f0d08ca4a5fe81a800cacb)
	 - [Depth-Limited Expectimax](#ab3291e21188d4069affc1afa9072371)
	 - [What Probabilities to Use ?](#09e97ac67711291782476420d32639a6)
		 - [Quiz: Informed Probabilities](#28f9be702977991f6e9af6eac821e5bf)
	 - [Modeling Assumptions](#96c41e6537362c1152d9cffd89d3ce2d)
	 - [Utilities](#ceba282b7418b7f199798b645e1cba56)
	 - [Preferences](#d0834fcec6337785ee749c8f5464f6f6)
	 - [Rationality](#63000348f12e5505f8ea8b0b2b208698)
	 - [Utility Scales](#21657c7363e3c0a908c10915dce59712)
	 - [Example: Human Rationality](#9fb9837709420f7dfb61a9c21dd50531)

...menuend



<h2 id="6778eced7db02d1b66c03c39306bc708"></h2>
# Adversarial Search

<h2 id="82c396e55e8a69361a547039258d0479"></h2>
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


<h2 id="cc82ac9a2727eb1d5950b8affab7d93b"></h2>
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


<h2 id="d821b153288450f3f70a8b5429bd79e7"></h2>
## Zero-Sum Games

 Zero-Sum Games | General Games
 --- | --- 
 Agents have opposite utilities (values on outcomes) | Agents have independent utilities (values on outcomes)
 Lets us think of a single value that one maximizes and the other minimizes | Cooperation, indifference, competition, and more are all possible
 Adversarial, pure competition | More later on non-zero-sum games



<h2 id="6778eced7db02d1b66c03c39306bc708"></h2>
## Adversarial Search

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_adversarial_search_illustration.png)

we're going to have an agent is trying to figure out what to do. Just like a regular single-agent search. 

Before the way you're going to decide what to do is we're going to think about consquences of our actions. 

The differences rather than thinking about sequence of actions that I can perform , I need think about my opponent. 

So I imagine taking an action and then I imagine my opponent will then be in the situation of thinking about the "opponent" should do.  And they're going to imagine that they're taking an action which I will respond. It will get this enbedded interleaving of our future states. 


---

<h2 id="06c1352495eca3c370be92255d91cc6e"></h2>
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

<h2 id="d21873e6049038af1b9127a1c8220791"></h2>
## Adversarial Game Trees

Let's think about the case where we have an adversary . 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_game_trees.png)

In the state of root , we can still do the same thought : move left or move right. 

The difference now is in each of these possible futures the ghost can move left or right. So there's still the tree of of possible futures. 

So we need to think about now what a value is in the case of an adversary. This is going to give us the idea of a ***minimax*** value. 


<h2 id="a4d1f6cf51517d66b29531f7e039ffb0"></h2>
## Minimax Values

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimaxValues.png)

8 is still gonna be the best outcome we can achieve under perfect play against an optimal adversary. 

We still know the value of Terminal States. For a state that is under my opponents control I imagine that this ghost is out there to minimize my value , so it will be -10.

---


<h2 id="0a6312d7d59a7975900e968c851dadd1"></h2>
##  Tic-Tac-Toe Game Tree

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_ticTac_game_tree.png)

Blue one moves first. 

The value of root will be one of { -1,1,0 }.


<h2 id="dcf0514b6a79cf87fcd3bd43487c2421"></h2>
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

<h2 id="a58343ec090ddd8a61a686ba6cb80359"></h2>
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



<h2 id="86563aad0e1c5702c26fc95c039b8f5d"></h2>
## Minimax Efficiency

 - How efficient is minimax?
    - Just like (exhaustive) DFS
    - Time: O(bᵐ)
    - Space: O(bm)
 - Pacma mple: For chess, b ≈35, m ≈100
    - Exact solution is completely infeasible
    - But, do we need to explore the whole tree?


<h2 id="41f6acef7d955252a54191e4a588c49d"></h2>
## Minimax Properties

game sample:

you get points when you win , you get points when you get a dot , you lost a point every step. 

If you play against a perfect player  you want to use minimax but if you are not playing against a player move random  then minimax is going to be overly pessimistic. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_minimax_properties.png)


<h2 id="febe674abc9aa524c322edbbd8ec668c"></h2>
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


<h2 id="1d6bb0121e05033d0b24687e099f1cd7"></h2>
## Depth Matters

 - Evaluation functions are always imperfect
 - The deeper in the tree the evaluation function is buried, the less the quality of the evaluation function matters
 - An important example of the tradeoff between complexity of features and complexity of computation


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_advS_depth_matters.png)


----

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_resource_limitation_pacman_example2.png)

For this example , if we look forward just a couple steps , we're going to need know it won't be able to see actually eating of the dot or any future collisions with the ghost.  We can not see whether or not we can be closer or farther from the dot. But we have to have an evaluation function that says that. 

If we can see all the way into the future , we can see the whole game play out on this board. The critical thing is that the blue ghost is going to go somewhere and once it goes somewhere it's committed. So what we should do now is moving towards the orange ghost because we are still not in any danger.  If you look deeply enough into the tree you see that what this allows you to do is force the blue ghost to make a decision before you have to.


<h2 id="374868e68849b0b659b2677c21e7e73d"></h2>
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

<h2 id="60f84bbd0786516b9c113184771ff9ad"></h2>
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


<h2 id="89d4e1dda46082b0db4e378df9ea47fa"></h2>
## Game Tree Pruning 



<h2 id="358c18c4263b1fc77ce96e4af26835e5"></h2>
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

<h2 id="c19957d4c3956796b41234017dc153e6"></h2>
### Pruning Exampe


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_advS_minimax_example.png)

 - 第2层
    - 最左节点, min-value 计算的 3
    - 中间节点
        - 1st successor is 2 , than means the min value of parent is ≤ 2. 
        - so the value of rest successor is not important now, because they will not influence the choice of max-value ,calculated by the first level node
        - computation break

<h2 id="e846bcc2e55ec4d7cfa03d4713218f5b"></h2>
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

<h2 id="ec4a6665d642ea66a394cbde7e464a8d"></h2>
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

<h2 id="fcbd892c255445e0e3c99ceeb0dbc2e9"></h2>
## Iterative Deepening

 - Iterative deepening uses DFS as a subroutine:
    1. Do a DFS which only searches for paths of length 1 or less.  i
        - (DFS gives up on any path of length 2)
    2. If “1” failed, do a DFS which only searches paths of length 2 or less.
    3. If “2” failed, do a DFS which only searches paths of length 3 or less.
        - ... and so on.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_iterative_deepening.png)


---

<h2 id="a45c912b3f29a85dfaf265df7e679a37"></h2>
# Expectimax and Utilities

Idea for day is going to think about the case where all uncertainty is controlled by chance and not by an adversary.

<h2 id="6ecc2099b9f0d08ca4a5fe81a800cacb"></h2>
## Expectimax Search 

left node will be 10

for the right node ,  if 9 and 100 happens equally likely, the value will be  (100+9)/2 = 54.5. 

so we should probably take the right node. 

---

Expectimax can not apply pruning.

---

<h2 id="ab3291e21188d4069affc1afa9072371"></h2>
## Depth-Limited Expectimax

we have 2 layers corresponding to the 2 sequence of random ghost actions before pacman moves again. 

<h2 id="09e97ac67711291782476420d32639a6"></h2>
## What Probabilities to Use ?

One important thing to remember is that just because we assign probabilities that reflect our believes to the outcome , does not mean that the thing on the other side of flipping a coin. 

If I think there is a 20% chance that the ghost go to left , it doesn't mean that the ghost has a random number generator. It just means that given my model which may be a simplification that's the best i can say given my evidence. 

<h2 id="28f9be702977991f6e9af6eac821e5bf"></h2>
### Quiz: Informed Probabilities

In general expectimax is the more general search procedures. You should always in principle use expectimax.


<h2 id="96c41e6537362c1152d9cffd89d3ce2d"></h2>
## Modeling Assumptions

<h2 id="ceba282b7418b7f199798b645e1cba56"></h2>
## Utilities


https://www.authorea.com/users/5754/articles/6087/_show_article


why do we want the goal is to be the input and the optimal behavior to be the output of the computation. why don't you just let the agent picks their own utilities? 

vacuum cleaner  example: the agent would like to do nothing ,and so easy to do nothing. 

why not prescribe ?  it's very hard to write down , complicated and context-defpendent.

idea: utilities go in , behavior comes out.

<h2 id="d0834fcec6337785ee749c8f5464f6f6"></h2>
## Preferences

Agent has to have preferences among various things. 

for example 0,1,2 ice cream scoops ,it has to have preferences among them called prizes, specific outcomes.  A and B might   be various numbers of scoops. we have to have preference among the prizes. but we also have to be able to order our preferences among the lotteries , which are situations where you're not sure which prize are going to get and not shown here. 

prizes are atomic outcomes and your lotteries which are mixtures with a certain probability. 

so there lotteries and prizes  we must have preference, means an agent has to prefer one of the other.  and the question is just other utilities that reflect those preferences. we say lotteries here we do not mean the actual act of gambling in the lotteries. someone plays gambling just because we like to play. 


<h2 id="63000348f12e5505f8ea8b0b2b208698"></h2>
## Rationality



We want utilities, we know we have to have preferences. Are they kind of good preferences? and bad preferences? are there always utility functions ?

Rational Preferences

preferences with start point 
we are going to try to figure out under what circumstance those preferences can be boiled down to utility function. 

so we'd like to constraints on these preferences before we call them rational . 

There is a wide variety of preferences that are ok : maybe the agent wants to make money, maybe the agent want to spend money , maybe agent like ice cream , maybe agent hate ice cream , these are all prefectly good preferences. 

But there are certain kinds of preferences just make no sense and so we need to constraints.  Here's one constraint the axiom of transitivity 传递性公理.This says if you prefer A to B and you prefer B to C , you better prefer A to C. 

Suppose that the agent has the nontransitive preferences A≻B≻C≻A, where A, B, and C are goods that can be freely exchanged. If the agent currently has A, then we could offer to trade C for A plus one cent. The agent prefers C, and so would be willing to make this trade. We could then offer to trade B for C, extracting another cent, and finally trade A for B. This brings us back where we started from, except that the agent has given us three cents. We can keep going around the cycle until the agent has no money at all. Clearly, the agent has acted irrationally in this case.





=== from book

Intuitively, the principle of Maximum Expected Utility (141EU) seems like a reasonable way to make decisions, but it is by no means obvious that it is the only rational way.

After all, why should maximizing the average utility be so special? What's wrong with an agent that maximizes the weighted sum of the cubes of the possible utilities, or tries to minimize the worst possible loss?  Could an agent act rationally just by expressing preferences between states, without giving them numeric values? Finally, why should a utility function with the required properties exist at all? 

These questions can be answered by writing down some constraints on the preferences that a rational agent should have and then showing that the MEU principle can be derived from the constraints. We use the following notation to describe an agent's preferences:

We use the following notation to describe an agent's preferences:

 NOTATION | preference 
 --- | --- 
  A ≻ B  | the agent prefers A over B
  A ~ B | the agent is indifferent between A and B
  A ≻= B | the agent prefers A over B , or is indifferent between them

现在显而易见的问题是，什么样的东西是A和B? 
他们可能是世界的状态，但往往不确定的是什么是真正提供的。 例如，提供意大利面菜或鸡的航空公司乘客不知道在锡箔盖下方潜藏着什么。

The pasta could be delicious or congealed, the chicken juicy or overcooked beyond recognition. 
We can think of the set of outcomes for each action as a ***lottery*** -- think of each action as a ticket. A lottery ***L*** with possible outcomes S₁,...,S<sub>n</sub> , that occur with probabilities p₁,...,p<sub>n</sub> is writte

```
L = [p₁,S₁; p₂,S₂; ... ; pn,Sn]
```

In general, each outcome Sᵢ of a lottery can be either an atomic state or another lottery. 
The primary issue for utility theory is to understand how preferences between complex lotteries are related to preferences between the underlying states in those lotteries. 
To address this issue we list six constraints that we require any reasonable preference relation to obey:

=== end from book


 - Orderability
    - (A≻B)∨(B≻A)∨(A~B)
    - given any 2 lotteries , a rational agent must either prefer one to ther other , or else rate the two as equally preferable.
    - that is , the agent cannot avoid deciding.
 - Transitivity 
    - (A≻B)∧(B≻C)⇒ (A≻C)
    - given any 3 lotteries , if an agent prefers A to B and prefers B to C , then the agent must prefer A to C
 - Continuity
    - A≻B≻C ⇒ ∃p[p,A; 1-p,C] ~ B
    - if some lottery B is between A and C in preference , then there is some probability *p* for which the rational agent will be indifferent between getting B for sure and the lottery that yields A with probability *p* and C with probability *1-p* .
 - Substitutability
    - A~B ⇒ [p,A; 1-p,C] ~ [p,B; 1-p,C]
    - if an agent is indifferent between two lotteries A and B , then the agent is indifferent betwwen two more complex lotteries that are the same except that B is substituted for A in one of them. This holds regardless of the probabilities and the other outcome(s) in the lotteries.
 - Monotonicity 单调性
    - A≻B ⇒ (p≥q ⇔ [p,A; 1-p,B] ≻= [q,A; 1-q,B]) 
    - suppose 2 lotteries have the same two possible outcomes, A and B. If an agent prefers A to B , then the agent must prefer the lottery that has a higher probability for A (and vice versa)
    - you prefer more A in the mix

These constraints are known as the axioms of utility theory. 
 
Each axiom can be motivated by showing that an agent that violates it will exhibit patently irrational behavior in some situations. 在某些情况下违反这些公理的agent会表现出不合理的行为。 For example, we can motivate transitivity by making an agent with nontransitive preferences give us all its money. 比如上面的 robot例子。

---

Basically if you accept these axioms there is an axiom says all of your preferences can be described with the utiity function. 
So if you obey these axioms we give you the stamp of rationality. and that means the preferences violate these are irrational preferences and meet this irrational. 


**Preferences lead to utility**

Notice that the axioms of utility theory are really axioms about preferences--they say nothing about a utility function. 
But in fact from the axioms of utility we can derive the following consequences :

 - Existence of Utility Function
    - U(A)>U(B) ⇔ A≻B
    - U(A)=U(B) ⇔ A=B
    - U(A)≥U(B) ⇔ A≻=B
    - If an agent's preferences obey the axioms of utility, then there exists a function U such that U(A) > U(B) if and only if A is preferred to B, and U(A) = U(B) if and only if the agent is indifferent between A and B.
 - Expected Utility of a Lottery:
    - `U[p₁,S₁; p₂,S₂; ... ; pn,Sn] = ΣpᵢU(Sᵢ)`.
    - The utility of a lottery is the sum of the probability of each outcome times the utility of that outcome.

In other words, once the probabilities and utilities of the possible outcome states are specified. the utility of a compound lottery involving those states is completely determined. 

<h2 id="21657c7363e3c0a908c10915dce59712"></h2>
## Utility Scales

QALY, or quality-adjusted life year. Patients with a disability are willing to accept a shorter life expectancy to be restored to full health. For example. kidney patients on average are indifferent between living two years on a dialysis machine and one year at full health.


<h2 id="9fb9837709420f7dfb61a9c21dd50531"></h2>
## Example: Human Rationality

Decision theory is a ***normative theory***: it describes how a rational agent should act.A descriptive theory, on the other hand, describes how actual agents -- for example, humans really do act. 

The application of economic theory would be greatly enhanced if the two coincided, but there appears to be same experimental evidence io the contrary.
The evideine suggests that humans are "predictably irrational".

The best-known problem is the Allais paradox (Allais, 1953). People are given a choice between lotteries A and B and thcn between C and D, which have the following prizes:

```
A : 80% chance of $4000     C : 20% chance of $4000 
B : 100% chance of $3000    D : 25% chance of $3000
```

Most people consistently prefer B over A (taking the sure thing), and C over D (taking the higher EMV).  The normative analysis disagrees? 

In that case, then B ≻ A implies that U($3000) > 0.8 U($4000), whereas C ≻ D implies exactly the reverse. In other words, there is no utility function that is consistent with these choices.

One explanation for the apparently irrational preferences is the **certainty effect** : people are strongly attracted to gains that are certain. There are several reasons why this may be so.

First, people may prefer to reduce their computational burden; by choosing certain outcomes, they don't have to compute with probabilities. But the effect persists even when the computations involved are very easy ones. Second, people may distrust the legitimacy of the stated probabilities. 
Third, people may be accounting for their emotional state as well as their financial state. People know they would experience regret if they gave up a certain reward (B) for an 80% chance at a higher reward and then lost. In other words, if A is chosen, there is a 20% chance of getting no money and feeling like a complete idiot, which is worse than just getting no money. 

So perhaps people who choose B over A and C over D are not being irrational; they are just saying that they are willing to give up $200 of F.MV to avoid a 20% chance of feeling like an idiot.








