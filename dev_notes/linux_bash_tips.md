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
