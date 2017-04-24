...menustart

 - [Decision Diagrams / Value of Perfect Information](#bcce11f51a8ba9f718e13496df69ff75)
	 - [Decision Networks](#4110b017c078c49b44248d46eddf6146)
		 - [Simple Example](#ecaa6de7751a679c6478caccd8dd7a12)
		 - [Ghostbusters Decision Network](#a457e316cc82b392c5e0160e69e95ab0)
	 - [Decision Networks Cont.](#a3ae179f8c3c60bae32aa8e7dc7f619a)

...menuend


<h2 id="bcce11f51a8ba9f718e13496df69ff75"></h2>

# Decision Diagrams / Value of Perfect Information

<h2 id="4110b017c078c49b44248d46eddf6146"></h2>

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



<h2 id="ecaa6de7751a679c6478caccd8dd7a12"></h2>

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
    - MEU(F=bad) = maxₐ EU(a|bad) = 53
          
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DN_example_expectimax_tree2.png)


<h2 id="a457e316cc82b392c5e0160e69e95ab0"></h2>

### Ghostbusters Decision Network

 - you receive -1 at every time step
 - you receive 250 if you buster the ghost
 - you receive 0 and game over if you buster and miss

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_GhostbustersDecisionNetwork.png)






## Value of Information

What we're interested in now is what is the value of information.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_valueOfInformation.png)

You have these sensors, how much would you be willing to pay to get an access to a sensor and measure its value. 

---

 - Idea: compute value of acquiring evidence
    - Can be done directly from decision network
 - Example: buying oil drilling rights
    - Two blocks A and B, exactly one has oil, worth k
    - You can drill in one location
    - Prior probabilities 0.5 each, & mutually exclusive
    - Drilling in either A or B has EU = k/2, MEU = k/2
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_valueOfInformation_example_drill_oil.png)
 - Question: what’s the **value of information** of O?
    - Value of knowing which of A or B has oil.
        - if you know the oil location (somebody tells you) , then your MEU is k. 
        - before, your MEU is k/2
        - the difference is k/2, so rationally you're willing to pay k/2 to get ot know where the oil is.
    - Value is expected gain in MEU from new info
    - Survey may say “oil in a” or “oil in b,” prob 0.5 each
    - If we know OilLoc, MEU is k (either way)
    - Gain in MEU from knowing OilLoc?
    - VPI(OilLoc) = k/2
        - value of **perfect** information
    - Fair price of information: k/2


### VPI Example: Weather

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_vpi_example_weather.png)

We can observe only Forecast. Question is how valuable is it to observe the forecast. 

 - MEU with no evidence
    - MEU(∅) = 70
 - MEU if forecast is bad
    - MEU(F=bad) = 53
 - MEU if forecast is good
    - MEU(F=good) = 95
 - Forecast distribution
    - P(F=good) = 0.59, P(F=bad) = 0.41
    - we can compute by running inference in BNs
    - 0.59·95 + 0.41·53 - 70 = 7.8 
    - in this case 7.8 means that you would be willing to pay 7.8 to get to listen to the forecast.
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_vpi_formular.png)
    - we have the VPI of a particular variable or set of variables E' given that you already observed another set of variables *e* which could be the empty set.
    - in our example *e* was the empty set , E' was equal to forecast. 
      

## Value of Information Cont.

 - Assume we have evidence E=e.  Value if we act now:
 - Assume we see that E’ = e’.  Value if we act then:
 - BUT **E’ is a random variable whose value is unknown**, so we don’t know what e’ will be

 - Expected value if E’ is revealed and then we act:
 - Value of information: how much MEU goes up by revealing E’ first then acting, over acting now:








---

 [1]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_chance_node.png)
 [2]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_action_node.png)
 [3]: ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_DM_utility_node.png)

