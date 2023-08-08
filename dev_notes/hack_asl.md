

https://github.com/daliansky/OC-little/blob/master/10-PTSWAK%E7%BB%BC%E5%90%88%E6%89%A9%E5%B1%95%E8%A1%A5%E4%B8%81

https://ocbook.tlhub.cn/00-%E6%80%BB%E8%BF%B0/00-1-ASL%E8%AF%AD%E6%B3%95%E5%9F%BA%E7%A1%80/

# ASL 语言基础

## 简述

- ACPI(Advanced Configuration & Power Interface)
    - ACPI 是一系列的接口，这个接口包含了很多表格
- DSDT (Differentiated System Description Table Fields) 
- SSDT (Secondary System Description Table Fields) 
    - DSDT 和 SSDT 既是其中的表格同时也是一些接口。
- ACPI 的一个特色就是专有一门语言来编写 ACPI 的那些表格。它就是 ASL (ACPI Source Language) 
    - ASL 经过编译器编译后，就变成了 AML (ACPI Machine Language)，

## ASL 准则

1. 变量命名不超过 4 个字符，且不能以数字开头。
2. Scope 形成作用域。 ACPI 有且仅有一个根作用域, 所以 DSDT 都以 (for example)
    ```asl
    DefinitionBlock ("", "DSDT", 2, "DELL  ", "CBX3   ", 0x01072009)
    {
    ```
    - 开始，同时以
    ```asl
    }
    ```
    - 结束, 这个就是根作用域.
3. 以 _ 字符开头的函数和变量都是系统保留的
    - 这就是为什么反编译某些AML以后得到的 ASL 出现 `_T_X`，重新编译的时候会出现警告。
4. Method 定义函数，函数可以定义在 Device 下或者 Scope 下。 
5. 根作用域 `\` 下有 `\_GPE`，`\_PR`，`\_SB`，`\_SI`，`\_TZ` 五个作用域。
    - `\_GPE`--- ACPI 事件处理
    - `\_PR` --- 处理器
        - CPU
    - `\_SB` --- 所有的设备和总线
        - Device (PCI0)
    - `\_SI` --- 系统指示灯
    - `\_TZ` --- 热区，用于读取某些温度
6. Device (xxxx) 也可看做是一个作用域，里面包含对设备的各种描述
    - 例如：_ADR、_CID、_UID、_DSM、_STA 等对设备的说明和状态控制
7. 符号 `\` 引用根作用域，`^` 引用上级作用域，同理 `^^` 为 上上级作用域
8. ACPI 为了更好理解，规范后来使用了新的 ASL 语法 ASL 2.0 (也叫做 ASL+), 新语法引入了与 C 语言等同的 `+-*/=, <<, >> 和逻辑判断 ==, !=` 等等
9. 函数最多可以传递 7 个参数，在函数里用 Arg0~Arg6 表示，不可以自定义。
10. 函数最多可以用 8 个局部变量，用 Local0~Local7，
    - **不用定义，但是需要初始化才能使用**，也就是一定要有一次赋值操作。



## ASL 常用的数据类型

ASL | 类型 | 定义变量
--- | --- | ---
Integer | 整数 | `Name (TEST, 0)`
String | 字符串 | `Name (MSTR,"ASL")`
Event | 事件 | 
Buffer | 数组 | `CreateWordField (FFFF, 0x05, GGGG)`
Package | 对象集合 | Name (_PRW, Package (0x02)<br> {<br> &nbsp;&nbsp; 0x0D, 0x03<br> })

## ASL 赋值方法

```asl
// b <= a
Store (a,b) /* 传统 ASL */
b = a      /*   ASL+  */
// example
Store (0, Local0)
Local0 = 0
```

## ASL 函数的定义

```asl
Method (MADD, 2, Serialized)
{
    Local0 = Arg0
    Local1 = Arg1
    Local0 += Local1
    Return (Local0)
}
```

- 2 是指定参数数量, 可选
- Serialized 是定义可序列化的函数, 可选
    - 当函数声明为 Serialized，内存中仅能存在一个实例。
    - 这个有点类似于多线程同步的概念， 两个地方同时调用 同一个函数，需要等待第一个调用结束，再开始执行第2个调用。
- 返回值 可选


## ACPI 预定义函数

- _OSI (Operating System Interfaces 操作系统接口)
    ```asl
    If (_OSI ("Darwin")) /* 判断当前的系统是不是 macOS */
    ```
- _STA (Status 状态)
    - _STA 方法的返回值最多包含 5 个 Bit，每个 Bit 的含义如下
        ```
        Bit[0] 设备是否存在
        Bit[1] 设备是否被启用且可以解码其资源
        Bit[2] 设备是否在 UI 中显示
        Bit[3] 设备是否正常工作
        Bit[4] 设备是否存在电池
        ```
    - ⚠️   _STA 分为两种，请勿与 PowerResource 的 _STA 混淆！！！
        - PowerResource 的 _STA 只有两个返回值 One 和 Zero
- _CRS (Current Resource Settings 当前资源设置)
    - _CRS 函数返回的是一个 Buffer，在触摸设备中会返回触摸设备所需的 GPIO Pin，APIC Pin 等等，可以控制设备的中断模式。


## ASL 流程控制

### If

```asl
   If (_OSI ("Darwin"))
   {
       OSYS = 0x2710
   }
   ElseIf (_OSI ("Linux"))
   {
       OSYS = 0x03E8
   }
   Else
   {
       OSYS = 0x07D0
   }
```

### Switch

```asl
   Switch (Arg2)
   {
       Case (1) /* 条件 1 */
       {
           If (Arg1 == 1)
           {
               Return (1)
           }
           BreakPoint /* 条件判断不符合，退出 */
       }
       Case (2) /* 条件 2 */
       {
           ...
           Return (2)
       }
       Default /* 如果都不符合，则 */
       {
           BreakPoint
       }
   }
```

### While 以及暂停 Stall

```asl
Local0 = 10
While (Local0 >= 0x00)
{
    Local0--
    Stall (32)  /* 暂停 32μs */
}
```


### For ( like C, Java)

```asl
for (local0 = 0, local0 < 8, local0++)
{
    ...
}
```

## 外部引用 External

```asl
External (  路径和名称  ,  引用类型)
```

example

```asl
// Name (_PRW, Package (0x02) { 0x0D, 0x03 })
External (_SB.PCI0.RP01._PRW, PkgObj)
```

## ASL 存在性判断语句 CondRefOf

判断所有类型 Object 的存在与否

```asl
    If (CondRefOf (\_SB.PCI0.I2C0.XSCN)) { ... }
```


# SSDT 补丁(.aml)加载顺序

- 通常情况下，我们的 SSDT 补丁的对象是机器的 ACPI (DSDT 或者其他 SSDT 文件)，这些原始的 ACPI 加载的时间早于我们的 SSDT 补丁。
    - 因此，我们的 SSDT 补丁在 Add 列表中 **没有顺序要求**。
- 有这样一种情况，当我们在一个 SSDT 补丁里定义了一个 Device 设备，又在另一个 SSDT 补丁里通过 Scope 引用这个 Device,
    - 那么，这两个补丁在 Add 列表中 **有顺序要求**。

- 补丁1：SSDT-XXXX-1.aml
    ```asl
    External (_SB.PCI0.LPCB, DeviceObj)
    Scope (_SB.PCI0.LPCB)
    {
        Device (XXXX)
        {
            Name (_HID, EisaId ("ABC1111"))
        }
    }    
    ```
- 补丁2：SSDT-XXXX-2.aml
    ```asl
    External (_SB.PCI0.LPCB.XXXX, DeviceObj)
    Scope (_SB.PCI0.LPCB.XXXX)
    {
          Method (YYYY, 0, NotSerialized)
         {
             /* do nothing */
         }
    }
    ```


