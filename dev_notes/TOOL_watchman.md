...menustart

 - [facebook watchman](#b50e0466a03291f83abf9cda054a962f)
     - [watch 某个目录](#d5725e1e142236069d95ca3b37eb719d)
     - [删除 某个watched 目录](#151d08852b1d146ac7c81968d3d018b0)
     - [查看 watch list](#71ddfb561fa5139ff5a2ab4f01e85d1b)
     - [设置trigger](#0014c3e14eb578443ec0f3caf758c03c)
     - [删除某个 trigger](#42f6410136119df6991d9591beb26ccb)
     - [查看 trigger 列表](#a1f2ce9a6b0ca6c348836701115c6454)
     - [关闭watchman 服务](#3947fc934eb080775ca62aa126dad96b)
     - [查看 watchman 相关路径设置](#0565f8f66838fec3a5ad3909c08ff395)
     - [一个简单的 监视 lua 文件改动的例子](#b99af44161fb3b1829c3e2067544f1b7)

...menuend


<h2 id="b50e0466a03291f83abf9cda054a962f"></h2>


#facebook watchman

<h2 id="d5725e1e142236069d95ca3b37eb719d"></h2>


### watch 某个目录

```bash
watchman watch /path/to/dir
```

<h2 id="151d08852b1d146ac7c81968d3d018b0"></h2>


### 删除 某个watched 目录

```bash
watchman watch-del /path/to/dir
```

<h2 id="71ddfb561fa5139ff5a2ab4f01e85d1b"></h2>


### 查看 watch list

```bash
watchman watch-list
```

<h2 id="0014c3e14eb578443ec0f3caf758c03c"></h2>


### 设置trigger

```bash
watchman -- trigger /path/to/dir triggername [patterns] -- [cmd]
```

patterns 必须使用单引号 '' , 如  '*.txt'

match 模式：  '*.lua' , 只会出发 根目录下的 lua 文件

正则查询:  -p '.lua$' , 所有 .lua 后缀的文件

<h2 id="42f6410136119df6991d9591beb26ccb"></h2>


### 删除某个 trigger 

```bash
watchman trigger-del /path/to/dir triggername
```

<h2 id="a1f2ce9a6b0ca6c348836701115c6454"></h2>


### 查看 trigger 列表

```bash
watchman trigger-list /path/to/dir
```

<h2 id="3947fc934eb080775ca62aa126dad96b"></h2>


### 关闭watchman 服务

```bash
watchman shutdown-server
```

<h2 id="0565f8f66838fec3a5ad3909c08ff395"></h2>


### 查看 watchman 相关路径设置

```bash
ps -ef | grep watchman
```


<h2 id="b99af44161fb3b1829c3e2067544f1b7"></h2>


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

        #flatten dist path , all lua file will in same flat folder
        _,v  = os.path.split( v )
        
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


