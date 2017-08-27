
# C# 基础知识系列

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

## 4 可空类型

 - 值类型， 是包括 null的值类型
 - `Nullable<T>`


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

### 迭代器的执行过程

 - `foreach (Friend f in friendcollection ) `
    1. foreach 开始
    2. friendcollection  调用 GetEnumerator() 获取迭代器
    3. in 调用 IEnumerator.MoveNext()
    4. Friend f 访问 IEnumerator.Current

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

调用 `WithIterator()`  不会产生任何输出，对编译器而言，就是实例化了一个 <WithIterator>d_0 对象。

<WithIterator>d_0 对 是编译器看到 方法中包含 yield return 语句 生成的一个迭代器类。


## 7 C# 3.0 特性

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

### 隐式类型

 - `var intarray = new[]{ 1,3,4 }`
 - 必须是局部变量，不能是字段
 - 变量声明时 必须被初始化
 - 不能初始化为 一个方法组， 也不能为一个 匿名函数
 - 不能初始化为 null

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

### 四.匿名类型

```c#
var person1 = new { Name="Bob", Age=1 };
```

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

## 10 Linq

 - C# 3.0 最重要的特性
 - Linq: Language Integrated Query  语言集成查询
 - Linq 主要包含4个组件
    - Linq to Objects: 可以查询 IEnumberable 或 IEnumberable<T> 集合
    - Linq to XML: 可以查询和操作 XML文件，比Xpath操作XML 更加方便
    - Linq to Dataset: 可以查询Dataset对象中的数据， 对数据增删改查
    - Linq to SQL: 可以查询关系数据库的数据
 - Linq 使操作这些数据源更简单






