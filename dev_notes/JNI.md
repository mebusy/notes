...menustart

- [JNI](#4ceb3f5b846fa736acaada4c2f37a419)
    - [JNI type](#3c0039dc7d45a744d2c9b232978cb819)
    - [JNI字段描述符](#bf35fd3a3fda4957619c07f85f036dd0)
    - [Get JavaVM](#c9c0d7e93e0fa367c4a2bdbcddad831d)
    - [Call JNI methods in Thread](#fa15bc9805662c14849ccf40909ac09c)
    - [Get JNIEnv in threads](#f07f47bc6f6a26bc270b1e488aec9251)
    - [FindClass in threads](#f102c7b4bc313edc56ef03574977c9c4)
    - [JNI call methods](#f86c3261eb610e6b5e421d813e16328c)
    - [Dump local reference table](#52f4967c772459b9a729c2451e425db8)
    - [JNI 中的引用](#555f3c5d95f6b94b6620e775945dd341)

...menuend


<h2 id="4ceb3f5b846fa736acaada4c2f37a419"></h2>


# JNI

<h2 id="3c0039dc7d45a744d2c9b232978cb819"></h2>


## JNI type

```
jboolean，jbyte，jchar，jshort，jint，jlong，jfloat，jdouble
```

<h2 id="bf35fd3a3fda4957619c07f85f036dd0"></h2>


## JNI字段描述符

“([Ljava/lang/String;)V” 它是一种对函数返回值和参数的编码。

这种编码叫做JNI字段描述符（JavaNative Interface FieldDescriptors)。

一个数组int[]，就需要表示为这样`"[I"`。

如果多个数组double[][][]就需要表示为这样 `"[[[D"`。

也就是说每一个方括号开始，就表示一个数组维数。多个方框后面，就是数组 的类型。

如果以一个L开头的描述符，就是类描述符，它后紧跟着类的字符串，然后分号";"结束。

比如:

- "Ljava/lang/String;" -- `String`
- "[I"  --  `int[]`
- "[Ljava/lang/Object;" --  `Object[]`

***JNI方法描述符，主要就是在括号里放置参数，在括号后面放置返回类型***

如下：

- "()Ljava/lang/String;" --  `String f()` ;
- "(ILjava/lang/Class;)J" -- `long f(int i, Class c)`;
- "([B)V"  --  `void String(byte[] bytes)`;
- "(II)V" -- void Func(int, int);


Java 类型 |  符号
-- | -- 
Boolean      |          Z
Byte         |       B
Char       |        C
Short      |          S
Int         |       I
Long       |         J
Float        |        F
Double       |         D
Void         |       V


objects  对象   以"L"开头，以";"结尾，中间是用"/"隔开的包及类名。

比如：`Ljava/lang/String`; 

如果是嵌套类，则用$来表示嵌套。例如 `"(Ljava/lang/String;Landroid/os/FileUtils$FileStatus;)Z"`



<h2 id="c9c0d7e93e0fa367c4a2bdbcddad831d"></h2>


## Get JavaVM

```c
jint JNI_OnLoad(JavaVM* vm, void* reserved) {
    ...
}
```

JNI_OnLoad will be invoked when library was loaded


<h2 id="fa15bc9805662c14849ccf40909ac09c"></h2>


## Call JNI methods in Thread
 1. 线程中调用的JNI 方法，不要试图去保存它们的值
    - The JNI method arg is a local reference and used only in this thread or the JNI method
    - That is, you can't keep **JNIEnv** value for futhure using in threads, but you can keep **JavaVM** to use in threads
 2. To call JNI method in thread , you should:
    - attach the **JavaVM** to thread , so that to get the **JNIEnv**
    - use that **JNIEnv** for JNI methods invoking
    - call JNI method as you want
    - detach **JavaVM** from thread


<h2 id="f07f47bc6f6a26bc270b1e488aec9251"></h2>


## Get JNIEnv in threads

```c
JNIEnv* getJNIEnv( bool *isAttached ) {
    JavaVM* g_vm = pJavaVm ;
    JNIEnv * g_env;

    *isAttached = false ;
    // double check it's all ok
    int getEnvStat = g_vm->GetEnv(reinterpret_cast<void**>(&g_env), JNI_VERSION_1_6) ;
    if (getEnvStat == JNI_EDETACHED) {
        Debug( "Get Env: not attached" );
        if (g_vm->AttachCurrentThread((JNIEnv **)( &g_env ),NULL)!= 0){
            Debug(  "Failed to attach" ) ;
        } else {
            *isAttached = true; 
        }
    } else if (getEnvStat == JNI_OK) {
        //
    } else if (getEnvStat == JNI_EVERSION) {
        Debug( "Get Env: version not supported" ) ;
    }

    return g_env ;
}
```

Detach:

```c
void endJNICall(JNIEnv* g_env) {
    JavaVM* g_vm = pJavaVm ;

    g_vm->DetachCurrentThread();
    Debug( " vm detached in endJNICall" ) ;
}
```

<h2 id="f102c7b4bc313edc56ef03574977c9c4"></h2>


## FindClass in threads

Q:Jni FindClass returns NULL in thread:

A: Basically this can occur if the thread where you ask FindClass is not the main thread and in your thread system does not build a map of java class IDs.

The following example code is to show how to use `ClassLoader` to find the target class. Further more, it use a global reference to keep the target class. 

```c

// used to find java class in any thread
static jobject gClassLoader;
static jmethodID gFindClassMethod;
static jclass  gClassJNI_Method ;

extern "C" {

    jint JNI_OnLoad(JavaVM* vm, void* reserved) {
        /*
      JNIEnv* jni_env = 0;
      vm->AttachCurrentThread(&jni_env, 0);

      jniEnv = jni_env ;
      /*/
      pJavaVm = vm ;

      bool isAttached = false ;
      JNIEnv* env = getJNIEnv( & isAttached );
      //replace with one of your classes in the line below

      const char* name = "com/ubi/androidmediadecode/JNI_Method" ;
      jclass randomClass = env->FindClass( name );
      jclass classClass = env->GetObjectClass(randomClass);
      jclass classLoaderClass = env->FindClass("java/lang/ClassLoader");
      
      jmethodID getClassLoaderMethod = env->GetMethodID(classClass, "getClassLoader", "()Ljava/lang/ClassLoader;");
      gClassLoader =  (jclass)env->NewGlobalRef( env->CallObjectMethod(randomClass, getClassLoaderMethod) ) ;
      if (env->ExceptionCheck()) {
          env->ExceptionDescribe();
      }

      gFindClassMethod = env->GetMethodID(classLoaderClass, "findClass","(Ljava/lang/String;)Ljava/lang/Class;");     


      jstring jstr =(*env).NewStringUTF( name );
      jclass cls = (jclass)((*env).CallObjectMethod( gClassLoader, gFindClassMethod, jstr )); 
      (*env).DeleteLocalRef(  jstr );

      gClassJNI_Method = (jclass)env->NewGlobalRef( cls ) ;
      
      (*env).DeleteLocalRef(  cls );
      (*env).DeleteLocalRef(  randomClass );
      (*env).DeleteLocalRef(  classClass );
      (*env).DeleteLocalRef(  classLoaderClass );

      //*/
      __android_log_print(ANDROID_LOG_INFO, "JNIMsg", "JNI_OnLoad" );
      return JNI_VERSION_1_6;
    }

}
```

<h2 id="f86c3261eb610e6b5e421d813e16328c"></h2>


## JNI call methods

call by the return type , eg:

```
CallStaticBooleanMethod
CallStaticByteMethod
CallStaticCharMethod
CallStaticDoubleMethod
CallStaticFloatMethod
CallStaticIntMethod
CallStaticLongMethod
CallStaticObjectMethod
CallStaticShortMethod
CallStaticStringMethod
CallStaticVoidMethod
```

```c
bool JNI_startupBink(char* filename) {
    bool isAttached = false ;
    JNIEnv* jniEnv  = getJNIEnv( &isAttached );

    jclass cls = JNI_findJavaClass(jniEnv) ;
    jmethodID method = (*jniEnv).GetStaticMethodID(  cls, "startupBink","(Ljava/lang/String;)Z"  ); 

    jstring jstr =(*jniEnv).NewStringUTF( filename );
    jboolean result=(*jniEnv).CallStaticBooleanMethod(cls,method,jstr);
    bool bRes = (bool)(result) ;
    (*jniEnv).DeleteLocalRef(  jstr );
    if (isAttached) endJNICall(jniEnv);

    return bRes;
}
```

Call a java function which returned an array , don't forget to invoke  `ReleaseByteArrayElements` method:

```c
    bool isAttached = false ;
    JNIEnv* jniEnv  = getJNIEnv( &isAttached );

    jclass cls = JNI_findJavaClass(jniEnv) ;
    jmethodID method = (*jniEnv).GetStaticMethodID(  cls,  "getDecodeData", "()[B" ); 
    jbyteArray retval = (jbyteArray)(*jniEnv).CallStaticObjectMethod(cls, method);
    
    jbyte * jbytes=  (*jniEnv).GetByteArrayElements(retval, 0);  

    int size = (*jniEnv).GetArrayLength(retval);  
    char* outData = (char*)jbytes ;
    
    ...
    
    (*jniEnv).ReleaseByteArrayElements( retval, jbytes ,0 );
    (*jniEnv).DeleteLocalRef(retval);
    if (isAttached) endJNICall(jniEnv);    
```


<h2 id="52f4967c772459b9a729c2451e425db8"></h2>


## Dump local reference table

You many got crash if the local reference table overflow, so it's useful to dump the info of "local reference table"

```c
jclass vm_class = env->FindClass("dalvik/system/VMDebug");
jmethodID dump_mid = env->GetStaticMethodID( vm_class, "dumpReferenceTables", "()V" );
env->CallStaticVoidMethod( vm_class, dump_mid );
```


<h2 id="555f3c5d95f6b94b6620e775945dd341"></h2>


## JNI 中的引用

在JNI规范中定义了三种引用：

- 局部引用（Local Reference)
    - 通过NewLocalRef和各种JNI接口创建（FindClass、NewObject、GetObjectClass 和 NewCharArray 等）。
    - 会阻止GC回收所引用的对象，不在本地函数中跨函数使用，不能跨线程使用。
    - 函数返回后局部引用所引用的对象会被JVM自动释放，或调用DeleteLocalRef释放。`(*env)->DeleteLocalRef(env,local_ref)`
    - 如果返回的是对象，eg. jclass, jstring, 务必 DeleteLocalRef 删除, 以避免 local reference table overflow
- 全局引用（Global Reference）
    - 用NewGlobalRef基于局部引用创建，会阻GC回收所引用的对象。可以跨方法、跨线程使用。
    - JVM不会自动释放，必须调用DeleteGlobalRef手动释放`(*env)->DeleteGlobalRef(env,g_cls_string);` 
- 弱全局引用（Weak Global Reference） 
    - 调用NewWeakGlobalRef基于局部引用或全局引用创建，
    - 不会阻止GC回收所引用的对象，可以跨方法、跨线程使用。
    - 引用不会自动释放，在JVM认为应该回收它的时候（比如内存紧张的时候）进行回收而被释放。或调用DeleteWeakGlobalRef手动释放。`(*env)->DeleteWeakGlobalRef(env,g_cls_string)`
        
