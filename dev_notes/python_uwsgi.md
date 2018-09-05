
# python uwsgi ,  for CentOS7 

## install 

```
yum install -y python-devel uwsgi uwsgi-plugin-python

pip install uwsgi --user
```


## run uwsgi

```
uwsgi --http-socket :9000 --plugin python --wsgi-file mind.py
```

 - note1: 如果要配置 ngnix的 proxy_pass, 需要使用 `--socket`
 - note2: for MacOSX, 你可能需要帮助 uwsgi 找到python, 以便找到 第三方库
    - `--home '/System/Library/Frameworks/Python.framework/Versions/2.7'`

## 使用脚本

```
!vi uwsgi.ini

[uwsgi]
http-socket = :9000
plugin = python
chdir = /root/uwsgi_mind/
wsgi-file = ./mind.py
stats = :9012
```

 - to run:  `uwsgi uwsgi.ini `

 - 自动启动脚本,见Centos7




