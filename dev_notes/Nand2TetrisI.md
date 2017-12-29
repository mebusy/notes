
# Week1 

## Introduction

### 0.0 Introduction

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_layers.png)

 - book: `<<The Elements of Computing System>>`

 - N2T , toolsuit
    - http://nand2tetris.org/software.php


## Boolean Functions and Gate Logic

### 1.2 Boolean Function Synthesis

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_truth_tab_2_bool_expr.png)

 - Truth Table to Boolean Expression ?
    - constructing a disjuctive normal form formula  构建一个分离的范式公式 
 - how
    1. go row by row in the truth table, focus only on the rows have a value(f) 1 
        - for example , the 1st row
    2. 写一个 范式，to get a value of 1 only at this row
        - that is， 只有 这一行 会得到 1， 其它都是 0
        - i.e. `( NOT(x) AND NOT(y) and NOT(z) )`
    3. do same operation on other row that have value 1
        - 3th :
            - `( NOT(x) AND y AND NOT(z) )` 
        - 5th :
            - `( x AND NOT(y) AND NOT(z)  )`
    4. 剩下的，就是把 这三个 范式， 用 OR 连接起来
 - 很长的范式，我们怎么能得到一个 最小范式呢？ 
    - In fact, this is an NP-hard problem.  

 - Theorem
    - Any Boolean function can be represented using an expression containing AND, OR and NOT operations.
    - Any Boolean function can be represented using an expression containing AND, NOT operations.
    - 还能更少吗？
 - There is yet another operation that by itself does suffice to actually compute everything -- the NADN function

x | y | NAND 
--- | --- | --- 
0 | 0 | 1
0 | 1 | 1 
1 | 0 | 1
1 | 1 | 0

 - `(x NAND y) == NOT(x AND y) `
 - 妙处在哪里？
    - NAND(x,x) == NOT(x)  ! 
 - **Any Boolean function can be represented using an expression containin only NAND operation.**
    1. NOT(x) == (x NAND x)
        - 现在你已经有NOT了！
    2. (x AND y) = NOT( x NAND y )

### 1.3 Logic Gates

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_gate_interface.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_gate_implementation.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_circuit_impl.png)







