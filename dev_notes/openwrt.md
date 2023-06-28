[](...menustart)

- [openwrt](#27d03b6f0fc0a15464669d7950529cae)
    - [刷固件](#066d67c2a791210e63c8e6777ff65294)
    - [R2S 连接硬件](#752b8691dd263cd43606d53be8c481fd)
    - [R2S 设置](#50253fdec44f8701e984f78844b449a5)
    - [Rpi 连接](#510b0501c2ea4da197aed7494488e288)
    - [Rpi 设置](#f669ab422f5fcf79de0338fae12db0ea)

[](...menuend)


<h2 id="27d03b6f0fc0a15464669d7950529cae"></h2>

# openwrt

<h2 id="066d67c2a791210e63c8e6777ff65294"></h2>

## 刷固件

- [lean openwrt](https://github.com/coolsnowwolf/lede)
- [openwrt-rpi](https://github.com/SulingGG/Openwrt-rpi)
- [tool: balena Etcher](https://www.balena.io/etcher/?ref=etcher_footer)

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
    - DHCP
        - 基本设置/ '忽略此接口'
        - ipv6 设置/ 全部'已禁用'
4. 网络/负载均衡
    - 全局/ 本地源接口 / none ?
5. 网络/Turbo ACC
    - + DNS加速
6. 网络/ 'DHCP/DNS'
    - 确认 DNS转发 :  `127.0.0.1#5333`


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

