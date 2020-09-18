...menustart

- [docker](#05b6053c41a2130afd6fc3b158bda4e6)
- [基本概念](#e2d6d0e301f7dcc1afe228f7cbcf285a)
    - [镜像（Image）](#19f6588aaa5d5f651bf694f2b7a7a6a3)
        - [分层存储](#f96eee41708b8eed50d6e54fcee9ff58)
    - [容器（Container）](#ce9d5c685661911c7fe0bcb1c08c3705)
    - [仓库（Repository）](#e9ce47c1438cc8cd01d7147f7d93a169)
        - [Docker Registry](#a6713cd9dc3c442c7735a2b08a2a768d)
        - [Docker Registry 公开服务](#c77b89c512b53b948badba879bcb7411)
        - [私有 Docker Registry](#3b51596a30d07a4cccce378ebc71a546)
- [安装](#e655a410ff21cd07e7a0150491e04371)
- [使用 Docker 镜像](#4da5582c2bd22e8a31b18a4362a2e4db)
    - [获取镜像](#dde7c093537b2671dc3e20601fe1ad50)
    - [运行](#4c763bb67e6013dd35dd97d1efd9c8f2)
    - [列出镜像](#edfeb4bbaa399a7dd5981ee43139839e)
        - [虚悬镜像](#27a7f5880024c773ace50993e2478d92)
        - [中间层镜像](#472571f817083bd6c1adc28636865cbc)
        - [列出部分镜像](#44e1a2382c5d3428c9e6991adff4b6cd)
        - [以特定格式显示](#572b05bc4b772aa9955181aa862e489e)
    - [利用 commit 理解镜像构成](#4b409ece8383ea0f14f598b08fa3f7fc)
        - [慎用 docker commit](#a93f325da3a605ac9c7976c259cc3c99)
    - [使用 Dockerfile 定制镜像](#ca15f31abd0e0c5beb65f69cd39f697e)
        - [FROM 指定基础镜像](#ad64b82a688e4563306595a8bcbd75df)
        - [RUN 执行命令](#c40a005104159611a8abcc3e7f4e8e8f)
        - [构建镜像](#0cd7fc52e88767f46089b6fc4bc14cdc)
        - [镜像构建上下文（Context）](#697df4e515f25078aa8b3ba4573d6964)
        - [其它 docker build 的用法](#e2ccb8bb6d2b9d1f6ef53430262eb335)
            - [直接用 Git repo 进行构建](#e3b76237c22c121138eb68b7e15928ed)
            - [用给定的 tar 压缩包构建](#ffc9590011c00baebbf79d7d2db28ba3)
            - [从标准输入中读取 Dockerfile 进行构建](#20183161339129a8f9da73bc60cc95ba)
            - [从标准输入中读取上下文压缩包进行构建](#c3257bd208d0a3934d193cf26aa2df71)
    - [Dockerfile 指令详解](#ab7b66399bb75089097e87d4fe04cf86)
        - [COPY 复制文件](#36960c37c1514474b4d1eb8f2e9af565)
        - [ADD 更高级的复制文件](#bc734ce94f563958ed54ed85e7c24626)
        - [CMD 容器启动命令](#d3bc2b31db3b0c82ec91ac3e2f9dd85b)
        - [ENTRYPOINT 入口点](#1cd6041bdc91a8e6a4c862d3636ce5ed)
        - [ENV 设置环境变量](#15a80d9facd5298221ecbed6e7ee75c7)
        - [ARG 构建参数](#14e2e3b76460818c68b72dfaa4534d96)
        - [VOLUME 定义匿名卷](#49b45cf4204f235e160ea09e07a16829)
        - [EXPOSE 声明端口](#a7a926de3ef2a0c352f59030d0bbc6dd)
        - [WORKDIR 指定工作目录](#5a844af8a8f0576eb7a818856d201a20)
        - [USER 指定当前用户](#40211142c56583b06d2fe618fa0b3405)
        - [HEALTHCHECK 健康检查](#28feabf1a02ad73fb34a3d5aa47c26e9)
        - [ONBUILD 为他人做嫁衣裳](#8487eec94911eb65c7d2f4bc18cbbe2b)
- [操作容器](#84c8ea5f92b2186182f00a2443cbab12)
    - [启动容器](#b093c1c365b165c1d14e32dba65e94f6)
        - [新建并启动](#54aae6275e57c681fe430764be974c77)
        - [启动已终止容器](#63e39864e294349dc722ce9ba8b51ee7)
    - [后台(background)运行](#28b855ee0bcfa0640199f634fb5c23a0)
        - [终止容器](#cd1786012578ed41f6a2435c1dcc5966)
    - [进入容器](#51fddac8e0d43b8c4cedf5c7536a2b12)
        - [attach 命令](#ed8bd9329f54fdae47e248ee852d1a1d)
    - [导出和导入容器](#bfc5650eb46f0bddb423c490b0c28be3)
        - [导入容器快照](#21eccb9f6a6709dc17c387515e123d28)
    - [删除](#2f4aaddde33c9b93c36fd2503f3d122b)
        - [清理所有处于终止状态的容器](#cd287c2794249580cfc4de4006ac9362)
- [访问仓库   Repository](#5e6078663fa925398d77b106c67215db)
    - [Docker Hub](#ec104a6054aee6dccf8a9fc8f6842317)
    - [私有仓库](#96387a3a5055939b42bfc6181ba784df)
        - [Deploy a registry server](#8c80d32c81877be8ad508c7e075bbc13)
            - [Run a local registry](#5f65c52efba3f11c0512e5433920dc5e)
            - [Copy an image from Docker Hub to your registry](#17443590fa63f19e5857da6f6407d646)
    - [配置文件 TODO](#919d9a1b6552e2443bcba07ac2fcf531)
- [Docker 数据管理](#092d280d669c713c8778047dbe6b2259)
    - [数据卷](#99b935d7193a1934689a928ae0139d33)
        - [创建一个数据卷](#f1a6ea6cc69a550bafe35f56eb079327)
        - [删除数据卷](#9e416de2b887c7c78160255665c297bd)
        - [挂载一个主机目录作为数据卷](#e5be13163123d804d337301b9c09eeb4)
        - [查看数据卷的具体信息](#f7d1e7013f50a458471e5d4c805fbb4f)
        - [挂载一个本地主机文件作为数据卷](#bb673754af06a1493de8c9a1255c3947)
    - [数据卷容器](#2df5c8a6ca62324d4237ab45a6fc7391)
    - [利用数据卷容器来备份、恢复、迁移数据卷](#35de814218f4269e2c883f78d4f1e504)
        - [备份](#664b37da2222287adcb1ecc4e48edb73)
        - [恢复](#c7db6d4f1a42987a0df962e927926f14)
- [使用网络](#55e0f8921afc8ae4c8c0536410b973af)
    - [外部访问容器](#fe6bb93e4d01fd9317947eef46670807)
        - [映射所有接口地址](#cc4add018dea50c5c26e286522ecaa9f)
        - [映射到指定地址的指定端口](#7a9d7a6fd9999d4c50012bf194a0d5f8)
        - [映射到指定地址的任意端口](#5bfc1ca85e80abb7f382b15b0d1e05ae)
        - [查看映射端口配置](#2689da8e24fd82172b01f89e377c0081)
    - [容器互联](#06dc7504152a3981b873a938686fbb62)
        - [自定义容器命名](#2a4bb5c86ebcad25a1debf231dc8e752)
        - [容器互联](#06dc7504152a3981b873a938686fbb62)
- [高级网络配置](#89a0c0e3c241795282a7a015dcf8f159)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [stop / rm all container](#106810e843fbd66af6ee48cb3ee7e07f)
    - [继续一个刚刚结束的container](#5e7908d41ed1f3e6e1906d575e2dfea0)
    - [pass proxy to docker container](#e64a823c0142aaac197cc68839f54da9)
    - [docker daemon proxy for Centos7](#ed931520f4337c85396faa61455d56ec)
    - [proxy when docker build](#68175df37efb964151e614c93d3e62ae)
    - [run bash of existing containter](#5ef5bd47a5282fb1ad1694bbb5f46954)
    - [get DockerFile from Image](#47a7dbe444a0af8498cf01950ad552ef)
    - [add a restart policy to a container](#9b68cd8277b36a785a1a8784426e3095)
    - [docker redis](#e03d31b41fc936f76920bb647520ef01)
    - [docker mysql](#5b1064e3e54b4f22a3419f9d198df904)
    - [docker cleanup](#ada28088d8540a0471c00fb0673b9882)
    - [docker pandoc](#b64e99ff98a5173b25e6d0d91bc330f3)

...menuend


<h2 id="05b6053c41a2130afd6fc3b158bda4e6"></h2>


# docker 

[official document](https://docs.docker.com/engine/installation/linux/docker-ce/centos/)

[docker 实践](https://yeasy.gitbooks.io/docker_practice/content/basic_concept/)

[docker samples , i.e. nginx, mysql](https://docs.docker.com/samples/library/mysql/)


<h2 id="e2d6d0e301f7dcc1afe228f7cbcf285a"></h2>


# 基本概念

理解了 镜像（Image）/ 容器（Container） / 仓库（Repository） 这三个概念 ，就理解了 Docker 的整个生命周期。

<h2 id="19f6588aaa5d5f651bf694f2b7a7a6a3"></h2>


## 镜像（Image）

- 操作系统分为内核和用户空间
- 对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持
- Docker 镜像（Image），就相当于是一个 root 文件系统
    - 比如官方镜像 ubuntu:14.04 就包含了完整的一套 Ubuntu 14.04 最小系统的 root 文件系统

<h2 id="f96eee41708b8eed50d6e54fcee9ff58"></h2>


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


<h2 id="ce9d5c685661911c7fe0bcb1c08c3705"></h2>


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



<h2 id="e9ce47c1438cc8cd01d7147f7d93a169"></h2>


## 仓库（Repository）

<h2 id="a6713cd9dc3c442c7735a2b08a2a768d"></h2>


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

<h2 id="c77b89c512b53b948badba879bcb7411"></h2>


### Docker Registry 公开服务

- Docker Registry 公开服务是开放给用户使用、允许用户管理镜像的 Registry 服务。
- 最常使用的 Registry 公开服务是官方的 [Docker Hub](https://hub.docker.com/) , 这也是默认的 Registry，并拥有大量的高质量的官方镜像。
    - 除此以外，还有 [CoreOS](https://coreos.com/) 的 [Quay.io](https://quay.io/repository/) , CoreOS 相关的镜像存储在这里
    - Google 的 [Google Container Registry](https://cloud.google.com/container-registry/) ，[Kubernetes](http://kubernetes.io/) 的镜像使用的就是这个服务。
- 由于某些原因，在国内访问这些服务可能会比较慢。国内的一些云服务商提供了针对 Docker Hub 的镜像服务（Registry Mirror），这些镜像服务被称为**加速器**。
    - 常见的有 [阿里云加速器](https://cr.console.aliyun.com/#/accelerator) 、[DaoCloud 加速器](https://www.daocloud.io/mirror#accelerator-doc) 、[灵雀云加速器](http://docs.alauda.cn/feature/accelerator.html) 等

<h2 id="3b51596a30d07a4cccce378ebc71a546"></h2>


### 私有 Docker Registry

- 除了使用公开服务外，用户还可以在本地搭建私有 Docker Registry。
- Docker 官方提供了 [Docker Registry 镜像](https://hub.docker.com/_/registry/)   ，可以直接使用做为私有 Registry 服务。
- 开源的 Docker Registry 镜像只提供了 [Docker Registry API](https://docs.docker.com/registry/spec/api/) 的服务端实现，足以支持 docker 命令，不影响使用
    - 但不包含图形界面，以及镜像维护、用户管理、访问控制等高级功能。
    - 在官方的商业化版本 [Docker Trusted Registry](https://docs.docker.com/datacenter/dtr/2.0/) 中，提供了这些高级功能。
 
---

<h2 id="e655a410ff21cd07e7a0150491e04371"></h2>


# 安装
 
 [安装](https://yeasy.gitbooks.io/docker_practice/content/install/centos.html)

For Centos:

- 1. 安装依赖包

```
yum remove docker \
                  docker-ce \
                  docker-cli \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine



yum install -y yum-utils \
           device-mapper-persistent-data \
           lvm2
```

- 2. set up the stable repository

```
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```


- 3. INSTALL DOCKER CE

```
yum install -y docker-ce
```

- 4. start up

```
$ systemctl enable docker
$ systemctl start docker
```


- FAQ 
    - Requires Pigz
    - Requires: container-selinux >= 2.9
    
```
# try
yum install --setopt=obsoletes=0 \
   docker-ce-17.03.2.ce-1.el7.centos.x86_64 \
   docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch

```

- FAQ 
    - 最新的版本 docker 不能使用 NTLM代理
    - 更换较旧的版本，比如 18.03.1 

```
// list docker-ce old versions
yum list docker-ce.x86_64  --showduplicates | sort -r
```



 [镜像加速](https://docs.docker.com/registry/recipes/mirror/#use-case-the-china-registry-mirror)

 [set docker daemon proxy](https://docs.docker.com/engine/admin/systemd/#httphttps-proxy)

---

<h2 id="4da5582c2bd22e8a31b18a4362a2e4db"></h2>


# 使用 Docker 镜像

Docker 运行容器前需要本地存在对应的镜像，如果镜像不存在本地，Docker 会从镜像仓库下载 ( 默认是 Docker Hub 公共注册服务器中的仓库 )

<h2 id="dde7c093537b2671dc3e20601fe1ad50"></h2>


## 获取镜像

```
docker pull [选项] [Docker Registry地址]<仓库名>:<标签>
```

- Docker Registry地址：地址的格式一般是 `<域名/IP>[:端口号]`。默认地址是 Docker Hub。
- 仓库名：如之前所说，这里的仓库名是两段式名称，既 `<用户名>/<软件名>`
    - 对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。

<h2 id="4c763bb67e6013dd35dd97d1efd9c8f2"></h2>


## 运行

以 ubuntu:14.04 为例，如果我们打算启动里面的 bash 并且进行交互式操作的话，可以执行下面的命令。

```
$ docker run -it --rm ubuntu:14.04 bash
```

- -it 
    - 这是两个参数，一个是 -i：交互式操作，一个是 -t 终端
- `—-rm`
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

<h2 id="edfeb4bbaa399a7dd5981ee43139839e"></h2>


## 列出镜像

```
$ docker images
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
redis                latest              5f515359c7f8        5 days ago          183 MB
<none>               <none>              00285df0df87        5 days ago          342 MB
ubuntu               16.04               f753707788c5        4 weeks ago         127 MB
ubuntu               latest              f753707788c5        4 weeks ago         127 MB
ubuntu               14.04               1e0c3dd64ccd        4 weeks ago         188 MB
```

- `IMAGE ID` 是镜像的唯一标识
- 一个镜像可以对应多个标签 TAG
    - ubuntu:16.04 和 ubuntu:latest 拥有相同的 ID，因为它们对应的是同一个镜像

<h2 id="27a7f5880024c773ace50993e2478d92"></h2>


### 虚悬镜像

- 上面的镜像列表中，还可以看到一个特殊的镜像，这个镜像既没有仓库名，也没有标签，均为 `<none>`
- 这个镜像原本是有镜像名和标签的，原来为 mongo:3.2，随着官方镜像维护，发布了新版本后，重新 docker pull mongo:3.2 时，mongo:3.2 这个镜像名被转移到了新下载的镜像身上，而旧的镜像上的这个名称则被取消，从而成为了 `<none>`。
    - 除了 docker pull 可能导致这种情况，docker build 也同样可以导致这种现象
- 由于新旧镜像同名，旧镜像名称被取消，从而出现仓库名、标签均为 `<none>` 的镜像。这类无标签镜像也被称为 **虚悬镜像(dangling image)**  
- 可以用下面的命令专门显示这类镜像：
    - `$ docker images -f dangling=true`
- 一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的，可以用下面的命令删除。
    - `$ docker rmi $(docker images -q -f dangling=true)`

<h2 id="472571f817083bd6c1adc28636865cbc"></h2>


### 中间层镜像

- 为了加速镜像构建、重复利用资源，Docker 会利用 **中间层镜像**
- 所以在使用一段时间后，可能会看到一些依赖的中间层镜像
- 默认的 docker images 列表中只会显示顶层镜像，如果希望显示包括中间层镜像在内的所有镜像的话，需要加 -a 参数。
    - `$ docker images -a`
- 这样会看到很多无标签的镜像，与之前的虚悬镜像不同，这些无标签的镜像很多都是中间层镜像，是其它镜像所依赖的镜像。这些无标签镜像不应该删除，否则会导致上层镜像因为依赖丢失而出错. 实际上，这些镜像也没必要删除.

<h2 id="44e1a2382c5d3428c9e6991adff4b6cd"></h2>


### 列出部分镜像

根据仓库名列出镜像

```
$ docker images ubuntu
```

列出特定的某个镜像，也就是说指定仓库名和标签

```
$ docker images ubuntu:16.04
```

除此以外，docker images 还支持强大的过滤器参数 --filter，或者简写 -f

比如，我们希望看到在 mongo:3.2 之后建立的镜像，可以用下面的命令：

```
$ docker images -f since=mongo:3.2
```

此外，如果镜像构建时，定义了 LABEL，还可以通过 LABEL 来过滤。

```
$ docker images -f label=com.example.version=0.1
```

<h2 id="572b05bc4b772aa9955181aa862e489e"></h2>


### 以特定格式显示

- 默认情况下，docker images 会输出一个完整的表格，但是我们并非所有时候都会需要这些内容

```
$ docker images -q
5f515359c7f8
05a60462f8ba
fe9198c04d62
00285df0df87
```

- `-q` 的 结果，可以直接 配合 `docker rmi ` 之类的命令进行批量处理

下面的命令会直接列出镜像结果，并且只包含镜像ID和仓库名：

```
$ docker images --format "{{.ID}}: {{.Repository}}"
5f515359c7f8: redis
05a60462f8ba: nginx
fe9198c04d62: mongo
00285df0df87: <none>
```

<h2 id="4b409ece8383ea0f14f598b08fa3f7fc"></h2>


## 利用 commit 理解镜像构成

- 在之前的例子中，我们所使用的都是来自于 Docker Hub 的镜像
- 直接使用这些镜像是可以满足一定的需求，而当这些镜像无法直接满足需求时，我们就需要定制这些镜像。

现在让我们以定制一个 Web 服务器为例子，来讲解镜像是如何构建的。

```
docker run --name webserver -d -p 80:80 nginx
```

这条命令会用 nginx 镜像启动一个容器，命名为 webserver，并且映射了 80 端口，这样我们可以用浏览器去访问这个 nginx 服务器。

如果是在 Linux 本机运行的 Docker，或者如果使用的是 Docker for Mac、Docker for Windows，那么可以直接访问：http://localhost；如果使用的是 Docker Toolbox，或者是在虚拟机、云服务器上安装的 Docker，则需要将 localhost 换为虚拟机地址或者实际云服务器地址。

直接用浏览器访问的话，我们会看到默认的 Nginx 欢迎页面。

现在，假设我们非常不喜欢这个欢迎页面，我们希望改成欢迎 Docker 的文字，我们可以使用 docker exec 命令进入容器，修改其内容。

```
$ docker exec -it webserver bash
root@3729b97e8226:/# echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
root@3729b97e8226:/# exit
exit
```

现在我们再刷新浏览器的话，会发现内容被改变了。

我们修改了容器的文件，也就是改动了容器的存储层。我们可以通过 docker diff 命令看到具体的改动。

```
$ docker diff webserver
C /root
A /root/.bash_history
C /run
A /run/nginx.pid
C /usr/share/nginx/html/index.html
C /var/cache/nginx
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp
```

现在我们定制好了变化，我们希望能将其保存下来形成镜像。

- 当我们运行一个容器的时候（如果不使用卷的话），我们做的任何文件修改都会被记录于容器存储层里。
- 而 Docker 提供了一个 docker commit 命令，可以将容器的存储层保存下来成为镜像
    - 换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。
    - 以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。

docker commit 的语法格式为：

```
docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]
```

我们可以用下面的命令将容器保存为镜像：

```
$ docker commit \
    --author "Tao Wang <twang2218@gmail.com>" \
    --message "修改了默认网页" \
    webserver \
    nginx:v2
sha256:07e33465974800ce65751acc279adc6ed2dc5ed4e0838f8b86f0c87aa1795214
```

可以用 docker history 具体查看镜像内的历史记录，如果比较 nginx:latest 的历史记录，我们会发现新增了我们刚刚提交的这一层。

```
$ docker history nginx:v2
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
07e334659748        54 seconds ago      nginx -g daemon off;                            95 B                修改了默认网页
e43d811ce2f4        4 weeks ago         /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon    0 B
<missing>           4 weeks ago         /bin/sh -c #(nop)  EXPOSE 443/tcp 80/tcp
..l
```

新的镜像定制好后，我们可以来运行这个镜像。

```
docker run --name web2 -d -p 81:80 nginx:v2
```

这里我们命名为新的服务为 web2，并且映射到 81 端口。如果是 Docker for Mac/Windows 或 Linux 桌面的话，我们就可以直接访问 http://localhost:81 看到结果，

<h2 id="a93f325da3a605ac9c7976c259cc3c99"></h2>


### 慎用 docker commit

使用 docker commit 命令虽然可以比较直观的帮助理解镜像分层存储的概念，但是实际环境中并不会这样使用。

- 首先，如果仔细观察之前的 docker diff webserver 的结果，你会发现除了真正想要修改的 /usr/share/nginx/html/index.html 文件外，由于命令的执行，还有很多文件被改动或添加了。
    - 这还仅仅是最简单的操作，如果是安装软件包、编译构建，那会有大量的无关内容被添加进来，如果不小心清理，将会导致镜像极为臃肿。
- 此外，使用 docker commit 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为**黑箱镜像**. 
    - 换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。
    - 这种黑箱镜像的维护工作是非常痛苦的
- 如果使用 docker commit 制作镜像，以及后期修改的话，每一次修改都会让镜像更加臃肿一次，所删除的上一层的东西并不会丢失，会一直如影随形的跟着这个镜像，即使根本无法访问到™。这会让镜像更加臃肿。

docker commit 命令除了学习之外，还有一些特殊的应用场合，比如被入侵后保存现场等。但是，不要使用 docker commit 定制镜像，定制行为应该使用 Dockerfile 来完成。

---

<h2 id="ca15f31abd0e0c5beb65f69cd39f697e"></h2>


## 使用 Dockerfile 定制镜像

镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。

还以之前定制 nginx 镜像为例，这次我们使用 Dockerfile 来定制。

在一个空白目录中，建立一个文本文件，并命名为 Dockerfile：

```
$ mkdir mynginx
$ cd mynginx
$ vi Dockerfile
```

其内容为：

```
FROM nginx
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
```

这个 Dockerfile 很简单，一共就两行。涉及到了两条指令，FROM 和 RUN。

<h2 id="ad64b82a688e4563306595a8bcbd75df"></h2>


### FROM 指定基础镜像

- FROM 是必备的指令，并且必须是第一条指令。
- 在 [Docker Hub](https://hub.docker.com/explore/) 上有非常多的高质量的官方镜像， 有可以直接拿来使用的服务类的镜像
    - 如 [nginx](https://hub.docker.com/_/nginx/) 、[redis](https://hub.docker.com/_/redis/) 、[mongo](https://hub.docker.com/_/mongo/) 、[mysql](https://hub.docker.com/_/mysql/)  、[httpd](https://hub.docker.com/_/httpd/) 、[php](https://hub.docker.com/_/php/) 、[tomcat](https://hub.docker.com/_/tomcat/) 等
    - 也有一些方便开发、构建、运行各种语言应用的镜像
    - 如 [node](https://hub.docker.com/_/node/) 、[openjdk](https://hub.docker.com/_/openjdk/) 、[python](https://hub.docker.com/_/python/) 、[ruby](https://hub.docker.com/_/ruby/) 、[golang](https://hub.docker.com/_/golang/) 等
- 如果没有找到对应服务的镜像，官方镜像中还提供了一些更为基础的操作系统镜像
    - 如: ubuntu、debian、[centos](https://hub.docker.com/_/centos/) 、fedora、alpine 等

除了选择现有镜像为基础镜像外，Docker 还存在一个特殊的镜像，名为 scratch。这个镜像是虚拟的概念，并不实际存在，它表示一个空白的镜像。

```
FROM scratch
...
```

- 如果你以 scratch 为基础镜像的话，意味着你不以任何镜像为基础，接下来所写的指令将作为镜像第一层开始存在。
- 不以任何系统为基础，直接将可执行文件复制进镜像的做法并不罕见，比如 swarm、coreos/etcd
- 对于 Linux 下静态编译的程序来说，并不需要有操作系统提供运行时支持，所需的一切库都已经在可执行文件里了，因此直接 FROM scratch 会让镜像体积更加小巧。
- 使用 Go 语言 开发的应用很多会使用这种方式来制作镜像，这也是为什么有人认为 Go 是特别适合容器微服务架构的语言的原因之一。

<h2 id="c40a005104159611a8abcc3e7f4e8e8f"></h2>


### RUN 执行命令

RUN 指令是用来执行命令行命令的。由于命令行的强大能力，RUN 指令在定制镜像时是最常用的指令之一。其格式有两种：

- shell 格式：RUN <命令>，就像直接在命令行中输入的命令一样。
    - 刚才写的 Dockrfile 中的 RUN 指令就是这种格式。
- exec 格式：RUN ["可执行文件", "参数1", "参数2"]，这更像是函数调用中的格式。

既然 RUN 就像 Shell 脚本一样可以执行命令，那么我们是否就可以像 Shell 脚本一样把每个命令对应一个 RUN 呢？比如这样：

```
FROM debian:jessie

RUN apt-get update
RUN apt-get install -y gcc libc6-dev make
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-3.2.5.tar.gz"
RUN mkdir -p /usr/src/redis
RUN tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1
RUN make -C /usr/src/redis
RUN make -C /usr/src/redis install
```

之前说过，Dockerfile 中每一个指令都会建立一层，RUN 也不例外。

每一个 RUN 的行为，就和刚才我们手工建立镜像的过程一样：新建立一层，在其上执行这些命令，执行结束后，commit 这一层的修改，构成新的镜像。

而上面的这种写法，创建了 7 层镜像。这是完全没有意义的，而且很多运行时不需要的东西，都被装进了镜像里，比如编译环境、更新的软件包等等。结果就是产生非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。 这是很多初学 Docker 的人常犯的一个错误。

Union FS 是有最大层数限制的，比如 AUFS，曾经是最大不得超过 42 层，现在是不得超过 127 层。

上面的 Dockerfile 正确的写法应该是这样：

```
FROM debian:jessie

RUN buildDeps='gcc libc6-dev make' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-3.2.5.tar.gz" \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && make -C /usr/src/redis \
    && make -C /usr/src/redis install \
    && rm -rf /var/lib/apt/lists/* \
    && rm redis.tar.gz \
    && rm -r /usr/src/redis \
    && apt-get purge -y --auto-remove $buildDeps
```

Dockerfile 支持 Shell 类的行尾添加 \ 的命令换行方式，以及行首 # 进行注释的格式。良好的格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

此外，还可以看到这一组命令的最后添加了清理工作的命令，删除了为了编译构建所需要的软件，清理了所有下载、展开的文件，并且还清理了 apt 缓存文件。这是很重要的一步，我们之前说过，镜像是多层存储，每一层的东西并不会在下一层被删除，会一直跟随着镜像。因此镜像构建时，一定要确保每一层只添加真正需要添加的东西，任何无关的东西都应该清理掉。

很多人初学 Docker 制作出了很臃肿的镜像的原因之一，就是忘记了每一层构建的最后一定要清理掉无关文件。

<h2 id="0cd7fc52e88767f46089b6fc4bc14cdc"></h2>


### 构建镜像

好了，让我们再回到之前定制的 nginx 镜像的 Dockerfile 来。让我们来构建这个镜像吧。

在 Dockerfile 文件所在目录执行：

```
$ docker build -t nginx:v3 .
```

输出: 

```
Step 1/2 : FROM nginx
---> 66216d141be6
Step 2/2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
---> Running in fc71a215b873
---> 3bee9a6a80f2
Removing intermediate container fc71a215b873
Successfully built 3bee9a6a80f2
Successfully tagged nginx:v3
```

docker build 命令

```
docker build [选项] <上下文路径/URL/->
```

在这里我们指定了最终镜像的名称 -t nginx:v3，构建成功后，我们可以像之前运行 nginx:v2 那样来运行这个镜像，其结果会和 nginx:v2 一样。

<h2 id="697df4e515f25078aa8b3ba4573d6964"></h2>


### 镜像构建上下文（Context）

我们的 docker build 命令最后有一个 `.` 

不少初学者以为这个路径是在指定 Dockerfile 所在路径，这么理解其实是不准确的。如果对应上面的命令格式，你可能会发现，这是在指定上下文路径。那么什么是上下文呢？

- 首先我们要理解 docker build 的工作原理。Docker 在运行时分为 Docker 引擎（也就是服务端守护进程）和客户端工具。
- Docker 的引擎提供了一组 REST API，被称为 Docker Remote API，而如 docker 命令这样的客户端工具，则是通过这组 API 与 Docker 引擎交互，从而完成各种功能。
- 因此，虽然表面上我们好像是在本机执行各种 docker 功能，但实际上，一切都是使用的远程调用形式在服务端（Docker 引擎）完成。
- 当我们进行镜像构建的时候，并非所有定制都会通过 RUN 指令完成，经常会需要将一些本地文件复制进镜像，比如通过 COPY 指令、ADD 指令等。
- 而 docker build 命令构建镜像，其实并非在本地构建，而是在服务端，也就是 Docker 引擎中构建的。

那么在这种客户端/服务端的架构中，如何才能让服务端获得本地文件呢？

- 这就引入了上下文的概念。当构建的时候，用户会指定构建镜像上下文的路径，docker build 命令得知这个路径后，会将路径下的所有内容打包，然后上传给 Docker 引擎。这样 Docker 引擎收到这个上下文包后，展开就会获得构建镜像所需的一切文件。

如果在 Dockerfile 中这么写：

```
COPY ./package.json /app/
```

这并不是要复制执行 docker build 命令所在的目录下的 package.json，也不是复制 Dockerfile 所在目录下的 package.json，而是复制 上下文（context） 目录下的 package.json。

因此，COPY 这类指令中的源文件的路径都是相对路径。这也是初学者经常会问的为什么 COPY ../package.json /app 或者 COPY /opt/xxxx /app 无法工作的原因，因为这些路径已经超出了上下文的范围，Docker 引擎无法获得这些位置的文件。如果真的需要那些文件，应该将它们复制到上下文目录中去。

现在就可以理解刚才的命令 docker build -t nginx:v3 . 中的这个 .，实际上是在指定上下文的目录，docker build 命令会将该目录下的内容打包交给 Docker 引擎以帮助构建镜像。

如果观察 docker build 输出，我们其实已经看到了这个发送上下文的过程：

```
$ docker build -t nginx:v3 .
Sending build context to Docker daemon 2.048 kB
...
```

一般来说，应该会将 Dockerfile 置于一个空目录下，或者**项目**根目录下。如果该目录下没有所需文件，那么应该把所需文件复制一份过来。如果目录下有些东西确实不希望构建时传给 Docker 引擎，那么可以用 .gitignore 一样的语法写一个 .dockerignore，该文件是用于剔除不需要作为上下文传递给 Docker 引擎的。

```dockerignore
# .dockerignore

# Ignore everything
**

# Allow files and directories
!/file.txt
!/src/**

# Ignore unnecessary files inside allowed directories
# This should go after the allowed directories
**/*~
**/*.log
**/.DS_Store
**/Thumbs.db
```

<h2 id="e2ccb8bb6d2b9d1f6ef53430262eb335"></h2>


### 其它 docker build 的用法

<h2 id="e3b76237c22c121138eb68b7e15928ed"></h2>


#### 直接用 Git repo 进行构建

docker build 还支持从 URL 构建，比如可以直接从 Git repo 中构建：

```
$ docker build https://github.com/twang2218/gitlab-ce-zh.git#:8.14
docker build https://github.com/twang2218/gitlab-ce-zh.git\#:8.14
Sending build context to Docker daemon 2.048 kB
Step 1 : FROM gitlab/gitlab-ce:8.14.0-ce.0
8.14.0-ce.0: Pulling from gitlab/gitlab-ce
aed15891ba52: Already exists
773ae8583d14: Already exists
...
```

这行命令指定了构建所需的 Git repo，并且指定默认的 master 分支，构建目录为 /8.14/，然后 Docker 就会自己去 git clone 这个项目、切换到指定分支、并进入到指定目录后开始构建。

<h2 id="ffc9590011c00baebbf79d7d2db28ba3"></h2>


#### 用给定的 tar 压缩包构建

```
$ docker build http://server/context.tar.gz
```

如果所给出的 URL 不是个 Git repo，而是个 tar 压缩包，那么 Docker 引擎会下载这个包，并自动解压缩，以其作为上下文，开始构建。


<h2 id="20183161339129a8f9da73bc60cc95ba"></h2>


#### 从标准输入中读取 Dockerfile 进行构建

```
docker build - < Dockerfile
```

或

```
cat Dockerfile | docker build -
```

如果标准输入传入的是文本文件，则将其视为 Dockerfile，并开始构建。这种形式由于直接从标准输入中读取 Dockerfile 的内容，它没有上下文，因此不可以像其他方法那样可以将本地文件 COPY 进镜像之类的事情。


<h2 id="c3257bd208d0a3934d193cf26aa2df71"></h2>


#### 从标准输入中读取上下文压缩包进行构建

```
$ docker build - < context.tar.gz
```

如果发现标准输入的文件格式是 gzip、bzip2 以及 xz 的话，将会使其为上下文压缩包，直接将其展开，将里面视为上下文，并开始构建。

<h2 id="ab7b66399bb75089097e87d4fe04cf86"></h2>


## Dockerfile 指令详解

<h2 id="36960c37c1514474b4d1eb8f2e9af565"></h2>


### COPY 复制文件

```
COPY <源路径>... <目标路径>
COPY ["<源路径1>",... "<目标路径>"]
```

和 RUN 指令一样，也有两种格式，一种类似于命令行，一种类似于函数调用。

COPY 指令将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置。比如：

```
COPY package.json /usr/src/app/
```

<源路径> 可以是多个，甚至可以是通配符，其通配符规则要满足 Go 的 filepath.Match 规则，如：

```
COPY hom* /mydir/
COPY hom?.txt /mydir/
```

<目标路径> 可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）。

目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。

此外，还需要注意一点，使用 COPY 指令，源文件的各种元数据都会保留。比如读、写、执行权限、文件变更时间等。这个特性对于镜像定制很有用。特别是构建相关文件都在使用 Git 进行管理的时候。


<h2 id="bc734ce94f563958ed54ed85e7c24626"></h2>


### ADD 更高级的复制文件

ADD 指令和 COPY 的格式和性质基本一致。但是在 COPY 基础上增加了一些功能。

- 这个功能其实并不实用，而且不推荐使用
- 如果 <源路径> 为一个 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，ADD 指令将会自动解压缩这个压缩文件到 <目标路径> 去。
- 在某些情况下，这个自动解压缩的功能非常有用，比如官方镜像 ubuntu 中：

```
FROM scratch
ADD ubuntu-xenial-core-cloudimg-amd64-root.tar.gz /
...
```

- 但在某些情况下，如果我们真的是希望复制个压缩文件进去，而不解压缩，这时就不可以使用 ADD 命令了。
- 在 Docker 官方的最佳实践文档中要求，尽可能的使用 COPY，因为 COPY 的语义很明确，就是复制文件而已，而 ADD 则包含了更复杂的功能，其行为也不一定很清晰。
- 最适合使用 ADD 的场合，就是所提及的需要自动解压缩的场合。

<h2 id="d3bc2b31db3b0c82ec91ac3e2f9dd85b"></h2>


### CMD 容器启动命令

CMD 指令的格式和 RUN 相似，也是两种格式：

```
shell 格式：CMD <命令>
exec 格式：CMD ["可执行文件", "参数1", "参数2"...]
```

Docker 不是虚拟机，容器就是进程。既然是进程，那么在启动容器的时候，需要指定所运行的程序及参数。CMD 指令就是用于指定默认的容器主进程的启动命令的。

在运行时可以指定新的命令来替代镜像设置中的这个默认命令。

比如，ubuntu 镜像默认的 CMD 是 /bin/bash，如果我们直接 docker run -it ubuntu 的话，会直接进入 bash。我们也可以在运行时指定运行别的命令，如 `docker run -it ubuntu cat /etc/os-release`。这就是用 cat /etc/os-release 命令替换了默认的 /bin/bash 命令了，输出了系统版本信息。

在指令格式上，一般推荐使用 exec 格式，这类格式在解析时会被解析为 JSON 数组，因此一定要使用双引号 "，而不要使用单引号。

如果使用 shell 格式的话，实际的命令会被包装为 sh -c 的参数的形式进行执行。比如：

```
CMD echo $HOME
```

在实际执行中，会将其变更为：

```
CMD [ "sh", "-c", "echo $HOME" ]
```

这就是为什么我们可以使用环境变量的原因，因为这些环境变量会被 shell 进行解析处理。

---

提到 CMD 就不得不提容器中应用在前台执行和后台执行的问题。这是初学者常出现的一个混淆。

Docker 不是虚拟机，容器中的应用都应该以前台执行，而不是像虚拟机、物理机里面那样，用 upstart/systemd 去启动后台服务，

**容器内没有后台服务的概念**。

一些初学者将 CMD 写为：

```
CMD service nginx start
```

然后发现容器执行后就立即退出了。甚至在容器内去使用 systemctl 命令结果却发现根本执行不了。这就是因为没有搞明白前台、后台的概念，没有区分容器和虚拟机的差异，依旧在以传统虚拟机的角度去理解容器。

对于容器而言，其启动程序就是容器应用进程，容器就是为了主进程而存在的，主进程退出，容器就失去了存在的意义，从而退出，其它辅助进程不是它需要关心的东西。

而使用 service nginx start 命令，则是希望 upstart 来以后台守护进程形式启动 nginx 服务。而刚才说了 CMD service nginx start 会被理解为 CMD [ "sh", "-c", "service nginx start"]，因此主进程实际上是 sh。那么当 service nginx start 命令结束后，sh 也就结束了，sh 作为主进程退出了，自然就会令容器退出。

正确的做法是直接执行 nginx 可执行文件，并且要求以前台形式运行。比如：

```
CMD ["nginx", "-g", "daemon off;"]
```

<h2 id="1cd6041bdc91a8e6a4c862d3636ce5ed"></h2>


### ENTRYPOINT 入口点

ENTRYPOINT 的格式和 RUN 指令格式一样，分为 exec 格式和 shell 格式。

ENTRYPOINT 的目的和 CMD 一样，都是在指定容器启动程序及参数。ENTRYPOINT 在运行时也可以替代，不过比 CMD 要略显繁琐，需要通过 docker run 的参数 --entrypoint 来指定。

当指定了 ENTRYPOINT 后，CMD 的含义就发生了改变，不再是直接的运行其命令，而是将 CMD 的内容作为参数传给 ENTRYPOINT 指令，换句话说实际执行时，将变为：

```
<ENTRYPOINT> "<CMD>"
```

那么有了 CMD 后，为什么还要有 ENTRYPOINT 呢？这种 `<ENTRYPOINT> "<CMD>"` 有什么好处么？让我们来看几个场景。

**场景一：让镜像变成像命令一样使用**

当存在 ENTRYPOINT 后，CMD 的内容将会作为参数传给 ENTRYPOINT

**场景二：应用运行前的准备工作**

启动容器就是启动主进程，但有些时候，启动主进程前，需要一些准备工作。

比如 mysql 类的数据库，可能需要一些数据库配置、初始化的工作，这些工作要在最终的 mysql 服务器运行之前解决。


此外，可能希望避免使用 root 用户去启动服务，从而提高安全性，而在启动服务前还需要以 root 身份执行一些必要的准备工作，最后切换到服务用户身份启动服务。或者除了服务外，其它命令依旧可以使用 root 身份执行，方便调试等。

这种情况下，可以写一个脚本，然后放入 ENTRYPOINT 中去执行，而这个脚本会将接到的参数（也就是 `<CMD>`）作为命令，在脚本最后执行。

比如官方镜像 redis 中就是这么做的：

```
FROM alpine:3.4
...
RUN addgroup -S redis && adduser -S -G redis redis
...
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 6379
CMD [ "redis-server" ]
```

可以看到其中为了 redis 服务创建了 redis 用户，并在最后指定了 ENTRYPOINT 为 docker-entrypoint.sh 脚本。

<h2 id="15a80d9facd5298221ecbed6e7ee75c7"></h2>


### ENV 设置环境变量

格式有两种：

- ENV `<key>` `<value>`
- ENV `<key1>`=`<value1>` `<key2>`=`<value2>`...

这个指令很简单，就是设置环境变量而已，无论是后面的其它指令，如 RUN，还是运行时的应用，都可以直接使用这里定义的环境变量。

```
ENV VERSION=1.0 DEBUG=on \
    NAME="Happy Feet"
```

这个例子中演示了如何换行，以及对含有空格的值用双引号括起来的办法，这和 Shell 下的行为是一致的。

定义了环境变量，那么在后续的指令中，就可以使用这个环境变量。比如在官方 node 镜像 Dockerfile 中，就有类似这样的代码：

```
ENV NODE_VERSION 7.2.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs
```

下列指令可以支持环境变量展开： 

- ADD、COPY、ENV、EXPOSE、LABEL、USER、WORKDIR、VOLUME、STOPSIGNAL、ONBUILD。

<h2 id="14e2e3b76460818c68b72dfaa4534d96"></h2>


### ARG 构建参数

格式：ARG <参数名>[=<默认值>]

构建参数和 ENV 的效果一样，都是设置环境变量。

所不同的是，ARG 所设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量的。

但是不要因此就使用 ARG 保存密码之类的信息，因为 docker history 还是可以看到所有值的。

Dockerfile 中的 ARG 指令是定义参数名称，以及定义其默认值。该默认值可以在构建命令 docker build 中用 --build-arg <参数名>=<值> 来覆盖。

<h2 id="49b45cf4204f235e160ea09e07a16829"></h2>


### VOLUME 定义匿名卷

格式为：
 
- VOLUME ["<路径1>", "<路径2>"...]
- VOLUME <路径>

之前我们说过，容器运行时应该尽量保持容器存储层不发生写操作，对于数据库类需要保存动态数据的应用，其数据库文件应该保存于卷(volume)中, 后面的章节我们会进一步介绍 Docker 卷的概念.

为了防止运行时用户忘记将动态文件所保存目录挂载为卷，在 Dockerfile 中，我们可以事先指定某些目录挂载为匿名卷，这样在运行时如果用户不指定挂载，其应用也可以正常运行，不会向容器存储层写入大量数据。

```
VOLUME /data
```

这里的 /data 目录就会在运行时自动挂载为匿名卷，任何向 /data 中写入的信息都不会记录进容器存储层，从而保证了容器存储层的无状态化。当然，运行时可以覆盖这个挂载设置。比如：

```
docker run -d -v mydata:/data xxxx
```

在这行命令中，就使用了 mydata 这个命名卷挂载到了 /data 这个位置，替代了 Dockerfile 中定义的匿名卷的挂载配置。

<h2 id="a7a926de3ef2a0c352f59030d0bbc6dd"></h2>


### EXPOSE 声明端口

格式为 EXPOSE <端口1> [<端口2>...]

EXPOSE 指令是声明运行时容器提供服务端口，这只是一个声明，在运行时并不会因为这个声明应用就会开启这个端口的服务。

在 Dockerfile 中写入这样的声明有两个好处，

- 一个是帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射；
- 另一个用处则是在运行时使用随机端口映射时，也就是 docker run -P 时，会自动随机映射 EXPOSE 的端口。

要将 EXPOSE 和在运行时使用 -p <宿主端口>:<容器端口> 区分开来。

- -p，是映射宿主端口和容器端口，换句话说，就是将容器的对应端口服务公开给外界访问，
- 而 EXPOSE 仅仅是声明容器打算使用什么端口而已，并不会自动在宿主进行端口映射。


<h2 id="5a844af8a8f0576eb7a818856d201a20"></h2>


### WORKDIR 指定工作目录

格式为 WORKDIR <工作目录路径>。

使用 WORKDIR 指令可以来指定工作目录（或者称为当前目录），以后各层的当前目录就被改为指定的目录，如该目录不存在，WORKDIR 会帮你建立目录。

之前提到一些初学者常犯的错误是把 Dockerfile 等同于 Shell 脚本来书写，这种错误的理解还可能会导致出现下面这样的错误：

```
RUN cd /app
RUN echo "hello" > world.txt
```

如果将这个 Dockerfile 进行构建镜像运行后，会发现找不到 /app/world.txt 文件，或者其内容不是 hello。

而在 Dockerfile 中，这两行 RUN 命令的执行环境根本不同，是两个完全不同的容器。这就是对 Dokerfile 构建分层存储的概念不了解所导致的错误。

因此如果需要改变以后各层的工作目录的位置，那么应该使用 WORKDIR 指令。


<h2 id="40211142c56583b06d2fe618fa0b3405"></h2>


### USER 指定当前用户

格式：USER <用户名>

USER 指令和 WORKDIR 相似，都是改变环境状态并影响以后的层。WORKDIR 是改变工作目录，USER 则是改变之后层的执行 RUN, CMD 以及 ENTRYPOINT 这类命令的身份。

这个用户必须是事先建立好的，否则无法切换。

```
RUN groupadd -r redis && useradd -r -g redis redis
USER redis
RUN [ "redis-server" ]
```

如果以 root 执行的脚本，在执行期间希望改变身份，比如希望以某个已经建立好的用户来运行某个服务进程，不要使用 su 或者 sudo，这些都需要比较麻烦的配置，而且在 TTY 缺失的环境下经常出错。建议使用 gosu，可以从其项目网站看到进一步的信息：https://github.com/tianon/gosu

```
# 建立 redis 用户，并使用 gosu 换另一个用户执行命令
RUN groupadd -r redis && useradd -r -g redis redis
# 下载 gosu
RUN wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true
# 设置 CMD，并以另外的用户执行
CMD [ "exec", "gosu", "redis", "redis-server" ]
```


<h2 id="28feabf1a02ad73fb34a3d5aa47c26e9"></h2>


### HEALTHCHECK 健康检查

格式：

- HEALTHCHECK [选项] CMD <命令>：设置检查容器健康状况的命令
- HEALTHCHECK NONE：如果基础镜像有健康检查指令，使用这行可以屏蔽掉其健康检查指令

HEALTHCHECK 指令是告诉 Docker 应该如何进行判断容器的状态是否正常，这是 Docker 1.12 引入的新指令。

通过该指令指定一行命令，用这行命令来判断容器主进程的服务状态是否还正常，从而比较真实的反应容器实际状态。

当在一个镜像指定了 HEALTHCHECK 指令后，用其启动容器，初始状态会为 starting，在 HEALTHCHECK 指令检查成功后变为 healthy，如果连续一定次数失败，则会变为 unhealthy。

HEALTHCHECK 支持下列选项：

- --interval=<间隔>：两次健康检查的间隔，默认为 30 秒；
- --timeout=<时长>：健康检查命令运行超时时间，如果超过这个时间，本次健康检查就被视为失败，默认 30 秒；
- --retries=<次数>：当连续失败指定次数后，则将容器状态视为 unhealthy，默认 3 次。

和 CMD, ENTRYPOINT 一样，HEALTHCHECK 只可以出现一次，如果写了多个，只有最后一个生效。

在 HEALTHCHECK [选项] CMD 后面的命令，格式和 ENTRYPOINT 一样，分为 shell 格式，和 exec 格式。命令的返回值决定了该次健康检查的成功与否：0：成功；1：失败；2：保留，不要使用这个值。

假设我们有个镜像是个最简单的 Web 服务，我们希望增加健康检查来判断其 Web 服务是否在正常工作，我们可以用 curl 来帮助判断，其 Dockerfile 的 HEALTHCHECK 可以这么写：

```
FROM nginx
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -fs http://localhost/ || exit 1
```

这里我们设置了每 5 秒检查一次（这里为了试验所以间隔非常短，实际应该相对较长），如果健康检查命令超过 3 秒没响应就视为失败，并且使用 curl -fs http://localhost/ || exit 1 作为健康检查命令。

使用 docker build 来构建这个镜像：

```
$ docker build -t myweb:v1 .
```

构建好了后，我们启动一个容器：

```
$ docker run -d --name web -p 80:80 myweb:v1
```

当运行该镜像后，可以通过 docker ps 看到最初的状态为 (health: starting)：

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                            PORTS               NAMES
03e28eb00bd0        myweb:v1            "nginx -g 'daemon off"   3 seconds ago       Up 2 seconds (health: starting)   80/tcp, 443/tcp     web
```

在等待几秒钟后，再次 docker ps，就会看到健康状态变化为了 (healthy)：


```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS               NAMES
03e28eb00bd0        myweb:v1            "nginx -g 'daemon off"   18 seconds ago      Up 16 seconds (healthy)   80/tcp, 443/tcp     web
```


为了帮助排障，健康检查命令的输出（包括 stdout 以及 stderr）都会被存储于健康状态里，可以用 docker inspect 来查看。

```
$ docker inspect --format '{{json .State.Health}}' web | python -m json.tool
```

<h2 id="8487eec94911eb65c7d2f4bc18cbbe2b"></h2>


### ONBUILD 为他人做嫁衣裳

格式：ONBUILD <其它指令>。

ONBUILD 是一个特殊的指令，它后面跟的是其它指令，比如 RUN, COPY 等，而这些指令，在当前镜像构建时并不会被执行。只有当以当前镜像为基础镜像，去构建下一级镜像的时候才会被执行。

Dockerfile 中的其它指令都是为了定制当前镜像而准备的，唯有 ONBUILD 是为了帮助别人定制自己而准备的。

TODO






---

<h2 id="84c8ea5f92b2186182f00a2443cbab12"></h2>


# 操作容器

简单的说，容器是独立运行的一个或一组应用，以及它们的运行态环境.

<h2 id="b093c1c365b165c1d14e32dba65e94f6"></h2>


## 启动容器

<h2 id="54aae6275e57c681fe430764be974c77"></h2>


### 新建并启动

下面的命令输出一个 “Hello World”，之后终止容器。

```
docker run ubuntu:14.04 /bin/echo 'Hello world'
```

下面的命令则启动一个 bash 终端，允许用户进行交互。

```
$ docker run -t -i ubuntu:14.04 /bin/bash
root@af8bae53bdd3:/#
```

其中，-t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开。


<h2 id="63e39864e294349dc722ce9ba8b51ee7"></h2>


### 启动已终止容器

可以利用 docker start 命令，直接将一个已经终止的容器启动运行。


<h2 id="28b855ee0bcfa0640199f634fb5c23a0"></h2>


## 后台(background)运行


更多的时候，需要让 Docker在后台运行而不是直接把执行命令的结果输出在当前宿主机下。此时，可以通过添加 -d 参数来实现。

此时容器会在后台运行并不会把输出的结果(STDOUT)打印到宿主机上面(输出结果可以用docker logs 查看)。

```
docker logs [container ID or NAMES]
```

**注： 容器是否会长久运行，是和docker run指定的命令有关，和 -d 参数无关**

使用 -d 参数启动后会返回一个唯一的 id，也可以通过 docker ps 命令来查看容器信息。


<h2 id="cd1786012578ed41f6a2435c1dcc5966"></h2>


### 终止容器

- 可以使用 docker stop 来终止一个运行中的容器
- 此外，当Docker容器中指定的应用终结时，容器也自动终止。
- 处于终止状态的容器，可以通过 docker start 命令来重新启动。
    - 此外，docker restart 命令会将一个运行态的容器终止，然后再重新启动它。

<h2 id="51fddac8e0d43b8c4cedf5c7536a2b12"></h2>


## 进入容器

在使用 -d 参数时，容器启动后会进入后台。 某些时候需要进入容器进行操作，有很多种方法，包括使用 docker attach 命令或 nsenter 工具等。

<h2 id="ed8bd9329f54fdae47e248ee852d1a1d"></h2>


### attach 命令

```
docker attach [container ID or NAMES]
```

<h2 id="bfc5650eb46f0bddb423c490b0c28be3"></h2>


## 导出和导入容器

如果要导出本地某个容器，可以使用 docker export 命令。

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                    PORTS               NAMES
7691a814370e        ubuntu:14.04        "/bin/bash"         36 hours ago        Exited (0) 21 hours ago                       test
$ docker export 7691a814370e > ubuntu.tar
```

这样将导出容器快照到本地文件。

<h2 id="21eccb9f6a6709dc17c387515e123d28"></h2>


### 导入容器快照

可以使用 docker import 从容器快照文件中再导入为镜像，例如

```
$ cat ubuntu.tar | docker import - test/ubuntu:v1.0
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              VIRTUAL SIZE
test/ubuntu         v1.0                9d37a6082e97        About a minute ago   171.3 MB
```

此外，也可以通过指定 URL 或者某个目录来导入，例如

```
docker import http://example.com/exampleimage.tgz example/imagerepo
```

**注**

- 用户既可以使用 docker load 来导入镜像存储文件到本地镜像库，也可以使用 docker import 来导入一个容器快照到本地镜像库。
- 这两者的区别在于容器快照文件将丢弃所有的历史记录和元数据信息（即仅保存容器当时的快照状态）
    - 而镜像存储文件将保存完整记录，体积也要大。
- 此外，从容器快照文件导入时可以重新指定标签等元数据信息。


<h2 id="2f4aaddde33c9b93c36fd2503f3d122b"></h2>


## 删除

```
$ docker rm  trusting_newton
```

如果要删除一个运行中的容器，可以添加 -f 参数。Docker 会发送 SIGKILL 信号给容器。

<h2 id="cd287c2794249580cfc4de4006ac9362"></h2>


### 清理所有处于终止状态的容器

```
docker rm $(docker ps -a -q)
```

**注意：这个命令其实会试图删除所有的包括还在运行中的容器，不过就像上面提过的 docker rm 默认并不会删除运行中的容器.**


<h2 id="5e6078663fa925398d77b106c67215db"></h2>


# 访问仓库   Repository

<h2 id="ec104a6054aee6dccf8a9fc8f6842317"></h2>


## Docker Hub

**登录**

可以通过执行 docker login 命令来输入用户名、密码和邮箱来完成注册和登录。 注册成功后，本地用户目录的 .dockercfg 中将保存用户的认证信息。

**基本操作**

用户无需登录即可通过 docker search 命令来查找官方仓库中的镜像，并利用 docker pull 命令来将它下载到本地。

例如以 centos 为关键词进行搜索：

```
docker search centos
```

根据是否是官方提供，可将镜像资源分为两类。 一种是类似 centos 这样的基础镜像，被称为基础或根镜像。这些基础镜像是由 Docker 公司创建、验证、支持、提供。这样的镜像往往使用单个单词作为名字。 还有一种类型，比如 tianon/centos 镜像，它是由 Docker 的用户创建并维护的，往往带有用户名称前缀。可以通过前缀 user_name/ 来指定使用某个用户提供的镜像，比如 tianon 用户。

另外，在查找的时候通过 -s N 参数可以指定仅显示评价为 N 星以上的镜像（新版本Docker推荐使用--filter=stars=N参数）。

**下载**

```
docker pull centos
```

用户也可以在登录后通过 docker push 命令来将镜像推送到 Docker Hub。

**自动创建**

自动创建（Automated Builds）功能对于需要经常升级镜像内程序来说，十分方便。

有时候，用户创建了镜像，安装了某个软件，如果软件发布新版本则需要手动更新镜像。。

而自动创建允许用户通过 Docker Hub 指定跟踪一个目标网站（目前支持 GitHub 或 BitBucket）上的项目，一旦项目发生新的提交，则自动执行创建。

要配置自动创建，包括如下的步骤：

- 创建并登录 Docker Hub，以及目标网站；
- 在目标网站中连接帐户到 Docker Hub；
- 在 Docker Hub 中 [配置一个自动创建](https://registry.hub.docker.com/builds/add/)
- 选取一个目标网站中的项目（需要含 Dockerfile）和分支；
- 指定 Dockerfile 的位置，并提交创建。

之后，可以 在Docker Hub 的 [自动创建页面](https://registry.hub.docker.com/builds/) 中跟踪每次创建的状态。


<h2 id="96387a3a5055939b42bfc6181ba784df"></h2>


## 私有仓库

<h2 id="8c80d32c81877be8ad508c7e075bbc13"></h2>


### Deploy a registry server

- Before you can deploy a registry, you need to install Docker on the host.
- A registry is an instance of the *registry* image, and runs within Docker.

<h2 id="5f65c52efba3f11c0512e5433920dc5e"></h2>


#### Run a local registry

```
$ docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

- The registry is now ready to use.
- Warning: These first few examples show registry configurations that are only appropriate for testing. A production-ready registry must be protected by TLS and should ideally use an access-control mechanism.

<h2 id="17443590fa63f19e5857da6f6407d646"></h2>


#### Copy an image from Docker Hub to your registry

1. Pull the ubuntu:16.04 image from Docker Hub.

```
docker pull ubuntu:16.04
```

2. Tag the image as `localhost:5000/my-ubuntu`.   This creates an additional tag for the existing image. When the first part of the tag is a hostname and port, Docker interprets this as the location of a registry, when pushing.

```
$ docker tag ubuntu:16.04 localhost:5000/my-ubuntu
```

if the register does not run on your local machine , change the `localhost` to your IP.

```
$ docker tag ubuntu:16.04 <YOUR_IP>:5000/my-ubuntu
```

- PROBLEM: http: server gave HTTP response to HTTPS client
- SOLUTION:
    - 1 Create or modify /etc/docker/daemon.json `{ "insecure-registries":["myregistry.example.com:5000"] }`
    - 2 Restart docker daemon `service docker restart`

3. Push the image to the local registry running at localhost:5000:

```
$ docker push localhost:5000/my-ubuntu
```

4. Remove the locally-cached ubuntu:16.04 and localhost:5000/my-ubuntu images, so that you can test pulling the image from your registry. 

```
$ docker image remove ubuntu:16.04
$ docker image remove localhost:5000/my-ubuntu
```

5. Pull the localhost:5000/my-ubuntu image from your local registry.

```
$ docker pull localhost:5000/my-ubuntu
```

For more details: [registry deploy and config](https://docs.docker.com/registry/deploying/)

<h2 id="919d9a1b6552e2443bcba07ac2fcf531"></h2>


## 配置文件 TODO




---

<h2 id="092d280d669c713c8778047dbe6b2259"></h2>


# Docker 数据管理


在容器中管理数据主要有两种方式：

- 数据卷（Data volumes）
- 数据卷容器（Data volume containers）


<h2 id="99b935d7193a1934689a928ae0139d33"></h2>


## 数据卷

数据卷是一个可供一个或多个容器使用的特殊目录，它绕过 UFS，可以提供很多有用的特性：

- 数据卷可以在容器之间共享和重用
- 对数据卷的修改会立马生效
- 对数据卷的更新，不会影响镜像
- 数据卷默认会一直存在，即使容器被删除

*注意：数据卷的使用，类似于 Linux 下对目录或文件进行 mount，镜像中的被指定为挂载点的目录中的文件会隐藏掉，能显示看的是挂载的数据卷*

<h2 id="f1a6ea6cc69a550bafe35f56eb079327"></h2>


### 创建一个数据卷

- 在用 docker run 命令的时候，使用 -v 标记来创建一个数据卷并挂载到容器里。
- 在一次 run 中多次使用可以挂载多个数据卷。

下面创建一个名为 web 的容器，并加载一个数据卷到容器的 /webapp 目录。

```
docker run -d -P --name web -v /webapp training/webapp python app.py
```

*注意：也可以在 Dockerfile 中使用 VOLUME 来添加一个或者多个新的卷到由该镜像创建的任意容器。*

<h2 id="9e416de2b887c7c78160255665c297bd"></h2>


### 删除数据卷

- 数据卷是被设计用来持久化数据的，它的生命周期独立于容器，Docker不会在容器被删除后自动删除数据卷，并且也不存在垃圾回收这样的机制来处理没有任何容器引用的数据卷。
- 如果需要在删除容器的同时移除数据卷。可以在删除容器的时候使用 docker rm -v 这个命令。

<h2 id="e5be13163123d804d337301b9c09eeb4"></h2>


### 挂载一个主机目录作为数据卷

使用 -v 标记也可以指定挂载一个本地主机的目录到容器中去。

```
docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py
```

上面的命令加载主机的 /src/webapp 目录到容器的 /opt/webapp 目录。

这个功能在进行测试的时候十分方便，比如用户可以放置一些程序到本地目录中，来查看容器是否正常工作。本地目录的路径必须是绝对路径，如果目录不存在 Docker 会自动为你创建它。

*注意：Dockerfile 中不支持这种用法，这是因为 Dockerfile 是为了移植和分享用的。然而，不同操作系统的路径格式不一样，所以目前还不能支持*

Docker 挂载数据卷的默认权限是读写，用户也可以通过 :ro 指定为只读。

```
$ sudo docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py
```

<h2 id="f7d1e7013f50a458471e5d4c805fbb4f"></h2>


### 查看数据卷的具体信息

在主机里使用以下命令可以查看指定容器的信息

```
$ docker inspect web
```

<h2 id="bb673754af06a1493de8c9a1255c3947"></h2>


### 挂载一个本地主机文件作为数据卷

-v 标记也可以从主机挂载单个文件到容器中

```
docker run --rm -it -v ~/.bash_history:/.bash_history ubuntu /bin/bash
```

这样就可以记录在容器输入过的命令了。


**注意：如果直接挂载一个文件，很多文件编辑工具，包括 vi 或者 sed --in-place，可能会造成文件 inode 的改变，从 Docker 1.1 .0起，这会导致报错误信息。所以最简单的办法就直接挂载文件的父目录**


<h2 id="2df5c8a6ca62324d4237ab45a6fc7391"></h2>


## 数据卷容器

- 如果你有一些持续更新的数据需要在容器之间共享，最好创建数据卷容器。
- 数据卷容器，其实就是一个正常的容器，专门用来提供数据卷供其它容器挂载的。
- 首先，创建一个名为 dbdata 的数据卷容器：

```
docker run -d -v /dbdata --name dbdata training/postgres echo Data-only container for postgres
```

然后，在其他容器中使用 --volumes-from 来挂载 dbdata 容器中的数据卷。

```
docker run -d --volumes-from dbdata --name db1 training/postgres
docker run -d --volumes-from dbdata --name db2 training/postgres
```

可以使用超过一个的 --volumes-from 参数来指定从多个容器挂载不同的数据卷。 也可以从其他已经挂载了数据卷的容器来级联挂载数据卷。

```
docker run -d --name db3 --volumes-from db1 training/postgres
```

**注意：使用 --volumes-from 参数所挂载数据卷的容器自己并不需要保持在运行状态**

如果删除了挂载的容器（包括 dbdata、db1 和 db2），数据卷并不会被自动删除。如果要删除一个数据卷，必须在删除最后一个还挂载着它的容器时使用 docker rm -v 命令来指定同时删除关联的容器。 这可以让用户在容器之间升级和移动数据卷。具体的操作将在下一节中进行讲解。

<h2 id="35de814218f4269e2c883f78d4f1e504"></h2>


## 利用数据卷容器来备份、恢复、迁移数据卷

可以利用数据卷对其中的数据进行进行备份、恢复和迁移。

<h2 id="664b37da2222287adcb1ecc4e48edb73"></h2>


### 备份

首先使用 --volumes-from 标记来创建一个加载 dbdata 容器卷的容器，并从主机挂载当前目录到容器的 /backup 目录。命令如下：

```
docker run --volumes-from dbdata -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /dbdata
```

容器启动后，使用了 tar 命令来将 dbdata 卷备份为容器中 /backup/backup.tar 文件，也就是主机当前目录下的名为 backup.tar 的文件。

<h2 id="c7db6d4f1a42987a0df962e927926f14"></h2>


### 恢复

如果要恢复数据到一个容器，首先创建一个带有空数据卷的容器 dbdata2。

```
docker run -v /dbdata --name dbdata2 ubuntu /bin/bash
```

然后创建另一个容器，挂载 dbdata2 容器卷中的数据卷，并使用 untar 解压备份文件到挂载的容器卷中。

```
docker run --volumes-from dbdata2 -v $(pwd):/backup busybox tar xvf /backup/backup.tar
```

为了查看/验证恢复的数据，可以再启动一个容器挂载同样的容器卷来查看

```
docker run --volumes-from dbdata2 busybox /bin/ls /dbdata
```


<h2 id="55e0f8921afc8ae4c8c0536410b973af"></h2>


# 使用网络

<h2 id="fe6bb93e4d01fd9317947eef46670807"></h2>


## 外部访问容器

容器中可以运行一些网络应用，要让外部也可以访问这些应用，可以通过 -P 或 -p 参数来指定端口映射。

- 当使用 -P 标记时，Docker 会随机映射一个 49000~49900 的端口到内部容器开放的网络端口。

使用 docker ps 可以看到，本地主机的 49155 被映射到了容器的 5000 端口。此时访问本机的 49155 端口即可访问容器内 web 应用提供的界面。

```
$ sudo docker run -d -P training/webapp python app.py
$ sudo docker ps -l
CONTAINER ID  IMAGE                   COMMAND       CREATED        STATUS        PORTS                    NAMES
bc533791f3f5  training/webapp:latest  python app.py 5 seconds ago  Up 2 seconds  0.0.0.0:49155->5000/tcp  nostalgic_morse
```

同样的，可以通过 docker logs 命令来查看应用的信息。

```
$ docker logs -f nostalgic_morse
* Running on http://0.0.0.0:5000/
10.0.2.2 - - [23/May/2014 20:16:31] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [23/May/2014 20:16:31] "GET /favicon.ico HTTP/1.1" 404 -
```

-p（小写的）则可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。支持的格式有 

- ip:hostPort:containerPort 
- ip::containerPort 
- hostPort:containerPort。

<h2 id="cc4add018dea50c5c26e286522ecaa9f"></h2>


### 映射所有接口地址

使用 hostPort:containerPort 格式本地的 5000 端口映射到容器的 5000 端口，可以执行

```
docker run -d -p 5000:5000 training/webapp python app.py
```

此时默认会绑定本地所有接口上的所有地址。


<h2 id="7a9d7a6fd9999d4c50012bf194a0d5f8"></h2>


### 映射到指定地址的指定端口

可以使用 ip:hostPort:containerPort 格式指定映射使用一个特定地址，比如 localhost 地址 127.0.0.1

```
docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py
```

<h2 id="5bfc1ca85e80abb7f382b15b0d1e05ae"></h2>


### 映射到指定地址的任意端口

使用 ip::containerPort 绑定 localhost 的任意端口到容器的 5000 端口，本地主机会自动分配一个端口。

```
docker run -d -p 127.0.0.1::5000 training/webapp python app.py
```

还可以使用 udp 标记来指定 udp 端口

```
docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
```

<h2 id="2689da8e24fd82172b01f89e377c0081"></h2>


### 查看映射端口配置

使用 docker port 来查看当前映射的端口配置，也可以查看到绑定的地址

```
$ docker port nostalgic_morse 5000
127.0.0.1:49155.
```

注意：

- 容器有自己的内部网络和 ip 地址（使用 docker inspect 可以获取所有的变量，Docker 还可以有一个可变的网络配置。）
- -p 标记可以多次使用来绑定多个端口

```
docker run -d -p 5000:5000  -p 3000:80 training/webapp python app.py
```

<h2 id="06dc7504152a3981b873a938686fbb62"></h2>


## 容器互联

容器的连接（linking）系统是除了端口映射外，另一种跟容器中应用交互的方式。

该系统会在源和接收容器之间创建一个隧道，接收容器可以看到源容器指定的信息。

<h2 id="2a4bb5c86ebcad25a1debf231dc8e752"></h2>


### 自定义容器命名

连接系统依据容器的名称来执行。因此，首先需要自定义一个好记的容器命名。

虽然当创建容器的时候，系统默认会分配一个名字。自定义命名容器有2个好处：

 1. 自定义的命名，比较好记，比如一个web应用容器我们可以给它起名叫web
 2. 当要连接其他容器时候，可以作为一个有用的参考点，比如连接web容器到db容器

使用 --name 标记可以为容器自定义命名。

```
docker run -d -P --name web training/webapp python app.py
```

使用 docker ps 来验证设定的命名。

```
$ sudo docker ps -l
CONTAINER ID  IMAGE                  COMMAND        CREATED       STATUS       PORTS                    NAMES
aed84ee21bde  training/webapp:latest python app.py  12 hours ago  Up 2 seconds 0.0.0.0:49154->5000/tcp  web
```

也可以使用 docker inspect 来查看容器的名字

```
$ sudo docker inspect -f "{{ .Name }}" aed84ee21bde
/web
```

<h2 id="06dc7504152a3981b873a938686fbb62"></h2>


### 容器互联

使用 --link 参数可以让容器之间安全的进行交互。

下面先创建一个新的数据库容器。

```
docker run -d --name db training/postgres
```

删除之前创建的 web 容器

```
docker rm -f web
```

然后创建一个新的 web 容器，并将它连接到 db 容器

```
docker run -d -P --name web --link db:db training/webapp python app.py
```

此时，db 容器和 web 容器建立互联关系。

- --link 参数的格式为 --link name:alias
    - 其中 name 是要链接的容器的名称，alias 是这个连接的别名。

使用 docker ps 来查看容器的连接

```
$ docker ps
CONTAINER ID  IMAGE                     COMMAND               CREATED             STATUS             PORTS                    NAMES
349169744e49  training/postgres:latest  su postgres -c '/usr  About a minute ago  Up About a minute  5432/tcp                 db, web/db
aed84ee21bde  training/webapp:latest    python app.py         16 hours ago        Up 2 minutes       0.0.0.0:49154->5000/tcp  web
```

- 可以看到自定义命名的容器，db 和 web，
- db 容器的 names 列有 db 也有 web/db。
    - 这表示 web 容器链接到 db 容器，web 容器将被允许访问 db 容器的信息。

Docker 在两个互联的容器之间创建了一个安全隧道，而且不用映射它们的端口到宿主主机上。在启动 db 容器的时候并没有使用 -p 和 -P 标记，从而避免了暴露数据库端口到外部网络上。


Docker 通过 2 种方式为容器公开连接信息：

 1. 环境变量
 2. 更新 /etc/hosts 文件

使用 env 命令来查看 web 容器的环境变量

```
$ docker run --rm --name web2 --link db:db training/webapp env
. . .
DB_NAME=/web2/db
DB_PORT=tcp://172.17.0.5:5432
DB_PORT_5000_TCP=tcp://172.17.0.5:5432
DB_PORT_5000_TCP_PROTO=tcp
DB_PORT_5000_TCP_PORT=5432
DB_PORT_5000_TCP_ADDR=172.17.0.5
...
```

- 其中 `DB_` 开头的环境变量是供 web 容器连接 db 容器使用，前缀采用大写的连接别名。

除了环境变量，Docker 还添加 host 信息到父容器的 /etc/hosts 的文件。下面是父容器 web 的 hosts 文件

```
$ sudo docker run -t -i --rm --link db:db training/webapp /bin/bash
root@aed84ee21bde:/opt/webapp# cat /etc/hosts
172.17.0.7  aed84ee21bde
. . .
172.17.0.5  db
```

- 这里有 2 个 hosts，第一个是 web 容器，web 容器用 id 作为他的主机名
- 第二个是 db 容器的 ip 和主机名。

可以在 web 容器中安装 ping 命令来测试跟db容器的连通。

```
root@aed84ee21bde:/opt/webapp# apt-get install -yqq inetutils-ping
root@aed84ee21bde:/opt/webapp# ping db
PING db (172.17.0.5): 48 data bytes
56 bytes from 172.17.0.5: icmp_seq=0 ttl=64 time=0.267 ms
56 bytes from 172.17.0.5: icmp_seq=1 ttl=64 time=0.250 ms
56 bytes from 172.17.0.5: icmp_seq=2 ttl=64 time=0.256 ms
```

用户可以链接多个父容器到子容器，比如可以链接多个 web 到 db 容器上。


<h2 id="89a0c0e3c241795282a7a015dcf8f159"></h2>


# 高级网络配置

- 当 Docker 启动时，会自动在主机上创建一个 docker0 虚拟网桥，
    - 实际上是 Linux 的一个 bridge，可以理解为一个软件交换机。它会在挂载到它的网口之间进行转发。
- 同时，Docker 随机分配一个本地未占用的私有网段（在 RFC1918 中定义）中的一个地址给 docker0 接口。
    - 比如典型的 172.17.42.1，掩码为 255.255.0.0。
    - 此后启动的容器内的网口也会自动分配一个同一网段（172.17.0.0/16）的地址。
- 当创建一个 Docker 容器的时候，同时会创建了一对 veth pair 接口（当数据包发送到一个接口时，另外一个接口也可以收到相同的数据包）
    - 这对接口一端在容器内，即 eth0；另一端在本地并被挂载到 docker0 网桥，名称以 veth 开头（例如 vethAQI2QT）。
- 通过这种方式，主机可以跟容器通信，容器之间也可以相互通信。Docker 就创建了在主机和所有容器之间一个虚拟共享网络。

![](https://yeasy.gitbooks.io/docker_practice/content/advanced_network/_images/network.png)

TODO




=====================================

---

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


# Misc

<h2 id="106810e843fbd66af6ee48cb3ee7e07f"></h2>


## stop / rm all container 

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```


<h2 id="5e7908d41ed1f3e6e1906d575e2dfea0"></h2>


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


<h2 id="e64a823c0142aaac197cc68839f54da9"></h2>


## pass proxy to docker container 

- set https_proxy and http_proxy in you host machine
- `docker run -e https_proxy -e http_proxy ... ` 

<h2 id="ed931520f4337c85396faa61455d56ec"></h2>


## docker daemon proxy for Centos7

- you need set proxy info in 
     - `/etc/systemd/system/docker.service.d/http-proxy.conf`
    - `/etc/systemd/system/docker.service.d/https-proxy.conf`
- for details , see https://docs.docker.com/config/daemon/systemd/#httphttps-proxy 

```
[Service]
Environment="HTTP_PROXY=http://host:port/"
```

```
[Service]                                        
Environment="HTTPS_PROXY=https://host:port/"  
```

<h2 id="68175df37efb964151e614c93d3e62ae"></h2>


## proxy when docker build 

```bash
docker build ... --build-arg http_proxy=http://host:port --build-arg http_proxys=https://host:port
```

<h2 id="5ef5bd47a5282fb1ad1694bbb5f46954"></h2>


## run bash of existing containter

```bash
docker exec -it <container> bash

docker exec -it <container> -- command args 
```


<h2 id="47a7dbe444a0af8498cf01950ad552ef"></h2>


## get DockerFile from Image

```
docker history --no-trunc $argv  | tac | tr -s ' ' | cut -d " " -f 5- | sed 's,^/bin/sh -c #(nop) ,,g' | sed 's,^/bin/sh -c,RUN,g' | sed 's, && ,\n  & ,g' | sed 's,\s*[0-9]*[\.]*[0-9]*[kMG]*B\s*$,,g' | head -n -1
```

- replace `$argv` with your ImageID


<h2 id="9b68cd8277b36a785a1a8784426e3095"></h2>


## add a restart policy to a container 

- i.e.

```
docker update --restart unless-stopped <container>
```


<h2 id="e03d31b41fc936f76920bb647520ef01"></h2>


## docker redis 


- run redis as memory cache

```
# 2.8
docker run -d --restart unless-stopped -p 6379:6379 --name redis-cache-2.8 -d redis:2.8 redis-server --save '' --appendonly no --maxmemory 1G --maxmemory-policy allkeys-lru

# 4.0
docker run -d --restart unless-stopped -p 6379:6379 --name redis-cache-4 -d redis:4.0 redis-server --save '' --appendonly no --maxmemory 1G --maxmemory-policy allkeys-lru

# 4.0,  快找，prod
docker run -d --restart unless-stopped -p 63791:6379 --name redis-cache-4-prod -d redis:4.0 redis-server --appendonly no --maxmemory 1G --maxmemory-policy allkeys-lru --rename-command FLUSHALL "" --rename-command FLUSHDB "" --rename-command CONFIG CONFIG_73e99d --rename-command KEYS ""
```

- with password:  `--requirepass <yourpassword>` 

- check with redis-cli

```bash
redis> config get save
0 save
1 ""
```

- GUI redis client on MacOSX
    - https://github.com/luin/medis


<h2 id="5b1064e3e54b4f22a3419f9d198df904"></h2>


## docker mysql

```
docker run -d --restart unless-stopped -p 3306:3306 --name mysql-test -e MYSQL_USER="root"  -e MYSQL_ROOT_PASSWORD="root" mysql:5.7 --character-set-server=utf8
```


<h2 id="ada28088d8540a0471c00fb0673b9882"></h2>


## docker cleanup

```
docker system prune
docker image prune
docker container prune
```

<h2 id="b64e99ff98a5173b25e6d0d91bc330f3"></h2>


## docker pandoc

```bash
docker run --volume "`pwd`:/data" --user `id -u`:`id -g` --rm  pandoc/latex:2.6
```

