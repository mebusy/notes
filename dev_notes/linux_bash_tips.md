# Linux Bash Tips

## 合并多个进程的输出到stdout

```bash
#!/usr/bin/env bash

# tested on  MacOS

set -euo pipefail

tmpdir="$(mktemp -d)"
fifo="$tmpdir/merged.fifo"
mkfifo "$fifo"

nohup cmd1 >"$fifo" 2>&1 & p1=$!
nohup cmd2 >"$fifo" 2>&1 & p2=$!
nohup cmd3 >"$fifo" 2>&1 & p3=$!

cleanup() {
  kill "$p1" "$p2" "$p3" 2>/dev/null || true
  rm -rf "$tmpdir"
}
trap cleanup INT TERM EXIT

bunyan <"$fifo"
```

example 2:

```bash
#!/bin/sh

set -euo pipefail

tmpdir="$(mktemp -d)"
fifo="$tmpdir/merged.fifo"
mkfifo "$fifo"

pids=()

# 10 times loop
for i in $(seq 1 10); do
    # Start a background process that writes to the FIFO
    sh -c  "while :; do echo $i `date`; sleep 1;  done"  >"$fifo" 2>&1 & pids+=("$!")
done



cleanup() {
    # 避免重复触发 cleanup 时因 set -e 直接退出
    set +e
    # print pids
    echo "Cleaning up... PIDs: ${pids[*]}"

    # 关键：把 $i 的值传进去（用 env），避免外层提前展开/引用问题
    if ((${#pids[@]})); then
        kill "${pids[@]}"  2>/dev/null || true
    fi
    rm -rf "$tmpdir"
}

trap cleanup INT TERM EXIT

cat <"$fifo"
```
