
# Rendering Path

## 1. rendering path 的 技术基础

 - 现代的图形渲染管线
    - Geometry → Vertex Shader → Tessellation Shader → Geometry Shader → Fragment Shader → FrameBuffer
 - 可编程管线的流程. 以OpenGL绘制一个三角形举例。
    - 首先用户指定三个顶点传给Vertex Shader
    - 然后用户可以选择是否进行Tessellation Shader（曲面细分可能会用到）和Geometry Shader（可以在GPU上增删几何信息）
    - 紧接着进行光栅化
    - 再将光栅化后的结果传给Fragment Shader进行pixel级别的处理
    - 最后将处理的像素传给FrameBuffer并显示到屏幕上

## 2. 几种常用的Rendering Path

 - Rendering Path其实指的就是渲染场景中光照的方式
    - 由于场景中的光源可能很多，甚至是动态的光源。所以怎么在速度和效果上达到一个最好的结果确实很困难。
    - 以当今的显卡发展为契机，人们才衍生出了这么多的Rendering Path来处理各种光照。

### 2.1 Forward Rendering

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_fwdrd.png)

 - Forward Rendering是绝大数引擎都含有的一种渲染方式
 - 要使用Forward Rendering，一般在Vertex Shader或Fragment Shader阶段对每个顶点或每个像素进行光照计算，并且是对每个光源进行计算产生最终结果 
 - Forward Rendering的核心伪代码

```
For each ligth:
    For each object affected by the light:
        framebuffer += object * light
```

 - Unity3D, 对于下图中的圆圈（表示一个Geometry），进行Forward Rendering处理

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_fwdrd_01.png)

 - 将得到下面的处理结果
    - 也就是说，对于ABCD四个光源我们在Fragment Shader中我们对每个pixel处理光照，
    - 对于DEFG光源我们在Vertex Shader中对每个vertex处理光照，
    - 而对于GH光源，我们采用球调和（SH）函数进行处理

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_fwdrd_02.png)

 - Forward Rendering优缺点
    - 光源数量对计算复杂度影响巨大，所以比较适合户外这种光源较少的场景（一般只有太阳光）
    - 对于多光源，我们使用Forward Rendering的效率会极其低下。
 - 必要的优化
    1.多在vertex shader中进行光照处理
    2.如果要在fragment shader中处理光照，我们大可不必对每个光源进行计算时，把所有像素都对该光源进行处理一次。因为每个光源都有其自己的作用区域。
        - 比如点光源的作用区域是一个球体，而平行光的作用区域就是整个空间了
        - 对于不在此光照作用区域的像素就不进行处理。
        - 但是这样做的话，CPU端的负担将加重，因为要计算作用区域
    3.对于某个几何体，光源对其作用的程度是不同，所以有些作用程度特别小的光源可以不进行考虑。
        - 典型的例子就是Unity中只考虑重要程度最大的4个光源。

## 2.2 Deferred Rendering


