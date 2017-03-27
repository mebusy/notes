

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

## Point

 - Homogeneous coordinates
    - represent coordinates in 2 dimensions with a 3-vector

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/robot_perception_homogeneous_coordinates.png)








