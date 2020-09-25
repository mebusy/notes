...menustart

- [android dev tips](#cedbb586db72ab93a1b4a11759bb2790)
    - [open browser](#36f510971eecdc6dcd92048cb126f598)
    - [whole-archieve prebuilt static library](#55322a5875714b1c278ba95d4d7dca27)
    - [whether is Main thread ?](#a8113f0e4f0db0e8f7a49b9697196e90)
    - [prevent background app auto close](#0f4a700a11434bbd0f28da36dc2ab2e7)
    - [Run on UI thread](#54caf15a8a382279ea87b2993c32b19d)
    - [run on working thread](#56b786df876f856f3bdbf37f4eca6a40)
    - [Using Gson](#27936d606faa31b6312be4d40984af57)
    - [AsyncTask](#97f8fab067a9df19dd2e8b75c5989fff)
    - [Update Eclipse project to ant](#64556a6168b58f000bc4bd5146c16844)
    - [MacOSX multiple Java version](#1346a911b293f1e15ae203e43f3af6b1)

...menuend


<h2 id="cedbb586db72ab93a1b4a11759bb2790"></h2>


# android dev tips



<h2 id="36f510971eecdc6dcd92048cb126f598"></h2>


## open browser

```java
import android.content.Intent ;
import android.net.Uri ;

public  static void openAppStore(  final String url ) {
    Intent viewIntent = new Intent(Intent.ACTION_VIEW,Uri.parse( url ));  
    // "android.intent.action.VIEW"
    mContext.startActivity(viewIntent);
}
```

<h2 id="55322a5875714b1c278ba95d4d7dca27"></h2>


## whole-archieve prebuilt static library

- use LOCAL_WHOLE_STATIC_LIBRARIES  instead of LOCAL_STATIC_LIBRARIES

<h2 id="a8113f0e4f0db0e8f7a49b9697196e90"></h2>


## whether is Main thread ?

```java
import android.os.Looper ;
public static boolean isMainThread() {
    return Looper.getMainLooper().getThread() == Thread.currentThread();
}
```


<h2 id="0f4a700a11434bbd0f28da36dc2ab2e7"></h2>


## prevent background app auto close

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // prevent auto restarting rather than resuming
        // on some android device
        if (!isTaskRoot()
                && getIntent().hasCategory(Intent.CATEGORY_LAUNCHER)
                && getIntent().getAction() != null
                && getIntent().getAction().equals(Intent.ACTION_MAIN)) {

            finish();
            return;
        }
        ...
```

<h2 id="54caf15a8a382279ea87b2993c32b19d"></h2>


## Run on UI thread

```java
	    mActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText( mActivity , str, Toast.LENGTH_SHORT ).show();
            }
        });
```

<h2 id="56b786df876f856f3bdbf37f4eca6a40"></h2>


## run on working thread

- more details : Cocos2dxHelper

```java
    private static Handler mWorkingHandler = null  ;
    private static Thread mWorkingThread = null;

    // should be initially called by working thread
    public static void setWorkingThread() {
        if ( mWorkingThread == null )
            mWorkingThread = Thread.currentThread(); 
    }
    public static void runOnWorkingThread( Runnable action ) {
        if ( mWorkingThread == null )
            return ;

        if ( mWorkingHandler == null ) {
            // Default constructor associates this handler with the Looper for the current thread.
            mWorkingHandler = new Handler() ;
        }

        if (Thread.currentThread() != mWorkingThread) {
             mWorkingHandler.post(action);
         } else {
             action.run();
         }

    }
```


<h2 id="27936d606faa31b6312be4d40984af57"></h2>


## Using Gson

[gson](https://github.com/google/gson)

in your app level build.gradle

```gradle
dependencies {
  implementation 'com.google.code.gson:gson:2.2.1'
}
```

using in your android project

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.util.HashMap;

/**
 * This class provides basic/common functionalities to be applied on Java Objects.
//*/
public final class ObjectUtils {

    private static final Gson GSON = new GsonBuilder().setPrettyPrinting().create();

    private ObjectUtils() {
         throw new UnsupportedOperationException("Instantiation of this class is not permitted in case you are using reflection.");
    }

    /**
     * This method is responsible for de-serializing the Java Object into Json String.
     *
     * @param object Object to be de-serialized.
     * @return String
     */
    public static String deserializeObjectToString(final Object object) {
        return GSON.toJson(object);
    }
    public static HashMap<String,Object> json2map( String json )  {
            HashMap<String,Object> map = new HashMap<String,Object>();
            map = (HashMap<String,Object>) GSON.fromJson(json, map.getClass());
            return map ;
    }
}
```

to use:

```java
import com.google.gson.internal.StringMap;
...

     HashMap<String,Object> map = ObjectUtils.json2map(  response.toString() );
    StringMap<String> ret_data = (StringMap<String>)map.get( "data" );
```

<h2 id="97f8fab067a9df19dd2e8b75c5989fff"></h2>


## AsyncTask

- This class was deprecated in API level 30.
- Use the standard java.util.concurrent or Kotlin concurrency utilities instead.


```java
 private class DownloadFilesTask extends AsyncTask<URL, Integer, Long> {
     // invoked on the UI thread before the task is executed. 
     // This step is normally used to setup the task, for instance by showing a progress bar in the user interface.
    protected void onPreExecute() {
        super.onPreExecute();
        Log.d(TAG + " PreExceute","On pre Exceute......");
    }

     // invoked on the background thread immediately after onPreExecute() finishes executing. 
     // The parameters of the asynchronous task are passed to this step.
     protected Long doInBackground(URL... urls) {
         int count = urls.length;
         long totalSize = 0;
         for (int i = 0; i < count; i++) {
             totalSize += Downloader.downloadFile(urls[i]);

             // This step can also use publishProgress(Progress...) to publish one or more units of progress. 
             // These values are published on the UI thread, in the onProgressUpdate(Progress...) step.
             publishProgress((int) ((i / (float) count) * 100));
             // Escape early if cancel() is called
             if (isCancelled()) break;
         }
         return totalSize;
     }

     protected void onProgressUpdate(Integer... progress) {
         // invoked on the UI thread after a call to publishProgress(Progress...).
         // This method is used to display any form of progress in the user interface while the background computation is still executing.
         setProgressPercent(progress[0]);
     }

     protected void onPostExecute(Long result) {
         // invoked on the UI thread after the background computation finishes.
         // The result of the background computation is passed to this step as a parameter.
         showDialog("Downloaded " + result + " bytes");
     }
 }
 
```

Once created, a task is executed very simply:

```java
 new DownloadFilesTask().execute(url1, url2, url3);
```

sometime you just want to do some simple test, and don't care about whether AsyncTask will freeze the UI thread ...

```java
TYPE ret = new DownloadFilesTask().execute(url1, url2, url3).get() ;
```


![](https://i.stack.imgur.com/ytin1.png)



<h2 id="64556a6168b58f000bc4bd5146c16844"></h2>


## Update Eclipse project to ant

```bash
android update project -p . -t android-23
ant debug
```


<h2 id="1346a911b293f1e15ae203e43f3af6b1"></h2>


## MacOSX multiple Java version

```bash
# 1 install java7
brew tap homebrew/cask-versions
brew cask install homebrew/cask-versions/zulu7
```

```bash
export JAVA_7_HOME=$(/usr/libexec/java_home -v1.7)
export JAVA_8_HOME=$(/usr/libexec/java_home -v1.8)
export JAVA_9_HOME=$(/usr/libexec/java_home -v9)

alias java7='export JAVA_HOME=$JAVA_7_HOME'
alias java8='export JAVA_HOME=$JAVA_8_HOME'
alias java9='export JAVA_HOME=$JAVA_9_HOME'

#default java8
export JAVA_HOME=$JAVA_8_HOME
```


## How to determine ABI of Android .so file 

```bash
# just for example, using NDK r20
$NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin/arm-linux-androideabi-readelf ../
```
