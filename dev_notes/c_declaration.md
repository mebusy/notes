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



