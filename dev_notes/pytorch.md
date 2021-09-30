...menustart

- [PyTorch](#95b88f180e9eb5678e0f9ebac2cbe643)
    - [Docker](#c5fd214cdd0d2b3b4272e73b022ba5c2)

...menuend


<h2 id="95b88f180e9eb5678e0f9ebac2cbe643"></h2>


# PyTorch

- [official tutorial](https://pytorch.org/tutorials/)
- [Understanding PyTorch with an example](pytorch_example.md)


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
