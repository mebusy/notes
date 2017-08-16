...menustart

 - [Centos7](#8db8d64778c367a62ad2b609fd6c2095)
	 - [YouCompleteMe](#067a2f97475db1552b986c54fc094f60)
	 - [mono](#654db8a14a5f633b9ba85ec92dc51f7c)
	 - [firewall](#36e5371ad91c9d2d09e9d7c0e76055db)
	 - [Mysql](#9edb3c572b56b91542af659480518681)

...menuend


<h2 id="8db8d64778c367a62ad2b609fd6c2095"></h2>

# Centos7


<h2 id="067a2f97475db1552b986c54fc094f60"></h2>

## YouCompleteMe

 - yum 安装 clang

```
CC=`which clang` CXX=`which clang++`  ./install.py ......
```

<h2 id="654db8a14a5f633b9ba85ec92dc51f7c"></h2>

## mono

```bash
yum install yum-utils
rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
yum-config-manager --add-repo http://download.mono-project.com/repo/centos7/

yum -y install mono-complete  
# mono-core mono-devel ? I forgot the exact command ...
```

 - build c# project 

```bash
xbuild /p:Configuration=Release xxx.sln
```

<h2 id="36e5371ad91c9d2d09e9d7c0e76055db"></h2>

## firewall 

open a port :

```bash
# add ssh port as permanent opened port
firewall-cmd --zone=public --add-port=22/tcp --permanent
```


Then, you can reload rules to be sure that everything is ok

```bash
firewall-cmd --reload

firewall-cmd --zone=public --list-ports
```

<h2 id="9edb3c572b56b91542af659480518681"></h2>

## Mysql

```
yum install mariadb-server mariadb  mariadb-devel

systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动
```

To make Mysql case sensitive,  find and modify `lower_case_table_names` to 1:

```
vi /etc/my.cnf

[mysqld]
lower_case_table_names=2
```

Delete anonymous user:

```
mysql> use mysql 
mysql> delete from user where user=''; 
mysql> FLUSH PRIVILEGES;
```

Create a database account, username and password is “kbe”:

```
mysql> grant all privileges on *.* to kbe@'%' identified by 'kbe';
mysql> grant select,insert,update,delete,create,drop on *.* to kbe@'%' identified by 'kbe';
mysql> FLUSH PRIVILEGES;
```



