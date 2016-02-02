...menustart

 * [Graphs Search and Connectivity](#f0d7fbb0d536bd31e98c816abecf06db)
	 * [Overview](#3b878279a04dc47d60932cb294d96259)
		 * [A few Motivations](#6a5969354d78fb42530a1ba9ef9c8a84)
		 * [Generic Graph Search](#f7714d50e6db96c58479fdaa5a307a37)
		 * [BFS vs. DFS](#8f0317dee85f46e2bef49cbc47b53c95)
	 * [BFS](#838fea3c1a3e8dd6c22fe9605a701668)
		 * [BFS 算法:](#9c054fc83157f4b9181e4cdc4fe6ff82)
 * [[all nodes initially unexplored]](#d176df2069c4df6c60921c3b256ab445)
		 * [Application: Shortest Paths](#a607a389d3fa7d06d4ce8c6940b4f3bf)
		 * [Application: Undirected Connectivity](#e47cac3e7cfeacdc8aed91eb9e98eea5)
	 * [DFS](#c1bb62b63c65be3760b715faad0bdf8d)
		 * [Application: Topological Sort](#c9350e8026b6019e6720cafd1dc497cd)
			 * [Straightforward Solution](#3543902b9027d30d2b49582942e85295)
			 * [Topological Sort via DFS (Slick)](#d7a8070d6eb65d2ff093c042be15718d)
		 * [Computing Strong Components: The Algorithm](#93b138293d718987548fc19b16f45497)
			 * [Strongly connected components (SCC) of a directed graph 有向图强连通分量](#b231ce60bec70f980b99bd9d572e0197)
			 * [Why Depth-First Search ?](#fefa6604dfa6c82f161b0fa76c9ea681)
			 * [Kosaraju's Two-Pass Algorithm](#901a2e2265db7c1c2e2049c90efca06d)
			 * [Kosaraju Algorithm Analysis](#e3579feaabb0560de815f22184bda921)
	 * [exam](#654816f85dfe2115674e7115c7d1ea51)

...menuend




<h2 id="f0d7fbb0d536bd31e98c816abecf06db"></h2>
# Graphs Search and Connectivity

<h2 id="3b878279a04dc47d60932cb294d96259"></h2>
## Overview

<h2 id="6a5969354d78fb42530a1ba9ef9c8a84"></h2>
### A few Motivations

 1. check if a network is connected (can get to anywhere from anywhere else)
 2. driving direction
 3. formulate a plan ( eg. how 2 fill in a sudoku puzzle as directed graph )
  
   - nodes: a partially completed puzzle
   - arcs : filling in one new squares

<h2 id="f7714d50e6db96c58479fdaa5a307a37"></h2>
### Generic Graph Search

Goal: 

 1. find everything findable from a given start vertex
 2. don't explore anything twice. Goal: O(m+n) time

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/generic_graph_search.png)

```
GenericAlgorithm( given Graph G , vertex s ):
- initial s explored , all other vertices unexplored
- while possible:
  - choose an edge (u,v) with u explored and v unexplored
    (if not halt)
  -mark v explored
```

**Claim**: at the end of algorithm, v explored <==> G has a path from s to v. (G undirected or directed)

<h2 id="8f0317dee85f46e2bef49cbc47b53c95"></h2>
### BFS vs. DFS

Breadth-First Search (BFS):

 - explore nodes in "layers"
 - can compute **shortest paths** (因为优先遍历同一层node,然后扩散出去)
 - can compute connected compnents of an *undirected* graph
 - O(m+n) time using a queue (FIFO)
  
Depth-First Search (DFS):

 - explore aggressively like a maze, backtrack only necessary
 - compute topological ordering of *directed* ***acyclic*** graph
 - compute connected components in *directed* graphs
 - O(m+n) time using a stack (LIFO or via recursion)

<h2 id="838fea3c1a3e8dd6c22fe9605a701668"></h2>
## BFS

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BFS.png)


<h2 id="9c054fc83157f4b9181e4cdc4fe6ff82"></h2>
### BFS 算法:

```
BFS( graph G , start vertex s)
<h2 id="d176df2069c4df6c60921c3b256ab445"></h2>
#[all nodes initially unexplored]
- mark s as explored
- let Q=queue data structure (FIFO initialized with s)
- while Q != ∅:
  - remove the 1st node of Q, call it v
  - for each edge (v ,w ):
    - if w unexplored:  # unexplored node only
      - mark w as explored
      - append w to end of Q
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BFS_search.png)   

 - At the end of BFS, v explored <=> G has a path from s to v.
 - running time of main loop = O(n_s + m_s) , where n_s = number of nodes reachable from s, m_s = number of edges reachable from s.

<h2 id="a607a389d3fa7d06d4ce8c6940b4f3bf"></h2>
### Application: Shortest Paths

Goal: compute dist(v), the fewest number of edges on a path from s to v.

Extra Code:

```
- initialize dist(v) = 0 if v=s , +∞ if v!=s
```

When considering edge(v,w):

```
- if w unexplored , then set dist(w) = dist(v) +1
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BFS_shortest_path.png)   

At termination , dist(v)=i <=> v in iᵗʰ large ( shortest s-v path has i edges )

<h2 id="e47cac3e7cfeacdc8aed91eb9e98eea5"></h2>
### Application: Undirected Connectivity

Most of this stuff about graph search it really doesn't matter undirected or directed, the big exception is when you're computing connectivity.

Here I'm only gonna talk about undirected graphs. In directed case , we can again get a very efficient algorithms for it.

 - Let G(V,E) be an undirected graph
 - Connected components = the "pieces" of G
 - Formal definition : equivalence classes (等价类) of the relation u~v <==> ∃ u-v path in G (U being related to V if and only if there's a path between U and V in the graph G)

Goal: compute all connected components

Why :

 - check if network is disconnected
 - graph visualization ( clustering )

 

算法（undirected case）:

```
- all node unexplored 
  #[assume labeled 1 to n]
- for i=1 to n :  
  - if i not yet explored : 
    - BFS(G,i)
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BFS_connected_components.PNG)   

<h2 id="c1bb62b63c65be3760b715faad0bdf8d"></h2>
## DFS

DFS explores aggressively and uses when trying to solve a maze.

DFS 算法有两种实现：

 1. BFS基础上,使用 stack 结构替代 queue, 以及一些细微修改
 2. recursive version


```
DFS(graph G , start vertex s):
- mark s as explored
- for every edge (s,v):
  - if v unexplored:
    - DFS(G,v)
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DFS.PNG) 

 - At the end of the algorithm , v marked as explored <=> ∃ path from s to v in G.
 - Running time is O(n_s + m_s ) , n_s is number of nodes reachable from s, m_s is number of edges reachable from s. Look at each node in connected compoment of s at most once, each edge at most twice.

<h2 id="c9350e8026b6019e6720cafd1dc497cd"></h2>
### Application: Topological Sort

A *topological ordering* of a ***directed*** graph G is a labelling *f* of G's node sucn that:

 1. the f(v) are the set { 1,2,...,n }
 2. (u,v) ∊ G => f(u) < f(v) ( acyclic )


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/topologicalSort.PNG)

So there are only two topological orderings of the directed graph above.

---

 - Motivation: sequence tasks while respecting all precedence constraints (优先约束)
 - Note: G has directed cycle => **NO** topological ordering
 - Theorem: no directed cycle => can compute topological ordering in O(m+n) time

<h2 id="3543902b9027d30d2b49582942e85295"></h2>
#### Straightforward Solution

Every directed acyclic graph has at least a sink vertex(汇顶点) . That is a vertex without any outgoing arcs. 上面的例子中, t 就是 sink vertex. 

Follow n arcs , we can see n+1 vertices . If those "n+1" vertices has only n distinct vertices, we're gonna see some vertex twice, and we have exhibited a directed cycle.

So vertices with no sink vertex has to have a directed cycle.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/sink_vertex.PNG)

To compute topological ordering:

The final position in the ordering are the sink vertices.

 - let v be a sink vertex of G
 - set f(v) = n 
 - recurse on G - {v}

If you take a directed acyclic graph, and you delete one or more vertices from it, you still gonna have a directed acyclic graph.
 
 
<h2 id="d7a8070d6eb65d2ff093c042be15718d"></h2>
#### Topological Sort via DFS (Slick)

```
DFS(graph G , start vertex s):
- mark s as explored
- for every edge (s,v):
  - if v unexplored:
    - DFS(G,v)
- set f(s) = current_label  // DFS遍历算法基础上新增
- current_label --          // DFS遍历算法基础上新增

DFS_Loop( graph G )
- mark all nodes unexplored
- current_label = n # to keep track of ordering
- for each vertex v ∊ G:
  - if v unexplored:
    - DFS(G,v)
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/topologicalSort_4nodes.PNG)

The above graph has 4 vertices, so we initialize the current_lable to be 4 . Assuming that we start from vertex V. We first call DFS from V,  the only place you can go from V is to T . So we recursively call DFS of T. There is no edges to go through. We finish the for-loop and so T is going to be assigned an F value equal to the current_lable, 4. 

So now we're done with T we back track back to V . We decrease current_label. Now there is no more outgoing arcs to explore, so its for-loop is finished. So it gets what's the new current_label, 3.  

Then maybe after that we tried on S. So, maybe S is the 3rd vertex that the for-loop considers, only SW arc is unexplored ...

Running Time : O(m+n) , you will not visit a node twice.

<h2 id="93b138293d718987548fc19b16f45497"></h2>
### Computing Strong Components: The Algorithm

如果有向图是强连通的，则任两个节点都是相互可达。故必可做一回路经过图中所有各点。

在有向图G中，如果两个顶点间至少存在一条路径，称两个顶点强连通(strongly connected)。如果有向图G的每两个顶点都强连通，称G是一个强连通图。

非强连通图有向图的 极大强连通子图，称为强连通分量(strongly connected components)。


<h2 id="b231ce60bec70f980b99bd9d572e0197"></h2>
#### Strongly connected components (SCC) of a directed graph 有向图强连通分量

G are the equivalence classes of the relation:

u~v <==> ∃ path u ~~> v and  v ~~> u in G 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/SCC.PNG)


<h2 id="fefa6604dfa6c82f161b0fa76c9ea681"></h2>
#### Why Depth-First Search ?

如上图，如果我们从 最右侧的SCC 中的任意一个 node开始查找, DFS可以找到这3个nodes 组成的SCC; 但是 如果最下面的 node开始查找, DFS会找到下方和有方两个SCC的集合; 如果我们直接从最左边的 node 开始查找，则DFS会找到整个graph. 

可以看到，从不同的node开始DFS, 会得到不同的结果. 所以，在应用DFS之前，我们需要一步预处理。

<h2 id="901a2e2265db7c1c2e2049c90efca06d"></h2>
#### Kosaraju's Two-Pass Algorithm

这个算法利用了一个事实，即转置图（同图中的每边的方向相反）具有和原图完全一样的强连通分量。

This algorithm can compute SCCs in O(m+n) time.


Algorithm : (given directed graph G)

 1. let G_rev = G wieh all arcs reversed
 2. run DFS_Loop on G_rev,计算出各顶点完成搜索的时间f
   let f(v) = "finishing time" of each v ∊ V. eg. S->v->w , `f(w)=1,f(v)=2,f(S)=3`

 3. run DFS_Loop on G
  processing nodes in decreasing order of finishing times (按照各顶点f值由大到小的顺序).DFS所得到的森林即对应连通区域。 [SCCs = nodes with the same "leader"]


The 2nd step will discover the strongly connected components one at a time in a very natural way, it's really important that 3rd step executes the depth first searches in a particular order, that it goes through the nodes of the graph in a particular order. 

The search on the reverse graph is going to compute an ordering of the nodes, which, when the second DFS goes through them in that order , it will just discover SCCs one at a time in linear time.

The nodes in the same strongly connected components will be labeld with exactly the same leader node.

**DFS-Loop**:

```
DFS_Loop( graph G )
global variable t = 0 // for finishing times for 1st pass
//t is to count how many nodes we have totally finished exploring at this point

global variable s = NULL  // compute "leaders" for 2nd pass
// what S keeps track of is the  most recent vertex from which a DFS was initiated, the current source vertex.

//Assume nodes labeled from 1 to n
//for 1st search , nodes are gonna be labelled totaly arbitary.
//for 2nd search , we're gonna use the finishing times as the labeling.

for i=n downto 1:
  if i not ye explored:
    s:=1
    DFS(G,i)

//-------------

DFS(graph G, node i)
- mark i explored
- set leader(i) := s //纪录这个node的leader
- for each arc (i,j) ∊ G:
  - if j not yet explored:
    - DFS( G,j )
- t++
- set f(i) := t
```

**example**:  

1st search, 从node 9出发, 假设先走9-6-3的路径 ; then 恢复到原图，2nd search.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Kosaraju_example.PNG)

**Running TIme**: 2*DFS = O(m+n)

<h2 id="e3579feaabb0560de815f22184bda921"></h2>
#### Kosaraju Algorithm Analysis

**Claim**: the SCCs of a directed graph induce an acyclic "meta-graph".

 - meta-nodes = the SCCs , C₁,...,C_k of G
 - ∃ arc C->Ċ <==> ∃ arc(i,j) ∊ G , with i ∊ C , j ∊ Ċ
   >![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/meta-nodes.PNG)

---

把有向图的 SCC 作为 meta-node, 最后得到的简图, is a directed acyclic graph:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/meta-graph.PNG)

So in fact, **the SCC of the origin graph G and its reversal G_rev are exactly the same**.

---

If C₁,C₂ is adjacent SCCs in G , `C₁-> C₂` ,  

Let f(v) = finishing times of DFS_Loop in `G_rev` .

Then max( f(v) , v ∊ C₁ ) < max( f(v) , v ∊ C₂ ) , G_rev 是  C₁ <- C₂ , 所以G_rev 中起点C₂的f(v)最大 , 而在 原图G中则f(v)最大的C₂为终点 。

Collorary 推论: maximum f-value of G must lie in a "Sink SCC".

ByCollorary: 2nd pass of DFS_Loop begins somewhere in a Sink SCC C*.

2nd pass 从 G 的C₁中的某个node 开始DFS_Loop是否非常坏的结果, Kosaraju算法可以确保 从 Sink SCC C₂中的某个node开始遍历，找出强连通分量。

for 2nd pass:

 - first call to DFS discovers C* and nothing else !
 - rest of DFS_Loop like recursing on G with C* deleted ( starts in a sink SCC of G-C*)
 

<h2 id="654816f85dfe2115674e7115c7d1ea51"></h2>
## exam

 1. Q1: θ(m)
 2. Q2: 邻接矩阵 vertex s-t path 搜索的时间复杂度： θ(n²)
 3. Q3: r<=d , r>=d/2
 4. Q4: Sometimes yes, sometimes no
 5. Q5: 给 directed graph G 添加一条边, 一般来说都会减少SCC的数量，但如果图本身是强连通图,SCC数量不变。

