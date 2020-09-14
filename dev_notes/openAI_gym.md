...menustart

- [gym](#e4d81f13f96fb9bc905f4ad89615032b)
    - [Install](#349838fb1d851d3e2014b9fe39203275)
    - [API](#db974238714ca8de634a7ce1d083a14f)
        - [Env](#aa9f9a8454a370443372f6259447844e)
        - [Observations](#263df4303fc8e2f27499caefad0c6f25)
        - [Space](#d511f8439ecde36647437fbba67a4394)
        - [Recording and uploading results](#580d8bcd9865196d4daf2e7514174d27)
        - [Evaluations](#d1ec602319f9da672ff7e6e84f8ec53d)

...menuend


<h2 id="e4d81f13f96fb9bc905f4ad89615032b"></h2>


# gym

<h2 id="349838fb1d851d3e2014b9fe39203275"></h2>


## Install 

```bash
pip install gym
pip install gym[all]
```

<h2 id="db974238714ca8de634a7ce1d083a14f"></h2>


## API

<h2 id="aa9f9a8454a370443372f6259447844e"></h2>


### Env

- reset(self):重置环境的状态，返回观察。
- step(self,action):推进一个时间步长，返回 observation，reward，done，info
- render(self,mode=’human’,close=False):重绘环境的一帧。默认模式一般比 较友好，如弹出一个窗口。


```python
import gym
env = gym.make('CartPole-v0')  # env: <TimeLimit<CartPoleEnv<CartPole-v0>>>
env.reset() # return [-0.00624315  0.00955091  0.02431831 -0.00755877]
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
    # step return: (array([ 0.02512375,  0.01964673,  0.04163345, -0.00201724]), 1.0, False, {})
```

--- 

查看所有的 env

```python
from gym import envs
print(envs.registry.all())
```




<h2 id="263df4303fc8e2f27499caefad0c6f25"></h2>


###  Observations
    
- env.step return 4 values
    - observation (object) 
        - 观察，一个与环境相关的对象描述你观察到的环境。如相 机的像素信息，机器人的角速度和角加速度，棋盘游戏中的棋盘状态
    - reward (float)
        - amount of reward achieved by the previous action.
    - done (boolean)
        - 判断是否到了重新设定(reset)环境的时刻了。done 为 true 说 明该 episode 完成
        - 需要 reset 环境
    - info(dict)
        - 用于调试的诊断信息。但是，正式的评价这不允许使用该信息进行 学习

<h2 id="d511f8439ecde36647437fbba67a4394"></h2>


### Space

我们从环境的动作空间中抽取随机动作。每个环境都带有描述有效动作和观察结果的一级Space对象：

```python
>>> print env.action_space
Discrete(2)
>>> print env.observation_space
Box(4,)
```

- Discrete space
    - allows a fixed range of non-negative numbers, so in this case valid actions are either 0 or 1.
- Box space
    - represents an n-dimensional box, so valid observations will be an array of 4 numbers. We can also check the Box's bounds:
    - 3.40282347e+38 is kind of *inf*

```python
>>> print env.observation_space.high
[  4.80000000e+00   3.40282347e+38   4.18879020e-01   3.40282347e+38]
>>> print env.observation_space.low
[ -4.80000000e+00  -3.40282347e+38  -4.18879020e-01  -3.40282347e+38]
```

introspection:

```python
from gym import spaces
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8
```

<h2 id="580d8bcd9865196d4daf2e7514174d27"></h2>


### Recording and uploading results

Gym makes it simple to record your algorithm's performance on an environment, as well as to take videos of your algorithm's learning.  Just wrap your environment with a Monitor Wrapper as follows:

```python
import gym
from gym import wrappers
env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, '/tmp/cartpole-experiment-1')
```


You can then upload your results to OpenAI Gym:

```python
import gym
gym.upload('/tmp/cartpole-experiment-1', api_key='YOUR_API_KEY')
```

<h2 id="d1ec602319f9da672ff7e6e84f8ec53d"></h2>


### Evaluations

登录 github 获取 api key



