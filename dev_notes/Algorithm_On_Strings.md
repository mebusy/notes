...menustart

 - [Week1 Suffix Trees](#ede56b0e2be5bbfcf53933d43ef1f740)
	 - [From Genome Sequencing to Pattern Matching](#a8d5f7810493a28ca313b038a21c0173)
	 - [Brute Force Approach to Pattern Matching](#0bbf0b0ddc6dc0d500db46cbd60489c2)
	 - [Herding Patterns into Trie](#cd82dafbae81bae40211a2c7f374942f)
	 - [Herding Text into Suffix Trie](#38728a7876efba9de4422511579b2ddd)
		 - [Where Are the Matches???](#e7849ccbb64da45c5b8246d6f100af54)
		 - [Memory Footprint of Suffix Trie](#9f208e275122ae4c1c110416a76cfffe)
	 - [From Suffix Tries to Suffix Trees](#6df9f85e12d53da5a7faab3233bbbcf3)
	 - [Constructing Suffix Tree:](#eeb864ae13cd09f3fc8b2e37ef0dac43)
	 - [Quiz](#ab458f4b361834dd802e4f40d31b5ebc)
 - [Week2 Burrows-Wheeler Transform and Suffix Arrays](#7b4bb7010bb5cc258a877c223ce396fa)
	 - [Burrows-Wheeler Transform](#c77af5b3abfc315781377fb29256c39f)
		 - [Text Compression by Run-Length Encoding](#ae31601ab819806b46842f7459b1a9f1)
		 - [Inverting Burrows-Wheeler Transform](#2958b02379af181c5d50fdb9eb76f1f8)
		 - [Using BWT for Pattern Matching](#353b08ef75d5176db7f70fe5d2e3d617)
		 - [Finding Pattern Matches Using BWT](#ad4f3a6c1f6f60c79912e399831fe50e)
		 - [Searching for ana using top and buttom pointers](#577c04ac242ce1b20da613dd6aaf2a9f)
	 - [Suffix Arrays](#4297164b1e2c9e6f4924b39ebdad0b14)
	 - [Approximate Pattern Matching](#699b0062252bc43a8e1c97a871b1b3fd)
 - [Week3: Algorithmic Challenges: Knuth-Morris-Pratt Algorithm](#a13edce40a6797ca350bb37ecae33e7d)
	 - [Exact Pattern Matching](#9f189b44c5da7aabf3ba7ce283ed775c)
	 - [Prefix Function](#56d24cce97717b776b1c66489991f675)
		 - [Enumerating borders](#d1d75d9e4070f158aeaa17e37bc34991)
		 - [Computing s(i + 1)](#7458f83cf5feb375ce613102ad4cf673)
		 - [ComputePrefixFunction(P)](#52b3a75d31d9676c1ccf5234adc3347b)
	 - [Knuth-Morris-Pratt Algorithm](#a27872b96c92390fbd9d96e8553f69ca)
		 - [Explanation](#b72ac10807b29c77f5b7e4b80ea40414)
		 - [pseudo code](#d5c1daf026b98296ae4747476c5a2b2d)
		 - [Conclusion](#6f8b794f3246b0c1e1780bb4d4d5dc53)
 - [Week 4](#024f2ea1afa39552cc7823dfeaeeba8c)
	 - [Suffix Array](#070de002eb9fe6a242a3eea58a6b0a47)
		 - [Construct Suffix Array](#b3d93ca2f2b1bae05ed120cebaaaf0c3)
		 - [Storing Suffix Array](#0315a918e4426dc96ef07eca2ff9c282)

...menuend


<h2 id="ede56b0e2be5bbfcf53933d43ef1f740"></h2>

# Week1 Suffix Trees 

<h2 id="a8d5f7810493a28ca313b038a21c0173"></h2>

## From Genome Sequencing to Pattern Matching

 - Times 杂志堆发生了爆炸，如何知道 某天的杂志说了什么？
 - 基因重组

---

 - Pattern Matching Problem:
    - Input: A string Pattern (read) and a string Text (genome).
    - Output: All positions in Text where Pattern appears as a substring.
 - Approximate Pattern Matching Problem:
    - Input: A string Pattern, a string Text, and an integer d
    - Output: All positions in Text where Pattern appears as a substring **with at most d mismatches**.
 - ***Multiple*** Pattern Matching Problem:
    - Input: A ***set of strings*** Patterns and a string Text.
    - Output: All positions in Text where a string from Patterns appears as a substring.

<h2 id="0bbf0b0ddc6dc0d500db46cbd60489c2"></h2>

## Brute Force Approach to Pattern Matching

 - Pattern drives along Text
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_pattern_drive_on_text.png)
 - Brute Force Approach Is Fast!
    - running time of single Pattern: O(|Text|·|Pattern|)
    - The runtime of the Knuth-Morris-Pratt algorithm: O(|Text|)
 - Brute Force Approach is Slow for Billions of Patterns
    - running time:  O(|Text|·|Patterns|)
    - For human genome:
        - |Text|≈ 3*10⁹
        - |Patterns|≈ 10¹²

<h2 id="cd82dafbae81bae40211a2c7f374942f"></h2>

## Herding Patterns into Trie

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_herding_pattern_into_trie.png)

⇓

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_herding_pattern_into_trie2.png)

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_pattern.png)

For simplicity, we assume that no pattern is a substring of another pattern.

```
TrieMatching(Text, Patterns):
    drive Trie(Patterns) along Text
    at each position of Text
        - walk down Trie(Patterns) by spelling symbols of Text
        - a pattern from Patterns matches Text each time you reach a leaf
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_pattern_match.png)

 - Our Bus Is Fast!
    - Runtime of TrieMatching: O(|Text|\* |LongestPattern|)
 - Memory Footprint of TrieMatching
    - Our trie has 30 edges
    - # edges = O(|Patterns|) !!!
    - For human genome: |Patterns|≈ 10¹²  

<h2 id="38728a7876efba9de4422511579b2ddd"></h2>

## Herding Text into Suffix Trie

New Idea: Packing Text onto a Bus

 - Generate all suffixes of Text
 - Form a trie out of these suffixes (suffix trie)
 - For each Pattern, check if it can be spelled out from the root downward in the suffix trie

 - panamabananas$
    - Adding “$” sign in the end. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_text.png)

 - this tree also told us that *a* appear in the text 6 times.

<h2 id="e7849ccbb64da45c5b8246d6f100af54"></h2>

### Where Are the Matches???

Maybe we find a match :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_match_banana.png)

But where is the match ? What is the position of "banana" in the Text ?

 - Idea:to find the positions of matches , add some information to leaves

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_suffix_trie_text.png)

 - Walking Down to the Leaves to Find Matches
    - Once we find a match, we “walk down” to the leaf (or leaves) in order to find the starting position of the match.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_suffix_trie_ana.png)

<h2 id="9f208e275122ae4c1c110416a76cfffe"></h2>

### Memory Footprint of Suffix Trie
 
 - The suffix trie is formed from |Text| suffixes with total length: 
    - |Text| \* (|Text|– 1)/2
 - For human genome:
    - |Text|≈ 3\*10⁹
 
---

<h2 id="6df9f85e12d53da5a7faab3233bbbcf3"></h2>

## From Suffix Tries to Suffix Trees

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_suffix_tree.png)

 - Since each suffix adds one leaf and at most one internal vertex to the suffix tree:
    - #vertices < 2|Text|
    - memory footprint of the suffix tree: O(|Text|)
    - Cheating!!! - how do we store all edge labels?
        - storing edge labels !
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_store_edge_labels.png)

 - Why did we bother to add “$” to “panamabananas”?
    - to make sure that each suffix corresponds to a leaf
    - 单字母的情况：eg. s$
 - Why do we want to make sure that each suffix correspond to a leaf?
    - construct suffix tree for “papa”(without adding “$”) 
    - and construct suffix tree for “papa$”
    - compare it, you will get the answer.


<h2 id="eeb864ae13cd09f3fc8b2e37ef0dac43"></h2>

## Constructing Suffix Tree:

 - Naive Approach
    - Quadratic runtime: O(|Text|²)
    - O(|Genome| + |Patterns|) to find pattern matches
 - Linear-Time Algorithm
    - Linear runtime (for a constant-size alphabet): O(|Text|)
    - Linear-time algorithm (Weiner, 1973) was simplified by Ukkonen (1995) but it is still too complex to cover in this course
 
--- 

 - pseudocode for constructing a trie from a collection of patterns:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_code_trie_construction.png)
 - pseudocode for matching a collection of patterns against the text using a trie:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_code_trie_matching.png)

---

<h2 id="ab458f4b361834dd802e4f40d31b5ebc"></h2>

## Quiz

- Q: What is the running time and the memory consumption of exact pattern matching using suffix tree for text *Text* and a set of patterns *Patterns* with length of the text denoted by |*Text*| , and the total length of all patterns denoted by |Patterns| ?
- A: 
    - Running time: O(|Text|+|Patterns| )
    - memory consumption: O(|Text|)
- solution
    1. first we need O(|Text|) to build the suffix tree.
    2. Then for each *Pattern* in *Patterns* we need additional O(|Pattern|) to match this pattern against the *Text*
        - The total time for all the patterns is thus O(|Patterns|) 
    3. The overall running time is O(|Text|+|Patterns| ) 
    4. We only need O(|Text|) additional memory to store the suffix tree and all the positions where at least one of the *Patterns* occurs in the *Text*. 

 - However, big-O notation hides constants!
    - suffix tree algorithms has large memory footprint ~ 20 · |Text| for long texts like human genome
 - Even more importantly , We want to find mutations! 
    - it is unclear how to develop fast **Approximate** Multiple Pattern Matching using suffix trees 



---

<h2 id="7b4bb7010bb5cc258a877c223ce396fa"></h2>

# Week2 Burrows-Wheeler Transform and Suffix Arrays 

<h2 id="c77af5b3abfc315781377fb29256c39f"></h2>

## Burrows-Wheeler Transform

So our goal now is to start from the genome, apply Burrows–Wheeler transform to the genome. And we can now, hopefully, compress Burrows–Wheeler transform of the genome. And after you apply this compression, we will greatly reduce memory for storing our genome. But it totally makes sense if we can invert this transformation. 

<h2 id="ae31601ab819806b46842f7459b1a9f1"></h2>

### Text Compression by Run-Length Encoding

 - Run-length encoding compresses a run of n identical symbols:
    - GGGGGGGGGGCCCCCCCCCCCAAAAAAATTTTTTTTTTTTTTTCCCCCG
    - -> 10G11C7A15T5C1G
 - genomes don’t have lots of runs... but they do have lots of repeats:
    - ***ACTGA***CCGAA***ACTGA***GTATCCG***ACTGA***A***ACTGA***TCAGT***ACTGA***CATTGC

 - Idea: Converting Repeats to Runs
 - Forming All Cyclic Rotations of Text
    - panamabananas$
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_cyclic_rotation_of_text.png)

--- 

 - Cyclic Rotations
    - panamabananas$ 
    - $panamabananas 
    - s$panamabanana 
    - as$panamabanan 
    - nas$panamabana 
    - anas$panamaban 
    - nanas$panamaba 
    - ananas$panamab 
    - bananas$panama 
    - abananas$panam 
    - mabananas$pana 
    - amabananas$pan 
    - namabananas$pa 
    - anamabananas$p
 - Sorting Cyclic Rotations
    - Sort the strings lexicographically ($ comes first)
    - BWT(panamabananas$)=smnpbnn**aaaaa**$a
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_text.png)
    - now it has many runs
 - Going Back From BWT(Genome) to Genome ? 

--- 


<h2 id="2958b02379af181c5d50fdb9eb76f1f8"></h2>

### Inverting Burrows-Wheeler Transform

 - Reconstructing banana from annb$aa
    - We know the last column of the Burrows-Wheeler matrix. 
    - We also know the first column , because the first column is simply sorting all elements of the Burrows-Wheeler transform.  排序一下可得
        - Sorting all elements of “annb$aa” gives first column of BWT matrix.
    - We now know 2-mer composition of the circular string banana$ 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_invert_banana_2mer.png)
    - Sorting gives us the first 2 columns of the matrix
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_invert_banana_first2column.png)
    - We now know 3-mer composition of the circular string banana$
    - Sorting gives us the first 3 columns of the matrix.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_invert_banana_first3column.png)
    - repeate the steps, until we reconstruct the entire matrix !
        - Symbols in the first row (after $) spell ***banana***.
 - More Memory Issues
    - Reconstructing Text from BWT(Text) required us to store |Text| cyclic rotations of |Text|.
    - Can we invert BWT(Text) with less space and without |Text| rounds of sorting?
 - A Strange Observation
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_invert_hiding_in_same_position.png)
    - 1st **a** in FirstColumn and 1st **a** in LastColumn are hiding at the same position along the cycle!
    - They Are Hiding at the Same Position!
 - Is It True in General?
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_still_sorted.png)
 - First-Last Property
    - the k-th occurrence of *symbol* in ***FirstColumn***
    - and the k-th occurrence of *symbol* in ***LastColumn***
    - correspond to appearance of *symbol* at the same position in ***Text***.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_first_last_property.png)

---

 - Inverting BWT again 
    - let's start with the *$* that is located in the first column first row.  It corresponds to s1 in the last column first row. 
    - we know where s1 is located in the first column. let's move there.  (red line)
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_invert_BWT_again_1.png)
    - And s1 in the first column correspond to a6 in the last column. And we know where a6 is located in the first column , so let's move to the postion a6. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_invert_BWT_again_2.png)
    - repeat such steps , We are done 
        - This Was Fast!
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_invert_BWT_again_done.png)
        - Memory: 2|Text|
        - Time: O(|Text|)

--- 

 - quiz:  What is the inverse of the Burrows-Wheeler Transform AGGGAA$ ?
    - 注： BWT string $并不是总在最后一位
 - A: GAGAGA$

首先列出 1st column and last colum

```
$₁ ... A₁
A₁ ... G₁
A₂ ... G₂
A₃ ... G₃
G₁ ... A₂
G₂ ... A₃
G₃ ... $₁


A₁
G₁A₁
A₂G₁A₁
G₂A₂G₁A₁
A₃G₂A₂G₁A₁
G₃A₃G₂A₂G₁A₁
```

The only question left, where is pattern matching in the Burrows-Wheeler transform ?

<h2 id="353b08ef75d5176db7f70fe5d2e3d617"></h2>

### Using BWT for Pattern Matching

 - Can we use BWT(Text) to design a more memory efficient linear-time algorithm for Multiple Pattern Matching?

<h2 id="ad4f3a6c1f6f60c79912e399831fe50e"></h2>

### Finding Pattern Matches Using BWT

 - Searching for **ana** in p**ana**mab**anana**s
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_pattern_match_ana_found.png)
 - Lets Start by Matching the Last Symbol (a) 
    - Searching for ani**a** in panamabananas
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_pattern_match_a.png)
 - Matching the Last Two Symbols (na)
    - Searching for a**na** in panamabananas
    - Three Matches of na Found!
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_pattern_match_na.png)
 - Matching **ana**
    - Searching for **ana** in panamabananas
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWT_pattern_match_ana.png)


<h2 id="577c04ac242ce1b20da613dd6aaf2a9f"></h2>

### Searching for ana using top and buttom pointers 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWMatching_top_bottom_pointer.png)


```
if positions from top to bottom in LastColumn contain symbol 
    topIndex ← first postion of symbol among position from top to bottom in LastColumn 
    bottomIndex ← lastpostion of symbol among position from top to bottom in LastColumn 
    top ← LastToFirst( topIndex )
    bottom ← LastToFirst( bottomIndex )
```


 - 1st iteration - a
    - in lastColumn[0,13]  contain *a* 
    - topIndex ← 7 in last column
    - lastIndex ← 13 in last column
    - top ← 1  in first column
    - bottom ← 6 in 1st column
 - 2nd iteration - n 
    - in lastColumn[1,6] contain *n*
    - topIndex ← 2 in last column
    - lastIndex ← 6 in last column
    - top ← 9  in first column
    - bottom ← 11 in 1st column
 - 3th iteration - a
    - in lastColumn[9,11] contain *a*
    - topIndex ← 9 in last column
    - lastIndex ← 11 in last column
    - top ← 3  in first column
    - bottom ← 5 in 1st column
 - We found  5-3+1 = 3 !!! 
 

In the 1st iteration, the range of position we are interested in is narrowed to all position where *a* appears in the 1st column (a₁-a₆) .

We are looking for the next symbol , which is *n* in *ana* , and we are looking for the 1st occurrences of this symbol in the last column , among positions from top to buttom, among rows from top to buttom.

As soon as we found the 1st and last occurrence of this symbol in this case , and the first-last property will tell us where this *n* and all n's in between are hiding in the first column.  As a result , the pointers top and buttom equal to 1 and 6 , are changing into 9 and 11, they narrow the search. 

And then we continue further, and that's how we find the positions of *ana* in the text. 

Now we have a  pattern matching algorithm based on Burrows-Wheeler Transform, and it has good memory footprint. 

The only problem , though , is that BW Mathing is very slow. It analyzes every symbol from top to bottom in the last column in each step. What should we do? 

 - BWMatching is slow
    - it analyzes every symbol from top to bottom in each step!

---     

 - The trick here is to introduce the count array. 
    - The count array describes the number of apearances of a given symbol , in the first i postion of the last collumn. 

 - Introducing Count Array 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWM_count_array.png)
    - so you have the array of #occurrences for every symbol , trough this array, you can calculate the index where every symbol first appear in first column(sorted) (FIRSTOCCURRENCE).
 - bettern Algorithm !!!
    - Count<symbol>( i, LastColumn )
        - it's 2D array
        - return #occurrences of *symbol* in the first i positions of LastColumn.

```
BetterBWMatching( FIRSTOCCURRENCE , LastColumn , Pattern , Count  )
    top ← 0
    bottom ← |LastColumn| -1
    
    while top <= bottom
        if Pattern is nonempty
            symbol ← last letter in Pattern
            remove last lettern from Pattern
            top ← FIRSTOCCURRENCE(symbol) + Count( top, LastColumn )
            bottom ← FIRSTOCCURRENCE(symbol) + Count( bottom +1 , LastColumn ) -1 
        else 
            return bottom - top +1 
    return 
end function 
```

 - top ← 0 , bottom ← 13 
 - 1st iteration 
    - symbol ← a 
    - top ← 1 + 0 = 1
    - bottom ← 1 + 6 -1 = 6
 - 2nd iteration 
    - symbol ← n 
    - top ← 9 + 0 = 9 
    - bottom ← 9 + 3 -1 = 11
 - 3th iteration
    - symbol ← a 
    - top ← 1 + 2 = 3
    - bottom ← 1 + 5 -1 = 5
 - we found 5-3+1 = 3 matching !!!! 


And as you can see, we don't need any more to explore every symbol between top and bottom indices in the last column. 

---

There is still one question. Where are the matches that they found ? Where do they appear in the text  ?

 - Where Are the Matches?
    - We know that ***ana*** occurs 3 times, but where does ***ana*** appear in Text???

---

<h2 id="4297164b1e2c9e6f4924b39ebdad0b14"></h2>

## Suffix Arrays

 - Suffix array  holds starting position of each suffix beginning a row.
 - panamabananas$
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_suffix_array.png)
 

 - Q: what is the suffix array of the string S = GAGAGAGA$ ?  ( raw text )
 - A: [8 1 3 5 7 0 2 4 6]
 - problem will occure if we don't have the raw text, but BWT text

```
8 $
7 A$
5 AGA$
3 AGAGA$
1 AGAGAGA$
6 GA$
4 GAGA$
2 GAGAGA$
0 GAGAGAGA$
```

 - Using the Suffix Array to Find Matches
    - Thus, ana occurs at positions 1, 7, 9 
        - a3 -> 1
        - a4 -> 7
        - a5 -> 9

So , when suffix array is constructed, we can very quickly answer the question where the occurrence of the part is. In this case of *ana* , our pattern appear at position 1,7,and 9. 

The challenge is how to construct the suffix array quickly. Because the naive algorithm is O(n²). 

There is a way to construct a suffix array if you're already construction a suffix tree. A suffix array is simply a depth-first reversal of the suffix tree. 

 - From Suffix Tree to Suffix Array: Depth-First Traversal
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_fromSuffixTreeToSuffixArray.png)
    - Indeed, you start from lead 5, continue to lead 3, , and then 1, ....  

 - Constructing Suffix Array
    - Depth-first traversal of suffix tree
        - O(|Text|) time and ~20·|Text| space
    - Manber-Myers algorithm (1990):
        - O(|Text|) time and ~4·|Text| space
    - But memory footprint is still large for human genome!
    - We will learn how to quickly construct suffix array without relying on suffix tree later in this course

 - Reducing Memory Footprint for Suffix Array
    - Can we store only a fraction of the suffix array but still do fast pattern matching?
        - 只 suffix array的一部分
    - Partial suffix array SuffixArrayK(Text) only contains values that are multiples of some integer K
        - eg. k=5 -- 0,5,10

 - Using the Partial Suffix Array to Find Matches
    - Where are these ana prefixes located in Text???
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWM_match_use_partial_suffix_array.png)
    - Focus on **a₄na**
        - Partial suffix array reveals position of a₁bana
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_BWM_match_use_partial_suffix_array_a4na.png)



---

<h2 id="699b0062252bc43a8e1c97a871b1b3fd"></h2>

## Approximate Pattern Matching

 - Returning to Search for Mutations
    - Approximate Pattern Matching Problem:
        - Input: A string Pattern, a string Text, and an integer d.
        - Output: All positions in Text where the string Pattern  appears as a substring with at most d mismatches.
 - Revealing Mutations by Analyzing ***Billions*** of Reads
    - ***Multiple*** Approximate Pattern Matching Problem
        - Input: A ***set*** of strings Patterns, a string Text, and an integer d.
        - Output: All positions in Text where a string from Patterns appears as a substring with at most d mismatches.
 - BWT Saves the Day Again !
    - eg. *ana* with 1 mismatch
    - searching for an**a** in panamabananas
        - We will start again with finding all rows in the BW matrix that start with *a*.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_10.png)
    - searching for ai**na** in panamabananas
        - Approximate matching with at most 1 mismatch
        - And among them , we want to find rows that containts *na*.  Among six rows that start with *a* , only three of them actually end with *n*, they form exact matching of the last 2 symbols of *ana* to our text.   They form exact matching of the last 2 symbols of *ana* to our text.
        - In the past , it was the only thing we interested, but now, we're actually interested in all six rows starting from *a*,  because we are interested in approximate matches as well. 
        - And to find approximate matches , we need to retain all the 6 rows, and specify the number of mismatches for each of these rows. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_20.png) ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_21.png) ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_22.png)
    - searching for **ana** in panamabananas
        - This row results in a 2nd mismatch (the $), so we discard it.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_30.png)
    - Five Approximate Matches Found!
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_40.png)
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_41.png)
 


---

 
 - In reality, approximate pattern matching with BWT is more complex (we omitted various details)

---


<h2 id="a13edce40a6797ca350bb37ecae33e7d"></h2>

# Week3: Algorithmic Challenges: Knuth-Morris-Pratt Algorithm 

<h2 id="9f189b44c5da7aabf3ba7ce283ed775c"></h2>

## Exact Pattern Matching

 - Strings T (Text) and P (Pattern).
 - All such positions in T (Text) where P (Pattern) appears as a substring.

---
 
 - Brute Force Algorithm
    - Slide the Pattern down Text
    - Running time Θ(|T||P|)
 - Is it possible to skip some of positions while sliding the Pattern along the Text using only the information about the Pattern and the result of the comparsion of last alignment of the Pattern and the Text ?
    - Yes. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_skipping_positions_0.png)
        - now we have find a matching. if we somehow pre-precessed the pattern , and know that 
        - the prefix without last character !=  the suffix without the first character ( 'bra' != 'abr' )
            - we can skip this position
        - the prefix without 2 last characters !=  the suffix without the 2 characters ( 'ra' != 'ab' )
            - we can skip this position
        - the prefix without 3 last characters ==  the suffix without the 3 characters  ( 'a'=='a' )
            - we can not skip this postion
        - so for next iteration, we can just move Pattern by |Pattern| - |'a'| = 3  position !
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_skipping_positions.png)
        - another example is when we don't even find the whole pattern in the text, we still can skip some of the positions 
        - in this example, the longest prefix which is common for the text and pattern consisits 6 characters , and the pattern is longer (not entirely matching)
        - So we can not compare prefixes of the pattern with suffixes of the same pattern 
        - But instead, we can do the same thing with the string marked in green -- the longest common prefix 
        - 'ab' == 'ab'
        - so for next iteration, we can just move Pattern by 6-|'ab'| =   4 position!  
    
---

 - Definition
    - **Border** of string S is a prefix of S which is equal to a suffix of S, but not equal to the whole S.
 - Example
    - *a* is a border of *arba*
    - *ab* is a border of *abcdab*
    - *abab* is a border of *ababab*
    - *ab* is **not** a border of *ab*

--- 

 - Shifting Pattern
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_shiftingPattern_uw.png)
    - Find longest common prefix *u* 
    - Find *w* the longest border of *u*
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_shiftingPattern_shift.png)
    - Move P such that prefix w in P aligns with suffix w of u in T.
 - Now you know we can skip some of the comparisons
 - But we shouldn't miss any of the pattern occurrences in the text
 - Is it *safe* to shift the pattern this way ? 

<h2 id="56d24cce97717b776b1c66489991f675"></h2>

## Prefix Function

 - Definition
    - Prefix function of a string P is a function s(i) that for each i returns the length of the longest border of the prefix **P[0..i]**.  
 - Example 
    - P abababcaab
    - S 0012340112
    - s(2) means the length of longest border of **aba**  -- *a*
    - s(5) means the length of longest border of **ababab**  -- *abab*
 - Lemma
    - P[0..i] has a border of length s(i + 1) − 1
        - ![][1]
        - P[0..i] may have several borders, does not has to be longest one
    - Corollary
        - s(i+1) ≤ s(i)+1
        - that is , the prefix function can not grow by more than 1  , from some position to next position 
        - 字符串增加一个字符，s 一般会变小，就算不变小，s 最多也就 增加1

--- 
 
<h2 id="d1d75d9e4070f158aeaa17e37bc34991"></h2>

### Enumerating borders

 - Lemma 
    - If s(i) > 0, then all borders of P[0..i] but for the longest one are also borders of P[0..s(i) − 1].
        - 对于一段字符串，非 最长 border, 本身也是 最长border的 border
        - let *u* be a border shorter than the longest border , so that |u| < s(i)
        - border *u* is both a prefix , and suffix  of the longest border : P[0..s(i)-1]
            - remark: P[0..s(i)-1] is longest border !!! 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_Enumerating_borders_lemma.png)
        - and *u* was also shorter than the longest border, that is *u* ≠ P[0..s(i)-1] ,  so *u* is indeed a border of P[0..s(i)-1]
 - Corollary
    - All borders of P[0..i] can be enumerated by taking the longest border **b1** of P[0..i], then the longest border **b2** of **b1**, then the longest border **b3** of **b2**, . . . , and so on.

---

<h2 id="7458f83cf5feb375ce613102ad4cf673"></h2>

### Computing s(i + 1)

Now lets think how to compute the prefix function.

 - s(0) is 0
 - now to compute s(i+1) if we already know the values of the s(i)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_compute_prefix_function_0.png)
    - those green part is the border as prefix and suffix of string
    - if the characters right after those 2 borders are same , then 
        - s(i+1) = s(i) + 1 
        - **case 1**
        - because s(i+1) > s(i) -- we just increase the length of border , the we have learned that the prefix function can not grow by more than 1. 
    - but if the characters are different , everything is a bit more complex 
        - we know that P[0..i] has a border of length s(i + 1) − 1. 
            - ![][1]
        - So if we find that border then the next green character after it will be the same as the character in position i+1 -- 'x'
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_compute_prefix_function_1.png)
        - so what we need to is going through all the borders of the prefix ending in position i, by **decreasing** length. 
            - and as soon as we find some border that the next character after it is the same as the character at position i+1, then
            - s(i + 1) = |some border of P[0..s(i) − 1]| + 1 
            - **case 2**
    - at some point , we may come to the station that the longest border is empty , and then we'll need to compare the character in position i+1 with the character in postion 0 
        - either they are the same , and then the prefix function is 1 
            -- **case 3**
        - or they are different , and then the prefix function has the value of 0.
            -- **case 4**

--- 

 - Example :
    - P : ababcababac
    - s(0) = 0
    - s(1) = 0 , case 4
    - s(2) = 1 , case 3
    - s(3) = 2 , case 1
    - s(4) = 0 , case 2 , failed
    - s(5) = 1 , case 3
    - s(6) = 2 , case 1
    - s(7) = 3 , case 1
    - s(8) = 4 , case 1
    - s(9) = 3 , case 2 , success
    - s(10) = 0 , case 2 , failed 

--- 

<h2 id="52b3a75d31d9676c1ccf5234adc3347b"></h2>

### ComputePrefixFunction(P)

(![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_compute_prefix_function_algorithm.png)

 - The running time of ComputePrefixFunction is O(|P|)
 - Now you know how to compute prefix function in linear time
 - But how to nd pattern in text??

---

<h2 id="a27872b96c92390fbd9d96e8553f69ca"></h2>

## Knuth-Morris-Pratt Algorithm

 - to find all the occurrences of a pttern in the text in the time linear in terms of the length of the **pattern** and length of **text**


 - Create new string S = P + '$' + T
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP.png)
    - where '$' is just **any** special character absent from both P and T
 - Compute prefix function s for string S
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_prefix_func.png)
    - For all positions i such that i > |P| and s(i) = |P|, add i − 2|P| to the output
        - so we'll look at all positions i , such that i is more than length of the pattern 
            - `i > |P|` --  after the pattern and '$'
        - if the prefix function for that position i , is equal to the length of the pattern , then we know there is a occurrence of the pattern in text ending in that postion 
            - `s(i) = |P|` -- 2 positions in this case 
        - we need find all the postions where the pattern starts, so from the position where it ends , we need to compute the position where it starts in the raw TEXT 
            - `i − 2|P|` 
 - '$' can prevent the error in the cases such like:
    - Pattern = "AAA"
    - Text = "A" 
 
<h2 id="b72ac10807b29c77f5b7e4b80ea40414"></h2>

### Explanation

 - For all i, s(i) ≤ |P| because of the special character '$'
 - If i > |P| and s(i) = |P|, then P = S[0..|P| − 1] = S[i − |P| + 1..i] = T[i − 2|P|..i − |P| − 1]
 - If s(i) < |P|, no full occurrence of |P| ends in position i 

<h2 id="d5c1daf026b98296ae4747476c5a2b2d"></h2>

### pseudo code

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_pseudo_code.png)

 - Lemma
    - The running time of Knuth-Morris-Pratt algorithm is O(|P| + |T|).
 - Proof
    - Building string S is O(|P| + |T|)
    - Computing prefix function is O(|S|) = O(|P| + |T|)
    - The for loop runs O(|S|) = O(|P| + |T|) iterations


<h2 id="6f8b794f3246b0c1e1780bb4d4d5dc53"></h2>

### Conclusion

 - Can search pattern in text in linear time
 - Can compute prefix function of a string in linear time
 - Can enumerate all borders of a string

---

In the next lessons, we will learn how to build suffix array and suffix tree in time O(N·lgN) , which will allow you to find many different patterns in the same text even faster than if you use algorithms like KMP.

 


---

<h2 id="024f2ea1afa39552cc7823dfeaeeba8c"></h2>

# Week 4

<h2 id="070de002eb9fe6a242a3eea58a6b0a47"></h2>

## Suffix Array

<h2 id="b3d93ca2f2b1bae05ed120cebaaaf0c3"></h2>

###  Construct Suffix Array
 
 - Input: String S
 - Output: All suffixes of S in lexicographic order
 
---
 
 - Alphabet
    - We assume the alphabet is ordered, that is, for any two different characters in the alphabet one of them is considered smaller than another. For example, in English 
        - ’a’ < ’b’ < ’c’ < · · · < ’z’ 
 - Definition
    - String S is lexicographically smaller than string T if S ̸= T and there exist such i that:
        - 0 ≤ i ≤ |S| 
        - S[0..i − 1] = T[0..i − 1]
            - (assume S[0.. − 1] is an empty string)
        - Either i = |S| (then S is a prefix of T) , or S[i] < T[i]
 - Example
    - “*a*b” < “*b*c” (i = 0)
    - “ab*c*” < “ab*d*” (i = 2)
    - “abc” < “abc*d*” (i = 3)
 - Suffix Array Example
    - S = ababaa
    - Suffixes in lexicographic order:
        - a
        - aa
        - abaa
        - ababaa
        - baa
        - babaa
 - Avoiding Prefix Rule
    - we want to avoid this case when S is a prefix of T
    - Inconvenient rule: if S is a prefix of T, then S < T
    - Append special character ‘$’ smaller than all other characters to the end of all strings
    - If S is a prefix of T, then S$ differs from T$ in position i = |S|, and $ < T[|S|], so S$ < T$
 - Example
    - S = “ababaa” -> S' = “ababaa$”
    - Suffixes in lexicographic order:
        - $
        - a$
        - aa$
        - abaa$
        - ababaa$
        - baa$
        - babaa$
    

<h2 id="0315a918e4426dc96ef07eca2ff9c282"></h2>

### Storing Suffix Array

 - Total length of all suffixes is
    - 1 + 2 + · · · + |S| = Θ(|S|²)
 - Storing them all is too much memory
 - Store only the order of suffixes O(|S|) 
    - the order is just a permutation of numbers 
    - and the number of those numbers is the |S| 
    - that is what we mean by **suffix array**
 - **Suffix array** is this order 

 - Example
    - S = ababaa$
    - Suffixes are numbered by their starting positions: ababaa$ is 0, abaa$ is 2
    - Suffix array: order = [6, 5, 4, 2, 0, 3, 1]
        - we start with an empty array
            - order = []
        - So the smallest suffix is just $. 
            - order = [6] 
        - And the next one is a$  , which is numbered 5 ; and then aa$ which is numbered 4
            - order = [6,5,4]
        - eventually , we got
            - order = [6,5,4,2,0,3,1]
 - So this is the kind of array which we call suffix array
    - which is the order of all the suffixes of the initial string.
    - and we don't store the suffixes themselves
 - However if we need to look at, for example the 3rd character of the 2nd suffix in order 
    - we can fist go into the array **order** , find out which suffix is 2
    - and that will be the 1st position of that suffix in the stream , and if we then add 2 to that, we'll that get character.
    - So in theory we can look at any character of any suffix really efficiently although we don't store sufixes directly.
 - OK, you know how to store suffix array
 - But how to construct it? 


## General Construction Strategy

### Sorting Cyclic Shifts

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_sorting_cyclic_shift.png)





---

 [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_prefix_func_lemma_0.png


