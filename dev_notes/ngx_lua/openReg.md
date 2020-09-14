...menustart

- [OpenResty](#34d3b17eb545626b3da04f656b32dba5)
    - [Hello World](#b10a8db164e0754105b7a99be72e3fe5)
    - [与其他 location 配合](#0e9ddb16cae12bbe4dc2ef1dee9a519a)
        - [内部调用 internal](#7e7169cfd1010b3a75a35c7035c9f49c)
        - [并行请求结果 capture_multi](#74c5b1f8490c21f2b3ef0d2078285193)
        - [流水线方式跳转 exec](#b9aa5c9bccf29ad02876bfb302515ddd)
        - [外部重定向 redirect](#6204c6255e2094adcdb78a9304a12985)
    - [获取 uri 参数](#6332af131d6935bf3d7818c230e932b4)
        - [获取请求 uri 参数](#8ad1878074c1c4d4922029f0801edd4c)
        - [传递请求 uri 参数](#131c02d5387e97c6a12a5d003d064608)
    - [获取请求 body](#501f0447592ecf46d66b8d0c33bfa998)
    - [输出响应体](#9cdce21d64b3eda20ffd4a1d985a93e2)
        - [ngx.say 与 ngx.print 均为异步输出](#5a133c7df0632cdd9da980956e49341c)
        - [如何优雅处理响应体过大的输出](#01730ff5798a5ad9fd0470f2fd9a847e)
    - [日志输出](#d5cbc6b298e61668d9142904c323a565)
        - [标准日志输出](#ae14caf007373643facb2990a75fc3d9)
        - [网络日志输出](#5d35b34aac80d856a0a8800c9ad8c855)
    - [简单API Server框架](#e25752827350f8b953dbed96b1e2146b)
    - [使用 Nginx 内置绑定变量](#0fed4bfac6edad9599bbda093993abc2)
    - [子查询 capture/capture_multi](#3b3ff6cfc8a6826438c02a8f663e35dc)
    - [不同阶段共享变量 ngx.ctx](#84e72e59fc559138e049799de3c59ada)
    - [防止 SQL 注入](#f96743151321aae02f6c3d2c0f24ca6d)
    - [如何发起新 HTTP 请求](#042d5977081f357a19a120018ae11d33)
        - [利用 proxy_pass](#cf2ce2505b174e42b2adc163b2a615b1)
        - [利用 cosocket](#b888cd5bb81793b53547243438aa8df6)
- [DNS](#ed5f2bdecbd4bd349d09412d1ff6a6fb)

...menuend


<h2 id="34d3b17eb545626b3da04f656b32dba5"></h2>


## OpenResty

<h2 id="b10a8db164e0754105b7a99be72e3fe5"></h2>


### Hello World

```
location / {
    default_type text/html;

    content_by_lua_block {
        ngx.say("HelloWorld")
    }
}
```

 -  openresty 1.9.3.2 以上，content_by_lua 改成了 content_by_lua_block

<h2 id="0e9ddb16cae12bbe4dc2ef1dee9a519a"></h2>


### 与其他 location 配合

利用不同 location 的功能组合，我们可以完成：

 - 内部调用
 - 流水线方式跳转
 - 外部重定向
 - 等几大不同方式

<h2 id="7e7169cfd1010b3a75a35c7035c9f49c"></h2>


#### 内部调用 internal

 - 例如对数据库、内部公共函数的统一接口，可以把它们放到统一的 location 中。
 - 通常情况下，为了保护这些内部接口，都会把这些接口设置为 **internal** 。
     - 这么做的最主要好处就是可以让这个内部接口相对独立，不受外界干扰。

示例代码：

```
location = /sum {
    # 只允许内部调用
    internal;

    # 这里做了一个求和运算只是一个例子，可以在这里完成一些数据库、
    # 缓存服务器的操作，达到基础模块和业务逻辑分离目的
    content_by_lua_block {
        local args = ngx.req.get_uri_args()
        ngx.say(tonumber(args.a) + tonumber(args.b))
    }
}

location = /app/test {
    content_by_lua_block {
        local res = ngx.location.capture(
                        "/sum", {args={a=3, b=8}}
                        )
        ngx.say("status:", res.status, " response:", res.body)
    }
}
```


<h2 id="74c5b1f8490c21f2b3ef0d2078285193"></h2>


#### 并行请求结果 capture_multi

```
location = /app/test_parallels {
    content_by_lua_block {
        local start_time = ngx.now()
        local res1, res2 = ngx.location.capture_multi( {
                        {"/sum", {args={a=3, b=8}}},
                        {"/subduction", {args={a=3, b=8}}}
                    })
        ngx.say("status:", res1.status, " response:", res1.body)
        ngx.say("status:", res2.status, " response:", res2.body)
        ngx.say("time used:", ngx.now() - start_time)
    }
}
```

<h2 id="b9aa5c9bccf29ad02876bfb302515ddd"></h2>


#### 流水线方式跳转 exec

```
location ~ ^/static/([-_a-zA-Z0-9/]+).jpg {
    set $image_name $1;
    content_by_lua_block {
        ngx.exec("/download_internal/images/"
                .. ngx.var.image_name .. ".jpg");
    };
}

location /download_internal {
    internal;
    # 这里还可以有其他统一的 download 下载设置，例如限速等
    alias ../download;
}
```

 - 注意，ngx.exec 方法与 ngx.redirect 是完全不同的
 - 前者是个纯粹的内部跳转并且没有引入任何额外 HTTP 信号。 
 - 这里的两个 location 更像是流水线上工人之间的协作关系。第一环节的工人对完成自己处理部分后，直接交给第二环节处理人（实际上可以有更多环节），它们之间的数据流是定向的。

<h2 id="6204c6255e2094adcdb78a9304a12985"></h2>


#### 外部重定向 redirect

不知道大家什么时候开始注意的，百度的首页已经不再是 HTTP 协议，它已经全面修改到了 HTTPS 协议上。但是对于大家的输入习惯，估计还是在地址栏里面输入 baidu.com ，回车后发现它会自动跳转到 https://www.baidu.com ，这时候就需要的外部重定向了。

```
location = /foo {
    content_by_lua_block {
        ngx.say([[I am foo]])
    }
}

location = / {
    rewrite_by_lua_block {
        return ngx.redirect('/foo');
    }
}
```

 - 外部重定向是可以跨域名的。
     - 例如从 A 网站跳转到 B 网站是绝对允许的
 - 在 CDN 场景的大量下载应用中，一般分为调度、存储两个重要环节。
     - 调度就是通过根据请求方 IP 、下载文件等信息寻找最近、最快节点，应答跳转给请求方完成下载。



---

<h2 id="6332af131d6935bf3d7818c230e932b4"></h2>


### 获取 uri 参数  
 
<h2 id="8ad1878074c1c4d4922029f0801edd4c"></h2>


#### 获取请求 uri 参数

uri 中 "?"后面的参数?

 - 获取一个 uri 有两个方法： 二者主要的区别是参数来源有区别(GET , POST )
     - ngx.req.get_uri_args
         - uri 请求参数
     - ngx.req.get_post_args
         - post 请求内容。


```
content_by_lua_block {
   local arg = ngx.req.get_uri_args()
   for k,v in pairs(arg) do
       ngx.say("[GET ] key:", k, " v:", v)
   end

   ngx.req.read_body() -- 解析 body 参数之前一定要先读取 body
   local arg = ngx.req.get_post_args()
   for k,v in pairs(arg) do
       ngx.say("[POST] key:", k, " v:", v)
   end
}
```

```
curl --noproxy 127.0.0.1  '127.0.0.1:8080/print_param?a=1&b=2' -d 'c=3&d=4'

[GET ] key:b v:2
[GET ] key:a v:1
[POST] key:d v:4
[POST] key:c v:3
```


<h2 id="131c02d5387e97c6a12a5d003d064608"></h2>


#### 传递请求 uri 参数

 - 调用 ngx.encode_args 进行转义

```
location /test {
       content_by_lua_block {
           local res = ngx.location.capture(
                    '/print_param',
                    {
                       method = ngx.HTTP_POST,
                       args = ngx.encode_args({a = 1, b = '2&'}),  -- 'a=1&b=2%26'
                       body = ngx.encode_args({c = 3, d = '4&'})   -- 'c=3&d=4%26'
                   }
                )
           ngx.say(res.body)
       }
   }
```   

---

<h2 id="501f0447592ecf46d66b8d0c33bfa998"></h2>


### 获取请求 body

 - 在 Nginx 的典型应用场景中，几乎都是只读取 HTTP 头即可，
     - 例如负载均衡、正反向代理等场景。
 - 但是对于 API Server 或者 Web Application ，对 body 可以说就比较敏感了。
     - 由于 OpenResty 基于 Nginx ，所以天然的对请求 body 的读取细节与其他成熟 Web 框架有些不同。
 - 由于 Nginx 是为了解决负载均衡场景诞生的，所以它默认是不读取 body 的行为，会对 API Server 和 Web Application 场景造成一些影响。
     - 根据需要正确读取、丢弃 body 对 OpenResty 开发是至关重要的。


POST a name to server:

```
# 默认读取 body
#lua_need_request_body on;  #不推荐

location /test {
            content_by_lua_block {
                local data = ngx.req.get_body_data()
                ngx.say("hello ", data)
            }
        }
```

```
$ curl --noproxy 127.0.0.1  127.0.0.1:8080/test -d jack
hello nil
```

 - 可以看到 data 部分获取为空
 - 要正确获取到 data
     - 打开 lua_need_request_body 选项强制本模块读取请求体 , 不推荐！！
     - 先调用 ngx.req.read_body() 
         - `ngx.req.read_body()  ; ngx.req.get_body_data();`
 - 如果设置了 `client_body_in_file_only on;` 
     - 请求体会被存入临时文件, 之后可以 ngx.req.get_body_file() 函数获取。


```
# 强制请求 body 到临时文件中（仅仅为了演示）
client_body_in_file_only on;

location /test {
    content_by_lua_block {
        ngx.req.read_body()
        local data = ngx.req.get_body_data()
        if nil == data then
            local file_name = ngx.req.get_body_file()
            ngx.say(">> temp file: ", file_name)
        end

        ngx.say("hello ", data)
    }
}
```


<h2 id="9cdce21d64b3eda20ffd4a1d985a93e2"></h2>


### 输出响应体

HTTP响应报文分为三个部分：

 1. 响应行
 2. 响应头
 3. 响应体

![](https://moonbingbing.gitbooks.io/openresty-best-practices/content/images/http_response_protocal.jpg)

- 对于 HTTP 响应体的输出， 调用 ngx.say 或 ngx.print 即可。
- ngx.say 会对输出响应体多输出一个 \n 。
    - 如果你用的是浏览器完成的功能调试，使用这两着是没有区别的。
    - 但是如果使用各种终端工具，这时候使用 ngx.say 明显就更方便了。
- ngx.say 与 ngx.print 均为异步输出

<h2 id="5a133c7df0632cdd9da980956e49341c"></h2>


#### ngx.say 与 ngx.print 均为异步输出

也就是说当调用 ngx.say 后并不会立刻输出响应体。参考下面的例子：


```
location /test {
    content_by_lua_block {
        ngx.say("hello")
        ngx.sleep(3)
        ngx.say("the world")
    }
}

location /test2 {
    content_by_lua_block {
        ngx.say("hello")
        ngx.flush() -- 显式的向客户端刷新响应输出
        ngx.sleep(3)
        ngx.say("the world")
    }
}

location /test3 {
    content_by_lua_block {
        ngx.say(string.rep("hello", 1000))
        ngx.sleep(3)
        ngx.say("the world")
    }
}
```

 - /test 响应内容实在触发请求 3s 后一起接收到响应体，
 - /test2 则是先收到一个 hello 停顿 3s 后又接收到后面的 the world。
 - /test3 和 /test 又不一样, 首先收到了所有的 "hello" ，停顿大约 3 秒后，接着又收到了 "the world"
     - 相同处理,不一样的输出时机



<h2 id="01730ff5798a5ad9fd0470f2fd9a847e"></h2>


#### 如何优雅处理响应体过大的输出

 - 1. 输出内容本身体积很大，例如超过 2G 的文件下载
     - 利用 HTTP 1.1 特性 CHUNKED 编码来完成
     - 注：其实 nginx 自带的静态文件解析能力已经非常好了。下面只是一个例子，实际中过大响应体都是后端服务生成的，为了演示环境相对封闭，所以这里选择本地文件。

```
local data
while true do
    data = file:read(1024)
    if nil == data then
        break
    end
    ngx.print(data)
    ngx.flush(true)
end
file:close()
```



 - 2. 输出内容本身是由各种碎片拼凑的，碎片数量庞大，例如应答数据是某地区所有人的姓名
     - 使用 ngx.print
     - 当有非常多碎片数据时，没有必要一定连接成字符串后再进行输出。完全可以直接存放在 table 中

```
local table = {
     "hello, ",
     {"world: ", true, " or ", false, {": ", nil} }
}
ngx.print(table)
```

```
hello, world: true or false: nil
```


<h2 id="d5cbc6b298e61668d9142904c323a565"></h2>


### 日志输出

<h2 id="ae14caf007373643facb2990a75fc3d9"></h2>


#### 标准日志输出

OpenResty 的标准日志输出原句为 ngx.log(log_level, ...) ，几乎可以在任何 ngx_lua 阶段进行日志的输出 。（ngx.ERR,ngx.INFO, ...）

```
print ( "tttt ")  -- ngx.INFO
ngx.log(ngx.ERR, "err:" , "error" )
ngx.log(ngx.INFO, " string:" )
```

 - 日志会输出到 logs/error.log ,  日志输出级别 会过滤掉一部分日志
 - 日志会输是异步的

日志级别:

 - ngx.STDERR     -- 标准输出
 - ngx.EMERG      -- 紧急报错
 - ngx.ALERT      -- 报警
 - ngx.CRIT       -- 严重，系统故障，触发运维告警系统
 - ngx.ERR        -- 错误，业务不可恢复性错误
 - ngx.WARN       -- 告警，业务中可忽略错误
 - ngx.NOTICE     -- 提醒，业务比较重要信息
 - ngx.INFO       -- 信息，业务琐碎日志信息，包含不同情况判断等
 - ngx.DEBUG      -- 调试


<h2 id="5d35b34aac80d856a0a8800c9ad8c855"></h2>


#### 网络日志输出

 - lua-resty-logger-socket 的目标是替代 Nginx 标准的 ngx_http_log_module 以非阻塞 IO 方式推送 access log 到远程服务器上。
 - 对远程服务器的要求是支持 syslog-ng 的日志服务。


<h2 id="e25752827350f8b953dbed96b1e2146b"></h2>


### 简单API Server框架

```
# 设置默认 lua 搜索路径，添加 lua 路径
lua_package_path 'abs_lua_path/?.lua;;';

# 对于开发研究，可以对代码 cache 进行关闭，这样不必每次都重新加载 nginx。
lua_code_cache off;

#初始化lua
#lua module中的数据, worker 共享
init_by_lua_file lua/_init.lua;

server {
    listen 80;

    # 在代码路径中使用nginx变量
    # 注意： nginx var 的变量一定要谨慎，否则将会带来非常大的风险
    location ~ ^/api/([-_a-zA-Z0-9/]+) {
        # 准入阶段完成参数验证
        access_by_lua_file  lua_path/access_check.lua;  # final path = path_nginx_prefix + path

        #内容生成阶段
        content_by_lua_file lua_path/$1.lua;
    }
}
```

 - content_by_lua_file 后面的参数 可以是 相对 nginx prefix path 的相对路径
 - lua_package_path  
     - 对后续的 lua require 命令生效 
     - lua 环境



<h2 id="0fed4bfac6edad9599bbda093993abc2"></h2>


### 使用 Nginx 内置绑定变量

Example:

```
content_by_lua_block {
    local a = tonumber(ngx.var.arg_a) or 0
    local b = tonumber(ngx.var.arg_b) or 0
    ngx.say("sum: ", a + b )
}
```

```
curl 'http://127.0.0.1/sum?a=11&b=12'
sum: 23
```

Example 简易防火墙:

```
# 使用access阶段完成准入阶段处理
access_by_lua_block {
    local black_ips = {["127.0.0.1"]=true}

    local ip = ngx.var.remote_addr
    if true == black_ips[ip] then
        ngx.exit(ngx.HTTP_FORBIDDEN)
    end
};
```

 - 大多数nginx 内置变量都是不允许写入的，例如刚刚的终端IP地址，在请求中是不允许对其进行更新的。
 - 对于可写的变量中的limit_rate，值得一提，它能完成传输速率限制，并且它的影响是单个请求级别。


```
location /download {
    access_by_lua_block {
        # 限制 1k/s 下载速度
        ngx.var.limit_rate = 1000
    };
}
```

<h2 id="3b3ff6cfc8a6826438c02a8f663e35dc"></h2>


### 子查询 capture/capture_multi

 - 发起非阻塞的内部请求访问目标 location。
 - 目标 location 可以是配置文件中其他文件目录，或 任何 其他 nginx C 模块，包括 ngx_proxy、ngx_fastcgi、ngx_memc、ngx_postgres、ngx_drizzle，甚至 ngx_lua 自身等等

 - 子请求只是模拟 HTTP 接口的形式， 没有 额外的 HTTP/TCP 流量，也 没有 IPC (进程间通信) 调用。
     - 所有工作在内部高效地在 C 语言级别完成。
 - 子请求与 HTTP 301/302 重定向指令 (通过 ngx.redirect) 完全不同，也与内部重定向 ((通过 ngx.exec) 完全不同。
 - 在发起子请求前，用户程序应总是读取完整的 HTTP 请求体 (通过调用 ngx.req.read_body 或设置 lua_need_request_body 指令为 on).
 - capture/capture_multi API 总是缓冲整个请求体到内存中。因此，当需要处理一个大的子请求响应，用户程序应使用 cosockets 进行流式处理，


```
res = ngx.location.capture(uri)
```

 - 返回一个包含四个元素的 Lua 表 (res.status, res.header, res.body, 和 res.truncated)。
 - res.status (状态) 保存子请求的响应状态码。
 - res.header (头) 用一个标准 Lua 表储子请求响应的所有头信息。如果是“多值”响应头，这些值将使用 Lua (数组) 表顺序存储。例如，如果子请求响应头包含下面的行：
     - Set-Cookie: a=3
     - Set-Cookie: foo=bar
     - Set-Cookie: baz=blah
     - 则 res.header["Set-Cookie"] 将存储 Lua 表 {"a=3", "foo=bar", "baz=blah"}
 - res.body (体) 保存子请求的响应体数据，它可能被截断。
     - 用户需要检测 res.truncated (截断) 布尔值标记来判断 res.body 是否包含截断的数据。
     - 这种数据截断的原因只可能是因为子请求发生了不可恢复的错误，例如远端在发送响应体时过早中断了连接，或子请求在接收远端响应体时超时。


例如，发送一个 POST 子请求，可以这样做：

```
res = ngx.location.capture(
     '/foo/bar',
     { method = ngx.HTTP_POST, body = 'hello, world' }
 )
```

 - method 选项默认值是 ngx.HTTP_GET
 - args 选项可以设置附加的 URI 参数，例如：
     - `ngx.location.capture('/foo?a=1',  { args = { b = 3, c = ':' } }   )`
     - 等同于 `ngx.location.capture('/foo?a=1&b=3&c=%3a')`


 - 请注意，通过 ngx.location.capture 创建的子请求默认继承当前请求的所有请求头信息，这有可能导致子请求响应中不可预测的副作用。
     - 例如，当使用标准的 ngx_proxy 模块服务子请求时，如果主请求头中包含 "Accept-Encoding: gzip"，可能导致子请求返回 Lua 代码无法正确处理的 gzip 压缩过的结果。
     - 通过设置 `proxy_pass_request_headers` 为 off ，在子请求 location 中忽略原始请求头。
 - ngx.location.capture 和 ngx.location.capture_multi 指令无法抓取包含以下指令的 location： 
     - add_before_body, add_after_body, auth_request, echo_location, echo_location_async, echo_subrequest, 或 echo_subrequest_async 。

 - 下面的代码不会如预期般工作

```
location /foo {
     content_by_lua '
         res = ngx.location.capture("/bar")
     ';
}
location /bar {
 echo_location /blah;
}
location /blah {
 echo "Success!";
}
```

<h2 id="84e72e59fc559138e049799de3c59ada"></h2>


### 不同阶段共享变量 ngx.ctx

 - 几种需要共享数据的场合
     - 1. 进程间
         - 通过共享内存的方式完成不同工作进程的数据共享
     - 2. 单个进程内不同请求的数据共享
         - 通过 Lua 模块方式完成
     - 3. 单个请求内不同阶段的数据共享
         - 最典型的例子，估计就是在 log 阶段记录一些请求的特殊变量
         - ngx.ctx 

```
location /test {
     rewrite_by_lua '
         ngx.ctx.foo = 76
     ';
     access_by_lua '
         ngx.ctx.foo = ngx.ctx.foo + 3
     ';
     content_by_lua '
         ngx.say(ngx.ctx.foo)
     ';
}
```

 - ngx.ctx 是一个表， 可以对他添加、修改。
     - 任意数据值，包括 Lua 闭包与嵌套表
 - 用来存储基于请求的 Lua 环境数据，其生存周期与当前请求相同 (类似 Nginx 变量)。
 - 它有一个最重要的特性：单个请求内的 rewrite (重写)，access (访问)，和 content (内容) 等各处理阶段是保持一致的。
 - 额外注意，每个请求，包括子请求，都有一份自己的 ngx.ctx 表
 - ngx.ctx 表查询需要 **相对昂贵的元方法调用**，这比通过用户自己的函数参数 直接传递基于请求的数据要慢得多。
     - 不要为了节约用户函数参数而滥用此 API，因为它可能对性能有明显影响。
 - ngx.ctx  不能直接共享给其他请求使用的



<h2 id="f96743151321aae02f6c3d2c0f24ca6d"></h2>


### 防止 SQL 注入

 - MySQL 
     - ndk.set_var.set_quote_sql_str
     - db:query(string.format([[select * from cats where id = '%s']], ndk.set_var.set_quote_sql_str(req_id)))
 - PostgreSQL
     - ndk.set_var.set_quote_pgsql_str


<h2 id="042d5977081f357a19a120018ae11d33"></h2>


### 如何发起新 HTTP 请求

<h2 id="cf2ce2505b174e42b2adc163b2a615b1"></h2>


#### 利用 proxy_pass

利用 proxy_pass 完成 HTTP 接口访问的成熟配置+调用方法:


```
http {
    upstream md5_server{
        server 127.0.0.1:81;        # ①
        keepalive 20;               # ②
    }

    server {
        listen    80;

        location /test {
            content_by_lua_block {
                -- read body
                ngx.req.read_body()
                local args, err = ngx.req.get_uri_args()

                -- ③
                local res = ngx.location.capture('/spe_md5',
                    {
                        method = ngx.HTTP_POST,
                        body = args.data
                    }
                )

                if 200 ~= res.status then
                    ngx.exit(res.status)
                end

                if args.key == res.body then
                    ngx.say("valid request")
                else
                    ngx.say("invalid request")
                end
            }
        }

        location /spe_md5 {
            proxy_pass http://md5_server;   -- ④
        }
    }

    server {
        listen    81;           -- ⑤

        location /spe_md5 {
            content_by_lua_block {
                ngx.req.read_body()
                local data = ngx.req.get_body_data()
                ngx.print(ngx.md5(data .. "*&^%$#$^&kjtrKUYG"))
            }
        }
    }
}
```


 - ① 上游访问地址清单
     - (可以按需配置不同的权重规则)； 
 - ② 上游访问长连接，是否开启长连接，对整体性能影响比较大
 - ③ 接口访问通过 ngx.location.capture 的子查询方式发起； 
 - ④ 由于 ngx.location.capture 方式只能是 nginx 自身的子查询，需要借助 proxy_pass 发出 HTTP 连接信号； 
 - ⑤ 公共 API 输出服务；
 - 借用 nginx 周边成熟组件力量，为了发起一个 HTTP 请求，我们需要绕好几个弯子，甚至还有可能踩到坑（upstream 中长连接的细节处理），显然没有足够优雅，所以我们继续看下一章节。


<h2 id="b888cd5bb81793b53547243438aa8df6"></h2>


#### 利用 cosocket

```
http {
    server {
        listen    80;

        location /test {
            content_by_lua_block {
                ngx.req.read_body()
                local args, err = ngx.req.get_uri_args()

                local http = require "resty.http"   -- ①
                local httpc = http.new()
                local res, err = httpc:request_uri( -- ②
                    "http://127.0.0.1:81/spe_md5",
                        {
                        method = "POST",
                        body = args.data,
                      }
                )

                if 200 ~= res.status then
                    ngx.exit(res.status)
                end

                if args.key == res.body then
                    ngx.say("valid request")
                else
                    ngx.say("invalid request")
                end
            }
        }
    }

    server {
        listen    81;

        location /spe_md5 {
            content_by_lua_block {
                ngx.req.read_body()
                local data = ngx.req.get_body_data()
                ngx.print(ngx.md5(data .. "*&^%$#$^&kjtrKUYG"))
            }
        }
    }
}
```

 - ① 引用 resty.http 
     - [github](https://github.com/pintsized/lua-resty-http) 
 - ② request_uri 函数完成了连接池、HTTP 请求等一系列动作。
 - 如果你的内部请求比较少，使用 ngx.location.capture+proxy_pass 的方式还没什么问题。
 - 但如果你的请求数量比较多，或者需要频繁的修改上游地址，那么 resty.http就更适合你。


<h2 id="ed5f2bdecbd4bd349d09412d1ff6a6fb"></h2>


## DNS

```nginx
# openresty/openresty:1.15.8.1-3-bionic

http {
    # use system resolver
    resolver local=on ipv6=off;
    resolver_timeout 5s;
```




