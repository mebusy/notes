
# 8 我是Makefile

 - make
    - make 会一次查找 GNUmakefile, makefile, Makefile 
        - 也可以使用 -f 指定一个工作文件
    - `-d` 参数用于调试 Makefile

## 8.2 基本概念

### 8.2.2 目标,条件和命令

```
# 目标 : 条件
#    命令
main.o : main.c line.h buffer.h tedef.h
    cc -c -o main.o main.c    
```


