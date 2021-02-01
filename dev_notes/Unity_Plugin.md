...menustart

- [Unity Plugin](#2962917f23f1d3e579023b279d5a53e5)
    - [Plugin Inspector](#f4af3b85dca0c4507ca55336825a6a50)
    - [Managed Plugins](#334c3c4f311455f3445d04c4b67a2dbd)
        - [Creating a DLL](#615030f8cecae4a4ce7e6e4680b9e71f)
        - [Using the DLL](#ccb1d2c22ab430836b0ac9c8fd75cef7)
        - [Step by Step Guide for MonoDevelop and Visual Studio](#a0c7997f40bf2289c6f6f3600ad4c990)
    - [Native Plugins](#7724ec709771ed12ee9db9d817ec7ec4)
    - [Low-level Native Plugin Interface](#45f4836b184bb61e6897d414e2adaa3a)
        - [Interface Registry](#21e58543396d6ee441246b0e6483dba9)
        - [Access to the Graphics Device](#e7dedd682cf6b74d514fab90df8ed549)
        - [Plugin Callbacks on the Rendering Thread](#2df08455093d0b5c92d03c8e2109a55f)
    - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)

...menuend


<h2 id="2962917f23f1d3e579023b279d5a53e5"></h2>


# Unity Plugin

<h2 id="f4af3b85dca0c4507ca55336825a6a50"></h2>


## Plugin Inspector

From v5 onwards, plugins can be placed at any convenient place in the project, since the target platforms are now selected from the inspector.

![](http://docs.unity3d.com/uploads/Main/PluginInspector.png)

To make transition easier from earlier Unity versions, Unity will try to set default plugins settings, depending on the folder where the plugin is located.

eg.

- Assets/**/Editor - Plugin will be set only compatible with Editor, and won’t be used when building to platform.
- Assets/Plugins/iOS - Plugin will be set only compatible with iOS.

 
<h2 id="334c3c4f311455f3445d04c4b67a2dbd"></h2>


## Managed Plugins

It is possible to compile a script to a dynamically linked library (DLL) using an external compiler.

<h2 id="615030f8cecae4a4ce7e6e4680b9e71f"></h2>


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

<h2 id="ccb1d2c22ab430836b0ac9c8fd75cef7"></h2>


### Using the DLL

DLLTest.dll into the Assets folder to use.

![](http://docs.unity3d.com/uploads/Main/DLLScreenshot.png)


<h2 id="a0c7997f40bf2289c6f6f3600ad4c990"></h2>


### Step by Step Guide for MonoDevelop and Visual Studio

[More details](http://docs.unity3d.com/Manual/UsingDLL.html)


---

<h2 id="7724ec709771ed12ee9db9d817ec7ec4"></h2>


## Native Plugins

Native Plugins are libraries of native code written in C, C++, Objective-C, etc. 

Note: For security reasons, **plugins are not usable in web player**.

The native plugin should provide a **simple C interface** which the C# script then exposes to other user scripts. 

It is also possible for Unity to call functions exported by the native plugin when certain low-level rendering events happen (for example, when a graphics device is created).


[Code Example](http://docs.unity3d.com/Manual/NativePlugins.html)

---



<h2 id="45f4836b184bb61e6897d414e2adaa3a"></h2>


## Low-level Native Plugin Interface

In addition to the basic script interface, Native Code Plugins in Unity can receive callbacks when certain events happen. 

This is mostly used to implement low-level rendering in your plugin and enable it to work with Unity’s multithreaded rendering.

<h2 id="21e58543396d6ee441246b0e6483dba9"></h2>


### Interface Registry

A plugin should export ***UnityPluginLoad*** and ***UnityPluginUnload*** to handle main Unity events. 

See IUnityInterface.h for the correct signatures. IUnityInterfaces is provided to the plugin to access further Unity APIs.

<h2 id="e7dedd682cf6b74d514fab90df8ed549"></h2>


### Access to the Graphics Device

A plugin can access generic graphics device functionality by getting the IUnityGraphics interface. In earlier versions of Unity a UnitySetGraphicsDevice function had to be exported in order to receive notification about events on the graphics device. Starting with Unity 5.2 the new IUnityGraphics interface (found in IUnityGraphics.h) provides a way to register a callback.

<h2 id="2df08455093d0b5c92d03c8e2109a55f"></h2>


### Plugin Callbacks on the Rendering Thread

Rendering in Unity can be multithreaded if the platform and number of available CPUs will allow for it.

Consequently, it is not always possible for your plugin to start doing some rendering immediately, since might interfere with whatever the render thread is doing at the time.

In order to do any rendering from the plugin, you should call ***GL.IssuePluginEvent*** from your script. This will cause **the provided native function to be called** from the **render thread**. For example, if you call *GL.IssuePluginEvent* from the camera’s **OnPostRender** function, you get a plugin callback immediately after the camera has finished rendering.




<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>


## Example

An example of function exposed in plugin:

```Cpp
static IUnityGraphics* s_Graphics = NULL;


extern "C" void    UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
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

```Cpp#
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
    - Such callbacks can now also be added to CommandBuffers via CommandBuffer.IssuePluginEvent.
- TODO


