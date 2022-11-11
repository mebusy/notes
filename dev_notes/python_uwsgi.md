[](...menustart)

- [python uwsgi ,  for CentOS7](#4772e5ef02f48618e5862db7f1c68160)
    - [install](#19ad89bc3e3c9d7ef68b89523eff1987)
    - [run uwsgi](#06ac6355a1466c1b747b9165bfd48c34)
    - [使用脚本](#12bb593fd1f45ba7bbe017d3fe06d51d)

[](...menuend)


<h2 id="4772e5ef02f48618e5862db7f1c68160"></h2>

# python uwsgi ,  for CentOS7 

<h2 id="19ad89bc3e3c9d7ef68b89523eff1987"></h2>

## install 

```
yum install -y python-devel uwsgi uwsgi-plugin-python

pip install uwsgi --user
```


<h2 id="06ac6355a1466c1b747b9165bfd48c34"></h2>

## run uwsgi

```
uwsgi --http-socket :9000 --plugin python --wsgi-file mind.py
```

- note1: 如果要配置 ngnix的 proxy_pass, 需要使用 `--socket`
- note2: for MacOSX, 你可能需要帮助 uwsgi 找到python, 以便找到 第三方库
    - `--home '/System/Library/Frameworks/Python.framework/Versions/2.7'`

<h2 id="12bb593fd1f45ba7bbe017d3fe06d51d"></h2>

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




