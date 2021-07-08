
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

- how do we tell PyTorch to do "auto-grad" ?
    - [backward()](https://pytorch.org/docs/stable/autograd.html#torch.autograd.backward)
    - invoke `loss.backward()`
- What about the actual values of the gradients? 
    - We can inspect them by looking at the [grad](https://pytorch.org/docs/stable/autograd.html#torch.Tensor.grad) attribute of a tensor.
- PS. **the gradients are accumulated**
    - So, every time we use the gradients to update the parameters, we need to zero the gradients afterwards.
    - [zero_()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.zero_)

```python
    lr = 1e-1
    n_epochs = 1000

    torch.manual_seed(42)
    a = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
    b = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)

    for epoch in range(n_epochs):
        yhat = a + b * x_train_tensor
        error = y_train_tensor - yhat
        loss = (error ** 2).mean()

        # No more manual computation of gradients!
        # a_grad = -2 * error.mean()
        # b_grad = -2 * (x_tensor * error).mean()

        # We just tell PyTorch to work its way BACKWARDS from the specified loss!
        loss.backward()
        # Let's check the computed gradients...
        print(a.grad)
        print(b.grad)

        # What about UPDATING the parameters? Not so fast...

        # FIRST ATTEMPT
        # AttributeError: 'NoneType' object has no attribute 'zero_'
        #   reassigning the update results to our parameters lost the gradient
        # a = a - lr * a.grad
        # b = b - lr * b.grad
        # print(a)

        # SECOND ATTEMPT
        # RuntimeError: a leaf Variable that requires grad has been used in an in-place operation.
        #   python is gonna build a dynamic computation graph from every Python operation 
        #   that involves any gradient-computing tensor or its dependencies.
        # a -= lr * a.grad
        # b -= lr * b.grad

        # THIRD ATTEMPT
        # We need to use NO_GRAD to keep the update out of the gradient computation
        # Why is that? It boils down to the DYNAMIC GRAPH that PyTorch uses...
        #   no_grad() allows us to perform regular Python operations on tensors, 
        #   independent of PyTorch’s computation graph.
        with torch.no_grad():
            a -= lr * a.grad
            b -= lr * b.grad

        # PyTorch is "clingy" to its computed gradients, we need to tell it to let it go...
        a.grad.zero_()
        b.grad.zero_()

    print(a, b)

# tensor([1.0235], requires_grad=True) tensor([1.9690], requires_grad=True)
```

### Dynamic Computation Graph

[PyTorchViz](https://github.com/szagoruyko/pytorchviz) package and its `make_dot(variable)` method allows us to easily visualize a graph associated with a given Python variable.

```python
from torchviz import make_dot
...

    make_dot(yhat)
```

### Optimizer

So far, we’ve been **manually** updating the parameters using the computed gradients. 

That’s probably fine for two parameters… but what if we had a whole lot of them?!

We use one of PyTorch’s **optimizers**, like [SGD](https://pytorch.org/docs/stable/optim.html#torch.optim.SGD) or [Adam](https://pytorch.org/docs/stable/optim.html#torch.optim.Adam).

- An optimizer takes 
    - the **parameters** we want to update,
    - the **learning rate** we want to use,  (and possibly many other hyper-parameters as well!) 
    - and performs the updates through its [step()](https://pytorch.org/docs/stable/optim.html#torch.optim.Optimizer.step) method.

Besides, we also don’t need to zero the gradients one by one anymore. We just invoke the optimizer’s [zero_grad()](https://pytorch.org/docs/stable/optim.html#torch.optim.Optimizer.zero_grad) method and that’s it!

```python
    torch.manual_seed(42)
    # parameters
    a = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
    b = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)

    lr = 1e-1
    n_epochs = 1000

    # Defines a SGD optimizer to update the parameters
    optimizer = optim.SGD([a, b], lr=lr)

    for epoch in range(n_epochs):
        yhat = a + b * x_train_tensor
        error = y_train_tensor - yhat
        loss = (error ** 2).mean()

        loss.backward()

        # No more manual update!
        # with torch.no_grad():
        #     a -= lr * a.grad
        #     b -= lr * b.grad
        optimizer.step()

        # No more telling PyTorch to let gradients go!
        # a.grad.zero_()
        # b.grad.zero_()
        optimizer.zero_grad()

    print(a, b)
```



