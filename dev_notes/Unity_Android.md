[](...menustart)

- [Unity - Android](#c2ffa44d58b8bac831cb4c782fb01ade)
    - [Android SDK Setup](#e0c2f5b13be3164313231f7289407244)
    - [Unity Remove 4](#bbddfbb27c097a0f4075d43d6e054e79)
    - [Inside the Android Build Process](#527af06b45ea8371224628d1e9f8a52d)
        - [Texture Compression](#dcabe0dca89861f1a51eb815d92b7f80)
        - [Features currently not supported by Unity Android](#76be2860342f35d1b19db62423df76d0)
        - [Android Scripting](#7753889e829e7f7c51771a01e862e7bf)
            - [Advanced Unity Mobile Scripting](#2db8de39645d281d9071415f5aac2319)
        - [Building Plugins for Android](#6a90ae54dfe15833c91435281d0ea1ef)
            - [Native Plugin](#0edb001a0a575634d2fcd655007e12e5)
            - [Android Library Projects](#4193dbb572f85515fe526433c9cf2a94)
            - [Deployment](#ea355214fd4bc7c57f471bd92918879b)
            - [Using Java Plugins](#538a16b6cc13007d77ca9afa193488ad)
                - [Using Your Java Plugin from Native Code](#85d7c5a7595a0c5f6ef85f4187416d99)
    - [Android SDK](#28e3c4f8fa197ba60f832800460e36e7)
        - [create AVD](#f6851bab6b694b76b183e4a29ab9d0e1)
    - [NDK](#a781e0468f15d9a9776aa0ec03389053)
        - [Android.mk](#3ae6be565f1e33e90e0b11f768de1f6c)
            - [Basics](#bbc9105ee8508ce6e083a589a351e83a)
            - [Variables and Macros](#71d8a20d51b4fd098e224bbceafe5e3e)
            - [NDK-defined variables](#34a0ad7ce398db363c3bea74d3bf8158)
            - [Module-Description Variables](#f1f83bbb1daf12a9ecb64594df31a8be)
            - [NDK-provided function macros](#23475e2848e87691b2297b77ec135d34)
        - [Application.mk](#8e3060573a2bb39017e391f1f7ec4997)
    - [Misc](#74248c725e00bf9fe04df4e35b249a19)
        - [获取 android id](#169abc368db1ed3b7ced23a4f442cb7b)
        - [获取 mac address](#83dc2a583afc95dfd2221b8220e16748)
        - [unity android get Current Application context](#cf00f742bf3ddb4dbebe6f4dbd32f96c)
        - [jar 打包](#29701a188748cb389ef5d6db4b65d70d)

[](...menuend)


<h2 id="c2ffa44d58b8bac831cb4c782fb01ade"></h2>

# Unity - Android

<h2 id="e0c2f5b13be3164313231f7289407244"></h2>

## Android SDK Setup

 1. [Installing the SDK](http://developer.android.com/sdk/installing/index.html) 
 2. add at least one **Android platform** with API level 9+
    - `cd android-sdk-macosx/tools`
    - `./android sdk`
        - 5.3 编android版本需要一个 5.0 SDK
    - ***SDK Platform***
        - A system image for the emulator, such as 
***ARM EABI v7a System Image***
 3. add the **Platform Tools** 
     - ***Android SDK Tools***
     - ***Android SDK Platform-tools***
     - ***Android SDK Build-tools*** (highest version)
 4. turn on ***“USB Debugging”*** on your device. 
    - Go to Settings -> Developer options, then enable USB debugging
    - To show the Developer options, Settings -> About XXX -> Build Version/Module multiple times
 5. Add the Android SDK path to Unity
    - *Unity > Preferences -> External Tools*
 6. If you use Gradle, also install Extra/**Android Support Library** 和 Extra/**Android Support Repository** 

<h2 id="bbddfbb27c097a0f4075d43d6e054e79"></h2>

## Unity Remove 4

Remote Setting:  Menu Edit > Project Settings > Editor
    
<h2 id="527af06b45ea8371224628d1e9f8a52d"></h2>

## Inside the Android Build Process

When building the app to the Android, be sure that the device has the ***“USB Debugging” and the “Allow mock locations”*** checkboxes checked in the device settings.

![](http://docs.unity3d.com/uploads/Main/android-device-dev.png)

You can ensure that the operating system sees your device by running `adb devices` command found in your Android SDK/platform-tools folder. This should work both for Mac and Windows.

```bash
$ adb devices
List of devices attached
08e9f72c    device
```

<h2 id="dcabe0dca89861f1a51eb815d92b7f80"></h2>

### Texture Compression

By default, Unity uses **ETC1/RGBA16** texture format for textures that don’t have individual texture format overrides (see Texture 2D / Per-Platform Overrides).


<h2 id="76be2860342f35d1b19db62423df76d0"></h2>

### Features currently not supported by Unity Android

- Graphics
    - Non-square textures are not supported by the ETC format.
    - Movie Textures are not supported, use a full-screen streaming playback instead
- Scripting
    - Dynamic features like **Duck Typing** are not supported. Use #pragma strict for your scripts to force the compiler to report dynamic features as errors.
        - dynamic key word so that 不使用继承的情况下使用了多态 ??? 
    - Video streaming via WWW class is not supported


<h2 id="7753889e829e7f7c51771a01e862e7bf"></h2>

### Android Scripting

macro : `UNITY_ANDROID`

<h2 id="2db8de39645d281d9071415f5aac2319"></h2>

#### Advanced Unity Mobile Scripting

- Device Properties
    - SystemInfo.deviceUniqueIdentifier
    - SystemInfo.deviceName
    - SystemInfo.deviceModel 
    - SystemInfo.operatingSystem.
- Anti-Piracy Check
    - You can check if your application is genuine (not-hacked) with the Application.genuine property

---

<h2 id="6a90ae54dfe15833c91435281d0ea1ef"></h2>

### Building Plugins for Android

<h2 id="0edb001a0a575634d2fcd655007e12e5"></h2>

#### Native Plugin

To build a plugin for Android, you should first obtain the ***Android NDK*** and familiarize yourself with the steps involved in building a **shared library**.

<h2 id="4193dbb572f85515fe526433c9cf2a94"></h2>

#### Android Library Projects

You can drop pre-compiled Android library projects into the Assets->Plugins->Android folder.

Pre-compiled means all .java files must have been compiled into **jar** files located in either the bin/ or the libs/ folder of the project. 

AndroidManifest.xml from these folders will get automatically **merged** with the main manifest file when the project is built. ( 子目录必须是android工程，project.properties 中必须有 `android.library=true` )


自定义 AndroidManifest.xml 时, activity 使用 UnityPlayerActivity :

```
<activity
            android:name="com.unity3d.player.UnityPlayerActivity"
```

或者使用自己的继承自 UnityPlayerActivity 的 Activity.

<h2 id="ea355214fd4bc7c57f471bd92918879b"></h2>

####  Deployment

For specific Android platform (armv7, x86), the libraries (lib*.so) should be placed in the following:

- Assets/Plugins/Android/libs/x86/
- Assets/Plugins/Android/libs/armeabi-v7a/

<h2 id="538a16b6cc13007d77ca9afa193488ad"></h2>

#### Using Java Plugins

The Android plugin mechanism also allows Java to be used to enable interaction with the Android OS.

A .jar file containing the .class files for your plugin

- Unity expects Java plugins to be built using JDK v1
    - `-source 1.6 -target 1.6`


<h2 id="85d7c5a7595a0c5f6ef85f4187416d99"></h2>

##### Using Your Java Plugin from Native Code

 1. copy .jar into Assets->Plugins->Android
 2. Unity will package your .class files together with the rest of the Java code and then access the code using JNI.


<h2 id="28e3c4f8fa197ba60f832800460e36e7"></h2>

## Android SDK

<h2 id="f6851bab6b694b76b183e4a29ab9d0e1"></h2>

### create AVD

```
android create avd --name A16_4.1.2 --target android-16 --abi armeabi-v7a
```

`--target` , `--abi` 参数具体的值，可以通过 list target 命令获得：

```
android list target
```

查看所有的AVD:

```
android list avd
```

Verify that the AVD is working:

```
emulator --avd A16_4.1.2
```

<h2 id="a781e0468f15d9a9776aa0ec03389053"></h2>

## NDK

<h2 id="3ae6be565f1e33e90e0b11f768de1f6c"></h2>

### Android.mk

- jni/**Android.mk**
- describes your sources and shared libraries to the build system 
- tiny GNU makefile fragment 
- defining project-wide settings that Application.mk, the build system, and your environment variables leave undefined. It can also override project-wide settings for specific modules
- allows you to group your sources into modules. 
    - A module is either a *static library*, a *shared library*, or a *standalone executable*
- can define one or more modules in each **Android.mk** file
 

<h2 id="bbc9105ee8508ce6e083a589a351e83a"></h2>

#### Basics

- **LOCAL_PATH**
    - Android.mk file must begin by defining the LOCAL_PATH :
    - `LOCAL_PATH := $(call my-dir)`
    - macro `my-dir` returns the the directory containing the Android.mk file itself
- **CLEAR_VARS**
    - `include $(CLEAR_VARS)`
    - CLEAR_VARS 指向一个特殊的 GNU Makefile (.mk), 这个 mk文件可以帮你 clear many LOCAL_XXX variables for you, such as LOCAL_MODULE, LOCAL_SRC_FILES, and LOCAL_STATIC_LIBRARIES, but not LOCAL_PATH. 
- **LOCAL_MODULE**
    - `LOCAL_MODULE := hello-jni`  -> libhello-jni.so
- **LOCAL_SRC_FILES**
    - `LOCAL_SRC_FILES := hello-jni.c`
    - LOCAL_SRC_FILES contain a list of C and/or C++ source files
- **BUILD_SHARED_LIBRARY**
    - `include $(BUILD_SHARED_LIBRARY)`
    - BUILD_SHARED_LIBRARY 指向一个 GNU makefile, 这个mk文件帮助你 collects all the information you defined in LOCAL_XXX variables.

<h2 id="71d8a20d51b4fd098e224bbceafe5e3e"></h2>

#### Variables and Macros

你可以自定义变量,但不要使用 NDK系统保留字, 推荐使用 MY_XXX 格式

NDK 保留字:

- Names that begin with LOCAL_, such as `LOCAL_MODULE`
- Names that begin with PRIVATE_, NDK_, or APP.
- Lower-case names, such as my-dir.


<h2 id="34a0ad7ce398db363c3bea74d3bf8158"></h2>

#### NDK-defined variables

- **CLEAR_VARS**
    - `include $(CLEAR_VARS)`
    - undefines nearly all LOCAL_XXX variables 
- **BUILD_SHARED_LIBRARY**
    - `include $(BUILD_SHARED_LIBRARY)`
    - collects all the information you defined in LOCAL_XXX variables
    - LOCAL_MODULE and LOCAL_SRC_FILES must have been defined
    - .so extension
- **BUILD_STATIC_LIBRARY**
    - `include $(BUILD_STATIC_LIBRARY)`
    - .a extension
- **PREBUILT_SHARED_LIBRARY**
    - specify a prebuilt shared library
    - LOCAL_SRC_FILES must be a single path to a prebuilt shared library, eg. `foo/libfoo.so`
    - You can also reference a prebuilt library in another module by using the LOCAL_PREBUILTS variable
- **PREBUILT_STATIC_LIBRARY**
- **TARGET_ARCH**
- **TARGET_PLATFORM**
- **TARGET_ARCH_ABI**
- **TARGET_ABI**

---

<h2 id="f1f83bbb1daf12a9ecb64594df31a8be"></h2>

#### Module-Description Variables

The variables in this section describe your module to the build system, and shoud follow the basic flow:

 1. Initialize or undefine the variables associated with the module, using the CLEAR_VARS variable.
 2. Assign values to the variables used to describe the module.
 3. Set the NDK build system to use the appropriate build script for the module, using the BUILD_XXX variable.

Variables:

- **LOCAL_PATH**
    - give the path of the current file
    - define it at the start of your Android.mk file
    - `LOCAL_PATH := $(call my-dir)`
- **LOCAL_MODULE**
    - set name of your module 
    - `LOCAL_MODULE := "foo"`
- **LOCAL_MODULE_FILENAME**
    - optional variable to override the names that the build system uses by default
    - `LOCAL_MODULE_FILENAME := libnewfoo`
    - You cannot override filepath or file extension.
- **LOCAL_SRC_FILES**
- **LOCAL_CPP_EXTENSION**
    - optional variable to indicate a file extension other than .cpp for your C++ source files
    - `LOCAL_CPP_EXTENSION := .cxx .cpp .cc`
- **LOCAL_CPP_FEATURES**
    - optional variable to indicate that your code relies on specific C++ features
    - for prebuilt binaries, this variable also declares which features the binary depends on
    - recommend to use this variable instead of enabling -frtti and -fexceptions directly in LOCAL_CPPFLAGS definition.
    - LOCAL_CPP_FEATURES is for each module, whiel LOCAL_CPPFLAGS is for all modules
    - `LOCAL_CPP_FEATURES := rtti features`
- **LOCAL_C_INCLUDES**
    - optional variable to specify a list of include search path
    - `LOCAL_C_INCLUDES := $(LOCAL_PATH)//foo`
    - define before LOCAL_CFLAGS or LOCAL_CPPFLAGS
- **LOCAL_CFLAGS**
    - optional variable sets compiler flags
    - `LOCAL_CFLAGS += -I<path>,`
- **LOCAL_CPPFLAGS** ?
- **LOCAL_STATIC_LIBRARIES**
    - stores the list of static libraries modules on which the current module depends
- **LOCAL_SHARED_LIBRARIES**
- **LOCAL_WHOLE_STATIC_LIBRARIES**
    - 变体
    - useful when there are circular dependencies among several static libraries
- **LOCAL_LDLIBS**
    - 编译模块时要使用的附加的链接器选项
    - example tells the linker to generate a module that links to /system/lib/libz.so at load time:
    - `LOCAL_LDLIBS := -lz` 
- **LOCAL_LDFLAGS**
    - example uses the ld.bfd linker on ARM/X86 GCC 4.6+, on which ld.gold is the default
    - `LOCAL_LDFLAGS += -fuse-ld=bfd`
- **LOCAL_ALLOW_UNDEFINED_SYMBOLS**
    - undefined reference will throw error when building shared library
    - undefined reference will generate warnning when building static library
- **LOCAL_ARM_MODE**
    - 默认情况下，arm目标二进制会以 thumb 的形式生成(16位)，
    - 你可以通过设置这个变量为 arm如果你希望你的 module 是以 32 位指令的形式
    - `LOCAL_ARM_MODE := arm`
    - `LOCAL_SRC_FILES := foo.c bar.c.arm` will build bar.c always in arm mode


<h2 id="23475e2848e87691b2297b77ec135d34"></h2>

#### NDK-provided function macros
    
Use `$(call <function>)` to evaluate **function macros**; 

they return textual information. 

- my-dir
    - `LOCAL_PATH := $(call my-dir)`
    - this macro really returns is the path of the last makefile, so `include $(LOCAL_PATH)/foo/Android.mk` will influence next `LOCAL_PATH := $(call my-dir)` call
- all-subdir-makefiles
- this-makefile 
    - Returns the path of the current makefile
- parent-makefile , grand-parent-makefile
- import-module
    - A function that allows you to find and include a module's Android.mk file by the name of the module 
    - `$(call import-module,<name>)`

<h2 id="8e3060573a2bb39017e391f1f7ec4997"></h2>

### Application.mk

- **APP_OPTIM**
    - Define this optional variable as either release(default) or debug
    - Declaring **android:debuggable** in your application manifest's `<application>` tag will cause this variable to default to debug instead of release
- **APP_CFLAGS**
- **APP_CPPFLAGS**
- **APP_LDFLAGS**
- **APP_ABI**
    - `APP_ABI := armeabi armeabi-v7a x86 mips` 
- **APP_PLATFORM**
- **APP_STL**
    - by default, the NDK build system provides C++ headers for the minimal C++ runtime library (system/lib/libstdc++.so) provided by the Android system


<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

## Misc

<h2 id="169abc368db1ed3b7ced23a4f442cb7b"></h2>

### 获取 android id

```
adb shell settings get secure android_id
```


<h2 id="83dc2a583afc95dfd2221b8220e16748"></h2>

### 获取 mac address

```
adb shell cat /sys/class/net/wlan0/address  
```

<h2 id="cf00f742bf3ddb4dbebe6f4dbd32f96c"></h2>

### unity android get Current Application context

```
using(AndroidJavaClass activityClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer")) {
    AndroidJavaObject activityContext = activityClass.GetStatic<AndroidJavaObject>("currentActivity");

    AndroidJavaClass cls = new AndroidJavaClass( "com.usft.jdc_androidtools.androidtools" );
    cls.CallStatic("setContext", activityContext );
    cls.Dispose ();
}
```

<h2 id="29701a188748cb389ef5d6db4b65d70d"></h2>

### jar 打包

```
jar cvfM test.jar -C build/intermediates/classes/release/ com/usft
```

- 将 build/intermediates/classes/release/ 目录下的com/xxxx 子目录，文件打包成 test.jar 
- M : 不创建 manifest 文件
- -C : 指定root目录，这些目录层级不会被打包进jar , com/usft 目录层级会被打包

---
