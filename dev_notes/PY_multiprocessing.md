...menustart

- [misc](#bc957e26ff41470c556ee5d09e96880b)
- [multiprocessing](#7d16d5f74fcafb1de1680fe3e95caee9)
    - [1. Process 创建进程](#dc1a9383b903911b01b71c8e0179c6d9)
        - [例1.1：创建函数并将其作为单个进程](#b0ffb6388e2c0e1cb47cc6b296bd5447)
        - [例1.2：创建函数并将其作为多个进程](#ad53f99d06670e9f003b7021ace3c950)
        - [例1.3：将进程定义为类](#34a15aa2e6a52c472f1d7f839e1f755f)
        - [例1.4：daemon程序对比结果](#157b9b8df424cb4ea14f839cb169de42)
    - [2. Lock 锁](#f2d8e041449ee7f8215288ffa489e5e7)
    - [3. Semaphore 信号](#84a93a4956101499a69692b1f755c8cc)
    - [4. Event 进程间同步](#81fcc5cb44cff9dd761655e784a65dd6)
    - [5. Queue 队列,进程间数据传递](#76a5f0b51a2d4b7fcf20ca7897f9a2bc)
    - [6. Pipe](#4947895871a9c40853bedd0110bf82db)
    - [7. Pool](#23dc6941df5635688ee2aa31cd26ddb4)
        - [例7.1：使用进程池](#15ea9a5d5012976d2c28a505a781e443)
        - [例7.3：使用进程池，并关注结果](#acca268bc49ea57fab2c41310811d403)

...menuend


<h2 id="bc957e26ff41470c556ee5d09e96880b"></h2>


# misc 

- 主线程对 CTRL-C signal的响应
    1. 无论主线程是否等待其他线程结束执行，如果主线程执行完了所有代码，将不会响应 CTRL-C
    2. 主线程 block 住的情况下，也不会响应 CTRL-C
    3. solution : `while True` in main thread.
- sys.exit() called in thread is as same as calling "thread.exit()" , it will not kill process.
    - solution: maintain a Queue.Queue in mainthread, and threads put `sys.quit()` callback to that queue ,and main thread will call it from the queue.
- CTRL-C will not terminate the thread , unless it runs as daemon.



<h2 id="7d16d5f74fcafb1de1680fe3e95caee9"></h2>


# multiprocessing

multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

<h2 id="dc1a9383b903911b01b71c8e0179c6d9"></h2>


## 1. Process 创建进程
创建进程的类：**Process**([group [, target [, name [, args [, kwargs]]]]])， 
target表示调用对象， 
args表示调用对象的位置参数元组。 
kwargs表示调用对象的字典。 
name为别名。 
group实质上不使用。
方法：is_alive()、join([timeout])、run()、start()、terminate()。其中，Process以start()启动某个进程。

属性：authkey、daemon（要通过start()设置）、exitcode(进程在运行时为None、如果为–N，表示被信号N结束）、name、pid。 


<h2 id="b0ffb6388e2c0e1cb47cc6b296bd5447"></h2>


### 例1.1：创建函数并将其作为单个进程

```python
import multiprocessing
import time

def worker(interval):
    n = 3
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (2,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
```
运行结果：

    p.pid: 77784
    p.name: Process-3
    p.is_alive: True
    The time is Mon Nov  9 14:12:46 2015
    The time is Mon Nov  9 14:12:48 2015
    The time is Mon Nov  9 14:12:50 2015


<h2 id="ad53f99d06670e9f003b7021ace3c950"></h2>


### 例1.2：创建函数并将其作为多个进程

```python
import multiprocessing
import time

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    
    p1.start()
    p2.start()
    
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
```

运行结果:

    worker_1
    worker_2
    The number of CPU is:4
    child   p.name:Process-14    p.id77846
    child   p.name:Process-13    p.id77845
    END!!!!!!!!!!!!!!!!!
    end worker_1
    end worker_2


    注意: 1.1 , 1.2 主进程和其他进程打印的顺序是不一定的。


<h2 id="34a15aa2e6a52c472f1d7f839e1f755f"></h2>


### 例1.3：将进程定义为类

```python
import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval
        
    def run(self):
        n = 3
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess(2)
    p.start()
```

运行结果:

    the time is Mon Nov  9 14:30:32 2015
    the time is Mon Nov  9 14:30:34 2015
    the time is Mon Nov  9 14:30:36 2015


    注：进程p调用start()时，自动调用run()

<h2 id="157b9b8df424cb4ea14f839cb169de42"></h2>


### 例1.4：daemon程序对比结果
daemon属性设置：
```python
p.daemon = True
p.start()           #必须在start()之前设置。
```

1. 不设置daemon属性，主进程和其他进程，各自之行完后各自结束
2. 设置daemon属性，如果主进程结束， 其他daemon进程也跟着结束
3. p.join() 通知主进程,等待该 daemon进程结束。

```python
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.daemon = True
    p.start()
    p.join()
    print "end!"
```

运行结果：

    work start:Mon Nov  9 14:37:07 2015
    work end:Mon Nov  9 14:37:10 2015
    end!

<h2 id="f2d8e041449ee7f8215288ffa489e5e7"></h2>


## 2. Lock 锁

当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。

```python
import multiprocessing
import sys

def worker_with(lock, f):
    with lock:
        fs = open(f, 'a+')
        n = 5
        while n > 1:
            fs.write("Lockd acquired via with\n")
            n -= 1
        fs.close()


def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 5
        while n > 1:
            fs.write("Lock acquired directly\n")
            n -= 1
        fs.close()
    finally:
        lock.release()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    f = "file.txt"
    w = multiprocessing.Process(target = worker_with, args=(lock, f))
    nw = multiprocessing.Process(target = worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    print "end"
```

运行结果:

    Lockd acquired via with
    Lockd acquired via with
    Lockd acquired via with
    Lockd acquired via with
    Lock acquired directly
    Lock acquired directly
    Lock acquired directly
    Lock acquired directly

<h2 id="84a93a4956101499a69692b1f755c8cc"></h2>


## 3. Semaphore 信号
Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。

    注: go语言中，一般使用 buffered channels 来实现 信号量控制


```python
import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + "acquire");
    time.sleep(i)
    print(multiprocessing.current_process().name + "release\n");
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)
    for i in range(3):
        p = multiprocessing.Process(target = worker, args=(s, i*2))
        p.start()
```

运行结果:

    Process-1acquire
    Process-1release
    Process-2acquire
    Process-3acquire
    Process-2release
    Process-3release


<h2 id="81fcc5cb44cff9dd761655e784a65dd6"></h2>


## 4. Event 进程间同步
    
event.wait() 会等待 ,直到 event 被 set() 或 超时。

```python
import multiprocessing
import time

def wait_for_event(e):
    print("wait_for_event: starting")
    e.wait()
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))

def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))

if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = "block",
            target = wait_for_event,
            args = (e,))
    w2 = multiprocessing.Process(name = "non-block",
            target = wait_for_event_timeout,
            args = (e, 2))
    w1.start()
    w2.start()
    time.sleep(3)
    e.set()
    print("main: event is set")
```

运行结果:

    wait_for_event: starting
    wait_for_event_timeout:starting
    wait_for_event_timeout:e.is_set->False
    main: event is set
    wairt_for_event: e.is_set()->True


<h2 id="76a5f0b51a2d4b7fcf20ca7897f9a2bc"></h2>


## 5. Queue 队列,进程间数据传递

Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。  

put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。 
如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。 
如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
 
get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。 
如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。 
如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。Queue的一段示例代码：

```python

def writer_proc(q):      
    q.put(1, block = False) 
    ...

if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))  
    writer.start()   
    writer.join()
    ...
```

<h2 id="4947895871a9c40853bedd0110bf82db"></h2>


## 6. Pipe 

Pipe方法返回(conn1, conn2)代表一个管道的两个端。 
Pipe方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发。 
duplex为False，conn1只负责接受消息，conn2只负责发送消息。
 
send和recv方法分别是发送和接受消息的方法。 
例如，在全双工模式下，可以调用conn1.send发送消息，conn1.recv接收消息。 
如果没有消息可接收，recv方法会一直阻塞。 
如果管道已经被关闭，那么recv方法会抛出EOFError。

```python
import multiprocessing
import time

def proc1(pipe):
    while True:
        for i in xrange(5):
            print "send: %s" %(i)
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    while True:
        print "proc2 rev:", pipe.recv()
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
```

运行结果：

    send: 0
    proc2 rev: 0
    send: 1
    proc2 rev: 1
    send: 2
    proc2 rev: 2
    send: 3
    proc2 rev: 3
    send: 4


<h2 id="23dc6941df5635688ee2aa31cd26ddb4"></h2>


## 7. Pool

当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

<h2 id="15ea9a5d5012976d2c28a505a781e443"></h2>


### 例7.1：使用进程池

```python
#coding: utf-8
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(4):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))         
        
    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   
    #调用join之前，先调用close函数，否则会出错。
    #执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    #join方法要在close或terminate之后使用。
    print "Sub-process(es) done."
```

运行结果:

    <multiprocessing.pool.ApplyResult object at 0x10ef2e610>
    <multiprocessing.pool.ApplyResult object at 0x10ef2e6d0>
    <multiprocessing.pool.ApplyResult object at 0x10ef2e750>
    <multiprocessing.pool.ApplyResult object at 0x10ef2e810>
    Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~
    msg: hello 0
    msg: hello 1
    msg: hello 2
    end
    end
    msg: hello 3
    end
    end
    Sub-process(es) done.

<h2 id="acca268bc49ea57fab2c41310811d403"></h2>


### 例7.3：使用进程池，并关注结果

```python
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"
    return "done" + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(3):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
        
    pool.close()
    pool.join()
    for res in result:
        print ":::", res.get()
        
    print "Sub-process(es) done."
```

运行结果:

    msg: hello 0
    msg: hello 1
    msg: hello 2
    end
    end
    end
    ::: donehello 0
    ::: donehello 1
    ::: donehello 2
    Sub-process(es) done.


