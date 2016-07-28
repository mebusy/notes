...menustart

 - [A Simple Syntax-Directed Translator](#30a63c77c1af80be66640ae14eeb6ad5)
	 - [2.1 Introduction](#af0cf6c4627b1e734c8a7fc86c534ac9)
	 - [2.2 Syntax Definition](#49e3a75fe90809fc7abafbcfbc51fd7b)
		 - [2.2.1 Definition of Grammars](#034fe90866337af0fbb672df1de0b66d)
		 - [2.2.2 Derivations](#1050ffd6bfcbf072adafa71cd6bc7391)
		 - [2.2.3 Parse trees (Concrete Syntax Tree)](#e270ca1319a8a19beaad53b4e3df5f0e)
		 - [2.2.4 Ambiguity](#4ad96debb40880b43bd7d10f5554a448)
		 - [2.2.5 Associativity of Operators](#711cb58dcac9926888c6efb7c422cb65)

...menuend


[龙书练习答案](https://github.com/fool2fish/dragon-book-exercise-answers)


<h2 id="30a63c77c1af80be66640ae14eeb6ad5"></h2>
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

Example 2.1 : lists of digits separated by plus or minus signs

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

<h2 id="1050ffd6bfcbf072adafa71cd6bc7391"></h2>
### 2.2.2 Derivations

 - A grammar derives strings by beginning with the start symbol 
 - and repeatedly replacing a nonterminal by the body of a production for that nonterminal. 
 - The terminal strings , that can be derived from the start symbol,  ***form*** the *language* which defined by the grammar.

For example 2.2 , we can use grammars 2.1 to deduce that 9-5+2 is a list as follows.

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

<h2 id="e270ca1319a8a19beaad53b4e3df5f0e"></h2>
### 2.2.3 Parse trees (Concrete Syntax Tree)

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
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_parse_tree_2.2)
 	- Each node in the tree is labeled by a *grammar symbol*
 	- An interior node and its children correspond to a *production*
 		- the interior node corresponds to the head of the production
 		- the children to the body
 - from left to right, the leaves of a parse tree form the *yield* of the tree
 	- which is the string *generated* or *derived* from the nonterminal at the root of the parse tree
 	- in this example , the yield is 9-5+2
 - Any tree imparts a natural *left-to-right* order to its leaves

Another denition of the language (generated by a grammar) is as the ***set of strings*** that can be generated by some parse tree. 

The process of finding a parse tree for a given string of terminals is called ***parsing*** that string.

<h2 id="4ad96debb40880b43bd7d10f5554a448"></h2>
### 2.2.4 Ambiguity

A grammar can have more than one parse tree generating a given string of terminals. Such a grammar is said to be *ambiguous*.

Since a string with more than one parse tree usually has more than one meaning, we need to design unambiguous grammars for compiling applications, or to use ambiguous grammars with additional rules to resolve the ambiguities.

Example 2.5 : Suppose we used a single nontertninal ***string*** and did not dis­tinguish between *digits* and *lists* , as in Example 2.1 , We could have written the grammar:

```
string → string + string | string - string | 0|1|2|3|4|5|6|7|8|9
```

Merging the notion of *digit* and *list* into the nonterminal *string* makes superficial sense, because a single *digit* is a special case of a *list*.

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_figure2.6_tow_parse_tree.png)
 - The two trees for 9-5+2 correspond to the two ways of parenthesizing the expression: (9-5) +2 and 9- (5+2)
 - This second parenthesization gives the expression the unexpected value 2 rather than the customary value 6.

<h2 id="711cb58dcac9926888c6efb7c422cb65"></h2>
### 2.2.5 Associativity of Operators

 - 9+5+2 is equivalent to (9+5)+2 and 9-5-2 is equivalent to (9-5)-2.
 - When an operand like 5 has operators to its left and right, con­ventions are needed for deciding which operator applies to that operand
 - We say that the operator + *associates* to the left
 	- because an operand with plus signs on both sides of it, belongs to the operator to its left
 - In most programming languages the four arithmetic operators, addition, subtraction, multiplication, and division are *left-associative*.
 - Some common operators such as exponentiation are *right-associative*.
 - As another example, the assignment operator = in C and its descendants is right­ associative
 	- that is, the expression a=b=c is treated in the same way as the expression a=(b=c)

Strings like a=b=c with a right-associative operator are generated by the following grammar:

```
right → letter = right | letter
letter → a | b | ... | z
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compilers_fig2.7_associative.png)

Note that the parse tree for 9-5-2 grows down towards the left, whereas the parse tree for a=b=c grows down towards the right.

2.2.6 Precedence of Operators

Consider the expression 9+5 * 2. There are two possible interpretations of this expression: (9+5) * 2 or 9+(5 * 2). The associativity rules for + and * apply to occurrences of the same operator, so they do not resolve this ambiguity. Rules defining the relative precedence of operators are needed when more than one kind of operator is present.

We say that * has *higher* precedence than + if * takes its operands before + does. In ordinary arithmetic, multiplication and division have higher precedence than addition and subtraction. 


Example 2.6 : A grammar for arithmetic expressions can be constructed from a *table* showing the associativity and precedence of operators. We start with the four common arithmetic operators and a precedence table, showing the operators in order of *increasing precedence*.

 - Operators on the same line have the same associativity and precedence:

```
left-associative: + ­-
left-associative: * /
```

 - We create two nonterminals *expr* and *term* for the two levels of precedence
 	- expr for + , -
 	- term for * , / 
 - and an extra nonterminal *factor* for generating basic units in expressions. 
 	- The basic units in expressions are presently *digits* and *parenthesized* expressions. (目前只考虑 数字和括号)
 	

```
factor → digit | ( expr )
```

 - Now consider the binary operators, * and /, that have the highest prece­dence. Since these operators associate to the left, the productions are similar to those for lists that associate to the left.

```
term → term * factor 
	 | term / factor
	 | factor
```

 - Similarly, *expr* generates lists of terms separated by the additive operators.

```
expr → expr + term 
	 | expr - term
	 | term
```

 - The resulting grammar is therefore

```
expr → expr + term  | expr - term | term
term → term * factor | term / factor | factor
factor → digit | ( expr )
```

Generalizing the Expression Grammar:

 - we can think of a *factor* as an expression that cannot be "torn apart" by any operator. If the factor is a parenthesized expression, the parentheses protect against such "tearing", while if the factor is a single operand, it cannot be torn apart.
 - A *term* is an expression that can be torn apart by operators of the highest precedence: * and / , but not by the lower-precedence operators.
 - An *expression* can be torn apart by any operator.
 - We can generalize this idea to any number n of precedence levels. We need **n+1** nonterminals. 
 	- The first,like *factor* in Example 2.6, can never be torn apart. 
 		- Typically, the production bodies for this nonterminal are only single operands and parenthesized expressions. 
 	- Then, for each precedence level, there is one nonterminal representing expressions that can be torn apart only by operators at that level or higher. 
 		- Typically, the productions for this nonterminal have bodies representing uses of the operators at that level, plus one body that is just the nonterminal for the next higher level .


With this grammar ,

 - an expression is a list of terms separated by either + or - signs, 
 - and a term is a list of factors separated by * or / signs. 
 - Notice that any parenthesized expression is a factor, so with parentheses we can develop expressions that have arbitrarily deep nesting (and arbitrarily deep trees) .


Example 2.7: Keywords allow us to recognize statements(语句), since most state­ment begin with a keyword or a special character. Exceptions to this rule include assignments and procedure calls. The statements defined by the (ambiguous) grammar in Fig. 2.8 are legal in Java.

```
stmt → id = expression ;
	 | if ( expression ) stmt
	 | if ( expression ) stmt else stmt 
	 | while ( expression ) stmt
	 | do stmt while ( expression ) ;
	 | { stmts }
stmts → stmts stmt
	 | ε
```

Figure 2.8: A grammar for a subset of Java statements

In the first production for *stmt*, the terminal **id** represents any identifier. The productions for *expression* are not shown. The assignment statements specified by the first production are legal in Java, although Java treats = as an assignment operator that can appear within an expression. For example, Java allows a = b = c, which this grammar does not.

The nonterminal *stmts* generates a possibly empty list of statements. The second production for *stmts* generates the empty list ε . The first production generates a possibly empty list of statements followed by a statement.

The placement of semicolons is subtle; they appear at the end of every body that does not end in *stmt*. This approach prevents the build-up of semicolons after statements such as if- and while-, which end with nested substatements. When the nested substatement is an assignment or a do-while, a semicolon will be generated as part of the substatement.



2.3 Syntax-Directed translation

Syntax-directed translation is done by attaching rules or program fragments to productions in a grammar. 

For example, consider an expression *expr* generated by the production

```
expr → expr₁ + term
```

Here, *expr* is the sum of the two subexpressions *expr₁* and *term*. (The subscript in *expr₁* is used only to distinguish the instance of *expr* in the production body from the head of the production). We can translate *expr* by exploiting its structure, as in the following pseudo-code:

```
translate expr₁; 
translate term; 
handle +;
```

Using a variant of this pseudocode, we shall build a syntax tree for *expr* in Section 2.8 by building syntax trees for *expr₁* and *term* and then handling + by constructing a node for it. For convenience, the example in this section is the translation of infix expressions into postfix notation.

This section introduces two concepts related to syntax-directed translation:

 - ***Attributes***
 	- An *attribute* is any quantity associated with a programming construct. 
 	- Examples of attributes are data types of expressions, the num­ber of instructions in the generated code, or the location of the first in­struction in the generated code for a construct, among many other pos­sibilities. 
 	- Since we use grammar symbols (nonterminals and terminals) to represent programming constructs, we extend the notion of attributes from constructs to the symbols that represent them.
 - ***(Syntax-directed) translation schemes***. 
 	- A *translation scheme* is a notation for attaching program fragments to the productions of a grammar. 
 	- The program fragments are executed when the production is used during syn­tax analysis. 
 	- The combined result of all these fragment executions, in the order induced by the syntax analysis, produces the translation of the program to which this analysis/synthesis process is applied.

Syntax-directed translations will be used throughout this chapter to trans­late infix expressions into postfix notation, to evaluate expressions, and to build syntax trees for programming constructs. A more detailed discussion of syntax­ directed formalisms appears in Chapter 5.


### 2.3.1 Postfix Notation

The examples in this section deal with translation into *postfix notation*. The *postfix notation* for an expression *E* can be defined inductively as follows:

 1. If E is a variable or constant, then the postfix notation for E is E itself.
 2. If E is an expression of the form E₁ ***op*** E₂, where ***op*** is any binary operator, then the postfix notation for E is ***E₁' E₂' op***, where E₁' and E₂' are the postfix notations for E₁ and E₂ , respectively.
 3. If E is a parenthesized expression of the form (E₁), then the postfix notation for E is the same as the postfix notation for E₁ .


Example 2.8 : The postfix notation for (9-5) +2 is 95-2+. 

 - That is, the trans­lations of 9, 5, and 2 are the constants themselves, by rule (1). 
 - Then, the translation of 9-5 is 95- by rule (2). The translation of (9-5) is the same by rule (3). 
 - Having translated the parenthesized subexpression, we may apply rule (2) to the entire expression, with (9-5) in the role of E₁ and 2 in the role of E₂, to get the result 95-2+.

As another example, the postfix notation for 9- (5+2) is 952+-. That is, 5+2 is first translated into 52+, and this expression becomes the second argument of the minus sign.

***No parentheses are needed in postfix notation***, because the position and ***arity*** (number of arguments) of the operators permits only one decoding of a postfix expression. The "trick" is to repeatedly scan the postfix string from the left, until you find an operator. Then, look to the left for the proper number of operands, and group this operator with its operands. Evaluate the operator on the operands, and replace them by the result. Then repeat the process, continuing to the right and searching for another operator.


Example 2.9 : Consider the postfix expression 952+-3*. 

Scanning from the left, we first encounter the plus sign. Looking to its left we find operands 5 and 2. Their sum, 7, replaces 52+, and we have the string 97-3*. Now, the leftmost operator is the minus sign, and its operands are 9 and 7. Replacing these by the result of the subtraction leaves 23*. Last, the multiplication sign applies to 2 and 3, giving the result 6.  


### 2.3.2 Synthesized Attributes

The idea of associating quantities with programming constructs -for example, values and types with expressions- can be expressed in terms of grammars. 

 - We associate attributes with nonterminals and terminals. 
 - Then, we attach rules to the productions of the grammar; 
 	- these rules describe how the attributes are computed at those nodes of the parse tree where the production in question is used to relate a node to its children.

A *syntax-directed definition* associates

 1. With each grammar symbol, a set of attributes, and
 2. With each production, a set of semantic rules for computing the values of the attributes associated with the symbols appearing in the production

Attributes can be evaluated as follows. 

 - For a given input string x, construct a parse tree for x. 
 - Then, apply the semantic rules to evaluate attributes at each node in the parse tree, as follows.

Suppose a node N in a parse tree is labeled by the grammar symbol X . 

 - We write X.a to denote the value of attribute a of X at that node. 
 - A parse tree showing the attribute values at each node is called an annotated parse tree. 

 For example, Fig. 2.9 shows an annotated parse tree for 9-5+2 with an attribute t associated with the nonterminals *expr* and *term*. The value 95-2+ of the attribute at the root is the postfix notation for 9-5+2. We shall see shortly how these expressions are computed.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Compiler_attr_vallue_in_parse_tree.png)

 - An attribute is said to be *synthesized* if its value at a parse-tree node N is de­termined from attribute values at the children of N and at N itself. 
 	- Synthesized attributes have the desirable property that they can be evaluated during a sin­gle bottom-up traversal of a parse tree. 
 - In Section 5.1.1 we shall discuss another important kind of attribute: the "inherited" attribute. 
 	- Informally, inherited at­ tributes have their value at a parse-tree node determined from attribute values at the node itself, its parent, and its siblings in the parse tree.


Example 2.10 : The annotated parse tree in Fig. 2.9 is based on the syntax­ directed definition in Fig 2.10 for translating expressions consisting of digits separated by plus or minus signs into postfix notation. 

 - Each nonterminal has a string-valued attribute *t* that represents the postfix notation for the expression generated by that nonterminal in a parse tree. 
 - The symbol `‖` in the semantic rule is the operator for string concatenation.


PRODUCTION | SEMANTIC RULES
--- | ---
expr → expr₁ + term | expr.t = expr₁.t ‖ term.t ‖ '+' 
expr → expr₁ - term | expr.t = expr₁.t ‖ term.t ‖ '-'
expr → term 		| expr.t = term.t
term → 0 			| term.t = '0'
term → 1 			| term.t = '1'
...					| ...
term → 9			| term.t = '9'

Figure 2.10: Syntax-directed definition for infix to postfix translation

 - The postfix form of a digit is the digit itself; 
 	- e.g., the semantic rule associ­ated with the production `term → 9` defines *term.t* to be 9 itself whenever this production is used at a node in a parse tree. 
 	- The other digits are translated similarly. 
 - As another example, when the production *expr* → *term* is applied, the value of *term.t* becomes the value of *expr.t* .
 - The production *expr* → *expr₁* + *term* derives an expression containing a plus operator. 
 	- The left operand of the plus operator is given by *expr₁* and the right operand by *term*. 
 	- The semantic rule `expr.t = expr₁.t ‖ term.t ‖ '+'` associated with this production constructs the value of attribute *expr.t* by con­catenating the postfix forms *expr₁.t* and *term.t* of the left and right operands, respectively, and then appending the plus sign. 
 	- This rule is a formalization of the definition of "postfix expression." 


```
Convention Distinguishing Uses of a Nonterminal

The nonterminal appears unsubscripted in the head and with distinct subscripts in the body. 
These are all occurrences of the same nonterminal, and the subscript is not part of its name.
```

### 2.3.3 Simple Syntax-Directed Definitions

The syntax-directed definition in Example 2.10 has the following important property: the string representing the translation of the nonterminal at the head of each production is the *concatenation of the translations of the nonterminals in the production body*, in the same order as in the production, with some optional additional strings interleaved. A syntax-directed definition with this property is termed *simple* .

Example 2.11 : Consider the  rst production and semantic rule from Fig. 2.10:

PRODUCTION | SEMANTIC RULES 
--- | ---
expr → expr₁ + term | expr.t = expr₁.t ‖ term.t ‖ '+'  (2.5)

 - Here the translation *expr.t* is the concatenation of the translations of *expr₁* and *term*, followed by the symbol +
 - Notice that *expr₁* and *term* appear in the same order in both the production body and the semantic rule. 
 - There are no additional symbols before or between their translations. 
 - In this example, the only extra symbol occurs at the end.

When translation schemes are discussed, we shall see that a simple syntax­ directed definition can be implemented by printing only the additional strings, in the order they appear in the definition.


### 2.3.4 Tree Traversals

Tree traversals will be used for describing attribute evaluation and for specifying the execution of code fragments in a translation scheme. A traversal of a tree starts at the root and visits each node of the tree in some order.

A *depth-first* traversal starts at the root and recursively visits the children of each node in any order, not necessarily from left to right. It is called "depth­ first" because it visits an unvisited child of a node whenever it can, so it visits nodes as far away from the root (as "deep" ) as quickly as it can.

 - a depth first traversal that visits the children of a node in left-to-right order
 - In this traversal, we have included the action of evaluating translations at each node, just before we finish with the node 
 	- that is, after translations at the children have surely been computed. 
 - In general, the actions associated with a traversal can be whatever we choose, or nothing at all.












