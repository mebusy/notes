...menustart

 - [Swift Optional](#7e8b6c75b8623a87364201114150aa60)
     - [有什么用？](#b49228e7dbd38a64c71a528307f8e0a2)
     - [Optional](#ebb061953c0454b2c8ee7b0ac615ebcd)
         - [Optional Binding](#23b4bcc6b144fc01dc2c5b7b903d7eb1)
         - [隐式解包Optional](#37f80459b8739bb1626224a44c92b348)
         - [Optional Chaining](#c6b4dba958efc3f0aa8e21e2cb38d36a)
         - [??的使用](#6549f14d25cd64e26d5474d70e651360)

...menuend


<h2 id="7e8b6c75b8623a87364201114150aa60"></h2>


# Swift Optional 

<h2 id="b49228e7dbd38a64c71a528307f8e0a2"></h2>


## 有什么用？

```oc
-(void)setObject:(id)object forKey:(NSString *)key]
```

上面的函数，object 参数可以 传入 nil, 是会存在潜在的 crash 的。 你希望在编译的时候可以确保 a 不为 nil.

所以我们对语言添加了规则：「所有类型都不能为 nil 」。

但是的确会有变量处于「有值」和「 nil 」两种状态，它们怎么表示呢？解决方案就是引入了 Optional 类型，意为「可以为 nil 的类型」。

在此种机制下， 「AnyObject」 就代表一个非空的 Object 类型， 「AnyObject？」 代表可以为空的 object 类型。面那个函数直接翻译过来应该表述成这样：

```swift
func setObject(object:AnyObject?, forKey:String？)
```

因为不想让 object 为 nil，那么我们重新定义这个函数：

```swift
func setObject(object:AnyObject, forKey:String)
```

<h2 id="ebb061953c0454b2c8ee7b0ac615ebcd"></h2>


## Optional

Optional的实际类型是一个enum: 

```swift
enum Optional<T>: _Reflectable, NilLiteralConvertible {
    case None
    case Some(T)
    //...
}
```

```swift
var number： Int? = 32
var numbet: Optional<Int> = 32
```

一个Optional对象只存在两种状态：包含一个值，或者为空，我们都可以通过解包（unwrap）来获取.


<h2 id="23b4bcc6b144fc01dc2c5b7b903d7eb1"></h2>


### Optional Binding

```swift
var myString: String? = "Hello"
```

你可以通过==和!=，将Optional值和nil做比较来判断它是否包含一个值。

```swift
if myString != nil{
    print("myString contain a string value of \(myString!)")
}
```

在上面的语句里，当我们确定myString包含一个值时，我们通过在myString后面添加一个!来进行强制解包(forced unwrapping)，获取Optional内包含的值。

> 对 nil Optional  强制解包 会导致运行时错误。

Swift提供了一种更加方便的形式来完成这一过程，所谓的Optional Binding:

```swift
if let actualString = myString {
    print("myString contain a string value of \(actualString )")
} else {
    print("myString is nil")
}
```

<h2 id="37f80459b8739bb1626224a44c92b348"></h2>


### 隐式解包Optional

相较于普通的Optional值，在Swift中我们还有一种特殊的Optional，在对它的成员或者方法进行访问时，编译器会自动进行解包，被称为隐式解包。

Optional(ImplicitlyUnwrappedOptional),在声明时，通过在类型后面添加!来告诉编译器这是一个隐式解包Optional：

```swift
let possisbleString: String! 
...
let implicitString: String = possibleString //此处我们不需要!来对possibleString 进行显示解包
```

很显然，隐式解包的写法会带来一个潜在的危险，如果尝试访问一个为空的隐式解包Optional, 就会遇到一个runtime error。

引入隐式解包Optional 完全是 历史的锅...


<h2 id="c6b4dba958efc3f0aa8e21e2cb38d36a"></h2>


### Optional Chaining

Optional Chaining，如同名字一样，我们可以通过一个链来安全的访问一个Optional的属性或者方法。

```swift
if let isPNG = imagePaths["star"]?.hasSuffix(".png") {
    print("The star image is in PNG format")
}
```

 - 这里通过在`imagePath["star"]`后面添加?来获取star所对应的图片路径
   - 如果不存在就直接是nil,
   - 如果存在则返回对应的path，然后紧接着调用path的hasSuffix方法。

使用Optional Chaining可以让我们摆脱很多不必要的判断和取值，从而精简代码。


<h2 id="6549f14d25cd64e26d5474d70e651360"></h2>


### ??的使用

当Optional解包后的值为nil时，我们可以通过使用??来设置一个默认值。


```swift
let defaultImagePath = "/images/default.png"
let heartPath = imagePaths["heart"] ?? defaultImagePath
print(heartPath)
```

当然了，我们也可以将??链接起来，设置多重默认值：

```
let shapePath = imagePaths["cir"] ?? imagePaths["squ"] ?? defaultImagePath
```








