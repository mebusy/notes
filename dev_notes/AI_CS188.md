...menustart

 - [AI , CS 188](#aea7deb258843dff16f9b84b46ec1461)
 - [Introduction](#0b79795d3efc95b9976c7c5b933afce2)
	 - [What is AI](#9fa835a40078a81e452b0cbb4362a6f5)
	 - [Rational Decisions](#113b7e5d42d49b2f76a69a3517ebcde9)
	 - [Designing Rational Agents](#04052b6bc5dad6a9f6a00dfb9cd988da)
	 - [Course Topics](#e3a18b70b77602c474ec9b3140b582e3)
 - [Uninformed Search](#faccc055dce5dfee94eba9a23ec379bc)
	 - [Reflex Agents](#9ef57e59fc5834eb1f86775a80163590)
	 - [Planning Agents](#b35ab1adff6f2f91e25f048a1f1ecfcc)
	 - [Search Problems](#fc72ba154e470ee2e177ed8e75ee4de2)
	 - [Search Problems Are Models](#0a9e0b58d3ed416bdb73713846200baa)
		 - [Example: Traveling in Romania](#30f0fbd7fae0ee74806b20a52d15e3ee)
	 - [What’s in a State Space ?](#e753d55f3a61b93cba852a33216321e0)
	 - [State Space Sizes ?](#05eb0fb2a7cf700d9734545149fc43fb)
	 - [Quiz: Safe Passage](#10f2374e81dfff89cef5eecf517b70ef)
	 - [State Space Graphs and Search Trees](#12227407175834cc50274fb425cf4e2d)
		 - [State Space Graphs](#91fa96e85b0a665a30ab89661d0137c4)
		 - [Search Trees](#fa3d63f947f57a28158a9af70e100ef3)
		 - [State Space Graphs vs. Search Trees](#3371ddd82f34162d684dfd1d1f40d8b3)
		 - [Quiz: State Space Graphs vs. Search Trees](#76acaf4079e010db2a41f612ceae95f4)
	 - [Tree Search](#6281565533d78912ee355e95d1263fef)
		 - [Searching with a Search Tree](#643025d557c3b9f6d43cdd62b77f5530)
		 - [General Tree Search](#a23c40de844ed1e2415dc477845012af)
		 - [Depth-First Search](#d292eaede65eb34e66db0db9ebb6b9bc)
			 - [Search Algorithm Properties](#6dda6174af1ce92b505f3c29643504c3)
			 - [Depth-First Search (DFS) Properties](#62a9189e6707b0db89f80a7a5bb6c15e)
		 - [Breadth-First Search](#ae5c4b868b5b24149decba70c74165c2)

...menuend



<h2 id="aea7deb258843dff16f9b84b46ec1461"></h2>
# AI , CS 188

http://ai.berkeley.edu/lecture_slides.html

https://edge.edx.org/courses/BerkeleyX/CS188x-8/Artificial_Intelligence/info


<h2 id="0b79795d3efc95b9976c7c5b933afce2"></h2>
# Introduction

<h2 id="9fa835a40078a81e452b0cbb4362a6f5"></h2>
## What is AI

The science of making machines that: 

<h2 id="113b7e5d42d49b2f76a69a3517ebcde9"></h2>
## Rational Decisions

 - We’ll use the term **rational** in a very specific, technical way:
 	- Rational: maximally achieving pre-defined goals
 	- Rationality only concerns what decisions are made  (not the thought process behind them)
 - Goals are expressed in terms of the **utility** of outcomes
 - Being rational means **maximizing your expected utility**

A better title for this course would be:

 - **Computational Rationality**


<h2 id="04052b6bc5dad6a9f6a00dfb9cd988da"></h2>
## Designing Rational Agents

 - An **agent** is an entity that *perceives* and *acts*.
 - A **rational agent** selects actions that maximize its (expected) utility.  
 - Characteristics of the **percepts**, **environment**, and **action space** dictate techniques for selecting rational actions
 - **This course** is about:
 	- General AI techniques for a variety of problem types
 	- Learning to recognize when and how a new problem can be solved with an existing technique

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_agent.png)


<h2 id="e3a18b70b77602c474ec9b3140b582e3"></h2>
## Course Topics

 - Part I: Making Decisions
 	- Fast search / planning
 	- Constraint satisfaction
 	- Adversarial and uncertain search
 - Part II: Reasoning under Uncertainty
 	- Bayes’ nets
 	- Decision theory
 	- Machine learning
 - Throughout: Applications
 	- Natural language, vision, robotics, games, …



<h2 id="faccc055dce5dfee94eba9a23ec379bc"></h2>
# Uninformed Search

 - Agents that Plan Ahead
 - Search Problems
 - Uninformed Search Methods
 	- Depth-First Search
 	- Breadth-First Search
 	- Uniform-Cost Search

Uninformed means that when we are exploring search tree we have no idea if we're getting closer to the goal or not.  


<h2 id="9ef57e59fc5834eb1f86775a80163590"></h2>
## Reflex Agents

 - Reflex agents
 	- Choose action based on current percept (and maybe memory)
 	- May have memory or a model of the world’s current state
 	- Do not consider the future consequences of their actions
 	- **Consider how the world IS**
 - Can a reflex agent be rational?
 	- No
 - Example
 	- blinking your eye (not using your entire thinking capabilities)
 	- vacuum cleaner moving towards nearest dirt

<h2 id="b35ab1adff6f2f91e25f048a1f1ecfcc"></h2>
## Planning Agents
 
 - Planning agents
 	- Ask “what if”
 	- Decisions based on (hypothesized) consequences of actions
 	- Must have a model of how the world evolves in response to actions
 	- Must formulate a goal (test)
 	- **Consider how the world WOULD BE**
 - **Optimal vs. complete planning**
 - **Planning vs. replanning**


<h2 id="fc72ba154e470ee2e177ed8e75ee4de2"></h2>
## Search Problems

 - A **search problem** consists of:
 	- A state space
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_state_space.png)
 	- A successor function (with actions, costs)
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_successor_func.png)
 	- A start state and a goal test
 - A **solution** is a sequence of actions (a plan) which transforms the start state to a goal state


<h2 id="0a9e0b58d3ed416bdb73713846200baa"></h2>
## Search Problems Are Models

<h2 id="30f0fbd7fae0ee74806b20a52d15e3ee"></h2>
### Example: Traveling in Romania

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_travel_i_romania.png)

 - State space
 	- Cities
 - Successor Fuction:
 	- Roads: Go to adjacent city with cost = distance
 - Start State:
 	- Arad
 - Goal Test
 	- Is state == Bucharest ?
 - Solution ?


<h2 id="e753d55f3a61b93cba852a33216321e0"></h2>
## What’s in a State Space ?

 - The **world state** includes every last detail of the environment
	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_world_space.png) 
 - A **search state** keeps only the details needed for planning (abstraction)


Search State Problem | Pathing  | Eat-All-Dots
--- | --- | ---
States | (x,y) location |  {(x,y), dot booleans}
Actions | NSEW | NSEW
Successor | update location only | update location and possibly a dot boolean
Goal test | is (x,y) == END | dots all flase


<h2 id="05eb0fb2a7cf700d9734545149fc43fb"></h2>
## State Space Sizes ?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_state_space_size.png)

 - World state
 	- Agent Positions: 120  
 		- 10x12
 	- Food Count : 30
 	- Ghost positions: 12 
 		- 1x6
 	- Agent facing: NSEW

 - How many
 	- World states ?
 		- 120 x 2³⁰ x 12² x 4
 	- State for pathing ?
 		- 120
 	- State for eat-all-dots ?
 		- 120 x 2³⁰


<h2 id="10f2374e81dfff89cef5eecf517b70ef"></h2>
## Quiz: Safe Passage

 - Problem: eat all dots while keeping the ghosts permanent-scared
 - What does the state space have to specify?
 	- (agent position, dot booleans, power pellet booleans, remaining scared time)


<h2 id="12227407175834cc50274fb425cf4e2d"></h2>
## State Space Graphs and Search Trees

<h2 id="91fa96e85b0a665a30ab89661d0137c4"></h2>
### State Space Graphs

 - State space graph: A mathematical representation of a search problem
 	- Nodes are (abstracted) world configurations
 	- Arcs represent successors (action results)
 	- The goal test is a set of goal nodes (maybe only one)
 - In a state space graph, each state occurs only once!
 - We can rarely build this full graph in memory (it’s too big), but it’s a useful idea

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_state_space_graph.png)

 - In a search graph, also each state occurs only once!

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_search_graph.png)

<h2 id="fa3d63f947f57a28158a9af70e100ef3"></h2>
### Search Trees

 - A search tree:
 	- A “what if” tree of plans and their outcomes
 	- The start state is the root node
 	- Children correspond to successors
 	- Nodes show states, but correspond to PLANS that achieve those states
 	- **For most problems, we can never actually build the whole tree**

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_search_tree.png)


<h2 id="3371ddd82f34162d684dfd1d1f40d8b3"></h2>
### State Space Graphs vs. Search Trees

 - Each NODE in in the search tree is an entire PATH in the state space graph.
 	- 节点x in search tree , 表示了 以x 为 start node 的整个子图	
 - We construct both on demand – and we construct as little as possible.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_state_space_graph2.png)  .VS.  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_search_tree2.png)


<h2 id="76acaf4079e010db2a41f612ceae95f4"></h2>
### Quiz: State Space Graphs vs. Search Trees

Consider this 4-state graph: 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_4_state_graph.png)

How big is its search tree (from S)?

** ∞ !**

 - **Important: Lots of repeated structure in the search tree!**


---

<h2 id="6281565533d78912ee355e95d1263fef"></h2>
## Tree Search

<h2 id="643025d557c3b9f6d43cdd62b77f5530"></h2>
### Searching with a Search Tree

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_search_with_a_search_tree.png)

 - Search
 	- Expand out potential plans (tree nodes)
 	- Maintain a ***fringe*** of partial plans under consideration ( here, fringe is the nodes with white background and black font ) 
 	- Try to expand as few tree nodes as possible


<h2 id="a23c40de844ed1e2415dc477845012af"></h2>
### General Tree Search

```
function TREE-SEARCH(problem,strategy) returns a solution, or failure
	initialize the search tree using the initial state of problem
	loop do
		if there are no candidates for expansion then 
			return failure
		end

		choose a leaf node for expansion according to strategy

		if the node contain a goal state then
			return the corresponding solution
		else
			expand the node and add the resulting node to the search tree
		end
	end
end function
```

 - Important ideas:
 	- Fringe
 		- 添加到 待处理列表中的 nodes
 	- Expansion
 		- 从待处理列表中 选择一个 nodes 展开
 	- Exploration strategy
 - Main question: which fringe nodes to explore?


<h2 id="d292eaede65eb34e66db0db9ebb6b9bc"></h2>
### Depth-First Search

 - Strategy: 
 	- expand a deepest node first
 - Implementation: 
 	- Fringe is a LIFO stack

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_deep_first_search.png)

> leftmost DFS

<h2 id="6dda6174af1ce92b505f3c29643504c3"></h2>
#### Search Algorithm Properties

- **Cartoon of search tree**:
	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_cartoon_of_search_tree.png)
	- b is the branching factor
	- m is the maximum depth
	- solutions at various depths
- **Number of nodes** in entire tree?
	- 1 + b + b² + ... + bᵐ = O(bᵐ)
- **Complete**: Guaranteed to find a solution if one exists?
- **Optimal**: Guaranteed to find the least cost path?
- Time complexity?
- Space complexity?




<h2 id="62a9189e6707b0db89f80a7a5bb6c15e"></h2>
#### Depth-First Search (DFS) Properties

 - What nodes DFS expand?
 	- Some left prefix of the tree.
 	- **Could process the whole tree!**
 	- If m is finite, takes time **O(bᵐ)** 最坏的情况，遍历所有的节点
 - How much space does the fringe take?
 	- Only has siblings on path to root, so **O(b·m)**  
 	- 每一层展开一个节点, 每个节点有 b successors, 最大m 层
 - Is it complete?
  	- Yes. but under some assumptions that have a cycle check to avoid recursion
  	- m could be infinite, so only if we prevent cycles 
 - Is it optimal?
 	- No, it finds the “leftmost” solution, regardless of depth or cost


<h2 id="ae5c4b868b5b24149decba70c74165c2"></h2>
### Breadth-First Search

 - Strategy: 
 	- expand a shallowest node first
 - Implementation: 
 	- Fringe is a FIFO queue

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BFS.png)


#### Breadth-First Search (BFS) Properties

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_bfs_property.png)

 - What nodes does BFS expand?
	- Processes all nodes above shallowest solution
	- Let depth of shallowest solution be *s*
	- Search takes time **O(bˢ)** , 最坏情况，遍历所有s 层节点
 - How much space does the fringe take?
	- Has roughly the last tier, so **O(bˢ)**
 - Is it complete?
	- Yes. *s* must be finite if a solution exists.
 - Is it optimal?
	- Only if costs are all 1 (more on costs later)





#### Iterative Deepening

 - Idea: get DFS’s space advantage with BFS’s time / shallow-solution advantages
 	- Run a DFS with depth limit 1.  If no solution…
 	- Run a DFS with depth limit 2.  If no solution…
 	- Run a DFS with depth limit 3.  …
 - Isn’t that wastefully redundant?
 	- 会有重复计算
 	- Generally most work happens in the lowest level searched, so not so bad!
 		- 计算量按指数级别展开，所以重复计算的计算量比例并不大


### Cost-Sensitive Search

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_cost_sensitive_search.png)

 - BFS finds the shortest path in terms of ***number of actions***.
 - It does not find the least-cost path.  
 - We will now cover a similar algorithm which does find the least-cost path.  


#### Uniform Cost Search

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_uniform_cost_search.png)

 - Strategy: 
 	- expand a cheapest node first:
 - Fringe is a priority queue (priority: cumulative cost)
 - 注意, 这个例子中，当搜索至 ...e->r->f 时，下一步展开不是 f->G , 而是 S->e 

#### Uniform Cost Search (UCS) Properties

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ucs_property.png)

 - What nodes does UCS expand?
	- Processes all nodes with cost less than cheapest solution!
	- If that solution costs C* and arcs cost at least ε , then the “effective depth” is roughly C\*/ε
	- Takes time **O(b<sup>C\*/ε</sup>)** (exponential in effective depth)
 - How much space does the fringe take?
	- Has roughly the last tier, so **O(b<sup>C\*/ε</sup>)**
 - Is it complete?
	- Yes. Assuming best solution has a finite cost and minimum arc cost is positive.
 - Is it optimal?
	- Yes!  (Proof next lecture via A\* )





### DFS vs BFS vs UCS

 \ | DFS | BFS | UCS 
 --- | --- | --- | --- 
Strategy | leftmost | shallowest | cheapest
Implementation | LIFO stack | FIFO queue | 
Completeness | Yes, only if no cycle  |  Yes | Yes, if best solution is finite , and cost is positive
optimal | No | Yes , only if cost are same | Yes
Time | O(bᵐ) |  O(bˢ)  |  O(b<sup>C\*/ε</sup>)
Space |  O(b·m) |  O(bˢ) | O(b<sup>C\*/ε</sup>)





## Search and Models

 - Search operates over models of the world
 	- The agent doesn’t actually try all the plans out in the real world!
 	- Planning is all “in simulation”
 	- Your search is only as good as your models

## Some Hints for P1

 - Graph search is almost always better than tree search (when not?)
 - Implement your closed list as a dict or set!
 - Nodes are conceptually paths, but better to represent with a state, cost, last action, and reference to the parent node

---

# Informed Search 

 - Informed Search
	- Heuristics
	- Greedy Search
	- A* Search
 - Graph Search

Those 3 informed search do a lot of duplicate work and graph search will be our solution to that to avoid that duplicate work.


## The One Queue

 - All these search algorithms are the same except for fringe strategies
 	- Conceptually, all fringes are priority queues 
 		- (i.e. collections of nodes with attached priorities)
 	- Practically, for DFS and BFS, you can avoid the log(n) overhead from an actual priority queue, by using stacks and queues
 	- Can even code one implementation that takes a variable queuing object


## Uniform Cost Issues

 - Remember: UCS explores increasing cost contours
 - The good: UCS is complete and optimal!
 - The bad:
 	- Explores options in every “direction”
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ucs_explore_in_all_directions.png)
 	- No information about goal location
 - We’ll fix that soon!


## Search Heuristics

 - A heuristic is:
	- A function that estimates how close a state is to a goal
	- Designed for a particular search problem
	- Examples: Manhattan distance, Euclidean distance for pathing

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_heruistics_euclidean_distance.png)

### Example

For romania traveling problem:  constructor a cost table h(x) with straight-line distance to Bucharest.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_heuristic_example_dist.png)

For pancake problem:

h(x) = the number of the largest pancake that is still out of place

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_heuristic_example_pancake.png)

---

## Greedy Search

启发式搜索的一种:

 - Strategy: expand a node that you think is closest to a goal state
 	- Heuristic: estimate of distance to nearest goal for each state
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_greedy_search.png)
 - A common case:
 	- Best-first takes you straight to the (**wrong**) goal
 - Worst-case: 
 	- like a badly-guided DFS


---

## A\* search

### Combining UCS and Greedy

 - Uniform-cost orders by path cost, or backward cost  g(n)
 - Greedy orders by goal proximity, or forward cost  h(n)
 - A\* Search orders by the sum: f(n) = g(n) + h(n)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Astar_graph.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Astar_tree.png)





---

h value 6 here is too high. 6 is much higher than 3. In fact anytime it's higher than the real cost you can have this problem.

you lose you optimality guarantee , but your A star starts to look a little more like greedy , mean that you might not find out the path to goal but you might find a path to goal more quickly. 


 - Whould it be admissible ?
 	- Yes
 - Would we save on nodes expanded ?
 	- Yes
 - What's wroing with it ?
 	- it can be quit expensive





admissible heuristic with tree search is optimal but graph search no guarantees.
