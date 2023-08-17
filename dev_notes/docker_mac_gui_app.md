[](...menustart)

- [Docker for Mac and GUI applications](#da8f018826cd634d83e9bedeef10f24e)
    - [1. install xquartz](#86f31b01b31e677cd37cf505c57369a3)
    - [2. setup xquartz](#b87bd81eea00083fb21d246bc3f3baef)
    - [better way](#c595faaa40f40ab409bc3f23debda184)
- [Other example](#48a8990e0175dd1649fdd9ffc44942aa)
    - [matplotlib X11 test program](#7f491c02453ff410c8d86998578039c0)

[](...menuend)


<h2 id="da8f018826cd634d83e9bedeef10f24e"></h2>

# Docker for Mac and GUI applications

https://fredrikaverpil.github.io/2016/07/31/docker-for-mac-and-gui-applications/


<h2 id="86f31b01b31e677cd37cf505c57369a3"></h2>

## 1. install xquartz

```bash
brew install xquartz
```

reboot Mac

<h2 id="b87bd81eea00083fb21d246bc3f3baef"></h2>

##  2. setup xquartz

1. run XQuartz
    ```bash
    open -a XQuartz
    ```
    - a xterm window should popup
2. In the XQuartz preferences, go to the “Security” tab and make sure you’ve got “Allow connections from network clients”
    - ![](https://fredrikaverpil.github.io/blog/assets/docker/xquartz_preferences.png)
3. run xhost and allow connections from your local machine
    ```bash
    ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
    xhost + $ip 
    ```
4. find your displaynumber
    ```bash
    display_number=`ps -ef | grep "Xquartz :\d" | grep -v xinit | awk '{ print $9; }'`
    echo $display_number
    ```
5. or you may want to integrate it in your .profile
    ```bash
    # x11
    _ip=`ifconfig en0 | grep inet | awk '$1=="inet" {print $2}'`
    xhost + $_ip > /dev/null 
    export DISPLAY=$_ip:0
    ```
6. test an GUI app, e.g. firefox
    ```bash
    # -v /tmp/.X11-unix:/tmp/.X11-unix 
    docker run --rm  --name firefox -e DISPLAY=$DISPLAY jess/firefox 
    ```


<h2 id="c595faaa40f40ab409bc3f23debda184"></h2>

## better way

```bash
xhost + localhost
```

- use `host.docker.internal` to access localhost on host from docker container.

```bash
docker run --rm  --name firefox -e DISPLAY=host.docker.internal jess/firefox 
```


---

<h2 id="48a8990e0175dd1649fdd9ffc44942aa"></h2>

# Other example

<h2 id="7f491c02453ff410c8d86998578039c0"></h2>

## matplotlib X11 test program 

```python
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()
```
