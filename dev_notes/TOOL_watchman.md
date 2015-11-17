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
match 模式：  '*.lua' , 只会出发 根目录下的 lua 文件
正则查询:  -p '.lua$' , 所有 .lua 后缀的文件

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


### 一个简单的 监视 lua 文件改动的例子

```bash
WATCH_ROOT=$PWD/../Resources/lua_scripts
DIST_FOLDER=$PWD/tmp
echo python $PWD/watch.py $WATCH_ROOT $DIST_FOLDER
watchman -- trigger $WATCH_ROOT watchLua  -p '.lua$'  -- python $PWD/watch.py $WATCH_ROOT $DIST_FOLDER
```

监视 Resources/lua_scripts, 如果有 lua 文件发生修改，调用 watch.py 脚本，处理文件同步。

```python
import os,sys , shutil


if len( sys.argv )>3:
	#print "py notifie:" , sys.argv[1:]
	WATCH_ROOT = sys.argv[1]
	DIST_FOLDER = sys.argv[2]

	print "all args:" , sys.argv[1:]

	if not os.path.exists( DIST_FOLDER ):
		os.makedirs( DIST_FOLDER )


	for v in sys.argv[3:]:
		print "py notifie:" , v

		full_path_src = os.path.join(  WATCH_ROOT , v  )

		# full path of dist file
		full_path_dist = os.path.join( DIST_FOLDER, v ) 
		path , f = os.path.split( full_path_dist )
		path2createOrDelete =  path

		#try to make dir
		if not os.path.exists( path2createOrDelete ):
			os.makedirs( path2createOrDelete )
		pass

		if os.path.exists( full_path_src  ):
			shutil.copy( full_path_src , full_path_dist )

		# src not exists, but dist exists
		elif os.path.exists( full_path_dist  ) :
			os.remove(full_path_dist)
			
```


