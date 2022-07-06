...menustart

- [Windows tis](#1e4f5759f3716323d239131f31dfac6d)
    - [SSH to Win10 WSL2](#e623b8257a43fa5e9f6166407a2e3914)

...menuend


<h2 id="1e4f5759f3716323d239131f31dfac6d"></h2>


# Windows tis


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
- install k8s
    - install kubectl...
    - https://github.com/kubernetes-sigs/kind/releases
    ```bash
    $ curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.14.0/kind-$(uname)-amd64
    $ chmod +x ./kind
    $ sudo mv ./kind /usr/local/bin/
    # create k8s cluster
    $ kind create cluster --name wslk8s
    Set kubectl context to "kind-wslk8s"
    You can now use your cluster with:
    kubectl cluster-info --context kind-wslk8s
    ```
    - test whether it works...
        ```bash
        $ kubectl cluster-info
        Kubernetes control plane is running at https://127.0.0.1:35537
        CoreDNS is running at https://127.0.0.1:35537/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

        To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
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
- OPEN THE FIREWALL
    - from the same Administrator Windows prompt, open an incoming Firewall Port. 
    - You can do it from the Advanced Firewall Settings, but even easier you can use netsh again!
    ```bash
    netsh advfirewall firewall add rule name=”Open Port 2222 for WSL2” dir=in action=allow protocol=TCP localport=2222
    ```


