...menustart

 - [工具集](#d1f4a2ca5ebae356829301a14367e0e6)
     - [1.1 go build](#5cb3fbe2f5c14eaeec65da239fb2278b)
         - [go build injection](#dc4c1d9510e06b1f42e03832e216b351)
         - [逃逸分析](#39e51e767418357eef4ac9bcb4330f50)
     - [1.2 go install](#bfae2838680a32e56e245ff108957b89)
     - [1.3 go clean](#a0d272d3a24a7f1986e0fa7bafb8a59d)
     - [1.4 go get](#467396f90a34e7517a6fe191507ebab1)
     - [1.5 go tool objdump](#10dff3e07c4de7491ca41d3f3d6a7968)
     - [1.6 go profile: pprof](#97696a7ea989ac7decac2e8be29a04f7)
 - [条件编译](#b19e1a4d4f517ccccc8fd5d402c438f9)
     - [通过 runtime.GOOS/GOARCH判断，或使用编译约束标记](#7fb897f760321cdc29a25ac77a31a041)
     - ["+build"注释, 指示编译器检查相关环境变量](#e4ee5701df42dfb4c09086d79e67d9f6)
     - [多个标记合并, 空格表示OR, 逗号AND, 感叹号NOT](#30ef583d7ef62bad4751c8e2e7299f50)
     - [如果GOOS,GOARCH条件不符合, 编译器忽略该文件](#ba18359c8922124ddf4b2ffbdad4b1d3)
     - [还可使用 文件名来表示编译约束](#e6bd662653ba70b565a32d84722fd015)
     - [忽略某个文件，或指定编译器版本号](#5c0242163713cc576762cc92f3c5e625)
 - [跨平台编译](#9f4c95c3ac51945acde06a53ffa196bd)
     - [首先得生成与平台相关的工具和标准库](#6aa488bb375a987c2f85c02db3220422)
     - [设置 GOOS GOARCH 环境变量编译目标平台文件](#0457f03fb15cf964e191b590da30f15e)

...menuend


<h2 id="d1f4a2ca5ebae356829301a14367e0e6"></h2>


## 工具集

<h2 id="5cb3fbe2f5c14eaeec65da239fb2278b"></h2>


### 1.1 go build


参数 |  说明 
--- |   --- 
-gcflags | 编译器参数 
-ldflags    |   连接器参数
-race | 允许数据竞争检测(arm64 only) 
-a  |   强制重新编译所有依赖包
-v  |   查看被编译的包名，包括依赖包   
-o  |   输出文件名 

gcflags

参数 |  说明 
--- |   --- 
-B  |   禁用边界检查 
-N  |   禁用优化
-l  |   禁用函数内联
-u  |   禁用 unsafe代码
-m  |   输出优化信息
-S  |   输出汇编代码


ldflags

参数 |  说明 | 示例
--- |   ---     |   ---
-w  |   禁用 DRAWF 调试信息
-s  |   禁用符号表
-X  |   修改字符串符号值    |   -X main.VER '0.99'


    go build -ldflags "-s -w" 可以减小 生成文件的大小
    -s 去掉符号表，  然后panic 的时候 stack trace的时候，就没有文件名／行号信息了
    -w 去掉 DWARF 调试信息，得到的程序就不能用 GDB调试了


<h2 id="dc4c1d9510e06b1f42e03832e216b351"></h2>


#### go build injection

```go
package main

import (
        "fmt"
)
var GitCommit string
func main() {
    fmt.Printf("Hello world, version: %s\n", GitCommit)
}
```

```bash
$ go build && \
  ./git-tester
Hello world, version:
```

 - Override go build

```bash
$ export GIT_COMMIT=$(git rev-list -1 HEAD)
$ go build -ldflags "-X main.GitCommit=$GIT_COMMIT"
$ ./git-tester
Hello world, version: 67b05a31758848e1e5237ad5ae1dc11c22d4e71e
```

<h2 id="39e51e767418357eef4ac9bcb4330f50"></h2>


#### 逃逸分析

```
go build -gcflags '-m -l'
```



<h2 id="bfae2838680a32e56e245ff108957b89"></h2>


### 1.2 go install

和 go build 参数相同，将生成文件拷贝到 bin,pkg目录.

优先使用 GOBIN 环境变量指定目录.

<h2 id="a0d272d3a24a7f1986e0fa7bafb8a59d"></h2>


### 1.3 go clean

参数 |  说明 
--- |   --- 
-n  | 查看但不执行清理命令
-x  | 查看并执行清理命令
-i  |   清除 bin, pkg 目录下文件
-r  |   清理所有依赖包 临时文件 


<h2 id="467396f90a34e7517a6fe191507ebab1"></h2>


### 1.4 go get

下载并安装扩展包.默认保存在GOPATH 第一个workspace

参数 |  说明 
--- |   --- 
-d  |   仅下载，不安装
-t  |   下载测试所需的依赖库
-u  |   更新包，包括其依赖包
-v  |   查看并执行命令


<h2 id="10dff3e07c4de7491ca41d3f3d6a7968"></h2>


### 1.5 go tool objdump

反汇编可执行文件

```bash
$ go tool objdump -s "main\.\w+" test
$ go tool objdump -s "main\.main" test
```


<h2 id="97696a7ea989ac7decac2e8be29a04f7"></h2>


### 1.6 go profile: pprof

见 [pprof](golang_pprof.md)


<h2 id="b19e1a4d4f517ccccc8fd5d402c438f9"></h2>


## 条件编译

<h2 id="7fb897f760321cdc29a25ac77a31a041"></h2>


##### 通过 runtime.GOOS/GOARCH判断，或使用编译约束标记

```go
// +build darwin linux
                            // 必须有空行
package main
```

<h2 id="e4ee5701df42dfb4c09086d79e67d9f6"></h2>


##### "+build"注释, 指示编译器检查相关环境变量

<h2 id="30ef583d7ef62bad4751c8e2e7299f50"></h2>


##### 多个标记合并, 空格表示OR, 逗号AND, 感叹号NOT

```go
// +build darwin linux
// +build amd64,!cgo
// 合并结果:
// (darwin OR linux) AND (amd64 AND (NOT cgo))
```

<h2 id="ba18359c8922124ddf4b2ffbdad4b1d3"></h2>


##### 如果GOOS,GOARCH条件不符合, 编译器忽略该文件

<h2 id="e6bd662653ba70b565a32d84722fd015"></h2>


##### 还可使用 文件名来表示编译约束

    支持*_GOOS,*_GOARCH,*_GOOS_GOARCH,*_GOARCH_GOOS格式

```bash
$ ls -l /usr/local/go/src/pkg/runtime
1545 11 29 05:38 os_darwin.c
1382 11 29 05:38 os_darwin.h
6990 11 29 05:38 os_freebsd.c
 791 11 29 05:38 os_freebsd.h
 644 11 29 05:38 os_freebsd_arm.c
8624 11 29 05:38 os_linux.c
1067 11 29 05:38 os_linux.h
 861 11 29 05:38 os_linux_386.c
2418 11 29 05:38 os_linux_arm.c
```

<h2 id="5c0242163713cc576762cc92f3c5e625"></h2>


##### 忽略某个文件，或指定编译器版本号

```go
// +build ignore
// +build go1.2   // 最低需要 go 1.2
```

<h2 id="9f4c95c3ac51945acde06a53ffa196bd"></h2>


## 跨平台编译

<h2 id="6aa488bb375a987c2f85c02db3220422"></h2>


##### 首先得生成与平台相关的工具和标准库

```bash
$ cd /usr/local/go/src
$ GOOS=linux GOARCH=amd64 CGO_ENABLED=0 ./make.bash --no-clean
// 参数 --no-clean 避免清除其他平台文件
```

<h2 id="0457f03fb15cf964e191b590da30f15e"></h2>


##### 设置 GOOS GOARCH 环境变量编译目标平台文件

```bash
$ GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o test
$ file test
learn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV)
$ uname -a
Darwin Kernel Version 12.5.0: RELEASE_X86_64 x86_64
```



