# VMWare UbuntuServer

1. Auto-Mount VMWare Shared Folder 
    ```bash
    mkdir -p /mnt/hgfs
    sudo vi /etc/fstab
    # add
    .host:/    /mnt/hgfs    fuse.vmhgfs-fuse    defaults,allow_other    0 0
    ```
2. remove snap if you want
    ```bash
    snap list
    # Then, remove listed package one by one:
    sudo snap remove --purge <package-name>
    # Disable and Stop Snap Services
    sudo systemctl disable snapd.service
    sudo systemctl disable snapd.socket
    sudo systemctl disable snapd.seeded.service

    sudo systemctl stop snapd.service
    sudo systemctl stop snapd.socket
    sudo systemctl stop snapd.seeded.service
    # Remove Snapd Completely
    sudo apt remove --purge snapd -y
    sudo apt autoremove -y
    rm -rf ~/snap
    # Prevent Snap from Being Reinstalled
    echo "Package: snapd
    Pin: release a=*
    Pin-Priority: -10" | sudo tee /etc/apt/preferences.d/no-snapd
    ```
3. install docker
    ```bash
    curl -fsSL https://get.docker.com | sudo bash
    ```
    - `/etc/docker/daemon.json` setup registry mirrors
4. install minikube
    ```bash
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    ```
    ```bash
    # if you need
    minikube addons enable ingress
    minikube addons enable dashboard
    minikube dashboard
    ```
    - minikube start options
        ```bash
        minikube start --cpus=4 --memory=8192 --driver=docker
        ```
    - kubectl
        ```bash
        alias kubectl="minikube kubectl --"
      ```
5. make minikube run as service, and share data with host
    - Create a systemd service file:
        ```bash
        sudo vi /etc/systemd/system/minikube.service
        ```
        ```bash
        [Unit]
        Description=Minikube with Auto Mount
        After=network.target

        [Service]
        Type=simple
        ExecStart=/bin/bash -c 'minikube start --driver=docker --registry-mirror=https://docker.m.daocloud.io --registry-mirror=https://dockerproxy.com --registry-mirror=https://docker.nju.edu.cn --registry-mirror=https://docker.mirrors.ustc.edu.cn  && minikube mount /home/ubserver/data:/mnt/data'
        Restart=always
        User=ubserver
        Group=ubserver
        Environment=HOME=/home/ubserver

        [Install]
        WantedBy=multi-user.target
        ```
        - replace `ubserver` with you username
    - Enable and start the service:
        ```bash
        sudo systemctl daemon-reload
        sudo systemctl enable minikube.service
        sudo systemctl start minikube.service
        ```
    - check minikube docker registry-mirror
        ```bash
        cat ~/.minikube/machines/minikube/config.json 
        ```

