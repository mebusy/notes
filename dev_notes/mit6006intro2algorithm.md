
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

