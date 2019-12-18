
# Netatalk for MacOSX time Machine , based on Centos7

## 1. download source code

```bash
https://sourceforge.net/projects/netatalk/
https://github.com/Netatalk/Netatalk
```

## 2. Compiling

```bash
yum install libgcrypt-devel
yum install libdb-devel
```

```bash
tar -xvf netatalk-3-1-12.tar.gz
cd Netatalk-netatalk-3-1-12/
autoreconf -i
./configure --with-init-style=redhat-systemd --with-shadow

make
make install 
```


## 3. Config file

```bash
adduser nas

# vi /usr/local/etc/afp.conf
[Global]
; Global server settings
 mimic model = TimeCapsul
 log level = default:warn
 log file = /var/log/afpd.log
 hosts allow = 192.168.1.0/24 #允许访问的主机地址
 uam list = uams_clrtxt.so uams_guest.so #必须，认证方式，目前只调通了guest模式
 guest account = nas #必须，guest对应的linux系统用户

[TimeMachine]
  path = /home/nas
  time machine = yes #必须，yes才支持mac timemachine
  rwlist = nas #必须，设置nas 读写权限
  force user = nas  #必须，用户映射
  # vol size limit = 100000  #限制贡献volume大小为100GB，单位为MB。
```

## 4. Start netatalk

```bash
systemctl start netatalk
systemctl enable netatalk
```

To check whether server is ready.

```bash
# lsof -i:548
COMMAND   PID USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
afpd    29393 root    4u  IPv6 13706292      0t0  TCP *:afpovertcp (LISTEN)
```

## 5. Mount afp server in MacOSX 

```
finder -> Go -> connect to Server 

add ...

afp://ip
```

----

## 5. let MacOSX auto detect afp servies

```bash
yum install avahi
```

```bash
# vi /etc/avahi/services/afpd.service 

<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
<name replace-wildcards="yes">%h</name>
<service>
<type>_afpovertcp._tcp</type>
<port>548</port>
</service>
<service>
<type>_device-info._tcp</type>
<port>0</port>
<txt-record>model=TimeCapsule</txt-record>
</service>
</service-group>
```


```bash
systemctl start avahi-daemon
systemctl enable avahi-daemon
```


