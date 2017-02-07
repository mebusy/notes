

MDP : the way of formalizing the idea of non-deterministic search which is search when your actions outcomes are uncertain.

why would we be unsure what the outcomes of our actions is going to be ?  Well, maybe we've got a robot on a ledge and we take the action across the ledge, what's gonna happen ? Maybe we'll cross the ledge ,maybe we will fall into the fire pit. We're not sure we can commit to the action. But of course the outcome is entirely under our control. 

maybe you're a can opener robot and you take the can and you open it , and what's underneath ? More can! 



## Example : Grid World 

Noisy movement: for example : North action

Reward : 2 kinds of rewards.  one are the terminal utilities, shown as the plus 1 and minus 1(also the exit to game end). Another kind of reward which is every step take comes along with a little tiny reward , and this is sometimes called a living reward or a living penalty based on whether it's positive or negative. 

Goal: in general the agent is going to involve getting to a big reward and taking it. 

## Grid World Actions

you're not sure what the results gonna be. 

if you take north , you may move left, and it's bad.  So when you plan you're gonna have to take these outcomes into account. 


## Markov Decision Processes

MDP is a lot like a search problem. 

unlike : successor function . unlike in search , we're going to take the successor function and break it into a few pieces. We're going to have an idea of actions which are the actions you take like north ,south, east, west. We're then gonna have a transition function . 

T(s,a,s')  :  in some state s , you take some action a , s' is a possible result. The function T(s,a,s')  tells you how likely that result is and in that sense it's a conditional probability. 

The transition function is basically the successor function. The differences is now there are lots of differents s's that can happen and they all have various probabilities t associated with them. 

Reward function (unlike)  R(s,a,s')  means you get a reward that depends on the state you are in , the action you took, and the outcome. You might not know your actual reward until you see whether or not you fell into the pit.  In some formulations R will only depend on s and s'. What is this ?  This is basically the cost function from search. In seach the cost would be small and in the case of MDPs in general we want the rewards to be big. 

Terminal state :   another import difference between MDPs and search problems is  MDP's very ofren go on forever .

MDP is basically taking search that we know and love , and adding the necessary machinery to support the idea that actions can have multiple outcomes. 

## What is Markov about MDPs ?

MDP means the probability distribution over your outcomes depends only on the current state and action , not on the whole histroy of how you got there.

So this is important property in MDP is to make sure that you define your transition function and your state in such a way that the transition probabilities depend only on the current state and action. 

## Policies

1 not work for MDPs. because we don't know what actions are gonna to do.  The relevant idea is not a plan now but a policy. Policy is a mapping from states to actions and tells  in each state what action to take. 

Expectimax didn't really compute an explicit policy in this sense. What expectimax did for these kinds of problems is from a given state it did a forward-thinking computation that produced one entry of the policy which you then took and wherever you land and you run expectimax again. 

So on one hand expectimax is a way of solving these problems and on the other hand it doesn't compute an explicit policy. That chould be a good thing or bad thing. It can be bad because you might redo a lot of work if you keep in the same state. It could be good because there are so many states you coundn't write down an explicit policy anyway. 

## Optimal Policies

The funny thing is the square left to "-1" squre. It's going into the wall. Why is it going into the wall?  This is an example of we feed the rules of the game in , we compute the optimal behavior , sometimes the behavior is not what we expected but it's still optimal. In this example, if you did anything else you would risk the pit. The agaent is pressing its check against the wall and justing waiting waiting waiting until it gets out of this scary situation safely. So this agent is very very conservative because each time step cost very little. 

What happens if we make this living penalty more severe. 

## Example: Racing

### Racing Search Tree

Any MDP is defining a search tree. So if you're in some particular state , for example if you're in the state where the car is cool, you have 2 actions: slow or fast. 

It's very like an expectimax tree but we'll see very shortly why we might not want to use expectimax to solve it. You can already see hints of it : it's a big tree but it's kinds of same blue and red stuff over and over again. There's just not that many states. This is the case where expectimax will do a lot of work. 


## MDP Search Trees

Queue State: when I'm in a state and I take an action I end up in a queue state , which you can think of as kind of the pair of the state and the action where I've committed to the action but I haven't done it yet. 
 
That is kind of expectimax tree except ...
 
 1. the probabilities are given to you by the transition function and 
 2. the rewards instead of being at the bottom are smeared throughout the tree, they come to you step-by-step.

## Utilities of Sequences

In a MDP the rewards come to you step-by-step , we need to figure out what our unility function acutally is. In the simplest case you just add up the rewards but it can be little more subtle than that.

For example shown here 


you might care whether or not you get these 4 gems step-by-step or all at the end in one big prize. This raises a general question for MDPs: what preferences or utilities should an agent have for rewards sequences. 

## Discounting 

## Stationary Preferences

What we want from an agent that looks at sequences of rewards in order to consider it kind of reasonable. 

stick the same reward in front of both 

if I liked A better than B now I should like it better shifted into the future as well and vice versa. 

## Infinite Utilities ?!

Here are multiple possible solutions, in general we'er gonna have discounts that usually saves us. 

## Recap: Defining MDPs

## Solving MDPs

### Optimal Quantities 

what the star means is  this is the value under optimal action.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_mdp_Optimal_Quantities_example.png)

Look at the left-bottom square with 0.49. The arrow is the policy.  What's that 0.49?  That is if you started in this state and you ran this game over and over again and sometimes you slipped, and sometimes you didn't , and you added up all of those utilities on average you would get 0.49, and you will achieve it by trying to go north whenever you're in the state. 

You can see it's better to be at 0.85 square by the exit that it is to be over here 0.49 square. Why ? Because if you're over here you have to pay that living reward and some discount to even get to the exit. The best thing is to actually be in the exit. 

Similarly you can see if you're essentially 2 steps from the exit, it's better to be at 0.74 square than at 0.57 next to the pit , because when something goes wrong , .74  is not a big deal, while .57 you fall into the pit and lose.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_mdp_Optimal_Quantities_example_qstate.png)

This shows the Q values. From each state , except for the exit state , you got 4 choices of actions . If you are in the 0.57 state next to the pit, and the action you've committed to is north , then you get that same .57. 

## Values of States 

So we want to be able to compute these values. We'd like to be able to take an MDP and compute these expectimax values for a state and actully we usually do with these algorithms we compute the values for all of the states. We'll see that there are ways to save time by doing all the states at once provided your MDP is small enough that you can actually go through all the states. 

### Racing Search Tree

## Time-Limited Values

What's a time step ? It's a reward. 

when you achieve the exit, you must take extra "exit" action to end game and get the reward.

iteration 2:  from the squre between wall and pit, I have time to do very stupid things -- going to the pit and receive a negative -- but that's not the optimal.  The optimal thing is kind of anything else. So I have zero. But if it allowed 3 steps I can get some rewards even from there. 



iteration 6: from left-bottom square , I am now possible to  get to a positive reward.
iteration 7: from left-bottom square , I can not only get there in the lucky way where nothing goes wrong I can also get there in various ways where something goes wrong once. 

iteration 100: most of the states are pretty good. 










 
