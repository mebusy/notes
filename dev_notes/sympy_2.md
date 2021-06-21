
# Sympy II

```python
import numpy as np
import sympy as smp
from sympy.vector import *
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import quad_vec
```

```python
x,y,z, u1,u2,u3, v1,v2,v3, t = smp.symbols( 'x y z  u1 u2 u3  v1 v2 v3  t' )
```

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

## Dot Product

```python
>>> np.dot(a,b)
50
>>> u.dot(v)
u₁⋅v₁ + u₂⋅v₂ + u₃⋅v₃
```


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

## Length of vector

```python
>>> np.linalg.norm(a)
3.7416573867739413
>>> u.norm()
   _______________________
  ╱     2       2       2 
╲╱  │u₁│  + │u₂│  + │u₃│  
```

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

See [Dot Product and Normals to Lines and Planes](dot_norm_lines_planes.md).

```python
>>> n1 = np.array( [3, -6, -2] )
>>> n2 = np.array( [2, 1, -2] )
>>> ans = np.cross( n1,n2 )
>>> ans
[14  2 15]
```

## Vector Calculus

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

## Arclength






