...menustart

- [Nginx 转发 websocket secure](#7c5ba97417d6a694ecb09b70b7874040)
    - [1 准备好 ca 证书](#a531b2993886b54ffe0570554f93f575)
    - [2 配置 nginx.conf](#d1981f613ae630bff78fe54af74f9c17)
- [Nginx配置proxy_pass转发的/路径问题](#f000b6463e33ea7670c393ee0b4927bf)

...menuend


<h2 id="7c5ba97417d6a694ecb09b70b7874040"></h2>


# Nginx 转发 websocket secure

<h2 id="a531b2993886b54ffe0570554f93f575"></h2>


## 1 准备好 ca 证书

https://github.com/mebusy/codeLib/tree/master/selfSignSSL

<h2 id="d1981f613ae630bff78fe54af74f9c17"></h2>


## 2 配置 nginx.conf

```
upstream weapp {
    server 10.192.81.132:5757;
}
upstream wss {
    server 10.192.81.132:5001;
}

server {
    listen 443 ssl;
    server_name  LB ;

    ssl on;
    ssl_certificate     /usr/local/openresty/nginx/ssl/10.192.81.132.crt;
    ssl_certificate_key /usr/local/openresty/nginx/ssl/10.192.81.132.key;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;


    location /wss {
        proxy_pass  http://wss;
        proxy_set_header            Host $host;
        proxy_set_header            X-real-ip $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    location / {
        proxy_pass  http://weapp;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/local/openresty/nginx/html;
    }
}
```

<h2 id="f000b6463e33ea7670c393ee0b4927bf"></h2>


# Nginx配置proxy_pass转发的/路径问题

- 在nginx中配置proxy_pass时，如果是按照^~匹配路径时,要注意proxy_pass后的url最后的/,当加上了/，相当于是绝对根路径，则nginx不会把location中匹配的路径部分代理走;如果没有/，则会把匹配的路径部分也给代理走。


```
location ^~ /static_js/
{
proxy_cache js_cache;
proxy_set_header Host js.test.com;
proxy_pass http://js.test.com/;
}
```

- 如上面的配置，如果请求的url是http://servername/static_js/test.html 会被代理成http://js.test.com/test.html

- 而如果这么配置

```
location ^~ /static_js/
{
proxy_cache js_cache;
proxy_set_header Host js.test.com;
proxy_pass http://js.test.com;
}
```

- 则会被代理到http://js.test.com/static_js/test.htm

- 当然，我们可以用如下的rewrite来实现/的功能

```
location ^~ /static_js/
{
proxy_cache js_cache;
proxy_set_header Host js.test.com;
rewrite /static_js/(.+)$ /$1 break;
proxy_pass http://js.test.com;
}
```
