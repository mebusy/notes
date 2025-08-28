[](...menustart)

- [SED – stream editor](#06d5c43de988900f788b9262daf37d39)
    - [Globally Replace - g](#09a87e5d5fd1cf429dc5702e15b429dd)
    - [Replace only on lines matching THE line pattern](#0ec666d632dea97f9e6fc8b34d9753d8)
    - [Find and Delete  - d](#692ebbacb84e6f8a7aab45236119e1d5)
    - [Multiple Commands  -e](#c481c5c5953e30563788d5e1e70b4a62)
    - [Specify Delimiter](#3a52a9a2e940669071b653b8d3f77037)

[](...menuend)


<h2 id="06d5c43de988900f788b9262daf37d39"></h2>

# SED – stream editor

sed allows you to filter & transform text, it's kind of a search/replace function.

syntax:

```bash
sed -i 's/find/replace/' filename
```

- `-i`  stands for  'inplace'

<h2 id="09a87e5d5fd1cf429dc5702e15b429dd"></h2>

## Globally Replace - g


```bash
sed -i 's/find/replace/g' filename
```

- last `g` specifies that this substitution is global.


<h2 id="0ec666d632dea97f9e6fc8b34d9753d8"></h2>

## Replace only on lines matching THE line pattern

```bash
sed '/LINE_PATTERN/s/find/replace/' filename
```


<h2 id="692ebbacb84e6f8a7aab45236119e1d5"></h2>

## Find and Delete  - d


```bash
sed '/LINE_PATTERN/d' filename
```


<h2 id="c481c5c5953e30563788d5e1e70b4a62"></h2>

## Multiple Commands  -e 

```bash
sed -e 's/find/replace/' -e 's/find2/replace2/' filename
```

<h2 id="3a52a9a2e940669071b653b8d3f77037"></h2>

## Specify Delimiter

The character follows 's'  stands for the delimiter, you can change if your text contain this delimiter.


```bash
sed 's|find|replace|' filename
```

# Tricks

## recursive replace in all files in a directory

```bash
# linux bash
find . -type f              -exec sed -i 's/find/replace/g' {} +

find . -type f -name "*.cs" -exec sed -i 's/find/replace/g' {} +
```

