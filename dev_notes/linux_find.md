[](...menustart)

- [Find](#4cfa6c981549e990fe2344e4c805405e)
    - [Find in directory](#97de7d89284f917e19aa5d3119afc123)
    - [Filter by type: file or directory](#e26e11efc3479c611271cf5851344488)
    - [Specify name](#84097f2e0947ac580708288db2041359)
    - [Filter by modify time](#9f2bb13c4bb08bea320f4acf95b22ce5)
    - [Filter by file size](#55b2375d0bd22dc93c0160bd362ad87e)
    - [Filter by permission](#f51bac44535b55aee39f71a17703223e)
    - [Limit walk depth](#4e297dd150e9616ca1219b457e85f7c9)

[](...menuend)


<h2 id="4cfa6c981549e990fe2344e4c805405e"></h2>

# Find

find – recursively walk a file hierarchy

SYNOPSIS

```bash
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
```


<h2 id="97de7d89284f917e19aa5d3119afc123"></h2>

## Find in directory

- find all files under current directory
    ```bash
    find .
    ```
- specify a directory, e.g. the user home directory
    ```bash
    find ~
    ```

<h2 id="e26e11efc3479c611271cf5851344488"></h2>

## Filter by type: file or directory

- find only directories
    ```bash
    find . -type d
    ```
- or find only files
    ```bash
    find . -type f
    ```


<h2 id="84097f2e0947ac580708288db2041359"></h2>

## Specify name

- find all txt files
    ```bash
    find . -type f -name "*.txt"
    ```
- use `-iname` to ignore name sensitive
    ```bash
    find . -type f -iname "*.txt"
    ```

<h2 id="9f2bb13c4bb08bea320f4acf95b22ce5"></h2>

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


<h2 id="55b2375d0bd22dc93c0160bd362ad87e"></h2>

## Filter by file size

- find all files which file size is over 5M
    ```bash
    find . -type f -size +5M
    ```

<h2 id="f51bac44535b55aee39f71a17703223e"></h2>

## Filter by permission

```bash
find . -perm 755
```


<h2 id="4e297dd150e9616ca1219b457e85f7c9"></h2>

## Limit walk depth

- find all markdown files in only current directory
    ```bash
    find . -type f -name "*.md" -maxdepth 1
    ```





