[](...menustart)

- [\[MacOS\] Run Docker Without Docker-Desktop](#bc00c0499363e10c195a32b09f289cf6)

[](...menuend)


<h2 id="bc00c0499363e10c195a32b09f289cf6"></h2>

# [MacOS] Run Docker Without Docker-Desktop

```bash
colima start --network-address --vm-type=vz --mount-type=virtiofs --cpu 2 --memory 4 --disk 64 --mount /Volumes/WORK:w --mount /Volumes/eWORK:w -k
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

