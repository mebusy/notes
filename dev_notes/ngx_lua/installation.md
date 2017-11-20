...menustart

 - [ngx_lua 安装,使用](#737edafc16acd1a5ff7fa0d34d5860a7)

...menuend


<h2 id="737edafc16acd1a5ff7fa0d34d5860a7"></h2>

## ngx_lua 安装,使用

 - OSX with homebrew 
     - brew install homebrew/nginx/nginx-full --with-lua-module --with-echo-module --with-http_ssl_module

 - 验证是否链了luajit
     - linux , `ldd`
         - `ldd  nginx | grep lua`
     - OSX otool
         - `otool -L /usr/local/nginx/sbin/nginx`

 - 新建项目
     - 创建 openresty-test 目录，并在该目录下创建 logs 和 conf 子目录分别用于存放日志和配置文件。
     - 拷贝 nginx.conf , mime.types 到 conf 目录
         - cp /usr/local/etc/nginx/mime.types conf/
         - cp /usr/local/etc/nginx/nginx.conf conf/
     - 启动
         - nginx -p openresty-test -c conf/nginx.conf     

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