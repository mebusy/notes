
# Deep Learning 

The way to turn scores into probabilities is to use **softmax** function , will be denoted by *S*. It can take any kind of scores and turn them into proper probabilities. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_softmax.png)

> scores -> probabilities

Proper probabilities , sum to 1.


```python
"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum( np.exp(x) , axis = 0 )


print(softmax(scores))
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DL_softmax_graph.png)


Caution:

 1. if we multiply scores by 10 , then probabilities get close to either 0.0 or 1.0
 2. if we divide scored by 10 , probabilities get close to the uniform distribution.

