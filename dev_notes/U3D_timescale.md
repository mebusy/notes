...menustart

- [Time.timeScale](#052b29689e3fddb3f8de79d80f5c356f)

...menuend


<h2 id="052b29689e3fddb3f8de79d80f5c356f"></h2>


## Time.timeScale

- 受Time.timeScale影响的因素:
    1. 物理模拟. FixedUpdate 
        - 当Time.timeScale=0时，FixedUpdate 函数不会被执行。
    2. Coroutines. 
        - Time.timeScale=0 协程函数不会停止,但是会停止WaitForSeconds. 协成函数还是会每一帧都触发，但是WaitForSeconds使用的是当前的Time.deltaTime会变成0
    3. Invoke  和 InvokeRepeating. 
        - 延迟一段时间后掉用指定函数.
    4. Particle System 粒子系统.
    5. Animations.  - 动画
        - 如果我们使用的是Animator，可以设置动画忽略Time.timeScale带来的影响. 只需要把UpdateMode设置为UnScaled Time.

- 不受 Time.timeScale影响的因素:
    1. Update - Time.timeScale不会影响Update的调用
    2. OnGUI -OnGui和对应的事件实现原理不基于Time.timeScale，所以也不会受影响。

**总结**:

 1. timeScale不影响Update和LateUpdate，会影响FixedUpdate
 2. timeScale不影响Time.realtimeSinceStartup，会影响Time.timeSinceLevelLoad和Time.time
 3. timeScale不影响Time.fixedDeltaTime和Time.unscaleDeltaTime，会影响Time.deltaTime
    

当timeScale等于0时：

 1. Update和LateUpdate可以执行，FixedUpdate不可以执行
 2. Time.realtimeSinceStartup依然在增加，Time.timeSinceLevelLoad和Time.time均不变
 3. Time.fixedDeltaTime不变，Time.deltaTime变为0，Time.unscaleDeltaTime就像游戏正常速度运行下的Time.deltaTime
 

再次总结： 

- 当想代码受timeScale控制时(如暂停、加速)，可以把代码放在FixedUpdate中，又或者跟Time.time或Time.deltaTime扯上关系；
- 否则，可以用Time.realtimeSinceStartup(类似正常状态下的Time.time)和Time.unscaleDeltaTime(类似正常状态下的Time.deltaTime)

 
