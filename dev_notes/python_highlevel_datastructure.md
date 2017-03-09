

# High Level Datastructure In Python 


# 1 Collections

## 1.1 Counter()

 - 可以 统计一个 元素 在给定序列中 ， 一共出现了多少次
 - 类似 统计一篇文章中出现的高频次 等应用

```python
>>> from collections import Counter
>>> li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
>>> Counter(li)
Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
```

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

# 2 Heapq

 - priority queue , implemented by heap 

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

 - 一个优先级队列的例子,每次pop操作都返回优先级最高的元素

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

# 4 Copy 

```python
>>> import copy
>>> # shallow copy
>>> d = copy.copy(c)
>>> # deep copy 
>>> d = copy.deepcopy(c)
```


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




