[](...menustart)

- [Golang Cheat Sheet](#8a43cf282b42bb608cfc7b417630c252)
- [1. ioutil](#0f3fc1e61949b5e304c5e47cddde9aab)
    - [NopCloser](#07e928d917a09673de8b88e9df0dda27)
    - [ReadAll](#9dd97e40c8f60288a89643e7bdbec41c)
    - [ReadDir](#9d897432b2883ab5520f3e8b4dcb29e6)
    - [ReadFile / WriteFile](#123f94d76ec25eba686b6bebaa54ff9f)
    - [TempDir / TempFile](#7645f5ea033085c383ae54528cdec0b5)
    - [Discard 变量](#e9ae82f4cad73ed0a458c5e2e4018d13)
- [3. 数据结构与算法](#b6b537259c4bc39d52d0e50e90219176)
    - [3.1 sort](#86907f07f3b152838a699a5843bb293a)
        - [Reverse()](#4cf2ed87db154d9a8850aeeeb5403a54)
        - [Search()](#eda22ee94ca4659a94510e901fc6b03a)
        - [sort包已经支持的内部数据类型排序](#98e48d4176430b53d9240ea51e7a71bd)
    - [3.2 index / suffixarray](#7c88f2e737c7a8fa9891112b9ff52018)
    - [3.3 container -- heap . list , ring](#10531adb8e2afff548686dde7f5d96df)
        - [3.3.1 heap](#4071d55221a7cf2dacd8cb0fd763b139)
        - [3.3.2 list 链表](#6f453dc352c6268d59baec4cf55a4c15)
        - [3.3.3 ring](#62237f8c1de14c5db300e1678e4afeec)

[](...menuend)


<h2 id="8a43cf282b42bb608cfc7b417630c252"></h2>

# Golang Cheat Sheet

<h2 id="0f3fc1e61949b5e304c5e47cddde9aab"></h2>

# 1. ioutil 

<h2 id="07e928d917a09673de8b88e9df0dda27"></h2>

## NopCloser

- 包装一个io.Reader，返回一个io.ReadCloser，而相应的Close方法啥也不做，只是返回nil

```go
rc, ok := body.(io.ReadCloser)
if !ok && body != nil {
    rc = ioutil.NopCloser(body)
}
```

<h2 id="9dd97e40c8f60288a89643e7bdbec41c"></h2>

## ReadAll

- 一次性读取io.Reader中的数

```go
func ReadAll(r io.Reader) ([]byte, error)
``` 

<h2 id="9d897432b2883ab5520f3e8b4dcb29e6"></h2>

## ReadDir 

- 读取目录并返回排好序的文件和子目录名（[]os.FileInfo)

<h2 id="123f94d76ec25eba686b6bebaa54ff9f"></h2>

## ReadFile / WriteFile

```go
func WriteFile(filename string, data []byte, perm os.FileMode) error
```

- WriteFile 当文件不存在时会创建一个（文件权限由perm指定

<h2 id="7645f5ea033085c383ae54528cdec0b5"></h2>

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

<h2 id="e9ae82f4cad73ed0a458c5e2e4018d13"></h2>

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

<h2 id="b6b537259c4bc39d52d0e50e90219176"></h2>

# 3. 数据结构与算法

<h2 id="86907f07f3b152838a699a5843bb293a"></h2>

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

<h2 id="4cf2ed87db154d9a8850aeeeb5403a54"></h2>

### Reverse()

- Reverse()返回的一个sort.Interface接口类型

<h2 id="eda22ee94ca4659a94510e901fc6b03a"></h2>

### Search()

- 使用“二分查找”算法
- 数组必须已经升序排序

<h2 id="98e48d4176430b53d9240ea51e7a71bd"></h2>

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

<h2 id="7c88f2e737c7a8fa9891112b9ff52018"></h2>

## 3.2 index / suffixarray

<h2 id="10531adb8e2afff548686dde7f5d96df"></h2>

## 3.3 container -- heap . list , ring 

<h2 id="4071d55221a7cf2dacd8cb0fd763b139"></h2>

### 3.3.1 heap 

```go
type Interface interface {
    sort.Interface
    Push(x interface{}) // add x as element Len()
    Pop() interface{}   // remove and return element Len() - 1.
}
```

package doc中的example:

```go
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

//============
h := &IntHeap{2, 1, 5}
heap.Init(h)
heap.Push(h, 3)
heap.Pop(h)
```

<h2 id="6f453dc352c6268d59baec4cf55a4c15"></h2>

### 3.3.2 list 链表

- 链表就是一个有prev和next指针的数组了。
- 它维护两个type，(注意，这里不是interface)

```go
type Element struct {
    next, prev *Element  // 上一个元素和下一个元素
    list *List  // 元素所在链表
    Value interface{}  // 元素
}

type List struct {
    root Element  // 链表的根元素
    len  int      // 链表的长度
}
```

基本使用是先创建list，然后往list中插入值，list就内部创建一个Element，并内部设置好Element的next,prev等


```go
    list := list.New()
    list.PushBack(1)
    list.PushBack(2)
```

<h2 id="62237f8c1de14c5db300e1678e4afeec"></h2>

### 3.3.3 ring

- ring 不需要像list一样保持list和element两个结构，只需要保持一个结构就行

```go
type Ring struct {
    next, prev *Ring
    Value      interface{}
}
```

- 初始化环的时候，需要定义好环的大小，然后对环的每个元素进行赋值
- 环还提供一个Do方法，能便利一遍环，对每个元素执行一个function

```go
    ring := ring.New(3)

    for i := 1; i <= 3; i++ {
        ring.Value = i
        ring = ring.Next()
    }

    // 计算1+2+3
    s := 0
    ring.Do(func(p interface{}){
        s += p.(int)
    })
    fmt.Println("sum is", s)
```


