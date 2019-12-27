...menustart

 - [Lua Tips](#cdff923ceb0686b15a9e6a7646ce39a5)
     - [luajit 优化清单](#124860a10068c39b324d96ce2ff9e594)
     - [android close luajit](#03849b48cc42973dbda2c89ebdc1ff53)
     - [GC setting](#198420b0c9c9176d55de8c58dcf4ccc8)
     - [random init](#7ecf64cd7995ca180352c318105b1856)
     - [lua module](#9741c873c3c8e2fd5d43335abc57499b)
     - [class](#a2f2ed4f8ebc2cbb4c21a29dc40ab61d)
     - [save / load](#c3641e56a8060f791a11698de3839a0f)
     - [iOS ffi](#7751b8d5fe7cb21e5515f6330b3ad09b)
     - [md5](#1bc29b36f623ba82aaf6724fd3b16718)
     - [base64](#95a1446a7120e4af5c0c8878abb7e6d2)
     - [des56](#ce509be573ac98e87743ae5e3ba37d52)
     - [json](#466deec76ecdf5fca6d38571f6324d54)
     - [not cache module](#13191226ee63cce3f5a2ef675051c00e)
     - [Luasocket](#aa10c42754e7263b5a85b332598e98b7)
     - [lua-curl](#772edb00955646c4775cfeae8610fb55)
     - [c access lua  Global  variable](#52d1c0a8e0957b2df01bb1ae04d48fad)
     - [UTC_ISO_8601totime](#4f32e37b3035e200ef8423edee6f5402)
     - [get time zone](#544369429982c1f0dbf82a4b37ca3663)
     - [bit operation](#f3d96fbe7760483bbb08625d5a30024e)

...menuend


<h2 id="cdff923ceb0686b15a9e6a7646ce39a5"></h2>


# Lua Tips

<h2 id="124860a10068c39b324d96ce2ff9e594"></h2>


## luajit 优化清单

 - http://wiki.luajit.org/NYI


<h2 id="03849b48cc42973dbda2c89ebdc1ff53"></h2>


## android close luajit

```lua
    if jit then
        jit.off()
    end
```


<h2 id="198420b0c9c9176d55de8c58dcf4ccc8"></h2>


## GC setting

```lua
collectgarbage("setpause", 200 )
collectgarbage("setstepmul", 5000)
```

 - execute a full gc

```lua
collectgarbage()
```

<h2 id="7ecf64cd7995ca180352c318105b1856"></h2>


## random init

```python
math.randomseed(os.time())
```

<h2 id="9741c873c3c8e2fd5d43335abc57499b"></h2>


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

<h2 id="a2f2ed4f8ebc2cbb4c21a29dc40ab61d"></h2>


## class

```lua
local P    = class("cBall",
                 function(self   )
                    return cActor:create(  )
                 end
                 )
cBall = P
```

<h2 id="c3641e56a8060f791a11698de3839a0f"></h2>


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

<h2 id="7751b8d5fe7cb21e5515f6330b3ad09b"></h2>


## iOS ffi 

 - https://github.com/mebusy/codeLib/blob/master/integrateLua/useful_luascript/luajit_ffi/ffi_func.lua

<h2 id="1bc29b36f623ba82aaf6724fd3b16718"></h2>


## md5

```lua
    local md5 =require ('md5')
    local md5_val  = md5.sumhexa ( "ABC" )
```

<h2 id="95a1446a7120e4af5c0c8878abb7e6d2"></h2>


## base64

```lua
    local mime = require'mime'
    print ( "base64 ABC: " , mime.b64( "ABC" ) )
    local _m = mime.unb64( msg )
```

<h2 id="ce509be573ac98e87743ae5e3ba37d52"></h2>


## des56

```lua
    local des56 = require 'des56'
    local key = '&3g4&gs*&3'
    local crypt = des56.crypt('1234567890', key)
    print ( "crypt" , crypt )
    local decrypt = des56.decrypt( crypt , key)
    print ('decrypt' , decrypt)
```


<h2 id="466deec76ecdf5fca6d38571f6324d54"></h2>


## json

```lua
    local json = require("json")
    data = json.encode(t)

    t = json.decode(data)
```

<h2 id="13191226ee63cce3f5a2ef675051c00e"></h2>


## not cache module

```lua
module("GameMapOpenInfiniteMode" , package.seeall ) 

if not LUA_MODULE_CACHE then
    package.loaded.GameMapOpenInfiniteMode = nil 
end 
```


<h2 id="aa10c42754e7263b5a85b332598e98b7"></h2>


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

<h2 id="772edb00955646c4775cfeae8610fb55"></h2>


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


<h2 id="52d1c0a8e0957b2df01bb1ae04d48fad"></h2>


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

<h2 id="4f32e37b3035e200ef8423edee6f5402"></h2>


## UTC_ISO_8601totime

```lua
function UTC_ISO_8601totime (s )
    local xyear, xmonth, xday ,h,m,s = s:match("(%d+)%-(%d+)%-(%d+)T(%d+):(%d+):(%d+)")
    return os.time({year = xyear, month = xmonth, day = xday, hour = h, min = m, sec = s})
end
```

<h2 id="544369429982c1f0dbf82a4b37ca3663"></h2>


## get time zone 

```
> print( os.difftime( os.time(), os.time(os.date("!*t", os.time()  )))  )
28800
```

<h2 id="f3d96fbe7760483bbb08625d5a30024e"></h2>


## bit operation 

[bit operation implemented in lua](lua_bit.md)


