[](...menustart)

- [unity C# 加密](#59079838bd54368031bb73b3999b5964)
    - [准备工作](#88210852e6553d4dd59f3c922ba608d0)
    - [编译](#984612f0e7ba26ecc8da6bd7c8759d28)
    - [加密](#56563edf23b9d717dc63981b8836fc60)
    - [解密](#1872008289c5e25292fe34cb024b7d9e)
    - [编译Windows平台mono.dll](#a54996b33b6ee1054017744535d1612e)

[](...menuend)


[TOC]

<h2 id="59079838bd54368031bb73b3999b5964"></h2>

# unity C# 加密

<h2 id="88210852e6553d4dd59f3c922ba608d0"></h2>

## 准备工作

 1. unity mono branch 源码
    - [mono](https://github.com/Unity-Technologies/mono/)
 2. Android NDK 
    - 查看所需ndk版本
        - 在你下载的源码工程中查看`external/buildscripts/build_runtime_android.sh`
        - 有下面类似的一句 `perl ${BUILDSCRIPTSDIR}/PrepareAndroidSDK.pl -ndk=r9 -env=envsetup.sh && source envsetup.sh` 
        - 其中 -ndk 的内容 就是所就是所需的NDK版本号。去下载即可. 

    - 配置 android NDK 环境变量
    
```
NDK_ROOT=/path/2/android-ndk-r10e
NDK=$NDK_ROOT 
ANDROID_NDK_ROOT=$NDK_ROOT 
export NDK_ROOT NDK ANDROID_NDK_ROOT 
```

<h2 id="984612f0e7ba26ecc8da6bd7c8759d28"></h2>

## 编译


1. brew install autoconf automake pkg-config 这些工具
    - el captain 自带 libtool, 如果 自带的 libtool编译出错，brew install libtool 
    - brew 可能不会把 libtool装到 /usr/local/bin上，导致 libtool 相关出错，把 brew libtool 连接到 /usr/local/bin

2. pl 脚本会使用 git 协议下载 krait-signal-handler.git, 如果使用 proxy的话, 可能会下载不到，可以预先下载好
    - cd external
    - `git clone https://github.com/Unity-Technologies/krait-signal-handler.git android_krait_signal_handler`
3. 替换 老旧文件:  android_krait_signal_handler/PrepareAndroidSDK.pm
    - `cp buildscripts/PrepareAndroidSDK.pm android_krait_signal_handler/PrepareAndroidSDK.pm` 

4. pl 脚本会 `use lib ("./perl_lib");` , 但是相对路径比较混乱，把mono 根目录下的 perl_lib 目录分别拷贝一份到  android_krait_signal_handler 和 buildscripts 目录下
5. 修改 external/android_krait_signal_handler/jni/Application.mk
    - clang3.3 改为 clang3.6 
    - `NDK_TOOLCHAIN_VERSION := clang3.6`
    - 看具体情况 NDK r10e 因为已经没有 clang3.3了，所以需要改成 NDK r10e 有的 clang3.6

6. 修改 external/android_krait_signal_handler/jni/build.pl
    - PrepareAndroidSDK::GetAndroidSDK(undef, undef, "r10e"); 

7. Terminal cd到mono根目录下，执行
    - `sh external/buildscripts/build_runtime_android.sh` 
8. 编译 release版本
    - build_runtime_android.sh 和 build_runtime_android_x86.sh
        - 去掉 `-fpic -g` 后面的 `-g`
        - `-g` 替换成 `-O2` 生成的 .so 会小点


<h2 id="56563edf23b9d717dc63981b8836fc60"></h2>

## 加密

- 加密 `assets/bin/Data/Managed/Assembly-CSharp.dll`

<h2 id="1872008289c5e25292fe34cb024b7d9e"></h2>

## 解密

- `mono/metadata/image.c`  文件
- `mono_image_open_from_data_with_name` 方法

```
MonoCLIImageInfo *iinfo;
MonoImage *image;
char *datac;

// start decrypt
if(name != NULL)
{
    if(strstr(name,"Assembly-CSharp.dll")){
        // TODO decrypt
    }
}
// end decrypt


if (!data || !data_len) {
    if (status)
        *status = MONO_IMAGE_IMAGE_INVALID;
    return NULL;
}
```
   

<h2 id="a54996b33b6ee1054017744535d1612e"></h2>

## 编译Windows平台mono.dll

 1. 打开Visual Studio Command Prompt(2010)
    - 这会编译出win32的 dll
    - 编译 x64版本dll, 使用 x64 Command Prompt 
 2. 进入mono-unity-4.5\msvc目录
 3. 执行`msbuild.exe mono.sln /p:Configuration=Release_eglib`
    - 注意：直接打开mono.sln解决方案，在Visual Studio底下是编译不了的。

