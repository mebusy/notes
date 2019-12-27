...menustart

 - [C# 基础知识系列](#fa94b771653cde1bb927b44cc47760b0)
     - [1. 委托](#e9bafc1ba9b32792e1a6767a5b90cb0b)
     - [2. 事件](#9ab5d9239891b8704b41fa25af9ff4d8)
     - [3 泛型](#ef9dd3e4da51997ee0ad36f4bffd7a0f)
     - [4 可空类型](#a01b9a5c094abd236183cf580055b070)
     - [5 匿名方法](#7cc9ae5fc50b276b255e933a6b62bb0c)
     - [6 迭代器](#9ba1d6d409520c3031f7588729aed101)
         - [迭代器的执行过程](#bad9144ea9ca4fa82d4aa0ea5e3ea0d0)
         - [迭代器的延迟计算](#2fcaf0c251bb72907daf4d7ec989dc37)
     - [7 C# 3.0 特性](#20cc25147a42e4fa9b50e9c8a84a1859)
         - [一. 自动实现的属性](#bce7c98a3eeee6f5f37a6ccef15810f5)
         - [隐式类型](#5671331782e45072798988ee21cf67f1)
         - [三. 对象集合初始化](#3282d55660474313ceab1e9ca18de830)
         - [四.匿名类型](#3c3d86c7bda7588d827ce5891115a72e)
     - [8 Lambda 表达式](#f3aeee35464ad2b54ddfd5b9e8e33ee0)
     - [9 扩展方法](#dc48b917570b210718938a1f427c98a0)
         - [在空引用上调用方法](#e188ac55989f14949d223a0b08aeb3ca)
     - [10 Linq](#a40e46bb8e65367d364d3b42e7f5bb27)
     - [11 动态类型](#bb4d84cc46c04279eb1b35c1fd7bb100)
     - [12 Async / Await](#74b653574acf96f0e265db4a4ef07db3)
     - [13 解析C# 中参数传递](#b43b5bcd822c27a24551fe2faa29f9d8)
     - [14 typeof  和 GetType 区别](#50d5399284c57a1336886a51b855596d)
     - [14 浅拷贝 和 深拷贝](#7c920bcef1735cc77408e22a57e3c919)
     - [c# 高级数据结构](#d554ea9229b0d95487b99114d79a0dfe)

...menuend


<h2 id="fa94b771653cde1bb927b44cc47760b0"></h2>


# C# 基础知识系列

<h2 id="e9bafc1ba9b32792e1a6767a5b90cb0b"></h2>


## 1. 委托

 - c# 中的委托相当于c++中的函数指针
 - 区别在于 委托诗歌类，委托是面向对象，类型安全的，是引用类型
 - 使用委托需要如下步骤
    1. 定义: `delegate void Mydelegate(type1 para1 , type2 para2);`
    2. 声明： `Mydelegate d;`
    3. 实例化: `d=new Mydelegate( obj.InstanceMethod );`
        - 把一个方法传递给委托构造器
    4. 作为参数传递给方法 `someMethond( d );`
 - someMethond 定义
 
```c#
private void someMethod( Mydelegate mydelegate ) {
    mydelegate( arg1, arg2 );
}
``` 

 - 调用单个方法,不通过 步骤2，3 实例化委托， 直接传入 和delegate相同类型的函数 也可
 - 实例化委托的强大在于 委托链

```c#
DelegateTest d1 = new ...
DelegateTest d2 = new ...
DelegateTest d3 = new ...
DelegateTest delegatechain = null;
delegatechain += d1 ;
delegatechain += d2 ;
delegatechain += d3 ;
```

<h2 id="9ab5d9239891b8704b41fa25af9ff4d8"></h2>


## 2. 事件

 - 事件 其实是委托， 确切的说 事件就是委托链
    - 定义事件 除了使用 event 关键字外， 还用刀了一个委托类型
    - event关键字，限定了外界对委托变量只能使用+=或-=操作符，对于其他的比如赋值或者调用都会被视为错误
 - 可以把事件 理解为 委托的一个属性，属性的返回值就是一个 委托类型。定义一个事件时，编译器会把它转化为 3段代码
    1. 一个被初始化为 null 私有委托字段 xxxEventHandle
        - 对一个委托列表的 头部引用
    2. `add_xxxEvent( xxxEventHandle value )`
        - 线程安全的方式， 添加一个委托
    2. `remove_xxxEvent( xxxEventHandle value )`
 - 实现观察者模式
    - 观察对象内部 维护 event
        - event 不需要实例化？？
        - event notify的时候，处于线程安全的考虑，将 event 的引用复制到一个临时变量中去
        - `xxxEventHandle temp = Interlocked.CompareExchange... `
        - `if (temp!=null) temp(this, objdata ) `
    - 外部观察者  通过该 event 进行注册

<h2 id="ef9dd3e4da51997ee0ad36f4bffd7a0f"></h2>


## 3 泛型

```c#
public static class ListPool<T> { 
    ...
}

...

public static void Swap<T> (ref T a, ref T b) {
    ...
}
```

 - 泛型类型 和 泛型参数
    - 泛型类型 有两种 表现方式： 泛型类型 和 泛型方法
    - 泛型参数 必须放在 `< >` 里面，用都好分隔
        - 如果 没有为 类型参数 提供 类型实参， 此时我们就声明了一个 未绑定的 泛型类型
        - 如果指定了 类型实参， 则称为 已构造类型
 - 类型推断
    - 泛型方法 支持类型推断
    - `// GenericMethodTest<int>(ref n1, ref n2);`
    - `GenericMethodTest (ref n1, ref n2);`
 - 类型约束
    - `where T : IComparable`

<h2 id="a01b9a5c094abd236183cf580055b070"></h2>


## 4 可空类型

 - 值类型， 是包括 null的值类型
 - `Nullable<T>`


<h2 id="7cc9ae5fc50b276b255e933a6b62bb0c"></h2>


## 5 匿名方法

 - C#为委托提供一种机制，可以为委托定义匿名方法
 - 匿名方法建立在 委托基础上
    - 委托是方法的包装， 匿名方法也是方法， 所以委托也可以包装匿名方法

```c#
MyDelagate my = delegate(string param)  
{  
    string str2 = " 匿名方法内部 ";  
    return param + str1 + str2;  
};  
```

 - C#3.0之后匿名方法可以使用λ表达式来进行定义

```c#
MyDelagate my = param => param + str1 + str2;
```

<h2 id="9ba1d6d409520c3031f7588729aed101"></h2>


## 6 迭代器
 
 - 实现一个迭代器， 必须实现 IEnumeralbe 接口

```c#
public class Friends: IEnumeralbe {
    ...
    //索引器
    public Friend this[int index] {
        get { return friendarray[index]; }    
    }
    // c# 2.0 简化迭代器的实现
    public IEnumerator GetEnumerator() {
        for (int index=0; index < friendarray.Length; index++>) {
            yield return friendarray[index] ;   
        }    
    }
}
```

<h2 id="bad9144ea9ca4fa82d4aa0ea5e3ea0d0"></h2>


### 迭代器的执行过程

 - `foreach (Friend f in friendcollection ) `
    1. foreach 开始
    2. friendcollection  调用 GetEnumerator() 获取迭代器
    3. in 调用 IEnumerator.MoveNext()
    4. Friend f 访问 IEnumerator.Current

<h2 id="2fcaf0c251bb72907daf4d7ec989dc37"></h2>


### 迭代器的延迟计算

从迭代器的执行过程中，可以知道 迭代器是延迟计算的。

```c#
public static IEnumerable<int> WithIterator() {
    for (int i=0;i<5;i++) {
        Console.WriteLine( ""+i ) ;
        if (i>1) 
            yield return i;   
    }    
}
```

调用 `WithIterator()`  不会产生任何输出，对编译器而言，就是实例化了一个 `<WithIterator>d_0` 对象。

`<WithIterator>d_0` 对 是编译器看到 方法中包含 yield return 语句 生成的一个迭代器类。


<h2 id="20cc25147a42e4fa9b50e9c8a84a1859"></h2>


## 7 C# 3.0 特性

<h2 id="bce7c98a3eeee6f5f37a6ccef15810f5"></h2>


### 一. 自动实现的属性

当类中定义的属性不需要一些额外的验证时，此时我们可以使用自动实现的属性，使代码更简洁。

C# 3 之前一般这样定义属性

```c#
private string _name ;
public string Name {
    get { return _name; }
    set { _name = value; }
}
```

C# 3之后又自动实现的属性之后，对于不需要额外验证的属性，可以使用 自动属性，不再需要额外定义一个私有字段了。 编译器编译时 会 自动创建一个私有的匿名字段。

```c#
public string Name { get ; set ; }
```

<h2 id="5671331782e45072798988ee21cf67f1"></h2>


### 隐式类型

 - `var intarray = new[]{ 1,3,4 }`
 - 必须是局部变量，不能是字段
 - 变量声明时 必须被初始化
 - 不能初始化为 一个方法组， 也不能为一个 匿名函数
 - 不能初始化为 null

<h2 id="3282d55660474313ceab1e9ca18de830"></h2>


### 三. 对象集合初始化

**3.1 对象初始化**

 - 不需要再考虑定义参数不同的构造函数来应付不同情况的初始化了

3.0前

```c#
Person person1 = new Person();
person1.Name = "bob" ;
person1.Age = 1 ; 
```

3.0后

```c#
# 构造函数 + 初始化
Person person4 = new Person() { Name="Bob", Age=1 };
```

**3.2 集合初始化**

3.0 前

```c#
List<string> names = new List<string>();
names.Add( "Bob1" ) ;
names.Add( "Bob2" ) ;
names.Add( "Bob3" ) ;
```

3.0 后

```c#
var names = new List<string> {
    "Bob1" , "Bob2" , "Bob3"     
};
```

<h2 id="3c3d86c7bda7588d827ce5891115a72e"></h2>


### 四.匿名类型

```c#
var person1 = new { Name="Bob", Age=1 };
```

<h2 id="f3aeee35464ad2b54ddfd5b9e8e33ee0"></h2>


## 8 Lambda 表达式

```c#
// c# 2 匿名方法 创建委托
// 不需要额外定义回调方法
Func<string,int> delegate=delegate(string text) {return text.Length};

// c# 3 lambda 表达式
Func<string,int> delegate= (string text) => text.Length ; 

// 可以省略参数类型， 再简化为
Func<string,int> delegate= (text) => text.Length ; 

// 如果lambda表达式只需要一个参数，并且那个参数可以隐式制定类型时
// 此时可以把 ()也省略
Func<string,int> delegate= text => text.Length ; 
```

---

C# 编译器还可以把 lambda表达式 转换成 表达式树。

<h2 id="dc48b917570b210718938a1f427c98a0"></h2>


## 9 扩展方法

 - 为现有的类 扩展添加方法
    - 没有扩展方法之前，只能通过继承，这样会带来若干问题：1.需要重现实现所有抽象方法，2.密封类无法被继承

```c#
public static class StreamExten {
    // 定义扩展方法
    public static void CopyToNewStream( this Stream inputsteam , Stream outputstream) {
        byte[] buffer = new byte[8192];
        int read;
        while ((read = inputstream.Read(buffer, 0, buffer.Length)) > 0) {
            outputstream.Write(buffer, 0, read);
        }
    }
}   

// 调用扩展方法
// responsestream.CopyToNewStream(output);
```

上面程序中为Stream类型扩展了一个CopyToNewStream()的方法.并不是所有方法都可以作为扩展方法来使用的。扩展方法必须具备下面的规则：

 - 它必须在一个非嵌套、非泛型的静态类中
 - 它至少要有一个参数
 - 第一个参数必须加上this关键字作为前缀（第一个参数类型也称为扩展类型，即指方法对这个类型进行扩展）
 - 第一个参数不能用其他任何修饰符（如不能使用ref out等修饰符）
 - 第一个参数的类型不能是指针类型


<h2 id="e188ac55989f14949d223a0b08aeb3ca"></h2>


### 在空引用上调用方法

 - 在C#中，在空引用上调用实例方法是会引发NullReferenceException异常
 - 但是可以在空引用上调用扩展方法

```c#
public static class NullExten {
    public static bool isNull(this string str) {
        return str == null;
    }
}
```
 
 - 因为并不是真在空引用中调用了方法，而是调用了静态类NullExten的静态方法IsNull,此时只是把空引用s传递给该方法作为传入参数
 - 由此可见 扩展方法只是一个语法糖

<h2 id="a40e46bb8e65367d364d3b42e7f5bb27"></h2>


## 10 Linq

 - C# 3.0 最重要的特性
 - Linq: Language Integrated Query  语言集成查询
 - Linq 主要包含4个组件
    - Linq to Objects: 可以查询 `IEnumberable` 或 `IEnumberable<T>` 集合
    - Linq to XML: 可以查询和操作 XML文件，比Xpath操作XML 更加方便
    - Linq to Dataset: 可以查询Dataset对象中的数据， 对数据增删改查
    - Linq to SQL: 可以查询关系数据库的数据
 - Linq 使操作这些数据源更简单
 - 因为效率和GC 问题， 移动端慎用

<h2 id="bb4d84cc46c04279eb1b35c1fd7bb100"></h2>


## 11 动态类型

 - introduced in c# 4.0
 - 略

<h2 id="74b653574acf96f0e265db4a4ef07db3"></h2>


## 12 Async / Await

 - C# 5.0 

<h2 id="b43b5bcd822c27a24551fe2faa29f9d8"></h2>


## 13 解析C# 中参数传递

 - C# 中的参数传递，根据 参数类型 可以分为4类
    - 值类型参数 的按值传递
    - 引用类型参数的 按值传递
    - 值类型参数的 按引用传递
    - 引用类型参数的 按引用传递 
 - 通过使用 ref/out 关键字 来实现参数的 按引用传递； 需要注意以下亮点
    - 方法的定义和调用 都必须同时 显示的使用 ref / out
    - CLR 允许通过 ref / out 参数实现方法重载
        - `private static void Add( string str ) `
        - `private static void Add( ref string str ) `
 - 按 引用传递 可以解决 由于值 传递时 引用副本而不引向引用本身的问题
    - 此时传递的是 引用的引用 ， 而不是 引用的拷贝

<h2 id="50d5399284c57a1336886a51b855596d"></h2>


## 14 typeof  和 GetType 区别

 - typeof 是 运算符， GetType 是方法
 - typeof 获得类型的 System.Type 对象， GetType() 获得当前实例的 Type
 - GetType() 是基类 System.Object 的方法， 是有 建立了一个实例之后 才能够调用
 - typeof 的参数 只能是 int, string, class, 自定义类型， 不能为具体实例


```c#
object m1 = 1 ;
Console.WriteLine( typeof(ValueType).IsValueType ) ; // False
Console.WriteLine( m1.GetType().IsValueType ) ;      // True
```

<h2 id="7c920bcef1735cc77408e22a57e3c919"></h2>


## 14 浅拷贝 和 深拷贝

 - 浅拷贝实现很简单， System.Object 的 MemberwiseClone 方法 就可以实现 浅拷贝
 - 深拷贝的实现方式有: 反射, 反序列化，和 表达式树
    - 反射实现方式， 对于互相引用的对象 会出现 StackOverFlow的错误
    - 建议使用 反序列化 方式

<h2 id="d554ea9229b0d95487b99114d79a0dfe"></h2>


## c# 高级数据结构

 - System.Collections.Generic
    - `Dictionary<TKey, TValue>`
    - `HashSet<T>`
    - `LinkedList<T>`  双重链列
    - `List<T>`
    - `Queue<T>`
    - `Stack<T>`
    - `SortedDictionary<TKey, TValue>`  根据键进行排序的键/值对的集合
    - `SortedList<TKey, TValue>`
    - `SortedSet<T>`
    - `SynchronizedCollection<T>`
    - `SynchronizedKeyedCollection<K, T>`
    - `SynchronizedReadOnlyCollection<T>`
 - 集合和同步（线程安全）
    - 默认情况下，System.Collections 和相关命名空间中的类不是线程安全的。
    - 多个阅读器可以放心地读取集合；但是，对集合的任何修改都会对访问该集合的所有线程（包括阅读器线程）产生不确定的结果。
    - 使用以下任意方法可令 System.Collections 类成为线程安全的：
        - 使用 Synchronized 方法创建线程安全包装，并通过该包装以独占方式访问集合。
        - 如果该类不具有 Synchronized 方法，则从该类派生并使用 SyncRoot 属性实现 Synchronized 方法。
        - 在访问该集合时对 SyncRoot 属性使用锁定机制，例如 C# 中的 lock 语句  
    - 在实现 Synchronized 方法时，派生类必须重写 IsReadOnly 属性才能返回正确的值。
    - Array 类不含 Synchronized 方法，并且，尽管它有一个 SyncRoot 属性，但该类不能从其派生。因此，只有通过锁定机制才可令数组是线程安全的
    - 泛型集合类不包含同步成员；不过，有些泛型类（如 Collection、Dictionary 和 List）显式实现从非泛型 ICollection 接口继承的同步成员。


