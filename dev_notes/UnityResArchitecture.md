...menustart

 - [Unity 资源架构](#b656670a94151f6937af7e6aae08ad5a)

...menuend


<h2 id="b656670a94151f6937af7e6aae08ad5a"></h2>

# Unity 资源架构

 - unity 资源文件： .prefab, .unity
    - unity 安装包里自带 binary2text , 可以把2进制的unity资源文件 转换为 可读的文本格式
        - Library 的文件也适用
 - .meta 文件
    1. 保存 guid
        - 不仅在 editor下适用，即便在发布的版本中，还是通过 guid 来查找资源，只不过它不直接适用guid，而是计算出一个 hash id, 通过 guid/hashid 相互的转换来找到对应的资源。
    2. 保存 import settting
 - 内存， 大致分为3块
    - native (c++底层) ， mono托管堆， 第三方插件管理的内存
    - 以一张 texture 为例:
        - 2M存放在native，profile里会出现在gfx driver 里面
        - 第二部分是 wrapper , Texture2D
  


