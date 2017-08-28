
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
