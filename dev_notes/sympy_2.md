[](...menustart)

- [Sympy II](#801a16e14d536204d62b1027d930e55b)
    - [Vectors and Geometry](#74b1059efb1bc9a7532a2ce3d5a81ca3)
    - [Dot Product](#5bdd3e655ff234af7768b8653b0f60d7)
    - [Cross Product](#9760c5309454db44d51707f32c0060ff)
    - [Length of vector](#f9bba2010e97be89ce1fc95f71647f89)
    - [Vector projection](#3b70d9f00a42a7046ded4e6bff7584e2)
    - [Plane in Space](#bcf24edbc600408e71f9aa704d3e765d)
    - [Vector Calculus](#c8eaf42af0904e677cb2a80b96160a91)
        - [Vector Derivatives](#10a81f2e36fc0ac7aab0584b0ec2b4d6)
        - [Vector Integrals](#eeb3262d99392c5b5ff1fffceb4ab63a)
    - [Partial/Directional Derivatives](#c64b5c9a944ab2b58eb473454d41d985)
        - [Basic](#972e73b7a882d0802a4e3a16946a2f94)
        - [The Chain Rule](#62568a512f5b51ee525d33114a235b26)
        - [Gradients](#e99e133f4481158db879726b7335d967)
        - [Directional Derivatives](#304e4b6f83f27847ed4376143530e7fe)
    - [Extreme Values and Saddle Points](#9ead2491dd2b785094f496773bc0b7c8)
    - [Multiple Integrals](#16755d7bea6907481a5e19b6a00a97e6)
    - [Integrals and Vector Fields](#feaf4037dd6168c2b44df65e617ebc7d)

[](...menuend)


<h2 id="801a16e14d536204d62b1027d930e55b"></h2>

# Sympy II

```python
import numpy as np
import sympy as smp
from sympy.vector import *
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import quad_vec

import sympy as smp
from sympy import init_session
init_session(quiet=True)
```

```python
x,y,z, u1,u2,u3, v1,v2,v3, t = smp.symbols( 'x y z  u1 u2 u3  v1 v2 v3  t' )
```

<h2 id="74b1059efb1bc9a7532a2ce3d5a81ca3"></h2>

## Vectors and Geometry

```python
>>> a = np.array([1,2,3])
>>> b = np.array([7,8,9])
>>> u = smp.Matrix( [u1,u2,u3] )
>>> v = smp.Matrix( [v1,v2,v3] )
>>> v
⎡v₁⎤
⎢  ⎥
⎢v₂⎥
⎢  ⎥
⎣v₃⎦
>>> 2*u + v
⎡2⋅u₁ + v₁⎤
⎢         ⎥
⎢2⋅u₂ + v₂⎥
⎢         ⎥
⎣2⋅u₃ + v₃⎦
```

<h2 id="5bdd3e655ff234af7768b8653b0f60d7"></h2>

## Dot Product

```python
>>> np.dot(a,b)
50
>>> u.dot(v)
u₁⋅v₁ + u₂⋅v₂ + u₃⋅v₃
```


<h2 id="9760c5309454db44d51707f32c0060ff"></h2>

## Cross Product

```python
>>> np.cross(a,b)
[-6 12 -6]
>>> u.cross(v)
⎡u₂⋅v₃ - u₃⋅v₂ ⎤
⎢              ⎥
⎢-u₁⋅v₃ + u₃⋅v₁⎥
⎢              ⎥
⎣u₁⋅v₂ - u₂⋅v₁ ⎦
```

<h2 id="f9bba2010e97be89ce1fc95f71647f89"></h2>

## Length of vector

```python
>>> np.linalg.norm(a)
3.7416573867739413
>>> u.norm()
   _______________________
  ╱     2       2       2 
╲╱  │u₁│  + │u₂│  + │u₃│  
```

<h2 id="3b70d9f00a42a7046ded4e6bff7584e2"></h2>

## Vector projection

```python
>>> proj_b_a = np.dot(a,b)/np.linalg.norm(b)**2 * b
>>> proj_b_a
[1.80412371 2.06185567 2.31958763]
>>> proj_v_u = u.dot(v)/v.norm()**2 * v
>>> proj_v_u
⎡v₁⋅(u₁⋅v₁ + u₂⋅v₂ + u₃⋅v₃)⎤
⎢──────────────────────────⎥
⎢      2       2       2   ⎥
⎢  │v₁│  + │v₂│  + │v₃│    ⎥
⎢                          ⎥
⎢v₂⋅(u₁⋅v₁ + u₂⋅v₂ + u₃⋅v₃)⎥
⎢──────────────────────────⎥
⎢      2       2       2   ⎥
⎢  │v₁│  + │v₂│  + │v₃│    ⎥
⎢                          ⎥
⎢v₃⋅(u₁⋅v₁ + u₂⋅v₂ + u₃⋅v₃)⎥
⎢──────────────────────────⎥
⎢      2       2       2   ⎥
⎣  │v₁│  + │v₂│  + │v₃│    ⎦
```

<h2 id="bcf24edbc600408e71f9aa704d3e765d"></h2>

## Plane in Space 

Plane: *n*·( P₀- [x,y,z] ) = 0

```python
>>> P0 = smp.Matrix( [4,4,8] )
>>> r = smp.Matrix( [x,y,z] )
>>> n = smp.Matrix( [1,1,1] )
>>> n.dot( P0 - r )
-x - y - z + 16
```

Q: Find vector parallel to the line of intersection of the two planes

3x-6y-2z = 15 and 2x+y-2z = 5. ( It's going to perpendicular to both normal vetors )

We know the normal vector of this plane *3x-6y-2z = 15* is its coefficient,

See [Dot Product and Normals to Lines and Planes](dot_norm_lines_planes.md) , or [三维空间中的平面方程](https://blog.csdn.net/hb707934728/article/details/72772443)


```python
>>> n1 = np.array( [3, -6, -2] )
>>> n2 = np.array( [2, 1, -2] )
>>> ans = np.cross( n1,n2 )
>>> ans
[14  2 15]
```

<h2 id="c8eaf42af0904e677cb2a80b96160a91"></h2>

## Vector Calculus

<h2 id="10a81f2e36fc0ac7aab0584b0ec2b4d6"></h2>

### Vector Derivatives

```python
>>> r = smp.Matrix( [3*t, smp.sin(t), t**2] )
>>> r
⎡ 3⋅t  ⎤
⎢      ⎥
⎢sin(t)⎥
⎢      ⎥
⎢   2  ⎥
⎣  t   ⎦
>>> smp.diff(r,t)
⎡  3   ⎤
⎢      ⎥
⎢cos(t)⎥
⎢      ⎥
⎣ 2⋅t  ⎦
```

Example: Find the angle between the velocity and acceleration as a function of time θ(t).

```python
>>> v = smp.diff(r,t)
>>> a = smp.diff(v,t)
>>> theta = smp.acos( v.dot(a)/(v.norm()*a.norm()) ).simplify()
>>> 
>>> theta.subs(t,6).evalf()
0.251108015692338

>>> tt = np.linspace(0,10,100)
>>> aa = smp.lambdify([t], theta) (tt)
>>> plt.plot(tt,aa)
[Line2D(_line0)]
>>> plt.xlabel( 't'. fontsize=20 )
>>> plt.show()
```

<h2 id="eeb3262d99392c5b5ff1fffceb4ab63a"></h2>

### Vector Integrals

```python
>>> r = smp.Matrix( [smp.exp(t) * smp.cos(t), t**4, 1/(1+t**2)] )
>>> r
⎡ t       ⎤
⎢ℯ ⋅cos(t)⎥
⎢         ⎥
⎢    4    ⎥
⎢   t     ⎥
⎢         ⎥
⎢   1     ⎥
⎢ ──────  ⎥
⎢  2      ⎥
⎣ t  + 1  ⎦
>>>
>>> smp.Integral(r).doit()
⎡ t           t       ⎤
⎢ℯ ⋅sin(t)   ℯ ⋅cos(t)⎥
⎢───────── + ─────────⎥
⎢    2           2    ⎥
⎢                     ⎥
⎢          5          ⎥
⎢         t           ⎥
⎢         ──          ⎥
⎢         5           ⎥
⎢                     ⎥
⎣       atan(t)       ⎦
>>>
>>> r = smp.Matrix( [smp.exp(t**2)*smp.cos(t)**3, smp.exp(-t**4), 1/(3+t**2) ] )
>>> r
⎡ ⎛ 2⎞        ⎤
⎢ ⎝t ⎠    3   ⎥
⎢ℯ    ⋅cos (t)⎥
⎢             ⎥
⎢       4     ⎥
⎢     -t      ⎥
⎢    ℯ        ⎥
⎢             ⎥
⎢     1       ⎥
⎢   ──────    ⎥
⎢    2        ⎥
⎣   t  + 3    ⎦
>>> # Integrate from t=0 to t=4
>>> smp.Integral(r).doit()  # can not solve ∫ smp.exp(t**2)*smp.cos(t)**3
>>> r_num = smp.lambdify([t], r)
>>> r_num(3)
 [[-7.86223546e+03]
  [ 6.63967720e-36]
 [ 8.33333333e-02]]
>>> # _vec means this function is a vector function
>>> # quad_vec returns ( result, error )
>>> quad_vec(r_num, 0, 4)[0]
 [[-4.83559254e+05]
  [ 9.06402477e-01]
 [ 6.70972506e-01]]
>>> # smp.Integral(r, (t,0,4) ).n()    WON't work
```

<h2 id="c64b5c9a944ab2b58eb473454d41d985"></h2>

## Partial/Directional Derivatives

<h2 id="972e73b7a882d0802a4e3a16946a2f94"></h2>

### Basic

```python
>>> f = y**2 * smp.sin(x+y)
>>> smp.diff(f,x)
 2
y ⋅cos(x + y)
>>> smp.diff(f,y)
 2
y ⋅cos(x + y) + 2⋅y⋅sin(x + y)
>>>
>>> smp.diff(f, x,y,y )
   2
- y ⋅cos(x + y) - 4⋅y⋅sin(x + y) + 2⋅cos(x + y)
>>> smp.diff(f, y,x,y )
# same result, the order does not matter
   2
- y ⋅cos(x + y) - 4⋅y⋅sin(x + y) + 2⋅cos(x + y)
```


<h2 id="62568a512f5b51ee525d33114a235b26"></h2>

### The Chain Rule

```python
>>> x,y,z,w,v = smp.symbols( 'x y z w v', cls=smp.Function )
>>> # suppse x,y,z are functions of t
>>> #   w is a function of x,y,z
>>> x = x(t)
>>> y = y(t)
>>> z = z(t)
>>> w = w(x,y,z)
>>> # find dw/dt
>>> smp.diff( w,t)
  d                        d            d                        d            d                        d
─────(w(x(t), y(t), z(t)))⋅──(x(t)) + ─────(w(x(t), y(t), z(t)))⋅──(y(t)) + ─────(w(x(t), y(t), z(t)))⋅──(z(t))
dx(t)                      dt         dy(t)                      dt         dz(t)                      dt
```

Or put in specific functions

```python
>>> w1 = x**2 + smp.exp(y)*smp.sin(z)
>>> smp.diff(w1,t).subs( [ (x, smp.sin(t)), (y, smp.cos(t)), (z, t**2) ] ).doit()
     cos(t)    ⎛ 2⎞    cos(t)           ⎛ 2⎞                  
2⋅t⋅ℯ      ⋅cos⎝t ⎠ - ℯ      ⋅sin(t)⋅sin⎝t ⎠ + 2⋅sin(t)⋅cos(t)
```

<h2 id="e99e133f4481158db879726b7335d967"></h2>

### Gradients

```python
>>> from sympy.vector import CoordSys3D
>>> C = CoordSys3D('')
>>>
>>> C.x, C.y, C.z
(x_, y_, z_)
>>> f = C.x * smp.sin(C.y)
>>> f
x_⋅sin(y_)
>>> smp.vector.gradient(f)
(sin(y_)) i_ + (x_⋅cos(y_)) j_
>>> smp.vector.gradient(f).to_matrix(C)
⎡ sin(y_)  ⎤
⎢          ⎥
⎢x_⋅cos(y_)⎥
⎢          ⎥
⎣    0     ⎦
```

<h2 id="304e4b6f83f27847ed4376143530e7fe"></h2>

### Directional Derivatives

Directional derivatives Dᵤf = ∇f·u

```python
>>> u = 4*C.i - 3*C.j + 2*C.k
>>> u
(4) i_ + (-3) j_ + (2) k_
>>> u = u.normalize()
>>> u
⎛4⋅√29⎞      ⎛-3⋅√29 ⎞      ⎛2⋅√29⎞   
⎜─────⎟ i_ + ⎜───────⎟ j_ + ⎜─────⎟ k_
⎝  29 ⎠      ⎝   29  ⎠      ⎝  29 ⎠   
>>>
>>> f
x_⋅sin(y_)
>>> smp.vector.gradient(f).dot(u)
  3⋅√29⋅x_⋅cos(y_)   4⋅√29⋅sin(y_)
- ──────────────── + ─────────────
         29                29
```

<h2 id="9ead2491dd2b785094f496773bc0b7c8"></h2>

## Extreme Values and Saddle Points

Extreme values of f(x,y) can occur at 

1. Boundary points of the domain of f
    - e.g. a surface with boundary
2. Critical Points ( f<sub>x</sub> = f<sub>y</sub> = 0 )

```python
>>> x, y = smp.symbols('x y', real = True)
>>> f = x**3 + 3*x*y + y**3
>>> f
 3            3
x  + 3⋅x⋅y + y
>>> smp.solve( [smp.diff(f,x ), smp.diff(f,y)] ) # solve to make all equations to be 0.
[{x: -1, y: -1}, {x: 0, y: 0}]
```

More, use 2nd derivatives to check...

<h2 id="16755d7bea6907481a5e19b6a00a97e6"></h2>

## Multiple Integrals 

```python
>>> smp.Integral( f, (z, 3,4-x**2-y**2 ), (y, 0,1-x**2), (x,0,1) )
        2      2   2               
1  1 - x     -x  -y  +4           
⌠   ⌠          ⌠                 
⎮   ⎮          ⎮       x dz dy dx
⌡   ⌡          ⌡                 
0   0          3          
>>> smp.integrate( f, (z, 3,4-x**2-y**2 ), (y, 0,1-x**2), (x,0,1) )
1/8
```

But most of the time, they need to be done numerically. e.g.:

```python
>>> f = x*smp.exp(-y)*smp.cos(z)
>>> smp.Integral( f, (z, 3,4-x**2-y**2 ), (y, 0,1-x**2), (x,0,1) )
       2     2   2
1 1 - x    -x  -y  +4
⌠   ⌠          ⌠
⎮   ⎮          ⎮          -y
⎮   ⎮          ⎮       x⋅ℯ  ⋅cos(z) dz dy dx
⌡   ⌡          ⌡
0   0          3
```

Use scipy to evaluate this numerically.

```python
>>> from scipy.integrate import tplquad
>>> f = lambda z,y,x : x*np.exp(-y) * np.cos(z)
>>> tplquad( f, 0, 1,
...     lambda x: 0, lambda x: 1-x**2,
...     lambda x, y: 3, lambda x,y: 4-x**2-y**2)[0]
-0.09109526451447894
```

<h2 id="feaf4037dd6168c2b44df65e617ebc7d"></h2>

## Integrals and Vector Fields 

TODO 32:00

https://www.youtube.com/watch?v=Teb28OFMVFc




