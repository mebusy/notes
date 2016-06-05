# Unity - Android

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

## Unity Remove 4

Remote Setting:  Menu Edit > Project Settings > Editor
    
## Inside the Android Build Process

When building the app to the Android, be sure that the device has the ***“USB Debugging” and the “Allow mock locations”*** checkboxes checked in the device settings.

![](http://docs.unity3d.com/uploads/Main/android-device-dev.png)

You can ensure that the operating system sees your device by running `adb devices` command found in your Android SDK/platform-tools folder. This should work both for Mac and Windows.

```bash
$ adb devices
List of devices attached
08e9f72c	device
```

### Texture Compression

By default, Unity uses **ETC1/RGBA16** texture format for textures that don’t have individual texture format overrides (see Texture 2D / Per-Platform Overrides).


### Features currently not supported by Unity Android

 - Graphics
    - Non-square textures are not supported by the ETC format.
    - Movie Textures are not supported, use a full-screen streaming playback instead
 - Scripting
    - Dynamic features like **Duck Typing** are not supported. Use #pragma strict for your scripts to force the compiler to report dynamic features as errors.
        - dynamic key word so that 不使用继承的情况下使用了多态 ??? 
    - Video streaming via WWW class is not supported


### Android Scripting

macro : `UNITY_ANDROID`

#### Advanced Unity Mobile Scripting

 - Device Properties
    - SystemInfo.deviceUniqueIdentifier
    - SystemInfo.deviceName
    - SystemInfo.deviceModel 
    - SystemInfo.operatingSystem.
 - Anti-Piracy Check
    - You can check if your application is genuine (not-hacked) with the Application.genuine property

---

### Building Plugins for Android

#### Native Plugin

To build a plugin for Android, you should first obtain the ***Android NDK*** and familiarize yourself with the steps involved in building a **shared library**.

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

####  Deployment

For specific Android platform (armv7, x86), the libraries (lib*.so) should be placed in the following:

 - Assets/Plugins/Android/libs/x86/
 - Assets/Plugins/Android/libs/armeabi-v7a/

#### Using Java Plugins

The Android plugin mechanism also allows Java to be used to enable interaction with the Android OS.

A .jar file containing the .class files for your plugin

 - Unity expects Java plugins to be built using JDK v1
    - `-source 1.6 -target 1.6`


##### Using Your Java Plugin from Native Code

 1. copy .jar into Assets->Plugins->Android
 2. Unity will package your .class files together with the rest of the Java code and then access the code using JNI.


## Android SDK

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

## NDK

### Android.mk

 - jni/**Android.mk**
 - describes your sources and shared libraries to the build system 
 - tiny GNU makefile fragment 
 - defining project-wide settings that Application.mk, the build system, and your environment variables leave undefined. It can also override project-wide settings for specific modules
 - allows you to group your sources into modules. 
    - A module is either a *static library*, a *shared library*, or a *standalone executable*
 - can define one or more modules in each **Android.mk** file
 

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

#### Variables and Macros

你可以自定义变量,但不要使用 NDK系统保留字, 推荐使用 MY_XXX 格式

NDK 保留字:

 - Names that begin with LOCAL_, such as `LOCAL_MODULE`
 - Names that begin with PRIVATE_, NDK_, or APP.
 - Lower-case names, such as my-dir.


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

### Application.mk

 - **APP_OPTIM**
    - Define this optional variable as either release(default) or debug
    - Declaring **android:debuggable** in your application manifest's <application> tag will cause this variable to default to debug instead of release
 - **APP_CFLAGS**
 - **APP_CPPFLAGS**
 - **APP_LDFLAGS**
 - **APP_ABI**
    - `APP_ABI := armeabi armeabi-v7a x86 mips` 
 - **APP_PLATFORM**
 - **APP_STL**
    - by default, the NDK build system provides C++ headers for the minimal C++ runtime library (system/lib/libstdc++.so) provided by the Android system


## Misc

### 获取 android id

```
adb shell settings get secure android_id
```


### 获取 mac address

```
adb shell cat /sys/class/net/wlan0/address  
```

### android get Current Application

```
public static Application getApplicationUsingReflection() throws Exception {
    return (Application) Class.forName("android.app.ActivityThread")
            .getMethod("currentApplication").invoke(null, (Object[]) null);
}
```

### jar 打包

```
jar cvfM test.jar -C build/intermediates/classes/release/ com/ubisoft
```

 - 将 build/intermediates/classes/release/ 目录下的com/ubisoft子目录，文件打包成 test.jar 
 - M : 不创建 manifest 文件
 - -C : 指定root目录，这些目录层级不会被打包进jar , com/ubisoft 目录层级会被打包

---
