[](...menustart)

- [\[MacOS\] Run Docker Without Docker-Desktop](#bc00c0499363e10c195a32b09f289cf6)

[](...menuend)


<h2 id="bc00c0499363e10c195a32b09f289cf6"></h2>

# [MacOS] Run Docker Without Docker-Desktop

```bash
# 注意： 强烈不推荐 开始k8s --kubernetes，CPU使用率会非常高, k8s 可以使用 kind
colima start [--kubernetes]  --network-address --vm-type=vz --mount-type=virtiofs --cpu 2 --memory 4 --disk 100 --mount-inotify=false  --mount /Volumes/eWORK:w
```

1. `brew install docker-credential-helper docker`
2. edit `~/.docker/config.json`
    ```json
    {
        "auths": {},
        "credsStore": "osxkeychain",
        "currentContext": "colima"
    }
    ```
3. `brew install colima`
4. parameters:
    - `--mount /Volumes/WORK:w` this is very important, you must make some Volumn writable which you want to mount 
    - `--network-address` mechanism for OSX , it asks for an admin pwd to be able to work.
    - `--mount-type=virtiofs`  virtiofs is limited to macOS and vmType `vz`. It is the fastest of the options.
        -  换成 `--mount-type=reverse-sshfs` 可以避免 macOS 的 FSEvents 监控导致cpu使用率过高, 但是会稍微慢一些
        - 也可以配合`--mount-inotify=false` 直接不扫描宿主目录变化 
    - 另外一个可以有效降低cpu使用率的方法是 把需要挂载的目录软连接到 `~/` 目录下
        - `ln -s /Volumes/eWORK ~/eWORK`
        - `colima start --mount ~/eWORK:w`

After the initial run above, you can use `colima start` or use `colima start -e` to edit the configuration file. Run `colima status` at any time to check Colima’s status.

https://ddev.readthedocs.io/en/latest/users/install/docker-installation/#macos

to start Colima automatically on reboot

```bash
brew services start colima
```

By default, Colima only mounts your home directory, so it’s easiest to use it in a subdirectory there. See the `~/.colima/default/colima.yaml`.

# Colima Registry Mirrors

在 Colima 中启用 Kubernetes + Docker runtime 时，docker 运行的是 Colima VM 内部的 Docker daemon，不是你的 macOS 系统 Docker。
要使 registry mirror 生效，必须正确配置 Colima VM 中的 Docker 守护进程。


```yaml
# vi ~/.colima/default/colima.yaml
# replace `docker: {}` with

docker:
  registry-mirrors:
    - https://docker.m.daocloud.io
    - https://dockerproxy.com
    - https://docker.nju.edu.cn
    - https://docker.mirrors.ustc.edu.cn
```

to verify whether mirrors setting works

```bash
colima ssh -- cat /etc/docker/daemon.json; echo
```


## colima cpu 占用高


```bash
> colima ssh
$ top
PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND 
536 root 20 0 17656 8320 7424 R 100.0 0.2 20,31 systemd-logind
```

已知bug, 在 MacOS上尤其明显

解决:

```bash
sudo systemctl disable systemd-logind --now
systemctl status systemd-logind
# 应该显示
inactive (dead)
```


