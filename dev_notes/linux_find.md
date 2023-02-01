
# Find

find – recursively walk a file hierarchy

SYNOPSIS

```bash
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
```


## Find in directory

- find all files under current directory
    ```bash
    find .
    ```
- specify a directory, e.g. the user home directory
    ```bash
    find ~
    ```

## Filter by type: file or directory

- find only directories
    ```bash
    find . -type d
    ```
- or find only files
    ```bash
    find . -type f
    ```


## Specify name

- find all txt files
    ```bash
    find . -type f -name "*.txt"
    ```
- use `-iname` to ignore name sensitive
    ```bash
    find . -type f -iname "*.txt"
    ```

## Filter by modify time

- find all files modified in last 10 minutes ( less than )
    ```bash
    find . -type f -mmin -10
    ```
- Combine! find all files modified  more than 1 minute, but less than 5 minutes
    ```bash
    find . -type f -mmin +1 -mmin -5
    ```
- replace `mmin` with `mtime`  if you want use `day` instead of `minute`.


## Filter by file size

- find all files which file size is over 5M
    ```bash
    find . -type f -size +5M
    ```

## Filter by permission

```bash
find . -perm 755
```


## Limit walk depth

- find all markdown files in only current directory
    ```bash
    find . -type f -name "*.md" -maxdepth 1
    ```





