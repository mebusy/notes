

# Nginx 转发 mysql 链接

nginx从1.9.0开始，新增加了一个stream模块，用来实现四层协议的转发、代理或者负载均衡等。

注意 stream和http是同级别的，不要放入http里面。

```bash
stream {
    upstream mysql33060 {
        server 10.192.91.74:33060 ;
    }
    upstream mysql33061 {
        server 10.192.91.74:33061 ;
    }


    server {
        listen 33060;
        # proxy_connect_timeout 10s;
        #proxy_timeout 300s;
        proxy_pass mysql33060;
    }


    server {
        listen 33061;
        # proxy_connect_timeout 10s;
        #proxy_timeout 300s;
        proxy_pass mysql33061;
    }

}
```
