
# Chapter 4  OpenGL 1.1: Light and Material

## 4.1 Introduction to Lighting

 - Lighting calculations are disabled by default in OpenGL.
 - you need to enable lighting by calling `glEnable(GL_LIGHTING)`.
    - If that's all you do, you will find that your objects are all completely black. If you want to see them, you have to turn on some lights.
 - The properties of a surface that determine how it interacts light are referred to as the **material** of the surface.  

### 4.1.1  Light and Material

 - When light strikes a surface, some of it will be reflected. 
 - In OpenGL , the complexity is approximated by two general types of reflection,  *specular reflection* and *diffuse reflection*.

![](../imgs/cg_gl_light_reflect.png)

 - In perfect specular ("mirror-like") reflection, an incoming ray of light is reflected from the surface intact(完整地).
    - The reflected ray makes the same angle with the surface as the incoming ray. 
    - A viewer can see the reflected ray only if the viewer is in exactly the right position.
    - Such reflections are referred to as  *specular highlights*.
    - In practice, we think of a ray of light as being reflected not as a single perfect ray, but as a cone of light, which can be more or less narrow.

![](../imgs/cg_gl_specular_cone.png)

 - Specular reflection from a very shiny surface produces very narrow cones of reflected light; specular highlights on such a material are small and sharp. 
    - A duller surface will produce wider cones of reflected light and bigger, fuzzier specular highlights.
    - In OpenGL, the material property that determines the size and sharpness of specular highlights is called *shininess*.
    - Shininess in OpenGL is a number in the range 0 to 128.  As the number increases, specular highlights get smaller. 
    - This image shows eight spheres that differ only in the value of the shininess material property: (from 0, increade by 16)
    - ![](../imgs/cg_gl_shininess.png)


 - In pure diffuse reflection, an incoming ray of light is scattered in all directions equally.
    - A viewer would see reflected light from all points on the surface. 
    - 如果入射光是均匀的平行光，责表面看起来被均匀照亮。如果入射光以不同的角度射入，比如来自附近的灯 或者照射表面是弯曲的，那么某一点的照射强度取决于光在改点的入射角度.

 - When light strikes a surface, some of the light can be absorbed, some can be reflected diffusely, and some can be reflected specularly. 
    - The amount of reflection can be different for different wavelengths.  材质反射各种波长光的程度 各不相同，这一性质形成了 材质特有的颜色。
    - We now see that a material can have two different colors -- a *diffuse color*  and a *specular color*. 
    - The diffuse color is the basic color of the object. The specular color determines the color of specular highlights. 
    - The diffuse and specular colors can be the same; for example, this is often true for metallic surfaces.  
        - Or they can be different; for example, a plastic surface will often have white specular highlights no matter what the diffuse color.
 - OpenGL goes even further.
    - In fact, there are two more colors associated with a material. 
 - The third color is the *ambient color* of the material, which tells how the surface reflects *ambient light*.
    - Ambient light refers to a general level of illumination that does not come directly from a light source. 
    - It consists of light that has been reflected and re-reflected so many times that it is no longer coming from any particular direction. 
    - Ambient light is why shadows are not absolutely black. 
    - 事实上，环境光只是对多重反射光的现实的粗略近似，但它比完全忽略多次反射要好。
    - The ambient color of a material determines how it will reflect various wavelengths of ambient light. 
    - *Ambient color* is generally set to be the same as the *diffuse color*. 
 - The fourth color associated with a material is an *emission color*.
    - 它不是和 前面3中颜色 同一意义上的颜色。 That is, it has nothing to do with how the surface reflects light. 
    - The emission color is color that does not come from any external source, and therefore seems to be emitted by the material itself. 
    - This does not mean that the object is giving off light that will illuminate other objects, 
        - but it does mean that the object can be seen even if there is no source of light (not even ambient light). (即便没有任何光源甚至环境光，物体也能被看到)
    - The emission color is usually black; that is, the object has no emission at all.
 - Material colors can also have *alpha components*,  but in OpenGL the only one may use alpha component is *diffuse* color .
 - In the case of the red, blue, and green components of the ambient, diffuse, or specular color, the term "color" really means reflectivity. 
    - That is, the red component of a color gives the proportion of red light hitting the surface that is reflected by that surface, and similarly for green and blue.

### 4.1.2  Light Properties




        




