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
		 - [Inverting Burrows-Wheeler Transform](#2958b02379af181c5d50fdb9eb76f1f8)
		 - [Using BWT for Pattern Matching](#353b08ef75d5176db7f70fe5d2e3d617)
		 - [Searching for ana using top and buttom pointers](#577c04ac242ce1b20da613dd6aaf2a9f)
	 - [Suffix Arrays](#4297164b1e2c9e6f4924b39ebdad0b14)
	 - [Approximate Pattern Matching](#699b0062252bc43a8e1c97a871b1b3fd)

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
    - BWT(panamabananas$)=smnpbnn***aaaaa***$a
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
    - searching for an***a*** in panamabananas
        - We will start again with finding all rows in the BW matrix that start with *a*.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_10.png)
    - searching for ai***na*** in panamabananas
        - Approximate matching with at most 1 mismatch
        - And among them , we want to find rows that containts *na*.  Among six rows that start with *a* , only three of them actually end with *n*, they form exact matching of the last 2 symbols of *ana* to our text.   They form exact matching of the last 2 symbols of *ana* to our text.
        - In the past , it was the only thing we interested, but now, we're actually interested in all six rows starting from *a*,  because we are interested in approximate matches as well. 
        - And to find approximate matches , we need to retain all the 6 rows, and specify the number of mismatches for each of these rows. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_20.png) ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_21.png) ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_22.png)
    - searching for ***ana*** in panamabananas
        - This row results in a 2nd mismatch (the $), so we discard it.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_30.png)
    - Five Approximate Matches Found!
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_40.png)
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AOS_approximate_matching_ana_41.png)
 


---

 
 - In reality, approximate pattern matching with BWT is more complex (we omitted various details)

---


# Week3: Algorithmic Challenges: Knuth-Morris-Pratt Algorithm 

## Exact Pattern Matching

 - Strings T (Text) and P (Pattern).
 - All such positions in T (Text) where P (Pattern) appears as a substring.

---
 
 - Brute Force Algorithm
    - Slide the Pattern down Text
    - Running time Θ(|T||P|)
 - Is it possible to skip some of positions while sliding the Pattern along the Text using only the information about the Pattern and the result of the comparsion of last alignment of the Pattern and the Text ?
    - Yes. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_on_string_KMP_skipping_positions.png)
    - 先预处理 Pattern, prefix *a* 在 Pattern 中的第二次出现是 4
    - 进行1一次匹配，from index 0 ， 得到 最长公共子序列 长度为 6
    - 下一次迭代 匹配的时候，可以直接 jump to postion 4. 









