# VMWare UbuntuServer


1. Auto-Mount VMWare Shared Folder 
    ```bash
    mkdir -p /mnt/hgfs
    sudo vi /etc/fstab
    # add
    .host:/    /mnt/hgfs    fuse.vmhgfs-fuse    defaults,allow_other    0 0
    ```
3. install docker
    ```bash
    curl -fsSL https://get.docker.com | sudo bash
    # or  sudo apt install docker.io -y
    ```
    - `/etc/docker/daemon.json` setup registry mirrors
    ```bash
    sudo groupadd docker
    sudo usermod -aG docker $USER
    # logout
    ```
4. install microk8s
    - https://github.com/canonical/microk8s
        ```bash
        sudo usermod -a -G microk8s $USER
        ```
    - kubectl
        ```bash
        alias kubectl="microk8s kubectl "
      ```
5. microk8s config registry-mirrors
    - https://microk8s.io/docs/registry-private
        - /var/snap/microk8s/current/args/certs.d/registry.k8s.io/host.toml
        - /var/snap/microk8s/current/args/certs.d/docker.io/host.toml
    - check
        ```bash
        microk8s ctr image pull  docker.io/library/mongo:6.0.6
        ```




