

# docker  MacOSX

## install 

```
brew install docker docker-machine
```


## start 

我們要透過 docker-machine 建立並啟動一個 VM 作為 docker 的環境，這邊我使用的 driver 為 VirtualBox，名字設定為 default：

```
docker-machine create --driver virtualbox default
```

接下來為重點，我們執行 docker-machine env default，可以查看 default 所設定的參數，而這些參數用於指定 docker 的 client 所要連線的參數：

```
$ docker-machine env default
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/qibinyi/.docker/machine/machines/default"
export DOCKER_MACHINE_NAME="default"
# Run this command to configure your shell:
# eval $(docker-machine env default)
```

照着上面说的，执行最后一句。 也可以把这句话 放入 ~/.profile 


## check your docker daemon

```
$ NO_PROXY=`docker-machine ip default` docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

Not working ?

 - try restart 
    - docker-machine restart default
 - or recreate docker env
    - docker-machine rm default


# docker Centos 

## 启动

```
$ systemctl enable docker
$ systemctl start docker
```


