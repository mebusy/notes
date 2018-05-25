# android DMP 文件解析


##  安装 google breakpad

 - build on linux

```
git clone https://github.com/google/breakpad.git  git_google-breakpad-read-only
cd git_google-breakpad-read-only
git clone https://chromium.googlesource.com/linux-syscall-support src/third_party/lss

./configure
make
```

##  把dmp文件转为txt文件

### 1 建立一个空文件夹，里面放进四个必要文件
 
 - 先copy dump_syms 和 minidump_stackwalk 

```
mkdir mybin
cp src/tools/linux/dump_syms/dump_syms  mybin
cp src/processor/minidump_stackwalk mybin
```

 - 然后 拷贝 dmp 文件 , 游戏 .so 文件到  my bin


### 2 准备symbols

 - 1 导出symbols文件

```
./dump_syms libgame.so > libgame.so.sym
```

 - 2 建立symbols文件夹

`创建文件夹 symbols/libgame.so/2D1C163A1347A1190B26F10560E926CE0`

后面那个一堆乱数字是前一步生成的“libgame.so.sym”文件的第一行复制出来的   `head libgame.so.sym`


 - 3 复制libgame.so.sym到新文件夹中，最终它的路径：

symbols/libgame.so/2D1C163A1347A1190B26F10560E926CE0/libgame.so.sym


---

 - 以上三步可以用下面的 脚本完成

```bash
# prepareSymbol.sh 
./dump_syms $1 > $1.sym

wait &&

PATH_NAME=`head $1.sym | grep -P -o '(?<=MODULE Linux arm )(\w+)'`


# echo $PATH_NAME

DIST=symbols/$1/$PATH_NAME
mkdir -p $DIST

mv $1.sym   $DIST
```


### 3. 导出 文本信息

```
./minidump_stackwalk dd3023f-f8bd-37c3-46e78f56-151901b1.dmp symbols/ > DmpInfo.txt
```

