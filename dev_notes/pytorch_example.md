
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

data from | data to | method | comments
--- | --- | --- | ---
numpy | cpu tensor | [from_numpy()](https://pytorch.org/docs/stable/torch.html#torch.from_numpy) |
cpu tensor | gpu tensor | [to()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.to) | [cuda.is_available()](https://pytorch.org/docs/stable/cuda.html?highlight=is_available#torch.cuda.is_available) to find out whether you have a GPU
cpu tensor | to float32 | [float()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.float) |
cpu tensor | numpy | [numpy()](https://pytorch.org/docs/stable/tensors.html?highlight=numpy#torch.Tensor.numpy) | you can convert CUDA(GPU) tensor to numpy
gpu tensor | cpu tensor | [cpu()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.cpu) | 


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
# <class 'numpy.ndarray'> <class 'torch.Tensor'> torch.FloatTensor
```

### Creating Parameters


- Initializes parameters "a" and "b" randomly
    - set `requires_grad=True` tells PyTorch we want it to compute gradients for us.
    ```python
    a = torch.randn(1, requires_grad=True, dtype=torch.float)
    b = torch.randn(1, requires_grad=True, dtype=torch.float)
    print(a, b)
    # tensor([-0.5836], requires_grad=True) tensor([-0.7957], requires_grad=True)
    ```
- if we want to run it on a GPU
    ```python
    a = torch.randn(1, dtype=torch.float).to(device)
    b = torch.randn(1, dtype=torch.float).to(device)
    # and THEN set them as requiring gradients...
    a.requires_grad_()
    b.requires_grad_()
    ```
- or specify the device at the moment of creation -- RECOMMENDED! 
    ```python
    a = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
    b = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
    ```

In PyTorch, every method that ends with an underscore (_) makes changes **in-place**, meaning, they will modify the underlying variable.


### Autograd


