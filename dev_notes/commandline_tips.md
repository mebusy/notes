
# Command Line Tips ( may incompatible on MacOSX and Linux)

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



## kill process by port

```bash
kill $(lsof -t -i :PORTNUMBER)
```


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


## [bash] wait previous command to finish 

```bash
#！/bin/sh
echo “1”
sleep 5&
echo “3”
echo “4”
wait  #会等待wait所在bash上的所有子进程的执行结束，本例中就是sleep 5这句
echo”5”
```


