
# SED – stream editor

sed allows you to filter & transform text, it's kind of a search/replace function.

syntax:

```bash
sed -i 's/find/replace/' filename
```

- `-i`  stands for  'inplace'

## Globally Replace - g


```bash
sed -i 's/find/replace/g' filename
```

- last `g` specifies that this substitution is global.


## Replace only on lines matching THE line pattern

```bash
sed '/LINE_PATTERN/s/find/replace/' filename
```


## Find and Delete  - d


```bash
sed '/LINE_PATTERN/d' filename
```


## Multiple Commands  -e 

```bash
sed -e 's/find/replace/' -e 's/find2/replace2/' filename
```

## Specify Delimiter

The character follows 's'  stands for the delimiter, you can change if your text contain this delimiter.


```bash
sed 's|find|replace|' filename
```


