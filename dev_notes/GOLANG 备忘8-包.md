# 包


    8.1 工作空间
    可在 GOPATH 中添加多个工作空间，但不能和 GOROOT 相同
    go get 使用第一个工作空间保存下载的第三方库
    8.3 包结构
    源文件头部以 "package " 申明包名称
    包由 同一目录下的多个 源文件组成
    包名类似 namespace, 与包所在的目录名,编辑文件名无关
    目录名最好不用 main, dll, std 这三个保留名称
    可执行文件必须包含 package main, 及 入口函数 main()
    包中成员 以首字母大小写决定访问权限
    8.3.1 导入包
    import 关键字导入, 不能形成导入循环
    导入时，可指定 包成员访问方式, 避免命名冲突
    8.3.2 自定义路径 TODO
    8.3.3 初始化
    初始化函数 func init()
    每个源文件都可以定义 一个或多个 初始化函数
    编辑器不保证 多个初始化函数的 执行次序
    初始化函数在单一线程被调用，仅执行一次
    初始化函数在包内所有全局变量初始化完成后执行
    无法主动调用 初始化函数
    可以初始化函数中使用 goroutine , 可等待其结束
    不要滥用初始化函数, 仅适合完成当前文件中的相关环境设置
    8.4 文档 TODO


## 8.1 工作空间

    每个workspace 必须由 bin,pkg,src 三个目录组成


    |____bin
    |     |____blessing
    |____pkg
    |     |____darwin_amd64
    |           |____c1mHTTPServer.a
    |           |____tools.a
    |____src
          |____blessing
                |____main.go


##### 可在 GOPATH 中添加多个工作空间，但不能和 GOROOT 相同

```bash
export GOPATH=$HOME/projects/golib:$HOME/projects/go
```

##### go get 使用第一个工作空间保存下载的第三方库


## 8.3 包结构

##### 源文件头部以  "package <name>" 申明包名称
##### 包由 同一目录下的多个 源文件组成
##### 包名类似 namespace, 与包所在的目录名,编辑文件名无关
##### 目录名最好不用 main, dll, std 这三个保留名称
##### 可执行文件必须包含 package main, 及 入口函数 main()
##### 包中成员 以首字母大小写决定访问权限

    public: 首字母大写，可被包外访问
    internal: 首字母小写，仅包内成员可以访问

### 8.3.1 导入包

##### import 关键字导入, 不能形成导入循环

```go
import "相对目录/包主文件名"
```

    根目录是指 从 <workspace>/pkg/<os_arch> 开始的子目录
    以标准库为例:

```go
￼import "fmt"      ->  /usr/local/go/pkg/darwin_amd64/fmt.a
import "os/exec"  ->  /usr/local/go/pkg/darwin_amd64/os/exec.a
```

##### 导入时，可指定 包成员访问方式, 避免命名冲突

```go
import     "yuhen/test"     //默认模式 test.A
import  M  "yuhen/test"     // 包重命名  M.A
import  .  "yuhen/test"     // 简便模式  A
import  _  "yuhen/test"     // 仅让该包执行初始化函数�􏱍􏱎􏴄􏳷􏳔􏳃􏰃􏰌
```

local 模式：

    workspace
        |+--- src
                |+--- learn
                        |+--- main.go 
                        |+--- test
                            |+--- test.go


main.go
```go
import "learn/test"  //正常模式
import "./test"      //本地模式，仅 go run main.go 有效
```


### 8.3.2 自定义路径 TODO

### 8.3.3 初始化

##### 初始化函数 func init() 

```go
func init() {
    fmt.Printf("now: %v\n", now)
}
```

##### 每个源文件都可以定义 一个或多个 初始化函数
##### 编辑器不保证 多个初始化函数的 执行次序
##### 初始化函数在单一线程被调用，仅执行一次
##### 初始化函数在包内所有全局变量初始化完成后执行
##### 无法主动调用 初始化函数
##### 可以初始化函数中使用 goroutine , 可等待其结束

```go
var now = time.Now()
func main() {
    fmt.Println("main:", int(time.Now().Sub(now).Seconds()))
}
func init() {
    fmt.Println("init:", int(time.Now().Sub(now).Seconds()))
    w := make(chan bool)
    go func() {
        time.Sleep(time.Second * 3)
        w <- true
    }()
    <-w 
}
输出:
init: 0
main: 3
```

##### 不要滥用初始化函数, 仅适合完成当前文件中的相关环境设置

---

### 8.4 文档 TODO

