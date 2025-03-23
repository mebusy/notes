# VMWare UbuntuServer


1. Auto-Mount VMWare Shared Folder 
    ```bash
    sudo mkdir -p /mnt/hgfs
    sudo vi /etc/fstab
    # add
    .host:/    /mnt/hgfs    fuse.vmhgfs-fuse    defaults,allow_other,uid=999,gid=999    0 0
    ```
    - `uid=999,gid=999`
        - VMware 共享文件夹的 vmhgfs-fuse 驱动不支持更改所有权，即使使用 sudo 也无效。因此，chown 命令会失败。
        - 在 /etc/fstab 里添加 uid 和 gid 选项，使共享文件夹归指定用户所有
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
6. export k8s config for usage from host
    ```bash
    microk8s config > /mnt/hgfs/<your-shared-folder>/microk8s.config
    ```


# FAQ

- how to keep `kubectl portforward` to ubuntu client k8s service keep alive
    ```bash
    vi /etc/sysctl.conf
    # add
    net.ipv4.tcp_keepalive_time=60
    net.ipv4.tcp_keepalive_intvl=10
    net.ipv4.tcp_keepalive_probes=5
    ```
