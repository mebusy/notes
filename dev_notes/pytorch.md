[](...menustart)

- [PyTorch](#95b88f180e9eb5678e0f9ebac2cbe643)
    - [Docker](#c5fd214cdd0d2b3b4272e73b022ba5c2)
    - [Tips](#a0d4cc0f54602c3f247c72f15a7d2dbf)

[](...menuend)


<h2 id="95b88f180e9eb5678e0f9ebac2cbe643"></h2>

# PyTorch

- [official tutorial](https://pytorch.org/tutorials/)
- [Understanding PyTorch with an example](pytorch_example.md)
- Justin Johnson has made an excellent [tutorial with examples](https://github.com/jcjohnson/pytorch-examples) for PyTorch on Github
- [cheate sheet](https://pytorch.org/tutorials/beginner/ptcheat.html)


<h2 id="c5fd214cdd0d2b3b4272e73b022ba5c2"></h2>

## Docker

```bash
function pytorch() {
    docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/workspace --pids-limit 16384 pytorch/pytorch:latest python3 $@
}
```

usage:

```bash
$ pytorch ex.py
```




<h2 id="a0d4cc0f54602c3f247c72f15a7d2dbf"></h2>

## Tips


 what  | how 
--- | ---
create Layer |  `self.fc1 = nn.Linear(input_size, hidden_size)`
init weights |  `nn.init.kaiming_normal_(self.fc1.weight)`
iint bias  | `nn.init.constant_(self.conv1.bias, 0)`
chain forward | `scores = self.fc2(F.relu(self.fc1(x)))`
stack model |  model = nn.Sequential( Flatten(), <br>nn.Linear(3 * 32 * 32, hidden_layer_size), <br>nn.ReLU(), <br>nn.Linear(hidden_layer_size, 10),<br>)


## Tutorial

https://www.youtube.com/watch?v=c36lUUr864M&t=1s

https://github.com/patrickloeber/pytorchTutorial

### Tensor

1. in-place operation
    - in-place method is suffixed with `_`
    ```python
    x = torch.randn(1)
    y = torch.randn(1)
    x.add_(y)
    ```
2. extract value from tensor
    ```python
    x = torch.randn(1)  # tensor([0.1234])
    x.item()  # 0.1234
    ```
3. re-shape
    ```python
    x = torch.randn(4, 4)
    y = x.view(16)
    z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
    ```
4. convert between numpy and tensor
    ```python
    a = torch.ones(5)
    b = a.numpy()
    ```
    ```python
    a = np.ones(5)
    b = torch.from_numpy(a)
    ```
    - if tensor is on CPU, they share the same memory
    - if tensor is on GPU, you need to move it to CPU first
        ```python
        a = torch.ones(5, dtype=torch.float16)
        a = a.cuda()  # a = a.to('cuda') | a = a.to('mps')
        # a is on GPU, move it to cpu and convert to numpy
        b = a.cpu().numpy()


---

### Autograd

- `requires_grad=True` to track computation
- `backward()` to compute gradient
- `grad` to get gradient
    ```python
    x = torch.randn(3, requires_grad=True)
    y = x + 2 # tensor([2.3538, 2.1904, 1.6464], grad_fn=<AddBackward0>)
    z = y * y * 2 # tensor([11.0805,  9.5954,  5.4214], grad_fn=<MulBackward0>)
    out = z.mean() # tensor(8.6991, grad_fn=<MeanBackward0>)
    out.backward() # dout/dx,  backward() should need a vector argument if out is not scalar
    x.grad  # tensor([3.1384, 2.9205, 2.1952])
    ```    
- 3 ways to stop tracking gradient
    1. `x.requires_grad_(False)`
    2. `x.detach()`
    3. wrap within `with torch.no_grad():` 
- after backward, `x.grad` accumulates gradient, so you need to zero it before next iteration
    ```python
    x.grad.zero_()
    ```
    - noramlly you may use optimizer to do this, `optimizer.zero_grad()`
- `Function` to define custom autograd function


--- 

### Logistic Regression

- zero mean and unit variance is always recommended when dealing with logistic regression
    ```python
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    ```


### TensorBoard

```bash
# run tensorboard server
tensorboard --logdir=runs 
```

example 

```python
############## TENSORBOARD ########################
from torch.utils.tensorboard import SummaryWriter
# default `log_dir` is "runs" - we'll be more specific here
writer = SummaryWriter('runs/mnist1')
###################################################

# add image
writer.add_image('mnist_images', img_grid)

# add graph
writer.add_graph(model, example_data.reshape(-1, 28*28).to(device))

# in training epoch loop
            writer.add_scalar('training loss', running_loss / 100, epoch * n_total_steps + i)
            running_accuracy = running_correct / 100 / predicted.size(0)
            writer.add_scalar('accuracy', running_accuracy, epoch * n_total_steps + i)


# result
    ############## TENSORBOARD ########################
    classes = range(10)
    for i in classes:
        labels_i = class_labels == i
        preds_i = class_preds[:, i]
        writer.add_pr_curve(str(i), labels_i, preds_i, global_step=0)
        writer.close()  # should n't be out side of loop ?
    ###################################################
```


### Save & Load Modelsave 

=== Complete model (Lazy)===

```python
torch.save(model, 'model.pth')

model = torch.load('model.pth')
model.eval()
```

=== State Dict ===

```python
arg=model.state_dict()
# use python's pickle module to serialize the model
torch.save(arg, 'model.pth')

arg=torch.load('model.pth')
model.load_state_dict(arg)
model.eval()
```

### Transfer Learning

```python
# Load pre-trained model
model = models.resnet18(pretrained=True)
# exchange the last FC layer
num_ftrs = model.fc.in_features
# create a new layer
model.fc = nn.Linear(num_ftrs, 2)
...
```

