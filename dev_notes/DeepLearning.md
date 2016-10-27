
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

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
```
