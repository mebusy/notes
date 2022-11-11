[](...menustart)

- [Basic Search](#c5c1098a067d3e19b900a3fdd6c6ad4d)
- [Boolean Operators](#99447b31568f35c690284a7990af044b)
- [Narrowing Search Results](#7ec8df286ac371d3900dc523ef9e9daa)
- [Filtering mdfind's output](#bbc752d74b076db37c447790cb425249)
- [Listing Metadata with mdls](#2f632d202624dbb9c7814dabbd14c77c)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [find files with specific extension](#d9e21c4547cc76da5ac8d583d3d40772)

[](...menuend)


<h2 id="c5c1098a067d3e19b900a3fdd6c6ad4d"></h2>

# Basic Search

```bash
$ mdfind invoice
```

- narrow down the search by adding terms. 

```bach
$ mdfind "invoice apress"   
```

<h2 id="99447b31568f35c690284a7990af044b"></h2>

# Boolean Operators

- All words passed in a query string to mdfind are implicitly **AND** together
    - That is, "invoice apress" means both words must appear
- Spotlight allows other Boolean operators as well:

```bash
|, the pipe character, means Boolean OR
- means to exclude a term
() create groups
```

- Working with these operators can be tricky.
- Whitespace is significant when building queries. 

- case1: To get all documents with "invoice" or "o'reilly"
    - with no space between the terms
    ```bash
    $ mdfind "invoice|o'reilly"
    ```
- case2: find all documents with "invoice" but not "apress",
    - with no intervening spaces, and parentheses around the term I want to exclude.
    ```bash
    $ mdfind "invoice(-apress)"
    ```

- case3: get a list of invoices or contracts from O'Reilly,
    ```bash
    $ mdfind "(invoice|contract) o'reilly"
    ```
 
- Note that in all these examples that have more than a single word, I'm using double quotes around the search term. 
    - This makes the Unix shell pass our multiple words as a single parameter. 
    - Otherwise, mdfind uses only the last word, so that
    ```bash
    $ mdfind invoice contract
    is the same as
    $ mdfind contract
    ```
- It( double quotes ) also prevents the shell from intercepting characters that it would use as special, like the parentheses, and passes them unmolested to mdfind. 
- This is especially important if I try to search for "O'Reilly". Without quotes, I will stuck in shell ...
    ```bash
    $ mdfind O'Reilly
    >
    ```

<h2 id="7ec8df286ac371d3900dc523ef9e9daa"></h2>

# Narrowing Search Results

- `-onlyin` option
    ```bash
    $ mdfind -onlyin ~/Downloads invoice
    ```
- can have multiple -onlyin options
    ```bash
    $ mdfind -onlyin ~/writing -onlyin "/Users/alester/to be filed" invoice
    ```
- Note that because of the spaces in /Users/alester/to be filed I must put the pathname in double quotes. 
- This also means I **can't use the tilde shortcut** `~` , because the tilde is a shell character that won't be expanded in quotes.

<h2 id="bbc752d74b076db37c447790cb425249"></h2>

# Filtering mdfind's output

- grep
- now mdfind gave you a list of searched file name.   you can use grep to filter the file name by some pattern
    ```bash
    | grep xxx 
    | grep -i xxx    // case-insensitive
    | grep -v xxx     // not include xxx
    ```

<h2 id="2f632d202624dbb9c7814dabbd14c77c"></h2>

# Listing Metadata with mdls

- The `mdls` command is the partner to mdfind
- mdls lists the metadata attributes associated with a given file.
    ```bash
    $ mdls ./InGameStateMachine.h
    kMDItemContentCreationDate         = 2017-12-20 04:57:57 +0000
    kMDItemContentCreationDate_Ranking = 2017-12-20 00:00:00 +0000
    ...
    ```

- If I'm only interested in certain attributes, I can use the -name option:
    ```bash
    $ mdls -name kMDItemFSSize ./InGameStateMachine.h  
    kMDItemFSSize = 15076
    ```
 
- Now I know some attributes name. I want to find files with kMDItemFSOwnerGroupID == 20
    ```bash
    $ mdfind -onlyin . 'kMDItemFSOwnerGroupID = 20'
    ```

- another example:
    - I know that I have more than three songs written by Roger Waters, so I'll rerun the search with wildcards, with an asterisk to mean "any string."
    ```bash
    $ mdfind 'kMDItemComposer = "*Waters*"'
    ```

- If I want a case-insensitive search, I can put the letter c outside the double quotes, as in this search to find all forms of "McCartney", regardless of the capitalization.
    ```bash
    $ mdfind 'kMDItemComposer = "*mccartney*"c'
    ```

- Maybe I want to find all my music files that were sampled at a bit rate lower than 128K:
    ```bash
    $ mdfind 'kMDItemAudioBitRate < 128000'
    ```

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

# Misc

<h2 id="d9e21c4547cc76da5ac8d583d3d40772"></h2>

##  find files with specific extension

- following cmd will find all files whose filename contains `.bak`
    ```bash
    $ mdfind -onlyin . -name .bak
    ```
    - it may include those files that not end with `.bak`
- this cmd will find all .bak files
    ```bash
    $ mdfind -onlyin . "kMDItemDisplayName == *.bak"
    ```


