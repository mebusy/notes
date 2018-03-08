
# Lua Tips

## android close luajit

```lua
    if jit then
        jit.off()
    end
```


## GC setting

```lua
collectgarbage("setpause", 200 )
collectgarbage("setstepmul", 5000)
```

## random init

```python
math.randomseed(os.time())
```

## lua module

 - 1

```lua
local _G = _G

-- no more external access after this point
setmetatable(P, {__index = _G})
setfenv(1, P)
```

 - 2

```lua
module( "MODULE_NAME" , package.seeall )
```

## class

```lua
local P    = class("cBall",
                 function(self   )
                    return cActor:create(  )
                 end
                 )
cBall = P
```

## save / load 

```lua
local P = {}
cGameSave = P

setmetatable(P, {__index = _G})
setfenv(1, P)

bMusic = true
bSfx = true

local record_file = "save.bin"

function save_record()
    --所需存档，在这里设置
    local t = {
        bMusic = bMusic,
        bSfx = bSfx,
    }

    local json = require("json")
    data = json.encode(t)
    print("record file len: %d" , #data )

    --save
    local path = CCFileUtils:sharedFileUtils():getWritablePath() .. record_file
    local f = io.open(path, "w")
    if f then
        local t = f:write(data)
        f:close()
        print("file saved")
    end

    t = nil
end

local function load_record()
    print("load_record")

    local path = CCFileUtils:sharedFileUtils():getWritablePath() .. record_file
    local f = io.open(path, "r")
    if f then
        local data  = f:read("*all")
        f:close()

        local json = require("json")
        -- keep t non-local
        t = json.decode(data)

        if t then
            for i,v in pairs(t) do
                loadstring( string.format( "cGameSave.%s = cGameSave.t.%s" , i ,i  )  )()
            end
        end

        t = nil
    else
        print("no save record find !!")
    end
end

xpcall( load_record , mylib.__G__TRACKBACK__ )
return cGameSave
```

## iOS ffi 

 - https://github.com/mebusy/codeLib/blob/master/integrateLua/useful_luascript/luajit_ffi/ffi_func.lua

## md5

```lua
    local md5 =require ('md5')
    local md5_val  = md5.sumhexa ( "ABC" )
```

## base64

```lua
    local mime = require'mime'
    print ( "base64 ABC: " , mime.b64( "ABC" ) )
    local _m = mime.unb64( msg )
```

## des56

```lua
    local des56 = require 'des56'
    local key = '&3g4&gs*&3'
    local crypt = des56.crypt('1234567890', key)
    print ( "crypt" , crypt )
    local decrypt = des56.decrypt( crypt , key)
    print ('decrypt' , decrypt)
```


## json

```lua
    local json = require("json")
    data = json.encode(t)

    t = json.decode(data)
```

## not cache module

```lua
module("GameMapOpenInfiniteMode" , package.seeall ) 

if not LUA_MODULE_CACHE then
	package.loaded.GameMapOpenInfiniteMode = nil 
end 
```

