...menustart

 - [Node.js](#3b2819dd4c24eda2faf2052eef449551)
 - [1. 简介](#25970172060d4cb30529e42f3381e390)
	 - [1.4.3 单线程](#f94e4aef98455fe6c3c572995ee8173d)
	 - [1.5 Node 应用场景](#a371eba560ca50469627146fd5506f8a)
		 - [1.5.1 I/O 密集型](#ef7ae775712dcc6ec2888d01b7b6189c)
		 - [1.5.2 是否不擅长CPU密集型业务](#7f94465afa6516fbea09da8fc65f0022)
 - [2. 模块机制](#b5b4754699837a6839e68942ce084e48)
 - [9. 玩转进程](#f2034d1194cb14b32dfd43ad3db3ef3a)
	 - [9.2 多进程架构](#1e2a8f43da09b9e970bdfbd9995b5751)
		 - [9.2.1 创建子进程](#394f2abd6f7bb2dcc7325eec4cbfe80f)
		 - [9.2.2 进程间通信](#8aac8877e59cdc14e782c31f82d8f461)
		 - [9.2.3 句柄传递](#88e977e004306ff315571b0b1e9efea1)
			 - [1. 句柄发送和还原](#3d214d69419965e2a9cd55781db747c0)
			 - [2. 端口共同监听](#617e0e8bcb553ff8fb4c13d5f1dd6a04)
	 - [9.3 集群稳定之路](#580b016110dc238ba42ff6cef470f9bc)
		 - [9.3.1􏰀 􏲒􏲓􏶎􏶏](#3722ffe26a10fb5330ec2d0c5809e401)
		 - [9.3.2 自动重启](#26b69febcd523f91ed7df3f4b4af5c23)
			 - [自杀信号](#6bcdd9159198086f18f0a641531859c8)
			 - [2. 限量重启](#19e7bc0667e049833d1138b93611b7e1)

...menuend



<h2 id="3b2819dd4c24eda2faf2052eef449551"></h2>
# Node.js

<h2 id="25970172060d4cb30529e42f3381e390"></h2>
# 1. 简介

<h2 id="f94e4aef98455fe6c3c572995ee8173d"></h2>
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


<h2 id="a371eba560ca50469627146fd5506f8a"></h2>
## 1.5 Node 应用场景

<h2 id="ef7ae775712dcc6ec2888d01b7b6189c"></h2>
### 1.5.1 I/O 密集型

I/O密集的优势主要在于Node利用事件循环的处理能力，而不是启动每一个线程为每一个请求服务，资源占用极少。

<h2 id="7f94465afa6516fbea09da8fc65f0022"></h2>
### 1.5.2 是否不擅长CPU密集型业务

 - Node 可以通过编写 C/C++ 扩展的方式更高效的利用CPU, 将一些V8不能做到性能极致的地方通过C++实现。
 - 如果单线程的Node 不能满足需求，甚至用了C/C++ 扩展后还觉得不够，那么通过子进程的方式，将一部分Node进程当作常驻服务用于计算。
 	- 然后利用进程间的消息来传递结果，将计算与I/O 分离。
 - CPU 密集不可怕，如果合理调度是诀窍。


<h2 id="b5b4754699837a6839e68942ce084e48"></h2>
# 2. 模块机制


<h2 id="f2034d1194cb14b32dfd43ad3db3ef3a"></h2>
# 9. 玩转进程

从严格意义上而言，Node并非真正的单线程架构，Node自身还有一定的I/O线程存在，这些I/O线程存在。

这部分线程对于 开发者而言是透明的，只有C++扩展时才会关注到。

<h2 id="1e2a8f43da09b9e970bdfbd9995b5751"></h2>
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


<h2 id="394f2abd6f7bb2dcc7325eec4cbfe80f"></h2>
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

<h2 id="8aac8877e59cdc14e782c31f82d8f461"></h2>
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


<h2 id="88e977e004306ff315571b0b1e9efea1"></h2>
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

<h2 id="3d214d69419965e2a9cd55781db747c0"></h2>
#### 1. 句柄发送和还原

上文介绍的虽然是句柄发送，但是仔细看看，句柄发送 跟 我们直接将服务器对象发送给 子进程 有没有差别？  它是否真的将服务器对象发送给了 子进程？ 为什么它可以发送到多个子进程？ 发送给子进程 为什么父进程中还存在这个对象？ 

目前 send() 	方法可以发送的句柄类型包括如下几种：

 - net.Socket   TCP 套接字
 - net.Server   TCP服务器， 任意建立在TCP服务上的应用层服务都可以享受到它带来的好处。
 - net.Native   C++层面的TCP套接字 或 IPC管道
 - dgram.Socket  UDP 套接字
 - dgram.Native   C++ 层面的UDP套接字

send() 方法在将消息发送到 IPC 管道前，将消息组装成两个对象, 一个对象是 handle, 另一个对象是 message.  message 参数如下:

```json
{
	cmd: 'NODE_HANDLE', 
	type: 'net.Server', 
	msg: message
}
```

发送到IPC管道中的实际上是我们要发送的句柄文件描述符，文件描述符实际上是一个整数值。这个message对象在写入到ICP管道时也会通过 JSON.stringify() 进行序列化。 所以最终发送到ICP管道中的信息都是字符串， send()方法能发送消息和句柄，并不意味着它能发送任意对象。

连接了IPC通道的子进程可以读取到父进程发来的消息， 将字符串通过 JSON.parse()解析还原为对象后，才出发message事件将消息体传递给应用层使用。 在这个过程中，消息对象还要被进行过滤处理，message.cmd 的值如果以NODE_ 为前缀，它将响应一个内部事件 internalMessage。如果message.cmd的值为NODE_HANDLE, 它将取出 message.type值和得到的文件描述符 一起还原出一个对应的对象:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_handle_send.png)

 以发送的TCP服务器句柄为例， 子进程收到消息后的 还原过程如下:

```JavaScript
function(message, handle, emit) {
	var self = this;
	// 子进程根据 message.type 创建对应 TCP服务器对象
	var server = new net.Server(); 
	// 然后监听到 文件描述符上
	server.listen(handle, function() {
		emit(server);  
	});
}
```

所以在子进程中， 开发者会有一种服务器就是从 父进程中直接传递过来的错觉。 **值得注意：** Node进程之间只有消息传递，不会真正传递对象。

目前 Node 只支持上述提到的几种句柄，并非任意类型的句柄都能在进程之间传递，除非它有完整的发送和还原过程。

<h2 id="617e0e8bcb553ff8fb4c13d5f1dd6a04"></h2>
#### 2. 端口共同监听 

 - 独立启动的多个进程中， TCP服务器端 socket套接字的文件描述符 并不相同，导致监听到相同的端口时会抛出异常
 - Node 底层对每个端口监听都设置了 SO_REUSEADDR 选项，这个选项的含义是 不同的进程 可以就相同的网卡和端口进行监听，这个套接字可以被不同的进程复用
 	- 对于 send() 发送的句柄还原出服务而言, 他们的文件描述符是相同的，所以监听相同端口不会引起一场。

```C
setsockopt(tcp->io_watcher.fd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on))
```

 - 多个应用监听相同端口时， 文件描述符同一时间只能被某个进程所用。 也就是说， 网络请求向服务端发送时， 只有一个幸运的进程能够抢到链接，只有它能为这个请求服务。这些进程服务是抢占式的。



<h2 id="580b016110dc238ba42ff6cef470f9bc"></h2>
## 9.3 集群稳定之路

搭建好了集群，充分利用了CPU资源，似乎就可以迎接客户端大量的请求了。但我们还有一些细节需要考虑。

 - 性能问题
 - 多个工作进程的存货状态管理
 - 工作进程的平滑重启
 - 配置活着静态数据的动态重新载入
 - 其他细节

是的，虽然我们创建了很多工作进程，但每个工作进程依然是在单线程上执行的，他的稳定性还不能得到完全的保障。 我们需要建立起一个健全的机制来保障Node应用的健壮性.

<h2 id="3722ffe26a10fb5330ec2d0c5809e401"></h2>
### 9.3.1􏰀 􏲒􏲓􏶎􏶏

再次回到子进程对向上，除了引人关注的 send() 方法 和 message 事件外，子进程还有些什么? 

除message事件外, 父进程能监听到的子进程相关事件:

 - error:  当子进程 无法被复制创建, 无法被杀死，无法发送消息时， 会触发改事件
 - exit:  子进程退出时 触发该事件。 如果是正常退出，第一个参数是 退出码，否则为 null. 如果进程是通过 kill() 方法杀死的, 会得到第二个参数，他表示杀死进程时的信号.
 - close:  在子进程的标准输入输出流 终止时， 触发该事件
 - disconnect:  在父进程 或 子进程中 调用 disconnect() 方法时触发该事件
 	- 在调用调用 disconnect() 方法时 将关闭监听 IPC 通道

除了 send() 外， 还能通过 kill() 方法给子进程发送消息。 kill() 方法并不能真正地将 通过IPC相连的子进程杀死，它只是给子进程发送了一个系统信号。 默认情况下，kill() 方法会发送一个 SIGTERM 信号。它与进程默认的kill() 方法类似:

```JavaScript
// 发送给子进程
child.kill([signal]);
// 发送给 目标进程
process.kill(pid, [signal]);
```

POSIX 标准中，， 有一套完备的信号系统， `kill -l` 可以看到详细的信号列表:

```bash
$ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
 5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
 9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
29) SIGINFO	30) SIGUSR1	31) SIGUSR2
```

Node 提供了这些信号对应的信号事件， 每个进程都可以监听这些信号事件。 如 SIGTERM 是软件终止信号，进程收到该信号时应当退出。

```JavaScript
process.on('SIGTERM', function() { 
	console.log('Got a SIGTERM, exiting...'); 
	process.exit(1);
});

console.log( 'server running with PID:' , process.pid );
process.kill( process.pid , 'SIGTERM' ) ;
```


<h2 id="26b69febcd523f91ed7df3f4b4af5c23"></h2>
### 9.3.2 自动重启

有了父子进程之间的相关事件后，就可以在这些关系之间创建出需要的机制了。  至少我们能够监听子进程的 exit 事件来获知其退出的消息, 接着前文的多进程架构，我们在主进程上要加入一些子进程管理的机制，比如重新启动一个工作进程来继续服务。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_restart_subprocess.png)

```JavaScript
// master.js
var fork = require('child_process').fork; 
var cpus = require('os').cpus();

var server = require('net').createServer(); 
server.listen(1337);

var workers = {};
var createWorker = function () {
	var worker = fork(__dirname + '/worker.js'); 
	// 􏶥退出时重􏶦启动􏶦的进程
	worker.on('exit', function () {
		console.log('Worker ' + worker.pid + ' exited.'); 
		delete workers[worker.pid];
		createWorker();
	});
	// 句柄转发
	worker.send('server', server); 
	workers[worker.pid] = worker;
	console.log('Create worker. pid: ' + worker.pid);
};

for (var i = 0; i < cpus.length; i++) { 
	createWorker();
}
// 进程自己退出时, 所有工作进程􏶥退出
process.on('exit', function () {
	for (var pid in workers) { 
		workers[pid].kill();
	} 
});	
```

在实际业务中，可能有隐藏的bug导致工作进程退出，那么我们需要仔细地处理这种异常，如下所示:

```JavaScript
// worker.js
var http = require('http');
var server = http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('handled by child, pid is ' + process.pid + '\n'); 
});
var worker;
process.on('message', function (m, tcp) {
	if (m === 'server') {
		worker = tcp;
		worker.on('connection', function (socket) {
			server.emit('connection', socket); 
		});
	} 
});

process.on('uncaughtException', function () {
	// 􏶮􏶯停止接收新的链接
	worker.close(function () {
		// 所有已有链接断开后，退出进程
		process.exit(1); 
	});
});
```

上述代码的处理流程是， 一旦有未捕获的异常出现，工作进程就会立即停止接收新的链接； 当所有的连接断开后，退出进程。 主进程在 监听到工作进程的exit后，将会立即启动新的进程服务，以此保证整个集群中 总是有进程在为用户服务的。

<h2 id="6bcdd9159198086f18f0a641531859c8"></h2>
#### 自杀信号

上述代码存在的问题是 要等到所有链接断开后 进程才会退出， 在极端的情况下， 所有工作进程都停止接收新的链接，全处在等待退出的状态。 但是等到进程完全退出才重启的过程中，会丢到大部分请求。

为此需要改进这个过程， 不能等到工作进程退出后才重启新的工作进程。 当然也不能暴力退出进程，因为这样会导致以连接的用户直接断开。 于是我们在退出的流程中增加一个自杀(suicide)信号。 工作进程在得知要退出时，向主进程发送一个自杀信号，然后才停止接收新的链接，当所有连接断开后才退出。 主进程在接收到自杀信号后，立即创建新的工作进程服务。

```JavaScript
// worker.js
process.on('uncaughtException', function (err) {
	process.send({act: 'suicide'}); 
	// 􏶮􏶯停止接收新的连接 
	worker.close(function () {
		// 所有已有链接断开后，退出进程
		process.exit(1); 
	});
});	
```

主进程将重启工作进程的任务，从 exit 事件的处理函数中转移到 message 事件的处理函数中：

```JavaScript
var createWorker = function () {
	var worker = fork(__dirname + '/worker.js'); 
	// 自杀时 启动􏶦新的进程
	worker.on('message', function (message) {
		if (message.act === 'suicide') { 
			createWorker();
		} 
	});
	worker.on('exit', function () {
		console.log('Worker ' + worker.pid + ' exited.');
		delete workers[worker.pid]; 
	});
	worker.send('server', server); 
	workers[worker.pid] = worker;
	console.log('Create worker. pid: ' + worker.pid);
};	
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_restart_suicide.png)


这里存在的问题是 有可能我们的链接是长连接，是不是 HTTP 服务这种短连接， 等待长连接断开可能需要较久的时间。 为此 为已有链接的断开设置一个超时时间是有必要的，在限定时间内强制退出:

```JavaScript
process.on('uncaughtException', function (err) {
	// 􏷀出现未捕获异常，说明代码的健壮性上是不合格的
	// 必须通过日志记录下问题的所在, 以帮助定位和追踪代码异常出现的位置
	logger.error(err);
	// 发送自杀信号
	process.send({act: 'suicide'}); 
	// 停止接收新的连接
	worker.close(function () {
		// 􏶩所有已有链接断开后，退出进程
		process.exit(1);
	});
	// 5秒后退出进程
	setTimeout(function () {
		process.exit(1); 
	}, 5000);
});
```

<h2 id="19e7bc0667e049833d1138b93611b7e1"></h2>
#### 2. 限量重启

工作进程不能无限制的重启，如果启动的过程中就发生了错误，或者启动后接到连接就收到错误会导致工作进程被频繁重启。

为了消除这种无意义的重启，在满足一定规则的限制下，不应当反复重启。比如在单位时间内规定只能重启多少次，超过限制就触发 giveup事件，告知放弃重启。

```JavaScript
// 重启次数 
var limit = 10;
// 时间单位
var during = 60000;
var restart = [];

var isTooFrequently = function () {
	// 记录重启时间
	var time = Date.now();
	var length = restart.push(time); 
	if (length > limit) {
		// 取出最后10个纪录
		restart = restart.slice(limit * -1); 
	}
	// 最后一次重启到前10次重启之间的时间间隔
	return restart.length >= limit && restart[restart.length - 1] - restart[0] < during; 
};


var workers = {};
var createWorker = function () {
	// 检查是否太过频繁
	if (isTooFrequently()) {
		// 触发giveup事件后, 不再重启
		process.emit('giveup', length, during); 
		return;
	}

	var worker = fork(__dirname + '/worker.js');
	...
```

giveup 事件是比 uncaughtException 更严重的异常事件。


### 9.3.3 负载均衡

Node 默认提供的机制是采用操作系统的抢占式策略。 一般而言，抢占式策略对大家是公平的，各个进程可以根据自己的繁忙度来进行抢占。但是对于Node而言，需要分清的是它的繁忙是由CPU,I/O 两个部分构成的，影响抢占的是CPU的繁忙度。 对不同的业务，可能存在 I/O繁忙，而CPU较为空闲的情况，这可能造成某个进程能够抢到较多请求，行程负载不均衡的情况。

为此 Node在 v0.11中提供了一种新的策略使得负载均衡更合理: Round-Robin, 又叫轮叫调度。 轮叫调度的工作方式是由主进程接收连接， 将其一次分发给工作进程。 分发的策略是在 N个工作进程中，每次选择第 i=(i+1) mod n . 在 cluster 模块中启用它的方式如下:

```JavaScript
// 启用 Round-Robin
cluster.schedulingPolicy = cluster.SCHED_RR 
// 不启用Round-Robin
cluster.schedulingPolicy = cluster.SCHED_NONE
```

或者在环境变量中设置: NODE_CLUSTER_SCHED_POLICY 的值

```bash
export NODE_CLUSTER_SCHED_POLICY=rr
export NODE_CLUSTER_SCHED_POLICY=none
```

Round-Robin 非常简单, 可以避免 CPU 和 I/O 繁忙差异导致的负载不均衡。Round-Robin 策略也可以通过代理服务器来实现，但是它会导致服务器上消耗的文件描述符是平常的两倍。


### 9.3.4 状态共享

Node 进程中不宜存放太多数据, 

 - 因为它会加重垃圾回收的负担，进而影响性能。
 - 同时，Node也不允许在多个进程之间共享数据。

但在实际的业务中, 往往需要共享一些数据，譬如配置数据, 这在多个进程中应当是一致的。为此，在不允许共享数据的情况下，我们需要一种方案和机制来实现数据在多个进程之间的共享。


***第三方数据存储***

解决数据共享最直接，简单的方式就是通过第三方来进行数据存储，比如将数据存放到 数据库，磁盘文件， 缓存服务(如 Redis) 中，所有工作进程启动时将其读取进内存。但这种方式存在的问题是，如果数据发生变化，还需要一种机制通知各个子进程，使得它们的内部状态也得到更新。

实现状态同步的机制有两种:

1. 各个子进程 向第三方进行定时轮询
	- 轮询带来的问题是，轮询时间不能过密，也不能过长
2. 主动通知
	- 当数据发生更新时，主动通知子进程
	- 仍需要一种机制来及时获取数据的改变，这个过程仍然不能脱离轮询，但可以减少轮询的进程数量。

我们将 这种 用来发送通知 和查询状态是否更改 的进程叫 通知进程。为了不混合业务逻辑，可以将这个进程设计为只进行轮询和通知，不处理任何业务逻辑。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Nodejs_notify_process.png)

这种推送机制 如果按进程间信号传递，在跨多台服务器会无效(因为其他服务器无法获取配置文件)，是故可以考虑采用 TCP或UDP的方案。 进程在启动时从通知服务处 读取第一次数据外，还将进程信息注册到通知服务处。 一旦发现数据更新后，根据注册信息，将更新后的数据发送给工作进程。

## 9.4 Cluster 模块

前文介绍如何通过 child_process 模块构件强大的单机集群。 上述提及的问题，Node在v0.8版本时新增的 cluster 模块就能解决。 child_process 来实现单机集群，有这么的细节要处理，对普通工程师而言是一件相对较难的工作，于是v0.8直接引入了 cluster 模块，用于解决多核 CPU的利用率问题，同时也提供了较晚上的API，用以处理进程的健壮性问题。

```JavaScript
// cluster.js
// 创建进程集群
var cluster = require('cluster');
cluster.setupMaster({ 
	exec: "worker.js"
});

var cpus = require('os').cpus();
for (var i = 0; i < cpus.length; i++) {
	cluster.fork(); 
}
```

就官方的文档而言，它更喜欢如下的形式作为示例:

```JavaScript
var cluster = require('cluster');
var http = require('http');
var numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
	// Fork workers
	for (var i = 0; i < numCPUs; i++) {
		cluster.fork(); 
	}
	
	cluster.on('exit', function(worker, code, signal) {
		console.log('worker ' + worker.process.pid + ' died');
	});
} else {
	// Workers can share any TCP connection
	// In this case its a HTTP server 
	http.createServer(function(req, res) {
		res.writeHead(200);
        res.end("hello world\n");
    }).listen(8000);
}
```

在进程中判断是主进程还是工作进程，主要取决于环境变量中是否有 NODE_UNIQUE_ID, 如下所示:

```JavaScript
cluster.isWorker = ('NODE_UNIQUE_ID' in process.env); 
cluster.isMaster = (cluster.isWorker === false);
```

但是官方示例中，忽而判断cluster.isMaster, 忽而判断cluster.isWorker，对于代码可读性十分差。我建议用 cluster.setupMaster()这个API, 将主进程和工作进程从代码上完全剥离。 

通过cluster.setMaster()创建子进程而不是食用 cluster.fork(), 程序结构不在凌乱，逻辑分明，代码的可读性和可维护性较好。

### 9.4.1 Cluster 工作原理

事实上 cluster 模块就是 child_process 和 net 模块的组合应用。

 - cluster 启动时，会在内部启动TCP服务器
 - cluster.fork() 子进程时， 将这个 TCP 服务器端socket的文件描述符发送给工作进程。
 	- 如果进程时通过 cluster.fork() 复制出来的，那么它的环境变量里就存在 NODE_UNIQUE_ID, 
 	- 如果工作进程中存在 listern()监听端口的调用，它将拿到该文件描述符，通过SO_REUSEADDR 端口重用, 从而实现多个子进程共享端口。
 	- 对于普通方式启动的进程，则不存在文件描述符传点共享等事情

在cluster 内部隐式创建TCP服务器的方式对使用者来说十分透明，但也正是这种方式使得它无法入直接使用child_process 那样灵活。在 cluster 模块应用中, 一个主进程只能管理一组工作进程； 而通过 child_process 可以更灵活地控制工作进程，甚至控制多组工作进程。其原因在于 child_process 可以隐式地创建多个TCP服务器，使得子进程可以共享多个的服务端socket.















