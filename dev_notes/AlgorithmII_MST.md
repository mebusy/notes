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

 - **Eager solution**
    - Maintain a PQ of vertices connected by an edge to *T*, were priority of vertex *v =* weight of shortest edge connecting *v* to *T*.
        - the Priority Queue is going to have vertices, those are vertices that are not on the tree, but are connected by an edge
        - so the PQ has at most one entry per vertex
    - Delete min vertex *v* and add its associated edge *e = v–w* to *T*.
        - show as the pic, the next step will delete vertex 2 from PQ , and add edge `0-2` to MST
    - Update PQ by considering all edges *e = v–x* incident to *v*
        - ignore if *x* is already in *T*
        - add *x* to PQ if not already on it
            - so vertex 3,6 will be added to PQ
        - **decrease priority** of *x* if *v–x* becomes shortest edge connecting x to T
            - after adding edge `0-2` to MST , the priority of vertex 3 should be decreased to 0.17 ( edge 2-3 ) , the priority of vertex 6 will be decreased to 0.40 ( edge 6-2 )

 - For this eager implementation, We're going to want the vertices that are connected to the tree by one vertex. And we're going to know the shortest edge connecting that vertex to the tree.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_eager.png)



#### Indexed priority queue

 - THe problem is , we have keys that the PQ algorithm doesn't really needs to know when we change values of keys.
    - so we have to do that throught the API.
    - and what we're going to do is allow the client to change the key by specifying the index and the new key.
    - and then the implementation will take care of changing the value and updating its data structure to reflect the changed values. 

 - since we are working with vertex indexed array and graphs, the priority queue implementation might do the same. 
    - we'll just associate an index, kind of pass the idea onto the PQ, to make it allow it to implement these operations.

 - Associate an index between 0 and N - 1 with each key in a priority queue.
    - Client can insert and delete-the-minimum.
    - Client can change the key by specifying the index.


```java
public class IndexMinPQ<Key extends Comparable<Key>>

----------------
// create indexed priority queue with indices 0, 1, ..., N-1
IndexMinPQ(int N) 

// associate key with index i
void insert(int i, Key key)

// decrease the key associated with index i
void decreaseKey(int i, Key key)

// is i an index on the priority queue?
boolean contains(int i)

// remove a minimal key and return its associated index
int delMin()
```

#### Implementation

 - Start with same code as MinPQ.
 - Maintain parallel arrays keys[], pq[], and qp[] so that:
    - keys[i] is the priority of i
    - pq[i] is the index of the key in heap position i
    - qp[i] is the heap position of the key with index i
 - Use swim(qp[i]) implement decreaseKey(i, key).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mst_prim_eger_implementation.png)

 - It's important to realize that it's possible to implement this decreased key operation in logarithmic time without ever having to search through everything,  using the idea of indexing.
 - `E + VlogV` can make a difference for a huge graph. 

## QA

 - Q: Minimum-weight feedback edge set
    - A feedback edge set of a graph is a subset of edges that contains at least one edge from every cycle in the graph. If the edges of a feedback edge set are removed, the resulting graph is acyclic. Given an edge-weighted graph, design an efficient algorithm to find a feedback edge set of minimum weight. Assume the edge weights are positive.
 - A: If the weight function is non-negative, then the set of edges not contained in a maximum weight spanning tree is indeed a MWFES. 




---

# 4.4 SHORTEST PATHS

 - Shortest paths in an edge-weighted digraph
    - Given an edge-weighted digraph, find the shortest path from *s* to *t*.
 - Shortest path variants
    - Which vertices?
        - Single source: from one vertex *s* to every other vertex
        - Source-sink: from one vertex *s* to another *t*.
        - All pairs: between all pairs of vertices.
    - Restrictions on edge weights?
        - Nonnegative weights.
        - Euclidean weights.
        - Arbitrary weights.
    - Cycles?
        - No directed cycles.
        - No "negative cycles."
 - Simplifying assumption. Shortest paths from *s* to each vertex *v* exist.

## shortest-paths properties

### Data structures for single-source shortest paths
 
 - Goal. Find the shortest path from *s* to every other vertex.
 - Observation. A **shortest-paths tree** (SPT) solution exists. Why?
    - if no 2 paths have the same length, then certainly it's going to be such a solution
    - if you've got 2 paths to the same vertex , you can delete the last edge on one of them and keep going 
    - what we want to do is compute a tree.
 - Consequence. Can represent the SPT with two vertex-indexed arrays:
    - distTo[v] is length of shortest path from s to v.
    - edgeTo[v] is last edge on shortest path from s to v.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_sp_sptree.png)

```java
public double distTo(int v) {  
    return distTo[v];  
}
public Iterable<DirectedEdge> pathTo(int v) {
   Stack<DirectedEdge> path = new Stack<DirectedEdge>();
   for (DirectedEdge e = edgeTo[v]; e != null; e = edgeTo[e.from()])
      path.push(e);
   return path;
}
```

### Edge relaxation

 - Relax edge *e = v→w* .
    - distTo[v] is length of shortest **known** path from s to v.
    - distTo[w] is length of shortest **known** path from s to w
    - edgeTo[w] is last edge on shortest **known** path from s to w
    - If *e = v→w* gives shorter path to w through v,  update both distTo[w] and edgeTo[w].

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_sp_relax_edge.png)

```java
private void relax(DirectedEdge e) {
    int v = e.from(), w = e.to();
    if (distTo[w] > distTo[v] + e.weight()) {
        distTo[w] = distTo[v] + e.weight();
        edgeTo[w] = e;
    }
}
```

### Shortest-paths optimality conditions

 - Proposition. 
    - Let G be an edge-weighted digraph. Then distTo[] are the shortest path distances from *s* iff:
        - distTo[s] = 0.
        - For each vertex *v*, distTo[v] is the length of some path from *s* to *v*.
        - For each edge *e = v→w*, distTo[w] ≤ distTo[v] + e.weight().
 - Pf. ⇐ [ necessary ]
    - Suppose that distTo[w] > distTo[v] + e.weight() for some edge *e = v→w*.
    - Then, e gives a path from s to w (through v) of length less than distTo[w].
 - Pf. ⇒ [ sufficient ]
    - Suppose that s = v0 → v1 → v2 → ... → vk = w is a shortest path from s to w.
    - Then, ( eᵢ = iᵗʰ edge on shortest path from s to w )
        - distTo[v1] ≤ distTo[v0] + e1.weight()
        - distTo[v2] ≤ distTo[v1] + e2.weight()
        - ...
        - distTo[vk] ≤ distTo[vk-1] + ek.weight()
    - Add inequalities; simplify; and substitute distTo[v0] = distTo[s] = 0:
        - distTo[w] = distTo[vk] ≤ e1.weight() + e2.weight() + ... + ek.weight()
    - Thus, distTo[w] is the weight of shortest path to w. 


### Generic shortest-paths algorithm

```
Generic algorithm (to compute SPT from s)
---------------------------
Initialize distTo[s] = 0 and distTo[v] = ∞ for all other vertices
Repeat until optimality conditions are satisfied:
    - Relax any edge.
```

 - Proposition. Generic algorithm computes SPT (if it exists) from s.
 - Pf sketch.
    - Throughout algorithm, distTo[v] is the length of a simple path from s to v (and edgeTo[v] is last edge on path).
    - Each successful relaxation decreases distTo[v] for some v.
    - The entry distTo[v] can decrease at most a finite number of times.

---

 - Efficient implementations. How to choose which edge to relax?
    - Ex 1. Dijkstra's algorithm (nonnegative weights).
    - Ex 2. Topological sort algorithm (no directed cycles).
    - Ex 3. Bellman-Ford algorithm (no negative cycles).


## Dijkstra's algorithm

 - Consider vertices in increasing order of distance from s ( vertex that not on the SP-tree and  with the lowest distTo[] value).
    - so , our source is 0 in the case showed as pic below, what vertices are closest to the source ?  0-1, 5.0
 - Add vertex to tree and relax all edges pointing from that vertex.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_sp_dijkstra_0.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_sp_dijkstra_1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_sp_dijkstra_2.png)


### Dijkstra's algorithm: correctness proof (TODO)

### Dijkstra's algorithm: Java implementation

```java
public class DijkstraSP {
   private DirectedEdge[] edgeTo;
   private double[] distTo;
   private IndexMinPQ<Double> pq;

   public DijkstraSP(EdgeWeightedDigraph G, int s) {
       edgeTo = new DirectedEdge[G.V()];
       distTo = new double[G.V()];
       pq = new IndexMinPQ<Double>(G.V());
       for (int v = 0; v < G.V(); v++)
           distTo[v] = Double.POSITIVE_INFINITY;
       distTo[s] = 0.0;

       pq.insert(s, 0.0);
       // relax vertices in order of distance from s
       while (!pq.isEmpty())
       {
           int v = pq.delMin();
           for (DirectedEdge e : G.adj(v))
               relax(e);
       }
   }
   private void relax(DirectedEdge e) {
       int v = e.from(), w = e.to();
       if (distTo[w] > distTo[v] + e.weight()) {
           distTo[w] = distTo[v] + e.weight();
           edgeTo[w] = e;
           // update PQ
           if (pq.contains(w)) pq.decreaseKey(w, distTo[w]);
           else                pq.insert     (w, distTo[w]);
       }    
   }
}
```


### Computing spanning trees in graphs

 - Dijkstra’s algorithm seem familiar?
    - Prim’s algorithm is essentially the same algorithm.
    - Both are in a family of algorithms that compute a graph’s spanning tree
 - Main distinction: Rule used to choose next vertex for the tree.
    - Prim’s: Closest vertex to the **tree** (via an undirected edge).
    - Dijkstra’s: Closest vertex to the **source** (via a directed path).
 - Note: DFS and BFS are also in this family of algorithms.

## edge-weighted DAGs

### Acyclic edge-weighted digraphs

 - Q. Suppose that an edge-weighted digraph has no directed cycles. Is it easier to find shortest paths than in a general digraph?
 - A. Yes!

---

 - Algorithm
    - Consider vertices in topological order.
    - Relax all edges pointing from that vertex.

### Shortest paths in edge-weighted DAGs

 - Proposition. Topological sort algorithm computes SPT in any edge- weighted DAG in time proportional to *E + V* .
 - Proof
    - TODO


```java
public class AcyclicSP {
   private DirectedEdge[] edgeTo;
   private double[] distTo;

   public DijkstraSP(EdgeWeightedDigraph G, int s) {
       edgeTo = new DirectedEdge[G.V()];
       distTo = new double[G.V()];

       for (int v = 0; v < G.V(); v++)
           distTo[v] = Double.POSITIVE_INFINITY;
       distTo[s] = 0.0;

       // new : topological order
       Topological topological = new Topological(G);
       for (int v : topological.order())
           for (DirectedEdge e : G.adj(v))
               relax(e);
   }
   private void relax(DirectedEdge e) {
       int v = e.from(), w = e.to();
       if (distTo[w] > distTo[v] + e.weight()) {
           distTo[w] = distTo[v] + e.weight();
           edgeTo[w] = e;
           // update PQ
           if (pq.contains(w)) pq.decreaseKey(w, distTo[w]);
           else                pq.insert     (w, distTo[w]);
       }    
   }
}
```

### Content-aware resizing

 - Seam carving: [Avidan and Shamir] Resize an image without distortion for display on cell phones and web browsers.





