...menustart

- [simctl iOS模拟器操作](#7135c26666c1e715aeffe14303892276)
    - [启动模拟器](#4ec0728efe7e68db35a1e6077f0deaae)
    - [启动某个特定模拟器](#9bb710bd8a9706a3e1f9262e167b9d05)
    - [安装 app bundle 到当前启动的模拟器中](#bfcfd6b70f52469736492a147544d405)
    - [用安装好的 app 打开web页面](#951f42007d7a6df508140b29d5bbe421)
    - [通过 bundle id 启动 app](#a7541a2fc37177c41fa4a72df5e41831)
    - [重启app](#f51c612b79aa3963cad0432d2eaafce7)
    - [应用](#5b0520a9bf5e8d87c0b8c6e58766e184)
        - [获取 激活设备的 apps目录, 并由此活动名字中包含 nba_heroes 的 app 应用目录](#8ae5fd09698f7625952015b04258d4f3)
        - [根据指定 bundle id, 重新打开当前device的相关app](#461860f98245977eac3a2994e72b05be)
        - [安装模拟器版本 app](#777203f91f5115a210fd9dc90df43d15)

...menuend


<h2 id="7135c26666c1e715aeffe14303892276"></h2>


# simctl iOS模拟器操作

<h2 id="4ec0728efe7e68db35a1e6077f0deaae"></h2>


#### 启动模拟器

```bash
open -a "Simulator"  
```

    注： xcode6 可能需要 open -a "iOS Simulator"


<h2 id="9bb710bd8a9706a3e1f9262e167b9d05"></h2>


#### 启动某个特定模拟器

```bash
open -a "iOS Simulator" --args -CurrentDeviceUDID udid
```

    udid 可以通过命令：xcrun simctl list 获得。



<h2 id="bfcfd6b70f52469736492a147544d405"></h2>


#### 安装 app bundle 到当前启动的模拟器中

```bash
xcrun simctl install booted taobao.app
```

    参数 booted 指的是当前启动的模拟器


<h2 id="951f42007d7a6df508140b29d5bbe421"></h2>


#### 用安装好的 app 打开web页面

```bash
xcrun simctl openurl booted taobao://h5.m.taobao.com/guang/index.html
```

    Tips：taobao:// 是模拟器在安装 taobao.app 时注册的协议（scheme），当出现次协议的 URL 请求时默认会使用手机淘宝打开。
    不同的 App 在系统注册的协议各不相同，需要根据实际情况填写。如果需要在 Safari 中打开直接用 http:// 协议头即可。


<h2 id="a7541a2fc37177c41fa4a72df5e41831"></h2>


#### 通过 bundle id 启动 app 

    需要确保 设备 状态是 激活状态


```bash
xcrun simctl launch 945EFCEC-F84E-44AD-AE49-2E61EC7DA29B org.reactjs.native.example.wordShorthand2016
```

会返回 launched app 's pid 

```bash
org.reactjs.native.example.wordShorthand2016: 11497
```

<h2 id="f51c612b79aa3963cad0432d2eaafce7"></h2>


#### 重启app

通过launch 返回的 pid

```bash
kill -9 pid
xcrun simctl launch ...
```

<h2 id="5b0520a9bf5e8d87c0b8c6e58766e184"></h2>


### 应用

<h2 id="8ae5fd09698f7625952015b04258d4f3"></h2>


#### 获取 激活设备的 apps目录, 并由此活动名字中包含 nba_heroes 的 app 应用目录

pcregrep -o1 表示，只输出捕获的 group(1)

```bash
BOOTED_DEVICE=`xcrun simctl list  | pcregrep -o1  '\(([-a-zA-Z0-9]+)\)\s+\(Booted\)'`
APP_PATH=`find /Users/user/Library/Developer/CoreSimulator/Devices/$BOOTED_DEVICE/data/Containers/Bundle/Application -name "Info.plist" | grep nba_heroes | pcregrep -o1 '(.*?)/Info.plist'`
```

<h2 id="461860f98245977eac3a2994e72b05be"></h2>


#### 根据指定 bundle id, 重新打开当前device的相关app

```bash
BOOTED_DEVICE=`xcrun simctl list  | pcregrep -o1  '\(([-a-zA-Z0-9]+)\)\s+\(Booted\)'`
APP_BID='com.testnba.app'
PID_FILE='.pid_app'

kill -9 $(cat $PID_FILE)
xcrun simctl launch $BOOTED_DEVICE $APP_BID  | grep -oE '\d+$'  > $PID_FILE

cat $PID_FILE
```

<h2 id="777203f91f5115a210fd9dc90df43d15"></h2>


#### 安装模拟器版本 app

```bash
xcrun simctl install booted /path/to/your.app
```
