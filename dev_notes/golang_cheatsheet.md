
# Golang Cheat Sheet

# 1. ioutil 

## NopCloser

 - 包装一个io.Reader，返回一个io.ReadCloser，而相应的Close方法啥也不做，只是返回nil

```go
rc, ok := body.(io.ReadCloser)
if !ok && body != nil {
    rc = ioutil.NopCloser(body)
}
```

## ReadAll

 - 一次性读取io.Reader中的数

```go
func ReadAll(r io.Reader) ([]byte, error)
``` 

## ReadDir 

 - 读取目录并返回排好序的文件和子目录名（[]os.FileInfo)

## ReadFile / WriteFile

```go
func WriteFile(filename string, data []byte, perm os.FileMode) error
```

 - WriteFile 当文件不存在时会创建一个（文件权限由perm指定

## TempDir / TempFile

 - 操作系统中一般都会提供临时目录，比如linux下的/tmp目录（通过os.TempDir()可以获取到)
 - 有时候，我们自己需要创建临时目录
    - 比如 通过TempDir创建一个临时目录，用于存放编译过程的临时文件
    
```go
b.work, err = ioutil.TempDir("", "go-build")
f1, err := ioutil.TempFile("", "gofmt")
```

 - 第一个参数如果为空，表明在系统默认的临时目录（os.TempDir）中创建临时目录
 - 第二个参数指定临时目录名的前缀，该函数返回临时目录的路径

注意：创建者创建的临时文件和临时目录要负责删除这些临时目录和文件。如删除临时文件：

```go
defer func() {
    f.Close()
    os.Remove(f.Name())
}()
```

## Discard 变量

 - Discard 对应的类型（type devNull int）实现了io.Writer接口
 - 同时，为了优化io.Copy到Discard，避免不必要的工作，实现了io.ReaderFrom接口。

devNull 在实现io.Writer接口时，只是简单的返回

```go
func (devNull) Write(p []byte) (int, error) {
    return len(p), nil
}
```

而ReadFrom的实现是读取内容到一个buf中，最大也就8192字节，其他的会丢弃（当然，这个也不会读取）。

---

# 3. 数据结构与算法

## 3.1 sort

 - sort.Interface

```go
type Interface interface {
    // 获取数据集合元素个数
    Len() int
    // 如果i索引的数据小于j所以的数据，返回true，不会调用
    // 下面的Swap()，即数据升序排序。
    Less(i, j int) bool
    // 交换i和j索引的两个元素的位置
    Swap(i, j int)
}
```

### Reverse()

 - Reverse()返回的一个sort.Interface接口类型

### Search()

 - 使用“二分查找”算法
 - 数组必须已经升序排序

### sort包已经支持的内部数据类型排序

 - sort包原生支持[]int、[]float64和[]string三种内建数据类型切片的排序操作
    - 即不必我们自己实现相关的Len()、Less()和Swap()方法。

```go
func Ints(a []int) { Sort(IntSlice(a)) }
func IntsAreSorted(a []int) bool //IntsAreSorted 
func SearchInts(a []int, x int) int

func Float64s(a []float64)
func Float64sAreSorted(a []float64) bool
func SearchFloat64s(a []float64, x float64) int

func Strings(a []string)
func StringsAreSorted(a []string) bool
func SearchStrings(a []string, x string) int
```

## 3.2 index / suffixarray

## 3.3 container -- heap . list , ring 



