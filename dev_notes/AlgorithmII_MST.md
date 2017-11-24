...menustart

 - [4.3 MINIMUM SPANNING TREES](#cded71731adc3237f9d3c51dd89049c0)
     - [introduction](#8800e1c9b3e22c44ba59a34db3fe4841)
         - [Example Problem](#fa051064ee16bea712664bb248654763)
     - [greedy algorithm](#a9728ca20b5c52a76d67320f3fe3ec4e)
         - [Cut property](#f027e6426815659632b54ae818592211)
         - [Greedy MST algorithm](#5d1da5f08e2888d73349900d4db5c622)
         - [Greedy MST algorithm: correctness proof](#bdd4ba94c65abf3884971d7a8b7cb542)
         - [Removing two simplifying assumptions](#3d825bc82fff7cd0178bee0eb6d5c38e)
     - [Kruskal's algorithm](#5efdc253657f5526080aea52d632d9a9)
         - [Kruskal's algorithm](#5efdc253657f5526080aea52d632d9a9)
         - [Kruskal's algorithm: correctness proof](#ea2e8ed0f2060e40803d07b642e735dd)
         - [Kruskal's algorithm: implementation challenge](#6769f30cada6dad70abd9ec0e78fab39)
         - [Kruskal's algorithm: running time](#6c146d59dece811375bd56462f359767)
     - [Prim's algorithm](#9f18a401049668114eca679e98d5f2e1)
         - [Prim's algorithm](#9f18a401049668114eca679e98d5f2e1)
         - [Prim's algorithm: proof of correctness](#38cd4863a58c575a66fc80ab33a4b1b0)
         - [Prim's algorithm: implementation challenge](#ca5d698ccb98d8b805ad4456d828f20c)
         - [Lazy Prim's algorithm: running time](#6da63afd831a4613957674b1c0c78ca5)
         - [Prim's algorithm: eager implementation](#ab84d0fc34342968251318250a1bf5d3)

...menuend


<h2 id="cded71731adc3237f9d3c51dd89049c0"></h2>

# 4.3 MINIMUM SPANNING TREES

<h2 id="8800e1c9b3e22c44ba59a34db3fe4841"></h2>

## introduction

 - Given. Undirected graph *G* with positive edge weights (connected).
 - Def. A **spanning tree** of *G* is a subgraph *T* that is both a **tree**  and **spanning** .
    - **tree** means it is connected and acyclic
    - **spanning** means it includes all of the vertices
 - Goal. Find a min weight spanning tree.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_g0.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_g0_mst.png)

 - Brute force. Try all spanning trees?

<h2 id="fa051064ee16bea712664bb248654763"></h2>

### Example Problem

 - 有一块木板，板上钉上了一些钉子，这些钉子可以由一些细绳连接起来。假设每个钉子可以通过一根或者多根细绳连接起来，那么一定存在这样的情况，即用最少的细绳把所有钉子连接起来
 - 在某地分布着N个村庄，现在需要在N个村庄之间修路，每个村庄之前的距离不同，问怎么修最短的路，将各个村庄连接起来。
 - 以上这些问题都可以归纳为最小生成树问题


<h2 id="a9728ca20b5c52a76d67320f3fe3ec4e"></h2>

## greedy algorithm

 - Simplifying assumptions.
    - Edge weights are distinct (no two edge weights are equal).
    - Graph is connected.
 - Consequence
    - MST exists and is unique.

<h2 id="f027e6426815659632b54ae818592211"></h2>

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

<h2 id="5d1da5f08e2888d73349900d4db5c622"></h2>

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

<h2 id="bdd4ba94c65abf3884971d7a8b7cb542"></h2>

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

<h2 id="3d825bc82fff7cd0178bee0eb6d5c38e"></h2>

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

<h2 id="5efdc253657f5526080aea52d632d9a9"></h2>

## Kruskal's algorithm

<h2 id="5efdc253657f5526080aea52d632d9a9"></h2>

### Kruskal's algorithm


 - Consider edges in ascending order of weight.
    - Add next edge to tree *T* unless doing so would create a cycle

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_Kruskal.png)

<h2 id="ea2e8ed0f2060e40803d07b642e735dd"></h2>

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


<h2 id="6769f30cada6dad70abd9ec0e78fab39"></h2>

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


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_Kruskal_challenge.png)


 - Efficient solution. Use the *union-find* data structure.
 
```java
public class KruskalMST {
    private Queue<Edge> mst = new Queue<Edge>();
    public KruskalMST(EdgeWeightedGraph G) {
        // build priority queue
        MinPQ<Edge> pq = new MinPQ<Edge>();
        for (Edge e : G.edges())
            pq.insert(e);

        UF uf = new UF(G.V());
        while (!pq.isEmpty() && mst.size() < G.V()-1) {
            // greedily add edges to MST
            Edge e = pq.delMin();
            int v = e.either(), w = e.other(v);
            // edge v–w does not create cycle
            if (!uf.connected(v, w)) {
                // merge sets
                uf.union(v, w);
                // add edge to MST
                mst.enqueue(e);
            }
        } 
    }
    public Iterable<Edge> edges() {  
        return mst;  
    }
}
```

<h2 id="6c146d59dece811375bd56462f359767"></h2>

### Kruskal's algorithm: running time

 - Proposition. Kruskal's algorithm computes MST in time proportional to *ElogE* (in the worst case).
 - Proof

operation | frequency | time per op
--- | --- | ---
build pq | 1 | ElogE
delete-min | E | logE
union | V | log\*V 
connected | E | log\*V 

 - Remark. If edges are already sorted, order of growth is Elog\*V.
    - recall: log\*V ≤ 5 in this universe

---

<h2 id="9f18a401049668114eca679e98d5f2e1"></h2>

## Prim's algorithm

<h2 id="9f18a401049668114eca679e98d5f2e1"></h2>

### Prim's algorithm

 - Start with vertex 0 and greedily grow tree *T*.
 - Add to *T* the min weight edge with exactly one endpoint in *T*
    - grow the tree one edge at a time, and always keeping it connected. 
 - Repeat until V-1 edges

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim.png)

 - start from vertex 0, the minimum weight edge connect to 0 is 0-7 , so we add it, now we have a MST , it have only 2 vertices 0,7
 - now we have 7 edges connect to our MST, we add the minimum one : 1-7
 - repeat ...
 - finally MST edges: 
    - 0-7  1-7  0-2  2-3  5-7  4-5  6-2

<h2 id="38cd4863a58c575a66fc80ab33a4b1b0"></h2>

### Prim's algorithm: proof of correctness

 - Proposition. [Jarník 1930, Dijkstra 1957, Prim 1959] Prim's algorithm computes the MST.
 - Proof
    - Prim's algorithm is a special case of the greedy MST algorithm.
    - Suppose edge *e* = min weight edge connecting a vertex on the tree to a vertex not on the tree.
    - Cut = set of vertices connected on tree
    - No crossing edge is black.
    - No crossing edge has lower weight.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_proof.png)

<h2 id="ca5d698ccb98d8b805ad4456d828f20c"></h2>

### Prim's algorithm: implementation challenge

 - Challenge. Find the min weight edge with exactly one endpoint in *T*.
 - How difficult?
    - E  :  try all edges
    - V 
    - logE : use a priority queue!
    - log\*E
    - 1
 - Lazy solution. Maintain a PQ of **edges** with (at least) one endpoint in *T*.
    - Key = edge; priority = weight of edge.
    - Delete-min to determine next edge `e = v–w` to add to *T*.
    - Disregard if both endpoints *v* and *w* are marked (both in *T*).
    - Otherwise, let *w* be the unmarked vertex (not in *T* ):
        - add to PQ any edge incident to *w* (assuming other endpoint not in *T*)
        - add *e* to *T* and mark *w*

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_lazy_impplementpng.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_lazy_1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_lazy_2.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_lazy_3.png)

 - edge becomes obsolete ( 2-7, 1-2 ) , lazy implementation leaves on PQ.

```java
public class LazyPrimMST {
    private boolean[] marked; // MST vertices
    private Queue<Edge> mst;  // MST edges
    private MinPQ<Edge> pq;  // PQ of edges
    
    public LazyPrimMST(WeightedGraph G) {
        pq = new MinPQ<Edge>();
        mst = new Queue<Edge>();
        marked = new boolean[G.V()];
        // assume G is connected
        visit(G, 0);
        while (!pq.isEmpty() && mst.size() < G.V() - 1)
        {
            // repeatedly delete the min weight edge e = v–w from PQ
            Edge e = pq.delMin();
            int v = e.either(), w = e.other(v);
            // ignore if both endpoints in T
            if (marked[v] && marked[w]) continue;
            // add edge e to tree
            mst.enqueue(e);
            // add v or w to tree
            if (!marked[v]) visit(G, v);
            if (!marked[w]) visit(G, w);
        }
    }

    private void visit(WeightedGraph G, int v) {
        marked[v] = true;  // add v to T
        for (Edge e : G.adj(v))
            if (!marked[e.other(v)]) {
                // for each edge e = v–w, 
                // add to PQ if w not already in T
                pq.insert(e);
            }
    }

    public Iterable<Edge> mst() {  
        return mst;  
    }
}
```

<h2 id="6da63afd831a4613957674b1c0c78ca5"></h2>

### Lazy Prim's algorithm: running time

 - Proposition. Lazy Prim's algorithm computes the MST in time proportional to `ElogE` and extra space proportional to *E* (in the worst case).
 - Proof

operation | frequency | binary heap
--- | --- | --- 
delete min | E | logE
insert | E | logE

---

<h2 id="ab84d0fc34342968251318250a1bf5d3"></h2>

### Prim's algorithm: eager implementation



