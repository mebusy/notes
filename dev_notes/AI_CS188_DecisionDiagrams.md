
# Decision Diagrams / Value of Perfect Information

## Decision Networks

DNs will be a lot like BNs, but there will be more types of nodes rather than just random variable nodes. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_dn_example0.png)

 - New node types:
    - ![][1] Chance nodes (just like BNs)
        - we have random variable for weather ,which could be sunny or rainy 
        - with a random variable for forecase , tends to be a noisy version of actual weather
        - 这部分其实就是 BNs
    - ![][2] Actions (rectangles, cannot have parents, act as observed evidence)
        - you have a choice here 
        - you can either take your umbrella with you , or you can leave it at home 
        - so this is something you get to set
    - ![][3] Utility node (diamond, depends on action and chance nodes)
        - dislike the utility we met before, this node is not a number ,but a function , a table 
        - it tells you for every possible combination of its parent values , what is the utility for experiencing that combination of parent values. 
        - over there, there are 2 parents: umbrella and weather.   It could be that 
            - it's sunny , you left your umbrella at home , now you get to play with the beach ball , probably have high utility
            - it's sunny , but you brought you umbrella , and now you don't get to play the beach ball , we get to carry umbrella around ,you are not so happy
            - it's rainy , you didn't bring an umbrella, that's the worst case
            - it's rainy , but you brought your umbrella, at least you have a way to protect yourself from the rain. 
        - all 4 of these will have a number associated with them , the utility for that particular outcome .
        - if there is only 1 agent , where will only be one utility node, if there's more than 1 agent there could be more than 1 utility node.

What are we going to be doing ?  We are still going to be maximizing expected utility. 

 - MEU: choose the action which maximizes the expected utility given the evidence
 - Can directly operationalize this with decision networks
    - Bayes nets with nodes for utility and actions
    - Lets us calculate the expected utility for each action
 - What will we do with a network like above ?
    - We'll look at every possible action we might take, compute the expected utility  if we were to take that action and then pick the action that maximizes the expected utility. 

---

So how do you select an action ?

 - Action selection
    - Instantiate all evidence
    - Set action node(s) each possible way
        - loop over all possible choices for the actions 
    - Calculate posterior for all parents of utility node, given the evidence
        - this case you would compute the conditional distribution of Weather, given the evidence. 
        - if weather itself is evidence it's very easy ,  if there's no evidence then it's just a prior for Weather
        - if there is some forecase you will essentially apply Bayes rule to find out P(weather | forecase)
    - Calculate expected utility for each action
    - Choose maximizing action



### Simple Example 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_dn_example_simple.png)

There are part of the problem specificaton of course.   If you are designing a robot to be deployed somewhere ,you would decide for that robot what the utilities are such that when the robot maximizes expected utility it does what you want it to try to achieve. 

 - we need to loop over all possible actions , the Umbrella 
    - Umbrella = leave
        - what is the expected utility ?  Sum over all possible outcomes for Weather 
        - EU(leave) = ∑<sub>w</sub> P(w)U(leave, w) = 0.7*100 + 0.3*0 = 70
    - Umbrella = take 
        - EU(take) = ∑<sub>w</sub> P(w)U(take, w) = 0.7* 20 + 0.3*70 = 35
 - Optimal decision = leave
    - MEU(∅) = maxₐ EU(a) = 70
        - ∅ means no evidence.   

This is a lot like expectimax tree. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DN_example_expectimax_tree.png)

 - Almost exactly like expectimax / MDPs
 - What’s changed?

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_dn_example_simple2.png)

We listened to the forecast and the forecast is bad.  

 - So in this kind of computations we compute the conditional distribution of the parents given evidence.
    - P(W|F=bad)
 - loop
    - Umbrella = leave  
        - EU(leave|bad) = ∑<sub>w</sub> P(w|bad)U(leave, w) = 0.34*100 + 0.66*0 = 34
    - Umbrella = take 
        - EU(take|bad) = ∑<sub>w</sub> P(w|bad)U(take, w) = 0.34*20 + 0.66*70 = 53
 - Optimal decision = take
    - MEU(F=bad) = maxₐ EU(a|bad) = 70  
          
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DN_example_expectimax_tree2.png)


### Ghostbusters Decision Network







## Decision Networks Cont.











---

 [1]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_chance_node.png)
 [2]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_action_node.png)
 [3]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_utility_node.png)

