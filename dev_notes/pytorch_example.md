
# Understanding PyTorch with an example

[Understanding PyTorch with an example: a step-by-step tutorial](https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e)

## A Simple Regression Problem

a linear regression with a single feature x

```octave
y = a + bx + ε
```

## Data Generation

Let’s start generating some synthetic data:  100 points for our feature x and create our labels ,

using **a = 1, b = 2** and some Gaussian noise.

Next, let’s split our synthetic data into train and validation sets, shuffling the array of indices and using the first 80 shuffled points for training.

```python
def data_gen():
    # Data Generation
    np.random.seed(42)

    a,b = 1,2
    x = np.random.rand(100, 1)
    y = a + b * x + .1 * np.random.randn(100, 1)

    # Shuffles the indices
    idx = np.arange(100)
    np.random.shuffle(idx)

    # Uses first 80 random indices for train
    train_idx = idx[:80]
    # Uses the remaining indices for validation
    val_idx = idx[80:]

    # Generates train and validation sets
    x_train, y_train = x[train_idx], y[train_idx]
    x_val, y_val = x[val_idx], y[val_idx]

    return x_train, y_train , x_val, y_val
```

![](https://miro.medium.com/max/1400/1*SsuTZ1y-pWikYJcaMnZgag.png)


## PyTorch

### Loading Data, Devices and CUDA

- numpy → CPU tensor
    - [from_numpy()](https://pytorch.org/docs/stable/torch.html#torch.from_numpy)
- CPU tensor → GPU tensor
    - [to()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.to)
    - [cuda.is_available()](https://pytorch.org/docs/stable/cuda.html?highlight=is_available#torch.cuda.is_available) to find out whether you have a GPU
- tensor -> float32 tensor
    - [float()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.float)

```python
import torch
import torch.optim as optim
import torch.nn as nn
from torchviz import make_dot

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Our data was in Numpy arrays, but we need to transform them into PyTorch's Tensors
# and then we send them to the chosen device
x_train_tensor = torch.from_numpy(x_train).float().to(device)
y_train_tensor = torch.from_numpy(y_train).float().to(device)

# Here we can see the difference - notice that .type() is more useful
# since it also tells us WHERE the tensor is (device)
print(type(x_train), type(x_train_tensor), x_train_tensor.type())
```



