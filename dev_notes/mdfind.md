...menustart

- [Basic Search](#c5c1098a067d3e19b900a3fdd6c6ad4d)
- [Boolean Operators](#99447b31568f35c690284a7990af044b)
- [Narrowing Search Results](#7ec8df286ac371d3900dc523ef9e9daa)
- [Filtering mdfind's output](#bbc752d74b076db37c447790cb425249)
- [Listing Metadata with mdls](#2f632d202624dbb9c7814dabbd14c77c)

...menuend


<h2 id="c5c1098a067d3e19b900a3fdd6c6ad4d"></h2>


# Basic Search

```
$ mdfind invoice
```

 - narrow down the search by adding terms. 

```
$ mdfind "invoice apress"   
```

<h2 id="99447b31568f35c690284a7990af044b"></h2>


# Boolean Operators

 - All words passed in a query string to mdfind are implicitly **AND** together
    - That is, "invoice apress" means both words must appear
 - Spotlight allows other Boolean operators as well:

```
|, the pipe character, means Boolean OR
- means to exclude a term
() create groups
```

 - Working with these operators can be tricky.
 - Whitespace is significant when building queries. 

 - case1: To get all documents with "invoice" or "o'reilly"
    - with no space between the terms

```
$ mdfind "invoice|o'reilly"
```

 - case2: find all documents with "invoice" but not "apress",
    - with no intervening spaces, and parentheses around the term I want to exclude.

```
$ mdfind "invoice(-apress)"
```

 - case3: get a list of invoices or contracts from O'Reilly,


```
$ mdfind "(invoice|contract) o'reilly"
```
 
 - Note that in all these examples that have more than a single word, I'm using double quotes around the search term. 
    - This makes the Unix shell pass our multiple words as a single parameter. 
    - Otherwise, mdfind uses only the last word, so that

```
$ mdfind invoice contract
is the same as
$ mdfind contract
```

 - It( double quotes ) also prevents the shell from intercepting characters that it would use as special, like the parentheses, and passes them unmolested to mdfind. 
 - This is especially important if I try to search for "O'Reilly". Without quotes, I will stuck in shell ...

```
$ mdfind O'Reilly
>
```

<h2 id="7ec8df286ac371d3900dc523ef9e9daa"></h2>


# Narrowing Search Results

 - `-onlyin` option

```
$ mdfind -onlyin ~/Downloads invoice
```

 - can have multiple -onlyin options

```
$ mdfind -onlyin ~/writing -onlyin "/Users/alester/to be filed" invoice
```

 - Note that because of the spaces in /Users/alester/to be filed I must put the pathname in double quotes. 
 - This also means I can't use the tilde shortcut `~` , because the tilde is a shell character that won't be expanded in quotes.

<h2 id="bbc752d74b076db37c447790cb425249"></h2>


# Filtering mdfind's output

 - grep
 - now mdfind gave you a list of searched file name.   you can use grep to filter the file name by some pattern

```
| grep xxx 
| grep -i xxx    // case-insensitive
| grep -v xxx     // not include xxx
```

<h2 id="2f632d202624dbb9c7814dabbd14c77c"></h2>


# Listing Metadata with mdls

 - The `mdls` command is the partner to mdfind
 - mdls lists the metadata attributes associated with a given file.

```
$ mdls ./InGameStateMachine.h
kMDItemContentCreationDate         = 2017-12-20 04:57:57 +0000
kMDItemContentCreationDate_Ranking = 2017-12-20 00:00:00 +0000
...
```

 - If I'm only interested in certain attributes, I can use the -name option:

```
$ mdls -name kMDItemFSSize ./InGameStateMachine.h  
kMDItemFSSize = 15076
```

 
 - Now I know some attributes name. I want to find files with kMDItemFSOwnerGroupID == 20

```
$ mdfind -onlyin . 'kMDItemFSOwnerGroupID = 20'
```

 - another example:
    - I know that I have more than three songs written by Roger Waters, so I'll rerun the search with wildcards, with an asterisk to mean "any string."

```
$ mdfind 'kMDItemComposer = "*Waters*"'
```

 - If I want a case-insensitive search, I can put the letter c outside the double quotes, as in this search to find all forms of "McCartney", regardless of the capitalization.

```
$ mdfind 'kMDItemComposer = "*mccartney*"c'
```

 - Maybe I want to find all my music files that were sampled at a bit rate lower than 128K:

```
$ mdfind 'kMDItemAudioBitRate < 128000'
```


