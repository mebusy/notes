
# go doc 和 godoc

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

 - 还想看到它们的源码

```
$ godoc -src fmt Printf
// Printf formats according to a format specifier and writes to standard output.
// It returns the number of bytes written and any write error encountered.
func Printf(format string, a ...interface{}) (n int, err error) {
    return Fprintf(os.Stdout, format, a...)
}
```


https://www.ctolib.com/docs-go-command-tutorial-c-0-5.html




