...menustart

- [Discrete Mathematics](#d2bcb78d5ac194c66f434e9fbcb3565e)
- [Chapter 1 Foundations of Logic](#1528d69d906941f195dbd4052b705454)
    - [1.1 Proposition Logic](#57af49f5272c485d0fbc802a05d36c22)
        - [The Implication Operator →](#8e71db7c81436b5c108940a9a5712cb2)
        - [Biconditional](#cba739368677d1686f6fbbfc3ef64e88)
    - [1.2 Proposition Equivalences](#aa8d3b3a207fde866ac608d5c61a3f3f)
    - [1.3 Predicates and Quantifiers](#964abe8e7ce3c7be1d9658b6dd67544f)
    - [1.4 Nested Quantifiers](#a38483049b36c18171570ccafddb3158)

...menuend


<h2 id="d2bcb78d5ac194c66f434e9fbcb3565e"></h2>


# Discrete Mathematics

<h2 id="1528d69d906941f195dbd4052b705454"></h2>


# Chapter 1 Foundations of Logic

<h2 id="57af49f5272c485d0fbc802a05d36c22"></h2>


## 1.1 Proposition Logic

<h2 id="8e71db7c81436b5c108940a9a5712cb2"></h2>


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

    - use `sympy`
        - let p : A is a knight
        - let q : B is a kinght 

```
>>> from sympy.logic.inference import satisfiable
>>> from sympy import Symbol
>>> p, q = symbols( 'p,q' )
>>> satisfiable( (p >> q & q >> ~p ) & ( ~p >> ~q & ~q >> ~p ) )
{p:False,q:False}
```

<h2 id="cba739368677d1686f6fbbfc3ef64e88"></h2>


### Biconditional

- `p<->q`
    - `p<->q` means **¬(p⊕q)**    // 异或




<h2 id="aa8d3b3a207fde866ac608d5c61a3f3f"></h2>


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
    - `p<->q ⇔ (p->q)^(q->p)`
    - `p<->q ⇔ (p^q)V(¬p^¬q)`
        - ⇔ ¬(p⊕q)  // ⊕ means 异或
    - `p<->q ⇔ ¬p<->¬q`

    


<h2 id="964abe8e7ce3c7be1d9658b6dd67544f"></h2>


## 1.3 Predicates and Quantifiers

- Predicate logic
    - 谓词逻辑是命题逻辑(proposition logic)的扩展，允许对整个实体类进行简明推理。
        - 命题逻辑将简单命题（句子）视为原子实体。
        - 谓词逻辑将句子的主语与其谓词区分开来
    - i.e. P(x) = "x is a girl."
    - P 是一个命题函数。 P(x) 是P在x 点上的值,是一个命题
- ∀,∃ 的 De Morgan law
    - ¬∀<sub>x</sub> P(x) ≡ ∃<sub>x</sub> ¬P(x)
    - ¬∃<sub>x</sub> P(x) ≡ ∀<sub>x</sub> ¬P(x)

<h2 id="a38483049b36c18171570ccafddb3158"></h2>


## 1.4 Nested Quantifiers

