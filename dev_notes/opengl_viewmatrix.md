...menustart

 - [OpenGL Viewer Transform Matrix](#8bc3626f04f3b50a0f6b9e17c9ccf6fa)

...menuend


<h2 id="8bc3626f04f3b50a0f6b9e17c9ccf6fa"></h2>


# OpenGL Viewer Transform Matrix



[GluLookAt,no chrome](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/gluLookAt.xml)
[GluLookAt code](https://www.khronos.org/opengl/wiki/GluLookAt_code)

```oc
GLK_INLINE GLKMatrix4 GLKMatrix4MakeLookAt(float eyeX, float eyeY, float eyeZ,
                                                  float centerX, float centerY, float centerZ,
                                                  float upX, float upY, float upZ)
{
    GLKVector3 ev = { eyeX, eyeY, eyeZ };
    GLKVector3 cv = { centerX, centerY, centerZ };
    GLKVector3 uv = { upX, upY, upZ };
    GLKVector3 n = GLKVector3Normalize(GLKVector3Add(ev, GLKVector3Negate(cv)));
    GLKVector3 u = GLKVector3Normalize(GLKVector3CrossProduct(uv, n));
    GLKVector3 v = GLKVector3CrossProduct(n, u);
    
    GLKMatrix4 m = { u.v[0], v.v[0], n.v[0], 0.0f,
                     u.v[1], v.v[1], n.v[1], 0.0f,
                     u.v[2], v.v[2], n.v[2], 0.0f,
                     GLKVector3DotProduct(GLKVector3Negate(u), ev),
                     GLKVector3DotProduct(GLKVector3Negate(v), ev),
                     GLKVector3DotProduct(GLKVector3Negate(n), ev),
                     1.0f };
    
    return m;
}
```

```oc
#import <GLKit/GLKit.h>

...

    GLKMatrix4 m = GLKMatrix4MakeLookAt(1,2,3,4,3,4,0,1,0);
    for ( int i=0; i<4;i++ ) {
        NSLog( @"row %d: %f,%f,%f,%f", i, m.m[i],m.m[i+4],m.m[i+8],m.m[i+12] ) ;
    }

row 0: -0.316228,0.000000,0.948683,-2.529822
row 1: -0.286039,0.953463,-0.095346,-1.334848
row 2: -0.904534,-0.301511,-0.301511,2.412091
row 3: 0.000000,0.000000,0.000000,1.000000
```


- The matrix maps the reference point to the negative z axis and the eye point to the origin. 

- construct step
    1. construct rotation matrix , using right, up, forward vector
    2. construct translates matrix 
    3. camera_matrix =  T * R   //  rotation first
    4. viewer_matrix = inv( camera_matrix )


```python
# not efficient , it is used for verification
def newLookAtMatOnTheFly2( eyePosition3D, center3D , upVector3D ):
    forward = np.zeros(3)
    # for camera , forward is mapped to -Z
    forward[0] = -(center3D[0] - eyePosition3D[0])
    forward[1] = -(center3D[1] - eyePosition3D[1])
    forward[2] = -(center3D[2] - eyePosition3D[2])
    forward = normalize( forward )

    # right hand , upxforward
    side = normalize(np.cross( upVector3D, forward ))
    up = np.cross( forward, side )

    # camera roated matrix
    m16 = np.zeros(16)  # column based
    for i in range(3):
        m16[i+0] = side[i]  # col 0 , 0-3
        m16[i+4] = up[i]  # col 1  ,  4-7
        m16[i+8] = forward[i]  # col 2  , 8-11
    m16[15] = 1

    matRot = m16.reshape(4,4).T
    matTranslate = newTranslatesMatrix( eyePosition3D[0],eyePosition3D[1],eyePosition3D[2] )
    # rotate first, then translate  
    matCamera = np.matmul( matTranslate, matRot  ) 
    # print ( "camera mat:" )
    # print( matCamera )
    return np.linalg.inv( matCamera )
```

```python
    eye = np.array([1,2,3])
    center = np.array([ 4,3,4])
    up = np.array( [0,1,0] )
    print (  newLookAtMatOnTheFly2( eye,center,up ) )
```

```bash
[[-0.31622777  0.          0.9486833  -2.52982213]
 [-0.28603878  0.95346259 -0.09534626 -2.28831021]
 [-0.90453403 -0.30151134 -0.30151134  2.7136021 ]
 [ 0.          0.          0.          1.        ]]
```

