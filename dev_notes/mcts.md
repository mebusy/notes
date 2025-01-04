[](...menustart)

- [Monte Carlo Tree Search](#d0a68bbde4a8ba76f8761cef0126247c)
    - [Four Phases](#18eb8ba1439923476980fa86411d6303)
    - [Tree Traversal & Node Expansion](#6272bdabc982f3f99130aecdc6565188)
    - [Rollout](#56ee398637559b61c89c9924f3f19733)
    - [Worked Example](#ccd190b6e6e99df9972443aab2ea15ac)

[](...menuend)


<h2 id="d0a68bbde4a8ba76f8761cef0126247c"></h2>

# Monte Carlo Tree Search

<h2 id="18eb8ba1439923476980fa86411d6303"></h2>

## Four Phases

1. Tree Traversal
    - using UCB1 formula
2. Node Expansion
    - add extra nodes to the tree
3. Rollout (Random Simulation)
    - random simulation of the game or the problem, in order to find a value
4. Backpropagation
    - take the value found in the rollout and backpropagate it up to the root node



<h2 id="6272bdabc982f3f99130aecdc6565188"></h2>

## Tree Traversal & Node Expansion

- <img src="../imgs/mcts_1_s.png" width=360 />
- you start at initial state s0
- you keep traversing the tree,  choosing the best child node based on the UCB1, until you reach a leaf node
- once you reach a leaf node, 
    - if it's never been sampled before, you don't expand it, you just do a rollout from there.
    - if it's have been sampled before, you expand it by adding all of its children to the tree, and then you choose one of them to rollout from.


<h2 id="56ee398637559b61c89c9924f3f19733"></h2>

## Rollout

- <img src="../imgs/mcts_2_s.png" width=420 />
- random choose an available action, and keep doing that until reach terminal state


<h2 id="ccd190b6e6e99df9972443aab2ea15ac"></h2>

## Worked Example

start at state s0, the first thing need to add the available actions

- <img src="../imgs/mcts_ex_1_s.png" width=300 />
    - N: visit count of parent node
- <img src="../imgs/mcts_ex_2_s.png" width=300 />

1st iteration, same ucb value, choose s1, s1 has not been visited yet, rollout it, get a terminal state (v:20), backpropagate it to s1.

- <img src="../imgs/mcts_ex_3_s.png" width=300 />

2nd iteration, ucb(s2) is infinite, choose  s2, rollout & backpropagate

- <img src="../imgs/mcts_ex_4_s.png" width=300 />

3rd iteration, ucb(s1) is maximum,  so choose s1, it is leaf node and already been visited before, so expand it, add s3, s4, choose s3, rollout & backpropagate

- <img src="../imgs/mcts_ex_5_s.png" width=300 />

4th iteration, ucb(s1) = 11.48, ucb(s2) = 12.10, choose s2, add s5, s6, rollout & backpropagate

- <img src="../imgs/mcts_ex_6_s.png" width=300 />


If we were asked to stop at this point. The search would essentially tell us that the best action to take is to go from s0 to s2. Because the average value of s2 is 24/2 = 12, and the average value of s1 is 20/2 = 10.

