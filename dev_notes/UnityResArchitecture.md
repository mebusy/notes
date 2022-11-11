[](...menustart)

- [Unite Beijing 2015](#0c293a6a2db2eb8e3c978bd886f70114)
- [Unity 资源架构](#b656670a94151f6937af7e6aae08ad5a)
- [Asset Bundles](#8a1b195e72d94755b074af742d0b0cf6)
    - [老版本创建 AB](#0b0ba87fc49100e5abed047e87709872)
    - [老版本加载 AB](#8fb356dc499af99071132fa005b5fa02)
    - [新版本打包](#0ddcb8f8137cb118ce292fb25eeb3346)
        - [建立 ASSET 到 ASSETBUNDLE的映射 (1)](#922ef5b2826051cb78894baf22e49160)
        - [建立 ASSET 到 ASSETBUNDLE的映射 (2)](#140bd46bb7082048e6b86f5993095c75)
        - [创建 ASSETBUNDLE (2)](#a70c85d4c2378c0ffbf56560693a63d8)
        - [BuildAssetBundleOptions](#5c5b627e609949b6a146e5d8845516b4)
        - [新的 BuildAssetBundleOptions](#599f569a4a7e2d2f75375e8c0d2a5ab6)
        - [查找 ASSETBUNDLE](#6297ddfb8b80d1a4392ee7ac8b71c319)
        - [5.0 Advanced Features](#54086f056a59578dd3a697bbe657be74)
            - [ASSETBUNDLE 增量式打包](#4e6583637514ecbe6bfdaf7c43b863d4)
            - [MANIFEST 文件](#99d53a33fd6a1bf62611e567a230fb36)
            - [MANIFEST ASSETBUNDLE](#0d136daf0d135271201fddb2162f3a5e)
            - [EDITOR SIMULATION](#0275f23626c41e070ecac3ea90ac2fc4)
        - [ASSETBUNDLE LOAD函数](#dfe815a1916b2373c98bab408b6bd919)
        - [DEMO Prject](#423868078a7986ec0ddcdfb8a0496654)

[](...menuend)


<h2 id="0c293a6a2db2eb8e3c978bd886f70114"></h2>

# Unite Beijing 2015

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
  

<h2 id="8a1b195e72d94755b074af742d0b0cf6"></h2>

# Asset Bundles


<h2 id="0b0ba87fc49100e5abed047e87709872"></h2>

## 老版本创建 AB

- 通过 Editor脚本创建
    - BuildPipeline.BuildAssetBundle()
    - BuildPipeline.BuildAssetBundleExplicitAssetNames()
        - 制定名字
    - BuildPipeline.BuildStreamedSceneAssetBundle()
        - build 一组scene 到 asset bundle
    - Push.../Pop...

<h2 id="8fb356dc499af99071132fa005b5fa02"></h2>

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

<h2 id="0ddcb8f8137cb118ce292fb25eeb3346"></h2>

## 新版本打包

<h2 id="922ef5b2826051cb78894baf22e49160"></h2>

### 建立 ASSET 到 ASSETBUNDLE的映射 (1)

- 方法1: UI
    - 通过 Editor 的 Preview窗口
- 方法2: 脚本
    - 通过 AssetImporter.assetBundleName
- 将映射关系保存在
    1. Asset Database中
    2. Meta file 中


<h2 id="140bd46bb7082048e6b86f5993095c75"></h2>

### 建立 ASSET 到 ASSETBUNDLE的映射 (2)

- 普通Assets
    - 一个Asset只能标记到一个AssetBundle
- 场景(scene)
    - 不能把scene 和 普通的asset 标记在同一个AssetBundle
    - 因为它们对应的build脚本不一样, build scene 其实就是在build一个player
- 文件夹
    - 包含它及其所有子文件夹的Assets
- 使用相对路径

<h2 id="a70c85d4c2378c0ffbf56560693a63d8"></h2>

### 创建 ASSETBUNDLE (2)

- 完全从脚本打包

```cpp#
BuildPipeline.BuildAssetBundles(
    string outputPath , 
    AssetBundleBuild[] builds ,
    BuildAssetBundleOptions options , 
    BuildTarget targetPlatform
) ;
```

- AssetBundleBuild 结构如下

```cpp#
struct AssetBundleBuild {
    public string assetBundleName ;
    public string assetBundleVariant ;
    public string assetNames;  // 一组assets
}
```

- 直接从AssetBundleBuild 创建 AssetBundle
- 不会影响 Asset Database 中已有的映射关系
- 更不会修改 Meta file


<h2 id="5c5b627e609949b6a146e5d8845516b4"></h2>

### BuildAssetBundleOptions

- 始终启用
    - CollectDependencies
    - CompleteAssets
    - DeterministicAssetBundle
- 保持不变
    - DisableWriteTypeTree
    - UncompressedAssetBundle

<h2 id="599f569a4a7e2d2f75375e8c0d2a5ab6"></h2>

### 新的 BuildAssetBundleOptions

- ForceRebuildAssetBundle
- IgnoreTypeTreeChanges
    - 忽略typetree的变化
    - 不能与DisableTypeTree同时使用
- AppendHashToAssetBundleName 
    - 当AssetBundle变化时产生不同的名字
    - 易于检测哪些AssetBundle是需要重新上传到CDN

<h2 id="6297ddfb8b80d1a4392ee7ac8b71c319"></h2>

### 查找 ASSETBUNDLE

- AssetBundle 的 Search Filter 
    - b:
- 可与其它Search Filter 共同使用
    - t: 类型
    - l: 标记
    - b: Asset Bundle


<h2 id="54086f056a59578dd3a697bbe657be74"></h2>

### 5.0 Advanced Features

<h2 id="4e6583637514ecbe6bfdaf7c43b863d4"></h2>

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

<h2 id="99d53a33fd6a1bf62611e567a230fb36"></h2>

#### MANIFEST 文件

- 为每个AssetBundle生成的Manifest文件
    - CRC
    - 包换的 Assets
    - 所依赖的 AssetBundles
    - Hash
    - ClassTypes
- Editor only

<h2 id="0d136daf0d135271201fddb2162f3a5e"></h2>

#### MANIFEST ASSETBUNDLE

- 每次Build都会产生一个 Manifest AssetBundle
- 仅包含一个 AssetBundleManifest对象
    - GetAllAssetBunles()
    - GetDirectDependencies(string)
    - GetAllDependencies(string)
    - GetAssetBundleHash(string)
    - GetAllAssetBundlesWithVariant()

<h2 id="0275f23626c41e070ecac3ea90ac2fc4"></h2>

#### EDITOR SIMULATION 

- 可以使用 AssetBundles 而不真正build
- 只适用于 EditorPlayMode
- 不适用于 AssetBundle variants

<h2 id="dfe815a1916b2373c98bab408b6bd919"></h2>

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

<h2 id="423868078a7986ec0ddcdfb8a0496654"></h2>

### DEMO Prject

- https://files.unity3d.com/vincent/assetbundle-demo/users_assetbundles-demo.zip


---






 




