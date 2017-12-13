

# 2.4 PRIORITY QUEUES

## binary heaps

### Complete binary tree

 - Binary tree. Empty or node with links to left and right binary trees.
 - Complete tree. Perfectly balanced, except for bottom level.

### Binary heap representations

 - Binary heap. Array representation of a heap-ordered complete binary tree.
 - Heap-ordered binary tree.
    - Keys in nodes
    - Parent's key no smaller than children's key
 - Array representation.
    - Indices start at 1.
    - Take nodes in **level** order
    - No explicit links needed !

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algor1_pq_heap_repre.png)

### Binary heap properties

 - Proposition. Largest key is a[1], which is root of binary tree.
 - Proposition. Can use array indices to move through tree.
    - Parent of node at k is at k/2.
    - Children of node at k are at 2k and 2k+1.
    - a[0] 不使用


### Promotion in a heap

 - Scenario. Child's key becomes **larger** key than its parent's key.
 - To eliminate the violation:
    - Exchange key in child with key in parent.
    - Repeat until heap order restored.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_swim.png)

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

### Insertion in a heap

 - Insert. Add node at end, then swim it up.
    - 添加新node到PQ最后，然后 swim到正确位置
 - Cost. At most 1 + lg N compares.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_insertion.png)

```java
public void insert(Key x) {
    // ++ first , because we don't use index 0
    pq[++N] = x;
    // swim up
    swim(N); 
}
```

### Demotion in a heap

 - Scenario. Parent's key becomes **smaller** than one (or both) of its children's.
 - To eliminate the violation:
    - Exchange key in parent with key in larger child. 
        - why not the smaller one ? Power struggle. Better subordinate promoted
    - Repeat until heap order restored.
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_sink.png)

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


### Delete the maximum in a heap

 - Delete max.
    - Exchange root with node at end, then sink it down.
    - 交换根节点 到最后一个节点， 然后新的根节点 sink 到正确位置
 - Cost. At most 2 lg N compares.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_deletemax.png)

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

### Priority queues implementation cost summary

 - order-of-growth of running time for priority queue with N items

implementation | insert | del max | max 
--- | --- | --- 
unordered array | 1 | N | N
ordered array | N | 1 | 1
**binary heap** | log N | log N | 1
d-ary heap | logd N | d logd N | 1 
Fibonacci | 1 | log N⁺ | 1 

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



## event-driven simulation


