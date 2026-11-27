[](...menustart)

- [performance profile](#b3b2af02ef1b4b395df5845889bc8fd9)
    - [JAVA](#c71e8d17d41c21de0d260881d69662ff)
    - [Node](#6c3a6944a808a7c0bbb6788dbec54a9f)

[](...menuend)


<h2 id="b3b2af02ef1b4b395df5845889bc8fd9"></h2>

# performance profile

<h2 id="c71e8d17d41c21de0d260881d69662ff"></h2>

## JAVA

```bash
wget https://github.com/async-profiler/async-profiler/releases/download/v3.0/async-profiler-3.0-macos.zip
unzip async-profiler-3.0-macos.zip
cd async-profiler-3.0-macos/bin
```

MacOS 上有权限问题， 需要 sudo运行。 并且macOS 10.15+ 对 attach 有严格权限限制（System Integrity Protection, SIP）。
终端或 Java 进程可能没有被允许调试。

解决办法：
系统偏好设置 → 安全性与隐私 → 隐私 → 开发者工具 → 允许 Terminal（或你用的 IDE）访问。


```bash
java <your-java-app> &

PID=$!

# APROF=./bin/aprof
if [ -n "$APROF" ]; then
    echo $PID
    # 等待程序初始化
    sleep 2

    rm -f result.svg
    echo "Profiling... $PID, if it not stop, manually kill it!"
    $APROF collect -d 86400 -f flamegraph.html $PID
    open flamegraph.html
fi
```


<h2 id="6c3a6944a808a7c0bbb6788dbec54a9f"></h2>

## Node

```bash 
node --prof server.js

运行一段时间后会生成 isolate-*.log

用 node --prof-process isolate-*.log 分析热点函数
```


