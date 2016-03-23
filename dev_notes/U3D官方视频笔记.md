# U3D官方视频笔记

## Project Management

Manager of managers

 - MainManager costomizes and manages all the submanagers
 - Submanagers operate as singletons and can easily address each other or colaborate.

**Submanagers**:

EventManager | Streamline messaging between classes
--- | ---
AudioManager | COntrol audio playback from one place
GUIManager  | centralize the controls to handle clicks , etc.
PoolManager | Persist perfab instances in RAM and display them as needed
LevelManager | Queue up levels and perfrom transitions between them.
GameManager | Manage the core game mechanics , usually project specific.
SaveManager | Save and load user preference and achievements
MenuManager | Controls all menus' animations,contents, and behaviors.

### Mid-size project must have

 - LevelManager
 - PoolManager
 - SaveManager

### LevelManager

#### Why level manager ?

**Issus 1**: You need to know the scene name or the index of the scene which you want to load, but most probably the name or order will be changed later.

```
Application.LoadLevel("FirstLevel");
Application.LoadLevel(1);
```

**Issus 2**: There's no simple method of passing arguments to a scene, eg, assuming you're resuing one scene for many different levels.

> Application.LoadLevel("FirstLevel" , ~~LevelArgs~~ );

#### LevelManager Design

 - Compose a configuration table
 - Create a new API:  `LevelManager.LoadNext();`
 - manager the transitions between two levels easily

---

### PoolManager

*A simple pool design*:

 - Maintain a list of dormant(暂时不用的) objects 
```
private List<GameObject> dormantObjects = new List<GameObject>();
```

 - The list contains all different types of game objects/perfabs
 - Spawn(), Despawn(), Trim() 

```
pubic GameObject Spawn( GameObject go ) {
    GameObject temp = nil;
    if (dormantObjects.Count > 0) {
        foreach ( GameObject dob in dormantObjects ) {
            if (dob.name == go.name) {
                // find an available GameObject
                temp = dob ;
                dormantObjects.Remove(temp);
                return temp ;
            } // end if dob.name
        } //end for
    } // end if
    
    //Now instantiate a new GameObject
    temp = GameObject.Instantiate(go) as GameObject ;
    temp.name = go.name ;
    return temp ;
} // end func
```

```
public void Despawn( GameObject go ) {
    go.transform.parent = PoolManager.transform ; // why shoud have this ?
    go.SetActive( false );
    dormantObjects.Add(go) ;
    Trim();
}
```

```
public void Trim() {
    while ( dormantObjects.Count > Capacity ) {
        GameObject dob = dormantObjects[0];
        dormantObjects.RemoveAt(0);
        Destroy( dob ) ;
    } // end while
} // end func
```


**A better design:

 - PoolManger   // top pool manager
    - SpawnPool  // for a type of prefabs
        - PrefaPool // for a prefab
            - Active instances
            - Inactive instances


#### Design Rules for PoolManager

 - As a singleston.
 - Manage multiple SpawnPools.

For prefab pool:

 - Create a PrefabPool for each prefab.
 - Maintain a list of activated objects and another list of deactive objects.
 - Centrally manager the Load/Unload process here.
 - Avoid setting an instance limitation number
 - if really necessary, follow the following rules:
    - Waits for 'cullDelay' in seconds and culls the 'despawned' list if above amount
    - cull less 5 instances each time
    - start a separate coroutine to do the culling work.


### MVCS: STRANGEIOC

#### The structure of a binding -1

 - Basic Structure 
    - IBinder.Bind<Key>().To<Value>();
 - The key triggers the value

#### Types Of Binding

 Key  | Value  | Notes   
--- | --- | --- 
event | callback | an event triggers a callback
interface | implementation | binds an interface to its implementation
class | dependent class | the instantiation of one class trigger the instantiation of its dependent class

#### Dispatcher

 - Simple format
    - dispatcher.Dispatch( AttackEvent.FIRE_MISSILE ); 
 - Event + Data
    - dispatcher.Dispatch( AttackEvent.FIRE_MISSILE, orientation )

#### Binding Interface & Implementation

```
interface IMonster {
    IWeapon weapon{get;set;}
}
class Monster:IMonster {
    [Inject]  // the magic word
    public IWeapon weapon{get;set;}
}

context.injectionBinder.Bind<IWeapon>().To<Gun>();
context.injectionBinder.Bind<IWeapon>().To<Cannon>();
```

 - If you inject something, you have to map it, otherwise , it will result in null pointer errors
 - Injection employs reflection, which is slow.

### MVVM: UFRAME

---

### Other Tips

#### .gitignore file  

where to get ?

#### Coding Standards

 - Use C#
 - Naming conventions
    - Use descriptive name 
 - Logical folder structure
    - Use named empty game objects as scene folders
 - Use cache
    - Cache component references , GetComponent<ComponentName>() is slow 
    - Cache objects references , GameObject.Find() is very slow
    - Memory allocation with object pools
    - Use sharing materials

#### Art Resource Standards

 - Reasonable & strict
 - Automatic tools

#### Unity Test Tools

 - Published by Unity
 - Asset Store
 - Free

---

## AssetBundle
 
Asset: Mesh,Material,Texture, Audio,etc...

### 资源管理方式

 - Assets
    - 只有被引用的资源会被打包
    - 适合存放静态资源
    - 不能动态加载
 - Resources
    - 支持动态加载
    - Resources.assets文件 (2G限制)
    - 随安装包完全下载，无法动态更新
 - StreamingAssets
    - 保持文件原始格式
        - 比如可以存放原始的jpg文件，而不导入成内部更是
    - 随安装包完全下载，无法动态更新
    - Application.streamingAssetsPath
 - AssetBundle

  \ | 动态加载 | 动态更新 | 本地缓存
 --- | --- | --- | ---
Assets |  No | No | N/A
Resources | Yes | No | N/A
AssetBundle | Yes | Yes | Yes
StreamingAssets | Yes | No | N/A

### AssetBundle

 - Asset 的集合
 - 压缩(缺省)
 - 动态加载
 - 动态更新

### AssetBundel 打包

依赖关系导致资源重复

 - Cube-> Mat <- Cylinder
 - Asset Bundle 1
    - Cube + Mat 
 - Asset Bundle 2
    - Cylinder + Mat

### 依赖关系打包

 - Asset Bundle 1 : Cube
 - Asset Bundle 2 : Cylinder
 - Asset Bundle 3 : Mat

### 打包策略

 - 尽可能的减少冗余资源
    - 减少 AppSize , 减少网络下载流量
 - 分类打包
    - 按类型, 或者用途打包 
 - AssetBundle 大小尽量不超过1M
    - 较少 IO 压力 

### 如何处理复杂依赖关系

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/complicated_ab_dependency.jpg)


### 获取依赖关系

```
public static string[] AssetDatabase.GetDependencies(string)
```

首先以每个资源为一个节点，以最低粒度构造有向图。

只考虑入度，直接打包 入度为0的资源，可以包含入度为1的资源。
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB1.jpg)

但是入度 >= 2的资源有可能被重复打包:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB3.jpg)

### 正确的打包方式

入度为1的资源可以被自动打包到上一级的AB包中, 为避免入度为2的资源重复打包，需要将它单独放到一个AB包.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB4.jpg)

大多数情况，有向图会变得很复杂:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB5.jpg)

我们可以对有向图进行简化，入度为1的可以简化，入度为2或以上的为共享资源：

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB6.jpg)

当前节点和父节点，共同拥有的依赖关系，可将2父节点的依赖关系删除, 比如 2 和 其父节点3 都依赖于 节点1，可以将 3-1的依赖关系删除: 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB7.jpg) 

### 图的深度优先遍历

入度为0的节点开始，遍历打包

### 保存依赖关系数据

依赖关系，加载的时候需要用到


### AssetBundle 加载

 - new WWW
 - WWW.LoadFromCacheOrDownload
 - AssetBundle.CreateFromMemory
 - AssetBundle.CreateFromFile

### 依赖关系加载

需要先加载所依赖的AB包, 然后再加载自身。

### 依赖关系卸载

通过 Reference Count 来判断是否需要卸载一个AB包

### 5.0 AB 打包

BuildAssetBundle() 方法内部有处理依赖关系，但是不能完全避免资源重复.

#### 最小粒度打包

可以直接使用该API，内置依赖关系处理

AssetBundleManifest.BuildAssetBundles

#### 更优的依赖关系打包

 - 仍需通过依赖关系图去分析
 - 生成Asset 到AssetBundle的关系映射
 - 分析结果生成AssetBundleBuild

#### 5.0的简化过程

 - 不再需要push / pop 依赖关系
 - 不需要通过图的遍历逐个生成AB包
 - 只需要找到入度为0和 入度>=2 的资源节点，一次性发送到BuildAssetBundles 处理

#### AssetBundlemanifest

#### 依赖关系加载

```
AssetBundlemanifest.GetAllDependencies()
AssetBundlemanifest.GetDirectDependencies()
```

#### AssetBundle 的拆分

避免 AssetBundle 过大

#### AssetBundle 的合并

如果两个资源拥有相同的 入度和出度(资源)依赖，则可以合并:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AB8.jpg) 

