...menustart

 - [ngx_lua 安装,使用](#737edafc16acd1a5ff7fa0d34d5860a7)
 - [run openresty in docker](#8cf251cb8d6c4c7584d34bd8e60273c8)

...menuend


<h2 id="737edafc16acd1a5ff7fa0d34d5860a7"></h2>

-----
-----

## ngx_lua 安装,使用


 - 验证是否链了luajit
     - linux , `ldd`
         - 
         ```bash
         ldd  `which nginx` | grep lua
         ```
     - OSX otool
         - `otool -L /usr/local/nginx/sbin/nginx`

 - 常用命令
     - nginx 修改端口
         - `nginx.conf`
     - nginx 指定配置文件
         - `nginx -c /opt/nginx/conf/nginx.conf` 启动时，指定配置文件    
         - nginx.conf 会 `include mime.types` 文件， 所以要把 mime.types 拷贝到新的 配置文件目录。
     - 查看 nginx 配置信息
         - nginx -V    
     - nginx 检查修改后的配置的正确性
         - sudo /usr/local/nginx/sbin/nginx -t
     - nginx 重启
        - sudo /usr/local/nginx/sbin/nginx -s reload
    - nginx 停止
        - 1. 查找nginx master 进程
            - `ps -ef | grep nginx`
        - 2. 平滑关闭 
            - `sudo kill -QUIT 进程号`
    - nginx 日志清理后， 日志不再生成的问题
        - 需要发送 USE1 信号给 nginx master 进程重新打开日志文件
        -
        ```bash
        kill -USR1 `ps axu | grep "nginx: master process" | grep -v grep | awk '{print $2}'`
        ```
    - 支持 HTTP Range
        - 配置文件中加入:
        -
        ``` 
        add_header Accept-Ranges bytes; # 断点下载
        ```



<h2 id="8cf251cb8d6c4c7584d34bd8e60273c8"></h2>

-----
-----

## run openresty in docker 

```bash
serverName=hdaserver

if [ "$1" == "force" ] ; then
    docker rm -f ${serverName}
fi

if [ "$(docker ps -aq -f name=${serverName})" ]; then
    echo "run an existing server "
    docker stop ${serverName} > /dev/null
    docker start ${serverName} > /dev/null
else

echo "run a new server instance"

mkdir -p logs
mkdir -p staticRes/ads

chmod -R 777 staticRes

NET_CONFIG="--net=host"
if [ `uname` == "Darwin" ] ; then
    NET_CONFIG="-p 9000:9000 -p 9011:9011 -p 9012:9012"
    echo ${NET_CONFIG}
fi

docker run --restart unless-stopped -d --name ${serverName} ${NET_CONFIG} --ulimit nofile=200000:200001 \
    -v `pwd`/conf/:/etc/nginx/conf.d/  \
    -v `pwd`/logs:/usr/local/openresty/nginx/logs \
    -v `pwd`/nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf \
    -v `pwd`/lua/:/usr/local/openresty/nginx/lua/ \
    -v `pwd`/luaRedis/:/usr/local/openresty/nginx/luaRedis/ \
    -v `pwd`/webTools/:/usr/local/openresty/nginx/webTools/ \
    -v `pwd`/staticRes/:/usr/local/openresty/nginx/staticRes/ \
    openresty/openresty:trusty

fi
```
