...menustart

 - [Unity 资源架构](#b656670a94151f6937af7e6aae08ad5a)

...menuend


<h2 id="b656670a94151f6937af7e6aae08ad5a"></h2>

# Unite Beijing 2015

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
  

# Asset Bundles


## 老版本创建 AB

 - 通过 Editor脚本创建
    - BuildPipeline.BuildAssetBundle()
    - BuildPipeline.BuildAssetBundleExplicitAssetNames()
        - 制定名字
    - BuildPipeline.BuildStreamedSceneAssetBundle()
        - build 一组scene 到 asset bundle
    - Push.../Pop...

## 老版本加载 AB

 - new WWW() 
    - WWW.assetBundle
 - WWW.LoadFromCacheOrDownload()
    - WWW.assetBundle
 - AssetBundle.CreateFromMemory()
 - AssetBundle.CreateFromMemoryImmediate()
    - 同步方法
 - AssetBundle.CreateFromFile()

---

## 新版本打包

### 建立 ASSET 到 ASSETBUNDLE的映射 (1)

 - 方法1: UI
    - 通过 Editor 的 Preview窗口
 - 方法2: 脚本
    - 通过 AssetImporter.assetBundleName
 - 将映射关系保存在
    1. Asset Database中
    2. Meta file 中


### 建立 ASSET 到 ASSETBUNDLE的映射 (2)

 - 普通Assets
    - 一个Asset只能标记到一个AssetBundle
 - 场景(scene)
    - 不能把scene 和 普通的asset 标记在同一个AssetBundle
    - 因为它们对应的build脚本不一样, build scene 其实就是在build一个player
 - 文件夹
    - 包含它及其所有子文件夹的Assets
 - 使用相对路径

### 创建 ASSETBUNDLE (2)

 - 完全从脚本打包

```c#
BuildPipeline.BuildAssetBundles(
    string outputPath , 
    AssetBundleBuild[] builds ,
    BuildAssetBundleOptions options , 
    BuildTarget targetPlatform
) ;
```

 - AssetBundleBuild 结构如下

```c#
struct AssetBundleBuild {
    public string assetBundleName ;
    public string assetBundleVariant ;
    public string assetNames;  // 一组assets
}
```

 - 直接从AssetBundleBuild 创建 AssetBundle
 - 不会影响 Asset Database 中已有的映射关系
 - 更不会修改 Meta file


### BuildAssetBundleOptions

 - 始终启用
    - CollectDependencies
    - CompleteAssets
    - DeterministicAssetBundle
 - 保持不变
    - DisableWriteTypeTree
    - UncompressedAssetBundle

### 新的 BuildAssetBundleOptions

 - ForceRebuildAssetBundle
 - IgnoreTypeTreeChanges
    - 忽略typetree的变化
    - 不能与DisableTypeTree同时使用
 - AppendHashToAssetBundleName 
    - 当AssetBundle变化时产生不同的名字
    - 易于检测哪些AssetBundle是需要重新上传到CDN

### 查找 ASSETBUNDLE

 - AssetBundle 的 Search Filter 
    - b:
 - 可与其它Search Filter 共同使用
    - t: 类型
    - l: 标记
    - b: Asset Bundle


### 5.0 Advanced Features

#### ASSETBUNDLE 增量式打包

 - 仅重新打包发生变化的 AssetBundle
 - 仅两种变化
    - Assets文件发生变化
    - TypeTree 发生变化
 - 以下各项会影响 AssetBundle的hash值
    - Asset files
    - Type trees
    - BuildTarget
    - BuildOption
    - Callbacks
        - PostProcess
    - ...
 - 两种类型的 TypeTree的变化
    - Runtime Class Typetree发生变化
        - 升级到新版本的Unity
    - Script TypeTree 发生变化
        - Public的成员变量发生变化
        - ... 

#### MANIFEST 文件

 - 为每个AssetBundle生成的Manifest文件
    - CRC
    - 包换的 Assets
    - 所依赖的 AssetBundles
    - Hash
    - ClassTypes
 - Editor only

#### MANIFEST ASSETBUNDLE

 - 每次Build都会产生一个 Manifest AssetBundle
 - 仅包含一个 AssetBundleManifest对象
    - GetAllAssetBunles()
    - GetDirectDependencies(string)
    - GetAllDependencies(string)
    - GetAssetBundleHash(string)
    - GetAllAssetBundlesWithVariant()

#### EDITOR SIMULATION 

 - 可以使用 AssetBundles 而不真正build
 - 只适用于 EditorPlayMode
 - 不适用于 AssetBundle variants

### ASSETBUNDLE LOAD函数

 - AssetBundle.LoadAsset()
 - AssetBundle.LoadAllAssets()
 - AssetBundle.LoadAssetWithSubAssets()
    - 不load整个ab， 只load某些sub assets
 - 所有的函数都提供了异步实现版本
 - AssetBundle.GetAllAssetNames()
 - AssetBundle.GetAllScenePaths()

---

 - 不再支持直接load组建类型
    - 内部也必须要先 load game object， 然后再load 组建
    - load game object -> GetComponent()

### DEMO Prject

- https://files.unity3d.com/vincent/assetbundle-demo/users_assetbundles-demo.zip


---






 




