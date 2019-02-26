# TCP/IP 详解

## 1 概述

 - 链路层/网络层/传输层/应用层
    - 路由器是 链路层/网络层 
    - 网桥是 链路层
 - 5类ip地址
    - 0 , 128, 192, 224, 240
 - 3类ip地址
    - 单播地址，广播地址, 多播地址
 - TCP/UDP 使用16bit 端口号区别应用程序
 - 以太网帧 分用过程
    - ![](../imgs/tcpip_ehternet_frame_flow.png)
 - 本书测试网络
    - ![](../imgs/tcpip_test_network.png)

## 2 链路层

 - 以太网帧数据，可能是 IP数据报，也可能是 ARP,RARP 的请求/问答
 - 路径MTU, 通讯中，最重要的MTU是 两台通讯主机路径中的最小MTU

## 3 IP

 - 特性
    - unreliable: 不保证达到，出错丢弃，然后发送  ICMP消息报给 信源端
    - connectionless: 独立，可以不按发送顺序接收
 - 3.3 IP路由选择
    - 直接相连，或在一个共享网络(i.e 以太网), IP数据报直接发送到 目的主机
        - 否则， 主机把数据报发给一默认的路由器, 由路由器来转发该数据报.
    - IP层可以从TCP/UDP/ICMP/IGMP接收数据报并发送(即本地生成的数据), 或这从一个网络接口(链路层)接收并发送数据报(即 待转发的数据报)
    - IP层 在内存中有一个路由表
        - 发送时，先搜索路由表一次.
        - 当数据报来自某个网络接口时, IP首先检查 目的IP是否是 本机IP之一，或者 广播地址, 
            - 如果是，送到指定协议模块进行处理
            - 如果不是，(1)如果IP层被设置为路由器功能,则转发, 否则(2)丢弃. 
 - 路由表
    - 路由表中的每一项都包含:
        - 目的IP地址
        - 下一站路由器 (next-hop router) 的IP地址, 或者 有直接连接的网络IP地址
        - 标志
            - 其中一个标志 指明目的地IP地址是 网络地址还是主机地址.
            - 另一个标志 指明下一个路由器是否为真正的下一站路由器, 还是一个直接相连的接口
        - 为数据报的传输 指定一个网络接口
    - 数据报传输过程中，目的地IP地址不变，链路层地址 始终指向 "下一站"的链路层地址(以太网接口地址)
        - 在8.5 中 将看到，只有使用 源路由选项时， 目的IP地址才有可能被修改, 但这种情况很少出现.
        - 以太网地址通过 ARP 获得
 - 子网寻址，子网掩码 
    - 给定IP地址和子网掩码后，主机就可以确定IP数据报的目的是:
        1. 本子网上的主机
        2. 本网络中，其他子网中的主机
        3. 其他网络上的主机
    - 如果知道本机的IP地址，那么就知道踏是否为 A类，B类，C类地址(从IP地址高位可以得知), 也就知道 netid 和subnetid之间的分界线.
    - 而根据子网掩码 就可知道 subnetid与hostid 之间的分界线.
 - 3.6 特殊的IP地址
    - 0 表示所有的 bit 全为0; -1 表示 bit 全为 1 
    - subnetid 为空表示 该地址没有进行子网划分
    - 1和2 是特殊的源地址， 中间是 环回地址， 最后4个是广播地址


netid | subnetid | hostid | source | target | desc 
--- | --- | --- | --- | --- | --- 
 0 |  | 0 |  OK | N/A |  网络上的主机
 0 |  | hostid | OK | N/A | 网络上特定主机 
 127 |  | 任何值 |  Ok | OK  |  环回地址
 -1 | | -1 | N/A | OK | 受限的广播， 永远不被转发
 netid |  | -1 |  N/A | OK | 以网络为目的 向netid 广播
 netid | subnetid | -1 | N/A | OK | 以子网为目的, 向netid、subnetid 广播
 netid | -1 | -1 | N/A | OK | 以所有子网为目的，向 netid广播



 - 3.8 ifconfig
    - `SIMPLEX`: 如果接口发送一帧数据到广播地址，那么就会为本机拷贝一份数据送到 环回地址

```
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
    ether 3c:07:54:69:98:05
    inet6 fe80::10f5:6919:c4ae:b50a%en0 prefixlen 64 secured scopeid 0x6
    inet 10.192.81.132 netmask 0xfffff800 broadcast 10.192.87.255
    nd6 options=201<PERFORMNUD,DAD>
    media: autoselect (1000baseT <full-duplex,energy-efficient-ethernet>)
    status: active
```

 - 3.9 netstat 也提供系统上的接口信息
    - `-i` 打印接口地址 ， `-n`  打印IP地址
    - 可以看到 MTU,输入分组数, 输入错误, 输出分组数,输出错误, 冲突

```
$ netstat -in
Name  Mtu   Network       Address            Ipkts Ierrs    Opkts Oerrs  Coll
lo0   16384 <Link#1>                        318487     0   318487     0     0
lo0   16384 127           127.0.0.1         318487     -   318487     -     -
lo0   16384 ::1/128     ::1                 318487     -   318487     -     -
lo0   16384 fe80::1%lo0 fe80:1::1           318487     -   318487     -     -
gif0* 1280  <Link#2>                             0     0        0     0     0
stf0* 1280  <Link#3>                             0     0        0     0     0
EHC25 0     <Link#4>                             0     0        0     0     0
EHC25 0     <Link#5>                             0     0        0     0     0
en0   1500  <Link#6>    3c:07:54:69:98:05  4497578     0  1183548     0     0
en0   1500  fe80::10f5: fe80:6::10f5:6919  4497578     -  1183548     -     -
en0   1500  10.192.80/21  10.192.81.132    4497578     -  1183548     -     -
en1   1500  <Link#7>    7c:c3:a1:9f:4e:63    26973     0   184365     0     0
en1   1500  169.254       169.254.211.156    26973     -   184365     -     -
...
```

## 4 ARP


    





