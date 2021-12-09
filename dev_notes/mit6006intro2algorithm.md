
# MIT 6.006 Notes

## 2. Data Structures and Dynamic Arrays


Data Structure | \| | Operation, <br>Worst Case O(·)  | &nbsp; |  &nbsp;
--- | :--- | --- | --- | --- 
&nbsp; | Static | Dynamic | Dynamic | Dynamic
&nbsp; | get_at(i)<br>set_at(i,x) | insert_first(x)<br>delete_first()| insert_last(x)<br>delete_last() | insert_at(i,x)<br>delete_at(i)
Array | ***1*** | n | n | n
Linked List | n | ***1*** | n | n 
Dynamic Array | ***1*** | n | ***1***<sub>(a)</sub> | n




- linked lists are great if you're working on the ends, even dynamically.
- (static) arrays are great if you're doing random access and nothing dynamic, nothing adding or deleting.
- dynamic arrays get all of the good running times of linked lists and all of the good running times of static arrays.
    - we won't get quite all of them, but most of them. 


### Dynamic Arrays ( Python lists )

```cpp
| A  | ---> |x₀|x₁|x₂|...|...|...| 
|len |    // length of array, # of items
|size|    // actual memory allocated
```

- relax constraint size (array) = n (# of items in sequence)
    - with a static array, we allocated an array of size exactly n. 
    - Let's relax that.  Let's not make it exactly n.
- enforce size = Θ(n) ≥ n, e.g. 2n
- maintain A[i] = x<sub>i</sub>
- re-size to 2n if not enough space
    - think about `n insert_last()` from an array of size 1, when do we resize ?
        - we can insert 1 item for free, as soon as we insert the 2nd item, then we have to resize(2).
        - the we insert the 3rd item,  we need resize(4) at first ...
    - we're going to resize at n equals 1,2,4,8,..., all the power of 2
        - ⇒ resize cost: Θ(1+2+4+8+...)
        - = Θ( ∑<sub>i=0</sub><sup>lgn</sup> 2<sup>i</sup> )
            - this is a geometric series & geometric series are dominated by the last term, the biggest term.
            - then in terms of Θ notation, you can just look at the last term and put a Θ around it, and you done
        - = Θ( 2<sup>lgn</sup> ) = Θ(n)
            - it's linear time, cool.
            - I'm doing n operations here, and I spent linear total time to do all of the resizing. That's like constant each, **kind of**.
        - the *kind of* is an important notion,  which we call **amortization**.
            - **amortization**: operation takes T(n) amortized time  if any k operations take ≤ kT(n) time
            - *amortized* means a particular kind of averaging over the sequence of operations


## 3. Sets

Data Structure | \| | Operation, O(·)  | &nbsp; |  &nbsp; |  &nbsp;
--- | :--- | --- | --- | --- | ---
&nbsp; | Container | Static | Dynamic | Order | &nbsp;
&nbsp; | build(X) | find(k) | insert(x)<br>delete() | find_min()<br>find_max() | find_prev(k)<br>find_next(k)
**Array** | n | n | n | n | n
**Sorted Array** | nlogn | logn | n | ***1*** | logn



## 4. Hashing

Data Structure | \| | Operation, O(·)  | &nbsp; |  &nbsp; |  &nbsp;
--- | :--- | --- | --- | --- | ---
&nbsp; | Container | Static | Dynamic | Order | &nbsp;
&nbsp; | build(X) | find(k) | insert(x)<br>delete() | find_min()<br>find_max() | find_prev(k)<br>find_next(k)
Array | n | n | n | n | n
Sorted Array | nlogn | logn | n | ***1*** | logn
**Direct Access Array** | u | ***1*** | ***1*** | u | u 

> u: the size of memory that the largest key is allowed to store.


- Can I do `find(k)` faster than O(lgn) ?
    - No. We can't do faster than O(lgn) for `find()`, which is a little weird.
        - the items that I'm storing in this data structure, for any way I saw these things, any algorithm of this certain type is going to require at least logarithmic time.
        - comparison model:  means the objects I'm storing, I can kind of think of them as black boxes. I don't get to touch tehse things, except the only way that I can distinguish between them is given a key and an item, or two items I can do a comparison on those keys, same?bigger?or smaller.
        - an algorithm in the comparison model is decision tree. This is eventually has n+1 leaves, n items and 1 `none`, which may represent the output. And the complexity of that algorithm is O(lgn) because this decision tree is binary tree, 
    - Yes. If the keys are numbers , we can use Direct Access Array.
        - i.e., if the key is 10, we store the data in 10th location in the Direct Access Array.
        - Θ(1) to find(k). 
        - how about inserting and deleting ? Θ(1) , BUT...
        - but we don't know how hight the numbers to. We have a problem of memory capacity.

