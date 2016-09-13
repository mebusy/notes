
# nginx 实战

## 日志分析工具

goaccess


## 支持 HTTP Range

配置文件中加入:

```
add_header Accept-Ranges bytes; # 断点下载
```