[](...menustart)

- [2 – Basic Concepts](#5eadd983edcd006d1d7c77cacf304d01)
    - [2.1 – Values and Types](#3053af0cf7ed59b35a33bbac43f61692)
    - [2.2 – Environments and the Global Environment](#450e6c4e856637db95564a960db61fa8)
    - [2.3 – Error Handling](#9ab14e9a3a5b6b4651d3f0f1d6fc3e3e)
    - [2.4 – Metatables and Metamethods](#e8338b957cfebba82f352026ce533a5c)
    - [2.5 – Garbage Collection](#b96bb9af2b541d8cd6752cb8b514f397)
        - [2.5.2 – Weak Tables](#2ee0667701209dc7ecf0ae9d309a8a95)
    - [2.6 – Coroutines](#a7629f76b2e07fbf8dbca4a41d7114c0)
- [3 – The Language](#ac362547474c89f8b882abc7326b6ebe)
- [4 – The Application Program Interface](#dfc1f4912c18595eb03abb457f9d5460)
    - [4.1 - The Stack](#ede5deeca64781b0f5637625fef01c6b)
- [5 – The Auxiliary Library](#da0790e25c16fe93480803e7aa545a29)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [Lua 多线程](#63f5a0b12473a9e9f903d98796a34e28)
    - [GC](#7359c3eb5c57547295a76ac1bf775b29)

[](...menuend)


[Lua 5.3 manual](http://www.lua.org/manual/5.3/manual.html#4)

<h2 id="5eadd983edcd006d1d7c77cacf304d01"></h2>

# 2 – Basic Concepts

<h2 id="3053af0cf7ed59b35a33bbac43f61692"></h2>

## 2.1 – Values and Types

- Variables do not have types; only values do.
- All values in Lua are first-class values.
- Eight basic types in Lua: 
    - nil, boolean, number, string, function, userdata, thread, and table. 
    - Both nil and false make a condition false; any other value makes it true. 
    - Strings can contain any 8-bit value, including embedded zeros ('\0'). 
    - Both functions written in Lua and functions written in C , are represented by the type *function*.
    - *userdata* can store arbitrary C data in Lua variables. A userdata value represents a block of raw memory. 
        - full userdata
            - an object with a block of memory managed by Lua
        - light userdata
            - simply a C pointer value.
        - By using metatables, the programmer can define operations for full userdata values.
    - *thread* represents independent threads of execution and it is used to implement coroutines. 
        - Lua supports coroutines on all systems, even those that do not support threads natively.
        - VM manages the lifetime of *threads*. 
    - *table* implements associative arrays
        - arrays that can have as indices not only numbers, but any Lua value except **nil** and **NaN**.
        - Any key with value nil is not considered part of the table.
        - `a.name` as syntactic sugar for `a["name"]`
- *Tables*, *functions*, *threads*, and (full) *userdata* values are objects: 
    - variables do not actually contain these values, only references to them.

<h2 id="450e6c4e856637db95564a960db61fa8"></h2>

## 2.2 – Environments and the Global Environment

- Any reference to a **free** name (that is, a name not bound to any declaration) var is syntactically translated to `_ENV.var`.
- Moreover, every chunk is compiled in the scope of an external local variable named `_ENV` .
    - so `_ENV` itself is never a free name in a chunk.
- Lua keeps a distinguished environment called the global environment.
    - In Lua, the global variable `_G` is initialized with this same value.
- When Lua loads a chunk, the default value for its `_ENV` upvalue is the global environment 
    - Therefore, by default, free names in Lua code refer to entries in the global environment 
        - (they are also called global variables).
    - You can use load (or loadfile) to load a chunk with a different environment. 
        - (In C, you have to load the chunk and then change the value of its first upvalue.) 

[5.2 ENV](https://blog.codingnow.com/2011/12/lua_52_env.html)

- Lua 5.2 去掉了5.1的 module, get/setfenv()

```lua
    -- Lua 5.1
    function foobar()
    setfenv(1, {})
     -- code here
    end
    -- Lua 5.2
    function foobar()
    local _ENV = {}
    -- code here
    end
```

<h2 id="9ab14e9a3a5b6b4651d3f0f1d6fc3e3e"></h2>

## 2.3 – Error Handling

- Lua code can explicitly generate an error by calling the *error* function. 
- If you need to catch errors in Lua, you can use *pcall* or *xpcall* to call a given function in protected mode.

```lua
function __G__TRACKBACK__(msg)
    --被 socket.try 保护的，msg是一个table
    if type(msg) == "table" then
        return
    end
    
    CCLOG(debug.traceback())
    CCLOG("LUA ERROR: " .. tostring(msg) .. "\n")
end
xpcall(main,  __G__TRACKBACK__)
```

<h2 id="e8338b957cfebba82f352026ce533a5c"></h2>

## 2.4 – Metatables and Metamethods

- Every value in Lua can have a metatable.
- This metatable is an ordinary Lua table that defines the behavior of the original value under certain special operations.
- You can change the behavior of operations over a value by setting specific fields in its metatable. 
    - For instance, when a non-numeric value is the operand of an addition, Lua checks for a function in the field "`__add`" of the value's metatable. 
    - If it finds one, Lua calls this function to perform the addition.
- To query a metatable of any value:
    - 
    ```lua
    getmetatable
    ```
- Lua queries metamethods in metatables using a raw access, to retrieve the metamethod for event ev in object o :
    - 
    ```lua
    rawget(getmetatable(o) or {}, "__ev")
    ```
- To replace the metatable of **tables** :
    - 
    ```lua
    setmetatable
    ```
    - You cannot change the metatable of other types from Lua code (except by using the debug library; you should use the C API for that.
- Tables and full userdata have individual metatables (although multiple tables and userdata can share their metatables). 
- Values of all other types share one single metatable per type;
    - that is, there is one single metatable for all numbers, one for all strings, etc. 


<h2 id="b96bb9af2b541d8cd6752cb8b514f397"></h2>

## 2.5 – Garbage Collection

- GC uses two numbers to control its garbage-collection cycles, both use percentage points as units. ( 100 means  an internal value of 1 )
    1. *garbage-collector pause* : how long the collector waits before starting a new cycle.
        - Values smaller than 100 mean the collector will not wait to start a new cycle. 
        - A value of 200 means that the collector waits for the total memory in use to double before starting a new cycle.
    2. *garbage-collector step multiplier* : controls the relative speed of the collector relative to memory allocation.
        - Larger values make the collector more aggressive but also increase the size of each incremental step. 
        - You should not use values smaller than 100, because they make the collector too slow and can result in the collector never finishing a cycle. 
        - The default is 200, which means that the collector runs at "twice" the speed of memory allocation.
- You can change these numbers by calling *lua_gc* in C or collectgarbage in Lua. 
    - i.e.
    ```lua
    collectgarbage("setpause", 150 )
    collectgarbage("setstepmul", 200)
    ```

<h2 id="2ee0667701209dc7ecf0ae9d309a8a95"></h2>

### 2.5.2 – Weak Tables

- A weak table is a table whose elements are weak references. 
- A weak reference is ignored by the garbage collector. 
    - In other words, if the only references to an object are weak references, then the garbage collector will collect that object.
- A weak table can have weak keys, weak values, or both. 
    - A table with weak values allows the collection of its values, but prevents the collection of its keys.
    - In any case, if either the key or the value is collected, the whole pair is removed from the table.
- The weakness of a table is controlled by the `__mode` field of its metatable. If the `__mode` field is a string containing the character 'k', the keys in the table are weak. If `__mode` contains 'v', the values in the table are weak.

- A table with weak keys and strong values is also called an **ephemeron** table. 
    - In an ephemeron table, a value is considered reachable only if its key is reachable. 
    - In particular, if the only reference to a key comes through its value, the pair is removed.

<h2 id="a7629f76b2e07fbf8dbca4a41d7114c0"></h2>

## 2.6 – Coroutines

- A coroutine only suspends its execution by explicitly calling a yield function.
- You create a coroutine by calling `coroutine.create`. 
    - Its sole argument is a function that is the main function of the coroutine.
    - The *create* function only creates a new coroutine and returns a handle to it (an object of type thread); it does not start the coroutine.
- You execute a coroutine by calling `coroutine.resume`. 
    - When you first call *resume*, passing the thread returned by *create*, and the arguments of main function.
- A coroutine can terminate its execution in two ways:
    1. normally, when its main function returns.  *resume* will return true,  plus any values returned by the main function.
    2. and abnormally, if there is an unprotected error. *resume* will return false, plus an error object. 
- A coroutine yields by calling `coroutine.yield`.        
    - When a coroutine yields, the corresponding coroutine.resume returns immediately, even if the yield happens inside nested function calls.
    - In the case of a yield, *resume* also returns true, plus any values passed to `coroutine.yield`.
- The next time you resume the same coroutine, it continues its execution from the point where it yielded
    - *yield* returning any extra arguments passed to coroutine.resume.
- That is, *yield* is used to **communicate between "main" thread and the coroutine**. 

```lua
     function foo (a)
       print("foo", a)
       return coroutine.yield(2*a)
     end
     
     co = coroutine.create(function (a,b)
           print("co-body", a, b)
           local r = foo(a+1)
           print("co-body", r)
           local r, s = coroutine.yield(a+b, a-b)
           print("co-body", r, s)
           return b, "end"
     end)
     
     print("main", coroutine.resume(co, 1, 10))
     print("main", coroutine.resume(co, "r"))
     print("main", coroutine.resume(co, "x", "y"))
     print("main", coroutine.resume(co, "x", "y"))

-- output
     co-body 1       10
     foo     2
     main    true    4
     co-body r
     main    true    11      -9
     co-body x       y
     main    true    10      end
     main    false   cannot resume dead coroutine
```


<h2 id="ac362547474c89f8b882abc7326b6ebe"></h2>

# 3 – The Language

- "A" = '\x41' = '\65'
- 
```lua
(print or io.write)('done')
```
- A block can be explicitly delimited to produce a single statement:
    - 
    ```lua
    stat ::= do block end
    ```
- `i, a[i] = i+1, 20`
- Control Structures
    - 
    ```lua
    while exp do block end
    repeat block until exp
    if exp then block {elseif exp then block} [else block] end
    ```

- For 
    - `for Name = exp , limit [, step] do block end`
    - `for ... in` 
    ```bash
    > for k,v in ipairs(t) do                                                                                                                     print(k,v)                                                                                                                            end
    1   a
    2   b
    3   c
    ```
- Both function calls and vararg expressions can result in multiple values. 
    - If an expression is used as the last (or the only) element , then no adjustment is made.
    - In all other contexts, Lua adjusts the result list to one element.
    - 
    ```lua
    g(f(), x)          -- f() is adjusted to 1 result
    g(x, f())          -- g gets x plus all results from f()
    a,b,c = f(), x     -- f() is adjusted to 1 result (c gets nil)
    a,b = ...          -- a gets the first vararg argument, b gets
                        -- the second (both a and b can get nil if there
                        -- is no corresponding vararg argument)
    a,b,c = x, f()     -- f() is adjusted to 2 results
    a,b,c = f()        -- f() is adjusted to 3 results
    return f()         -- returns all results from f()
    return ...         -- returns all received vararg arguments
    return x,y,f()     -- returns x, y, and all results from f()
    {f()}              -- creates a list with all results from f()
    {...}              -- creates a list with all vararg arguments
    {f(), nil}         -- f() is adjusted to 1 result
    ```
    - Any expression enclosed in parentheses always results in only one value. 
        - Thus, `(f(x,y,z))` is always a single value
- Arithmetic Operators
    - 
    ```lua
    //: integer division
    %: modulo
    ^: exponentiation
    ```
- Bitwise Operators
    - 
    ```lua
    &: bitwise AND
    |: bitwise OR
    ~: bitwise exclusive OR
    >>: right shift
    <<: left shift
    ~: unary bitwise NOT
    ```
    - Caution: it is logical shift, not arithmetic shift !!!
- Coercions and Conversions
    - Bitwise operators always convert float operands to integers.
    - Exponentiation and float division always convert integer operands to floats.
    - 
    ```bash
    > "a" .. 2
    a2
    ```
    - 
    ```bash
    > "4" / 2   -- 2.0
    ```
- The computation of the length of a table has a guaranteed worst time of **O(log n)**.
- Only concatenation ('..') and exponentiation ('^') operators are right associative. 
    - `2^2^3 = 256.0`
- Function Calls
    - Gramma
        - `functioncall ::=  prefixexp args | prefixexp ‘:’ Name args `
        - `args ::=  ‘(’ [explist] ‘)’ | tableconstructor | LiteralString `
    - `v:name(args)` is syntactic sugar for `v.name(v,args)`, except that v is evaluated only once.
    - `f{fields}` is syntactic sugar for `f({fields})`
    - `f'string' (or f"string" or f[[string]])` is syntactic sugar for `f('string')`


<h2 id="dfc1f4912c18595eb03abb457f9d5460"></h2>

# 4 – The Application Program Interface

- All API functions and related types and constants are declared in the header file `lua.h`.
- Each Lua state has one or more threads, which correspond to independent, cooperative lines of execution. 
    - The type lua_State refers to a thread. 
    - (Indirectly, through the thread, it also refers to the Lua state associated to the thread.)
    - 从实现角度来看，一个 thread 就是一个Lua与C交互的栈，每个栈包含函数调用链和数据栈，还有独立的调试钩子和错误息。
    - 当调用Lua C API中的大多数函数时，这些函数都是在特定的栈（或线程）上.
- A pointer to a thread must be passed as the first argument to every function in the library, except to `lua_newstate`.
    - which creates a Lua state from scratch and returns a pointer to the **main** thread in the new state.
    - This is also global state of the VM. 
        - You can create a new thread within the global state,  by `lua_State *lua_newthread (lua_State *L)`
        - and the coroutine is a thread as well.
        - 
        ```
        > co = coroutine.create(function() print("hi") end)
        > print(co)
        thread: 0x7f8be6601288
        ```
- 
```
             global_State
                  |
    -----------------------------
    |             |             |
 lua_State    lua_State    lua_State
```

<h2 id="ede5deeca64781b0f5637625fef01c6b"></h2>

## 4.1 - The Stack 

- Lua uses a virtual stack to pass values to and from C. 
    - Each element in this stack represents a Lua value (nil, number, string, etc.). 
- Whenever Lua calls C, the called function gets a new stack,
    - which is independent of previous stacks and of stacks of C functions that are still active.
    - This stack initially contains any arguments to the C function and it is where the C function can store temporary Lua values and must push its results to be returned to the caller.
- For convenience, most query operations in the API do not follow a strict stack discipline. 
    - Instead, they can refer to any element in the stack by using an index: 
        - A positive index represents an absolute stack position (starting at 1); 
        - a negative index represents an offset relative to the top of the stack.
    - More specifically, if the stack has n elements, then 
        - index 1 , -n represents the first element.
        - and index n , -1 represents the last element; 







<h2 id="da0790e25c16fe93480803e7aa545a29"></h2>

# 5 – The Auxiliary Library

- The auxiliary library provides several convenient functions to interface C with Lua.
- All functions and types from the auxiliary library are defined in header file `lauxlib.h` and have a prefix `luaL_`.





<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

# Misc

<h2 id="63f5a0b12473a9e9f903d98796a34e28"></h2>

## Lua 多线程

- 单个 Lua 虚拟机只能工作在一个线程下，如果你需要在同一个进程中让 Lua 并行处理一些事务，必须为每个线程部署独立的 Lua 虚拟机。
- lua 多线程库
    - [Lanes](https://github.com/LuaLanes/lanes) , 有 deep userdata 可以在不同线程间共享。
    - [Effil](https://github.com/effil/effil) , 使用effil.table 去模拟 table 并让多个虚拟机可以共享数据。

<h2 id="7359c3eb5c57547295a76ac1bf775b29"></h2>

## GC

- [Lua GC](https://www.lua.org/wshop18/Ierusalimschy.pdf)








