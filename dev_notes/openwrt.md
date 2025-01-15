[](...menustart)

- [openwrt](#27d03b6f0fc0a15464669d7950529cae)
    - [刷固件](#066d67c2a791210e63c8e6777ff65294)
    - [设置](#e366ccf1556c0672dcecba135ed5472e)
- [R2S](#5a7ab9dcc8db0c926579b7534ecf3861)
    - [R2S 连接硬件](#752b8691dd263cd43606d53be8c481fd)
    - [R2S 设置](#50253fdec44f8701e984f78844b449a5)
    - [Rpi 连接](#510b0501c2ea4da197aed7494488e288)
    - [Rpi 设置](#f669ab422f5fcf79de0338fae12db0ea)
- [VBox run openwrt on Host machine](#9d548d8b61422c151c5b8652c1003587)
- [VMWare run openwrt](#50ef7031fba0114ee4c0545b669bf368)
    - [download](#fd456406745d816a45cae554c788e754)
    - [convert image to vmdk](#1db4db8b788df81c79488948b4c11419)
    - [create new Linux VM](#bfd90f2b7e62cddc79f22d128ecbe892)
    - [lanuch openwrt](#7bd4bccda2889c8f0cffb7a333f1a567)
        - [modify IP address](#d1a0135f0e3e61dfd3a41a1b1bfe9667)
        - [install passwall](#8fc6717e5ac38ba94024aa7ae724eac0)

[](...menuend)


<h2 id="27d03b6f0fc0a15464669d7950529cae"></h2>

# openwrt

<h2 id="066d67c2a791210e63c8e6777ff65294"></h2>

## 刷固件

- [lean openwrt](https://github.com/coolsnowwolf/lede)
- [openwrt-rpi](https://github.com/SulingGG/Openwrt-rpi)
- [tool: balena Etcher](https://www.balena.io/etcher/?ref=etcher_footer)

<h2 id="e366ccf1556c0672dcecba135ed5472e"></h2>

## 设置

1. 修改 IP 地址
    ```bash
    vi /etc/config/network
    # option ipaddress
    service network restart
    ```
2. 修改 密码
    - 系统/管理权
3. 网络/接口/LAN
    - + ipv4 网关
    - + option dns: 114.114.114 (vbox 下安装可能需要，确保 可以访问外网)
    - + IPv4 广播:  192.168.71.255 , (e.g.)
    - DHCP
        - 基本设置/ '忽略此接口'
        - ipv6 设置/ 全部'已禁用'
4. 网络/负载均衡
    - 全局/ 本地源接口 / none ?
5. 网络/Turbo ACC
    - + DNS加速
6. 网络/ 'DHCP/DNS'
    - 确认 DNS转发 :  `127.0.0.1#5333`
    - 高级设置: 禁止解析 IPv6 DNS (maybe)
7. passwall
    - 主要
        - 主开关
        - TCP节点/ UDP节点
    - DNS
        - DNS分流: SmartDNS (maybe)
    - 高级设置
        - TCP转发端口: 所有


<h2 id="5a7ab9dcc8db0c926579b7534ecf3861"></h2>

# R2S

<h2 id="752b8691dd263cd43606d53be8c481fd"></h2>

## R2S 连接硬件

- 光猫 -- WAN(R2S)LAN-- WAN(无线路由器)
    - 无线路由 WAN 上网设置 为 DHCP, 自动配置DNS
    - LAN DHCP 也必须开启, 不能和 R2S 在同一个网段
- 光猫 -- WAN(R2S)LAN-- WAN/LAN 任意(AP / 有线中继)
    - 现在无线路由器 就是个 交换机了
    - 无限路由器 设置 静态IP 地址，方便管理
    - 默认网关，DNS服务器1 设置为 R2S IP地址
- 无线路由器 不支持AP模式怎么办？ 手动设置
    - WAN 设置不动
    - 关闭LAN DHCP
    - 重新设置 LAN口局域网IP地址，可以设为和R2S 同一个网段
    - 光猫 -- WAN(R2S)LAN-- LAN 任意( 不能用WAN口 ！)



<h2 id="50253fdec44f8701e984f78844b449a5"></h2>

## R2S 设置

1. 修改密码  系统/管理权
2. 网络接口
	- WAN6  嫌碍眼你就删除。。。
	- WAN   如果光猫拨号，什么也不用动
			如果自己拨号， 设置为 PPPoE
	- LAN   高级设置/ 去掉 IPV6
3. 网络 Turbo Acc 加速
    - 默认只有第一项开启了
    - 可以 再开启 BBR / DNS 加速

<h2 id="510b0501c2ea4da197aed7494488e288"></h2>

## Rpi 连接

- 接到主路由 LAN口

<h2 id="f669ab422f5fcf79de0338fae12db0ea"></h2>

## Rpi 设置

1. [旁路由设置](https://mlapp.cn/1008.html)
2. 电脑网络设置，
    - gateway 设置为 192.168.1.10 ( Rpi )


<h2 id="9d548d8b61422c151c5b8652c1003587"></h2>

# VBox run openwrt on Host machine

https://www.youtube.com/watch?v=XmUGMOoccOc


convert image to vdi

```bash
VBoxManage convertfromraw --format VDI openwrt-x86-64-combined-squashfs.img openwrt.vdi
```

<h2 id="50ef7031fba0114ee4c0545b669bf368"></h2>

# VMWare run openwrt

<h2 id="fd456406745d816a45cae554c788e754"></h2>

## download 

<details>
<summary>install officical release</summary>

https://downloads.openwrt.org/

openwrt-x86-generic-combined-ext4.img.gz



convert image to vmdk

```bash
# 0
brew install qemu
# 1
gunzip ...

# 2
qemu-img convert -f raw -O vmdk  openwrt-15.05-x86-64-combined-ext4.img openwrt-15.05-x86-64-combined-ext4.vmdk
```

</details>


Or immortalwrt  release

https://downloads.immortalwrt.org/

down the `vmdk` file directly

<h2 id="bfd90f2b7e62cddc79f22d128ecbe892"></h2>

## create new Linux VM

img kernel version: https://openwrt.org/docs/techref/targets/kernelversions

- config
    - HDD
        - use an existing virtual disk, select the vmdk file
        - create a copy , NOT share
        - increate HDD size to 0.5G later
    - Advanced
        - Disable Side Channel Mitigations: yes
    - Network: 
        - Bridged Networking / Ethernet


<h2 id="7bd4bccda2889c8f0cffb7a333f1a567"></h2>

## lanuch openwrt

<h2 id="d1a0135f0e3e61dfd3a41a1b1bfe9667"></h2>

### modify IP address

```bash
$ vi /etc/config/network
```

change the IP address to the same subnet as your host machine

`$ reboot`   and access the openwrt web interface

- network/interface:
    - general settrings
        - 'IPV4 Gateway' : your gateway
    - Advanced settings
        - 'Use custom DNS servers':
    - DHCP Server
        - Ignore interface: yes


### Install Passwall

immortalwrt example

```bash
opkg update
opkg install luci-compat luci-lib-ipkg
opkg install luci-app-passwall
```
