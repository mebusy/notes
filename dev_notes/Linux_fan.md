
# Linux

## 2.2 用户的身份

### 2.2.3  /etc/passwd 文件查看用户

```
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
...
byqi:x:16220:100:Qi Bin Yi - Senior Gameplay Programmer - APAC - SHA:/home/byqi:/bin/bash
```

 - 存放用户基本信息
    - 每行一个用户, 由 `:` 分割成7个字段，结构如下
        - 用户名:密码:UID:GID:用户全名:home目录:shell
    - 没有真正的密码，只有一个 `x` ,  真正的密码保存在 `/etc/shadow` 文件内
 - 虽然系统只区分 0和非0的 UID或GID, 但是在习惯上还是进行了一些分段的
    - 0 是给 root的
    - 1~499 属于系统用户的
    - 500~ 2³²-1 分配给普通用户

### 2.2.4  /etc/group 文件查看组

```
#  cat /etc/group
root:x:0:
bin:x:1:
...
nobody:x:99:
users:x:100:
...
security:x:31336:atremblay,mloll,lgordon,tmoreggia  ...
```

 - `/etc/passwd` 中 GID的来源
 - 组名:用户组密码:GID:用户组内的用户名
 - 用户组内的用户名
    - 可以看到 有的组 有组内用户名，有的没有
    - `/etc/passwd` 中， 某个用户的 GID字段代表的就是专职用户组, 或 初始用户组
        - 对于专职的用户来讲，是可以不出现在 用户组内的用户名 这个字段的。
    - 使用 `groups` 命名 可以查看所有的 "支持用户组" , "支持用户组" 列表的 第一个出现的那个组还有一个称呼: "有效用户组"


### 2.2.5 管理用户/组

 - `useradd` 在任何 Linux发行版 都是一样的 , `adduser` 的实现 各不相同 
 - 添加一个用户

```
useradd jagen
```

 - 设置用户密码

```
passwd jagen
```

### 2.2.6 夺面双雄 -- 利用 sudo 假借身份

 - 给某个用户赋予 sudo 特权，实际上就是更改 `/etc/sudoers` 文件

```
root          ALL=(ALL) ALL
```

 - 它的含义是说 root 用户可以使用 sudo 特权，以root 权限执行任何命令 (一句废话)
 - 给普通用户添加 sudo 特权

```
jagen          ALL=(ALL) ALL
```

 - 给用户组(i.e. wheel)的所有用户 添加sudo 特权

```
%wheel         ALL=(ALL) ALL
## Same thing without a password
# %wheel    ALL=(ALL)   NOPASSWD: ALL
```

 - 添加部分 命令的sudo特权
    - 如下 sudo 仅能执行 如下两个命令

```
%users ALL=/sbin/mount  /mnt/cdrom,  /sbin/umount  /mntcdrom
```

 - `su` 命令可以临时切换用户，  默认是切换到 root 用户
    - `su` 命令 需要输入 目标用户的密码
    - `exit` 切换回 原始用户
 - 如果使用 `su` 成功切换到 root 用户下, 那么就可以在不知道密码的情况下，切换到 任意用户， 比如执行 `su jagen -`
 - 顺便说一下，拥有sudo特权的用户啊，是可以通过执行 `sudo su -` 或 `sudo su` 直接使用自己的密码 切换成root 用户
    - 原理是 root 用户使用 `su` 命令切换到 任何用户都不提示密码
    - 这显然是不安全的， 应该在 `/etc/sudoers` 文件中明确禁止 su 被 sudo 特权执行


### 2.2.7 我是谁

```bash
[byqi]$ whoami
byqi
[byqi]$ who am i
byqi     pts/0        2018-07-13 03:17 (10.192.81.82)
[byqi]$ who
byqi     pts/0        2018-07-13 03:17 (10.192.81.82)
[byqi]$ sudo su 

[root]# whoami
root
[root]# who am i
byqi     pts/0        2018-07-13 03:17 (10.192.81.82)
[root]# who
byqi     pts/0        2018-07-13 03:17 (10.192.81.82)
```

 - 换脸大法 能骗过 `whoami` , 但骗不过 `who am i` 和 `who`
 - 要解释背后的运行机制，  需要引入两个概念
    - 实际用户 UID : 用户登陆时所用的用户
    - 有效用户 EUID (Effective UID) : 当前执行操作的用户
 - 如果有些shell 必须只能某些用户来执行， 使用`su`切换的都不行，那么就需要利用 `who am i` 这个命令来确认了



## 2.3 文件和它与权限的关系

### 2.3.2 文件属性和权限

 - linux 系统中，每个文件都会由一个 特定的拥有者(一般是创建它的用户) 和 所属的 用户组, 这是属于它的固有属性
 - 文件可以利用这两个固有属性 来规定它的拥有者或者其所属用户组内的用户 是否拥有对它的 访问权利，即 读，写，执行
    - 另外还规定了 其他不相关人等，也就是 第三个固有属性，对它的 读写执行的权限。
 - 这3个固有属性 和 3个权利 合起来，就构成了文件的针对系统中所有用户的访问控制。

```bash
# ls -l
drwxr-xr-x. 10 root root 4096 Jul  2 23:24 lua
-rw-r--r--.  1 root root 3702 Jul  9 01:23 nginx.conf
```

```
-rw-r--r--.       1     root      root       3702       Jul  9 01:23    nginx.conf
文件类型和权限  连接数  owner  所属用户组   文件大小    最后修改日期    文件名
```

```
-           rwx   r-x      r-x
文件类型   owner  用户组   其他
```

文件类型 |  说明
--- | --- 
 `-`| 普通文件
 d  | 目录
 l  |  软/硬 连接
 b |  块设备，如磁盘等保存大块数据的设备
 c | 字符设备，如鼠标，键盘
 s | socket 文件
 p | 命名管道文件


 - 文件权限 
    - 对于目录
        - `x` 权限可以控制用户是否能够打开它
        - 如果想使用 ls 命令 来查看这个目录下的文件列表， 则必须用于 `r` 权限, 否则即便能进入，也无济于事
        - 如果要在目录中创建文件， 则要有 `w`权限
    - 对于文件
        - 读取需要 `r` , 编辑器编辑需同时具备 `r` 和 `w` 两个权限
        - 如果一个文件是shell脚本或者其他可执行的文件，要能够被执行，应当具备`x` 权限
 - 隐藏属性
    - linux文件的隐藏属性，就是在 文件名前 添加 `.`

### 2.3.3 文件连接到底是什么

 - 文件的 “连接数”到底是什么鬼？
 - linux 所使用的文件系统是一种基于 inode的文件系统
    - inode 是 索引节点， 是所有类 Unix 操作系统中的一种数据结构
    - 每一个新创建的文件都会被 分配一个 唯一的 inode
 - 我们可以把 inode 简单理解成一个指针， 它指向的是文件所在的磁盘中的物理位置
    - `ls -l ` 命令显示的文件属性，也保存在 inode中
 - 系统是通过inode定位每一个文件的，而不是通过文件名.
    - 所以通常情况， 为了提高文件系统的执行效率，访问过的文件的inode会缓存在内存中。 
    - “连接数” 这个属性，就是 inode的引用计数。
    - linux 允许一个文件拥有多个名字， 也就是说， 文件名只是 相当于对inode的一次引用
 - `ls` 命令建立的软连接 ，也称符号连接， 不是真正的连接
    - 和 windows 的快捷方式类似， 只是一个普通文件
    - 软连接的文件属性和目标文件属性完全不同
    - 软连接 也要占据一个新的 inode, 是一个新的文件， 不影响 inode 的引用计数
 - 硬连接 的属性和 目标文件的属性 完全相同，因为引用的是 相同的inode, 仅仅将 inode的引用计数进行了 +1 操作.
 - 软硬连接 在使用的时候区别不大， 都相当于 是一个文件具有不同的路径和文件名
    - 硬连接 使得同一个文件 能够拥有不同的路径, 还能防止 恶意被删除.

### 2.3.4 修改文件的属性和权限

 - 想要操作文件的属性和权限，你必须具备对文件的写权利，或者root

修改内容 | 命令
--- | ---
文件名 | mv
最后更新时间 | touch
用户组 | chgrp (不常用，chown也能做)
文件权限 | chmod 

```
chown [-R] username filename
chown [-R] username:group filename
```

```
# chmod
数字法:
    r=4, w=2, x=1
    chmod 700 .bashrc
文字法
    u,g,o,a  (user, group, other, all)
    +,-,=
    i.e. 去掉.bashrc 执行权限
    chmod a-x .bashrc
    chmode ugo-x .bachrc
```

### 2.3.5 深入文件权限

 - 

