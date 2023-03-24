
# Bash

## Common

- `;`
    - bash在解析字符的时候，对待“;”跟看见回车是一样的行为
- `[ ... ]`
    - 其实就是个shell test命令的另一种写法
    - 命令加参数要用空格分隔, 所以 `[ ... ]` 需要加空格
- `[[ ... ]]`
    - a *Bash extension* , bash, zsh, yash support it
    - `bash` built-in, and cannot be used in a `#!/bin/sh` script
    - benefits
        - `==` and `!=` perform pattern matching, so the right-hand side can be a glob pattern
            ```bash
            $ [[ abc = *bc ]] ; echo $?
            0
            ```
        - `=~` performs regular expression matching. Captured groups are stored in the `BASH_REMATCH` array.
        - boolean operators `&&` and `||`
        - no word splitting, so it's not strictly necessary to quote your variables.
    - drawback:
        - your script is now bash-specific.
- `(...)`
    - indicate a *subshell*
    - What's inside is a list of commands (just like outside parentheses)
    - These commands are executed in a separate subprocess, 
        - so any redirection, assignment, etc. performed inside the parentheses has **NO EFFECT** outside the parentheses.
    - With a leading dollar sign, `$(…)` is a command substitution
    - the output from the command is used as part of the command line
- `((...))`
    - double parentheses surround an *arithmetic instruction*
    - mostly used for assignments and in conditionals. This only exists in ksh/bash/zsh, not in plain sh.
    - The same syntax is used in arithmetic expressions `$((…))`, which expand to the integer value of the expression.
- list
    - 若干shell命令组成的序列， 使用 `管道`，`;`，`&` ，`&&` ，`||` 这些符号串联起来
- 一切皆表达式
    - shell在执行任何东西（注意是任何东西，不仅是命令）的时候都会有一个 return status
    - 0-255
        - 0为真（true）
        - 非0为假（false）
    - `echo $?` 来查看上一个执行命令的返回值
- `!`
    - 对表达式求反
- bash 通配符
    - `?` 单个字符
    - `*` 任意数量的字符
    - `[...]`  类似正则表达式中的`[]`
- `$` 变量
    - `$0` 获得自己执行命令的进程名称
    - `$n` 第n个参数
    - `$#` 参数个数
    - `$*`, `$@` holds list of all arguments passed to the script
        - There is no difference if you do NOT put `$*` or `$@` in quotes.
        - But if you put them inside quotes (which you should, as a general good practice), 
            - then `$@` will pass your parameters as separate parameters, 
            - whereas `$*` will just pass all params as a single parameter.
        - https://stackoverflow.com/questions/22589032/what-is-the-difference-between-and
    - `$?` 上一个命令的返回值
    - 所以上述所有取值都可以写成`${x}`的方式

## if

```bash
if list; then list; elif list; then list; ... else list; fi
```

等价于

```bash
if list
then 
  list
elif list
then 
  list
... 
else 
  list
fi
```

- if 后面跟的就是个shell命令
    - return status 作为 condition (0 is true)
    - `if cd mydir; then ...`
- if语法中 后面最常用的命令就是 `[]`
    - `if [ $ret -eq 0 ] ...`
    - 等价于 `if test $ret -eq 0 ...`


## while / until

```bash
while list-1
do
    list-2
done

until list-1
do
    list-2
done
```

- `while list-1; do list-2; done`
- `until list-1; do list-2; done`

## case

```bash
case EXPRESSION in

  PATTERN_1)
    STATEMENTS
    ;;

  PATTERN_2)
    STATEMENTS
    ;;

  PATTERN_N)
    STATEMENTS
    ;;

  *)
    STATEMENTS
    ;;
esac
```

## for loop

```bash
for VARIABLE in LIST
do
    command1
    command2
done
```

- while `LIST` could be
    1. `for VARIABLE in 1 2 3 4 5 .. N`
    2. `for VARIABLE in file1 file2 file3`
    3. `for OUTPUT in $(Linux-Or-Unix-Command-Here)`
    4. `for i in {1..5}`
        - bash3.0+

C-sytle syntax

```bash
for (( initializer; condition; step ))
do
  shell_COMMANDS
done
```

e.g.

```bash
for (( c=1; c<=5; c++ ))
do
   echo "Welcome $c times"
done
```


## select

```bash
select i in a b c d
do
    echo $i
done
```

提供给了我们一个构建交互式菜单程序的方式

<details>

```bash
$ ./select.sh
1) a
2) b
3) c
4) d
#?


#!/bin/bash
select i in a b c d
do
    case $i in
        a)
        echo "Your choice is a"
        ;;
        b)
        echo "Your choice is b"
        ;;
        c)
        echo "Your choice is c"
        ;;
        d)
        echo "Your choice is d"
        ;;
        *)
        echo "Wrong choice! exit!"
        exit
        ;;
    esac
done
```

</details>

## continue / break

内建命令，并不是关键字




