
# 4.3 MINIMUM SPANNING TREES

## introduction

 - Given. Undirected graph *G* with positive edge weights (connected).
 - Def. A **spanning tree** of *G* is a subgraph *T* that is both a **tree**  and **spanning** .
    - **tree** means it is connected and acyclic
    - **spanning** means it includes all of the vertices
 - Goal. Find a min weight spanning tree.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_g0.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_g0_mst.png)

 - Brute force. Try all spanning trees?

### Example Problem

 - 有一块木板，板上钉上了一些钉子，这些钉子可以由一些细绳连接起来。假设每个钉子可以通过一根或者多根细绳连接起来，那么一定存在这样的情况，即用最少的细绳把所有钉子连接起来
 - 在某地分布着N个村庄，现在需要在N个村庄之间修路，每个村庄之前的距离不同，问怎么修最短的路，将各个村庄连接起来。
 - 以上这些问题都可以归纳为最小生成树问题


## greedy algorithm

 - Simplifying assumptions.
    - Edge weights are distinct (no two edge weights are equal).
    - Graph is connected.
 - Consequence
    - MST exists and is unique.

### Cut property

 - Def. A **cut** in a graph is a partition of its vertices into two (nonempty) sets.
    - 对图切一刀，把顶点分成两份
 - Def. A **crossing edge** connects a vertex in one set with a vertex in the other.
 - Cut property. Given any cut, the crossing edge of min weight is in the MST.
    - The cut defines a set of crossing edges. 
    - The minimum weight crossing edge is in the MST.
    - Remember no two edges have the same weight so there's a single edge that has minimum weight in the crossing edges of a cut.
    - 描述了一个 cut 和 MST 的联系

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_cut_property.png)

 - Proof.
    - Suppose min-weight crossing edge *e* is not in the MST.
    - Adding *e* to the MST creates a cycle.
    - Some other edge *f* in cycle must be a crossing edge.
        - Otherwise the MST wouldn't be connected
    - Removing *f* and adding *e* is also a spanning tree.
    - Since weight of *e* is less than the weight of *f*, that spanning tree is lower weight.
    - Contradiction.
 - now given that property, we can develop what's called a greedy algorithm

### Greedy MST algorithm

Easiest algorithm, we can come up with. 

 - Start with all edges colored gray.
 - Find cut with no black crossing edges; color its min-weight edge black.
    - The algorithm's going to color some of the edges black. 
    - And color the minimum-weight edge of that cut black, and just repeat the algorithm. 
    - when you cut, 避开那些已经被染黑的边
    - As we get more and more black edges it's going to be harder to find a cut with no black crossing edges. 
 - Repeat until V - 1 edges are colored black.
    - And the claim is that that's going to compute an MST. 

### Greedy MST algorithm: correctness proof

 - Proposition. The greedy algorithm computes the MST.
 - Proof
    - Any edge colored black is in the MST (via cut property).
    - Fewer than V - 1 black edges => cut with no black crossing edges.
        - means, when we have fewer than v-1 black edges, there has to be a cut that has no black crossing edges. so that the algorithm doesn't get stuck.
        - the way to think about that is just take he verticies in one of the connected components ( vertices connected by black edges ), and make that the cut. Since that's a connected component , there's gonna be no black edges in the crossing edges for that cut.  
        - if you don't have an MST yet, there's going to be some cut with no black edges. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_greedyalgor_proof.png)

 - but how to implementations of the greedy algorithm ?
    - how we choose the cut? Which cut are we going to use? And also, how to find the minimum weight edge in the cut?
    - Those could both be expensive operations. And prohibitively expensive for huge graphs. 
 - Efficient implementations. Choose cut? Find min-weight edge?
    1. Kruskal's algorithm. [stay tuned]
    2. Prim's algorithm. [stay tuned]
    3. Borüvka's algorithm.
 - Before getting to those, what about removing the two simplifying assumptions? 

### Removing two simplifying assumptions

 - Q. What if edge weights are not all distinct?
 - A. Greedy MST algorithm still correct if equal weights are present!
    - there's multiple MSTs. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_equal_weights.png)
    - our correctness proof fails, but that can be fixed
 - Q. What if graph is not connected?
 - A. Compute minimum spanning forest = MST of each component.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_equal_unconnected.png)

 - **Greed is good.**
    - Basically what the greedy algorithm gives us is an easy way to prove correctness for specific algorithms. 
    - And then we can prove correctness of a more complicated algorithm. 
    - In general, in algorithm design this is proven to be affective in all kinds of domains. 
    - Trying to come up with a general algorithm that you can prove works efficiently and then using that to help design 

---

## Kruskal's algorithm

### Kruskal's algorithm


 - Consider edges in ascending order of weight.
    - Add next edge to tree *T* unless doing so would create a cycle

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_Kruskal.png)

### Kruskal's algorithm: correctness proof

 - Proposition. *[Kruskal 1956]* Kruskal's algorithm computes the MST.
 - Proof
    - Kruskal's algorithm is a special case of the greedy MST algorithm
    - Suppose Kruskal's algorithm colors the edge `e = v–w` black.
    - Cut = set of vertices connected to *v* in tree *T*.
        - we'll define a cut. That is the set of vertices that are connected to v. 
        - So it might be just a v, but if theres any black edges connecting v to other vertices we put all of those in the cut. 
    - No crossing edge is black.
        - So for that cut there's no black crossing edge. Cuz it's a component. 
    - No crossing edge has lower weight. Why?
        - And the other thing is that there's no crossing edge with lower weight than `v-w`.
            - because we are considering the edges in increasing order of their weight. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_Kruskal_proof.png)


### Kruskal's algorithm: implementation challenge

 - Challenge. Would adding edge `v–w` to tree *T* create a cycle? If not, add it.
 - How difficult?
    - E + V
    - V 
        - run DFS from v, check if w is reachable 
        - if v,w is reachable, adding edge `v-w` definitely will create a cycle.
    - logV
    - log\*V 
        - use the union-find data structure !
    - 1








