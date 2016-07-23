
# Node.js

# 1. 简介

### 1.4.3 单线程

 - 无法利用多核CPU
 - 错误会引起整个应用退出，健壮性值得考验
 - 大量计算占用CPU导致无法继续调用异步I/O. 

大计算量问题的解决方案：

 - google 的 Gears
 	- 启用一个完全独立的进程，将需要计算的程序发送到这个进程
 	- 在结果得出后，通过事件将结果传递回来
 	- 这个模型将计算量分发到其他进程上，以此来降低运算造成阻塞的几率
 - HTML5 定制的 Web Workers 标准
 	- google 放弃了 Gears, 全力支持Web Workers
 	- Web Workers 创建工作线程来进行计算，以解决 JavaScript 大计算阻塞UI渲染的问题
 	- 工作线程为了不阻塞主线程，通过消息传递的方式来传递运行结果, 这也使得工作线程不能访问到主线程中的UI。

Node 采用和 Web Workers 相同的思路来解决单线程中大计算量的问题: ***child_process***

子进程的出现，意味着Node 可以从容的应对单线程在健壮性和无法利用多核CPU访问的问题。

通过将计算分发到各个子进程，可以将大量计算分解到，然后再通过进程之间的事件消息来传递结果，这可以很好地保持应用模型的简单和低依赖。

通过 Master-Worker的管理方式，也可以很好的管理各个工作进程，以达到更高的健壮性。 详见第9章。


## 1.5 Node 应用场景

### 1.5.1 I/O 密集型

I/O密集的优势主要在于Node利用事件循环的处理能力，而不是启动每一个线程为每一个请求服务，资源占用极少。

### 1.5.2 是否不擅长CPU密集型业务

 - Node 可以通过编写 C/C++ 扩展的方式更高效的利用CPU, 将一些V8不能做到性能极致的地方通过C++实现。
 - 如果单线程的Node 不能满足需求，甚至用了C/C++ 扩展后还觉得不够，那么通过子进程的方式，将一部分Node进程当作常驻服务用于计算。
 	- 然后利用进程间的消息来传递结果，将计算与I/O 分离。
 - CPU 密集不可怕，如果合理调度是诀窍。


# 2. 模块机制


# 9. 玩转进程

从严格意义上而言，Node并非真正的单线程架构，Node自身还有一定的I/O线程存在，这些I/O线程存在。

这部分线程对于 开发者而言是透明的，只有C++扩展时才会关注到。

## 9.2 多进程架构

Node提供了 child_process模块，并且也提供了 child_process.fork()函数供我们实现进程的复制。

worker.js , 监听1000-2000之间的一个随机端口

```JavaScript
var http = require('http'); http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('Hello World\n');
}).listen(Math.round((1 + Math.random()) * 1000), '127.0.0.1');
```

master.js , 根据当前机器的CPU数量复制对应Node进程数

```JavaScript
var fork = require('child_process').fork; 
var cpus = require('os').cpus();
for (var i = 0; i < cpus.length; i++) {
	fork('./worker.js'); 
}
```

在 linux 系统下可以通过 ps aux | grep worker.js 查看到进程的数量

```bash
$ ps aux | grep worker.js
jacksontian 1475 0.0 0.0 2432768 600 s003 S+ 3:27AM 0:00.00 grep worker.js
jacksontian 1440 0.0 0.2 3022452 12680 s003 S 3:25AM 0:00.14 /usr/local/bin/node ./worker.js 
jacksontian 1439 0.0 0.2 3023476 12716 s003 S 3:25AM 0:00.14 /usr/local/bin/node ./worker.js 
jacksontian 1438 0.0 0.2 3022452 12704 s003 S 3:25AM 0:00.14 /usr/local/bin/node ./worker.js 
jacksontian 1437 0.0 0.2 3031668 12696 s003 S 3:25AM 0:00.15 /usr/local/bin/node ./worker.js
```



















