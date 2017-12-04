# CS61A sp17

# Lecture #22: The Scheme Language

## Data Types

 - **atoms**
    - The classical atoms:
        - Numbers: integer, floating-point, complex, rational.
        - Symbols.
        - Booleans: `#t`, `#f`.
        - The empty list: `()`
        - Procedures (functions).
    - Some newer-fangled, mutable atoms:
        - Vectors: Python lists.
        - Strings
        - Characters: Like Python 1-element strings
 - **pairs**
    - Pairs are like **two-element** Python lists , where the elements are (recursively) Scheme values.

## Symbol notion

 - Lisp最早是被设计来处理符号数据(如公式)。这些符号通常递归的被定义( an exp = op + subexps ). 
 - the notion of a symbol:
    - Essentially a constant string
    - Two symbols with the same “spelling” (string) are by default the same object (but usually, case is ignored).
 - The main operation on symbols is **equality**.
    - e.g. `a bumblebee numb3rs * + / wide-ranging !?@*!!`

## Pairs and Lists

 - The Scheme notation for the pair
    - (V1 . V2)
 - Lists are so prevalent that there is a standard abbreviation:

Abbreviation | Means
--- | ---
(V )  | (V . ())
(V1 V2 · · · Vn) | (V1 . (V2 . (· · · (Vn . ()))))
(V1 V2 · · · Vn−1 . Vn) | (V1 . (V2 . (· · · (Vn−1 . Vn))))

 - one can build practically any data structure out of pair
    - In Scheme, the main one is the (linked) list
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/scheme_linklist.png)

## Programs

 - Scheme expressions and programs are **instances of Lisp data structures**  (“Scheme programs are Scheme data”).
 - At the bottom, numerals, booleans, characters, and strings are expressions that stand for themselves.
 - Most lists (aka forms) stand for function calls:
    - `(OP E1 · · · En)`

## Quotation

 - Since programs are data, we have a problem:
    - How do we say, eg., “Set the variable x to the three-element list (+ 1 2)” 
    - without it meaning “Set the variable x to the value 3?”
 - In English, we call this a **use vs. mention distinction**
 - For this, we need a special form -- a construct that does **not** simply evaluate its operands.
 - `(quote E)` yields E itself as the value, without evaluating it as a Scheme expression:
    - `(quote (+ 1 2))` =>  `(+ 1 2) `
 - 简化版本 `'(xxx)'`

## Special Forms
 
 - `(quote E)` is a sample of **special form** : an exception to the general rule for evaluting functional forms
 - A few other special forms also have meanings that generally do not involve simply evaluating their operands:
    - `(if (> x y) x y) ; like python A if X else B`
    - `(and (integer?) (> x y) (< x z)) ; like python and `  
    - `(or (not (integer? x)) (< x L) (> x U)) ; Like Python ’or’`
    - `(lambda (x y) (/ (* x x) y)) ; Like Python lambda , yields function`
    - `(define pi 3.14159265359) ; Definition`
    - `(define (f x) (* x x)) ; Function Definition`
    - `(set! x 3) ; Assignment ("set bang")`

## Traditional Conditionals

 - the fancy traditional Lisp conditional form: `cond`
    - cond: chains a series of tests to select a result

```scheme
scm> (define x 5)
scm> (cond ((< x 1) ’small)
        ((< x 3) ’medium)
        ((< x 5) ’large)
        (#t ’big))
big
```

 - which is the Lisp version of Python’s 

```python
"small" if x < 1 else "medium" if x < 3 else "large" if x < 5 else "big"
```

## Symbols

 - When evaluated as a program, a symbol acts like a variable name.
 - Variables are bound in environments, just as in Python, although the syntax differs.
 - To define a new symbol, either use it as a parameter name (later), or use the “define” special form:
    - This (re)defines the symbols in the current environment.

```python
(define pi 3.1415926)
(define pi**2 (* pi pi))
```

 - To assign a new value to an existing binding, use the **set!** special form:
    - `(set! pi 3)`
    - pi must be defined (not like Python).

## Function Evaluation

 - Function evaluation is just like Python
 - To create a new function, we use the **lambda** special form:

```scheme
scm> ( (lambda (x y) (+ (* x x) (* y y))) 3 4)
25
scm> (define fib
        (lambda (n) (if (< n 2) n (+ (fib (- n 2)) (fib (- n 1))))))
scm> (fib 5)
5
```

 - 把一个lambda 赋给一个 symbol 太常见了，这么写略繁琐

```scheme
scm> (define (fib n)
    (if (< n 2) n (+ (fib (- n 2)) (fib (- n 1)))))
```

## Numbers

```scheme
scm> (/ 5 2)
2.5
scm> (quotient 5 2) 
2
scm> (< 2 4 8)  ; chain compare like python
#t
(integer? 5)
#t
```

## Lists and Pair

 - Pairs (and therefore lists) have a basic constructor and accessors
    - cons : constructor
    - car : **C**ontents of the **A**ddress part of **R**egister number
    - cdr : **C**ontents of the **D**ecrement part of **R**egister number,
    - cpr : Contents of the Prefix part of Register number
    - ctr : Contents of the Tag part of Register number
    - cadr :
    - cadar : ... 
 - between the first letter ('c') and the last ('r'),
    - a 'a' means "the car of" and a 'd' means "the cdr of".
    - so
        - cadr is "the car of the cdr",
        - cddr is the cdr of the cdr,
        - cadar is the "car of the cdr of the car" (thus the parameter has to be a list of list),



```scheme
scm> (cons 1 2)
(1 . 2)
scm> (cons 'a (cons 'b '()))
(a b)
scm> (define L (a b c)) ; define won'e evaluate oprands
scm> (car L)
a
scm> (cdr L)
(b c)
(cadr L) ; (car (cdr L))
b
scm> (cdddr L) ; (cdr (cdr (cdr L)))
()
```

 - And one that is especially for lists:

```scheme
scm> (list (+ 1 2) 'a 4)
(3 a 4)
```

## Binding Constructs: Let

 - Sometimes, you’d like to introduce local variables or named constants
 - The let special form does this:

```scheme
scm> (define x 17)
scm> (let ((x 5)
        (y (+ x 2)))
        (+ x y))
24
```

 - This is a derived form, equivalent to:
    - 想象 let 是在给你定义参数

```scheme
scm> ((lambda (x y) (+ x y)) 5 (+ x 2))
```

 - TODO, 为什么 最后加法x 的值是17 ？

## Loops and Tail Recursion

 - In Scheme, **tail-recursive functions must work like iterations**
 - 一般可以通过增加一个 helper function 来实现 tail-recursive

---

# Lecture #23: Programming Languages and Programs

## Metalinguistic Abstraction

 - We’ve created abstractions of actions
    - functions, and of things , classes
 - **Metalinguistic abstraction** refers to the creation of languages
    - abstracting **description**. 
    - Programming languages are one example

## A Sample Language: Calculator

 - Prefix notation expression language for basic arithmetic Python-like syntax, with more flexible built-in functions.

```python
calc> add( 1, 2, 3, 4)
10
calc> mul() 1
calc> sub(100, mul( 7, add( 8, div(-12, - 3))))
16.0
calc> -(100, *( 7, +( 8, /(-12, - 3))))
16.0
```






