...menustart

- [openResty](#dd4d42e37fae513558da90ea00333063)
- [LUA](#883d3b066b7cbbfc99038e621863c6e0)
    - [字符串处理优化](#919b03a1a05100a1c3897ec9978c2ebe)
    - [luajit 2.1 新增 table.new / table.clear](#67075b940448924623dbcd7dd916fac3)
    - [Datatime](#ee19ffff9a3511cac5b979f823aff7a3)
- [Nginx](#62e0b5b350c9e3d2c19aa801d9442ba9)
    - [Nginx Location 中避免使用 if](#532027cfdc2f244c80e4855803dc96a1)
    - [Nginx 静态文件服务](#7b9633c105cfd5818516ea5c9612b038)
    - [使用 Nginx 内置绑定变量](#0fed4bfac6edad9599bbda093993abc2)
- [OpenResty](#34d3b17eb545626b3da04f656b32dba5)
    - [与其它location配合](#4a0d753d1874716bf3a5312c9fb40a78)
        - [location 重定向](#1f782bbcb0f358140e9b846159cc0c40)
        - [子查询](#98250245cb03144174da323894914f76)
    - [不同阶段共享变量](#77e016da9947e8d99f14987047d01f56)
    - [防止 SQL 注入](#f96743151321aae02f6c3d2c0f24ca6d)
    - [如何发起新 HTTP 请求](#042d5977081f357a19a120018ae11d33)
- [LuaNginxModule](#9cca9de1daf187e925e4af72d9eb1bd1)
    - [正确的记录日志](#2081eee0b4b974d68a1d64f844b561e0)
    - [log response body](#e64b0c98f68c9a90948513a701a70acf)
    - [encrypt response data](#dff3ed0ff2d4834c3779f000ab86d29e)
    - [OpenResty 的缓存](#ade50a0c00771d6260bb66a3c31e149a)
    - [Sleep](#243924bfd56a682be235638b53961e09)
    - [定时任务](#a1bd9760fc7a20ba5c57564d2d173bf0)
    - [请求返回后继续执行](#0c17af5ce22abf1dcf75152b78f8ec1c)
    - [变量的共享范围](#ecf8271962fadee06343c2d4e99b56c2)
        - [全局变量](#fcfffbf5d7dd5c491645e2e0947eddb8)
        - [模块变量](#d7e0e1ac2e013da43d23f0d0c9e344bf)
    - [动态限速](#31547d6d7bad726c77008c90d284ad09)
    - [如何引用第三方 resty 库](#4ec18a5d7bdffacc089a0c2b5d465d8c)
    - [获取work id](#eea3840ea98c24e707b61bb59dde0ea5)
    - [缓存失效风暴](#34db7f6a4a045a7a92bcfdf5da877d48)
- [Web 服务](#dfe5ebff296eb614727bc480c587e9b8)
    - [连接池用法](#484a10ad9f2ffd3dbf637a4a42baad6e)
    - [TIME_WAIT 问题](#177d8aff42db24f9cb72c02652fc4aed)
    - [ngx.print  / ngx.say](#99c54081e0eda78c9d255f5dd5405816)
    - [remote_address](#cf69af8b80a73bcdbb6312d4922bbdaa)

...menuend


<h2 id="dd4d42e37fae513558da90ea00333063"></h2>


# openResty 

<h2 id="883d3b066b7cbbfc99038e621863c6e0"></h2>


# LUA


<h2 id="919b03a1a05100a1c3897ec9978c2ebe"></h2>


## 字符串处理优化

 - string.gsub / string.match 的方法无法jit 优化，尽量使用 ngx_lua 模块提供的 ngx.re.match 等接口
 - openresty 正则表达式 : https://moonbingbing.gitbooks.io/openresty-best-practices/lua/re.html


<h2 id="67075b940448924623dbcd7dd916fac3"></h2>


## luajit 2.1 新增 table.new / table.clear

 - 前者主要用来预分配 Lua table 空间，后者主要用来高效的释放 table 空间，并且它们都是可以被 JIT 编译的
 - 具体可以参考一下 OpenResty 捆绑的 lua-resty-\* 库

<h2 id="ee19ffff9a3511cac5b979f823aff7a3"></h2>


## Datatime

 - 在 Lua 中，函数 time、date 和 difftime 提供了所有的日期和时间功能。
    - 这些函数通常会引发不止一个昂贵的系统调用，同时无法为 LuaJIT JIT 编译，对性能造成较大影响。
 - 推荐使用 ngx_lua 模块提供的带缓存的时间接口
    - ngx.today, ngx.time, ngx.utctime, ngx.localtime, ngx.now, ngx.http_time，以及 ngx.cookie_time 等。

<h2 id="62e0b5b350c9e3d2c19aa801d9442ba9"></h2>


# Nginx
 
<h2 id="532027cfdc2f244c80e4855803dc96a1"></h2>


## Nginx Location 中避免使用 if

 - if 指令是 rewrite 模块中的一部分, 是实时生效的指令
 - 在 if 里写入一些非 rewrite 指令, 会出现不可预期的问题
 - 唯一正确的修复方式是完全禁用 if 中的非 rewrite 指令

<h2 id="7b9633c105cfd5818516ea5c9612b038"></h2>


## Nginx 静态文件服务

 - https://moonbingbing.gitbooks.io/openresty-best-practices/ngx/static_file.html

<h2 id="0fed4bfac6edad9599bbda093993abc2"></h2>


## 使用 Nginx 内置绑定变量

 - https://moonbingbing.gitbooks.io/openresty-best-practices/openresty/inline_var.html
 - `ngx.var.VARIABLE`

<h2 id="34d3b17eb545626b3da04f656b32dba5"></h2>


# OpenResty

<h2 id="4a0d753d1874716bf3a5312c9fb40a78"></h2>


## 与其它location配合

<h2 id="1f782bbcb0f358140e9b846159cc0c40"></h2>


### location 重定向

 - 外部重定向:  ngx.redirect
 - 内部重定向:  ngx.exec

<h2 id="98250245cb03144174da323894914f76"></h2>


### 子查询
    
 - 发起非阻塞的内部请求
 - `ngx.location.capture`



<h2 id="77e016da9947e8d99f14987047d01f56"></h2>


## 不同阶段共享变量

 - 在 OpenResty 的体系中，可以通过共享内存的方式完成不同工作进程的数据共享
    - 可以通过 Lua 模块方式完成单个进程内不同请求的数据共享
    - 单个请求内不同阶段的数据共享使用  ngx.ctx 
 - ngx.ctx 是一个表
    - 它用来存储基于请求的 Lua 环境数据，其生存周期与当前请求相同 (类似 Nginx 变量)。
    - 每个请求，包括子请求，都有一份自己的 ngx.ctx 表
 - https://moonbingbing.gitbooks.io/openresty-best-practices/openresty/share_var.html


<h2 id="f96743151321aae02f6c3d2c0f24ca6d"></h2>


## 防止 SQL 注入

 - https://moonbingbing.gitbooks.io/openresty-best-practices/openresty/safe_sql.html
 - 对于 MySQL ，可以调用 ndk.set_var.set_quote_sql_str ，对用户提交的内容 进行一次过滤即可。

<h2 id="042d5977081f357a19a120018ae11d33"></h2>


## 如何发起新 HTTP 请求

 - 利用 proxy_pass
 - 利用 cosocket

<h2 id="9cca9de1daf187e925e4af72d9eb1bd1"></h2>


# LuaNginxModule

<h2 id="2081eee0b4b974d68a1d64f844b561e0"></h2>


## 正确的记录日志

 - 日志 统一放到 log_by_lua\* 阶段
 - 配合 ngx.ctx

<h2 id="e64b0c98f68c9a90948513a701a70acf"></h2>


## log response body

 - add `body_filter_by_lua 'ngx.log(ngx.INFO,ngx.arg[1])';`  to right location

<h2 id="dff3ed0ff2d4834c3779f000ab86d29e"></h2>


## encrypt response data

```nginx
body_filter_by_lua_file lua/body_filter_gameserver.lua ;
```

注意: body_filter 在一个请求中可能会被多次调用，每次filter一个chunk

```lua
-- lua/body_filter_gameserver.lua
local req_headers = ngx.req.get_headers()
local clientCodeVersion  = tonumber(  req_headers["clientCodeVersion"] ) or -1 

if clientCodeVersion >= 20 and ngx.arg[1] and not ngx.is_subrequest then  
    -- ngx.log( ngx.INFO, "client version code: " .. clientCodeVersion  )
    local key = string.sub( "UMC_HDA_OHIAOSJDAS" , 1, 16)
    local iv = "0123456789ABCDEF"
    local src = ngx.arg[1]

    local aes = require "resty.aes"
    local str = require "resty.string"
    local aes_128_cbc_with_iv = assert(aes:new(key,
        nil, aes.cipher(128,"cbc"), {iv=iv}))
        -- AES 128 CBC with IV and no SALT
    local encrypted = aes_128_cbc_with_iv:encrypt( src )
    -- ngx.log("AES 128 CBC (WITH IV) Encrypted HEX: ", str.to_hex(encrypted))
    -- ngx.log( ngx.INFO , "AES 128 CBC (WITH IV) Decrypted: ",  aes_128_cbc_with_iv:decrypt(encrypted))

    
    ngx.arg[1] = ngx.encode_base64(encrypted)  .. ','
    ngx.log( ngx.INFO, ngx.arg[1]  .. src .. ngx.req.get_method() )
end
```

```lua
-- head_filter.lua
-- 假设上游的服务器返回了 Content-Length 报头，而 body_filter_by_lua* 又修改了响应体的实际大小。
-- 客户端收到这个报头后，按其中的 Content-Length 去处理，顺着一头栽进坑里。由于Nginx 的流式响应，发出去的报头就像泼出去的水，要想修改只能提前进行。
-- OpenResty 提供了跟 body_filter_by_lua* 相对应的 header_filter_by_lua*。
-- header_filter 会在 Nginx 发送报头之前调用，所以可以在这里置空 Content-Length 报头：

ngx.header.content_length = nil
```


<h2 id="ade50a0c00771d6260bb66a3c31e149a"></h2>


## OpenResty 的缓存

 - 使用 Lua shared dict
    - 所有 worker 之间共享的，内部使用的 LRU 算法
    - shared.dict 使用的是共享内存，每次操作都是全局锁
 - 使用Lua LRU cache
    - worker 级别的，不会在 Nginx wokers 之间共享
    - 永远不会触发锁，效率上有优势，并且没有 shared.dict 的体积限制，内存上也更弹性
    - 不同 worker 之间数据不同享，同一缓存数据可能被冗余存储。
 
<h2 id="243924bfd56a682be235638b53961e09"></h2>


## Sleep

 - ngx.sleep(0.1)

<h2 id="a1bd9760fc7a20ba5c57564d2d173bf0"></h2>


## 定时任务

 - https://moonbingbing.gitbooks.io/openresty-best-practices/ngx_lua/timer.html
 - ngx.timer.at
 - ngx.timer 运行在自己的 coroutine 里面
    - https://moonbingbing.gitbooks.io/openresty-best-practices/ngx_lua/lua-variable-scope.html
 - 如何只启动一个 timer 工作？
    - https://moonbingbing.gitbooks.io/openresty-best-practices/ngx_lua/how_one_instance_time.html



<h2 id="0c17af5ce22abf1dcf75152b78f8ec1c"></h2>


## 请求返回后继续执行

 - https://moonbingbing.gitbooks.io/openresty-best-practices/ngx_lua/continue_after_eof.html

<h2 id="ecf8271962fadee06343c2d4e99b56c2"></h2>


## 变量的共享范围

<h2 id="fcfffbf5d7dd5c491645e2e0947eddb8"></h2>


### 全局变量

 - 在 OpenResty 里面，只有在 init_by_lua\* 和 init_worker_by_lua\* 阶段才能定义真正的全局变量。
 - 其他阶段里面，OpenResty 会设置一个隔离的全局变量表，以免在处理过程污染了其他请求。
 - 即使在上述两个可以定义全局变量的阶段，也尽量避免这么做。
    - 全局变量能解决的问题，用模块变量也能解决， 而且会更清晰、更干净。

<h2 id="d7e0e1ac2e013da43d23f0d0c9e344bf"></h2>


### 模块变量

 - 由于 Lua VM 会把 require 进来的模块缓存到 package.loaded 表里，除非设置了 lua_code_cache off， 模块里定义的变量都会被缓存起来。
 - 重要的是，模块变量在每个请求中是共享的
 - 模块变量的共享特性，在高并发情况下，可能会出现问题
    - 每个请求的数据在传递和存储时须特别小心，只应通过你自己的函数参数来传递，或者通过 ngx.ctx 表。
    - 前者效率显然较高，而后者胜在能跨阶段使用。


<h2 id="31547d6d7bad726c77008c90d284ad09"></h2>


## 动态限速

 - limit_rate 限制响应速度
    - Nginx 有一个 $limit_rate，这个变量反映的是当前请求每秒能响应的字节数
 - limit_conn 限制连接数
 - limit_req 限制请求数
 - 参考 官方 [lua-resty-limit-traffic](https://github.com/openresty/lua-resty-limit-traffic)


<h2 id="4ec18a5d7bdffacc089a0c2b5d465d8c"></h2>


## 如何引用第三方 resty 库

 - OpenResty 引用第三方 resty 库非常简单，只需要将相应的文件拷贝到 resty 目录下即可。

<h2 id="eea3840ea98c24e707b61bb59dde0ea5"></h2>


## 获取work id

 - seq_id = ngx.worker.id()

<h2 id="34db7f6a4a045a7a92bcfdf5da877d48"></h2>


## 缓存失效风暴

 - https://moonbingbing.gitbooks.io/openresty-best-practices/lock/cache-miss-storm.html

<h2 id="dfe5ebff296eb614727bc480c587e9b8"></h2>


# Web 服务

<h2 id="484a10ad9f2ffd3dbf637a4a42baad6e"></h2>


## 连接池用法

 - https://moonbingbing.gitbooks.io/openresty-best-practices/web/conn_pool.html

<h2 id="177d8aff42db24f9cb72c02652fc4aed"></h2>


## TIME_WAIT 问题

 - https://moonbingbing.gitbooks.io/openresty-best-practices/web/time_wait.html
 - 主动关闭的一方会进入 TIME_WAIT 状态，并且在此状态停留两倍的 MSL 时长。
 - Nginx 在某些情况下，会主动关闭客户端的请求，
    -  问题出在 User-Agent，Nginx 认为终端的浏览器版本太低，不支持 keep alive，所以直接 close 了。
 - `keepalive_disable none;`


<h2 id="99c54081e0eda78c9d255f5dd5405816"></h2>


## ngx.print  / ngx.say

 - ngx.say 会自动添加一个换行符
 - 支持 array table, 可以直接concat后输出

<h2 id="cf69af8b80a73bcdbb6312d4922bbdaa"></h2>


## remote_address

 - remote_addr代表客户端的IP，但它的值不是由客户端提供的，而是服务端根据客户端的ip指定的，当你的浏览器访问某个网站时，假设中间没有任何代理，那么网站的web服务器（Nginx，Apache等）就会把remote_addr设为你的机器IP，如果你用了某个代理，那么你的浏览器会先访问这个代理，然后再由这个代理转发到网站，这样web服务器就会把remote_addr设为这台代理机器的IP。
 - 但是实际场景中，我们即使有代理，也需要将$remote_addr设置为真实的用户IP，以便记录在日志当中，当然nginx是有这个功能，但是需要编译的时候添加--with-http_realip_module 这个模块，默认是没有安装的。
 - openResty 使用了 `--with-http_realip_module `





