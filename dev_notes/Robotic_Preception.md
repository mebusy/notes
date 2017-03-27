

# 1.4 Vanishing Points

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_vanishing_point.png)

 - Properties
    - Any two parallel lines have the same vanishing point
    - The ray from C through v point is parallel to the lines
    - An image may have more than one vanishing point


## Vanishing lines

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_vanishing_lines.png)

 - Multiple Vanishing Points
    - Any set of parallel lines on the plane define a vanishing point
    - The union of all of these vanishing points is the horizon line
        - also called vanishing line
    - Note that different planes define different vanishing lines
 

 - Applicaiton
    - Comparing heights
    - Measuring height

---

# 1.5 Projective projection

## The projective plane

 - What is the geometric intuition?
    - a point in the image is a *ray* in projective space
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_projective_plane.png)
    - Each point (x,y) on the plane is represented by a ray (sx,sy,s)
    - all points on the ray are equivalent:  (x, y, 1) ≅ (sx, sy, s)
        - 一个点的齐次坐标乘上一个非零标量，则所得之坐标会表示同一个点。

## Point

 - Homogeneous coordinates 齐次坐标
    - represent coordinates in 2 dimensions with a 3-vector

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_projective_lines2.png)

image plane上的line  ，是投影空间中，rays 组成的一个平面

---

## 齐次坐标 


 - 1.1.齐次坐标的引入
    - 在欧式空间里，两条共面的平行线无法相交，然而在投影空间(Projective Space)内却不是这样
    - 欧式空间采用(x,y,z)来表示一个三维点，但是无穷远点(∞,∞,∞)在欧式空间里是没有意义的, 但是在投影空间中进行图形和几何运算并不是一个简单的问题
    - 齐次坐标系，采用N+1个量来表示N维坐标。 例如，在二维齐次坐标系中，我们引入一个量w,将一个二维点(x,y)表示为(X,Y,w)的形式，其转换关系是
        - x = X/w , y = Y/w
    - 例如，在欧式坐标中的一个二维点(1,2)可以在齐次坐标中表示为(1,2,1)
        - 如果点逐渐移动向无穷远处， 其欧式坐标变为(∞,∞)，而齐次坐标变为(1,2,0)
        - 齐次坐标下不需要∞就可以表示无限远处的点。
 - 1.2.”齐次”之名由何而来？
    - 一个二维点(1,2)转换为齐次坐标，根据规则，我们可以选择刚才用到的(1,2,1)，也可以 选择(2,4,2)，还可以选择(4,8,4),(8,16,8)...，即(k,2k,k),k∈ℝ 都是“合法”的齐次坐标表示
    - 这些 点都映射到欧式空间中的一点，即这些点具有尺度不变性(Scale Invariant)，是“齐性的”(同族的)，所以称之为齐次坐标。
 - 1.3.平行线相交:不太严格的证明
    - 考虑两条平行线：
        - Ax + By + C = 0
        - Ax + By + D = 0
    - 在欧式空间中，C=D时两条线重合，否则不相交(平行?)。尝试用 x/w, y/w 替换 x,y, (如前面提到的，用N+1个量表示N维坐标，这里增加了一个量w) ,可以得到
        - Ax + By + Cw = 0
        - Ax + By + Dw = 0
    - 可以得到解(x,y,0)，即两条平行线在(x,y,0)处相遇，称之为无穷点
 - 1.4.重要性
    - 齐次坐标表示是计算机图形学的重要手段之一，它既能够用来明确区分向量和点，同时也更易用于进行仿射（线性）几何变换
    
 - 2.1 平面点
    - 欧式坐标表示：  X = (x,y) ∈ ℝ²
    - 齐次坐标表示：  x̃ = (x̂,ŷ,w) ∈ ℙ²
    - w=0 时称为无穷点(points at infinity)， 其中 ℙ² = ℝ³-(0,0,0)  为2D投影空间. 齐次矢量  x̃  可转换为欧式表示：
        -  x̃ = (x̂,ŷ,w) = w(x,y,1) = wX̄ , X̄ 称为增广矢量(augmented vector)。
 - 2.2 平面线 
    - 齐次表示： l̃ =(a,b,c)
    - 对应欧式空间直线方程： X̄·l̃ = ax+by+c = 0 
    - 例外是在 l̃ = (0,0,1) 时为无穷线，包含了所有的2维无穷点。
    - 见 后面的 Line Representation
    - 采用齐次坐标系时，可求得两条直线的交点的齐次表达：
        - x̃ = l̃₁ x l̃₂
    - 同时，两个点确定的直线方程的齐次表达为：
        - l = x̃₁ x x̃₂
 - 2.3.为什么更易用于仿射变换？
    - 对于一个2维点p=(x,y)仿射变换(T)是线性变换(Ap)和平移变换(+t)的叠加:
        - T(p) = Ap + t
    - 线性变换在欧式空间中可以表示为矩阵乘积形式，如旋转变换和缩放变换,而平移变换却不能用矩阵相乘的形式表达。
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_linear_transform.png)
    - 现在引入齐次坐标系表达 p̃ =(x,y,1) (尺度不变性，实际上在高一维的空间映射到w=1w=1平面, 这样计算后结果直接可导出到欧式空间)。可以将rotate,scale,transfer变换表示为：
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_affine_transform.png)
    - 然后我们可以导出仿射变换的矩阵形式，
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_affine_transform_maxtrix_multiply.png)
    - 其中O₁ₓ₂=[0,0], 仿射变换保留了点的共线/面性质及比例, 这在图形处理中非常重要，比如对于 平面上的一个几何形状进行变换，只需要对其顶点进行变换就可实现.而齐次坐标系的 引入使仿射变换能以紧凑统一的矩阵形式表达和计算，这体现了其对仿射变换的重要性。
 - 2.4.为什么能够明确区分向量和点？
    - [a,b,1] 点
    - [a,b,0] 向量


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_homogeneous_coordinates.png)

## Projective lines

 - What does a line in the image correspond to in projective space?
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_projective_lines.png)
    - A line is a plane of rays through origin
        - all rays (x,y,z) satisfying: ax + by + cz = 0
        - (a,b,c)·(x,y,z) = l·p = 0
    - A line is also represented as a homogeneous 3-vector l
        - l is just the surface normal ob the set of planes


## Line Representation

 - 极坐标系下的直线方程
    - 在直角坐标系中有一条直线l，原点到该直线的垂直距离为ρ，垂线与x轴的夹角为θ，这这一条直线式唯一的，且其直线方程为：
    - `ρ = xcosθ + ysinθ`    
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_line_representation.png)
 - a line is `ρ = xcosθ + ysinθ`
    - ρ is the distance from the origin to the line
    - θ is the norm direction of the line
 - It can also be written as
    - cosθ = a/√(a²+b²)
    - sinθ = b/√(a²+b²)
    - ρ = -c/√(a²+b²)
    - => -c/√(a²+b²) = a/√(a²+b²)·x + b/√(a²+b²)·y => -c = ax + by  => ax + by + c = 0  

## Example of Line

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_example_of_line.png)

---

# 1.6 Projective projection2

##  Projective lines from two points 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_projective_lines_from_2_points.png)

## Line passing through two points

l = *x* x *x'*







