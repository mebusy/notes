...menustart

 - [Unity 着色器训练营-第一期](#c312d2f70b33e7b9fc109a7f18b7064c)
 - [Vertex/Fragment Shader 流程图](#5f35020575fd0f69782095488cd2d31a)
     - [网格数据](#7f9c5e8dc5b4304f3dd93429b593e7cf)
     - [顶点函数  Vertex](#10bfff2b9f6e3f8264f386b9db32e2c3)
     - [顶点到片元结构体 v2f](#952f518b997e7016e2d36d7378723cbf)
     - [片元函数](#dfe265012d0b7450d8f3ea4fa60dc9ac)
     - [对象渲染到屏幕](#8b96d0b90c9fc07c078397b6e8e3525f)
 - [Shader 简介](#5b10f0101701b5aeeac2e1839b046f9a)
 - [内置函数](#78162069390d96b9230a2f222f902b54)

...menuend


<h2 id="c312d2f70b33e7b9fc109a7f18b7064c"></h2>


# Unity 着色器训练营-第一期

<h2 id="5f35020575fd0f69782095488cd2d31a"></h2>


# Vertex/Fragment Shader 流程图

 1. 网格数据
 2. 顶点函数
 3. 顶点到片元结构体
 4. 片元函数
 5. 对象渲染到屏幕


<h2 id="7f9c5e8dc5b4304f3dd93429b593e7cf"></h2>


## 网格数据

 - 常数属性数据 Properties
    - shader的变量
    - 可以由 `资源，脚本和动画数据` 驱动
    - 可以起  vertex/fragment 函数中使用
 - 网格数据
    - 将 网格mesh 数据输入到 Shader 
    - 使用 appdata struct 把网格数据 直接给 顶点函数

```c
struct appdata
{
    float4 vertex : POSITION ;
    float2 uv : TEXCOORD0 ;
    // 也可使用 UV TEXCOORD 1,2 等
    float3 normal : NORMAL ;
    float4 tangent : TANGENT ;
    float4 vertexColor: COLOR ;    
}
```

 - 冒号后边的是语义，帮助结构体更好的传递，以及更容易被理解


<h2 id="10bfff2b9f6e3f8264f386b9db32e2c3"></h2>


## 顶点函数  Vertex 

 - 用来构建对象
 - 输入参数是 网格数据， 输出的是  顶点到片元struct ( Vertex to Fragment , 简称 v2f )

```c
v2f vert(appdata v) 
{
    v2f o;
    // 在这里操纵你对象的结构
    o.vertex = UnityObjectToClipPos( v.vertex );
    o.uv = TRANSFORM_TEX( v.uv, _MainTex )
    return o;
}
```

 - UnityObjectToClipPos 封装了 computing M\*VP matrix product

<h2 id="952f518b997e7016e2d36d7378723cbf"></h2>


## 顶点到片元结构体 v2f

 - v2f 用于存储从 顶点函数 输出和 片元函数 输入的数据
 - 计算输出的 顶点位置， 自动绘制在屏幕上

```c
struct v2f
{
    float2 uv : TEXCOORD0 ; 
    float4 vertex: SV_POSITION ;    
}
```

 - SV_POSITION : sv 是 system value的简写，system 代表屏幕
 - 同样可以根据需要，输出更多的需要的数据

```c
struct v2f
{
    float2 uv : TEXCOORD0 ; 
    float4 vertex: SV_POSITION ;    

    float3 positionOfObject : TEXCOORD1 ;
    float normalAngle : TEXCOORD2 ; 
    float4 calculatedLightingColor : COLOR0;
}
```

 - 可变数据浮点数
    - float 高精度 ， 一般 32 bit
    - half 中精度 ， 一般 16 bit
    - fixed 低精度 ， 一般 11 bit
        - 值域 0-2, 可以用于 COLOR 表示

<h2 id="dfe265012d0b7450d8f3ea4fa60dc9ac"></h2>


## 片元函数    

 - 用于 画 你的对象
 - 将输入的 v2f结构体 和输出数据绘制到 屏幕上

```c
fixed4 frag (v2f i) : SV_Target
{
    // 纹理采样
    fixed4 col = tex2D( _MainTex , i.uv )  
    return col ;   
}
```

 - SV_Target : 输出到 屏幕上的一个像素点

<h2 id="8b96d0b90c9fc07c078397b6e8e3525f"></h2>


## 对象渲染到屏幕   

<h2 id="5b10f0101701b5aeeac2e1839b046f9a"></h2>


# Shader 简介

 - SubShader 
    - 每个shader可以有多个 SubShader , 一般会根据我运行的平台的不同而去使用不同的 SubShader
 - Tags 
    - 告知 SubShader 如何，何时去渲染物体
    - eg. "RenderType"
    - eg. "LightMode"="ForwardBase"   光照模式
 - Pass
    - 每个 SubShader 可以有多个 Pass, eg. 有个pass处理外套的光照，有个pass处理钩边
    - 每个Pass 会单独占用一个draw call
 - CGPROGRAM / ENDCG
    - `#pragma vertex vert`
        - 声明 vertex 函数 `vert`
    - `#pragma fragment frag` 
    - `#include "UnityCG.cginc"` 引入库
    - `float4 _TintColor;`  
        - 在 CG 中实例化 shader Properties
 - FallBack 
    - 后备方案

<h2 id="78162069390d96b9230a2f222f902b54"></h2>


# 内置函数

 - Texture Blending - lerp
 - Texture Cutout : 渐渐消失的效果

```c
_Cutout_Value( "Cutout Value" , Range(0.0, 1.0))=0.5 

float4 cutoutTextureColor = tex2D(_Cutout_Texture, IN.cutoutUV);
clip( cutoutTextureColor.rgb - _Cutout_Value ) ;
```

 - Normal Extrusion
    - vertex 坐标受到法线方向的 挤压
    - 变胖子或瘦子
 - animation clip 动画控制shader
    - eg. set `Skinned Mesh Render.Material._Wave_Distance` 
 - 脚本控制




