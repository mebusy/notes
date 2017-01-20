
# Adversarial Search


We will talk about zero sum and deterministic games. They are games of perfect information.

Think about how this is different from search. 

In search I gave you the search problem , and what you gave me back is a plan or path it is a sequences of actions that executed and it was guaranteed to succeed.

That's not going to work here because we don't control our opponent. So we can't just give a plan that guarantes to succeed. What we need to do is we need a function which tells us in any given state what to do . That is the policy in the game case it's often called strategy. 


Deterministic Games

Terminal Utilities:  this tell us for an end-state how much it is worth to each of the players.

the solution to a game like this is a policy which map states to actions.



Adversarial Search

we're going to have an agent is trying to figure out what to do. Just like a regular single-agent search before the way you're going to decide what to do is we're going to think about consquences of our actions. 

The differences rather than thinking about sequence of actions that I can perform , I need think about my opponent. 

So I imagine taking an action and then I imagine my opponent will then be in the situation of thinking about the "opponent" should do.  And they're going to imagine that they're taking an action which I will respond. It will get this enbedded interleaving of our future states. 


---

Single-Agent Trees

some of there paths go forever , some of these paths end because it meet the last of the game terminates. 

And what we actually do ? We image there is  associated values with this. Let's say this is the best possible outcome where I go straight to the dot ate it. And there are various other outcomes buried further in the other trees and I can associate numbers with them.

In the case of single-agent , I get to pick any outcome I like.  In this  actual search case , showed as the pic , we should make that value-8 outcome happen.


For terminal state the value is known. What about the other ones?  

well in this state I have a choice I can get 8 or I can get whatever is down below the left path. So I can write the value of the state is defined to be the maximum over the values of its children. 

In single-agent case, we choose maximum value.

---

Let's think about the case where we have an adversary . In the state of root , we can still do the same thought : move left or move right. The difference now is in each of these possible futures the ghost can move left or right. So there's still the tree of of possible futures. 

So we need to think about now what a value is in the case of an adversary. This is going to give us the idea of a ***minimax*** value. 


Minimax Values

It's still gonna be the best outcome we can achieve under perfect play against an optimal adversary. 

We still know the value of Terminal States. For a state that is under my opponents control I imagine that this ghost is out there to minimize my value , so it will be -10.

Tic-Tac-Toe Game Tree

Blue one moves first. 

The value of root will be one of { -1,1,0 }.


Pacman game sample:

you get points when you win , you get points when you get a dot , you lost a point every step. 

If you play against a perfect player  you want to use minimax but if you are not playing against a player move random  then minimax is going to be overly pessimistic. 



Resource Limits

For a chess game, we can't possibly search the whole game tree. Essentially we've got resource limits in this case time. That tell us we can only look forward so far into the tree before the exponential growth of the tree gets this.

So we can only search just some limited depth from the tree. Now the problem is we get to the end of our search we don't have terminal utilities because we are not actually at the end of the game. 

So we need to replace the terminal utilities in the minimax algorithm with what's called evaluation function, which takes a non-terminal position and gives us some estimate of what the terminal utility under that tree would be under minimax plan.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_resource_limitation_pacman_example2.png)

















