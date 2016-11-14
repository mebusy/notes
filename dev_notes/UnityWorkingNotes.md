

# 工作相关 Unity 笔记

## PostProcessBuild

PostProcessBuild 这个 attribute 修饰的 **static** function 会在 Unity 建置完之后被呼叫。这个函式需要接受两个参数，一个是 BuildTarget enum ，代表建置的目标平台。另一个是 string 是建置的目标目录。

[使用 PostProcessBuild 设定 Unity 产生的 Xcode Project](http://blog.chunfuchao.com/?p=359&cpage=1&variant=zh-cn)


 - PS: `OnPostprocessBuild(BuildTarget target, string pathToBuiltProject)` 的参数 pathToBuiltProject ， 使用 cmd line编译时，不包含路径 






## Unity Archive

https://unity3d.com/get-unity/download/archive


## isDebug

```
Debug.isDebugBuild
```

## comments in inspector
```
[Header("Button Settings")]
[Tooltip("Arbitary text message")]
```

## open new OSX unity instance 

```
open -na Unity
```


## change the order or child object

```
transform.SetSiblingIndex
transform.GetSiblingIndex
```

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


## UGUI event callback

```
Dropdown scriptCameraList = cameraList.GetComponent<Dropdown> (  );

scriptCameraList.onValueChanged.AddListener((int id ) =>
{
		cameraChoosed( id );
});
```

## 获取脚本名字

```
this.GetType().Name
```

## UI Text 真实宽高

```
text.preferredWidth
text.preferredHeight
```

## iOS9 App Slicing

http://forum.unity3d.com/threads/second-preview-build-for-ios-9-on-demand-resources-and-app-slicing-support.353491/


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

## native plugin bool 返回值问题

```
[DllImport ("__Internal")]
[return: MarshalAs(UnmanagedType.U1)]
private static extern bool carFileExists(  string path ) ;
```

## Unity Engine/Editor 源码

https://bitbucket.org/Unity-Technologies/ui/src/b5f9aae6ff7c2c63a521a1cb8b3e3da6939b191b?at=5.3

## 调用父类 override 方法

```
base.func( ... )
```

## 优化

### 5.3 UI 系统

不需要交互的UI组件, 去掉 ray caster 选项
移动平台，使用 touchInputModule

### assetbundle 内存管理

创建时：

 - 加载完后立即AssetBundle.Unload(false),释放AssetBundle文件本身的内存镜像，但不销毁加载的Asset对象

释放时：

 - 如果有Instantiate的对象，用Destroy进行销毁
 - Resources.UnloadUnusedAssets,释放已经没有引用的Asset
 - 如果需要立即释放内存加上GC.Collect()


***注意： 尽管guid相同, 不同 ab 实例，会 load出多分asset ，导致内存泄漏***    
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

### MonoCompatibility

http://docs.unity3d.com/410/Documentation/ScriptReference/MonoCompatibility.html
 


## Build from command line

```
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -projectPath "${WORKSPACE}" -executeMethod Build.Build_iOS_Device -quit -logFile /dev/stdout
```

## 关闭 Debug.Log 日志

```
Debug.logger.logEnabled=false;  ???
```

##  IOS - Could not produce class with ID

这是因为你勾选了strip code,有些脚本类是被Resource下的资源引用的,打包后将Resource下的资源移除出去了，一些代码由于检测不到引用就被strip掉了，但是从AssetBundle里加载出来又需要根据ID打到对应代码。

 - http://docs.unity3d.com/Manual/ClassIDReference.html 找到ID对应的class
 - 在Assets目录下新建文件link.xml,把不该strip掉的类加进去
 - 有些类比如 AnimatorController(ID-91)属于Editor包里的，不能用link.xm加回来，可以在Resource下建一个空的prefab,在上面挂一个AnimatorController，打包时留下这个prefab就可以确保这个类不被strip掉了。


```
<?xml version="1.0" encoding="utf-8"?>
<linker>
    <assembly fullname="System">
        <type fullname="System.Net.HttpRequestCreator" preserve="all"/>        
    </assembly>

    <assembly fullname="UnityEngine">
        <type fullname="UnityEngine.CircleCollider2D" preserve="all"/>
    </assembly>
</linker>
```

## check if animation is end

```
if (animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 1 && !animator.IsInTransition(0))
```

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

## Change UI Opacity , Alpha

```
AlarmText.gameObject.SetAlpha((float)0.5);
```


## ClearChildren

```
public static void ClearChildren(this GameObject mbe) {
	int childrenCount = mbe.gameObject.transform.childCount;
	for (int i = childrenCount - 1; i >= 0; i--) {
		UnityEngine.Object.Destroy(mbe.gameObject.transform.GetChild(i).gameObject);
	}
}
```

## Force canvas sorting order

```
if (obj) {
	Canvas canvas = obj.AddComponent<Canvas> ();
	canvas.overrideSorting = true;
	canvas.sortingOrder = SORTING_ORDER_BYOND_POPUP_PAGES;
}
```

## change Image's Source Image

```
image.sprite = [your sprite]
```

