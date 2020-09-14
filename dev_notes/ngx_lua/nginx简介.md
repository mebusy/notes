...menustart

- [Nginx](#62e0b5b350c9e3d2c19aa801d9442ba9)
    - [location 匹配规则](#65036706833561dc5b0be60031e23734)
    - [ReWrite语法](#93636e7713b2bfbfb6870fa0c2f4052d)
    - [可以用来判断的表达式](#b69cd322affa5f72ee270ece8cf29113)
    - [if 是邪恶的](#6cee1d1d18aeb9bff5d6d226016c0eef)
    - [Nginx 静态文件服务](#7b9633c105cfd5818516ea5c9612b038)
        - [如何安装和配置基础缓存  Basic Caching](#f9ec24bd7c322b41cb742de2eef83411)
        - [缓存微调 TODO](#1e0c9af54f0620b1412ad6c496f3e341)
        - [跨多硬盘分割缓存 TODO](#3d124ed5fca2ee7d48481e391205c5f4)
    - [反向代理](#39fdee1a60aa3d1942ecac9bc4d55129)
    - [负载均衡](#4eaa6f6da0f943db22ee7df8ed5e8d86)
        - [upstream 负载均衡概要](#8c7abf9252c14e770bb8b7a63465baa7)
        - [upstream 支持的负载均衡算法](#0e5e6e2abcca5d5200772a59178c69a7)
        - [upstream 支持的状态参数](#b1577d4475a60b4aee2a200c3b54108f)
        - [配置 nginx 进行健康状态检查](#0c23468b07d39fbbf4b89831f45c318d)
    - [Nginx 陷阱和常见错误](#42f78f76deabbbea593e4d7fb7fc4db6)

...menuend


<h2 id="62e0b5b350c9e3d2c19aa801d9442ba9"></h2>


## Nginx

<h2 id="65036706833561dc5b0be60031e23734"></h2>


### location 匹配规则

 语法规则:

 ```
 location [=|~|~*|^~] /uri/ { … }
 ```

符号 | 含义 | 优先级 
--- | --- | ---
=    | 精确匹配  | 1
^~    | 表示 uri 以某个**常规字符串**开头，理解为匹配 url 路径即可。nginx 不对 url 做编码，因此请求为/static/20%/aa，可以被规则^~ /static/ /aa匹配到（注意是空格） | 2
~    | 区分大小 写的正则匹配 | 3
~*    | 不区分大小写的正则匹配 | 4
/    | 通用匹配，任何请求都会匹配到 | 5


**Example**:

```
location = / {
   #规则A
}
location = /login {
   #规则B
}
location ^~ /static/ {
   #规则C
}
location ~ \.(gif|jpg|png|js|css)$ {
   #规则D
}
location ~* \.png$ {
   #规则E
}
location / {
   #规则F
}
```

那么产生的效果如下：

 - 访问根目录 /， 比如 http://localhost/ 将匹配规则 A
 - 访问 http://localhost/login 将匹配规则 B， **http://localhost/register 则匹配规则 F**
 - 访问 http://localhost/static/a.html 将匹配规则 C
 - 访问 http://localhost/a.gif, http://localhost/b.jpg 将匹配规则 D 和规则 E，但是规则 D 顺序优先，规则 E 不起作用，而 http://localhost/static/c.png 则优先匹配到规则 C
 - 访问 http://localhost/a.PNG 则匹配规则 E，而不会匹配规则 D，因为规则 E 不区分大小写。
 - 访问 http://localhost/category/id/1111 则最终匹配到规则 F，因为以上规则都不匹配，这个时候应该是 nginx 转发请求给后端应用服务器，比如 FastCGI（php），tomcat（jsp），nginx 作为反向代理服务器存在。

所以实际使用中， 一般至少有三个匹配规则定义，如下：

```
# 直接匹配网站根，通过域名访问网站首页比较频繁，使用这个会加速处理，官网如是说。
# 这里是直接转发给后端应用服务器了，也可以是一个静态首页
# 第一个必选规则
location = / {
    proxy_pass http://tomcat:8080/index
}

# 第二个必选规则是处理静态文件请求，这是 nginx 作为 http 服务器的强项
# 有两种配置模式，目录匹配或后缀匹配，任选其一或搭配使用
location ^~ /static/ {
    root /webroot/static/;
}
location ~* \.(gif|jpg|jpeg|png|css|js|ico)$ {
    root /webroot/res/;
}

# 第三个规则就是通用规则，用来转发动态请求到后端应用服务器
# 非静态文件请求就默认是动态请求，自己根据实际把握
# 毕竟目前的一些框架的流行，带.php、.jsp后缀的情况很少了
location / {
    proxy_pass http://tomcat:8080/
}
```

<h2 id="93636e7713b2bfbfb6870fa0c2f4052d"></h2>


### ReWrite语法

 - last – 基本上都用这个 Flag
 - break – 中止 Rewirte，不在继续匹配
 - redirect – 返回临时重定向的 HTTP 状态 302
 - permanent – 返回永久重定向的 HTTP 状态 301

<h2 id="b69cd322affa5f72ee270ece8cf29113"></h2>


### 可以用来判断的表达式

 - -f 和 !-f 用来判断是否存在文件
 - -d 和 !-d 用来判断是否存在目录
 - -e 和 !-e 用来判断是否存在文件或目录
 - -x 和 !-x 用来判断文件是否可执行


<h2 id="6cee1d1d18aeb9bff5d6d226016c0eef"></h2>


### if 是邪恶的

 - 避免使用 if 指令
     - 当在 location 区块中使用 if 指令的时候会有一些问题, 在某些情况下它并不按照你的预期运行而是做一些完全不同的事情。 而在另一些情况下他甚至会出现段错误。 
    - 在 location 区块里 if 指令下唯一 100% 安全的指令应该只有:  `return …;   rewrite … last;`

 - 如何替换掉 if
     - 使用 try_files 如果他适合你的需求
     - 在其他的情况下使用 return … 或者 rewrite … last
     - 还有一些情况可能要把 if 移动到 server 区块下( 只有当其他的 rewrite 模块指令也允许放在的地方才是安全的 )。
 
 - 原因
     - if 指令是 rewrite 模块中的一部分, 是实时生效的指令。 在if里写入一些非rewrite指令, 会导致各种错误。


<h2 id="7b9633c105cfd5818516ea5c9612b038"></h2>


### Nginx 静态文件服务

最简单的本地静态文件服务配置:

```
server {
    listen       80;
    server_name www.test.com;
    charset utf-8;
    root   /data/www.test.com;
    index  index.html index.htm;
}
```

这个配置可以用, 但是远远没有发挥 Nginx 的半成功力。

下面是一个改进的配置: 

```
http {
    # 这个将为打开文件指定缓存，默认是没有启用的，max 指定缓存数量，
    # 建议和打开文件数一致，inactive 是指经过多长时间文件没被请求后删除缓存。
    open_file_cache max=204800 inactive=20s;

    # open_file_cache 指令中的inactive 参数时间内文件的最少使用次数，
    # 如果超过这个数字，文件描述符一直是在缓存中打开的，如上例，如果有一个
    # 文件在inactive 时间内一次没被使用，它将被移除。
    open_file_cache_min_uses 1;

    # 这个是指多长时间检查一次缓存的有效信息
    open_file_cache_valid 30s;

    # 默认情况下，Nginx的gzip压缩是关闭的， gzip压缩功能就是可以让你节省不
    # 少带宽，但是会增加服务器CPU的开销哦，Nginx默认只对text/html进行压缩 ，
    # 如果要对html之外的内容进行压缩传输，我们需要手动来设置。
    gzip on;
    gzip_min_length 1k;
    gzip_buffers 4 16k;
    gzip_http_version 1.0;
    gzip_comp_level 2;
    gzip_types text/plain application/x-javascript text/css application/xml;

    server {
        listen       80;
        server_name www.test.com;
        charset utf-8;
        root   /data/www.test.com;
        index  index.html index.htm;
    }
}
```

<h2 id="f9ec24bd7c322b41cb742de2eef83411"></h2>


#### 如何安装和配置基础缓存  Basic Caching

 - proxy_cache_path 用来设置缓存的路径和配置，
 - proxy_cache 用来启用缓存


```
proxy_cache_path /path/to/cache levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m
use_temp_path=off;

server {
    ...
    location / {
        proxy_cache my_cache;
        proxy_pass http://my_upstream;
    }

}

```

参数及对应配置说明:

 1. 本地磁盘目录  /path/to/cache/
 2. levels 在 /path/to/cache/ 设置了一个两级层次结构的目录。
     - 将大量的文件放置在单个目录中会导致文件访问缓慢，所以针对大多数部署，我们推荐使用两级目录层次结构。如果 levels 参数没有配置，则 Nginx 会将所有的文件放到同一个目录中。
 3. keys_zone 设置一个共享内存区，该内存区用于存储缓存键和元数据，有些类似计时器的用途。将键的拷贝放入内存可以使 Nginx 在不检索磁盘的情况下快速决定一个请求是HIT还是MISS，这样大大提高了检索速度。一个 1MB 的内存空间可以存储大约 8000个key，那么上面配置的 10MB 内存空间可以存储差不多 80000 个 key。
 4. max_size 设置了缓存的上限（在上面的例子中是 10G）。
     - 这是一个可选项；如果不指定具体值，那就是允许缓存不断增长，占用所有可用的磁盘空间。
     - 当缓存达到这个上线，处理器便调用 cache manager 来移除最近最少被使用的文件，这样把缓存的空间降低至这个限制之下。
 5. inactive 指定了项目在不被访问的情况下能够在内存中保持的时间。在上面的例子中，如果一个文件在 60 分钟之内没有被请求，则缓存管理将会自动将其在内存中删除，不管该文件是否过期。该参数默认值为 10 分钟（10m）。注意，非活动内容有别于过期内容。 Nginx 不会自动删除由缓存控制头部指定的过期内容（本例中 Cache-Control:max-age=120）。过期内容只有在 inactive 指定时间内没有被访问的情况下才会被删除。如果过期内容被访问了，那么 Nginx 就会将其从原服务器上刷新，并更新对应的inactive计时器。
 6. Nginx 最初会将注定写入缓存的文件先放入一个临时存储区域，use_temp_path=off命令指示 Nginx 将在缓存这些文件时将它们写入同一个目录下。
     - 强烈建议你将参数设置为off来避免在文件系统中不必要的数据拷贝。use_temp_path在 Nginx 1.7版本和 Nginx Plus R6中有所介绍。
 7. proxy_cache 命令启动缓存那些URL与location部分匹配的内容（本例中，为/）。
     - 你同样可以将proxy_cache命令添加到server部分，这将会将缓存应用到所有的那些location中未指定自己的proxy_cache命令的服务中。


<h2 id="1e0c9af54f0620b1412ad6c496f3e341"></h2>


#### 缓存微调 TODO
<h2 id="3d124ed5fca2ee7d48481e391205c5f4"></h2>


#### 跨多硬盘分割缓存 TODO

<h2 id="39fdee1a60aa3d1942ecac9bc4d55129"></h2>


### 反向代理

反向代理 配置

```
worker_processes 1;

pid logs/nginx.pid;
error_log logs/error.log warn;

events {
    worker_connections 3000;
}

http {
    include mime.types;
    server_tokens off;

    ## 下面配置反向代理的参数
    server {
        listen    80;

        ## 1. 用户访问 http://ip:port，则反向代理到 https://github.com
        location / {
            proxy_pass  https://github.com;
            proxy_redirect     off;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        }

        ## 2.用户访问 http://ip:port/README.md，则反向代理到
        ##   https://github.com/.../README.md
        location /README.md {
            proxy_set_header  X-Real-IP  $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass https://github.com/moonbingbing/openresty-best-practices/blob/master/README.md;
        }
    }
}
```

 - proxy_pass 
     - proxy_pass 后面跟着一个 URL，用来将请求反向代理到 URL 参数指定的服务器上。
     - 例如上面例子中的 proxy_pass https://github.com，则将匹配的请求反向代理到 https://github.com。
 - proxy_set_header
     - 默认情况下，反向代理不会转发原始请求中的 Host 头部，如果需要转发，就需要加上这句：proxy_set_header Host $host;
     - 除了上面提到的常用配置项，还有 proxy_redirect、proxy_set_body、proxy_limit_rate 等参数


<h2 id="4eaa6f6da0f943db22ee7df8ed5e8d86"></h2>


### 负载均衡

<h2 id="8c7abf9252c14e770bb8b7a63465baa7"></h2>


#### upstream 负载均衡概要

```
upstream test.net{
    ip_hash;
    server 192.168.10.13:80;
    server 192.168.10.14:80  down;
    server 192.168.10.15:8009  max_fails=3  fail_timeout=20s;
    server 192.168.10.16:8080;
}
server {
    location / {
        proxy_pass  http://test.net;
    }
}
```

 - upstream 是 Nginx 的 HTTP Upstream 模块，
     - 这个模块通过一个简单的调度算法来实现客户端 IP 到后端服务器的负载均衡。
     - 在上面的设定中，通过 upstream 指令指定了一个负载均衡器的名称 test.net。 这个名称可以任意指定，在后面需要用到的地方直接调用即可。

<h2 id="0e5e6e2abcca5d5200772a59178c69a7"></h2>


#### upstream 支持的负载均衡算法

upstream 支持的负载均衡算法

Nginx 的负载均衡模块目前支持 6 种调度算法， 后两项属于第三方调度算法。

 - 轮询（默认）：每个请求按时间顺序逐一分配到不同的后端服务器，如果后端某台服务器宕机，故障系统被自动剔除，使用户访问不受影响。
     - Weight 指定轮询权值，Weight 值越大，分配到的访问机率越高，主要用于后端每个服务器性能不均的情况下。
 - ip_hash：每个请求按访问IP的hash结果分配，
     - 这样来自同一个IP的访客固定访问一个后端服务器，有效解决了动态网页存在的session共享问题。
 - fair：这是比上面两个更加智能的负载均衡算法。此种算法可以依据页面大小和加载时间长短智能地进行负载均衡，也就是根据后端服务器的响应时间来分配请求，响应时间短的优先分配。
     - Nginx本身是不支持fair的，如果需要使用这种调度算法，必须下载Nginx的upstream_fair模块。
 - url_hash：此方法按访问 url 的 hash 结果来分配请求，使每个 url 定向到同一个后端服务器，可以进一步提高后端缓存服务器的效率。
     - Nginx 本身是不支持 url_hash 的，如果需要使用这种调度算法，必须安装 Nginx 的 hash 软件包。
 - least_conn：最少连接负载均衡算法，简单来说就是每次选择的后端都是当前最少连接的一个 server(这个最少连接不是共享的，是每个 worker 都有自己的一个数组进行记录后端 server 的连接数)。
 - hash：这个 hash 模块又支持两种模式 hash, 一种是普通的 hash, 另一种是一致性 hash(consistent)。


<h2 id="b1577d4475a60b4aee2a200c3b54108f"></h2>


#### upstream 支持的状态参数

 - down：表示当前的server暂时不参与负载均衡。
 - backup：预留的备份机器。
     - 当其他所有的非 backup 机器出现故障或者忙的时候，才会请求 backup 机器，因此这台机器的压力最轻。
     - 当负载调度算法为 ip_hash 时，后端服务器在负载均衡调度中的状态不能是 backup。
 - max_fails：允许请求失败的次数，默认为 1。
     - 当超过最大次数时，返回 proxy_next_upstream 模块定义的错误。
 - fail_timeout：在经历了 max_fails 次失败后，暂停服务的时间。
     - max_fails 可以和 fail_timeout 一起使用。

<h2 id="0c23468b07d39fbbf4b89831f45c318d"></h2>


#### 配置 nginx 进行健康状态检查

```
upstream webservers {
    server 192.168.18.201 weight=1 max_fails=2 fail_timeout=2;
    server 192.168.18.202 weight=1 max_fails=2 fail_timeout=2;
}
```

<h2 id="42f78f76deabbbea593e4d7fb7fc4db6"></h2>


### Nginx 陷阱和常见错误

 - 糟糕的配置: 把 root 放在 location 区块内
 - 重复的 index 指令
 - 用 if 检查文件是否存在
     - 使用 if 指令来判断文件是否存在是很可怕的，如果你在使用新版本的 Nginx ， 你应该看看 try_files 。
 - 脚本文件名里面的 FastCGI 路径
     - 推荐: fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
     - 糟糕: fastcgi_param  SCRIPT_FILENAME    /var/www/yoursite.com/$fastcgi_script_name;
 - 费力的 rewrites
     - 糟糕的配置:     rewrite ^/(.*)$ http://example.com/$1 permanent;
    - 好点儿的配置：    rewrite ^ http://example.com$request_uri? permanent;
    - 更好的配置：    return 301 http://example.com$request_uri;
 - 忽略 http:// 的rewrite
     - 糟糕的配置：rewrite ^ example.com permanent;
    - 推荐的配置：rewrite ^ http://example.com permanent;    
 - 代理所有东西
     - 把 所有东西 都丢给了 PHP 。 Apache 可能要这样做，但在 Nginx 里你不必这样。 
     - 换个思路，try_files 有一个神奇之处，它是按照特定顺序去尝试文件的。 这意味着 Nginx 可以先尝试下静态文件，如果没有才继续往后走。 
     - 这样PHP就不用参与到这个处理中，会快很多。 特别是如果你提供一个1MB图片数千次请求的服务，通过PHP处理还是直接返回静态文件呢？ 

```
server {
    server_name _;
    root /var/www/site;
    location / {
        try_files $uri $uri/ @proxy;
    }
    location @proxy {
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass unix:/tmp/phpcgi.socket;
    }
}
```

 - 代理所有东西 Cont.
     - 如果请求的 URI 存在， Nginx 会处理掉； 如果不存在，检查下目录是不是存在，是的话也可以被 Nginx 处理； 只有在 Nginx 不能直接处理请求的URI的时候，才会进入 proxy 这个 location 来处理。
 - 配置的修改没有起效
     - 浏览器缓存。你的配置可能是对的，但怎么尝试结果总是不对，百思不得其解。 罪魁祸首是你的浏览器缓存。当你下载东西的时候，浏览器做了缓存。
     - 使用 curl 避免
 - VirtualBox
    - 如果你在 VirtualBox 的虚拟机中运行 Nginx ，而它不工作，可能是因为 sendfile() 引起的麻烦。  
    - 只用简单的注释掉 sendfile 指令，或者设置为 off。 该指令大都会写在 Nginx .conf 文件中： `sendfile off;`
 - 丢失（消失）的 HTTP 头
     - 如果你没有明确的设置 `underscores_in_headers on;` , Nginx 将会自动丢弃带有下划线的 HTTP 头(根据 HTTP 标准，这样做是完全正当的). 
     - 这样做是为了防止头信息映射到 CGI 变量时产生歧义，因为破折号和下划线都会被映射为下划线。
 - 没有使用标准的 Document Root Location
     - 在所有的文件系统中，一些目录永远也不应该被用做数据的托管。这些目录包括 / 和 /root 。 
     - 你永远不应该使用这些目录作为你的 document root。    
     - 服务器很容易变成肉鸡
 - 使用默认的 Document Root
     - 不要假设默认的 document root 里面的数据在 升级系统 的时候会原封不动。
 - 使用主机名来解析地址
     - `server http://someserver;`
     - 使用主机名对应 IP 地址，而不是主机名。 这可以防止 Nginx 去查找 IP 地址，也去掉了去内部、外部解析程序的依赖。
 - 在 HTTPS 中使用 SSLv3
     - 由于 SSLv3 的 POODLE 漏洞， 建议不要在开启 SSL 的网站使用 SSLv3。 你可以简单粗暴的直接禁止 SSLv3， 用 TLS 来替代：
     - `ssl_protocols TLSv1 TLSv1.1 TLSv1.2;`
