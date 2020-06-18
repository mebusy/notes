...menustart

 - [android dev tips](#cedbb586db72ab93a1b4a11759bb2790)
     - [TextEdit remove the restrict by android::digits](#e0c06a36076f5a0639f1c587a1072b0b)
     - [TextEdit add input filter](#8d305b8ceb34e7bb075ba809c621ba63)
     - [open browser](#36f510971eecdc6dcd92048cb126f598)
     - [whole-archieve prebuilt static library](#55322a5875714b1c278ba95d4d7dca27)
     - [whether is Main thread ?](#a8113f0e4f0db0e8f7a49b9697196e90)
     - [prevent background app auto close](#0f4a700a11434bbd0f28da36dc2ab2e7)
     - [run on working thread](#56b786df876f856f3bdbf37f4eca6a40)

...menuend


<h2 id="cedbb586db72ab93a1b4a11759bb2790"></h2>


# android dev tips

<h2 id="e0c06a36076f5a0639f1c587a1072b0b"></h2>


## TextEdit remove the restrict by android::digits

```java
EditText text = (EditText)mLayout.findViewById(R.id.exchange_input);
text.setKeyListener( new EditText( this.context ).getKeyListener() ) ;
text.setInputType(InputType.TYPE_CLASS_TEXT );
```

<h2 id="8d305b8ceb34e7bb075ba809c621ba63"></h2>


## TextEdit add input filter

```java
EditText text = (EditText)mLayout.findViewById(R.id.exchange_input);
text.addTextChangedListener(new LimitInputTextWatcher(text));
```

```java
import android.text.Editable;
import android.text.TextWatcher;
import android.widget.EditText;

import java.util.HashMap;
import java.lang.StringBuilder ;


public class LimitInputTextWatcher implements TextWatcher {
    /**
     * et
     */
    private EditText et = null;

    /**
     * 构造方法
     *
     * @param et
     */
    public LimitInputTextWatcher(EditText et) {
        this.et = et;
        makeCharLimit() ;
    }


    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void afterTextChanged(Editable editable) {
        String str = editable.toString();
        String inputStr = filterString( str );
        et.removeTextChangedListener(this);
        // et.setText方法可能会引起键盘变化,所以用editable.replace来显示内容
        editable.replace(0, editable.length(), inputStr.trim());
        et.addTextChangedListener(this);

    }

    // TODO
    String allChars = ... // filter strings

    HashMap<String, Integer> hmap_allChars = new HashMap<String , Integer>();
    void makeCharLimit() {
        int nStr = allChars.length() ;
        for ( int i = 0 ; i< nStr ; i++ ) {
            String item = allChars.substring( i, i+1  ) ;
            hmap_allChars.put( item, 1 ) ; 
        } 
        // test 
        // for ( String key :  hmap_allChars.keySet() ) {
        //     System.out.println( key );   
        // }
    }
    
    
    StringBuilder sb = new StringBuilder () ;
    static final int MAXLENGTH = 8 ;
    String filterString( String testString  ) {
        sb.setLength(0);
        int nStr = testString.length() ;
        for ( int i = 0 ; i< nStr ; i++ ) {
            String sub = testString.substring( i, i+1  ) ;
            // System.out.println( sub );
            if ( hmap_allChars.containsKey( sub )  ) {
                sb.append( sub ) ;
                if(sb.length() >= MAXLENGTH ) break ;
            }
        } 
        return sb.toString() ;
    }

}
```

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

<h2 id="56b786df876f856f3bdbf37f4eca6a40"></h2>


## run on working thread

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

/**
 * This class provides basic/common functionalities to be applied on Java Objects.
 */
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
}
```




