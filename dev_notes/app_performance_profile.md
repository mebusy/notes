# performance profile

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


## Node

```bash 
node --prof server.js

运行一段时间后会生成 isolate-*.log

用 node --prof-process isolate-*.log 分析热点函数
```


