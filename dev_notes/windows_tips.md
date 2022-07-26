...menustart

- [Windows tis](#1e4f5759f3716323d239131f31dfac6d)
    - [Use WSL2](#c869ce86f93962ab5ce5ed38b89a408c)
    - [SSH to Win10 WSL2](#e623b8257a43fa5e9f6166407a2e3914)

...menuend


<h2 id="1e4f5759f3716323d239131f31dfac6d"></h2>


# Windows tis


<h2 id="c869ce86f93962ab5ce5ed38b89a408c"></h2>


## Use WSL2 

- install WSL2 on Win10
    ```bash
    wsl.exe --install
    ```
    - reboot, and wait to finish Ubuntu setup
    - update apt
        ```bash
        sudo apt update && apt upgrade -y 
        ```

- install docker
    - https://docs.docker.com/engine/install/ubuntu/
    ```bash
    $ curl -fsSL https://test.docker.com -o test-docker.sh
    $ sudo sh test-docker.sh
    ...
    # IMPORTANT: systemctl not work on WLS !!!
    #   use service instead
    $ sudo service docker start
    ```
    - now make docker rootless... it's painful under WSL2... 
        - so I decide to add a group user...
        ```bash
        $ sudo groupadd docker
        $ sudo usermod -aG docker $USER 
        ```


<h2 id="e623b8257a43fa5e9f6166407a2e3914"></h2>


## SSH to Win10 WSL2

- modify sshd port
    - /etc/ssh/sshd_config
    ```bash
    Port 2222
    #AddressFamily any
    ListenAddress 0.0.0.0
    ...
    PasswordAuthentication yes
    ```
- restart sshd
    - on Ubuntu
    ```bash
    $ sudo systemctl restart ssh
    ```
    - on centos
    ```bash
    $ sudo systemctl restart sshd
    ```
- you wsl2 ip address is something like 172.x.x.x, mine is 172.23.129.80
- FORWARD PORTS INTO WSL2
    - from an win10 **Administrator Windows prompt**, add a portproxy rule
        ```bash
        netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2222 connectaddress=172.23.129.80 connectport=2222
        ```
    - You can list all your portproxy rules like this if you're concerned:
        ```bash
        netsh interface portproxy show v4tov4 
        ```
    - You can remove them all if you want with
        ```bash
        netsh int portproxy reset all
        ```
    - or remove specific one
        ```bash
        > netsh interface portproxy delete v4tov4 listenport=33057 listenaddress=0.0.0.0
        ```
    - BUT... the IP of wsl will change after rebooting...
        - PS: follow script NOT work
        ```bat
        @echo off

        REM netproxy.bat
        REM    Run this script on start up on Windows 10
        REM    create a shortcut, right-click on the shortcut > Properties > Advanced > Run as administrator. 
        REM    press Windows+R, then type shell:startup
        REM    put  netproxy.bat there.

        REM fake unix $() command by BAT FOR /F
        for /f %%i in ('wsl hostname -I') do set WSLIP=%%i
        echo WSLIP is %WSLIP%

        for %%p in ( 2222 8001 80 33056 33057 5050 ) do (
          netsh interface portproxy set v4tov4 listenaddress=0.0.0.0 listenport=%%p connectaddress=%WSLIP% connectport=%%p
        )

        netsh interface portproxy show v4tov4 
        ```
- OPEN THE FIREWALL
    - from the same Administrator Windows prompt, open an incoming Firewall Port. 
    - You can do it from the Advanced Firewall Settings, but even easier you can use netsh again!
    ```bash
    netsh advfirewall firewall add rule name=”Open Port 2222 for WSL2” dir=in action=allow protocol=TCP localport=2222
    ```
- delete firewall rule
    ```bash
    > netsh advfirewall firewall show rule status=enabled name=all | FIND /I "WSL"
    Rule Name:                            Open Port 33056 for WSL2
    Rule Name:                            Open Port 33057 for WSL2
    Rule Name:                            Open Port 8001 for WSL2
    Rule Name:                            Open Port 2222 for WSL2
    > netsh advfirewall firewall delete rule name="Open Port 33056 for WSL2"
    Deleted 1 rule(s).
    ```

