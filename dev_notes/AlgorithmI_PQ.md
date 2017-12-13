

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

### Insertion in a heap

 - Insert. Add node at end, then swim it up.
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


