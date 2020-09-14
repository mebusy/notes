...menustart

- [Python 内存测试](#9188973c8c1616026f7ac7774fbd8e52)

...menuend


<h2 id="9188973c8c1616026f7ac7774fbd8e52"></h2>


# Python 内存测试

 - install `psutil`

```python
import gc 
import os 
import psutil

def test(): 
    for i in range(10000000):
        pass


if __name__ == '__main__' :
    gc.collect()
    test()
    p = psutil.Process(os.getpid())
    mem =  p.memory_info() 
    print mem ,  mem.rss / 1024/1024  , "M used"
```

```bash
# range
pmem(rss=332668928L, vms=4710641664L, pfaults=82478, pageins=0) 317 M used

# xrange
pmem(rss=6696960L, vms=4385259520L, pfaults=2897, pageins=0) 6 M used
```


