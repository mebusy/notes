
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








 
