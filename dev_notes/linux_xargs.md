
# XArgs

- some shell commands can not take stdin and use that as a parameter, to do this you need another program to help with this and that is what `xargs` command does.
- xargs allows to take standard input and pass that along as an argument into another command.

```bash
$ seq 5 | echo  # echo can not take stdin as parameter

$ seq 5 | xargs echo  # xargs can help
1 2 3 4 5
```


## -t

Echo the command to be executed to standard error immediately before it is executed.

```bash
$ seq 5 | xargs -t echo
echo 1 2 3 4 5
1 2 3 4 5
```


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

## -P maxprocs

Parallel mode: run at most `maxprocs` invocations of utility at once.  If `maxprocs` is set to 0, xargs will run as many processes as possible.

```bash
$ seq 5 | xargs -n 1 -P 2 bash -c 'echo $0;sleep 1'
# execution will took 3 seconds
```


