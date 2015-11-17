
# simctl iOS模拟器操作

#### 启动模拟器

```bash
open -a "Simulator"  
```

    注： xcode6 可能需要 open -a "iOS Simulator"


#### 启动某个特定模拟器

```bash
open -a "iOS Simulator" --args -CurrentDeviceUDID udid
```

    udid 可以通过命令：xcrun simctl list 获得。



#### 安装 app bundle 到当前启动的模拟器中

```bash
xcrun simctl install booted taobao.app
```

    参数 booted 指的是当前启动的模拟器


#### 用安装好的 app 打开web页面

```bash
xcrun simctl openurl booted taobao://h5.m.taobao.com/guang/index.html
```

    Tips：taobao:// 是模拟器在安装 taobao.app 时注册的协议（scheme），当出现次协议的 URL 请求时默认会使用手机淘宝打开。
    不同的 App 在系统注册的协议各不相同，需要根据实际情况填写。如果需要在 Safari 中打开直接用 http:// 协议头即可。


#### 通过 bundle id 启动 app 

    需要确保 设备 状态是 激活状态


```bash
xcrun simctl launch 945EFCEC-F84E-44AD-AE49-2E61EC7DA29B org.reactjs.native.example.wordShorthand2016
```

会返回 launched app 's pid 

```bash
org.reactjs.native.example.wordShorthand2016: 11497
```

#### 重启app

通过launch 返回的 pid

```bash
kill -9 pid
xcrun simctl launch ...
```

### 应用

#### 获取 激活设备的 apps目录, 并由此活动名字中包含 nba_heroes 的 app 应用目录

```bash
BOOTED_DEVICE=`xcrun simctl list  | grep -oE '\([-a-zA-Z0-9]+\)\s+\(Booted\)' | grep -oE '^\([-a-zA-Z0-9]+'  | grep -oE '[-a-zA-Z0-9]+'`
APP_PATH=`find /Users/qibinyi/Library/Developer/CoreSimulator/Devices/$BOOTED_DEVICE/data/Containers/Bundle/Application -name *.app | grep nba_heroes`
```




