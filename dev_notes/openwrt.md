
# openwrt

## 刷固件

- [lean openwrt](https://github.com/coolsnowwolf/lede)
- [openwrt-rpi](https://github.com/SulingGG/Openwrt-rpi)
- [tool: balena Etcher](https://www.balena.io/etcher/?ref=etcher_footer)


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

## Rpi 连接

- 接到主路由 LAN口

## Rpi 设置

1. [旁路由设置](https://mlapp.cn/1008.html)
2. 电脑网络设置，
    - gateway 设置为 192.168.1.10 ( Rpi )







