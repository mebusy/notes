...menustart

- [C# 基础知识系列](#fa94b771653cde1bb927b44cc47760b0)
    - [9 扩展方法](#dc48b917570b210718938a1f427c98a0)
    - [12 Async / Await](#74b653574acf96f0e265db4a4ef07db3)
    - [13 解析C# 中参数传递](#b43b5bcd822c27a24551fe2faa29f9d8)
    - [14 typeof  和 GetType 区别](#50d5399284c57a1336886a51b855596d)
    - [14 浅拷贝 和 深拷贝](#7c920bcef1735cc77408e22a57e3c919)
    - [c# 高级数据结构](#d554ea9229b0d95487b99114d79a0dfe)

...menuend


<h2 id="fa94b771653cde1bb927b44cc47760b0"></h2>


# C# 基础知识系列


<h2 id="dc48b917570b210718938a1f427c98a0"></h2>


## 9 扩展方法

- 为现有的类 扩展添加方法
    - 没有扩展方法之前，只能通过继承，这样会带来若干问题：1.需要重现实现所有抽象方法，2.密封类无法被继承

```cpp#
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


```cpp#
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


