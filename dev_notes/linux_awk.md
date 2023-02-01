
# AWK

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


## Specify field separator

- awk treats space as the column delimiter
- use `-F` to specify a delimiter
    ```bash
    $awk -F ':' '{...}'
    ```

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






