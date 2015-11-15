#facebook watchman

### watch 某个目录

```bash
watchman watch /path/to/dir
```

### 删除 某个watched 目录

```bash
watchman watch-del /path/to/dir
```

### 查看 watch list

```bash
watchman watch-list
```

### 设置trigger

```bash
watchman -- trigger /path/to/dir triggername [patterns] -- [cmd]
```

patterns 必须使用单引号 '' , 如  '*.txt'

### 删除某个 trigger 

```bash
watchman trigger-del /path/to/dir triggername
```

### 查看 trigger 列表

```bash
watchman trigger-list /path/to/dir
```

### 关闭watchman 服务

```bash
watchman shutdown-server
```

### 查看 watchman 相关路径设置

```bash
ps -ef | grep watchman
```



