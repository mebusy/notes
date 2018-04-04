
# Lua Tips

## luajit 优化清单

 - http://wiki.luajit.org/NYI


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

 - execute a full gc

```lua
collectgarbage()
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


## Luasocket

http://w3.impa.br/~diego/software/luasocket/http.html#request

 - simple request

```lua
http.request(url [, body])
```


 - generic request 

```lua
#!/usr/bin/env lua
local http=require("socket.http");
local ltn12 = require("ltn12")

local request_body = [[login=user&password=123]]
local response_body = {}

local res, code, response_headers = http.request{
    url = "http://httpbin.org/post",
    method = "POST",
    headers = {
        ["Content-Type"] = "application/x-www-form-urlencoded";
        ["Content-Length"] = #request_body;
    },
    source = ltn12.source.string(request_body),
    sink = ltn12.sink.table(response_body),
}

print(res)
print(code)

if type(response_headers) == "table" then
    for k, v in pairs(response_headers) do
        print(k, v)
    end
end

print("Response body:")

if type(response_body) == "table" then
    print(table.concat(response_body))
else
    print("Not a table:", type(response_body))
end
```

 - 异步 request

```lua
module( "asyncRequest" , package.seeall )

local url = require("socket.url")
local dispatch = require("dispatch")
local http = require("socket.http")
dispatch.TIMEOUT = 10

handler = dispatch.newhandler("coroutine")

local nthreads = 0

-- get the status of a URL using the dispatcher
function getstatus(link)
    local parsed = url.parse(link, {scheme = "file"})
    --[[
    for k,v in pairs( parsed ) do
        print (k,v)
    end
    ]]
    if parsed.scheme == "http" or parsed.scheme == "https" then
        nthreads = nthreads + 1
        handler:start(function()
            local r, c, h, s = http.request{
                method = "HEAD",
                url = link,
                create = handler.tcp
            }
            if r and c == 200 then
                io.write('\t', link, '\n')
            else
                io.write('\t', link, ': ', tostring(c), '\n')
            end
            nthreads = nthreads - 1
        end)
    end
end

function exec()
    getstatus( "https://www.baidu.com" )

    while nthreads > 0 do
        print ( "handler:step()" )
        handler:step()
    end
end
```

## lua-curl

 - example 1

```lua
local cURL = require("cURL")

headers = {
  "Accept: text/*",
  "Accept-Language: en",
  "Accept-Charset: iso-8859-1,*,utf-8",
  "Cache-Control: no-cache"
}

login_url = "https://10.10.2.1/cgi-bin/acd/myapp/controller/method?userid=tester&password=123123"

c = cURL.easy{
  url            = login_url,
  ssl_verifypeer = false,
  ssl_verifyhost = false,
  httpheader     = headers,
  writefunction  = function(str)
    succeed = succeed or (string.find(str, "srcId:%s+SignInAlertSupressor--"))
  end
}

c:perform()
```

 - example 2

```lua
    local curl = require('cURL')
    local easy = curl.easy()
        :setopt_url('https://github.com')
        :setopt_writefunction(io.write)

    easy:setopt(curl.OPT_SSL_VERIFYHOST, 0)
    easy:setopt(curl.OPT_SSL_VERIFYPEER, 0)
    easy:perform():close()
```

 - more example
    - https://www.tuicool.com/articles/yY3Erub
    - http://www.cnblogs.com/moodlxs/archive/2012/10/15/2724318.html


## c access lua  Global  variable

```c
    lua_getglobal(L, "z");
    z = (int)lua_tointeger(L, -1);
    lua_pop(L, 1);
```

```c
    lua_pushnumber(L, 10);
    lua_setglobal(L, "z");
```

## UTC_ISO_8601totime

```lua
function UTC_ISO_8601totime (s )
    local xyear, xmonth, xday ,h,m,s = s:match("(%d+)%-(%d+)%-(%d+)T(%d+):(%d+):(%d+)")
    return os.time({year = xyear, month = xmonth, day = xday, hour = h, min = m, sec = s})
end
```

## get time zone 

```
> print( os.difftime( os.time(), os.time(os.date("!*t", now)))  )
28800
```

