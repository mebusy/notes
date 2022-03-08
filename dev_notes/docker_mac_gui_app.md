
# Docker for Mac and GUI applications

https://fredrikaverpil.github.io/2016/07/31/docker-for-mac-and-gui-applications/


## 1. install xquartz

```bash
brew install xquartz
```

reboot Mac

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
5. test an GUI app, e.g. firefox
    ```bash
    docker run --rm  --name firefox -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix jess/firefox 
    ```


