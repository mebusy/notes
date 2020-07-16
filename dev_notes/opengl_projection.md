...menustart

 - [OpenGL projection matrix](#0f2b3b75b7ab66400a079d4462330c14)
     - [Perspective](#a80420eef88d11f77532f1b9cb467fa3)
     - [Frustum](#6662e570aa6f4c7113c69b4c240dab96)

...menuend


<h2 id="0f2b3b75b7ab66400a079d4462330c14"></h2>


# OpenGL projection matrix


<h2 id="a80420eef88d11f77532f1b9cb467fa3"></h2>


## Perspective


**GLKit**

```oc
void mtxLoadPerspective(float* mtx, float fov, float aspect, float nearZ, float farZ)
{
    float f = 1.0f / tanf( (fov * (M_PI/180)) / 2.0f);
    
    mtx[0] = f / aspect;
    mtx[1] = 0.0f;
    mtx[2] = 0.0f;
    mtx[3] = 0.0f;
    
    mtx[4] = 0.0f;
    mtx[5] = f;
    mtx[6] = 0.0f;
    mtx[7] = 0.0f;
    
    mtx[8] = 0.0f;
    mtx[9] = 0.0f;
    mtx[10] = (farZ+nearZ) / (nearZ-farZ);
    mtx[11] = -1.0f;
    
    mtx[12] = 0.0f;
    mtx[13] = 0.0f;
    mtx[14] = 2 * farZ * nearZ /  (nearZ-farZ);
    mtx[15] = 0.0f;
}

// mtxLoadPerspective(projection , 90 , 2 , 5, 1000 )

// 0.500000,0.000000,0.000000,0.000000
// 0.000000,1.000000,0.000000,0.000000
// 0.000000,0.000000,-1.010050,-10.050251
// 0.000000,0.000000,-1.000000,0.000000


// mtxLoadPerspective(projection , 60 , 2 , 5, 1000 )

// 0.866025,0.000000,0.000000,0.000000
// 0.000000,1.732051,0.000000,0.000000
// 0.000000,0.000000,-1.010050,-10.050251
// 0.000000,0.000000,-1.000000,0.000000
```

[khronos gluPerspective, pls open in safari](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/gluPerspective.xml)

- Parameters
    - fovy:  Specifies the field of view angle, in degrees, in the y direction.
    - aspect:  Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height).
    - zNear: Specifies the distance from the viewer to the near clipping plane (always positive).
    - zFar: Specifies the distance from the viewer to the far clipping plane (always positive).
- In general, the aspect ratio in gluPerspective should match the aspect ratio of the associated viewport. 

![](../imgs/opengl_glperspective.png)


<h2 id="6662e570aa6f4c7113c69b4c240dab96"></h2>


## Frustum 

[khronos glFrustum, safari](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glFrustum.xml)

same as perspective

- Parameters
    - left, right: Specify the coordinates for the left and right vertical clipping planes.
    - bottom, top: Specify the coordinates for the bottom and top horizontal clipping planes.
    - nearVal, farVal: Specify the distances to the near and far depth clipping planes. Both distances must be positive.

![](../imgs/open_projection_frustum.png)

[more frustum details](http://www.songho.ca/opengl/gl_projectionmatrix.html)

z in the eye space is always projected to -ZNear on the near plane.

(x<sub>e</sub>,y<sub>e</sub>,z<sub>e</sub>)

will be projected to the near plane

(-n/z<sub>e</sub> · x<sub>e</sub>, -n/z<sub>e</sub> · y<sub>e</sub>, -n)   (PS. this coordinate not normalized in frustum)

x' = x<sub>e</sub>·n/ -z<sub>e</sub>

PS. Many 3d points will be projected on the same 2d point on the near plane( z' is fixed on ), the z-info will be lost. so we need the 4th deminsion to store z-info.


```
? 0  0   0
0  ?  0   0
0  0  A   B
 0  0  -1  0   // that is w=-z
```

z' = z/w = (A·z + B·1)/w = (A·z + B)/-z

To find the coefficients, A and B,

1. (A·-zn + B)/zn = -1   =>  -A·zn + B = -zn
2. (A·-zf + B)/zf = 1    =>  -A·zf + B = zf

solve this equation:

A = -(zf+zn)/(zf-zn)

B = -2·zf·zn/(zf-zn)


