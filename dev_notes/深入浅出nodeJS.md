
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

```JavaScript
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

```JavaScript
 #!/usr/bin/env node
```

事实上，后面3种方法都是 spawn() 的延伸应用。

### 9.2.2 进程间通信

在前端浏览器中，JavaScript 主线程与UI渲染公用同一个线程，两者互相阻塞。

为了解决这个问题，HTML5 提出了 WebWorker API, 允许创建工作线程并在后台运行，使得一些阻塞较为严重的计算不影响主线程的UI渲染。

它的API 如下所示

```JavaScript
var worker = new Worker('worker.js'); 
worker.onmessage = function (event) {
	document.getElementById('result').textContent = event.data; 
};
```

worker.js:

```JavaScript
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

```JavaScript
// parent.js
var cp = require('child_process');
var n = cp.fork(__dirname + '/sub.js');
n.on('message', function (m) { 
	console.log('PARENT got message:', m);
});
n.send({hello: 'world'});
```

```JavaScript
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

**注意**：只有启动的子进程是Node进程时，子进程才会根据环境变
量去链接IPC通道，对于其他类型的子进程则无法实现进程间通信，除非其他进程也按约定去连接这个已经创建好的IPC通道。


### 9.2.3 句柄传递

建立好进程间的IPC后，如果仅仅只用来发送一些简单的数据，显然不够我们的实际应用使用。

问题描述: 如果启动多个服务器实例来监听，无法同时监听同一个端口。 这个问题破坏了我们将多个进程监听同一个端口的想法。

要解决问题，通常的做法是每个进程监听不同的端口，其中主进程监听主端口(80), 主进程对外接收所有的网络请求，再将这些请求分别代理道不同的端口的进程上。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_proxy.png)

通过代理，可以避免端口不能重复监听的问题，甚至可以在代理进程上做适当的负载均衡。 由于进程每接收到一个连接，将会用掉一个文件描述描述符，因此代理方案中客户端连接到工作进程，需要用掉两个文件描述符。操作系统的文件描述符是有限的，代理方案浪费掉一倍数量的文件描述符的做法影响了系统的扩展能力。

为了解决上述问题，Node在0.5.9版本引入了进程间发送句柄的功能。send()方法除了能通过IPC发送数据外，还能发送句柄，第二个可选参数就是句柄：

```JavaScript
child.send(message, [sendHandle])
```

句柄是一种可以用来标识资源的引用，他的内部包含了指向对象的文件描述符。比如句柄可以用来标识一个服务器socket对象，一个客户端socket对象，一个UDP套接字，一个管道等。

发送句柄意味着什么？ 在前一个问题中，我们可以去掉代理这种方案，使主进程接收到socket请求后，将这个socket直接发送给工作进程，而不是重新与工作进程之间建立新的socket连接来转发数据，以解决文件描述符浪费的问题。

```JavaScript
// parent.js
var cp = require('child_process'); 
var child1 = cp.fork('child.js'); 
var child2 = cp.fork('child.js');

// Open up the server object and send the handle 
var server = require('net').createServer(); 
server.on('connection', function (socket) {
	socket.end('handled by parent\n'); 
});
server.listen(1337, function () {
	// 发送句柄给 子进程
	child1.send('server', server); 
	child2.send('server', server);
});
```

```JavaScript
// child.js
process.on('message', function (m, server) { 
	if (m === 'server') {
		server.on('connection', function (socket) {
			socket.end('handled by child, pid is ' + process.pid + '\n');
		}); 
	}
});
```

这个示例中，直接将一个TCP服务发送给了子进程。用curl测试:

```bash
$ curl "http://127.0.0.1:1337/" handled by child, pid is 24673 
$ curl "http://127.0.0.1:1337/" handled by parent
$ curl "http://127.0.0.1:1337/" handled by child, pid is 24672
```

测试的结果每次出现的结果都可能不同，结果可能被父进程处理，也可能被子进程处理。并且这是在TCP层面上完成的事情，我们尝试将其转化到HTTP层面来试试。 对于主进程来而言，我们甚至想要它更轻量一点，那么是否将服务器句柄发送给子进程之后，就可以关掉服务器的监听，让子进程来处理请求呢？

```JavaScript
// parent.js
var cp = require('child_process');

var child1 = cp.fork('child.js'); 
var child2 = cp.fork('child.js');

// Open up the server object and send the handle 
var server = require('net').createServer(); 
server.listen(1337, function () {
	// 发送句柄给 子进程
	child1.send('server', server); 
	child2.send('server', server);
	// 关 
	server.close();
});
```

```JavaScript
// child.js
var http = require('http');
var server = http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('handled by child, pid is ' + process.pid + '\n'); 
});
process.on('message', function (m, tcp) { 
	if (m === 'server') {
		tcp.on('connection', function (socket) {
			server.emit('connection', socket);
		});
    }
});
```

```bash
$ curl "http://127.0.0.1:1337/" handled by child, pid is 24852 
$ curl "http://127.0.0.1:1337/" handled by child, pid is 24851
```

这样以来，所有的请求都是由子进程处理了。这个过程中，服务的过程发生了一次改变：


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_9.5.png)  ->  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_9.6.png)

我们发现，多个子进程可以同时监听相同端口，再没有 EAADINUSE 一场发生了。

***1. 句柄发送和还原***

上文介绍的虽然是句柄发送，但是仔细看看，句柄发送 跟 我们直接将服务器对象发送给 子进程 有没有差别？  它是否真的将服务器对象发送给了 子进程？ 为什么它可以发送到多个子进程？ 发送给子进程 为什么父进程中还存在这个对象？ 

目前 send() 	方法可以发送的句柄类型包括如下几种：

 - net.Socket   TCP 套接字
 - net.Server   TCP服务器， 任意建立在TCP服务上的应用层服务都可以享受到它带来的好处。
 - net.Native   C++层面的TCP套接字 或 IPC管道
 - dgram.Socket  UDP 套接字
 - dgram.Native   C++ 层面的UDP套接字

send() 方法在将消息发送到 IPC 管道前，将消息组装成两个对象, 一个对象是 handle, 另一个对象是 message.  message 参数如下:

```JSON
{
	cmd: 'NODE_HANDLE', 
	type: 'net.Server', 
	msg: message
}
```

发送到IPC管道中的实际上是我们要发送的句柄文件描述符，文件描述符实际上是一个整数值。这个message对象在写入到ICP管道时也会通过 JSON.stringify() 进行序列化。 所以最终发送到ICP管道中的信息都是字符串， send()方法能发送消息和句柄，并不意味着它能发送任意对象。

连接了IPC通道的子进程可以读取到父进程发来的消息， 将字符串通过 JSON.parse()解析还原为对象后，才出发message事件将消息体传递给应用层使用。 在这个过程中，消息对象还要被进行过滤处理，message.cmd 的值如果以NODE_ 为前缀，它将响应一个内部事件 internalMessage。如果message.cmd的值为NODE_HANDLE, 它将取出 message.type值和得到的文件描述符 一起还原出一个对应的对象:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_handle_send.png)















