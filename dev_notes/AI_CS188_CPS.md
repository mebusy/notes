...menustart

 - [Constraint Satisfaction Problems I](#8c8072703357c878142be0f423e13a69)
	 - [What is Search For?](#6135abe1c86a58db9f536d2f0279d4b1)
	 - [Constraint Satisfaction Problems](#ff7da4833835bc7f3506b068905f376c)
	 - [CSP Example: Map Coloring](#7c497b01fb991be051180f4dd6bc4dfd)
	 - [Exampe: N-Queens](#aee23a02cf0a428f8a3380804926c5ba)
	 - [Constraint Graphs](#5e3fadab67cd58dfc836b52e0eec6403)
		 - [Example : Cryptarithmetic](#e4f09537d31b275d624175f497d7a7a0)
		 - [Example: Sudoku](#1b0c55d7a4c5a4fc32c6095016869b4e)
		 - [Example: The Waltz Algorithm](#de9c82c8eb4d71f6d701b657ce8528b9)
	 - [Varieties of CSPs and Constraints](#b9434fb596306e69d9867441d7d9fa5f)
		 - [Varieties of CSPs](#62e238fa7cf63ce3e6bcd9fe1ebead89)
		 - [Varieties of Constraints](#03a54c9ac014bf6015d74f7b0468f36c)
	 - [Solving CSPs](#c7847ab059ee8aebf6d6b477f0c5c5a3)
		 - [Standard Search Formulation](#8aac949f2dcb8f35a610fe421087b36d)
		 - [Backtracking Search](#fe6282319a2be73c021b58a6d190368e)
		 - [Improving Backtracking](#b9b8d3f554a684894d60e5c3a7cdcf8e)
		 - [Filtering](#9a588db8471730dbfebac65cd5467ad8)
			 - [Forward Checking](#2dc9675ac8062df94ad72d42c57f68e1)
			 - [Constraint Propagation](#7e161a29d4c082578ae409a87a8988f0)

...menuend



<h2 id="8c8072703357c878142be0f423e13a69"></h2>
# Constraint Satisfaction Problems I

CPS


<h2 id="6135abe1c86a58db9f536d2f0279d4b1"></h2>
## What is Search For?

 - Assumptions about the world:  
 	- a single agent
 	- deterministic actions
 	- fully observed state
 		- you KNOW the configuration that you start in
 		- and then you plan about exactly how the world will evolve
 	- discrete state space

 - Planning: sequences of actions
 	- The path to the goal is the important thing
 	- Paths have various costs, depths
 	- Heuristics give problem-specific guidance

 - Identification: assignments to variables
 	- The goal itself is important, not the path
 	- All paths at the same depth (for some formulations)
 	- CSPs are specialized for identification problems

<h2 id="ff7da4833835bc7f3506b068905f376c"></h2>
## Constraint Satisfaction Problems

 - Standard search problems:
 	- State is a “black box”: arbitrary data structure
 	- Goal test can be any function over states
 	- Successor function can also be anything
 - Constraint satisfaction problems (CSPs):
 	- A special subset of search problems
 	- State is defined by ***variables Xᵢ***  with values from a ***domain D** (sometimes D depends on i)
 	- Goal test is a ***set of constraints*** specifying allowable combinations of values for subsets of variables
 - Allows useful general-purpose algorithms with more power than standard search algorithms

<h2 id="7c497b01fb991be051180f4dd6bc4dfd"></h2>
## CSP Example: Map Coloring

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_map_coloring.png)

 - Variables: WA, NT, Q, NSW, V, SA, T
 - Domains: D = {red, green, blue}
 - Constraints: adjacent regions must have different colors
 	- Implicit: WA ≠ NT 
 	- Explicit: (WA, NT) ∈ { (red,green),(red,blue), ... }
 - Solutions are assignments satisfying all constraints, e.g.
 	- {WA=red, NT=green, Q=red, NSW=green, V=red, SA=blue, T=green}

<h2 id="aee23a02cf0a428f8a3380804926c5ba"></h2>
## Exampe: N-Queens

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_N_queens.png)

Formulation 1:

 - Variables: Xᵢⱼ
 - Domains: {0,1}
 - Constraints
 	- ∀i,j,k (Xᵢⱼ, X<sub>ik</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>kj</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>i+k, j+k</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>i+k, j-k</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- Σ Xᵢⱼ = N


Formulation 2:

 - Variables: Q<sub>k</sub>
 	- in each row , the value is going to be where the Queen for that row is.
 - Domains: {1,2,3, ... , N } 
 - Constraints:
 	- Implicit: ∀i,j non-threatening(Qᵢ,Qⱼ) 
 	- Explicit: (Q₁,Q₂) ∈ { (1,3),(1,4), ... } , ...


<h2 id="5e3fadab67cd58dfc836b52e0eec6403"></h2>
## Constraint Graphs

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_constraints_graph.png)

 - Binary CSP: 
 	- each constraint relates (at most) two variables
 - Binary constraint graph: 
 	- nodes are variables, arcs show constraints
 - General-purpose CSP algorithms use the graph structure to speed up search. 
 	- E.g., Tasmania is an independent subproblem!


<h2 id="e4f09537d31b275d624175f497d7a7a0"></h2>
### Example : Cryptarithmetic

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Cryptarithmetic.png)

 - Variables:
 	- F T U W R O X₁ X₂ X₃
 - Domains:
 	- { 0,1,2,3,4,5,6,7,8,9 }
 - Constraints:
 	- all diff ( F T U W R O  )
 	- O + O = R + 10·X₁   进位
 	- ...

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Cryptarithmetic_graph.png)

there are boxes which are constraints and the boxes are connected to all of the variables that participate in that constraints. 

<h2 id="1b0c55d7a4c5a4fc32c6095016869b4e"></h2>
### Example: Sudoku

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_example_sudoku.png)

 - Variablels:
 	- Each (open) square
 - Domains:
 	- { 1,2, ... , 9 }
 - Constraints:
 	- 9-way alldiff for each columen
 	- 9-way alldiff for each row
 	- 9-way alldiff for each region
 	- (or can have a bunch of pairwise inequality constraints)


<h2 id="de9c82c8eb4d71f6d701b657ce8528b9"></h2>
### Example: The Waltz Algorithm

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Waltz_algorithm.png)

 - The Waltz algorithm is for interpreting line drawings of solid polyhedra as 3D objects
 - An early example of an AI computation posed as a CSP 

Approach:
 
 - Each intersection is a variable
 - Adjacent intersections impose constraints on each other
 - Solutions are physically realizable 3D interpretations

<h2 id="b9434fb596306e69d9867441d7d9fa5f"></h2>
## Varieties of CSPs and Constraints

<h2 id="62e238fa7cf63ce3e6bcd9fe1ebead89"></h2>
### Varieties of CSPs

 - Discrete Variables
	- Finite domains
		- Size d means O(dn) complete assignments
		- E.g., Boolean CSPs, including Boolean satisfiability (NP-complete)
	- Infinite domains (integers, strings, etc.)
		- E.g., job scheduling, variables are start/end times for each job
		- Linear constraints solvable, nonlinear undecidable

 - Continuous variables
	- E.g., start/end times for Hubble Telescope observations
	- Linear constraints solvable in polynomial time by LP methods (see cs170 for a bit of this theory)

<h2 id="03a54c9ac014bf6015d74f7b0468f36c"></h2>
### Varieties of Constraints

 - Varieties of Constraints
	- Unary constraints involve a single variable (equivalent to reducing domains), e.g.:
		- SA ≠ green
	- Binary constraints involve pairs of variables, e.g.:
		- SA ≠ WA
	- Higher-order constraints involve 3 or more variables: 
		- e.g., cryptarithmetic column constraints

- Preferences (soft constraints):
	- E.g., red is better than green
	- Often representable by a cost for each variable assignment
	- Gives constrained optimization problems
	- (We’ll ignore these until we get to Bayes’ nets)

<h2 id="c7847ab059ee8aebf6d6b477f0c5c5a3"></h2>
## Solving CSPs

<h2 id="8aac949f2dcb8f35a610fe421087b36d"></h2>
### Standard Search Formulation

 - Standard search formulation of CSPs
 - States defined by the values assigned so far (partial assignments)
	- Initial state: 
		- the empty assignment, {}
	- Successor function: 
		- assign a value to an ***unassigned*** variable
	- Goal test: 
		- the current assignment is complete and satisfies all constraints

We’ll start with the straightforward, naïve approach, then improve it


<h2 id="fe6282319a2be73c021b58a6d190368e"></h2>
### Backtracking Search 

 - Backtracking search is the basic ***uninformed*** algorithm for solving CSPs
 - Idea 1: One variable at a time
	- Variable assignments are commutative, so fix ordering
	- I.e., [WA = red then NT = green] same as [NT = green then WA = red]
	- Only need to consider assignments to a single variable at each step

 - Idea 2: Check constraints as you go
	- I.e. consider only values which do not conflict previous assignments
	- Might have to do some computation to check the constraints
	- “Incremental goal test”

 - Depth-first search with these two improvements
	is called backtracking search (not the best name)

 - Can solve n-queens for n <= 25

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_backtrack_search_example.png)

```
function BACKTRACKING-SEARCH( csp ) return solution/failure
	return RECURSIVE-BACKTRACKING( {} , csp )

function RECURSIVE-BACKTRACKING( assignment, csp ) return soln/failure
	if assignment is complete then return assignment
	var <- SELECT-UNASSIGNED-VARIABLE( VARIABLES[csp], assigment, csp )

	// for each value in that values , you loop through them in some order
	for each value in ORDER-DOMAIN-VALUES( var, assignment , csp ) do
		// for each of those values you check if
		// this variable takes this new value did I break a constraint.
		if value is consistent with assigment given CONSTRAINTS[csp] then
			add {var = value} to assignment
			result <- RECURSIVE-BACKTRACKING( assignment , csp )
			if result ≠ failure then return result
			// result is failure
			remove {var = value} from assignment
	return failure
```

 - Backtracking = DFS + variable-ordering + fail-on-violation
 - What are the choice points?


<h2 id="b9b8d3f554a684894d60e5c3a7cdcf8e"></h2>
### Improving Backtracking

 - General-purpose ideas give huge gains in speed
 - Ordering:
	- Which variable should be assigned next?  变量顺序
	- In what order should its values be tried?  值选择顺序
 - Filtering: 
 	- Can we detect inevitable failure early?
 - Structure: 
 	- Can we exploit the problem structure?
 	- Do things like notice tasmanis separate and solve it separately

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_CSP_order_filter.png)

<h2 id="9a588db8471730dbfebac65cd5467ad8"></h2>
### Filtering

Filtering is about ruling out suspects.

<h2 id="2dc9675ac8062df94ad72d42c57f68e1"></h2>
#### Forward Checking

Filtering | Forward checking
--- | ---
Keep track of domains for unassigned variables and cross off bad options | Cross off values that violate a constraint when added to the existing assignment


idea : keep track of all of the unassigned variables , keep track of what values they might reasonably take when we finally get to them.

in forward checking every time I assign a variable right which collapses its domain to a single choice for now , I checked to see whether there are other unassigned variables that have some illegal values when I take into account that new assignment. 


example 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_forward_checking_example.png)

If we assigned red to WA , we should remove red choice from NT , SA.

so that basic idea when I assigned something I look at its ***neighbors*** in the graph and cross things off, that's called forward checking.

forward checking doesn't check interactions between unassigned variables just checks interactions between assigned variables and their neighbors.  只检测 比邻的 变量


<h2 id="7e161a29d4c082578ae409a87a8988f0"></h2>
#### Constraint Propagation

Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_constraints_propagation.png)

NT and SA cannot both be blue! Why didn’t we detect this yet?

Constraint propagation: reason from constraint to constraint.

#### Consistency of A Single Arc

The idea of checking single arcs:

so far we talked about checking an assignment against its neighbors and here we were talking just in this last slide about checking between two unassigned variables.

what does it mean to check an arc ?  we look at an arc what it means to check it is formally we check whether or not is consistent so we say: 

An arc X → Y is consistent if for every x in the tail ( not arrow ) there is some y in the head which could be assigned without violating a constraint

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_consistency_of_Arc.png)

Forward checking: Enforcing consistency of arcs pointing to each new assignment

#### Arc Consistency of an Entire CSP

A simple form of propagation makes sure all arcs are consistent:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_arc_consistenct_of_an_entire_CSP.png)

***Remember: Delete from  the tail!***

 - Important: If X loses a value, neighbors of X need to be rechecked!
 - Arc consistency detects failure earlier than forward checking
 - Can be run as a preprocessor or after each assignment 
 - What’s the downside of enforcing arc consistency?

#### Enforcing Arc Consistency in a CSP

```
function AC-3(csp) return the CSP, possibly with reduced domains
	inputs: csp // a binary CSP with variables {X₁, X₂, ... ,Xn}
	local variables: queue // a queue of arcs, initially all the arcs in csp
	while queue is not empty do
		(Xᵢ, Xⱼ) <- REMOVE-FIRST(queue)
		if REMOVE-INCONSISTENT-VALUES(Xᵢ, Xⱼ) then
			for each X_k in NEIGHBORS[Xᵢ] do
				add (X_k, Xᵢ) to queue
end func

function REMOVE-INCONSISTENT-VALUES(Xᵢ, Xⱼ) returns true iff succeeds
	removed <- false
	for each x in DOMAIN[Xᵢ] do
		if no value y in DOMAIN[Xⱼ] allows (x,y) to satisfy the constraint Xᵢ <-> Xⱼ
			then delete x from DOMAIN[Xᵢ]; removed <- true
	return removed
end func
```

 - Runtime: O(n²d³), can be reduced to O(n²d²)
 - but detecting all possible future problems is NP-hard 


#### Limitations of Arc Consistency

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_arc_consistency_wrong.png)

 - After enforcing arc consistency:
 	- Can have one solution left
 	- Can have multiple solutions left
 	- Can have no solutions left 
 	- Not know it

 - Arc consistency still runs inside a backtracking search!


### Ordering

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_backtracking_ording.png)

#### Ordering: Minimum Remaining Values

 - Variable Ordering:  Minimum remaining values (MRV):
 	- Choose the variable with the fewest legal left values in its domain
 - Why min rather than max?
 	- Also called “most constrained variable”
	- “Fail-fast” ordering

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ordering_MRV.png)

--- 

#### Ordering: Least Constraining Value

 - Value Ordering: Least Constraining Value
 	- Given a choice of variable, choose the least constraining value
 		- 选择这个值，产生的约束最少
 	- I.e., the one that rules out the fewest values in the remaining variables
	- Note that it may take some computation to determine this!  (E.g., rerunning filtering)
 - Why least rather than most?
	- Combining these ordering ideas makes 1000 queens feasible

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ordering_LCV1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ordering_LCV2.png)




