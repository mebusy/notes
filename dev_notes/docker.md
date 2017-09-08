
# docker 

[official document](https://docs.docker.com/engine/installation/linux/docker-ce/centos/)

[docker 实践](https://yeasy.gitbooks.io/docker_practice/content/basic_concept/)

# 基本概念

理解了 镜像（Image）/ 容器（Container） / 仓库（Repository） 这三个概念 ，就理解了 Docker 的整个生命周期。

## 镜像（Image）

 - 操作系统分为内核和用户空间
 - 对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持
 - Docker 镜像（Image），就相当于是一个 root 文件系统
    - 比如官方镜像 ubuntu:14.04 就包含了完整的一套 Ubuntu 14.04 最小系统的 root 文件系统

### 分层存储

 - 镜像包含操作系统完整的 root 文件系统，其体积往往是庞大的
 - 因此在 Docker 设计时，就充分利用 [Union FS](https://en.wikipedia.org/wiki/Union_mount) 的技术，将其设计为分层存储的架构。
 - 所以严格来说，镜像只是一个虚拟的概念，其实际 由多层文件系统联合组成

---

 - 镜像构建时，会一层层构建，前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。
    - 比如，删除前一层文件的操作，实际不是真的删除前一层的文件，而是仅在当前层标记为该文件已删除。
    - 在最终容器运行的时候，虽然不会看到这个文件，但是实际上该文件会一直跟随镜像。
 - 因此，在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。
 - 分层存储的特征还使得镜像的复用、定制变的更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。


## 容器（Container）

 - 镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体.
 - 容器的实质是进程
    - 但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间
    - 因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。
    - 容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。
 - 镜像使用的是分层存储，容器也是如此
    - 每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，
    - 我们可以称这个为容器运行时读写而准备的存储层为**容器存储层**
 - **容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡**
    - 因此，任何保存于容器存储层的信息都会随容器删除而丢失
 - **容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化** 
    - 所有的文件写入操作，都应该使用 [数据卷（Volume）](https://docs.docker.com/engine/tutorials/dockervolumes/), 或者绑定宿主目录, 在这些位置的读写会跳过容器存储层，直接对宿主(或网络存储)发生读写，其性能和稳定性更高。
 - 数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。
    - 因此，使用数据卷后，容器可以随意删除、重新 run，数据却不会丢失。



## 仓库（Repository）

### Docker Registry

 - 镜像构建完成后，可以很容易的在当前宿主上运行
 - 但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务
 - [Docker Registry](https://docs.docker.com/registry/) 就是这样的服务。

---

 - 一个 Docker Registry 中可以包含多个仓库（Repository）；
 - 每个仓库可以包含多个标签（Tag）
 - 每个标签对应一个镜像。

---

 - 通常，一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的各个版本。
    - 我们可以通过 <仓库名>:<标签> 的格式来指定具体是这个软件哪个版本的镜像。
    - 如果不给出标签，将以 latest 作为默认标签。
 - 以 Ubuntu 镜像 为例，ubuntu 是仓库的名字，其内包含有不同的版本标签，如，14.04, 16.04。
    - 我们可以通过 ubuntu:14.04，或者 ubuntu:16.04 来具体指定所需哪个版本的镜像。
    - 如果忽略了标签，比如 ubuntu，那将视为 ubuntu:latest
 - 仓库名经常以 两段式路径 形式出现，比如 jwilder/nginx-proxy
    - 前者往往意味着 Docker Registry 多用户环境下的用户名，后者则往往是对应的软件名
    - 但这并非绝对，取决于所使用的具体 Docker Registry 的软件或服务。

### Docker Registry 公开服务

 - Docker Registry 公开服务是开放给用户使用、允许用户管理镜像的 Registry 服务。
 - 最常使用的 Registry 公开服务是官方的 [Docker Hub](https://hub.docker.com/) , 这也是默认的 Registry，并拥有大量的高质量的官方镜像。
    - 除此以外，还有 [CoreOS](https://coreos.com/) 的 [Quay.io](https://quay.io/repository/) , CoreOS 相关的镜像存储在这里
    - Google 的 [Google Container Registry](https://cloud.google.com/container-registry/) ，[Kubernetes](http://kubernetes.io/) 的镜像使用的就是这个服务。
 - 由于某些原因，在国内访问这些服务可能会比较慢。国内的一些云服务商提供了针对 Docker Hub 的镜像服务（Registry Mirror），这些镜像服务被称为**加速器**。
    - 常见的有 [阿里云加速器](https://cr.console.aliyun.com/#/accelerator) 、[DaoCloud 加速器](https://www.daocloud.io/mirror#accelerator-doc) 、[灵雀云加速器](http://docs.alauda.cn/feature/accelerator.html) 等

### 私有 Docker Registry

 - 除了使用公开服务外，用户还可以在本地搭建私有 Docker Registry。
 - Docker 官方提供了 [Docker Registry 镜像](https://hub.docker.com/_/registry/)   ，可以直接使用做为私有 Registry 服务。
 - 开源的 Docker Registry 镜像只提供了 [Docker Registry API](https://docs.docker.com/registry/spec/api/) 的服务端实现，足以支持 docker 命令，不影响使用
    - 但不包含图形界面，以及镜像维护、用户管理、访问控制等高级功能。
    - 在官方的商业化版本 [Docker Trusted Registry](https://docs.docker.com/datacenter/dtr/2.0/) 中，提供了这些高级功能。
 
---

# 安装
 
 [安装](https://yeasy.gitbooks.io/docker_practice/content/install/centos.html)

 [镜像加速](https://docs.docker.com/registry/recipes/mirror/#use-case-the-china-registry-mirror)

 [set docker proxy](https://docs.docker.com/engine/admin/systemd/#httphttps-proxy)

---

# 使用 Docker 镜像

Docker 运行容器前需要本地存在对应的镜像，如果镜像不存在本地，Docker 会从镜像仓库下载 ( 默认是 Docker Hub 公共注册服务器中的仓库 )

## 获取镜像

```
docker pull [选项] [Docker Registry地址]<仓库名>:<标签>
```

 - Docker Registry地址：地址的格式一般是 `<域名/IP>[:端口号]`。默认地址是 Docker Hub。
 - 仓库名：如之前所说，这里的仓库名是两段式名称，既 `<用户名>/<软件名>`
    - 对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。

## 运行

以 ubuntu:14.04 为例，如果我们打算启动里面的 bash 并且进行交互式操作的话，可以执行下面的命令。

```
$ docker run -it --rm ubuntu:14.04 bash
```

 - -it 
    - 这是两个参数，一个是 -i：交互式操作，一个是 -t 终端
 - -rm 
    - 容器退出后随之将其删除
 - bash：放在镜像名后的是**命令**
    - 这里我们希望有个交互式 Shell，因此用的是 bash

进入容器后，我们可以在 Shell 下操作，在容器中 执行任何所需的命令

```
root@e7009c6ce357:/# cat /etc/os-release
NAME="Ubuntu"
VERSION="14.04.5 LTS, Trusty Tahr"
ID=ubuntu
VERSION_ID="14.04"
...

root@e7009c6ce357:/# exit
exit
$
```







---

# 常用操作

## stop / rm all container 

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```


## 继续一个刚刚结束的container 

```
docker start -a -i `docker ps -q -l`
```

Explanation: 

 - docker start start a container (requires name or ID)
    -a attach to container
    -i interactive mode
 - docker ps List containers
    -q list only container IDs
    -l list only last created container


