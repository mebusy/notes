...menustart

- [包](#5442dfce9bae4548d3851889266c5381)
    - [8.1 工作空间](#de9cc15b3a9e2ba75fda079cc5b28e1f)
        - [可在 GOPATH 中添加多个工作空间，但不能和 GOROOT 相同](#b3e0604118859c109dd897ac7ae854f8)
        - [go get 使用第一个工作空间保存下载的第三方库](#913047a1d520b9ffb6ca7aec854b966c)
    - [8.3 包结构](#0dbeeae9f285bcc430fd68fe456e41b3)
        - [源文件头部以  "package pkg_name" 申明包名称](#0c04edb05053e4d7e495c33b906f4485)
        - [包由 同一目录下的多个 源文件组成](#6938f144bcee557efd011309c199e35e)
        - [包名类似 namespace, 与包所在的目录名,编辑文件名无关](#e17b159af5c5ad59d85168752c6428f1)
        - [目录名最好不用 main, dll, std 这三个保留名称](#e7c8ec2bebe87fc347307b7aed9b0469)
        - [可执行文件必须包含 package main, 及 入口函数 main()](#aa701bd12fb529e83f40eb243c75e782)
        - [包中成员 以首字母大小写决定访问权限](#f02028bd734d65715515416056124dc4)
        - [8.3.1 导入包](#f62e6d06725318423ee08bd8a4ed2e7d)
            - [import 关键字导入, 不能形成导入循环](#7dba5b53facd739c0eab95743310162a)
            - [导入时，可指定 包成员访问方式, 避免命名冲突](#a6b9ea4812ebe5edb3aeaccc19dbc584)
        - [8.3.2 自定义路径 TODO](#bc316ed1f50721e986d3778dbb98900c)
        - [8.3.3 初始化](#bd32478b325dcb90a9aa82078eb68e07)
            - [初始化函数 func init()](#1c67af6fda4f5fc80c00a7020a74914e)
            - [每个源文件都可以定义 一个或多个 初始化函数](#e0e5e502f607443792fa83dc2e4707db)
            - [编辑器不保证 多个初始化函数的 执行次序](#cd1c90ededc5d3a9ca7a76705db7a874)
            - [初始化函数在单一线程被调用，仅执行一次](#d0e07d685ddabb136c2e116a2d88a07c)
            - [初始化函数在包内所有全局变量初始化完成后执行](#8009dbeb820d7018e73bcf1ff0c7afd1)
            - [无法主动调用 初始化函数](#4d5af1b2778d1d186a0bf2663bfe7186)
            - [可以初始化函数中使用 goroutine , 可等待其结束](#e6bb68503f344f18a7066f6431a5b7a7)
            - [不要滥用初始化函数, 仅适合完成当前文件中的相关环境设置](#688c0716b76107dd51aa2613615246b9)
        - [8.4 文档 TODO](#b99256f3c5776118ab291be9233de98d)

...menuend


<h2 id="5442dfce9bae4548d3851889266c5381"></h2>


# 包




<h2 id="de9cc15b3a9e2ba75fda079cc5b28e1f"></h2>


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


<h2 id="b3e0604118859c109dd897ac7ae854f8"></h2>


##### 可在 GOPATH 中添加多个工作空间，但不能和 GOROOT 相同

```bash
export GOPATH=$HOME/projects/golib:$HOME/projects/go
```

<h2 id="913047a1d520b9ffb6ca7aec854b966c"></h2>


##### go get 使用第一个工作空间保存下载的第三方库


<h2 id="0dbeeae9f285bcc430fd68fe456e41b3"></h2>


## 8.3 包结构

<h2 id="0c04edb05053e4d7e495c33b906f4485"></h2>


##### 源文件头部以  "package pkg_name" 申明包名称
<h2 id="6938f144bcee557efd011309c199e35e"></h2>


##### 包由 同一目录下的多个 源文件组成
<h2 id="e17b159af5c5ad59d85168752c6428f1"></h2>


##### 包名类似 namespace, 与包所在的目录名,编辑文件名无关
<h2 id="e7c8ec2bebe87fc347307b7aed9b0469"></h2>


##### 目录名最好不用 main, dll, std 这三个保留名称
<h2 id="aa701bd12fb529e83f40eb243c75e782"></h2>


##### 可执行文件必须包含 package main, 及 入口函数 main()
<h2 id="f02028bd734d65715515416056124dc4"></h2>


##### 包中成员 以首字母大小写决定访问权限

    public: 首字母大写，可被包外访问
    internal: 首字母小写，仅包内成员可以访问

<h2 id="f62e6d06725318423ee08bd8a4ed2e7d"></h2>


### 8.3.1 导入包

<h2 id="7dba5b53facd739c0eab95743310162a"></h2>


##### import 关键字导入, 不能形成导入循环

```go
import "相对目录/包主文件名"
```

    根目录是指 从 `<workspace>/pkg/<os_arch>` 开始的子目录
    以标准库为例:

```go
import "fmt"      ->  /usr/local/go/pkg/darwin_amd64/fmt.a
import "os/exec"  ->  /usr/local/go/pkg/darwin_amd64/os/exec.a
```

<h2 id="a6b9ea4812ebe5edb3aeaccc19dbc584"></h2>


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


<h2 id="bc316ed1f50721e986d3778dbb98900c"></h2>


### 8.3.2 自定义路径 TODO

<h2 id="bd32478b325dcb90a9aa82078eb68e07"></h2>


### 8.3.3 初始化

<h2 id="1c67af6fda4f5fc80c00a7020a74914e"></h2>


##### 初始化函数 func init() 

```go
func init() {
    fmt.Printf("now: %v\n", now)
}
```

<h2 id="e0e5e502f607443792fa83dc2e4707db"></h2>


##### 每个源文件都可以定义 一个或多个 初始化函数
<h2 id="cd1c90ededc5d3a9ca7a76705db7a874"></h2>


##### 编辑器不保证 多个初始化函数的 执行次序
<h2 id="d0e07d685ddabb136c2e116a2d88a07c"></h2>


##### 初始化函数在单一线程被调用，仅执行一次
<h2 id="8009dbeb820d7018e73bcf1ff0c7afd1"></h2>


##### 初始化函数在包内所有全局变量初始化完成后执行
<h2 id="4d5af1b2778d1d186a0bf2663bfe7186"></h2>


##### 无法主动调用 初始化函数
<h2 id="e6bb68503f344f18a7066f6431a5b7a7"></h2>


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

<h2 id="688c0716b76107dd51aa2613615246b9"></h2>


##### 不要滥用初始化函数, 仅适合完成当前文件中的相关环境设置

---

<h2 id="b99256f3c5776118ab291be9233de98d"></h2>


### 8.4 文档 TODO

