[](...menustart)

- [Unity Prefab 研究](#78b2b08ad01c22c1f14bc8819c10dd29)
    - [空 prefab](#6d709c5dbee8c6e1d4833e35ea5ed9a3)
    - [空 prefab, 添加一个 game object](#e386fc72a64bbb6f28f320bfcc082f2a)
    - [prefab 上挂载一个空脚本后](#35ca7ecc7d43115b34d96761e3a112d7)
    - [脚本增加一个 public int aaa](#8e11a01ecccc92c779ea4236c659dacf)
        - [prefab 修改 aaa 属性的值](#d7521ff8314459d28ef10fa96c59e054)
    - [脚本添加 public GameObject bbb](#94720a7b28fb47e9d387e0e3182ce839)
    - [bbb 挂载 prefab 自身](#b4236c8d3afa787bc275008053008471)
    - [继续添加脚本 public GameObject\[\] ccc ;](#6631c7ed396f518c2bfa5571fe54398b)
    - [给 ccc\[0\] ， 挂载 prefab 自身后](#4e88c150f945c68cc53c3796fdc3c04e)
        - [ccc size 设回0](#d26305a20f7a0ecc5633081925662694)
    - [修改 ccc size 为 5](#580d91660f00d6322bd42b9483f32333)
    - [脚本中，删除 public int aaa;](#bc66081dee086ba862581d22f6a78bfb)
    - [小结](#5db9fd7c5a5554033a1f4bb7e6d86e7e)

[](...menuend)


<h2 id="78b2b08ad01c22c1f14bc8819c10dd29"></h2>

# Unity Prefab 研究

<h2 id="6d709c5dbee8c6e1d4833e35ea5ed9a3"></h2>

## 空 prefab

```
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1001 &100100000
Prefab:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Modification:
    m_TransformParent: {fileID: 0}
    m_Modifications: []
    m_RemovedComponents: []
  m_ParentPrefab: {fileID: 0}
  m_RootGameObject: {fileID: 0}
  m_IsPrefabParent: 1

```

<h2 id="e386fc72a64bbb6f28f320bfcc082f2a"></h2>

## 空 prefab, 添加一个 game object


增加 2个大的字段 `GameObject:`  和  `Transform:`

`GameObject` 字段的 `m_Component` 中有 `Transform` 的 id

```
GameObject:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 100100000}
  serializedVersion: 4
  m_Component:
  - 4: {fileID: 450296}
```


同时, `prefab` 字段的 `m_ObjectHideFlags:` 0->1 , `m_RootGameObject:` {fileID:  0 -> game object ID

```
Prefab:
  m_ObjectHideFlags: 1
  ...
  m_RootGameObject: {fileID: 101870}
```


<h2 id="35ca7ecc7d43115b34d96761e3a112d7"></h2>

## prefab 上挂载一个空脚本后

增加了一个 `MonoBehaviour:` 字段,

同时  `GameObject` 字段的 `m_Component` 增加了 `MonoBehaviour` 的 id

```
  m_Component:
  - 4: {fileID: 450296}
  - 114: {fileID: 11481900}
```


<h2 id="8e11a01ecccc92c779ea4236c659dacf"></h2>

## 脚本增加一个 public int aaa

无变化

<h2 id="d7521ff8314459d28ef10fa96c59e054"></h2>

###  prefab 修改 aaa 属性的值


MonoBehaviour 中 立刻出现了 aaa的修改：

```
MonoBehaviour:
  ...
  aaa: 5
```

同时, Prefab 中的   `m_Modification: -> m_Modifications:` 也记录了修改：

```
    m_Modifications:
    - target: {fileID: 0}
      propertyPath: aaa
      value: 5
      objectReference: {fileID: 0}
```


<h2 id="94720a7b28fb47e9d387e0e3182ce839"></h2>

## 脚本添加 public GameObject bbb

无变化


<h2 id="b4236c8d3afa787bc275008053008471"></h2>

## bbb 挂载 prefab 自身

MonoBehaviour 中:  

```
MonoBehaviour:
  ...
  aaa: 5
  bbb: {fileID: 101870}
```
  

Prefab 中:

```
    m_Modifications:
    - target: {fileID: 0}
      propertyPath: aaa
      value: 5
      objectReference: {fileID: 0}
    - target: {fileID: 0}
      propertyPath: bbb
      value: 
      objectReference: {fileID: 101870}
```

<h2 id="6631c7ed396f518c2bfa5571fe54398b"></h2>

## 继续添加脚本 public GameObject[] ccc ;

ccc size 设为 1 后

MonoBehaviour 中 增加了 :

```
  ccc:
  - {fileID: 0}
```

Prefab: 也增加了 , 纪录 ccc size 的信息

```
    m_Modifications:
    ...
    - target: {fileID: 0}
      propertyPath: ccc.Array.size
      value: 1
      objectReference: {fileID: 0}
```


<h2 id="4e88c150f945c68cc53c3796fdc3c04e"></h2>

## 给 ccc[0] ， 挂载 prefab 自身后

MonoBehaviour 中：

```
  ccc:
  - {fileID: 101870}
```

Prefab: 增加了 ：

```
    - target: {fileID: 0}
      propertyPath: ccc.Array.data[0]
      value: 
      objectReference: {fileID: 101870}
```


<h2 id="d26305a20f7a0ecc5633081925662694"></h2>

### ccc size 设回0 

MonoBehaviour: 中

```
  ccc: []
```

prefab中：

```
    - target: {fileID: 0}
      propertyPath: ccc.Array.size
      value: 1 -> 0
```

但是

```
    - target: {fileID: 0}
      propertyPath: ccc.Array.data[0]
      value: 
      objectReference: {fileID: 101870}
```

并不会消失， 也不会改变， 

这时候，size 再改为1， ccc.Array.data[0] 的信息还是不会发生任何改变，
所以 prefab 中的 m_Modifications 中 array 元素信息，可能是过期的，或者无用的。

<h2 id="580d91660f00d6322bd42b9483f32333"></h2>

## 修改 ccc size 为 5

MonoBehaviour:

```
  ccc:
  - {fileID: 0}
  - {fileID: 0}
  - {fileID: 0}
  - {fileID: 0}
  - {fileID: 0}
```

Prefab:

```
    m_Modifications:
    - target: {fileID: 0}
      propertyPath: ccc.Array.size
      value: 5
      objectReference: {fileID: 0}
```

<h2 id="bc66081dee086ba862581d22f6a78bfb"></h2>

## 脚本中，删除 public int aaa;

prefab 不发生变化，仅当 prefab 中的任意 property 发生变化，并保存后，才会同步更新所有的信息。


<h2 id="5db9fd7c5a5554033a1f4bb7e6d86e7e"></h2>

## 小结

脚本外部的修改并不会导致 prefab 发生修改， 仅当 prefab 本身发生编辑事件后，才会同步更新 外部脚本的修改到 prefab.

随意，unity 处理 prefab， 并不是完全根据prefab 文件的描述，而是需要结合外部脚本的修改情况，做相应修改。

