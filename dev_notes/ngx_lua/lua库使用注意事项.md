...menustart

- [ngx_lua 中 使用Lua库注意事项](#d0e7b64b0f812084fef447a088ff7709)

...menuend


<h2 id="d0e7b64b0f812084fef447a088ff7709"></h2>


## ngx_lua 中 使用Lua库注意事项

- time、date 和 difftime 
     - 在 OpenResty 的世界里，不推荐使用这里的标准时间函数，因为这些函数通常会引发不止一个昂贵的系统调用，同时无法为 LuaJIT JIT 编译，对性能造成较大影响。
     - 推荐使用 ngx_lua 模块提供的带缓存的时间接口，如 ngx.today, ngx.time, ngx.utctime, ngx.localtime, ngx.now, ngx.http_time， 以及 ngx.cookie_time 等。

- I/O 库文件操作
     - 这些文件 I/O 操作，在 OpenResty 的上下文中对事件循环是会产生阻塞效应。 
     - OpenResty 比较擅长的是高并发网络处理，在这个环境中，任何文件的操作，都将阻塞其他并行执行的请求。
     - 实际中的应用，在 OpenResty 项目中应尽可能 让 **网络处理部分**、**文件 I/0 操作部分** 相互独立，不要揉和在一起。