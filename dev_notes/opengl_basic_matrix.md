
# Baisc Matrix

## OpenGL Translate Matrix

[glTranslate](https://lmb.informatik.uni-freiburg.de/people/reisert/opengl/doc/glTranslate.html)

```
1 0 0 x
0 1 0 y
0 0 1 z
0 0 0 1
```

inverse of T 

```
1 0 0 -x
0 1 0 -y
0 0 1 -z
0 0 0 1
```

```python
trans: 1,2,3
[[1. 0. 0. 1.]
 [0. 1. 0. 2.]
 [0. 0. 1. 3.]
 [0. 0. 0. 1.]]
inv trans:
[[ 1.  0.  0. -1.]
 [ 0.  1.  0. -2.]
 [ 0.  0.  1. -3.]
 [ 0.  0.  0.  1.]]
```


##  Rotate Matrix * Translate Matrix 

```
r * t ============================
[[0.26726124 0.57735027 0.52320456 2.99157548]
 [0.53452248 0.57735027 0.52320456 3.25883672]
 [0.80178373 0.57735027 0.67269158 3.97455901]
 [0.         0.         0.         1.        ]]

t * r 
[[0.26726124 0.57735027 0.52320456 1.        ]
 [0.53452248 0.57735027 0.52320456 2.        ]
 [0.80178373 0.57735027 0.67269158 3.        ]
 [0.         0.         0.         1.        ]]
```

The sub 3x3 matrix doesn't changed


