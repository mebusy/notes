[](...menustart)

- [Command Line Tips ( may incompatible on MacOSX and Linux)](#f213e24a291202fd8e154c3471e2653e)
    - [show pid of process by name](#ca16a9ebaa795350051c2666d4a7f8ba)
    - [kill process by port](#48cd249a485752b67116301484bb3978)
    - [check port using](#ab1922f2cde102e230acb305eb9338f2)
    - [wait previous command to finish](#541ac88de2966e25923b3142914c12fa)
    - [concat 2 stdout to one file](#06f8febd60d902a29111157609148ed4)
    - [ssh to server and execute something on command](#fb5aa28bd5781882fcbe8c435e69d705)

[](...menuend)


<h2 id="f213e24a291202fd8e154c3471e2653e"></h2>

# Command Line Tips ( may incompatible on MacOSX and Linux)

<h2 id="ca16a9ebaa795350051c2666d4a7f8ba"></h2>

## show pid of process by name

- On Linux, you can use `pidof`
- On MacOS, try
    ```bash
    ps -ax | grep -m1 <process-name> | awk '{print $1}'
    ```

- `ps -aux` : 查看进程状态
    parameter | function
    --- | ---
    `-a` | 显示所有用户有终端控制的进程
    `-u` | 显示用户以及其他详细信息
    `-x` | 显示没有控制终端的进程
    - ps 允许省略参数前的`-` : `ps aux`



<h2 id="48cd249a485752b67116301484bb3978"></h2>

## kill process by port

```bash
kill $(lsof -t -i :PORTNUMBER)
```


<h2 id="ab1922f2cde102e230acb305eb9338f2"></h2>

## check port using

Linux: 

```bash
netstat -tunlp | grep 8080
```

The closest equivalent you can get on macOS is:

```bash
netstat -p tcp -van | grep '^Proto\|LISTEN' | grep 8080
```

Or use lsof  (list opened files)

```bash
sudo lsof -i:8080
```

NOTE: lsof just list files opened by current users,  you need add `sudo` if you want to see all opened files.


<h2 id="541ac88de2966e25923b3142914c12fa"></h2>

## wait previous command to finish 

```bash
#！/bin/sh
echo “1”
sleep 5&
echo “3”
echo “4”
wait  #会等待wait所在bash上的所有子进程的执行结束，本例中就是sleep 5这句
echo”5”
```

<h2 id="06f8febd60d902a29111157609148ed4"></h2>

## concat 2 stdout to one file 

NOTE: the last `;` is key important to Linux

```bash
{ command1 && command2 ; } > dist.file
```


<h2 id="fb5aa28bd5781882fcbe8c435e69d705"></h2>

## ssh to server and execute something on command

- solution1: ssh one line command
    ```bash
    ssh 192.168.171.161 "uptime;hostname"
    ```
- solution2: if the job is complex, add `bash` command to suppress *Pseudo-terminal* warning
    ```bash
    ssh 192.168.171.161 bash <<EOF
      uptime
      hostname
    EOF
    ```



