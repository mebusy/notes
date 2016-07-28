...menustart

 - [A Simple Syntax-Directed anslator](#7bb979e48c0b2e41ffcc943354eea3dd)
	 - [2.1 Introduction](#af0cf6c4627b1e734c8a7fc86c534ac9)
	 - [2.2 Syntax Definition](#49e3a75fe90809fc7abafbcfbc51fd7b)
		 - [2.2.1 Definition of Grammars](#034fe90866337af0fbb672df1de0b66d)

...menuend



<h2 id="7bb979e48c0b2e41ffcc943354eea3dd"></h2>
# A Simple Syntax-Directed Translator

This chapter is an introduction to the compiling techniques in Chapters 3 through 6 of this book

 - We start small by creating a syntax-directed translator that maps infix arith­metic expressions into postfix expressions. 
 - We then extend this translator to map code fragments as shown in Fig. 2.1 into three-address code of the form in Fig. 2.2.


```java
{
	int i; int j; float[100] a; float v; float x;
	while ( true ) {
		do i = i+1;  while ( a[i] < v );
		do j = j-1;  while ( a[j] > v ); 
		if ( i >= j ) break;
		x = a[i]; a[i] = a[j]; a[j] = x ;
	} 
}
```

Figure 2.1: A code fragment to be translated




```
 1: i = i + 1
 2: t1 = a [ i ]
 3: if t1 < v goto 1
 4: j = j - 1
 5: t2 = a [ j ]
 6: if t2 > v goto 4
 7: ifFalse i >= j goto 9
 8: goto 14
 9: x = a [ i ]
10: t3 = a [ j ]
11: a [ i ] = t3
12: a [ i ] = x
13: goto 1
14:
```

Figure 2.2: Simpli ed intermediate code 


<h2 id="af0cf6c4627b1e734c8a7fc86c534ac9"></h2>
## 2.1 Introduction

For review:

 - The analysis phase of a compiler breaks up a source program into constituent pieces and produces an internal representation for it
 	- that representation called *intermediate code*. 
 	- Analysis is organized around the "syntax"
 	- The ***syntax*** of a programming language describes the proper form of its pro­grams
 		- context-free grammar can be used to help guide the translation of programs
 	- while the ***semantics*** of the language defines what its programs mean
 - The synthesis phase translates the intermediate code into the target program.


For simplicity, we consider the syntax-directed translation of infix expressions to postfix form, a notation in which operators appear after their operands. 

For example, the postfix form of the expression `9 - 5 + 2` is `95 - 2+`. 

Translation into postfix form is rich enough to illustrate syntax analysis, yet simple enough. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_frontend_model.png)

Figure 2.3: A model of a compiler front end

 - A lexical analyzer allows a translator to handle multicharacter constructs like identifiers , but are treated as units called tokens during syntax analysis
 - Next, we consider intermediate-code generation
 	- two forms of intermedi­ate code :
 		- 1- *abstract syntax trees* or simply *syntax trees*
 			- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_AST_example.png)
 			- represents the hierarchical syntactic structure of the source program
 			- syntax trees is further translated into three-address code
 		- 2-  "three-address" instructions
 			- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_3addr_inst_example.png)
 			- instructions form:  x = y **op** z
 				- **op** is a binary operator
 				- y and z the are addresses for the operands
 				- x is the address for the result of the operation
 			- a three­ address instruction carries out at most one operation, typically a computation, a comparison, or a branch.	


<h2 id="49e3a75fe90809fc7abafbcfbc51fd7b"></h2>
## 2.2 Syntax Definition

 - We introduce a notation - the "context-free grammar," or "grammar" for short 
	- used to specify the syntax of a language. 
	- A grammar naturally describes the hierarchical structure of most program­ming language constructs. 
	- For example, an if-else statement in Java can have the form
		- `if ( expression ) statement else statement`
	- using the variable expr to denote an expres­sion and the variable stmt to denote a statement, this structuring rule can be expressed as
		- `stmt → if ( expr ) stmt else stmt`
		- Such a rule is called a ***production***
			- in which the arrow may be read as "can have the form."
			- lexical elements like the keyword if and the paren­theses are called ***terminals***
			- Variables like expr and stmt represent *sequences of terminals* and are called ***nonterminals***.

<h2 id="034fe90866337af0fbb672df1de0b66d"></h2>
### 2.2.1 Definition of Grammars

Tokens is ofen terminal.

 - In a compiler, the lexical analyzer reads the characters of the source pro­gram, groups them into lexically meaningful units called *lexemes*, and pro­duces as output tokens representing these lexemes. 
 - A token consists of two components, a token name and an attribute value. 
 	- The token names are abstract symbols that are used by the parser for syntax analysis. 
 		- Often, we shall call these token names ***terminals***, since they appear as terminal symbols in the grammar for a programming language. 
 	- The attribute value, if present, is a pointer to the symbol table that contains additional infor­mation about the token. 
 		- This additional information is not part of the grammar, so in our discussion of syntax analysis, often we refer to tokens and terminals synonymously.


A context-free grammar has four components:

 1. A set of ***terminal*** symbols, sometimes referred to as "tokens." 
 	- The terminal are the elementary symbols of the language defined by the grammar.
 2. A set of ***nonterminals***, sometimes called "syntactic variables." 
 	- Each non­terminal represents a set of strings of terminals
 3. A set of ***productions*** 
 	- each *production* consists of :
 	- a nonterminal, called the *head* or *lefe side* of the production, 
 	- an arrow, 
 	- and a sequence of terminals and/or nonterminals, called the *body* or *right side* of the produc­tion. 
 	- The intuitive intent of a production is to specify one of the written forms of a construct; 
 		- if the head nonterminal represents a construct, 
 		- then the body represents a written form of the construct.
 4. A designation of one of the nonterminals as the *start* symbol.


We specify grammars by listing their productions

 - with the productions for the start symbol listed first
 - We assume that digits, signs such as < and <=, and boldface strings such as **while** are terminals
 - and any nonitalicized name or symbol may be assumed to be a terminal.
 - For notational convenience, productions with the ***same nonterminal*** as the head can have their bodies grouped
 	- with the alternative bodies separated by the symbol "|" , which we read as "or."

Example : lists of digits separated by plus or minus signs

```java
list → list + digit 		(2.1)
list → list - digit 		(2.2)
list → digit  				(2.3)
digit → 0|1|2|3|4|5|6|7|8|9		(2.4)	
```

The first 3 productions with nonterminal *list* as head , equivalently can be grouped:

```
list → list + digit | list - digit |  digit
```

According to our conventions, the terminals of the grammar are the symbols: `+ - 1 2 3 4 5 6 7 8 9` ,

The nonterminals are the italicized names *list* and *digit*, with *list* being the start symbol because its productions are given first. 

We say a production is *for* a nonterminal if the nonterminal is the head of the production. A string of terminals is a sequence of zero or more terminals. The string of zero terminals, written as `ε`, is called the *empty* string.

### 2.2.2 Derivations

 - A grammar derives strings by beginning with the start symbol 
 - and repeatedly replacing a nonterminal by the body of a production for that nonterminal. 
 - The terminal strings , that can be derived from the start symbol,  ***form*** the *language* which defined by the grammar.

For example, we can use grammars 2.1 to deduce that 9-5+2 is a list as follows.

 - a) 9 is a list by production (2.3), since 9 is a digit.
 - b) 9-5 is a list by production (2.2), since 9 is a list and 5 is a digit.
 - c) 9-5+2 is a list by production (2.1), since 9-5 is a list and 2 is a digit.



Example 2.3  function call , may have 0,1,2 parameters

```java
	call → id ( optparams ) 
optparams → params | ε
   params → params , param | param
```

We have not shown the productions for *param*, since parameters are really arbitrary expressions. Shortly, we shall discuss the appropriate productions for the various language constructs, such as expressions, statements, and so on.

 - *Parsing* is the problem of taking a string of terminals and figuring out how to derive it from the start symbol of the grammar, 
 - and if it cannot be derived from the start symbol of the grammar, then reporting syntax errors within the string. 
 - Parsing is one of the most fundamental problems in all of compiling; 
 	- In this chapter, for simplicity, we begin with source programs like 9-5+2 in which each character is a terminal; 
 - in general, a source program has multicharacter lexemes that are grouped by the lexical analyzer into tokens, whose first components are the terminals processed by the parser.

### 2.2.3 Parse trees

 - A parse tree pictorially shows how the start symbol of a grammar derives a string in the language. 
 - If nonterminal A has a production A → XYZ, then a parse tree may have an interior node labeled A with three children labeled X, Y, and Z, from left to right:
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compilers_parse_tree_AXYZ.png)
 - Formally, given a context-free grammar, a parse tree according to the gram­mar is a tree with the following properties:
 	- The root is labeled by the start symbol
 	- Each leaf is labeled by a terminal or by ε.
 	- Each interior node is labeled by a nonterminal.
 	- If A is the nonterminal labeling some interior node and X₁ , X₂ , ... , Xn are the labels of the children of that node from left to right, then there must be a production A → X₁X₂...Xn. Here, X₁,X2,... ,Xn each stand for a symbol that is either a terminal or a nonterminal. 


Example 2.4 : The derivation of 9-5+2 in Example 2.2 is illustrated by the tree in Fig. 2.5.

 - Parse tree for 9-5+2 according to the grammar in Example 2.1
 - 










