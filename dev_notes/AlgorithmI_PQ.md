...menustart

 - [2.4 PRIORITY QUEUES](#31a8f3f664a49f0116e7d7ceacaff56c)
     - [binary heaps](#01f70acef6efe0e1e07b6c8847ae493a)
         - [Complete binary tree](#45c2a6499668ae8a669f5f812b56379a)
         - [Binary heap representations](#05a360d5d6f9939aabfd6bd00823d80e)
         - [Binary heap properties](#2e582e415db1ab1e6e72b8278b9385e1)
         - [Promotion in a heap](#8bff03ac1b55987683317d94044219d1)
         - [Insertion in a heap](#cb0565d93960f3556f5f0ca7c24c3134)
         - [Demotion in a heap](#32a8207179f9f552bbec38561312becf)
         - [Delete the maximum in a heap](#34f42d75083165489f2d1288aa203637)
         - [Priority queues implementation cost summary](#dee2139d14dc9b4129086c422806e8a4)
         - [Binary heap considerations](#08fdfb23883b137987adc5a563f835b0)
     - [event-driven simulation](#2b3a9baf85c09205eff605615163f824)

...menuend


<h2 id="31a8f3f664a49f0116e7d7ceacaff56c"></h2>


# 2.4 PRIORITY QUEUES

<h2 id="01f70acef6efe0e1e07b6c8847ae493a"></h2>


## binary heaps

<h2 id="45c2a6499668ae8a669f5f812b56379a"></h2>


### Complete binary tree

 - Binary tree. Empty or node with links to left and right binary trees.
 - Complete tree. Perfectly balanced, except for bottom level.

<h2 id="05a360d5d6f9939aabfd6bd00823d80e"></h2>


### Binary heap representations

 - Binary heap. Array representation of a heap-ordered complete binary tree.
 - Heap-ordered binary tree.
    - Keys in nodes
    - Parent's key no smaller than children's key
 - Array representation.
    - Indices start at 1.
    - Take nodes in **level** order
    - No explicit links needed !

![](../imgs/algor1_pq_heap_repre.png)

<h2 id="2e582e415db1ab1e6e72b8278b9385e1"></h2>


### Binary heap properties

 - Proposition. Largest key is a[1], which is root of binary tree.
 - Proposition. Can use array indices to move through tree.
    - Parent of node at k is at k/2.
    - Children of node at k are at 2k and 2k+1.
    - a[0] 不使用


<h2 id="8bff03ac1b55987683317d94044219d1"></h2>


### Promotion in a heap

 - Scenario. Child's key becomes **larger** key than its parent's key.
 - To eliminate the violation:
    - Exchange key in child with key in parent.
    - Repeat until heap order restored.

![](../imgs/algorI_pq_swim.png)

```java
private void swim(int k) {
    // 1 is root, do not care
    // parent is smaller 
    while (k > 1 && less(k/2, k)) {
        exch(k, k/2); // swap key
        k = k/2;     // check the new violation of the upper level
    }    
}
```

 - Peter principle. Node promoted to level of incompetence.
 - swim/sink 都需要递归检查
    - swim 用于 insertion
    - sink 用于 delete max

<h2 id="cb0565d93960f3556f5f0ca7c24c3134"></h2>


### Insertion in a heap

 - Insert. Add node at end, then swim it up.
    - 添加新node到PQ最后，然后 swim到正确位置
 - Cost. At most 1 + lg N compares.

![](../imgs/algorI_pq_insertion.png)

```java
public void insert(Key x) {
    // ++ first , because we don't use index 0
    pq[++N] = x;
    // swim up
    swim(N); 
}
```

<h2 id="32a8207179f9f552bbec38561312becf"></h2>


### Demotion in a heap

 - Scenario. Parent's key becomes **smaller** than one (or both) of its children's.
 - To eliminate the violation:
    - Exchange key in parent with key in larger child. 
        - why not the smaller one ? Power struggle. Better subordinate promoted
    - Repeat until heap order restored.
 
![](../imgs/algorI_pq_sink.png)

```java
private void sink(int k) {
    while (2*k <= N) {
        int j = 2*k;
        // child node at k are 2k,2k+1 
        // choose the largest child as j
        if (j < N && less(j, j+1)) j++;
        if (!less(k, j)) break;
        exch(k, j);
        k = j;    
    }    
}
```


<h2 id="34f42d75083165489f2d1288aa203637"></h2>


### Delete the maximum in a heap

 - Delete max.
    - Exchange root with node at end, then sink it down.
    - 交换根节点 到最后一个节点， 然后新的根节点 sink 到正确位置
 - Cost. At most 2 lg N compares.

![](../imgs/algorI_pq_deletemax.png)

```java
public Key delMax() {
    Key max = pq[1];
    // 交换，N = N-1
    exch(1, N--);
    // new root sink
    sink(1);
    // prevent loitering
    pq[N+1] = null ;
    return max;    
}
```

<h2 id="dee2139d14dc9b4129086c422806e8a4"></h2>


### Priority queues implementation cost summary

 - order-of-growth of running time for priority queue with N items

implementation | insert | del max | max 
--- | --- | --- | --- 
unordered array | 1 | N | N
ordered array | N | 1 | 1
**binary heap** | log N | log N | 1
d-ary heap | logd N | d logd N | 1 
Fibonacci | 1 | log N⁺ | 1 

<h2 id="08fdfb23883b137987adc5a563f835b0"></h2>


### Binary heap considerations

 - Immutability of keys
 - Underflow and overflow
    - Underflow: throw exception if deleting from empty PQ
    - Overflow: add no-arg constructor and use resizing array
 - Minimum-oriented priority queue
    - Replace less() with greater()
    - Implement greater().
 - Other operations.
    - Remove an arbitrary item
    - Change the priority of an item
    - can implement with sink() and swim() [stay tuned]
    

 - resize array
    - grow : If array is full, create a new array of twice the size, and copy items
        - `if (N == s.length) resize(2 * s.length);`
    - sink: halve size of array s[] when array is one-quarter full.
        - `if (N > 0 && N == s.length/4) resize(s.length/2);`

```java
private void resize(int capacity) {
   String[] copy = new String[capacity];
   for (int i = 0; i < N; i++)
      copy[i] = s[i];
   s = copy;
}
```



<h2 id="2b3a9baf85c09205eff605615163f824"></h2>


## event-driven simulation


