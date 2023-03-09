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






