...menustart

- [PyTorch](#95b88f180e9eb5678e0f9ebac2cbe643)

...menuend


<h2 id="95b88f180e9eb5678e0f9ebac2cbe643"></h2>


# PyTorch

- [official tutorial](https://pytorch.org/tutorials/)
- [Understanding PyTorch with an example](pytorch_example.md)


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
