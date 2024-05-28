[](...menustart)

- [Python3 tips](#a1f4779bb48ab8eccef9c7430a8f591e)
    - [Print Colored Output](#574083d4ce2c240d64205f07595f82c4)
    - [Yaml, References Variables , and Concat Strings](#37fde4cf4b72158aff18de1784ec0f23)
    - [remove single-line / multiple-line comments](#2ff3865f3455ca50e9de317f1c7851ea)
    - [defaultdict tree](#7a652adbada4c294364e2c3c61fb5c25)
    - [lru_cache](#89dd193fac1729cebfd50aff749b688c)

[](...menuend)


<h2 id="a1f4779bb48ab8eccef9c7430a8f591e"></h2>

# Python3 tips


<h2 id="574083d4ce2c240d64205f07595f82c4"></h2>

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


<h2 id="37fde4cf4b72158aff18de1784ec0f23"></h2>

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


<h2 id="2ff3865f3455ca50e9de317f1c7851ea"></h2>

## remove single-line / multiple-line comments

```python
import re

RE_COMMENTS = re.compile(
    r"""
    (^)?            # match comment starts at the beginning of a line, as long as the MULTILINE-flag is used.
    [^\S\n]*        # match any whitespace character except newline.
                    # We don't want to match line breaks if the comment starts on it's own line.
    /               # comments start /
        (?:             # Non-capturing start
            \*(.*?)\*/[^\S\n]*          # match multiline comments
            |/[^\n]*                    # single line comment
        )               # Non-capturing end
    ($)?        # match if the comment stops at the end of a line, as long as the MULTILINE-flag is used.
    """,
    re.DOTALL | re.MULTILINE | re.VERBOSE,
)


def comment_replacer(match):
    start, mid, end = match.group(1, 2, 3)
    if mid is None:
        # single line comment
        return ""
    elif start is not None or end is not None:
        # multi line comment at start or end of a line
        return ""
    elif "\n" in mid:
        # multi line comment with line break
        return "\n"
    else:
        # multi line comment without line break
        return " "


# usage: data = remove_comments(data)
def remove_comments(text):
    return RE_COMMENTS.sub(comment_replacer, text)
```


<h2 id="7a652adbada4c294364e2c3c61fb5c25"></h2>

## defaultdict tree

```python
from collections import defaultdict
import json

def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))
```

```bash
# output
{
    "Page": {
        "Python": {
            "defaultdict": {
                "Title": "Using defaultdict",
                "Subtitle": "Create a tree"
            }
        },
        "Java": null
    }
}
```

<h2 id="89dd193fac1729cebfd50aff749b688c"></h2>

## lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
```


## cgi server

CGIHTTPRequestHandler

```bash
python -m http.server --cgi 
```

- This defaults to ['/cgi-bin', '/htbin'] and describes directories to treat as containing CGI scripts.


## open a link in webbrowser

```bash
python -m webbrowser [-t|-n] <url>
```


