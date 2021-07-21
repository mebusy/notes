# Python3 tips


## Print Colored Output

solution 1: use `colorma`

```python
import colorama
from colorama import Fore, Style
print(Fore.BLUE + "Hello World" + Style.RESET_ALL + "ccc" )
# or
print(f"{Fore.BLUE}Hello World{Style.RESET_ALL}ccc")
```

Style.RESET_ALL is used to reset all color settings

---

solution 2: use `sys.stderr` / `sys.stdout` 

```python
import sys

# Colored printing functions for strings that use universal ANSI escape sequences.
# fail: bold red, pass: bold green, warn: bold yellow, 
# info: bold blue, bold: bold white

class ColorPrint:

    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)
```


## Yaml, References Variables , and Concat Strings

```yaml
ENV: &env "dev"  # &env to create a node

namespace: !join [ "my-ns-" , *env ]  # use *env to dereference, and 
                                      # use customized `!join` to concat 2 parts
```


```python
import yaml

def loadconf():
    ## define custom tag handler
    def join(loader, node):
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])

    ## register the tag handler
    yaml.add_constructor('!join', join)

    # load conf
    with open("./conf.yaml") as fp:
        conf = yaml.load(fp.read(), Loader=yaml.FullLoader  )  # , Loader=yaml.SafeLoader
```

