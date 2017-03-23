

# Hidden Markov Model 

This pacman can eat ghost but first he has to find them. So soon as pacman start moving , you will see in the bottom colord numbers , which are kind of noisy readings of how far the ghosts are. 

Now let's say I want to eat the orange ghost. If you could somehow take these numbers over time and combine them with your model of how the world works --  means where are the walls, where are the maze -- and also your model of how the ghosts move , and figure out where they are. 


## Markov Models

 - A **Markov Model** is a chain-structured Bayes' net (BN)
    - Each node is identically distributed (stationarity)
    - Value of X at a given time is called the **state**
    - As a Bayes' net
        - P(X₁)
        - P(X<sub>t</sub> | X<sub>t-1</sub>)
    - Parameters: called **transition probability** or dynamics, specify how the state evolves over time (also, initial state probabilities)
        - this is the model how the world changes
    - Same as MDP transition model , but no choice of action
        - here is no action, you just watching 


### Conditional Independence

 - Basic conditional independence:
    - Past and future independent of the present
        - the past anything before the current state and future anything beyond the current state are independent given the current state
    - Each time step only depends on the previous
    - This is called the (first order) Markov property
 - Note that the chain is just a (growable) BN
    - We can always use generic BN reasoning on it if we truncate the chain at a fixed length

---

## Hidden Markov Models

A Markov model can talk about how the world changes , but if I forecast into the future sooner or later I just don't know anything anymore. 

But hidden Markov model says 2 things: I know how the world changes in a time step which let me figure out roughly what's gonna happen in the absense of evidence and at every time step I also getting some kind of reading -- I got some evidence that helps me sharpen my belief about what's happening. So as the same time that time passes ,evidence also comes in. The robot moves and takes another sonar reading.

-- pic

---

 - Markov chains not so useful for most agents 
    - need observations to update your beliefs
 - Hidden Markov models (HMMs)
    - Underlying Markov chain over states *S*
    - You observe outpus (effects) at each time step
    - As a Bayes' net :
        - pic
        - structure:  1 hidden variable , and 1 observed variable 
        - what we're gonna have is that every time there's ganna be a hidden variable that structure like a markov chain and each time the evidence depends only on the state observed but only on the state at that time (E | X). 

---

### Example : Weather HMM 

 - the hidden variable: where or not it's raining -- True or False
 - the observed variable: 






