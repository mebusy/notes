
# Centos7


## YouCompleteMe

 - yum 安装 clang

```
CC=`which clang` CXX=`which clang++`  ./install.py ......
```

## mono

```bash
yum install yum-utils
rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
yum-config-manager --add-repo http://download.mono-project.com/repo/centos7/
```

 - build c# project 

```bash
xbuild /p:Configuration=Release xxx.sln
```

## firewall 

open a port :

```bash
# add ssh port as permanent opened port
firewall-cmd --zone=public --add-port=22/tcp --permanent
```


Then, you can reload rules to be sure that everything is ok

```bash
firewall-cmd --reload
```

## Mysql

```
yum install mariadb-server mariadb  mariadb-devel

systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动
```


