[](...menustart)

- [XArgs](#3f43a8743eade0074a537f7f38a8899e)
    - [-t](#b7cc4b6b2b8c0f37377b5cc259385de0)
    - [-I alias](#e5609751fdeeccc7f4fc2691c6f82f12)
    - [-n number](#259f085821c8ece082980839c0a87d3c)
    - [-P maxprocs](#59d1e8dcbb71e4e67597a52af6a4158f)

[](...menuend)


<h2 id="3f43a8743eade0074a537f7f38a8899e"></h2>

# XArgs (eXtended arguments)

**Reads items from standard input (stdin) and builds command-line arguments from them.**

```bash
stdin → argument list → command execution
```

- some shell commands can not take stdin and use that as a parameter, to do this you need another program to help with this and that is what `xargs` command does.
- xargs allows to take **standard input** and pass that along as **an argument** into another command.
    - stdin -> argument

```bash
$ seq 5 | echo  # echo can not take stdin as parameter

$ seq 5 | xargs echo  # xargs can help
1 2 3 4 5
```


<h2 id="b7cc4b6b2b8c0f37377b5cc259385de0"></h2>

## -t

Echo the command to be executed to standard error immediately before it is executed.

```bash
$ seq 5 | xargs -t echo
echo 1 2 3 4 5
1 2 3 4 5
```


<h2 id="e5609751fdeeccc7f4fc2691c6f82f12"></h2>

## -I alias

specify a placeholder, basically an alias for the arguments.

```bash
$ ls | xargs -I {} echo /home/dt/{}
/home/dt/Applications
/home/dt/Desktop
/home/dt/Documents
/home/dt/Downloads
...
```

you can specify anything as the placeholder, as the alias

```bash
$ ls | xargs -I zzz echo /home/dt/zzz
/home/dt/Applications
/home/dt/Desktop
/home/dt/Documents
/home/dt/Downloads
...
```

the replstr of alias has max-length limit, default is 255, it the length of replstr is greater than its limit, the `alias` will not match, to solve this problem, you may specify the max-lenght

```bash
xargs -S 10240 -I {} ...
```


<h2 id="259f085821c8ece082980839c0a87d3c"></h2>

## -n number

Set the maximum number of arguments taken from standard input for each invocation of utility.

```bash
$ ls | xargs
Applications Desktop Documents Downloads Google Drive Library Movies Music Pictures Public go

$ ls | xargs -n 1
Applications
Desktop
Documents
Downloads
...
```

<h2 id="59d1e8dcbb71e4e67597a52af6a4158f"></h2>

## -P maxprocs

Parallel mode: run at most `maxprocs` invocations of utility at once.  If `maxprocs` is set to 0, xargs will run as many processes as possible.

```bash
$ seq 5 | xargs -n 1 -P 2 bash -c 'echo $0;sleep 1'
# execution will took 3 seconds
```

If `maxprocs` is set to 0, xargs will run as many processes as possible.


## Very Important Option: -0

- Regular xargs splits on whitespace.
- If filenames contain spaces, it's dangerous.
- Correct way:
    ```bash
    find . -name "*.log" -print0 | xargs -0 rm
    ```
- Here:
    - `-print0` separates results with null character
    - `-0` tells xargs to split on null
