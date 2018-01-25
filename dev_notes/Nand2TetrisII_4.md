...menustart

 - [Week4  Compiler I : Syntax Analysis](#30cc36d5a2b0e1c1cbad3f796a36e58d)
     - [Unit 4.2: Lexical Analysis](#a6e48139193e1fc0ff363058aa4ce501)
         - [Tokenizing (first approximation)](#5bc49567966c595b4a1fb29fd9ec6c69)
         - [Jack tokens](#f7236a026647622e46d365447d25d104)
         - [Jack tokenizer](#af703fb4c8a243566c3896834a1b2860)
     - [Unit 4.3: Grammars](#6e417ba0facd9e0860964597560025b5)
     - [Unit 4.4: Parse Trees](#82afddbe6b0bdf72c94e81cdc1677109)
     - [Unit 4.5: Parser Logic](#aa2314b6b2014b9f4b3a24f0ddfeb4b9)
         - [Parser design](#11d1b10a8e1eefdd441063908053af6f)
         - [Some observations about grammars and parsing](#d0310f6535296147836c000e8cc3c48a)
     - [Unit 4.6: The Jack Grammar](#87609c9974b897143d9c161013658dba)

...menuend


<h2 id="30cc36d5a2b0e1c1cbad3f796a36e58d"></h2>

# Week4  Compiler I : Syntax Analysis


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compiler_roadmap.png)

<h2 id="a6e48139193e1fc0ff363058aa4ce501"></h2>

## Unit 4.2: Lexical Analysis

<h2 id="5bc49567966c595b4a1fb29fd9ec6c69"></h2>

### Tokenizing (first approximation)

 - Source file :  
    - stream of characters 
 - after tokenizing :
    - stream of tokens
 - A *token* is a string of characters that has a meaning 

<h2 id="f7236a026647622e46d365447d25d104"></h2>

### Jack tokens 

 - keyword
    - class, char, while, ...
 - symbol 
    - `{}`, `/`, `=`
 - integer constant
    - 0 ... 32767
 - string constant
 - identifier


<h2 id="af703fb4c8a243566c3896834a1b2860"></h2>

### Jack tokenizer 

- Handles the compiler's input
- Allows advancing the input
- Supplies the *current token's value and type*
    
```xml
...
<keyword> if </keyword>
<symbol> ( </symbol>
<identifier> x </identifier>
...
```

<h2 id="6e417ba0facd9e0860964597560025b5"></h2>

## Unit 4.3: Grammars

 - The artifact that defines in what order we can put tokens together legibly is called **grammar**
 - A *grammar* is a set of rules, descriing how tokens can be combined to create valid language constructs
 - Each *rule* consists of a left-hand side , listing a template's name , and a right-hand side , describing how the template is composed:
    - Terminal rule: right-hand side includes constants only
    - Non-terminal rule: all other rules 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_grammar_subset.png)


 - Parsing:
    - determining if a given input conforms to a grammar
    - In the process, uncovering the grammatical structure of the given input 

<h2 id="82afddbe6b0bdf72c94e81cdc1677109"></h2>

## Unit 4.4: Parse Trees

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_parse_tree.png)

<h2 id="aa2314b6b2014b9f4b3a24f0ddfeb4b9"></h2>

## Unit 4.5: Parser Logic


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_grammar_subset.png)

```
class CompilationEngine {
    compileStatements() {
        // code for compiling statments    
    }    
    compileIfStatement() {
        // code for compiling if statment
    }
    ...
    compileTerm() {
        // code for compiling a term     
    }
}   
```


Guild lines for compilcation engine :

- CompilationEngine is going to consist of a set of methods ,
    - one method almost for every non-terminal rule  in the corresponding grammar 

- Parsing logic :  eg: `while (count < 100>) { let count = count +1 ; }`
    - Follow the right-hand side of the rule, and parse the input accordingly 
        - from the key word `while` , we know it is a while statement
        - then we know the next token should be `(` , oh , it is a terminal rule , we can record it in the output file
        - so on , and so forth
    - If the right-hand side specifies a non-terminal rule xxx , call compileXXX . 
    - Do this recursively.


<h2 id="11d1b10a8e1eefdd441063908053af6f"></h2>

### Parser design 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_parser_design.png)

<h2 id="d0310f6535296147836c000e8cc3c48a"></h2>

### Some observations about grammars and parsing 

 - LL grammar: can be parsed by a recursive descent parser **without backtracking**
    - LL is quite friendly : once you start to parse something, you never have to go back .
    - When you make a decision that what you have is a while statement of if statement , you don't have to kind of retract your progress and find out that you made a mistake and you had to parse it in a different way. 
 - LL(k) parser:  a parser that needs to look ahead **at most** k tokens in order to determine which rule is applicable. 
    - ie. `x*foo , x*foo[12], x*foo.val`  , when the current token is `foo` ,  we don't know whether `foo` is a variable / array / object , we need at most 1 token more.
 - The grammar that we saw so far is LL(1). 


<h2 id="87609c9974b897143d9c161013658dba"></h2>

## Unit 4.6: The Jack Grammar

### Lexical elements

 - 5 categories of terminla elements (tokens)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_grammar_lexical_elements.png)

### Program Structure 

 - A Jack program is a collection of *classes*, each appearing in a separate file , and each compiled separately.  
 - Each class is structured as follows:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_grammar_program_structure.png)

### Statements 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_grammar_statement.png)

### Expressions


