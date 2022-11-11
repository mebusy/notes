[](...menustart)

- [go doc 和 godoc](#0b1ba65761a964f84e21fae57faa0496)
    - [go doc](#97dafa559620d720a718b8756436b45d)
    - [godoc](#d320d9ee424223b08261a39e229971dd)
        - [本机的Go文档Web服务](#556ff244b88890038cf38b8e5ac21e8a)

[](...menuend)


<h2 id="0b1ba65761a964f84e21fae57faa0496"></h2>

# go doc 和 godoc

<h2 id="97dafa559620d720a718b8756436b45d"></h2>

## go doc


标记名称 | 标记描述
--- | --- 
-c | 加入此标记后会使go doc命令区分参数中字母的大小写。默认情况下，命令是大小写不敏感的。
-cmd | 加入此标记后会使go doc命令同时打印出main包中的可导出的程序实体（其名称的首字母大写）的文档。默认情况下，这部分文档是不会被打印出来的。
-u | 加入此标记后会使go doc命令同时打印出不可导出的程序实体（其名称的首字母小写）的文档。默认情况下，这部分文档是不会被打印出来的。


- go doc命令可以后跟一个或两个参数
    - 当然，也可以不附加任务参数
    - 如果不附加参数，那么go doc命令会试图打印出当前目录所代表的代码包的文档及其中的包级程序实体的列表。
- 例如 , 在项目代码包所在目录中src运行go doc命令的话 

```
$ go doc -cmd
package main // import "."

var Chan = make(chan int, 10)
var ChanAU = make(chan int, 1)
var HOST = flag.String("host", "localhost", "")
var PORT = flag.Int("port", 5757, "")
func GetIntranetIp() string
func SetActiveUser(key int)
func Summary()
type Message struct{ ... }
type User struct{ ... }
    func NewUser(id int) *User
```

- 如果你需要指定代码包或程序实体，那么就需要在go doc命令后附上参数了

```
$ go doc -cmd -u User
type User struct {
    Id    int
    St    string
    Ended bool
}

func NewUser(id int) *User
func (u *User) CreateRoom(c *gosocketio.Client)
func (u *User) EnterRoom(c *gosocketio.Client)
func (u *User) Play(c *gosocketio.Client)
func (u *User) QueryRoom(c *gosocketio.Client)
func (u *User) QueryRoom2(c *gosocketio.Client)
func (u *User) Start()
func (u *User) StartGame(c *gosocketio.Client)
func (u *User) Update(c *gosocketio.Client)

$ go doc -cmd -u User.Start
func (u *User) Start()
```

<h2 id="d320d9ee424223b08261a39e229971dd"></h2>

## godoc

- 查看代码包fmt的文档

```
$ godoc fmt

$ godoc fmt Printf
func Printf(format string, a ...interface{}) (n int, err error)
    Printf formats according to a format specifier and writes to standard
    output. It returns the number of bytes written and any write error
    encountered.

$ godoc fmt Printf Println
```

- 如果想看到它们的源码

```
$ godoc -src fmt Printf
// Printf formats according to a format specifier and writes to standard output.
// It returns the number of bytes written and any write error encountered.
func Printf(format string, a ...interface{}) (n int, err error) {
    return Fprintf(os.Stdout, format, a...)
}
```

- 如果我们想在查看代码包net中的结构体类型Listener的文档的同时查看关于它的示例代码，那么我们只需要在执行命令时加入标记-ex。
    - 使用方法如下：

```
$ godoc -ex net/http FileServer
```

- 在实际的Go语言环境中，我们可能会遇到一个命令源码文件所产生的可执行文件与代码包重名的情况。
- 比如，这里介绍的标准命令go和官方代码包go。现在我们要明确的告诉godoc命令要查看可执行文件go的文档，我们需要在名称前加入cmd/前缀：

```
$ godoc cmd/go
```

- 一般情况下，godoc命令会去Go语言根目录和环境变量GOPATH包含的工作区目录中查找代码包。我们可以通过加入标记-goroot来制定一个Go语言根目录。

```
$ godoc -goroot="/usr/local/go" fmt
```

<h2 id="556ff244b88890038cf38b8e5ac21e8a"></h2>

###  本机的Go文档Web服务

```
$ godoc -http=:9090 -index
```

- `-index`标记开启搜索索引。这个索引会在服务器启动时创建并维护。如果不加入此标记，那么无论在Web页面还是命令行终端中都是无法进行查询操作的。

- 如果我们在本机用godoc命令启动了Go文档Web服务器，且IP地址为192.168.1.4、端口为9090，那么我们就可以在另一个命令行终端甚至另一台能够与本机联通的计算机中通过如下命令进行查询了。查询命令如下：

```
$ godoc -q -server="192.168.1.4:9090" Listener
```

- 命令的最后为要查询的内容，可以是任何你想搜索的字符串，而不仅限于代码包、函数或者结构体的名称。
    - 标记-q开启了远程查询的功能。 
    - 如果不指明远程查询服务器的地址，那么该命令会自行将地址“:6060”和“golang.org”作为远程查询服务器的地址。
