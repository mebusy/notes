
# Chapter 8 Beyond Realtime Graphics

## Section 8.1 Ray Tracing

 - probably the best known technique for higher quality graphics
 - The idea behind it is
    - To find out what you see when you look in a given direction, consider a ray of light that arrives at your location from that direction, and follow that light ray backwards to see where it came from. 
    - Or, as it is usually phrased, cast a ray from your location in a given direction, and see what it hits.That's what you see when you look in that direction.
 - The operation of determining what is hit by a ray is called **ray casting**. 
 
### 8.1.1 Ray Casting

 - **THREE.RayCaster** in the three.js API
    - take an initial point and a direction (given as a vector), they determine a ray 
    - The **RayCaster** can find all the intersections of the ray with a given set of objects in the *three.js* scene, sorted by distance from ray's starting point.

![](http://math.hws.edu/graphicsbook/c8/ray-casting-3d.png)

 - We are interested in the first intersection, say C
    - We need to compute the color of C
    - we need a normal vector at C , the material properties of the surface at C , and the light that is illuminating the surface.
    - If the angle between one light source (L) and the normal vector is greater than 90 degrees, then the light source lies behind the surface and so does not add any illumination. Otherwise, we can use ray casting again:
        - Cast a ray from C in the direction L.
        - If that ray hits an object before it gets to the light, then that object will block light from that source from reaching C.
    - A ray from a point on a surface in the direction of a light source is called a **shadow ray**, 
        - because it can be used to determine whether the surface point lies in the shadow of another object.
 - Ray casting is conceptually simple, but implementation details can be tricky. 
    - surfaces are often given as **triangular meshes**, with properties specified only at the vertices of the triangles.
    - We will have to compute the properties of that intersection point by *interpolating* the property values at the vertices.
    - The interpolation algorithm typically uses something called **barycentric coordinates** on the triangle: 
        - If A, B, and C are the vertices of a triangle, and P is a point in the triangle, then 
        - P can be written uniquely in the form a*A + b*B + c*C, 
            - where a, b, and c are numbers in the range zero to one, and a + b + c = 1.
        - The coefficients a, b, and c are called the **barycentric coordinates** of the point P in the triangle. 
 - How to test whether a line intersects a triangle and how to find barycentric coordinates of the point of intersection?  
    - There are formulas.

### 8.1.2  Recursive Ray Tracing

 - Basic ray casting can be used to compute OpenGL-style rendering and, with the addition of shadow rays, to implement shadows as well. 
 - More features can be implemented by casting a few more rays. The improved algorithm is called **ray tracing**.

---

 - In reality, an object that has a mirror-like surface doesn't just reflect light sources; it also reflects other objects.
    - To do that, we can cast a "reflected ray" from A.
    - The direction of the reflected ray is determined by the normal vector to the surface at A and by the direction from A to the viewer.

![](http://math.hws.edu/graphicsbook/c8/ray-tracing-2d.png)

 - Here, the reflected ray from point A hits the purple square at point B. and the viewer will see a reflection of point B at A. 
 - To find out what the reflection of B looks like, we need to know the color of the the ray that arrives at A from B. 
 - But finding a color for B is the same sort of problem as finding a color for A, and we should solve it in the same way: 
    - by applying the ray-tracing algorithm to B! 
    - That is, we use the material properties of the surface at B, we cast shadow rays from B towards light sources to determine how B is illuminated, and—if the purple square has a mirror-like surface—we cast a reflected ray from B to find out what it reflects. 
    - In the illustration, the reflected ray from B hits a pentagon at point C.
 - Because applying the ray-tracing algorithm at one point can involve applying the same algorithm at additional points, ray tracing is a **recursive** algorithm. 
 - Ray tracing can be extended in a similar way to handle transparency or, more properly, translucency. 
    - When computing a color for a point on a translucent object, we need to take into account light that arrives at that point through the object. 
    - To do that, we can cast yet another ray from that point, this time ***into*** the object. 
    - When a light ray passes from one medium, such as air, into another medium, such as glass, the path of the light ray can bend. called *refraction*
 - The above illustration shows the refracted ray from point A passing through the object and emerging from the object at D. 
    - To find a color for that ray, we would need to find out what, if anything, it hits, and we would need to apply ray tracing recursively at the point of intersection.
    
---

 - 





            


