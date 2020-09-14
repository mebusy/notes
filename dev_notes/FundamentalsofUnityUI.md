...menustart

- [Fundamentals of Unity UI](#1dfc0817fb1b2cab37c5877272360d75)
- [术语](#6d5c26750224532b44582db82a984403)
- [渲染细节](#2a168379a54008088b779159b876072f)
- [The Batch building process (Canvases)](#919839be384cb16c603fcf7941d47a2b)
- [The rebuild process (Graphics)](#4b236b0defe0140ab7c6ca4d6eb9ce03)
- [Layout rebuilds](#48573fb33426281a66a7df414d308adf)
- [Graphic rebuilds](#3bb07e02843305c2da7e77bb4877f16b)

...menuend


<h2 id="1dfc0817fb1b2cab37c5877272360d75"></h2>


# Fundamentals of Unity UI

<h2 id="6d5c26750224532b44582db82a984403"></h2>


# 术语

 - **Canvas**
    - A Canvas is a native-code Unity component that is used by Unity’s rendering system
        - to provide layered geometry that will be drawn in, or on top of, a game’s world-space.
    - Canvas负责把它们上面几何体合并成批次，生成合适的渲染指令，发送给Unity的图像系统
        - 所有这些都是Unity 本地C++代码实现的，被称作**rebatch** 或者 **batch build** 
        - When a Canvas has been marked as containing geometry that requires rebatching, the Canvas is considered **dirty**.
 - Geometry is provided to Canvases by **Canvas Renderer components**.
 - **Sub-canvas** 
    - 一个 Sub-canvas 是一个嵌套在另一个Canvas下的Canvas。
    - Sub-canvases isolate their children from their parent; 
    - a dirty child will not force a parent to rebuild its geometry, and vice versa
        - There are certain edge cases where this is not true, such as when changes to a parent Canvas cause a child Canvas to be resized
 - **Graphic** 
    - Graphic是Unity UI库提供的基类。
    - 它是所有能为Canvas系统提供可绘制几何图形的Unity UI C# 类的基类（Image，RawImage，Text）。
    - 大部分内置的Unity UI图形都是 MaskableGraphic的子类，这样它们可以通过IMaskable接口来实现遮罩。
    - 主要的可绘制的子类是 Image 和 Text，它们提供了同名的组件。
 - **Layout components**
    - Layout components 控制RectTransform的大小和位置，通常被用来创建一些复杂的排版，这些排版依赖于它们内容的相对大小和相对位置。
    - 排版组件只依赖于RectTransform，并且只影响它们管理的RectTransform。它们不依赖图形类，并且它们可以独立于Unity UI图形组件使用。
 - 图形组件和排版组件，都依赖于 **CanvasUpdateRegistry** 类, 这是UnityEditor内不可见的接口。
    - 这个类记录那些需要被更新的排版和图形组件，并且当其关联的Canavs触发willRenderCanvases事件时，触发更新。
 - 图形组件和排版组件的更新被称为 **重建(rebuild)**


<h2 id="2a168379a54008088b779159b876072f"></h2>


# 渲染细节

 - 当使用Unity UI 制作用户界面时，记住，所有的被canvas绘制的图形都是被放在透明渲染队列。
 - 这意味着，Unity UI产生的图形都会使用透明混合（alpha blending）从后向前渲染。
 - 有一个重要的性能点要注意：图形上的每一个像素都会被采样，即使它被另一个不透明的图形完全覆盖。在移动设备上，大量的的过度绘制（overdraw）可以快速超出GPU填充率的上限。

<h2 id="919839be384cb16c603fcf7941d47a2b"></h2>


# The Batch building process (Canvases)

 - The batch building process is the process whereby a Canvas combines the meshes representing its UI elements and generates the appropriate rendering commands to send to Unity’s graphics pipeline. 
 - The results of this process are cached and reused until the Canvas is marked as dirty, which occurs whenever there is a change to one of its constituent meshes.
 - Canvas使用的网格都是从绑定在Canvas上的CanvasRenderer获得，但是不包含子Canvas的网格。
 - Calculating the batches requires sorting the meshes by depth and examining them for overlaps, shared materials and so on. 
    - This operation is multi-threaded, and so its performance will generally be very different across different CPU architectures, and especially between mobile SoCs (which generally have few CPU cores) and modern desktop CPUs (which often have 4 or more cores).

<h2 id="4b236b0defe0140ab7c6ca4d6eb9ce03"></h2>


# The rebuild process (Graphics)

 - The Rebuild process is where the layout and meshes of Unity UI’s C# Graphic components are recalculated. 
    - This is performed in the CanvasUpdateRegistry class. Remember, this is a C# class and its source can be found on [Unity’s Bitbucket](https://bitbucket.org/Unity-Technologies/ui/).
 - 在CanvasUpdateRegistry内部，需要关注的方法是PerformUpdate。当Canvas组件触发WillRenderCanvases事件时都会调用这个方法。这个事件每一帧都会执行一次。
 - PerformUpdate执行三个步骤：
    - 标记为dirty的排版组件通过ICanvasElement.Rebuild方法重建布局。
    - 任何注册过的裁剪组件（如mask），需要去裁剪所有可剔除的组件。这是通过ClippingRegistry.Cull实现的。
    - 被标记为dirty的图形组件，重建它们的图形元素。
 - 对于排版和图形的重建，这些过程都会分解成过个部分。排版重建分成三个过程（PreLayout, Layout and PostLayout），图形重建包含两个过程（PreRender and LatePreRender）。

<h2 id="48573fb33426281a66a7df414d308adf"></h2>


# Layout rebuilds

 - To recalculate the appropriate positions (and potentially sizes) of components contained within one or more Layout components, it is necessary to apply the Layouts in their appropriate hierarchical order. 
 - Layouts closer to the root in the GameObject hierarchy can potentially alter the positions and sizes of any Layouts that may be nested within them, and so must be calculated first.
 - 为了实现这个，Unity UI 按照hierarchy中深度对dirty的排版组件排序，越高的（父节点少的）排在前面。排序后的布局组件被要求重建它们的布局；这就是通过改变布局组件来控制UI元素位置和大小。

<h2 id="3bb07e02843305c2da7e77bb4877f16b"></h2>


# Graphic rebuilds

 - When Graphic components are rebuilt, Unity UI passes control to the Rebuild method of the ICanvasElement interface. 
 - 图形实现这个接口，在PreRender阶段执行两个步骤。
    - 如果定点数据被标记为dirty（如RectTransfom改变大小），那么需要重建网格。
    - 如果材质数据标记为dirty（如材质或者纹理改变），关联的CanvasRenderer的材质也需要被更新。
 - 图形重建不是通过按照指定顺序设置图形组件层级执行的，不需要任何排序操作。






