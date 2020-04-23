...menustart

 - [High Level Datastructure In Python](#7fd56e59b5fba7ede4bdfe85d4ca3e80)
 - [1 Collections](#255caa31493a976f6d48a798880b037d)
     - [1.1 Counter()](#fdfff165187c00eddf4de38373dae439)
     - [1.2 Deque](#6a7d8a9f9964930eeb69ad32b992c975)
     - [1.3 Defaultdict](#79c19eeedbe88e9f7463649482c2d96c)
 - [2 Heapq](#accc7ea4c2626a83ee808ea519a956a1)
 - [3 Bisect](#bdcdfbb57bb9cc2e3ffde8fe201d6778)
     - [Searching Sorted Lists](#2f868162e8d150124929f479e23cbf03)
     - [Other Examples](#08b87bb6671fe3c2c92f77e4f561e7fb)
 - [4 Copy](#487df11c262ee217b21843a7dfe5d472)
 - [5 Pprint](#ec77e0a5fa7be31d129ddd57e635c4bc)

...menuend


<h2 id="7fd56e59b5fba7ede4bdfe85d4ca3e80"></h2>


# High Level Datastructure In Python 


<h2 id="255caa31493a976f6d48a798880b037d"></h2>


# 1 Collections

<h2 id="fdfff165187c00eddf4de38373dae439"></h2>


## 1.1 Counter()

 - 可以 统计一个 元素 在给定序列中 ， 一共出现了多少次
 - 类似 统计一篇文章中出现的高频次 等应用

```python
>>> from collections import Counter
>>> li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
>>> Counter(li)
Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
```

<h2 id="6a7d8a9f9964930eeb69ad32b992c975"></h2>


## 1.2 Deque 

 - double-ended queue 
    - 经过优化的append和pop操作，在队列两端的相关操作都能够达到近乎O(1)的时间复杂度
    - thread safe
 - why not list ?
    - list 在遇到 pop(0), insert(0,v) 这类既改变长度，又改变元素位置的操作时，复杂到会上升到O(n)

```python
>>> from collections import deque
>>> q = deque(xrange(5))
>>> q.append(5)
>>> q.appendleft(6)
>>> q
deque([6, 0, 1, 2, 3, 4, 5])
>>> q.pop()
5
>>> q.popleft()
6
>>> q.rotate(3) #Rotate the deque n steps to the right
>>> q
deque([2, 3, 4, 0, 1])
>>> q.rotate(-1)
>>> q
deque([3, 4, 0, 1, 2])
```

<h2 id="79c19eeedbe88e9f7463649482c2d96c"></h2>


## 1.3 Defaultdict

 - 拥有和普通dict 相同的操作 
 - 通过设定一个默认类型，当访问到不存在的 entry 时，通过 default_factory 创建一个默认值 entry

```python
>>> from collections import defaultdict
>>> defaultdict(int)
defaultdict(<type 'int'>, {})
>>> dd = defaultdict(list)
>>> dd
defaultdict(<type 'list'>, {})
>>> dd["not exist"]
[]
>>> dd
defaultdict(<type 'list'>, {'not exist': []})
```

<h2 id="accc7ea4c2626a83ee808ea519a956a1"></h2>


# 2 Heapq


```python
>>> import heapq
>>> heap = []
>>> for value in [20, 10, 30, 50, 40]:
...     heapq.heappush(heap, value)
... 
>>> while heap:
...     print heapq.heappop(heap)
... 
10
20
30
40
50
```

 - 两个非常重要的模块函数，可以直接对 list 使用
    - `heapq.nlargest()`
    - `heapq.nsmallest`
    - 还可以带 lambda 函数，完成更复杂的功能

```python
>>> import heapq
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heapq.nlargest(3, nums)
[42, 37, 23]
>>> heapq.nsmallest(3, nums)
[-4, 1, 2]
```

##  Priority Queue 

<details>
<summary>
一个优先级队列的例子,每次pop操作都返回优先级最高的元素
</summary>

```python
class PriorityQueue:                                                            
    def  __init__(self):                                                        
        self.heap = []                                                          
        self.count = 0                                                          
                                                                                
    def push(self, item, priority):
        # self.count is added for stable ?                                      
        entry = (priority, self.count, item)                                    
        heapq.heappush(self.heap, entry)                                        
        self.count += 1                                                         
                                                                                
    def pop(self):                                                              
        return heapq.heappop(self.heap)[-1]
                                                                                
    def isEmpty(self):                                                          
        return len(self.heap) == 0                                              
```

</details>


<details>
<summary>
python official implementation , 通过标记删除再添加的方式，实现更新优先级
</summary>

```python
import itertools
import heapq

REMOVED = '<removed-task>'      # placeholder for a removed task


class PriorityQueue():

    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count

    def add(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq :
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


if __name__ == '__main__':
    import random

    for _ in range(1000):
        samples = random.sample(range(1000), k=60)
        s_min = min(samples)
        s_max = max(samples)
        pq = PriorityQueue()
        for v in samples :
            pq.add( v,v )
        assert s_min == pq.pop()
        # update
        pq.add( s_max , -3 )
        assert s_max == pq.pop()
```

</details>

<h2 id="bdcdfbb57bb9cc2e3ffde8fe201d6778"></h2>


# 3 Bisect

 - 提供 保持list 元素序列的支持，使用了二分法完成大部分的工作
 - 保持有序插入

```python
>>> import bisect
>>> a = [(0, 100), (150, 220), (500, 1000)]  # bisect assume a is sorted
>>> bisect.insort_right(a, (250,400)) # right means add to the right of the rightmost x
>>> a
[(0, 100), (150, 220), (250, 400), (500, 1000)]
```

 - `bisect.bisect`  寻找插入点
    - 注意：不是寻找元素位置

```python
>>> bisect.bisect(a , (150, 220) )
2
>>> bisect.bisect(a , (777, 220) )
4
```

<h2 id="2f868162e8d150124929f479e23cbf03"></h2>


##  Searching Sorted Lists

The above bisect() functions are useful for finding insertion points but can be tricky or awkward to use for common searching tasks. The following five functions show how to transform them into the standard lookups for sorted lists:


```python
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
```


<h2 id="08b87bb6671fe3c2c92f77e4f561e7fb"></h2>


## Other Examples

The bisect() function can be useful for numeric table lookups.

This example uses bisect() to look up a letter grade for an exam score (say) based on a set of ordered numeric breakpoints: 90 and up is an ‘A’, 80 to 89 is a ‘B’, and so on:

```python
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect(breakpoints, score)
        return grades[i]

>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```


<h2 id="487df11c262ee217b21843a7dfe5d472"></h2>


# 4 Copy 

```python
>>> import copy
>>> # shallow copy
>>> d = copy.copy(c)
>>> # deep copy 
>>> d = copy.deepcopy(c)
```


<h2 id="ec77e0a5fa7be31d129ddd57e635c4bc"></h2>


# 5 Pprint 

 - 提供比较优雅的数据结构打印方式
 - 可用于打印 层次较深的字典或是JSON对象
 - 或用来漂亮的打印 matrix

```python
>>> import pprint
>>> matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
>>> pp = pprint.PrettyPrinter(width=20)
>>> pp.pprint( matrix )
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```




