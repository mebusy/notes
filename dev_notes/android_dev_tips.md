
# android dev tips

## TextEdit remove the restrict by android::digits

```java
EditText text = (EditText)mLayout.findViewById(R.id.exchange_input);
text.setKeyListener( new EditText( this.context ).getKeyListener() ) ;
text.setInputType(InputType.TYPE_CLASS_TEXT );
```

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

## whole-archieve prebuilt static library

 - use LOCAL_WHOLE_STATIC_LIBRARIES  instead of LOCAL_STATIC_LIBRARIES


