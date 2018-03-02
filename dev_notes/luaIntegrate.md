...menustart

 - [Integrate LUA](#ce184863f05a7ff711ae5677ccb11667)
     - [1. include lua header files](#cd27a050b3dd39ef6a61a72c21f8fcb7)
     - [2. create your lua state class](#4e920d09e03dfa78fd32050f46acef83)
     - [3. print problem](#ccc897386af8da03fafcfabcc025c998)
     - [4. add lua search path](#67479c3ef43bc4a573dec363b3707a90)
     - [5. tolua++](#625a412884d68edbd61698c43079471b)
         - [template](#66f6181bcb4cff4cd38fbc804a036db6)
         - [name space](#3fec93f66682ce9c63af27dec7b911a2)
         - [enumerate](#2a45a91d039693c9fb96a16030a13c5e)
         - [struct](#0f8d6fb56fe6cdf55ad0114ec5b51dbb)
     - [6. c++ reigster lua callback](#5b77d3c94d428927df167f348def0026)

...menuend


<h2 id="ce184863f05a7ff711ae5677ccb11667"></h2>

# Integrate LUA

<h2 id="cd27a050b3dd39ef6a61a72c21f8fcb7"></h2>

## 1. include lua header files

```c
extern "C" {
#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"
}
```

<h2 id="4e920d09e03dfa78fd32050f46acef83"></h2>

## 2. create your lua state class

```c
    LuaState::LuaState(void) {
    }


    LuaState::~LuaState(void) {
    }

    void LuaState::Init() {
        L = lua_open();
        // load the libs
        luaL_openlibs(L);
    }
```

<h2 id="ccc897386af8da03fafcfabcc025c998"></h2>

## 3. print problem 

 - sometime lua print function will not output to your engine's console 

```c
namespace {
int lua_print(lua_State * luastate) {
    int nargs = lua_gettop(luastate);

    std::string t;
    for (int i=1; i <= nargs; i++)
    {
        if (lua_istable(luastate, i))
            t += "table";
        else if (lua_isnone(luastate, i))
            t += "none";
        else if (lua_isnil(luastate, i))
            t += "nil";
        else if (lua_isboolean(luastate, i))
        {
            if (lua_toboolean(luastate, i) != 0)
                t += "true";
            else
                t += "false";
        }
        else if (lua_isfunction(luastate, i))
            t += "function";
        else if (lua_islightuserdata(luastate, i))
            t += "lightuserdata";
        else if (lua_isthread(luastate, i))
            t += "thread";
        else
        {
            const char * str = lua_tostring(luastate, i);
            if (str)
                t += lua_tostring(luastate, i);
            else
                t += lua_typename(luastate, lua_type(luastate, i));
        }
        if (i!=nargs)
            t += "\t";
    }
    // HERE , replace with your engine's log function
    CCLOG("[LUA-print] %s", t.c_str());

    return 0;
}
}  // namespace {
```

 - register lua_print 

```c
    // Register our version of the global "print" function
    const luaL_reg global_functions [] = {
        {"print", lua_print},
        {NULL, NULL}
    };
    luaL_register(m_state, "_G", global_functions);
```

<h2 id="67479c3ef43bc4a573dec363b3707a90"></h2>

## 4. add lua search path

```
void LuaState::addSearchPath(const char* path)
{
    lua_getglobal(m_state, "package");                                  /* L: package */
    lua_getfield(m_state, -1, "path");                /* get package.path, L: package path */
    const char* cur_path =  lua_tostring(m_state, -1);
    lua_pushfstring(m_state, "%s;%s/?.lua", cur_path, path);            /* L: package path newpath */
    lua_setfield(m_state, -3, "path");          /* package.path = newpath, L: package path */
    lua_pop(m_state, 2);                                                /* L: - */
}
```

<h2 id="625a412884d68edbd61698c43079471b"></h2>

## 5. tolua++

 - tolua
 - tolua_fix.h/c
 - after exporting files via tolua,  you should add the generated function `TOLUA_API int  tolua_onyx_plus_open (lua_State* tolua_S);` to your Lua_state init function.

 - tolua 传递 userdata 总是使用 指针，然后做相应的必须转换  `*ptr`

<h2 id="66f6181bcb4cff4cd38fbc804a036db6"></h2>

### template

 https://www8.cs.umu.se/kurser/TDBD12/VT04/lab/lua/tolua++.html

 - 使用 TEMPLATE_BIND 实例化多个 binding
 - 目前只支持 class level   ， 
    - function level not support yet

<h2 id="3fec93f66682ce9c63af27dec7b911a2"></h2>

### name space 

 - call by lua
```lua
namespace.classname:functionname( ... )
```

<h2 id="2a45a91d039693c9fb96a16030a13c5e"></h2>

### enumerate

 - pkg 文件 函数声明 有用到 enum的情况，需要把 enum的定义也放入 pkg 文件

<h2 id="0f8d6fb56fe6cdf55ad0114ec5b51dbb"></h2>

### struct 

 - C++ 
    - only classes (and structs) with a constructor will have a 'new()' method
    - You can add the constructor on your pkg (even if it's not actually implemented).
 - C
    - the only solution I can think of is to have a function that creates a new struct and returns it

<h2 id="5b77d3c94d428927df167f348def0026"></h2>

## 6. c++ reigster lua callback

 - 使用 cocos2dx 的 tolua-fix 方法
 - 在 .pkg 文件中， 使用 `LUA_FUCNTION` ( 实质是一个 int 类型 ) 声明一个handle 
    - `void registerScriptHandler(int handler);`
 - tolua-fix 会 处理成一个 lua function ref
    - `LUA_FUNCTION handler = (  toluafix_ref_function(tolua_S,2,0));`
 - 在 c++ 代码中 保存这个handle， 然后，使用 executeFunctionByHandler 来执行这个函数
 - lua 方面的相关调用

```lua
    local shs = ScriptHandlerSample()
    shs:registerScriptHandler( function()  print("lua callback");  end )
```

## 7. lua / Java

https://segmentfault.com/a/1190000004252394
