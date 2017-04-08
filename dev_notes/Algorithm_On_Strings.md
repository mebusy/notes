
# Week1 Suffix Trees 

## From Genome Sequencing to Pattern Matching

 - Times 杂志堆发生了爆炸，如何知道 某天的杂志说了什么？
 - 基因重组

---

 - Pattern Matching Problem:
    - Input: A string Pattern (read) and a string Text (genome).
    - Output: All positions in Text where Pattern appears as a substring.
 - Approximate Pattern Matching Problem:
    - Input: A string Pattern, a string Text, and an integer d
    - Output: All positions in Text where Pattern appears as a substring ***with at most d mismatches***.
 - ***Multiple*** Pattern Matching Problem:
    - Input: A ***set of strings*** Patterns and a string Text.
    - Output: All positions in Text where a string from Patterns appears as a substring.

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

## Herding Text into Suffix Trie

New Idea: Packing Text onto a Bus

 - Generate all suffixes of Text
 - Form a trie out of these suffixes (suffix trie)
 - For each Pattern, check if it can be spelled out from the root downward in the suffix trie

 - panamabananas$
    - Adding “$” sign in the end. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_text.png)

 - this tree also told us that *a* appear in the text 6 times.

### Where Are the Matches???

Maybe we find a match :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_trie_match_banana.png)

But where is the match ? What is the position of "banana" in the Text ?

 - Idea:to find the positions of matches , add some information to leaves

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_suffix_trie_text.png)

 - Walking Down to the Leaves to Find Matches
    - Once we find a match, we “walk down” to the leaf (or leaves) in order to find the starting position of the match.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorithm_string_suffix_trie_ana.png)

### Memory Footprint of Suffix Trie
 
 - The suffix trie is formed from |Text| suffixes with total length: 
    - |Text| \* (|Text|– 1)/2
 - For human genome:
    - |Text|≈ 3\*10⁹
 
---

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


## Constructing Suffix Tree:

 - Naive Approach
    - Quadratic runtime: O(|Text|2)
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

---


