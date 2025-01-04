[](...menustart)

- [OrbStack](#9faf850c7baa5ee4dbd707c977a27c8b)
    - [install](#19ad89bc3e3c9d7ef68b89523eff1987)
        - [if you have already installed Docker Desktop...](#22282a051540360e2ce6d59685fe4142)
    - [Migrate Containers from Docker Desktop](#b3467c5b249c59392691fc075f922adc)
    - [change config & restart](#ec7955673a495dc451e3777191d74208)
    - [和宿主机互通](#6aff2782e923eb11b0b989a9f768e7ee)
        - [ssh](#1787d7646304c5d987cf4e64a3973dc7)

[](...menuend)


<h2 id="9faf850c7baa5ee4dbd707c977a27c8b"></h2>

# OrbStack

<h2 id="19ad89bc3e3c9d7ef68b89523eff1987"></h2>

## install

```bash
brew install orbstack
```

```bash
# run orb to initialize
orb
```

<h2 id="22282a051540360e2ce6d59685fe4142"></h2>

### if you have already installed Docker Desktop...

double check the current docker version.

```bash
$ docker version | grep Context
 Context:           orbstack
```

if the context shows 'Linux/docker', you should manually switch to 'orbstack' context.

```bash
docker context use orbstack
```

<h2 id="b3467c5b249c59392691fc075f922adc"></h2>

## Migrate Containers from Docker Desktop

```bash
orb migrate docker
```


<h2 id="ec7955673a495dc451e3777191d74208"></h2>

## change config & restart

~/.orbstack/config/docker.json

```bash
orb restart docker
```


<h2 id="6aff2782e923eb11b0b989a9f768e7ee"></h2>

## 和宿主机互通

1. `orb` 开头的命令直接操作容器
    - e.g.
    ```bash
    orb sudo apt-get update
    ```
2. 进入 虚拟机
    ```bash
    orb
    ```
3. 回到宿主机
    ```bash
    mac
    ```

<h2 id="1787d7646304c5d987cf4e64a3973dc7"></h2>

### ssh

```bash
ssh [user-name@]<vm-name>@orb
```
