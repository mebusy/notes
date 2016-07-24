
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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_master_worker.png)


图9-1就是著名的Master-Worker模式，又称主从模式。图中的进程分为：主进程和工作进程。这是典型的分布式架构中用于并行处理业务的模式。

 - 主进程不负责具体的业务处理，而是负责调度或管理工作进程，它是趋向于稳定的。
 - 工作进程负责具体的业务处理

fork() 进程是昂贵的。好在Node通过事件驱动的方式在单线程上解决了大并发的问题，这里启动多个进程只是为了充分将CPU资源利用起来，而不是为了解决并发问题。


### 9.2.1 创建子进程

child_process 模块提供了4个方法用于创建子进程

 - spawn(): 启动一个子进程来执行命令
 - exec(): 启动一个子进程来执行命令，与spawn不同的是接口, 它有一个回调函数获知子进程的状况
 - execFile(): 启动一个子进程来执行文件
 - fork(): 与 spawn 类似, 不同点在于它创建Node的子进程只需指定要执行的JavaScript文件模块即可


`node worker.js` 这个命令分别用 上述4种方法实现:

```
var cp = require('child_process');

cp.spawn('node', ['worker.js']);
cp.exec('node worker.js', function (err, stdout, stderr) {
	// some code 
});
cp.execFile('worker.js', function (err, stdout, stderr) { 
	// some code
}); 
cp.fork('./worker.js');
```

类型 | 回调/异常 | 进程类型 | 执行类型 ｜ 可设置超时
--- | --- | --- | --- | --- | ---
spawn | x | 任意 | 命令 | x
exec | ✓ |  任意 | 命令 | ✓
execFile | ✓ |  任意 | 可执行文件 | ✓
fork | x | Node | JavaScript 文件 | x 

这里的可执行文件是指可以直接执行的文件，如果是 JavaScript 文件通过 execFile()执行, 它的首行内容必须添加如下代码：

```
 #!/usr/bin/env node
```

事实上，后面3种方法都是 spawn() 的延伸应用。

### 9.2.2 进程间通信

在前端浏览器中，JavaScript 主线程与UI渲染公用同一个线程，两者互相阻塞。

为了解决这个问题，HTML5 提出了 WebWorker API, 允许创建工作线程并在后台运行，使得一些阻塞较为严重的计算不影响主线程的UI渲染。

它的API 如下所示

```
var worker = new Worker('worker.js'); 
worker.onmessage = function (event) {
	document.getElementById('result').textContent = event.data; 
};
```

worker.js:

```
var n = 1;
search: while (true) {
	n += 1;
	for (var i = 2; i <= Math.sqrt(n); i += 1)
		if (n%i == 0) 
			continue search;
     // found a prime
	postMessage(n); 
}
```

主线程和工作线程之间通过 onmessage() 和 postMessage() 进行通信。


Node 主/子进程之间的通信 API 一定程度上相似, 进程间 通过 send()方法 发送数据，message 事件接收数据。

```
// parent.js
var cp = require('child_process');
var n = cp.fork(__dirname + '/sub.js');
n.on('message', function (m) { 
	console.log('PARENT got message:', m);
});
n.send({hello: 'world'});
```

```
// sub.js
process.on('message', function (m) { 
	console.log('CHILD got message:', m);
});
process.send({foo: 'bar'});
```

通过fork() 或者其他 API，创建子进程之后, 为了实现父子进程之间的通信, 父子进程之间将会创建IPC通道。通过 IPC 通道，父子进程之间才能通过 message和send() 传递消息。

***进程间通信原理***

IPC的全称是 Inter-Process Communication. 实现进程间通信的技术有很多，如命名管道，匿名管道，socket，信号量，共享内存，消息队列，Domain Socket等。

Node中实现IPC通道的是管道(pipe)技术，但此管道非彼管道。在Node中管道是个抽象层面的称呼，具体细节实现由libuv提供, unix系统采用 Unix Domain Socket实现。表现在应用层上的进程间通信只有简单的message事件和send()方法。

父进程在实际创建子进程前，会创建IPC通道并监听它，然后才真正创建出子进程，并通过环境变量( NODE_CHANNEL_FD ) 告诉子进程这个IPC通道的文件描述符。子进程在启动过程中，根据文件描述符去链接这个已经存在的IPC通道，从而完成父子进程之间的连接。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_IPC.png)

Node中，IPC通道被抽象为 Stream 对象，在调用 send() 时发送数据(类似 write())，在接收到消息会通过message事件( 类似于 data)
触发给应用层。

**注意**：只有启动的子进程是Node进程时，子进程才会根据环境变量去链接IPC通道，对于其他类型的子进程则无法实现进程间通信，除非其他进程也按约定去连接这个已经创建好的IPC通道。


### 9.2.3 句柄传递

建立好进程间的IPC后，如果仅仅只用来发送一些简单的数据，显然不够我们的实际应用使用。

问题描述: 如果启动多个服务器实例来监听，无法同时监听同一个端口。 这个问题破坏了我们将多个进程监听同一个端口的想法。

要解决问题，通常的做法是每个进程监听不同的端口，其中主进程监听主端口(80), 主进程对外接收所有的网络请求，再将这些请求分别代理道不同的端口的进程上。














