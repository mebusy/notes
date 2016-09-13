
# nginx 实战

## 日志分析工具

goaccess


## 支持 HTTP Range

配置文件中加入:

```
add_header Accept-Ranges bytes; # 断点下载
```


## colorize output

30-37, select foreground color
40-47, select background color

Intensity | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
--- | --- | --- | --- | --- | --- | --- | --- | ---
Normal | Black | Red | Green | Yellow | blue | Megenta | Cyan | White



 - example : tail -f logs/error.log | perl -pe 's/error/\e[1;31m$&\e[0m/g;s/html/\e[1;31m$&\e[0m/g'  
 - \e[30;47m 表示 black letters on white background
 - \e[31m 表示 red
 - \e[1;31m 表示 bright red
 - 最后的 \e[0m 表示颜色复位


