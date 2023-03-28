[](...menustart)

- [Bash](#7024ff0860dec6ab1519a3f71c7d8779)
    - [Common](#d13bc5b68b2bd9e18f29777db17cc563)
    - [if](#39c8942e1038872a822c0dc75eedbde3)
    - [while / until](#8ec47e29c787d7e06995e367d36ae96c)
    - [case](#cd14c323902024e72c850aa828d634a7)
    - [for loop](#9a499caceec56c05b0f6d0b9dc864f45)
    - [select](#99938282f04071859941e18f16efcf42)
    - [continue / break](#2278dab81c22a2a29d9f84d9a618ad33)
    - [built-in commands](#09a03771d1d8425ee09a0543cb085691)
    - [Execution](#8f44785c8c19412c5b6611db30984514)
    - [环境变量](#3867e350ebb33a487c4ac5f7787e1c29)
    - [常用环境变量](#3d07adb9606ee94b6396caf87b7d6885)
    - [redirection](#94a83445293b766bbc8eced03aeca4bd)
    - [pipeline](#99f6f4be0908f24bb4a22a4ffb277da4)
    - [数组操作](#b2cd6f460120d71c5dba4731c34dee64)
    - [扩展](#2dc90225b8033d17c41b08f39fa42de2)
        - [大括号扩展](#745adcbbabbc720ab0eba67b1fb06fbc)
        - [变量扩展](#afbb26efcbdb6a4c1c6a481099d27ea3)

[](...menuend)


<h2 id="7024ff0860dec6ab1519a3f71c7d8779"></h2>

# Bash

<h2 id="d13bc5b68b2bd9e18f29777db17cc563"></h2>

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

<h2 id="39c8942e1038872a822c0dc75eedbde3"></h2>

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


<h2 id="8ec47e29c787d7e06995e367d36ae96c"></h2>

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

<h2 id="cd14c323902024e72c850aa828d634a7"></h2>

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

<h2 id="9a499caceec56c05b0f6d0b9dc864f45"></h2>

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


<h2 id="99938282f04071859941e18f16efcf42"></h2>

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

<h2 id="2278dab81c22a2a29d9f84d9a618ad33"></h2>

## continue / break

内建命令，并不是关键字


<h2 id="09a03771d1d8425ee09a0543cb085691"></h2>

## built-in commands

- source, or `.`
    - 读取文件的内容，并在当前bash环境下将其内容当命令执行
- read
    - 从 标准输入读取输字符串到一个变量中
        - `read -p "Login: " username`
    - 读取到数组中
        - `read -a test`
- mapfile
    - 将一个文本文件直接变成一个数组，每行作为数组的一个元素
- readarray
    - 同上
    - 如果内建命令放到管道环境中执行，那么bash会给它创建一个subshell进行处理。于是创建的数组实际上与父进程没有关系
- printf
    - 进行格式化输出
- getopts
    - 命令行参数处理


<h2 id="8f44785c8c19412c5b6611db30984514"></h2>

## Execution

- 优先级
    - alias
    - keyword
    - function
    - built-in commands  (cd, pwd, etc...)
    - hash (用hash命令可以查看 hash情况)
    - external commands
- you can use `type` to check whether a command is built-in, external, alias, or etc.
    ```bash
    $ type pwd
    pwd is a shell builtin
    $ type docker
    docker is /usr/local/bin/docker
    $ type myfind
    myfind is a shell function from /Users/xxx/.myProfile
    ```
- 脚本的退出
    - built-in command `exit` , 人为指定退出的返回码是多少
    - 如果不使用exit 指定，使用最后执行命令的返回码
- 调试
    - `-v` 可视模式, 执行bash程序的时候将要执行的内容也打印出来
    - `-x` 跟踪模式(xtrace),  跟踪各种语法的调用，并打印出每个命令的输出结果
    - `-n` 检查bash的语法错误, 不会真正执行bash脚本
    - `-e` 脚本命令执行错误的时候直接退出

<h2 id="3867e350ebb33a487c4ac5f7787e1c29"></h2>

## 环境变量

- `env`
    - 查看当前bash已经定义的环境变量
- `aaa=100`
    - 这是个一般变量，不能被子进程继承
- `export`
    - 可以将一个一般变量转成环境变量
    - `export aaa`

<h2 id="3d07adb9606ee94b6396caf87b7d6885"></h2>

## 常用环境变量

- 进程信息
    - HOSTNAME
    - HOSTTYPE
    - OLDPWD / PWD
    - HOME
    - SHELL
    - BASHPID
    - UID / EUID
    - GROUPS  用户组
    - PPID  父进程PID
- RANDOM
    - 得到一个0-32767的随机数
        ```bash
        echo $RANDOM
        24746
        ```
- ulimit
    - 查看和设置bash环境中的资源限制
    - `ulimit -a`


<h2 id="94a83445293b766bbc8eced03aeca4bd"></h2>

## redirection

- shell在产生一个新进程后，新进程的前三个文件描述符都默认指向三个相关文件
    - 0 stdin
    - 1 stdout
    - 2 stderr
- stdin redirection
    - 可以读取其他终端输入
    - `cat < /dev/pts/3`
- stdout redirection
    - `>`
- stderr redirection
    - `2>`
- 常见用法
    - 只看报错信息
        - `xxx > /dev/null`
    - 只看正确输出
        - `xxx 2> /dev/null`
    - 所有输出都不看
        - `xxx &> /dev/null`
        - or `xxx >& /dev/null`
    - 将标准报错输出，重定向到和标准输出相同的地方
        - `xxx 2>&1`
        - `&1` 表示 引用 fd 1
    - 从描述符3读取
        - `3<`


<h2 id="99f6f4be0908f24bb4a22a4ffb277da4"></h2>

## pipeline

- `|`
    - `command1 | command2`
    - 将command1的stdout跟command2的stdin 通过管道(pipe)连接起来
- `|&`
    - `command1 |& command2`
    - 将command1 stdout 和 stderr 都跟command2的和stdin连接起来
    - `command1 2>&1 | command2` 的简写方式


<h2 id="b2cd6f460120d71c5dba4731c34dee64"></h2>

## 数组操作

- 定义数组
    - `declare -a array`
- 元素赋值
    - `array[0] = 1000`
- 取值
    - `${array[0]}`
    - `${array[*]}`   (get all)
    - `${#array[*]}`  (数组长度)
- 定义一个关键数组
    - `declare -A array`


<h2 id="2dc90225b8033d17c41b08f39fa42de2"></h2>

## 扩展

<h2 id="745adcbbabbc720ab0eba67b1fb06fbc"></h2>

### 大括号扩展

```bash
$ {a,b,c,d}{1,2,3,4}
a1 a2 a3 a4 b1 b2 b3 b4 c1 c2 c3 c4 d1 d2 d3 d4

$ {a,c}.conf
a.conf c.conf
```

<h2 id="afbb26efcbdb6a4c1c6a481099d27ea3"></h2>

### 变量扩展

- `:-` A or 1000
    - `${aaa:-1000}`
- `:=` A or A=1000
    - `${aaa:=1000}`
- Slice
    - `${aaa:10:5}`
        - aaa[10:15]，`[start:length]`
    - `${aaa:10}`
        - aaa[10:]
    - `${aaa: -5}`
        - aaa[:-5] 注意负号 前面的空格
    - `${#aaa}`
        - 变量值的长度
    - `${aaa#pattern}`
        - remove pattern
        - 从左往右, 从头**match** 到第一个 `^pattern`，删除pattern，取其后面的字串
    - `${aaa##pattern}`
        - greedy version
        - keey base path
            ```bash
            $ aaa="/Volumes/WORK/WORK/test"
            $ echo ${aaa##*/}
            test
            ```
        - get file extension
            ```bash
            ${aaa##*.}
            ```
    - `${aaa%pattern}`
        - also remove pattern, except it apply to the back of variable.
            ```bash
            $ FILE="xcache-1.3.0.tar.gz"
            $ echo "${FILE%.tar.gz}"
            xcache-1.3.0
            ```
        - remove file extension
            ```bash
            ${aaa%.*}
            ```
    - `${aaa%%pattern}`
        - greedy version
- 字符串替换
    - `${aaa/pattern/string}`
        - 将`pattern`匹配到的第一个字符串替换成`string`
    - `${aaa//pattern/string}`
        - 全局替换

- 算数扩展
    - `((...))`
        ```bash
        $ a=1
        $ ((a++))
        $ echo $a
        2
        ```
    - 支持 整数运算/位运算/关系运算/三元运算
    - 内建命令let
        - `let i=i**2`
        - `(())` 的另一种写法


