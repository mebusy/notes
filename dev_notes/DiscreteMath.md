
# Discrete Mathematics

# Chapter 1 Foundations of Logic

## 1.1 Proposition Logic

### The Implication Operator →

 - p → q
    - p → q does not say that p causes q!
    - p → q does not require that p or q are ever true! 
 - English Phrases Meaning  p → q   
    - p implies q
    - if p ,then q
    - if p, q  
        - q if p
    - when p, q
        - q when p
    - whenever p, q
        - q whenever p
    - p only if q 
    - p is sufficient for q 
    - q is necessary for p
    - q follows from p
    - q is implied by p
 - 从集合的角度考虑
    - 1 p→q 叫蕴含式，因为 p 蕴含于 q，即 p 是 q 的子集 
        - 比如 p“A能被4整除”，q“A能被2整除”，p 是 q 的真子集
        - 则 p->q 描述出来就是“A若能被4整除，就能被2整除”，或者“A只有能被2整除，才能被4整除”，这显然是对的
    - 2 当 p 假，就是空集，空集是任何集合的子集，所以 p=0 时不管 q 是啥，蕴含式都对；
    - 3 当 p 真 q 假，就是 q 作为空集却有个非空子集，这显然不对
    - 以上是 p q 有内在联系的情况，可以推广到它们无联系
 - example 1
    - you can access the internet from campus only if you are a computer science major or you are not a freshman.
        - p = you can access the internet from the campus
        - q = you are a computer science major
        - r = you are a freshman
    - p → q V ¬r
 - example 2
    - You cannot ride the roller coaster if you are under 4 feet tall **unless** you are older than 16 years old.
        - q = you can ride ...
        - r = you are under 4 feet ...
        - s = you are older than 16 ...
     - r ^ ¬s → ¬q

 - Logic Puzzles
    - There are 2 kinds of inhabitants in an island, knights and knaves. Kinghts always tell the truth, and knaves always lie.
        - A: B is a knight
        - B: Both of them are opposite types.
        - which kind of A and B ?
    - sol: 列举法
        - 1 assume A is a knight  => B is a knight => "Both of them are opposite types" 是真话 , 和假设相悖
        - 2 assume A is a knave => B is a knave => "Both of them are opposite types" 是假话，  符合假设 => A and B are both knaves.

### Biconditional

 - p<->q
    - p<->q means **¬(p⊕q)**    // 异或




## 1.2 Proposition Equivalences

 - Equivalence Laws
    - Commutative 交换律
    - Associative 结合律
    - Distributive 分配律
        - pV(q^r)⇔ (pVq)^(pVr)
        - p^(qVr)⇔ (p^q)V(p^r)
    - De Morganís
        - ¬(p^q)⇔ ¬pV¬q
        - ¬(pVq)⇔ ¬p^¬q
 - 最重要的两条 蕴含式相关的逻辑等价
    - p->q ⇔ ¬q->¬p
    - p->q ⇔ ¬pVq
        - p^¬q ⇔ ¬(p->q) 
 - Biconditional
    - p<->q ⇔ (p->q)^(q->p)
    - p<->q ⇔ (p^q)V(¬p^¬q)
        - ⇔ ¬(p⊕q)  // ⊕ means 异或
    - p<->q ⇔ ¬p<->¬q

    


## 1.3 Predicates and Quantifiers

## 1.4 Nested Quantifiers

