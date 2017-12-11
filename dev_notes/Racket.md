
# Racket

## Curring

 - Currying is an idiom that works in any language with closures
 - Currying is when you break down a function that takes multiple arguments into a series of functions that take part of the arguments.
 - It is a transformation that can be applied to functions to allow them to take one less argument than previously.
 - Here's an example in JavaScript:


```
function add (a, b) {
  return a + b;
}

add(3, 4); returns 7

function add (a) {
  return function (b) {
    return a + b;
  }
}

add(3)(4);
var add3 = add(3);
add3(4);
```

 - Less common in Racket because it has real multiple args

```scheme
(define pow
    (lambda (x)
        (lambda (y)
            (if (= y 0)
                1
                (* x ((pow x) (- y 1)))))))

(define three-to-the (pow 3))
(define eightyone (three-to-the 4))
(define sixteen ((pow 2) 4))

; Sugar for defining curried functions: 
(define ((pow x) y) (if ... ) )
```

## Local bindings

Racket has 4 ways to define local variables. If any will work, use `let`

 - let
    - can bind any number of local variables 
    - The expressions are all evaluated in the environment from **before the let-expression**
        - means won't use the definition in `let` statement
    - Convenient for things like `(let ([x y][y x]) …)`
    - in the following example , the local variable x will take the parameter x then +3 , the local variable y **also take the parameter x then +2**

```scheme
(define (silly-double x)
    (let ([x (+ x 3)]
          [y (+ x 2)])
      (+ x y -5)))
```

 - let\*
    - The expressions are evaluated in the environment produced from the **previous bindings**
        - means it will also use the definition in `let` statement ( the earlier ones )

```shceme
(define (silly-double x)
    (let* ([x (+ x 3)]
           [y (+ x 2)])
       (+ x y -8)))
```

 - letrec
    - The expressions are evaluated in the environment that includes **all the bindings**
        - means it will also use the definition in `let` statement , not only the earlier ones but also the later ones.
    - Needed for mutual recursion 
        - f calls g, g calls f
        - only ues `letrec` when you have to execute mutual recursion   
    - because expressions are still evaluated in order , it may lead to some implicite bugs
        - if you change the `y` definition in `silly-triple` as `[y (+ w 2)]` , it will raise an exception when you call it.


```shceme
(define (silly-triple x)
    (letrec ([y (+ x 2)]
             [f (lambda(z) (+ z y w x))] ; used w
             [w (+ x 7)])
       (f -9)))
 
; Letrec is ideal for recursion
(define (silly-mod2 x)
 (letrec
  ([even? (lambda (x)(if (zero? x) #t (odd? (- x 1))))]
   [odd?  (lambda (x)(if (zero? x) #f (even? (- x 1))))])
  (if (even? x) 0 1)))
```

 - define
    - In certain positions, like the beginning of function bodies, you can put defines
        - For defining local variables, same semantics as `letrec` 

```scheme
(define (silly-mod2 x)
    (define (even? x)(if (zero? x) #t (odd? (- x 1))))
    (define (odd? x) (if (zero? x) #f (even?(- x 1))))
    (if (even? x) 0 1))
```

## Top-Level Bindings

 - The bindings in a file work like local defines, i.e., `letrec`
    - can refer to earlier or later bindings
    - But refer to later bindings only in function bodies 
        - Because bindings are evaluated in order
    - cannot define the same variable twice in module
 - Racket has a module system
    - Each file is implicitly a module , Not really “top-level” 
    - A module can shadow bindings from other modules it uses
        - Including Racket standard library
    - So we could redefine `+` or any other function


### REPL
 
Unfortunate detail: 

 - REPL works slightly differently
    - Not quite `let*` or `letrec`
 - Best to avoid recursive function definitions or forward references in REPL

## Mutation With set!

 - Racket really has assignment statements
    - But used only-when-really-appropriate!
    - people generally programming a Racket do not use them a lot. 
    - `(set! x e)`
 - Once you have side-effects, sequences are useful:
    - `(begin e1 e2 ... en)`
 - Mutating top-level definitions is particularly problematic
    - What if any code could do set! on anything?
    - – How could we defend against this?
 - A general principle: 
    - If something you need not to change might change, make a local copy of it. 
    - Example:

```scheme
(define b 3)
   (define f
     (let ([b b])
      (lambda (x) (* 1 (+ x b)))))
```

 - what if some code redefine `* +` ?
    - in scheme , it is a problem
    - but in Racket , it may not be a problem
        - Each file is a module
        - If a module does not use set! on a top-level variable, then Racket makes it constant and forbids set! outside the module

## The Truth About Cons

 - cons just makes a pair
    - Often called a cons cell
    - By convention and standard library, lists are nested pairs that eventually end with null

```scheme
; this is not a list !
(define pr (cons 1 (cons #t "hi"))) ; '(1 #t . "hi")

(define lst (cons 1 (cons #t (cons "hi" null))))
```

 - Passing an improper list to functions like length is a run-time error
 - So why allow improper lists?
    - Pairs are usefu

## mcons For Mutable Pairs

 - What if you wanted to mutate the contents of a cons cell?
    - In Racket you cannot (major change from Scheme)
        - scheme has `set-car!`
    - This is good
        - List-aliasing irrelevant
        - Implementation can make list? fast since listness is determined when cons cell is created
 - Since mutable pairs are sometimes useful , Racket provides them too:
    - mcons
    - mcar
    - mcdr
    - mpair?
    - set-mcar!
    - set-mcdr!

## Delayed Evaluation and Thunks

 - Thunks delay 
    - A zero-argument function used to delay evaluation is called a thunk
    - As a verb: thunk the expression

```scheme
1 
; after thunk
(lambda() 1)
```

## Delay and Force

 - Assuming some expensive computation has no side effects, ideally we would:
    - Not compute it until needed
    - Remember the answer so future uses complete immediately Called **lazy evaluation**
 - An ADT represented by a mutable pair

```scheme
(define (my-delay th)
     (mcons #f th))
(define (my-force p)
    (if (mcar p)
         (mcdr p)
         (begin (set-mcar! p #t)
             (set-mcdr! p ((mcdr p)))
             (mcdr p))))
```

 - Using **promises**

```scheme
(define (f p)
    (… (if (…) 0 (… (my-force p) …))
       (if (…) 0 (… (my-force p) …))
       …
       (if (…) 0 (… (my-force p) …))))

(f (my-delay (lambda () e)))
```


## Using Streams

 - A stream is an infinite sequence of values
    - So cannot make a stream by making all the values
    - Key idea: Use a thunk to delay creating most of the sequence
    - Just a programming idiom
 - A powerful concept for division of labor
    - Stream producer knows how create any number of values
    - Stream consumer decides how many values to ask for
 - We will represent streams using pairs and thunks
 - Let a stream be a thunk that when called returns a pair:
    - `'(next-answer . next-thunk)`
    - 注意和 iterator的区别
 - So given a stream s, the client can get any number of elements

```scheme
– First: (car (s))
– Second: (car ((cdr (s))))  ; double (( on cdr 
– Third: (car ((cdr ((cdr (s))))))
```

 - How can one thunk create the right next thunk? Recursion!
    - Make a thunk that produces a pair where cdr is next thunk
    - A recursive function can return a thunk where recursive call does not happen until thunk is called
 
```scheme
(define ones (lambda () (cons 1 ones))) ; 1,1,1 ...

(define nats                        ; 1,2,3,...
 (letrec ([f (lambda (x) (cons x (lambda () (f (+ x 1)))))])
     (lambda () (f 1))
 )
)

(define powers-of-two   ; 2,4,8,...
 (letrec ([f (lambda (x) (cons x (lambda () (f (* x 2)))))])
     (lambda () (f 2))
 )
)
```

### Getting it wrong

 - This goes into an infinite loop making an infinite-length list

```scheme
(define ones-bad (lambda () cons 1 (ones-bad)))  ; cdr returned is not a thunk!
(define (ones-bad)(cons 1 (ones-bad)))  ; same as above, (define (x) ...) means x is a function takes no parameters
```

## Memoization

 - If a function has no side effects and does not read mutable memory, no point in computing it twice for the same arguments
    - Can keep a cache of previous results
 - Similar to promises, but if the function takes arguments, then there are multiple “previous results”
 - For recursive functions, this memoization can lead to exponentially faster programs
    - Related to algorithmic technique of dynamic programming
 - (An association list (list of pairs) is a simple but sub-optimal data structure for a cache; okay for our example)

## Macros: The Key Points

 - A **macro definition** describes how to transform some new syntax into different syntax in the source language
 - A macro is one way to implement syntactic sugar
    - “Replace any syntax of the form `e1 andalso e2` with `if e1 then e2 else false`”
 - A **macro system** is a language (or part of a larger language) for defining macros 
 - **Macro expansion** is the process of rewriting the syntax for each **macro use**
    - Before a program is run (or even compiled)

### Tokenization

 - First question for a macro system: How does it tokenize?
 - Macro systems generally work at the level of tokens not sequences of characters
    - So must know how programming language tokenizes text
 - Example: “macro expand head to car ”
    - Would not rewrite (+ headt foo) to (+ cart foo)
    - Would not rewrite head-door to car-door
        - But would in C where head-door is subtraction

### Parenthesization

 - Second question for a macro system: How does associativity work?
 - C/C++ basic example:
    - `#define ADD(x,y) x+y`
 - Probably not what you wanted:
    - `ADD(1,2/3)*4 ` means `1 + 2 / 3 * 4` , not `(1 + 2 / 3) * 4`
 - So C macro writers use lots of parentheses, which is fine:
    - `#define ADD(x,y) ((x)+(y))`
 - Racket won’t have this problem:
    - Macro use: (macro-name …)
    - After expansion: ( something else in same parens )

### Scope 


 - Third question for a macro system: Can variables shadow macros?
 - Suppose macros also apply to variable bindings. Then:

```scheme
(let ([head 0][car 1]) head) ; 0
(let* ([head 0][car 1]) head) ; 0
```

Would become

```scheme
(let ([car 0][car 1]) car) ; error , not allowed declare twice
(let* ([car 0][car 1]) car) ; 1 , first car will be shadowed
```

 - This is why C/C++ convention is all-caps macros and non-all-caps for everything else
 - Racket does not work this way – it gets scope “right”!
    - **the local variable would simply shadow the macro !**

## Racket Macros with define-syntax



