[](...menustart)

- [AWK](#00dbc48aa9a98544b52efb89b6ae601a)
    - [Syntax](#92e9d6227d5534e7afc27a11179c808e)
    - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
    - [Specify field separator](#afdd5066763979dfed0ba27a5e973afe)
    - [Use Regular Expression](#2f04f3e6eee339eeb0ddb6c39606424d)
    - [BEGIN / END](#cf99b2a271634d8ea4a068771d8d0462)

[](...menuend)


<h2 id="00dbc48aa9a98544b52efb89b6ae601a"></h2>

# AWK

· | 全称 | 描述 | example
---|---|---|---
NR | Number of Records | 当前记录行号, 从1开始, 全局累加，不管处理多少个文件 | `awk '{ print NR, $0 }' file.txt` 会在每行前打印行号。
FNR | File Number of Records | 当前文件记录行号, 每个文件单独计数 |  `awk '{ print FNR, NR, $0 }' file1.txt file2.txt`
NF | Number of Fields | 字段数 | `awk '{ print NF, $NF }' file.txt` NF 是字段数, $NF 是最后一个字段（非常常用）

- `$1, $2, ... $NF` 可以直接用来访问行的各个字段。
- `$0` 代表整行文本。

· | 全称 | 描述 | example
---|---|---|---
OFS | Output Field Separator | 输出字段分隔符，默认是空格 | `awk 'BEGIN { OFS=","; print "a", "b", "c" }'` 会输出 `a,b,c`
ORS | Output Record Separator | 输出记录分隔符，默认是换行符 | `awk 'BEGIN { ORS="---\n"; print "a"; print "b"; print "c" }'` 会输出 `a---\nb---nc---\n`
FS | Field Separator | 输入字段分隔符，默认是空格 | `awk -F, '{ print $1, $2 }'` 会把逗号作为字段分隔符。
RS | Record Separator | 输入记录分隔符，默认是换行符 | `awk 'BEGIN { RS="---" } { print $0 }'` 会把 `---` 作为记录分隔符。


· | 全称 | 描述 | example
---|---|---|---
FILENAME | - | 当前处理的文件名 | `awk '{ print FILENAME, $0 }' file.txt` 带上文件名打印每行。
ARGC | - | 命令行参数个数 | `awk 'BEGIN { print ARGC }' file.txt arg1 arg2`
ARGV | - | 命令行参数数组 | `awk 'BEGIN { for (i=0; i<ARGC; i++) print ARGV[i] }' file.txt arg1 arg2`


## awk 的设计哲学（这是核心）

### 1. 世界观：文本 = 记录流（record stream）

- awk 不认为自己在“处理文件”，而是在：**处理一串有结构的记录**.
- 默认：
    - 记录（record）== 一行
    - 字段（field） == 以 FS 分隔的列
    ```bash
    record 1 -> $1 $2 $3
    record 2 -> $1 $2 $3
    ```
- 所以 awk 的第一性原理是：
    - 对每条记录执行同一段逻辑
    - 这就是为什么, 不用写循环。
    ```awk
    { sum += $3 }
    ```

### 2. 程序结构：隐式 for-each

- awk 程序等价于：
    ```awk
    while (getline) {
        if (pattern) action;
    }
    ```
- 设计哲学：**程序员只描述“条件 + 动作”**.

### 3. Pattern → Action，而不是 Control Flow

- awk 不是 if/for 为中心，而是：
    ```awk
    pattern { action }
    ```
- 甚至 pattern 可以省略：
    ```awk
    { print }
    ```
- 这本质上是一个 规则系统（rule engine）。

### 4. 内建状态，而非对象模型

- awk 的状态来源：
    - 关联数组
    - NR / NF / FNR
    - 用户变量
- 哲学: 状态应当显式、扁平、可观察
    - 这也是 awk 非常适合统计、聚合的原因。

### 5. 流式优先（Streaming First）

- awk 的核心约束：
    - 不缓存全文件
    - 一次遍历
    - 记录级处理
- 所以：
    - 能用数组解决的就用数组
    - 能一次算完的绝不回头

## 进阶

### 阶段 2： 精通 4 个核心概念（80% 能力）

1. FS / RS / OFS / ORS
    ```awk
    BEGIN { FS=","; OFS="\t" }
    ```
2. NR / FNR / NF
    ```awk
    NR==1 { print "header" }
    NF<3 { next }
    ```
3. 关联数组（awk 的灵魂）
    ```awk
    count[$1]++
    sum[$1] += $3
    END { for (key in count) print key, count[key] }
    ```
4. END / BEGIN
    ```awk
    BEGIN { init }
    { process }
    END { report }
    ```
    - 这是一个 Map → Reduce 的模型


### 阶段 3：把 awk 当“数据库引擎”

用 SQL 思维写 awk

SQL | awk
---|---
SELECT | {print}
WHERE | pattern
GROUP BY | array[key]
HAVING | END
ORDER BY | sort


example

```awk
awk '{cnt[$2]++} END{for(k in cnt) if(cnt[k]>10) print k,cnt[k]}'
```

## awk 的“内功心法”（高手共识）

### 1. awk 是声明式，不是命令式

```awk
$3 > 100 { print }
```

不是：`如果……然后……`, 而是： **凡是满足条件的记录，都做这件事**.


### 2. awk 的变量是“列驱动”的


不要写：

```awk
for(i=1;i<=NF;i++) ...
```

### 3. 好 awk 程序长得像“公式”

这是一条数据公式，不是脚本。

```awk
{ sum[$1]+=$3; cnt[$1]++ }
END { for(k in sum) print k, sum[k]/cnt[k] }
```




------------------



<h2 id="92e9d6227d5534e7afc27a11179c808e"></h2>

## Syntax

Think of awk as just a simple program that iterates over your file one line at a time.

For every line in the file it checks to see whether that line has a certain pattern, if that line match a pattern, some action is performed.

NOTE: awk won't stop when if match a pattern, it will keep matching the rest patterns.

```bash
# PSEUDO
awk 'if(PATTERN1){ACTION1} if(PATTERN2){ACTION2} ...'
```

Since this way of doing things is so common, the `if` statement is never written, and the brackets `()`, even the `PATTERN`, can be omitted.

```bash
# syntax
awk 'PATTERN1{ACTION1} PATTERN2{ACTION2} ...'
```

<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>

## Example

- print the first 2 lines
    - `NR` stands for `Row Number`
    ```bash
    $ ls -l | awk 'NR==1{print $0} NR==2{print}'
    total 0
    drwx------@  3 root  staff    96 Dec  4  2021 Applications
    ```
- print full information of the first 3 lines,  and only last field for the rest lines
    - `NR` stands for `Number of Fields`
    ```bash
    ls -l | awk 'NR<=3{print} NR>3{print $NF}'
    total 0
    drwx------@  3 root  staff    96 Dec  4  2021 Applications
    drwx------@ 14 root  staff   448 Jan 31 18:43 Desktop
    Documents
    Downloads
    Library
    Movies
    Music
    ```
- print the last 2nd filed
    ```bash
    awk '....{print $(NF-1)}'
    ```


<h2 id="afdd5066763979dfed0ba27a5e973afe"></h2>

## Specify field separator

- awk treats space as the column delimiter
- use `-F` to specify a delimiter
    ```bash
    $awk -F ':' '{...}'
    ```
- The delimiter can be a regular expression.
    ```bash
    $awk -F '[.:]' '{...}'
    ```

<h2 id="2f04f3e6eee339eeb0ddb6c39606424d"></h2>

## Use Regular Expression

- print folder names which ends with `s`
    ```bash
    ls -l | awk '/s$/{print $NF}'
    Applications
    Documents
    Downloads
    Movies
    Pictures
    ```
- you can specify which field RE to be match
    ```bash
    ls -l | awk '$0 ~ /s$/{print $NF}'
    ```

<h2 id="cf99b2a271634d8ea4a068771d8d0462"></h2>

## BEGIN / END

- `BEGIN` / `END`  are special pattern in awk.  It doesn't match any specific line,  but instead, cause the action to execute when awk *starts up* / *shut down*.

```bash
ls -l | awk '
  BEGIN{temp_sum=0; total_records=0; print "Begin calculating average file size"}
  NR>1{temp_sum += $5; total_records +=1;}
  END{print "Average file size:" temp_sum/total_records }
'
```

```bash
Begin calculating average file size
Average file size:506.273
```






