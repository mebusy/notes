
# Windows tis

## SSH to Win10 WSL2

- modify sshd port
    - /etc/ssh/sshd_config
    ```bash
    Port 2222
    #AddressFamily any
    ListenAddress 0.0.0.0
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
- OPEN THE FIREWALL
    - from the same Administrator Windows prompt, open an incoming Firewall Port. 
    - You can do it from the Advanced Firewall Settings, but even easier you can use netsh again!
    ```bash
    netsh advfirewall firewall add rule name=”Open Port 2222 for WSL2” dir=in action=allow protocol=TCP localport=2222
    ```


