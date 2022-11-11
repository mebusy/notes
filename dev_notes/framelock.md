[](...menustart)

- [UDP](#f5ef036b4d8b630721e51fe23489fbc9)
- [帧同步 Lockstep](#4237cc523ddf51a463a91d770ebafc75)
    - [1 客户端计算的一致性](#d5096ffe34c40c04bb3c8ebcda25887b)
    - [2 逻辑和显示分离](#71ade8c4ad1d399e5de3d4c3811320ab)
    - [3 让操作流畅](#40939848cc300fb489826d839a1243c2)
- [Lockstep VS Rollback](#16731c5804652b67d31b9d80f92e9419)
- [实现 #1 传统客户端](#8fb429f2c732df02beed40b4aee2d98a)
- [实现 #2 预测回滚](#9eafae7566ddfa5de0886c16c02cbd00)
- [Overwatch](#fcaeeb6e34b4303e99b91206bd325f2b)
- [Mortal Kombat](#0be50d21cd18f6cf70ec79971504b63b)
- [Halo](#aa6df57fb6fe377d80b4a257b4a92cba)

[](...menuend)


<h2 id="f5ef036b4d8b630721e51fe23489fbc9"></h2>

# UDP

- 问题
    1. udp包无序
    2. 丢包问题
- 解决
    1. 服务器/客户端 发送的包都带一个序号，并且对收到的包进行排序
    2. 一个简单抗丢包策略是 每次发送 前后3帧数据, 使用冗余包来抗丢包.
        - 如果还是发生了丢包， 服务器可以选择忽略，客户端必须使用 TCP API 从服务器重新拉取丢失的数据.



<h2 id="4237cc523ddf51a463a91d770ebafc75"></h2>

# 帧同步 Lockstep

几个难点。是的，都是客户端的。

<h2 id="d5096ffe34c40c04bb3c8ebcda25887b"></h2>

## 1 客户端计算的一致性

1. 浮点数计算 在不同的平台上结果不一致
    - 包括 系统提供的随机数，数学库(如:三角函数) 等等...
    - 解决方案
        1. 使用定点数取代浮点数
        2. 三角函数查表
        3. 自己实现 PRNG
    - PS. 浮点数计算的一致性在APP game中是确定存在的
        - **但是在微信小游戏 v8/JSC 虚拟机下是否存在一致性问题，有必要先做个测试**.
2. 一些容器遍历顺序的不确定性, map, dictionary 等等
    - 逻辑上 不要依赖遍历的顺序
3. 物理引擎
    - 慎重使用第三方物理引擎



<h2 id="71ade8c4ad1d399e5de3d4c3811320ab"></h2>

## 2 逻辑和显示分离

- 游戏逻辑不要依赖于动画,或其他的美术资源
- 做到脱离美术资源，一样可以跑比赛的逻辑。
- 游戏设计成 可以使用不同的 time step 进行 update


<h2 id="40939848cc300fb489826d839a1243c2"></h2>

## 3 让操作流畅

- Lockstep 模式下，客户端不能再对玩家的输入 立刻作出反应，而是在某个逻辑帧将操作发送给服务器，等到从服务器那里收到 这个逻辑帧所有玩家的操作后，执行游戏逻辑。
- 问题1: 网速慢的玩家会卡到网速快的玩家 。 
    - 解决方案: 服务器采用 乐观帧同步。
- 问题2: 对玩家输入作出反应至少需要等待一个RTT的时间,如果降低操作延迟感?
    - Predict/Rollback
        - [Understanding Fighting Game Networking](http://mauve.mizuumi.net/2012/07/05/understanding-fighting-game-networking/)
    - 开发难度非常大.
    - 客户端在感知到自己延迟增大的情况下，加速预测
    - 需要对游戏世界做快照，一旦发生回滚，使用快照立刻恢复游戏世界。
    - 真实玩家越多, Predict/Rollback 效果越差，因为预测很容易发生错误，会频繁回滚。


<h2 id="16731c5804652b67d31b9d80f92e9419"></h2>

# Lockstep VS Rollback

- Lockstep
    - 只发送玩家操作
    - 直到收到从服务器返回的所有玩家操作后，才开始处理逻辑
    - 取决于网络情况, 输入被延迟不同的时间
- Rollback
    - 只发送玩家操作
    - 不需要等待服务器的返回数据
    - 当收到了服务器的数据, 回滚并向前执行游戏逻辑


 · | Rollback | Lockstep
--- | --- | ---
简单| | Y
视觉平滑 | | Y
高效 | | Y 
低带宽 | Y | Y
反应灵敏 | Y | 
延迟 | Y | 



-------------------------------------------------



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
Robust | Y | Y 
Low bandwitdh | Y | Y
Responsive | Y | 
Single Frame Latency | Y | 

- High-Level Lessons Learned
    - Design game systems to drive visual state, *not* depend on it
    - Design systems to update with variable time steps
        - Parametriacally is even better

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

