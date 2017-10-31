
# Essence of linear algebra

## 3 Linear transformations and matrices

 - Grid lines remain parallel and evenly spaced
    - 你应该把 线性变化 看作是 "保持网格线 平行，且 等距分布" 的变化
 - 你应该如何用数值去描述 这些线性变化呢？
    - what formular do you give the computer , so that if you give it the coordinates of a vector, it can give you the coordinates of where that vector lands?
    - it turns out that you only need to record where the 2 basis vectors, î,ĵ, each land
    - for example , consider the vector v with coordinates (-1,2), means that  `v⃑ = -1î +2ĵ`
        - if we play some transformation, and follow where all 3 of these vectors go
        - the property that grid lines remain parallel and evenly spaced has a really important consequence:
            - the place where v lands, will be -1 times the vector where î landed, plus 2 times the vector where ĵ landed
        - in other words, it started off as a certain linear combination of î and ĵ, and it ends up is that **same** linear combination of where those 2 vectors landed. 
        - This means you can deduce where v must go based only on where  î and ĵ each land. 
        - This is why it is very useful to keep a copy of the original grid in the background
        - for the transformation shown here, we can read off that î lands on (1,-2) , ĵ lands on (3,0) , this means v⃑ ends up `-1*(1,-2) +2*(3,0) = (5,2)` 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_linear_transformation.png)
 - 所以，只要记录了 变换后的 î,ĵ, 我们就可以推断出任意向量在 变化后的 位置，完全不必 观察变换本身是什么样

```
⎡x⎤ = x⎡ 1⎤ +y⎡ 3⎤ = ⎡ 1x + 3y⎤
⎣y⎦    ⎣-2⎦   ⎣ 0⎦   ⎣-2x + 0y⎦  
```

 - you can calculate where any transformed vector lands using this formula.
 - what all of this is saying that a 2D linear transormation is completely described by just 4 numbers
    - the 2 coordinates for î lands
    - and the 2 coordinates for ĵ lands

```
⎡ 1 3⎤
⎣-2 0⎦
```

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_linear_transform_r0.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_linear_transform_r1.png)

 - 我们完全可以把 矩阵的列， 看作变换后的基向量; 把矩阵·向量乘法 看作它们的 线性组合。
    - 这样是不是更有趣呢？

```octave
octave:1> a = [ 1 3 ; -2 0 ]
a =

   1   3
  -2   0

octave:2> a*[-1;2]
ans =

   5
   2

octave:4> inv(a)
ans =

  -0.00000  -0.50000
   0.33333   0.16667

octave:5> inv(a)*[5;2]
ans =

  -1.0000
   2.0000
```
    
---

 - 描述 逆时针旋转90度矩阵
   - î lands on (0,1), ĵ lands on (-1,0), 所以矩阵就是

       
```
⎡ 0 -1⎤
⎣,1  0⎦
```

 - **记住，矩阵是空间的变换**
 

## 4. Matrix multiplication as composition

 - Often-times you find yourself wanting to describe the effect of applying one transformation and then another. 
    - eg. maybe you want to describe what happens when you first rotate the plane 90° counterclockwise, then apply a shear.
 - This new linear transformation is commonly called the "composition" of the 2 separate transformations we applied.
 - Like any linear transformation , it can be described with a matrix all of its own, by following î,ĵ.
    - In this example, the final matrix is [ 1 -1 ; 1 0 ]
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_linear_trans_compostion.png)
 - Here's one way to think about that new matrix:
    - if you were to take some vector and pump it through the rotation then the shear 
    - the long way to compute where it ends up is to , first , multiply it on the left by the rotation matrix; then,take whatever you get and multiply that on the left by the shear matrix. 
    - this is the same as just applying only that composition matrix
 - **Always remember, the multiplying 2 matrices like this has the geometric meaning of applying one transformation then another**
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_matrix_multiply.png)
    - `f(g(x))`
 - In next example, we will find the composition matrix by , just using the numberial entries in each matrix 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_linear_trans_compostion2.png)
    - First , we need to figure out where î goes.
        - after applying M1 , the new coordinates of î, by definition, are given by that 1st column of M1, [1;1] 
        - to see what happenes after applying M2 , multiply the matrix for M2 by that vector : `M2*[1;1] = [2;1]`.
        - [2;1] will be the 1st column of the composition matrix
    - Likewise to ĵ, the 2nd colnmn of the composition maxtrix is [0;-2]
    - 矩阵乘法 block ?
 - 证明 矩阵乘法结合律 (AB)C = A(BC) ?
    - 事实上，括号如何添加，并不会影响 A,B,C 三个变化的执行顺序, 所以最终会得到相同的结果

## 5. The determinant

 - 有件事对理解各种linear transformation 很有用，那就是测量 变换 究竟对 空间有**多少** 拉伸或挤压，更具体一点，就是测量一个给定区域面积 增大或减小的比例
 - This very special scaling factor , the factor by which a linear transformation changes any area, is called **the determinant of that transformation.**
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_determinant.png)
 - The full concept of the determinant allows for negative values
    - what would scaling an area by a negative amount even mean ? 
    - This has to do with the idea of orientation. 
        - Feels like flipping space , any transformation that do this are said to "invert the orientation of space."
    - Another way to think about it , is in terms of î,ĵ.   
        - In their starting positions, ĵ is to the left of î. 
        - If , after a transformation, ĵ is now on the right of î, the orientation of space has been inverted.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_invert_orientation.png)
 - Wheneven the orientation is inverted, the determinant will be negative.
    - the absolute value of the determinant though still tells you the factor by which areas have been scaled. 
 - What `det(M)<0` means in 3D ?
    - One way to describe orientation in 3D is with the right hand rule
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ESS_LA_right_hand_rule.png)
    - if you still can do it after transformation, orientation has not changed. 
 - det(M₁M₂) = det(M₁)det(M₂)

## 6. Inverse matrices, column space and null space

 - Usefulness of matrices
    - 描述对空间的操纵，这对 计算机图形学 和 机器人学很有用
    - 解 线性方程组 Linear system of equations 
 - rank: Number of **dimensions** in the output
    - 代表着变换后 空间的维数
    - 当变化的结果为一条直线时，我们称这个变换的 rank 为1
    - 当变化的结果为一条平面时，我们称这个变换的 rank 为2
    - 更精确的定义是 the number of dimensions in the column space.
 - Column Space
    - 不管是一条直线，一个平面，还是三维空间，所有可能的变换结果的集合，is called the **Column Space** of a matrix *A*
 - Null Space
    - 对一个full rank矩阵来说，唯一能变换后 落在原点上的，就是zero vector itself.
    - 但对于一个 非满秩矩阵来说，它将空间压缩到更多的维度, 也就是说会有 一系列 向量在变换后 成为零向量。
        - eg. 如果一个三维线性变换 将空间压缩到一条直线上，那么就有一整个平面上的向量在变换后落在原点。
    - 这些 变换后落在原点的向量的集合，is called the **Null Space** , or **Kernel** of the matrix 
    - In terms of the linear system of equation Ax=b , if b happens to be the zero vector, the null space gives you all of the possible solutions to the equation. 

## footnote. Nonsquare matrices as transformations between dimensions

```
⎡ 2 0⎤
⎢-1 1⎥
⎣-2 1⎦
```

 - 3x2 matrix
 - column space is, 一个过原点的 二维平面, 但 矩阵依然是 满秩矩阵
 - 这个矩阵的几何意义就是 将二维空间 映射到 三位空间上
    - 因为矩阵 有两列，表明 输入空间有 两个基向量
    - 有三行，表明 每一个基向量在 变换后 都用三个独立的坐标来描述

```
⎡ 3 1 4⎤
⎣ 1 5 9⎦
```

 - 2x3 matrix
 - 输入空间 有3个基向量
 - 2 rows 表明 基向量在变换后 仅用两个坐标描述， 所以它们一定落在二维空间内
 - 因此 这是一个从 三维空间 到 二维空间的变换

## 7. Dot products and duality 






