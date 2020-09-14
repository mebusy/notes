...menustart

- [9 特种文件系统](#1f2926170990cf2be315dea64f695138)
    - [9.2 进程文件系统 procfs](#530245fecdfde469a4e7671a391909df)
        - [9.2.2 /proc 目录](#0725a0d61db90b83f77a95a287e57039)
        - [9.2.3 procfs 实战](#8e736138fbc50e7e4678aae7a5c1c001)
    - [9.3 tmpfs 满足你对 "时空" 的双重渴望](#92f11218638e56b59b5012b7f9dc69ad)
        - [9.3.3 tmpfs实战](#53e039499b6c1a8a91b3f21fd6ab739c)

...menuend


<h2 id="1f2926170990cf2be315dea64f695138"></h2>


# 9 特种文件系统

- 有一种文件系统， 根本不在磁盘上。
    - 这种文件系统就是大名鼎鼎的 ram-based filesystem
- 实际上， Linux系统中， /dev, /proc, /sys 目录里面的内容和硬盘 没有半毛钱关系。


<h2 id="530245fecdfde469a4e7671a391909df"></h2>


## 9.2 进程文件系统 procfs

- procfs 是一个 伪文件系统( 启动时动态生成的文件系统 ) 
    - 用于 用户空间通过内核访问进程信息。
    - 经过不断的演进， 如今 Linux 提供的 procfs 已经不单单用于访问进程信息， 还是一个用户空间与内核交换数据修改系统行为的接口
    - 这个文件系统 通常被 挂接到 /proc 目录

<h2 id="0725a0d61db90b83f77a95a287e57039"></h2>


### 9.2.2 /proc 目录

- /proc 目录下有很多的文件，如
    - cpuinfo
    - devices  可以用到的设备(块设备/字符设备)
    - diskstats  磁盘 I/O 统计信息
    - loadavg 负载信息
    - meminfo
    - mounts  已挂接的文件系统列表
    - partitions 磁盘分区信息
    - filesystems 支持的文件系统
    - interrupts 中断使用情况
    - iomem  I/O 内存映射信息
    - ioports I/O 端口分配信息
    - stat 全面统计状态表
    - swaps  交换空间使用情况
    - uptime 系统正常运行时间
    - version 内核版本
    - ...

- /proc 目录下还有很多目录 
    - [number] 
        - 每个进程对应一个目录， 目录名就是进程id
        - 只读
        - 典型的工具如 top, ps 等 ， 就是依据这些目录中的文件的内容 进程工作的
    - acpi  高级配置 与 电源接口
    - driver 驱动信息
    - fs 文件系统特别信息
    - ide  IDE 设备信息
    - irq 中断请求设置接口
    - net 网络各种状态信息
    - self  访问 proc 文件系统的进程的信息，等同于 /proc/pid_whoAccessProc
    - scsi SCSI 设备信息
    - sys 内核配置接口
        - 包含的文件大多是可写的, 通过 改写这些文件的内容，可以起到修改内核参数的目的。
        - 实际上 sysctl 即使利用这个目录实现的全部功能。
        - 使用 c 语言编程时， 系统调用的 sysctl 是这个接口的封装
    - sysvipc  记录中断产生次数
    - tty   tty 驱动信息


<h2 id="8e736138fbc50e7e4678aae7a5c1c001"></h2>


### 9.2.3 procfs 实战

- 中断平衡
- 一般情况下， 一台计算机，只有一个CPU.  所有设备为了获得CPU的青睐，就通过一种叫中断的机制来骚扰一下CPU. 
- 随着时代发展， 计算机开始朝 多核和多CPU方向发展。在这种情况下， 如何合理的将来自不同设备的中断请求划分给不同的CPU 就成了一个新的问题。
- 由此引入了一个新的概念： 中断平衡。
- 有了中断平衡，我们就又引入了以恶搞新的特权， 中断的CPU独享特权。 即可以指定某科具体的CPU 或 CPU的某颗核心 专门吹了某个或某些中断请求。
- 大多数 Linux 发行版都有一个默认的 中断平衡策略.
    - 但是 这些默认的中断平衡策略并不一定能够满足某个特定系统的性能要求，比如 一个有着非常繁重的网络资源请求的系统
- 默认的策略是， 网卡的中断请求在 多CPU 环境下， 仅发给 CPU0.
    - 在一定的情况下，会导致 CPU0的 占用率达到100%， 而其他的CPU 仅 2%-3%.
    - 解决的方法就是， 让网卡把中断请求 发给其他 CPU， 不过这也需要网卡配合才行，幸好现在大多数网卡都具备这个能力。
- 中断的CPU亲缘性
    - 设置好 中断的CPU亲缘性， 就可以让中断只发往 那些它所亲缘的CPU.
- 在设置之前，我们要先搞清楚， 我们的物理设备， 到底使用的是哪个中断

```base
# cat /proc/interrupts 
           CPU0       CPU1       CPU2       CPU3       
  0:        118          0          0          0   IO-APIC-edge      timer
  1:         10          0          0          0   IO-APIC-edge      i8042
  8:          0          0          0          0   IO-APIC-edge      rtc0
  9:          0          0          0          0   IO-APIC-fasteoi   acpi
 12:        155          0          0          0   IO-APIC-edge      i8042
 14:          0          0          0          0   IO-APIC-edge      ata_piix
 15:        118      93852          0          0   IO-APIC-edge      ata_piix
 19:        177          0          0    1432668   IO-APIC-fasteoi   enp0s3
 21:       6864      10541          0          0   IO-APIC-fasteoi   0000:00:0d.0, snd_intel8x0
 22:          0          0          0          0   IO-APIC-fasteoi   ohci_hcd:usb1
NMI:          0          0          0          0   Non-maskable interrupts
LOC:     849924     718090     472647    8967183   Local timer interrupts
SPU:          0          0          0          0   Spurious interrupts
PMI:          0          0          0          0   Performance monitoring interrupts
IWI:       6197      18815       4398    1127656   IRQ work interrupts
RTR:          0          0          0          0   APIC ICR read retries
RES:     158227     142863      67456     230946   Rescheduling interrupts
CAL:       2005       1675       5180       5082   Function call interrupts
TLB:       2451       2389       2288       2165   TLB shootdowns
TRM:          0          0          0          0   Thermal event interrupts
THR:          0          0          0          0   Threshold APIC interrupts
DFR:          0          0          0          0   Deferred Error APIC interrupts
MCE:          0          0          0          0   Machine check exceptions
MCP:        321        321        321        321   Machine check polls
ERR:          0
MIS:          0
PIN:          0          0          0          0   Posted-interrupt notification event
PIW:          0          0          0          0   Posted-interrupt wakeup event
```

- 这个例子中，我们可以看到我们的网卡 enp0s3 使用的是 19号中断，多集中在 CPU3
- 具体的是设置 /proc/irq/[interrupt num]/smp_affinity  文件的内容
    - 文件非常简单，  就一个16 进制数
        - 01 就意味着只有 CPU0 处理对应的中断
        - 0f 就意味着  CPU0 - CPU3 都处理对应中断


<h2 id="92f11218638e56b59b5012b7f9dc69ad"></h2>


## 9.3 tmpfs 满足你对 "时空" 的双重渴望

- 曾经内存比金子都贵，现在经白菜价了。 很多时候，磁盘都忙不过来，这时候完全可以让内存帮帮忙。 tmpfs 就是让你这么干的一个好帮手。

<h2 id="53e039499b6c1a8a91b3f21fd6ab739c"></h2>


### 9.3.3 tmpfs实战

**1 使用tmpfs**

- 使用 tmpfs 最基本的就是要把它挂接到文件系统的某一个节点

```
#mount tmpfs /tmp -t tmpfs
```

- 这个时候 /tmp 目录就开始使用 tmpfs 文件系统了。
    - 很爽吗？ 问题很快就会出现。 最典型的问题就是 用光了 VM.
    - 因为 tmpfs 是根据需要动态增大或减少内存。
- tmpfs 的设计者们早就想到了这个问题， 于是提供了一个参数， 来设定 tmpfs 的最大占用量
    - 实际使用中， 这个上限未必够用， 或者 仍然会导致 VM 被用光。需要好好规划.

```
#mount tmpfs /tmp -t tmpfs -o size=64m
```

**2 绑定挂接**

```
# mkdir /dev/shm/tmp
# chmod 1777 /dev/shm/tmp
# mount --bind /dev/shm/tmp /tmp
```

- `/dev/shm` 是 一个默认的 tmpfs 文件系统
- 将 `/dev/shm/tmp` 这个 tmpfs 绑定挂接到 /tmp 上， 这样所有使用/tmp目录作为临时目录的程序都会受益于 tmpfs 所提供的标准tmpfs ，同时 /dev/shm 它的最大容量限制一般可以被认为是最为优秀的， 比自己动手分析 好容易得多。


**3 应用加速**

- 可以利用 /dev/shm 创建一个 nginx_tmp 目录， 然后使用这个目录作为nginx的 各种 缓存临时目录.





