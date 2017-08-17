
# KBEngine 

# Install 

 1. kbengine/kbe/tools/server/install/installer.py 修改
    - line 548 : `"~"` -> `os.path.expanduser("~")`
    - line 555 : add `import os` before `if os.geteuid() > 0: ` 
 2. for virtual machine 
    - /sbin/ip route add broadcast 255.255.255.255 dev lo
 3. setting mysql before install
    - when run installer.py , choose remote mysql server , to skip mysql service checking 

# Misc

 1. assets/res/server/kbengine.xml , 关闭 自动创建账号
 

# Login System
 - baseApp
    - set server info

```cs
public class clientApp : KBEMain {
    void Awake() {
        this.ip = "10.192.93.63";
    }
}
```

 - Event
    - onConnectionState
    - onLoginFailed
 - login to server
    - `KBEngine.Event.fireIn( "login" , userName.text , password.text , System.Text.Encoding.UTF8.GetBytes( "this info is from client" ) );`
 - to receive callbacks

```cs
# register built-in event
KBEngine.Event.registerOut( "onConnectionState" , this , "onConnectionState");
KBEngine.Event.registerOut ("onLoginFailed", this, "onLoginFailed");
...
//==== callbacks =============
public void onConnectionState( bool status  ) {
    if (!status)
        print ("connect failed");
    else 
        print ( "connect successfully" );
}

public void onLoginFailed ( UInt16 s ) {
    print (s);
    if (s == 20 )
        print ("login failed " +  System.Text.Encoding.ASCII.GetString( KBEngineApp.app.serverdatas () ) );
    else
        print ("login failed " +  KBEngineApp.app.serverErr(s));
}
```

 - after login successfully , kbengine will instantialzie an `Account` instance 
    - and `__init__()` method will called 
    - you can fireOut your custom event in `__init__()` method

```cs
public class Account : Entity {
    public override void __init__() {
        KBEngine.Event.fireOut( "onLoginSuccessfully", new object[]{KBEngineApp.app.entity_uuid, id, this} );
    }
}
``` 

```cs
// on other cs file
KBEngine.Event.registerOut ("onLoginSuccessfully", this, "onLoginSuccessfully");
...
public void onLoginSuccessfully( UInt64 uuid, Int32 id, Account account ) {
    if (account != null) {
        print ("LoginSuccessfully" + uuid );
        Application.LoadLevel("02");
    }
}
```

---

# Say hello to server 

## server side 

 - modify `scripts/entity_defs/Account.def` 

```
<BaseMethods>     
    <reqHello>
        <Exposed/>
    </reqHello> 
</BaseMethods>  
```
this means client can use `baseCall` to call server method `reqHello`

```
<ClientMethods>             
    <onHello>  
        <Arg> UNICODE </Arg>
    </onHello>>      
</ClientMethods>     
```

this means server can call client method "onHello"


 - modify `scripts/base/Account.py` , add method `reqHello`

```python
def reqHello(self):            
    self.client.onHello( "欢迎!" )  
```

## client side 

 - Entity class has `baseCall` method 
 - In your `Account` class, invode `caseCall`  to call server method , eg, `reqHello` method 
    - tips: you can use `Account account = (Account)KBEngineApp.app.player () ;` to get Account instance.

```cs
public void reqHello() {
    // we do it on base , client call server method ?
    baseCall("reqHello");
}
```

 - and define a callback methods with same name as server called 

```cs
//==== callbacks ===================
public void onHello(string data) {
    KBEngine.Event.fireOut ("onHello", new object[] { data });
}
```

---

# Avatar List

 - avatar property
    - name
    - roleType
    - level 
 - list data struct 
    - `{value: [ { "name":xx, "roleType":xxx, "level":xx } , {...} , {...} ] }`
 - we need add *Avatar* entity 
    
## Register Entity

 - modify `scripts/entities.xml`
    - add `<Avatar hasClient="true"></Avatar>`
 - define Avatar entity
    - create new Avatar.def under `scripts/entity_defs/`
    - add properties

```cs
<Properties>                  
    <name>                    
        <Type> UNICODE </Type>              
        <Flags> ALL_CLIENTS </Flags>
        <Persistent> true </Persistent>
    </name>                   
    <roleType>                
        <Type> UINT8 </Type>  
        <Flags> BASE </Flags> 
        <Persistent> true </Persistent>
    </roleType>               
    <level>                   
        <Type> UINT16 </Type> 
        <Flags> CELL_PUBLIC_AND_OWN </Flags>
        <Persistent> true </Persistent>
    </level>                  
</Properties>                 
```

 - create base Avatar script
    - create new Avatar.py under `scripts/base/`

```python
# -*- coding: utf-8 -*-               
import KBEngine        
from KBEDebug import * 
                       
class Avatar(KBEngine.Proxy):
    def __init__(self):     
        KBEngine.Proxy.__init__(self)
```

 - create cell Avatar scrpit (if needed)
    - create new Avatar.py under `scripts/cell/`


```python
# -*- coding: utf-8 -*-               
import KBEngine        
from KBEDebug import * 
                       
class Avatar(KBEngine.Entity):
    def __init__(self):     
        KBEngine.Entity.__init__(self)
```





