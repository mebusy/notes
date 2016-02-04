
# Unity Plugin

## Plugin Inspector

From v5 onwards, plugins can be placed at any convenient place in the project, since the target platforms are now selected from the inspector.

![](http://docs.unity3d.com/uploads/Main/PluginInspector.png)

To make transition easier from earlier Unity versions, Unity will try to set default plugins settings, depending on the folder where the plugin is located.

eg.

 - Assets/**/Editor - Plugin will be set only compatible with Editor, and won’t be used when building to platform.
 - Assets/Plugins/iOS - Plugin will be set only compatible with iOS.

 
## Managed Plugins

It is possible to compile a script to a dynamically linked library (DLL) using an external compiler.

### Creating a DLL

If the DLL contains no code that depends on the Unity API then you can simply compile it to a DLL using the appropriate compiler options. 

If you do want to use the Unity API then you will need to make Unity’s own DLLs available to the compiler. 

On a Mac, **/Applications/Unity/Unity.app/Contents/Frameworks/Managed/**

and the two DLLs are called **UnityEngine.dll** and **UnityEditor.dll**.

As an example, the command line for the Mono C# compiler, mcs, might look like this on Mac OS:

```bash
mcs -r:/Applications/Unity/Unity.app/Contents/Frameworks/Managed/UnityEngine.dll -target:library ClassesForDLL.cs 
```

 - -r option specifies a path to a library to be included in the build
    - in this case the UnityEngine library
 - -target option specifies which type of build is required
    - the word “library” is used to select a DLL build
 - Assuming all goes well, the resulting DLL file will appear shortly in the same folder as the source file.

### Using the DLL

DLLTest.dll into the Assets folder to use.

![](http://docs.unity3d.com/uploads/Main/DLLScreenshot.png)


### Step by Step Guide for MonoDevelop and Visual Studio

[More details](http://docs.unity3d.com/Manual/UsingDLL.html)


---

## Native Plugins

Native Plugins are libraries of native code written in C, C++, Objective-C, etc. 

Note: For security reasons, **plugins are not usable in web player**.

The native plugin should provide a **simple C interface** which the C# script then exposes to other user scripts. 

It is also possible for Unity to call functions exported by the native plugin when certain low-level rendering events happen (for example, when a graphics device is created).


[Code Example](http://docs.unity3d.com/Manual/NativePlugins.html)

---



## Low-level Native Plugin Interface

In addition to the basic script interface, Native Code Plugins in Unity can receive callbacks when certain events happen. 

This is mostly used to implement low-level rendering in your plugin and enable it to work with Unity’s multithreaded rendering.

### Interface Registry

A plugin should export ***UnityPluginLoad*** and ***UnityPluginUnload*** to handle main Unity events. 

See IUnityInterface.h for the correct signatures. IUnityInterfaces is provided to the plugin to access further Unity APIs.

### Access to the Graphics Device

A plugin can access generic graphics device functionality by getting the IUnityGraphics interface. In earlier versions of Unity a UnitySetGraphicsDevice function had to be exported in order to receive notification about events on the graphics device. Starting with Unity 5.2 the new IUnityGraphics interface (found in IUnityGraphics.h) provides a way to register a callback.

### Plugin Callbacks on the Rendering Thread

Rendering in Unity can be multithreaded if the platform and number of available CPUs will allow for it.

Consequently, it is not always possible for your plugin to start doing some rendering immediately, since might interfere with whatever the render thread is doing at the time.

In order to do any rendering from the plugin, you should call ***GL.IssuePluginEvent*** from your script. This will cause **the provided native function to be called** from the **render thread**. For example, if you call *GL.IssuePluginEvent* from the camera’s **OnPostRender** function, you get a plugin callback immediately after the camera has finished rendering.




## Example

An example of function exposed in plugin:

```C
static IUnityGraphics* s_Graphics = NULL;


extern "C" void	UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
UnityPluginLoad(IUnityInterfaces* unityInterfaces)
{
    ...
    s_Graphics = s_UnityInterfaces->Get<IUnityGraphics>();
    s_Graphics->RegisterDeviceEventCallback(OnGraphicsDeviceEvent);
	...
}

extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
UnityPluginUnload()
{
	s_Graphics->UnregisterDeviceEventCallback(OnGraphicsDeviceEvent);
}


extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API 
        SetTimeFromUnity (float t) 
{ 
    g_Time = t; 
}
```


 - extern "C"
    - If you are using C++ (.cpp) or Objective-C (.mm) to implement the plugin then you must ensure the functions are declared with C linkage to avoid name mangling issues.
 - A plugin should export ***UnityPluginLoad*** and ***UnityPluginUnload***
 - A plugin can access generic graphics device functionality by getting the IUnityGraphics interface.
    - IUnityGraphics interface provides a way to register a callback.
 - TODO

---

Native plugin rendering events are only called if a plugin is used by some Unity script.

This means we have to DllImport at least one function in some active script.

```C#
#if UNITY_IPHONE && !UNITY_EDITOR
	[DllImport ("__Internal")]
#else
	[DllImport ("RenderingPlugin")]
#endif
	private static extern void SetTimeFromUnity(float t);
	
#if UNITY_IPHONE && !UNITY_EDITOR
	[DllImport ("__Internal")]
#else
	[DllImport("RenderingPlugin")]
#endif
	private static extern IntPtr GetRenderEventFunc();
	
	...
	
	private IEnumerator CallPluginAtEndOfFrames()
	{
		while (true) {
			// Wait until all frame rendering is done
			yield return new WaitForEndOfFrame();

			// Set time for the plugin
			SetTimeFromUnity (Time.timeSinceLevelLoad);

			// Issue a plugin event with arbitrary integer identifier.
			// The plugin can distinguish between different
			// things it needs to do based on this ID.
			// For our simple plugin, it does not matter which ID we pass here.
			GL.IssuePluginEvent(GetRenderEventFunc(), 1);
		}
	}	
```

 - [DllImport ("**__Internal**")]
    - use __Internal for statically linked
 - must be **static extern** ?
 - GL.IssuePluginEvent
    - call native function from the **render thread**.
 - TODO


