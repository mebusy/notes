...menustart

 - [KBEngine](#18cd2f733f76d1da621dab13f59c7272)
 - [Install](#349838fb1d851d3e2014b9fe39203275)
 - [Misc](#74248c725e00bf9fe04df4e35b249a19)
 - [Login System](#b65900167c5add9414d6f7a28eb639af)
 - [Say hello to server](#9a9a71efcb676c76eb1e51d60ae2cb31)
     - [server side](#d3ecf7a46680a0dd28cc7a616800e186)
     - [client side](#2f66c7f591948a0efcf4d4f44052b519)
 - [Avatar List](#26c985492cc3eb77b7d7e3333d30d1a1)
     - [Register Entity](#4451dbc15dd7b598f0579474e56e74a8)
     - [client](#62608e08adc29a8d6dbc9754e659f125)

...menuend


<h2 id="18cd2f733f76d1da621dab13f59c7272"></h2>

-----
-----

# KBEngine 

<h2 id="349838fb1d851d3e2014b9fe39203275"></h2>

-----
-----

# Install 

 1. kbengine/kbe/tools/server/install/installer.py 修改
    - line 548 : `"~"` -> `os.path.expanduser("~")`
    - line 555 : add `import os` before `if os.geteuid() > 0: ` 
 2. for virtual machine 
    - /sbin/ip route add broadcast 255.255.255.255 dev lo
 3. setting mysql before install
    - when run installer.py , choose remote mysql server , to skip mysql service checking 

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

-----
-----

# Misc

 1. assets/res/server/kbengine.xml , 关闭 自动创建账号
 

<h2 id="b65900167c5add9414d6f7a28eb639af"></h2>

-----
-----

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

<h2 id="9a9a71efcb676c76eb1e51d60ae2cb31"></h2>

-----
-----

# Say hello to server 

<h2 id="d3ecf7a46680a0dd28cc7a616800e186"></h2>

-----

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

<h2 id="2f66c7f591948a0efcf4d4f44052b519"></h2>

-----

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

<h2 id="26c985492cc3eb77b7d7e3333d30d1a1"></h2>

-----
-----

# Avatar List

 - avatar property
    - name
    - roleType
    - level 
 - list data struct 
    - `{value: [ { "name":xx, "roleType":xxx, "level":xx } , {...} , {...} ] }`
 - we need add *Avatar* entity 
    
<h2 id="4451dbc15dd7b598f0579474e56e74a8"></h2>

-----

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

--- 

 - define AVATAR list  data structure
    - `scripts/entity_defs/alias.xml`

```
<root>                                       
    <DBID> UINT64 </DBID>
 
    <AVATAR_INFO> FIXED_DICT
        <Properties>
            <dbid>
                <Type> DBID </Type>
            </dbid>
            <name>
                <Type> UNICODE </Type>
            </name>
            <roleType>
                <Type> UINT8 </Type>
            </roleType>
            <level>
                <Type> UINT16 </Type>
            </level>
        </Properties>
    </AVATAR_INFO>
    <AVATAR_INFO_LIST> FIXED_DICT
        <Properties>
            <value>
                <Type> ARRAY
                    <of> AVATAR_INFO  </of>
                </Type>
            </value>
        </Properties>
    </AVATAR_INFO_LIST>
</root>
```

 - now add above struct to Account.def
    - `scripts/entity_defs/Account.def`

```
<Properties>                             
    <characters>
        <Type> AVATAR_INFO_LIST </Type>
        <Flags> BASE </Flags>
        <Persistent> true </Persistent>  
    </characters>             
</Properties>  
```

 - now we define a method to create Avatar 

`scripts/entity_defs/Account.def`   

```
<onCreateAvatarResult>
    <Arg> UINT8 </Arg>
    <Arg> AVATAR_INFO </Arg>
</onCreateAvatarResult>

<reqCreateAvatar>    
    <Exposed/>       
    <Arg> UINT8 </Arg>
    <Arg> UNICODE </Arg>
</reqCreateAvatar>   
```

`scripts/base/Account.py `

```python
def reqCreateAvatar(self, roleType, name ):               
    # initialize Avatar entity properties
    props = {
        "name":name,
        "roleType":roleType,
        "level": 1     
    }    
         
    avatar = KBEngine.createBaseLocally( "Avatar" , props )
    if avatar is not None:
        avatar.writeToDB( self._onCharacterSaved )
         
def _onCharacterSaved( self, success , avatar ):
    if success:
        info = {
            "dbid": avatar.databaseID ,
            "name": avatar.cellData[ "name" ] ,
            "roleType": avatar.roleType,
            "level" :1 
        }
        # characters is defined in AVATAR_INFO_LIST
        self.characters["value"].append( info )
        self.writeToDB(  )
         
        avatar.destroy()
         
        # send to client
        self.client.onCreateAvatarResult( 0, info )

```

<h2 id="62608e08adc29a8d6dbc9754e659f125"></h2>

-----

## client 

```cs
public void reqCreateAvatar( int roleType, string name ) {
    baseCall ("reqCreateAvatar", new object[]{ roleType, name  });
}
public void onCreateAvatarResult( byte retcode , object avatarInfo ) {
    KBEngine.Event.fireOut ("onCreateAvatarResult", new object[]{ retcode, avatarInfo  });
}
```



