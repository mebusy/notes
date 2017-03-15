...menustart

 - [Swift](#ae832e9b5bda2699db45f3fa6aa8c556)
 - [Swift 初见](#615cb80db0ce206ba8b503e8cfd8dc29)
	 - [简单值](#784a1eecef63971124e06e00d4234693)
	 - [控制流](#22151ac437197cee5637f0a298a3647b)

...menuend


<h2 id="ae832e9b5bda2699db45f3fa6aa8c556"></h2>

# Swift 

<h2 id="615cb80db0ce206ba8b503e8cfd8dc29"></h2>

# Swift 初见

<h2 id="784a1eecef63971124e06e00d4234693"></h2>

## 简单值

```
var myVariable = 42   // var 变量 , 自动判断类型
let myConstant = 42   // let 常量
let explicitDouble: Double = 70   // 声明类型
```

```
let apples = 3
let oranges = 5
let appleSummary = "I have \(apples) apples."
let fruitSummary = "I have \(apples + oranges) pieces of fruit." 
```

使用方括号[]来创建数组和字典，并使用下标或者键（key）来访问元素。

```
var shoppingList = ["catfish", "water", "tulips", "blue paint"]
shoppingList[1] = "bottle of water"
var occupations = [ "Malcolm": "Captain", "Kaylee": "Mechanic", ]
occupations["Jayne"] = "Public Relations" 
```

创建一个空数组或者字典

```
let emptyArray = String[]()
let emptyDictionary = Dictionary<String, Float>() 
```

如果类型信息可以被推断出来，你可以用[]和[:]来创建空数组和空字典

```
shoppingList = []  
```


<h2 id="22151ac437197cee5637f0a298a3647b"></h2>

## 控制流

 - if, switch
 - for-in、for、while、 do-while

```
let individualScores = [75, 43, 103, 87, 12] 
for score in individualScores {
	...
}
```