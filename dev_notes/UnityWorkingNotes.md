[](...menustart)

- [工作相关 Unity 笔记](#a90ab7f09671a6dc89b3cdc8613d0a16)
    - [PostProcessBuild](#24591dbf27c3a0c975b8163849f47178)
    - [Unity Archive](#5799eca64b957c331cb821ef1c3c8c24)
    - [isDebug](#481ef6dbcc3f87fb143b77c2109eceac)
    - [comments in inspector](#d39c56b9dd99c012ae6fffa9403fe7fa)
    - [open new OSX unity instance](#4711c2c702d40b633bec546b1a32a686)
    - [change the order or child object](#15f9357cdfc48bea7cdf4fd8cc236113)
    - [AB: build AssetBundles](#5b22d03d81d05e11ed4b6cfd33e70535)
    - [get the name of all AssetBundles](#cb0ff2950ad57780b5f2bb4110114794)
    - [inform when Asset changed](#e367c873199629ef974a3f1e21f97981)
    - [clean Asset Bundle name](#3d6a9a1fcd9bd7d8daf655c4614fb2e1)
    - [set Asset Bundle name](#861750dc9ccbf173077aeeba3d2fdad2)
    - [UGUI event callback](#51bea0e0c0bb0336803f59dd4caf3a25)
    - [获取脚本名字](#de581e014cf8ac9cb436e6d698c2cf55)
    - [UI Text 真实宽高](#befbb8a946733519ec4f2ef2c50f675c)
    - [iOS9 App Slicing](#acd0632863feeca076212c99f111cbf4)
    - [遍历目录](#899fbb2716ba93c4b3b5ef8b591ae61f)
    - [native plugin bool 返回值问题](#ccc5ee00fef5a89cbbce16503d586e13)
    - [Unity Engine/Editor 源码](#84fd441f91b7d1374c49ebe97bf583dc)
    - [调用父类 override 方法](#856d7efa01ab9a923a3b060622542f19)
    - [优化](#aa84ec947f0a72b161a8d27598eda21e)
        - [5.3 UI 系统](#0311b56e7bb9ed6bcfd178613c7dccbb)
        - [assetbundle 内存管理](#c75153b751bc0aab3db405c5b421864a)
        - [code strip & `link.xml`](#f36000a3efff5fdb8233c537ea001725)
        - [MonoCompatibility](#9a429b30c57c8bd08af8a4cf4a8c6300)
    - [Build from command line](#5fc677a1b86704002cd1192e55cd2c98)
    - [关闭 Debug.Log 日志](#642693738e7080f3ccc7a49d81b58a7c)
    - [IOS - Could not produce class with ID](#32ab589131f3f3759f07498d06782aed)
    - [check if animation is end](#726caa74f03c8b3adce2c7cdd35895a5)
    - [iOS , overwrite UnityAppController](#f31468ec634654039cc0cc16f1ddff39)
    - [check 32-bit or 64-bit](#bea1ee4e93f2d2997848462b810321b7)
    - [RectTransform](#0985b5715fbcf7cd9d7b06666b3e3645)
    - [Change UI Opacity , Alpha](#22c2cfe7924149154316a72025caca79)
    - [ClearChildren](#d847f9321932800f839faa27122a8046)
    - [Force canvas sorting order](#c5efce759624fef37e581461dc508df7)
    - [change Image's Source Image](#3f5ccb63301562c1f2962e4fc33e13c8)
    - [c/c++ plugin Log](#b172f09ca5430b87593e0828ad617151)
    - [detect whether an object has been destroyed ?](#3a888050a1995af5dc4e05e533970e5c)
    - [ScrollView 实践](#93b2ba0c1f3e74fd40ccfbdb46ee7061)
    - [reset scroll rect content to original postion](#ff5c99f331bda1f9bf2e5016b22ad46e)
    - [Dictionary iteration](#ef0a7a0190d13816c3e68a733eb06cfc)
    - [AES , encrypt by python, decrypt by c#](#f02e785cdfc7d8abbaef854a66a36db5)
    - [http request under proxy](#7fcc9c98fbea86b9d5a1ed3186960a6f)
    - [convert Input.mouseposition to object local space](#7edf8bc89ea87e0d4a69a09a5739ce2e)

[](...menuend)


<h2 id="a90ab7f09671a6dc89b3cdc8613d0a16"></h2>

# 工作相关 Unity 笔记

<h2 id="24591dbf27c3a0c975b8163849f47178"></h2>

## PostProcessBuild

PostProcessBuild 这个 attribute 修饰的 **static** function 会在 Unity 建置完之后被呼叫。这个函式需要接受两个参数，一个是 BuildTarget enum ，代表建置的目标平台。另一个是 string 是建置的目标目录。

[使用 PostProcessBuild 设定 Unity 产生的 Xcode Project](http://blog.chunfuchao.com/?p=359&cpage=1&variant=zh-cn)


- PS: `OnPostprocessBuild(BuildTarget target, string pathToBuiltProject)` 的参数 pathToBuiltProject ， 使用 cmd line编译时，不包含路径 






<h2 id="5799eca64b957c331cb821ef1c3c8c24"></h2>

## Unity Archive

https://unity3d.com/get-unity/download/archive


<h2 id="481ef6dbcc3f87fb143b77c2109eceac"></h2>

## isDebug

```
Debug.isDebugBuild
```

<h2 id="d39c56b9dd99c012ae6fffa9403fe7fa"></h2>

## comments in inspector
```
[Header("Button Settings")]
[Tooltip("Arbitary text message")]
```

<h2 id="4711c2c702d40b633bec546b1a32a686"></h2>

## open new OSX unity instance 

```
open -na Unity
```


<h2 id="15f9357cdfc48bea7cdf4fd8cc236113"></h2>

## change the order or child object

```
transform.SetSiblingIndex
transform.GetSiblingIndex
```

<h2 id="5b22d03d81d05e11ed4b6cfd33e70535"></h2>

## AB: build AssetBundles

```
    [MenuItem ("Assets/Build AssetBundles")]
    public static void BuildAllAssetBundles ()
    {
        // clean all exist asset bundle name
        ClearAssetBundlesName.clean ();
        // re-set asset bundle
        SetAssetBundleName.setNames();

        // create out folder
        string outputPath = "./OutAssetBundles" ;
        //Path.Combine (AssetBundlesOutputPath,Platform.GetPlatformFolder(EditorUserBuildSettings.activeBuildTarget));
        if (!Directory.Exists (outputPath))
        {
            Directory.CreateDirectory(outputPath);
        }

        // build pipline
        BuildPipeline.BuildAssetBundles ( outputPath  );

        ClearAssetBundlesName.clean ();

        AssetDatabase.Refresh ();
    }
```

BuildAssetBundleOptions:

```
BuildAssetBundleOptions.ChunkBasedCompression |  BuildAssetBundleOptions.DeterministicAssetBundl
```

ChunkBasedCompression 适合实时动态加载


<h2 id="cb0ff2950ad57780b5f2bb4110114794"></h2>

## get the name of all AssetBundles

```
public class GetAssetBundleNames
{
    public static void GetNames ()
    {
        var names = AssetDatabase.GetAllAssetBundleNames();
        foreach (var name in names)
            Debug.Log ("AssetBundle: " + name);
    }
}
```

<h2 id="e367c873199629ef974a3f1e21f97981"></h2>

## inform when Asset changed

```
// info when asset changed
public class MyPostprocessor : AssetPostprocessor {

    void OnPostprocessAssetbundleNameChanged ( string path,
        string previous, string next) {
        Debug.Log("AB: " + path + " old: " + previous + " new: " + next);
    }
}
```

<h2 id="3d6a9a1fcd9bd7d8daf655c4614fb2e1"></h2>

## clean Asset Bundle name

```
public class ClearAssetBundlesName {

    public static void clean()
    {
        int length = AssetDatabase.GetAllAssetBundleNames ().Length;
        Debug.Log ( "---- existing ab name num:" + length);
        string[] oldAssetBundleNames = new string[length];
        for (int i = 0; i < length; i++) 
        {
            oldAssetBundleNames[i] = AssetDatabase.GetAllAssetBundleNames()[i];
        }

        for (int j = 0; j < oldAssetBundleNames.Length; j++) 
        {
            AssetDatabase.RemoveAssetBundleName(oldAssetBundleNames[j],true);
        }
        length = AssetDatabase.GetAllAssetBundleNames ().Length;
        Debug.Log ( "----- new ab name num:" + length);
    }
}
```

<h2 id="861750dc9ccbf173077aeeba3d2fdad2"></h2>

## set Asset Bundle name

```
public class SetAssetBundleName {
    //*
    public static void setNames( ) {
        
        walk( "./Assets" );
    }
    //*/
    static void walk(string source )
    {
        DirectoryInfo folder = new DirectoryInfo (source);
        FileSystemInfo[] files = folder.GetFileSystemInfos ();
        int length = files.Length;
        for (int i = 0; i < length; i++) {
            if(files[i] is DirectoryInfo)
            {
                walk(files[i].FullName);
            }
            else
            {
                if(!files[i].Name.EndsWith(".meta") && !files[i].Name.EndsWith(".cs") )
                {
                    setAssetBundleName (files[i].FullName);
                    //Debug.Log( files[i].Name ) ;
                }
            }
        }
    }
    static void setAssetBundleName(string source)
    {
        string _source = Replace (source);
        string _assetPath = "Assets" + _source.Substring (Application.dataPath.Length);
        string _assetPath2 = _source.Substring (Application.dataPath.Length + 1);
        //Debug.Log (_assetPath);

        //在代码中给资源设置AssetBundleName
        AssetImporter assetImporter = AssetImporter.GetAtPath (_assetPath);

        string assetName = "nofolder"; 
        int indexLastSlash = _assetPath2.LastIndexOf ("/");
        if (indexLastSlash > 0)
            assetName = _assetPath2.Substring (0, _assetPath2.LastIndexOf ("/"));
        else
            assetName = _assetPath2 ;

        // add suffix to avoid the case: bot res file and folder in a parent folder
        assetName += ".unity"; 
        
        //Debug.Log (assetName);
        assetImporter.assetBundleName = assetName;
    }

    static string Replace(string s)
    {
        return s.Replace("\\","/");
    }
}
```


<h2 id="51bea0e0c0bb0336803f59dd4caf3a25"></h2>

## UGUI event callback

```
Dropdown scriptCameraList = cameraList.GetComponent<Dropdown> (  );

scriptCameraList.onValueChanged.AddListener((int id ) =>
{
        cameraChoosed( id );
});
```

<h2 id="de581e014cf8ac9cb436e6d698c2cf55"></h2>

## 获取脚本名字

```
this.GetType().Name
```

<h2 id="befbb8a946733519ec4f2ef2c50f675c"></h2>

## UI Text 真实宽高

```
text.preferredWidth
text.preferredHeight
```

<h2 id="acd0632863feeca076212c99f111cbf4"></h2>

## iOS9 App Slicing

http://forum.unity3d.com/threads/second-preview-build-for-ios-9-on-demand-resources-and-app-slicing-support.353491/


<h2 id="899fbb2716ba93c4b3b5ef8b591ae61f"></h2>

## 遍历目录 

```
private static void GetDirs(string dirPath, ref List<string> dirs)  
{   
    if ( !Directory.Exists (dirPath))
        return;

    foreach (string path in Directory.GetFiles(dirPath))  
    {  
        //获取所有文件夹中包含后缀为 .prefab 的路径  
        //if (System.IO.Path.GetExtension(path) == ".prefab")  
        dirs.Add( path );   // path.Substring(path.IndexOf("Assets"))
        //Debug.Log(path.Substring(path.IndexOf("Assets")));  
        
    }  

    if (Directory.GetDirectories(dirPath).Length > 0)  //遍历所有文件夹  
    {  
        foreach (string path in Directory.GetDirectories(dirPath))  
        {  
            GetDirs(path, ref dirs);  
        }  
    }  
}
```

<h2 id="ccc5ee00fef5a89cbbce16503d586e13"></h2>

## native plugin bool 返回值问题

```
[DllImport ("__Internal")]
[return: MarshalAs(UnmanagedType.U1)]
private static extern bool carFileExists(  string path ) ;
```

<h2 id="84fd441f91b7d1374c49ebe97bf583dc"></h2>

## Unity Engine/Editor 源码

https://bitbucket.org/Unity-Technologies/ui/src/b5f9aae6ff7c2c63a521a1cb8b3e3da6939b191b?at=5.3

<h2 id="856d7efa01ab9a923a3b060622542f19"></h2>

## 调用父类 override 方法

```
base.func( ... )
```

<h2 id="aa84ec947f0a72b161a8d27598eda21e"></h2>

## 优化

<h2 id="0311b56e7bb9ed6bcfd178613c7dccbb"></h2>

### 5.3 UI 系统

不需要交互的UI组件, 去掉 ray caster 选项
移动平台，使用 touchInputModule

<h2 id="c75153b751bc0aab3db405c5b421864a"></h2>

### assetbundle 内存管理

创建时：

- 加载完后立即AssetBundle.Unload(false),释放AssetBundle文件本身的内存镜像，但不销毁加载的Asset对象

释放时：

- 如果有Instantiate的对象，用Destroy进行销毁
- Resources.UnloadUnusedAssets,释放已经没有引用的Asset
- 如果需要立即释放内存加上GC.Collect()


***注意： 尽管guid相同, 不同 ab 实例，会 load出多分asset ，导致内存泄漏***    
<h2 id="f36000a3efff5fdb8233c537ea001725"></h2>

### code strip & `link.xml`

```
<linker>
       <assembly fullname="UnityEngine">
               <type fullname="UnityEngine.Animation" preserve="all"/>
               <type fullname="UnityEngine.MeshCollider" preserve="all"/>
               <type fullname="UnityEngine.AnimationClip" preserve="all"/>
               <type fullname="UnityEngine.ParticleSystemRenderer" preserve="all"/>
       </assembly>
       <assembly fullname="Assembly-CSharp">
               <type fullname="MediaPlayerCtrl" preserve="all"/>
       </assembly>
</linker>


```

<h2 id="9a429b30c57c8bd08af8a4cf4a8c6300"></h2>

### MonoCompatibility

http://docs.unity3d.com/410/Documentation/ScriptReference/MonoCompatibility.html
 


<h2 id="5fc677a1b86704002cd1192e55cd2c98"></h2>

## Build from command line

```
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -projectPath "${WORKSPACE}" -executeMethod Build.Build_iOS_Device -quit -logFile /dev/stdout
```

<h2 id="642693738e7080f3ccc7a49d81b58a7c"></h2>

## 关闭 Debug.Log 日志

```
Debug.logger.logEnabled=false;  ???
```

<h2 id="32ab589131f3f3759f07498d06782aed"></h2>

##  IOS - Could not produce class with ID

这是因为你勾选了strip code,一些代码由于检测不到引用就被strip掉了，但是从AssetBundle里加载出来又需要根据ID找到对应代码。

- http://docs.unity3d.com/Manual/ClassIDReference.html 找到ID对应的class
- 在Assets目录下新建文件link.xml,把不该strip掉的类加进去
- 有些类比如 AnimatorController(ID-91)属于Editor包里的，不能用link.xm加回来，可以在Resource下建一个空的prefab,在上面挂一个AnimatorController，打包时留下这个prefab就可以确保这个类不被strip掉了。


```
<linker>
    <assembly fullname="UnityEngine">
        <type fullname="UnityEngine.Animation" preserve="all"/>
        <namespace fullname="UnityEngine.Audio" preserve="all"/>
    </assembly>
    <assembly fullname="System">
        <type fullname="System.Net.HttpWebRequest" preserve="all"/>
        <type fullname="System.Net.WebResponse" preserve="all"/>
    </assembly>
    <assembly fullname="System">
        <namespace fullname="System.Net" preserve="all"/>
        <namespace fullname="System.Net.Configuration" preserve="all"/>
    </assembly>
    <assembly fullname="mscorlib">
         <namespace fullname="System.Security.Cryptography" preserve="all"/>
    </assembly>
    <assembly fullname="Mono.Security">
        <namespace fullname="Mono.Security.Protocol.Tls" preserve="all"/>
        <namespace fullname="Mono.Security.X509" preserve="all"/>
    </assembly>
</linker>
```

<h2 id="726caa74f03c8b3adce2c7cdd35895a5"></h2>

## check if animation is end

```
if (animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 1 && !animator.IsInTransition(0))
```

<h2 id="f31468ec634654039cc0cc16f1ddff39"></h2>

## iOS , overwrite UnityAppController

```
#import "UnityAppController.h"

@interface CustomAppController : UnityAppController
@end

// let unity call CustomAppController , instead of UnityAppController
IMPL_APP_CONTROLLER_SUBCLASS (CustomAppController)

@implementation CustomAppController

- (BOOL)application:(UIApplication*)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions
{
    [super application:application didFinishLaunchingWithOptions:launchOptions];
    
    
    return YES;
}

@end
```


<h2 id="bea1ee4e93f2d2997848462b810321b7"></h2>

## check 32-bit or 64-bit

```
if (IntPtr.Size == 4) {
    //32 Bit
}
else if (IntPtr.Size == 8)
{ 
    //64 Bit
} 
```

<h2 id="0985b5715fbcf7cd9d7b06666b3e3645"></h2>

## RectTransform

```
rectTrans.offsetMin= new Vector2(-11, -12 );
rectTrans.offsetMax= new Vector2(13, 14 );

等价:

Left: -11
Button: -12
Right: -13
Top:  -14
```

<h2 id="22c2cfe7924149154316a72025caca79"></h2>

## Change UI Opacity , Alpha

```
AlarmText.gameObject.SetAlpha((float)0.5);
```


<h2 id="d847f9321932800f839faa27122a8046"></h2>

## ClearChildren

```
public static void ClearChildren(this GameObject mbe) {
    int childrenCount = mbe.gameObject.transform.childCount;
    for (int i = childrenCount - 1; i >= 0; i--) {
        UnityEngine.Object.Destroy(mbe.gameObject.transform.GetChild(i).gameObject);
    }
}
```

<h2 id="c5efce759624fef37e581461dc508df7"></h2>

## Force canvas sorting order

```
if (obj) {
    Canvas canvas = obj.AddComponent<Canvas> ();
    canvas.overrideSorting = true;
    canvas.sortingOrder = SORTING_ORDER_BYOND_POPUP_PAGES;
}
```

<h2 id="3f5ccb63301562c1f2962e4fc33e13c8"></h2>

## change Image's Source Image

```
image.sprite = [your sprite]
```

<h2 id="b172f09ca5430b87593e0828ad617151"></h2>

## c/c++ plugin Log

C# code:

```cpp#
using UnityEngine;
using System ;
using System.Collections;
using System.Runtime.InteropServices;

public class PluginTools : MonoBehaviour {

    #if UNITY_IPHONE || UNITY_XBOX360
    [DllImport ("__Internal")]
    #else
    [DllImport ("BR_Plugin")]
    #endif

    private static extern void SetDebugFunction( IntPtr fp );



    //[UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void MyDelegate(string str);

    [MonoPInvokeCallback(typeof(MyDelegate))]
    static void CallBackFunction(string str)
    {
        Debug.Log(":: " + str);
    }
        
    public static void Init () {
        MyDelegate callback_delegate = new MyDelegate( CallBackFunction );
        IntPtr intptr_delegate =
            Marshal.GetFunctionPointerForDelegate(callback_delegate);
        SetDebugFunction( intptr_delegate );
    }

}
```

c/c++ code

```cpp
#include <string.h>
#include <stdio.h>

typedef void (*FuncPtr)( const char * );
FuncPtr _DebugFunc;

void SetDebugFunction(FuncPtr fp )
{
    _DebugFunc = fp;
}

```

for using:

```cpp
typedef void (*FuncPtr)( const char * );
extern FuncPtr _DebugFunc;

#define DebugLog(  fmt, ... )    \
do { \
static char log_buf[1024] ; \
memset( log_buf , 0 , sizeof(log_buf)); \
sprintf(log_buf,  fmt, ##__VA_ARGS__); \
_DebugFunc( log_buf ); \
} while (0)

```

<h2 id="3a888050a1995af5dc4e05e533970e5c"></h2>

## detect whether an object has been destroyed ?

```
bool bInvalidObj  = gameObject == null || gameObject.Equals(null)  || ReferenceEquals (gameObject, null);
```

<h2 id="93b2ba0c1f3e74fd40ccfbdb46ee7061"></h2>

## ScrollView 实践

- scroll content 
    - ScrollRect 组建中必须 设置 Content field, UGUI 创建的 scroll view 已自动设好
    - cell item 需要添加到 content 上 , as child
- content 上一般需要添加
    - Vertical/Horizontal Layout Group 
        - 设置 Child Force Expand
    - Content Size Fitter ( 自动调整 content size )
        - 设置成 Preferred Size 
- cell item 
    - 添加 Layout Element

<h2 id="ff5c99f331bda1f9bf2e5016b22ad46e"></h2>

## reset scroll rect content to original postion 

```cpp#
scrollrect.content.anchoredPosition = Vector2.zero;
```

<h2 id="ef0a7a0190d13816c3e68a733eb06cfc"></h2>

## Dictionary iteration 

```cpp#
foreach(KeyValuePair<EventSignal,EventManager.EventFunc> entry in myRegisterEvents )
{
    // to use entry.Key , entry.Value 
}
        
```

<h2 id="f02e785cdfc7d8abbaef854a66a36db5"></h2>

## AES , encrypt by python, decrypt by c# 

- Microsoft's implementation of PKCS7 is a bit different than Python's
- [python rkcs7](https://raw.githubusercontent.com/janglin/crypto-pkcs7-example/master/pkcs7.py)

```python
# encrypt
from Crypto.Cipher import AES
from Crypto import Random
from pkcs7 import PKCS7Encoder

iv = Random.new().read(AES.block_size)
aes = AES.new(aes_key, AES.MODE_CBC, iv )
base_encrypt = aes.encrypt(PKCS7Encoder().encode( d.encode( "utf8" ) ))
encrypt_d = base64.b64encode( iv + base_encrypt   )
```

```cpp#
using System;
using System.IO;
using System.Security.Cryptography;

// c# decrypt
public String Decrypt_CBC_AES( string base64str, byte[] Key )
{
    byte[] _entireText = System.Convert.FromBase64String (base64str);

    byte[] IV = new byte[16];
    Array.Copy ( _entireText , IV, 16 );

    byte[] cipherText = new byte[ _entireText.Length - 16 ] ;
    Array.Copy (_entireText, 16, cipherText, 0 , cipherText.Length );
    _entireText = null;


    // defaults to CBC and PKCS7
    var aes = new AesManaged();
    aes.Key = Key;
    aes.IV = IV;

    var decryptor = aes.CreateDecryptor();
    var text_bytes = decryptor.TransformFinalBlock(cipherText, 0, cipherText.Length);

    //var text = textEncoder.GetString(text_bytes);
    return System.Text.UTF8Encoding.UTF8.GetString( text_bytes );

}
```

<h2 id="7fcc9c98fbea86b9d5a1ed3186960a6f"></h2>

## http request under proxy 

 1. do not use WWW , use WebClint instead
 2. set https / http proxy in you environment 
    - `HTTPS_proxy` , `HTTP_proxy`
    - be aware of the upper/lower case
 3. start unity from `Unity.app/Contents/MacOS/Unity` , not by clicking Unity.app

<h2 id="7edf8bc89ea87e0d4a69a09a5739ce2e"></h2>

## convert Input.mouseposition to object local space 

```cpp#
Vector2 localpoint;
RectTransformUtility.ScreenPointToLocalPointInRectangle(rectTransform, Input.mousePosition, GetComponentInParent<Canvas>().worldCamera, out localpoint);
Vector2 normalizedPoint = Rect.PointToNormalized(rectTransform.rect, localpoint);

Debug.Log(normalizedPoint);
```


