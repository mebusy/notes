...menustart

- [PyTorch](#95b88f180e9eb5678e0f9ebac2cbe643)
    - [Docker](#c5fd214cdd0d2b3b4272e73b022ba5c2)

...menuend


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




## Tips


 what  | how 
--- | ---
create Layer |  `self.fc1 = nn.Linear(input_size, hidden_size)`
init weights |  `nn.init.kaiming_normal_(self.fc1.weight)`
iint bias  | `nn.init.constant_(self.conv1.bias, 0)`
chain forward | `scores = self.fc2(F.relu(self.fc1(x)))`
stack model |  model = nn.Sequential( Flatten(), <br>nn.Linear(3 * 32 * 32, hidden_layer_size), <br>nn.ReLU(), <br>nn.Linear(hidden_layer_size, 10),<br>)


