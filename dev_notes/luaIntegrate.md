
# Integrate LUA

## 1. include lua header files

```c
extern "C" {
#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"
}
```

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

## 5. tolua++

 - tolua
 - tolua_fix.h/c


