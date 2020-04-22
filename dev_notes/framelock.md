...menustart

 - [帧同步](#a9592bd6610be7f901063c580069e497)
     - [客户端计算的一致性](#d262643e7cacb177cde62b3346ad0abd)
     - [网络](#7ddbe15c845fa27a2bab496183042ca6)
 - [实现 #1 传统客户端](#8fb429f2c732df02beed40b4aee2d98a)
 - [实现 #2 预测回滚](#9eafae7566ddfa5de0886c16c02cbd00)
 - [Overwatch](#fcaeeb6e34b4303e99b91206bd325f2b)
 - [Mortal Kombat](#0be50d21cd18f6cf70ec79971504b63b)
 - [Halo](#aa6df57fb6fe377d80b4a257b4a92cba)
 - [其他](#0d98c74797e49d00bcc4c17c9d557a2b)

...menuend


<h2 id="a9592bd6610be7f901063c580069e497"></h2>


# 帧同步

<h2 id="d262643e7cacb177cde62b3346ad0abd"></h2>


##  客户端计算的一致性

1. 使用定点数取代浮点数
2. 三角函数查表
3. 自己实现 PRNG


<h2 id="7ddbe15c845fa27a2bab496183042ca6"></h2>


## 网络

server负责统一tick，并转发client的指令，通知其他client 


- 网络协议的选择
    - 基于可靠传输的UDP
        - UDP上加一层封装，自己去实现丢包处理，消息序列，重传等类似TCP的消息处理方式，保证上层逻辑在处理数据包的时候，不需要考虑包的顺序，丢包等。
        - 类似实现 Enet, KCP
        - 不是非常合适在帧同步中使用
    - 冗余信息的UDP
        - 需要上层逻辑自己处理丢包，乱序，重传等问题
        - 两端的消息里面，带有确认帧信息
            - 比如客户端（C）通知服务器（S）第100帧的数据，S收到后通知C，已收到C的第100帧，如果C一直没收到S的通知（丢包，乱序等原因），就会继续发送第100帧的数据给S，直到收到S的确认信息。
        - kcp+fec的模式 实现上更好？？？


[游戏逻辑回滚](https://zhuanlan.zhihu.com/p/38468615)  适合少数角色联机的，对操作反馈要求非常高的, 比如格斗游戏



<h2 id="8fb429f2c732df02beed40b4aee2d98a"></h2>


# 实现 #1 传统客户端

1. 服务器定期广播
2. 客户端只有接收到服务器的消息后，才step  模拟

对输入做预测？

会有延迟

<h2 id="9eafae7566ddfa5de0886c16c02cbd00"></h2>


# 实现 #2 预测回滚

- 客户端本地有2个 buffer， 
    - 客户端把操作发给服务器的时候，还会 插入到本地的buffer: LBuffer.
        - 本地buffer，其他玩家的操作，需要客户端自己使用一定的算法做预测
    - 同时从服务器接收到的，放入 SBuffer 
- step 的时候，某一个step的，如果 服务器的输入到了的话，就用 SBuffer 的数据, 否则就用 LBuffer 
    - 因为 LBuffer 中的其他玩家输入都是预测的，所以会出现预估失败的情况
    - 客户端的帧，一般都是超前服务器的
        - 比如客户端在第7帧的时候，服务器第2帧数据才到， 如果和本地第二帧的数据不一样了，你预测失败了，这个时候，就需要回滚到第1帧执行完后的状态。然后重新step直到当前帧
- 如何回滚
    1. 数据备份
        - 代码生成
        - memcpy
    2. 数据恢复
        - 写入文件
        - 命令 ( 如 地图中删除一个物件)



<h2 id="fcaeeb6e34b4303e99b91206bd325f2b"></h2>


# Overwatch 

- client go head by half RTT + buffer 
- mispredict
    - rollback
    - regenerate LBuffer , re-predict
- client 的包丢失
    - the server tries to keep this tiny buffer of unsimulated input as small as possible 
    - if the server has to starve out this little buffer, it's just gonna guess and duplicate your last input
    - and by the time that real input arrives you look how to reconcile that and make sure you don't lose any buttons, but they're gonna mispredict. 
        - if server can not receive the frame packet from client,  server send its packet, and tells clents  by the way hey I lost some input something's wrong. 
        - what's gonna happen is the client is going to start to simulate slightly faster :
            - if the fixed time step is 16ms, the client is just going to pretent that the fixed time step is now 15.2 ms. it's gonna advance much faster.  it will lead to that the server's gonna have a much bigger buffer.
    - once the server realizes that you're healthy it'll send you messages saying hey you know it's fine , the client will do the opposite.  The feedback loop is happening constantly and the goal of it is to try to minimize mispredictions because of input duplication. 
    - once client catch up the input that was skipped is in danger of being lost, to solve this problem, the client always sends up a sliding window of input 
        - it send all of the input that have simulated from the last acknowledged frame from server. 
        - the subsequent packets still has all those inputs. 


<h2 id="0be50d21cd18f6cf70ec79971504b63b"></h2>


# Mortal Kombat 

- Lockstep
    - only send gamepad data
    - the game will not proceed until it has input from the remote player for the current frame
    - input is delayed  by enough frames to cover the network latency
- Rollback
    - only send gamepad data
    - Game proceeds without remote input
    - when remote input is received , rollback and simulate forward


 · | Rollback | Lockstep
--- | --- | ---
simple | | Y
visually smooth | | Y
Performant | | Y 
Robuts | Y | Y 
Low bandwitdh | Y | Y
Responsive | Y | 
Single Frame Latency | Y | 

- High-Level Lessons Learned
    - Design game systems to drive visual state, *not* depend on it
    - Design systems to update with variable time steps
        - Parametriacally is even better
    - Everyone should work with debug rollback system enabled
    - Defer processing until after the rollback window if reasonable 
    - Bog is no longer a function of a single frame

<h2 id="aa6df57fb6fe377d80b4a257b4a92cba"></h2>


# Halo

- "The TRIBES engine networking model", Frohnmayer and Gift, GDC 1999
- A host/client model, resilient to cheating
- Protocols for semi-reliable data delivery
- Support persistent *state* and transient *events*
- Highly scalable to match available bandwidth

- UDP state sync
    - server -> client, world state, packet drop is not essential
    - client -> server, commands is essential, each command packet contains all command from the acknowledged frame.


<h2 id="0d98c74797e49d00bcc4c17c9d557a2b"></h2>


# 其他

- 通过发送 前后3帧数据，抗丢包
- 逻辑和显示的分离

http://mauve.mizuumi.net/2012/07/05/understanding-fighting-game-networking/


