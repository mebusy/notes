
# Sympy 

## Install 

```bash
$ pip3 install sympy --user
```

## Import Library

```python
import sympy as smp
```

```python
# pretty print
from sympy import init_session
init_session(quiet=True)
# init_session will also init common symbols below
```

```python
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
```

## Basic

- Define symbols
    ```python
    >>> x, y = smp.symbols( 'x y' )
    >>> x**2
    x**2
    >>> z = x**2 + y
    >>> z
    x**2 + y
    ```
- Substitutes symbols 
    ```python
    >>> z.subs(x, 4)
    y + 16
    ```
- Commonly used mathematical functions
    ```python
    >>> smp.asin(x)
    asin(x)
    >>> smp.exp(x)
    exp(x)
    >>> smp.log(x)
    log(x)
    >>> smp.log(x, 10) # base 10
    log(x)/log(10)
    ```
- Keep Rational
    ```python
    >>> x**(3/2)
    x**1.5
    >>> # if you want keep rational
    >>> x**( smp.Rational( 3,2) )
    x**(3/2)
    ```

## Limit

```python
>>> smp.sin(x/2 + smp.sin(x) )
   ⎛x         ⎞
sin⎜─ + sin(x)⎟
   ⎝2         ⎠
>>> # take the limit as x approach to PI
>>> smp.limit( smp.sin(x/2 + smp.sin(x) ) , x, smp.pi  )
1
```

```python
# +/- side
>>> z = 2*smp.exp(1/x) / (smp.exp(1/x)+1)
>>> z
2*exp(1/x)/(exp(1/x) + 1)
>>> # take limit as x approach to 0⁺
>>> smp.limit(z, x, 0, dir='+')
2
>>> # from negative side
>>> smp.limit(z, x, 0, dir='-')
0
```

```python
# x -> infinite
>>> z = (smp.cos(x)-1)/x
>>> z
cos(x) - 1
──────────
    x
>>> smp.limit(z, x, smp.oo)
0
```

## Derivatives

```python
>>> z =  (1 + smp.sin(x))/(1 - smp.cos(x))
>>> z
1 + sin(x)
──────────
1 - cos(x)
>>> z ** 2
            2
(1 + sin(x))
─────────────
            2
(1 - cos(x))
>>> smp.diff( z**2, x)
                                      2
2⋅(sin(x) + 1)⋅cos(x)   2⋅(sin(x) + 1) ⋅sin(x)
───────────────────── - ──────────────────────
                2                       3
    (1 - cos(x))            (1 - cos(x))
```

```python
>>> z = smp.log(x,5)**(x/2)
>>> z
        x
        ─
        2
⎛log(x)⎞
⎜──────⎟
⎝log(5)⎠
>>> smp.diff(z, x)
        x
        ─ ⎛   ⎛log(x)⎞           ⎞
        2 ⎜log⎜──────⎟           ⎟
⎛log(x)⎞  ⎜   ⎝log(5)⎠      1    ⎟
⎜──────⎟ ⋅⎜─────────── + ────────⎟
⎝log(5)⎠  ⎝     2        2⋅log(x)⎠
```


```python
# chain rule
>>> f, g = symbols('f g', cls=Function)
>>> g = g(x)
>>> z = f(x+g)
>>> z
z(x + g(x))

>>> smp.diff(z, x)
⎛d           ⎞ ⎛ d        ⎞│
⎜──(g(x)) + 1⎟⋅⎜───(f(ξ₁))⎟│
⎝dx          ⎠ ⎝dξ₁       ⎠│ξ₁=x + g(x)
```

## Basci Antiderivatives

```python
>>> z = smp.csc(x) * smp.cot(x)
>>> z
cot(x)⋅csc(x)
>>> smp.integrate( z )
 -1   
──────
sin(x)
>>> # note: smp.integrate won't show `+ C`
```

## Initial Value Problems

```bash
Given dy/dx =  8⋅x + csc²(x) with y(π/2)=-7, solve for y(x)

>>> integral = smp.integrate( 8*x + smp.csc(x)**2, x )
>>> integral
   2   cos(x)
4⋅x  - ──────
       sin(x)
>>> integral.subs(x, smp.pi/2)
 2
π   # but we want it to be -7.
    # so we add the term C = -π² -7

>>> C = -smp.pi**2 - 7
>>> y = integral + C
>>> y
   2    2       cos(x)
4⋅x  - π  - 7 - ──────
                sin(x)
>>> y.subs(x, smp.pi/2)
-7
```

## Definite Integrals

```python
>>> y = smp.exp(x) / smp.sqrt( smp.exp(2*x)+9)
>>> y
       x
      ℯ
─────────────
   __________
  ╱  2⋅x
╲╱  ℯ    + 9
>>> # integral [0, ln(4)]
>>> smp.integrate( y, (x, 0, smp.log(4) ) ) # use a turple
-asinh(1/3) + asinh(4/3)
```


```python
>>> y = (x**10) * smp.exp(x)
>>> y
 10  x
x  ⋅ℯ 
>>> # integrate [1,t]
>>> smp.integrate(y, (x,1,t) )
⎛ 10       9       8        7         6          5           4           3            2                      ⎞  t 
⎝t   - 10⋅t  + 90⋅t  - 720⋅t  + 5040⋅t  - 30240⋅t  + 151200⋅t  - 604800⋅t  + 1814400⋅t  - 3628800⋅t + 3628800⎠⋅ℯ  

           
- 1334961⋅ℯ
```

## Improper Integrals

```python
>>> y = 16*smp.atan(x)/(1+x**2)
>>> y
16⋅atan(x)
──────────
   2      
  x  + 1  
>>> # integrate [0,∞)
>>> smp.integrate(y, (x,0,smp.oo))
   2
2⋅π 
```

## Sequences and Series

solve ∑<sub>n=0</sub>∞ 6/4ⁿ

```python
>>> smp.Sum(6/4**n, (n,0,smp.oo))
  ∞        
 ___       
 ╲         
  ╲      -n
  ╱   6⋅4  
 ╱         
 ‾‾‾       
n = 0   
>>> smp.Sum(6/4**n, (n,0,smp.oo)).doit()
8
```

```python
>>> smp.Sum( (1+smp.cos(n))/n, (n,1,smp.oo) )
  ∞
 ____
 ╲
  ╲
   ╲  cos(n) + 1
   ╱  ──────────
  ╱       n
 ╱
 ‾‾‾‾
n = 1
>>> smp.Sum( (1+smp.cos(n))/n, (n,1,smp.oo) ).doit()
  ∞
 ____
 ╲
  ╲
   ╲  cos(n) + 1
   ╱  ──────────
  ╱       n
 ╱
 ‾‾‾‾
n = 1   # doit() does not get the answer
```

doit() will try to find a symbolic way to find the answer, but sometimes you have to use a numerical method, in other words you approximate it , you find many many terms and see what it converges to.

```python
>>> smp.Sum( (1+smp.cos(n))/n, (n,1,smp.oo)).n()
0.e+2
>>> # is this anser correct? No, because this expression actually diverge
>>> smp.Sum( (1+smp.cos(n))/n**2, (n,1,smp.oo)).n()
1.969 # but I know it converges if I change /n to /n²
```




