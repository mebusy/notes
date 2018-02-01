...menustart

 - [Integrate LUA](#ce184863f05a7ff711ae5677ccb11667)
     - [1. include lua header files](#cd27a050b3dd39ef6a61a72c21f8fcb7)
     - [2. create your lua state class](#4e920d09e03dfa78fd32050f46acef83)
     - [3. print problem](#ccc897386af8da03fafcfabcc025c998)
     - [4. add lua search path](#67479c3ef43bc4a573dec363b3707a90)
     - [5. tolua++](#625a412884d68edbd61698c43079471b)

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



### template

 https://www8.cs.umu.se/kurser/TDBD12/VT04/lab/lua/tolua++.html

 - 使用 TEMPLATE_BIND 实例化多个 binding
 - 目前只支持 class level   ， 
    - function level not support yet

### name space 

 - call by lua
```lua
namespace.classname:functionname( ... )
```


