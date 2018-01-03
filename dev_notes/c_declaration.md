...menustart

 - [C Declaration](#4d4d41296119a89b97e6c8d1d2b12d61)
     - [How a Declaration Is Formed](#0e8496ac4e183c0a93f348bea3eb755a)
     - [how to combine variables in structs and unions](#b6883b80c1162c486c5fc1f7cd01ef57)
         - [A Word About structs](#f630d4bf06506c3ab082d636b29f7243)

...menuend


<h2 id="4d4d41296119a89b97e6c8d1d2b12d61"></h2>

# C Declaration 

<h2 id="0e8496ac4e183c0a93f348bea3eb755a"></h2>

## How a Declaration Is Formed

 - declaration vs declarator
    - A declarator is the part of a declaration that gives an object, type, or function its **name** and indicates whether an object is a **pointer, or array**. 

 - roughly, a declarator is 
    - the identifier 
    - and any pointers, 
    - function brackets, 
    - or array indica-tions that go along with it
 - Here we also group any initializer here for convenience.


Name in C  |  Looks in C | How Many
--- | --- | ---
pointer |  `* const  volatile`  |  0 or many
·  |  const,volatile 可选,位置可交换  |  ·
direct_declarator | `identifier`    | exactly one
· | `identifier[optional_size]...`    | ·
· | `identifier(args...)`    | ·
· | `(declarator)`    | ·
initializer | `= initial_value` | 0 or 1


 - A declaration is made up of the parts shown below
    - not all combinations are valid
 - A declaration gives the basic underlying type of the variable and any initial value.



Name in C  |  Looks in C | How Many
--- | --- | ---
type-specifier |  `void char short int long` |  at least one type-specifier 
· | `signed unsigned`    | (not all combinations are valid)
· | `float double`  | ·
· | `struct_specifier` | ·
· | `enum_specifier` | ·
· | `union_specifier` | ·
storage-class |  `extern static register` |  ·
· | `auto typedef` | ·
type-qualifier |  `const volitile` |  ·
 ---- | ------------------ | ----
declarator |  *definition above* | exactly one
more declarators | `, declarator`  |  0 , or more
semi-colon | `;` | 1 


 - remember there are restrictions on legal declarations. You can't have any of these:
    - a function can't return a function, so you'll never see `foo()()`
    - a function can't return an array, so you'll never see `foo()[]`
    - an array can't hold a function, so you'll never see `foo[]()`
 - You can have any of these:
    - a function returning a pointer to a function is allowed:  `int (* fun())()`
    - a function returning a pointer to an array is allowed:  `int (* foo())[]`
    - an array holding pointers to functions is allowed: `int (*foo[])()`
    - an array can hold other arrays, so you'll frequently see `int foo[][]`

<h2 id="b6883b80c1162c486c5fc1f7cd01ef57"></h2>

## how to combine variables in structs and unions

and also look at enums.

<h2 id="f630d4bf06506c3ab082d636b29f7243"></h2>

### A Word About structs

 - The syntax for structs is easy to remember: 
    - the usual way to group stuff together in C is to put it in braces: `{ stuff... }` 
    - The keyword struct goes at the front so the compiler can distinguish it from a block:
    - `struct {stuff... }`
 - The stuff in a struct can be any other data declarations: 
    - individual data items, arrays, other structs, pointers, and so on.  
 - We can follow a struct definition by some variable names, declaring variables of this struct type, for example:
    - `struct {stuff... } plum, pomegranate, pear;`
 - **"structure tag"**: 
    - The only other point to watch is that we can write an optional "structure tag" after the keyword
    - `struct fruit_tag {stuff... } plum, pomegranate, pear;` 
 - tag 的好处是，以后的声明可以 不再带 `{stuff...}`
    - `struct fruit_tag` can now be used as a shorthand for `struct {stuff... }` , in future declarations.
 - A struct thus has the general form:

```c
struct optional_tag {
type_1 identifier_1;
type_2 identifier_2;
...
type_N identifier_N;
} optional_variable_definitions;
```

```c
struct date_tag { short dd,mm,yy; } my_birthday, xmas;
struct date_tag easter, groundhog_day;
```

 - variables `my_birthday, xmas, easter, and groundhog_day` all have the identical type. 

 - Structs can also have bit fields, unnamed fields, and word-aligned fields.
    - This is commonly used for "programming right down to the silicon," and you'll see it in systems programs. 
    - A bit field must have a type of int, unsigned int, or signed int (or a qualified version of one of these)

```c
/* process ID info */
struct pid_tag {
unsigned int inactive :1;
unsigned int          :1; /* 1 bit of padding */
unsigned int refcount :6;
unsigned int          :0; /* pad to next word boundary
*/
short pid_id;
struct pid_tag *link;
};
```

 - Finally there are two parameter passing issues associated with structs.
 - when paramters are passed to a called function , parameters are passed in registers (for speed) where possible (并不是只会压进栈). 
    - Be aware that an int "i" may well be passed in a completely different manner to a struct "s" whose only member is an int.
    - Assuming an int parameter is typically passed in a register, you may find that structs are instead passed on the stack.
 - The second point to note is that by putting an array inside a struct like this:

```c
/* array inside a struct */
struct s_tag { int a[100]; };
```

 - you can now treat the array as a **first-class type**.
    - You can copy the entire array with an assignment statement, 
    - pass it to a function by value,
    - and make it the return type of a function.
        - 数组终于可以做这些事情了。。。

```c
struct s_tag { int a[100]; };
struct s_tag orange, lime, lemon;
struct s_tag twofold (struct s_tag s) {
    int j;
    for (j=0;j<100;j++) s.a[j] *= 2;
    return s;
}
main() {
    int i;
    for (i=0;i<100;i++) lime.a[i] = 1;
    lemon = twofold(lime);
    orange = lemon; /* assigns entire struct */
}
```

 - Let's finish up by showing one way to make a struct contain a pointer to its own type, as needed for lists, trees, and many dynamic data structures.

```c
/* struct that points to the next struct */
struct node_tag { int datum;
                  struct node_tag *next;
                };
struct node_tag a,b;
a.next = &b;       /* example link-up */
a.next->next=NULL;
```

### struct 内存对齐

 - 公式1:前面的地址必须是后面的地址 整数倍,不是就补齐
 - 公式2:整个Struct的地址必须是最大字节的整数倍

```c
Struct E1 { 
    int a;char b; char c
} e1;
```
 
 - Example above
    - 第一地址肯定存放a是4Byte地址
    - 第二地址,b要1Byte的地址 -- 公式一登场:    4 == 1\*N (N等于正整数)  答"是"!
        - 地址现在为5Byte
    - 下一个c要1Byte的地址同上 , 
        - 地址现在为6Byte  
    - 公式二登场，在这个E1中最大的字节是4，而我们的地址字节是6，4的整数倍不是6，所以，要加2Byte（总地址），So，整个字节为8!
 - CAUTION:
    - 每个特定平台上的编译器都有自己的默认“对齐系数”。可以通过预编译命令#pragma pack(n) 

---

 - 背书式：
    - 各成员变量存放的起始地址 相对于结构的起始地址 的偏移量必须为该变量的类型所占用的字节数的倍数
    - 各成员变量在存放的时候根据在结构中出现的顺序依次申请空间
        - 同时按照上面的对齐方式调整位置 空缺的字节自动填充
    - 同时为了确保结构的大小 为结构的字节边界数(即该结构中占用最大的空间的类型的字节数) 的倍数

### A Word About unions

 - **union** have a similar appearance to structs, but the memory layout has one crucial difference
    - Instead of each member being stored after the end of the previous one, **all the members have an offset of zero**.
    - The storage for the individual members is thus overlaid: only one member at a time can be stored there.
 - The good news is that unions have exactly the same general appearance as structs, but with the keyword `struct` replaced by `union`.
 - A union has the general form:

```c
union optional_tag {
    type_1 identifier_1;
    type_2 identifier_2;
      ...
    type_N identifier_N;
} optional_variable_definitions;
```

 - Unions can also be used
    1. for one interpretation of two different pieces of data 
    2. two different interpretations of the same data

```c
// case 1
union secondary_characteristics {
    char has_fur;
    short num_of_legs_in_excess_of_4;
};
struct creature {
    char has_backbone;
    union secondary_characteristics form;
};
```

```c
// case 2
union bits32_tag {
    int whole;                       /* one 32-bit value */
    struct {char c0,c1,c2,c3;} byte; /* four 8-bit bytes */
} value;
```

 - This union allows a programmer to extract the full 32-bit value, or the individual byte fields `value.byte.c0`, and so on.
 - There are other ways to accomplish this, but the union does it without the need for extra assignments or type casting.

### A Word About enums

 - Enums (enumerated types) are simply a way of associating a series of names with a series of integer values. 
 - In a weakly typed language like C, they provide very little that can't be done with a `#define`

```c
enum optional_tag {stuff... } optional_variable_definitions;
```

 - `The stuff...` in this case is a list of identifiers, possibly with integer values assigned to them. 

```c
enum sizes { small=7, medium, large=10, humungous };
```

 - The integer values start at zero by default. 
    - If you assign a value in the list, the next value is +1 greater, and so on. 
 - There is one advantage to enums:
    - unlike `#defined` names which are typically discarded during compilation, 
    - enum names usually persist through to the debugger, and can be used while debugging your code.
 
---

## The Precedence Rule

 - We have now reviewed the building blocks of declarations. 
 - The precedence rule for understanding C declarations is the one that the language lawyers like best.
 - It's high on brevity, but very low on intuition.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/c_precedence_rule_for_declaration.png .png)



