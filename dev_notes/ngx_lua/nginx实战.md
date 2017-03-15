...menustart

 - [nginx 实战](#8b1ed3f8e89a45a45f67fcc9212623bf)
	 - [日志分析工具](#9f9644e514e387c31a9e7e520eec5756)
	 - [支持 HTTP Range](#6ddbbf1feb5c733b7f27c100ccb4cf0d)
	 - [colorize output](#7d8e924c3c4202c090b5a4ee59044419)

...menuend


<h2 id="8b1ed3f8e89a45a45f67fcc9212623bf"></h2>

# nginx 实战

<h2 id="9f9644e514e387c31a9e7e520eec5756"></h2>

## 日志分析工具

goaccess


<h2 id="6ddbbf1feb5c733b7f27c100ccb4cf0d"></h2>

## 支持 HTTP Range

配置文件中加入:

```
add_header Accept-Ranges bytes; # 断点下载
```


<h2 id="7d8e924c3c4202c090b5a4ee59044419"></h2>

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
 - pattern 以 ; 分割； 越往前优先级越高
 - $& 表示整个匹配
 - $1 表示 \1 , $2 表示 \2


