# 工具

    工具集
        1.1 go build
        1.2 go install
        1.3 go clean
        1.4 go get
        1.5 go tool objdump
    条件编译
        通过 runtime.GOOS/GOARCH判断，或使用编译约束标记
        "+build"注释, 指示编译器检查相关环境变量
        多个标记合并, 空格表示OR, 逗号AND, 感叹号NOT
        如果GOOS,GOARCH条件不符合, 编译器忽略该文件
        还可使用 文件名来表示编译约束
        忽略某个文件，或指定编译器版本号
    跨平台编译
        首先得生成与平台相关的工具和标准库
        设置 GOOS GOARCH 环境变量编译目标平台文件

## 工具集

### 1.1 go build


参数 |  说明 | 
--- |   --- |   ---
-gcflags | 编译器参数 |
-ldflags    |   连接器参数
-race | 允许数据竞争检测(arm64 only) |
-a  |   强制重新编译所有依赖包 |    
-v  |   查看被编译的包名，包括依赖包    |   
-o  |   输出文件名  |   

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


### 1.2 go install

和 go build 参数相同，将生成文件拷贝到 bin,pkg目录.

优先使用 GOBIN 环境变量指定目录.

### 1.3 go clean

参数 |  说明 
--- |   --- 
-n  | 查看但不执行清理命令
-x  | 查看并执行清理命令
-i  |   清除 bin, pkg 目录下文件
-r  |   清理所有依赖包 临时文件 


### 1.4 go get

下载并安装扩展包.默认保存在GOPATH 第一个workspace

参数 |  说明 
--- |   --- 
-d  |   仅下载，不安装
-t  |   下载测试所需的依赖库
-u  |   更新包，包括其依赖包
-v  |   查看并执行命令


### 1.5 go tool objdump

反汇编可执行文件

```bash
$ go tool objdump -s "main\.\w+" test
$ go tool objdump -s "main\.main" test
```

## 条件编译

##### 通过 runtime.GOOS/GOARCH判断，或使用编译约束标记

```go
// +build darwin linux
                            // 必须有空行
package main
```

##### "+build"注释, 指示编译器检查相关环境变量

##### 多个标记合并, 空格表示OR, 逗号AND, 感叹号NOT

```go
// +build darwin linux
// +build amd64,!cgo
// 合并结果:
// (darwin OR linux) AND (amd64 AND (NOT cgo))
```

##### 如果GOOS,GOARCH条件不符合, 编译器忽略该文件

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

##### 忽略某个文件，或指定编译器版本号

```go
// +build ignore
// +build go1.2   // 最低需要 go 1.2
```

## 跨平台编译

##### 首先得生成与平台相关的工具和标准库

```bash
$ cd /usr/local/go/src
$ GOOS=linux GOARCH=amd64 CGO_ENABLED=0 ./make.bash --no-clean
// 参数 --no-clean 避免清除其他平台文件
```

##### 设置 GOOS GOARCH 环境变量编译目标平台文件

```bash
$ GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o test
$ file test
learn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV)
$ uname -a
Darwin Kernel Version 12.5.0: RELEASE_X86_64 x86_64
```



