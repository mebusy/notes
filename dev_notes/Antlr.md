...menustart

- [Antlr](#c120884bab20a4738205e724e2b9d501)
- [install](#19ad89bc3e3c9d7ef68b89523eff1987)
- [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
- [表达式求值](#4564981cafbb7b9957cbeba1a42df75f)
- [The Definitive ANTLR 4 Reference : Part I](#bb02524b3a160a2990a57229f860e16f)
- [CHAPTER 1. Meet ANTLR](#bc400908d979a205604e4010630b4f6b)
    - [1.1 Install](#93164cfae6b8aa76e5b75cf93496064b)
    - [1.2 Executing ANTLR and Testing Recognizers](#0dec518672c3eef4cf20bf32e552c95b)
- [Chapter 4. A Quick Tour](#2f3e2a80e82065ea6587c0af3e180bb1)
    - [Importing Grammars](#db53b037af7f9dc70111a66512e3f27c)
    - [Building a Calculator Using a Visitor](#5da8502a515f881c0dab186a4e69ba5d)
    - [Building a Translator with a Listener](#29ca8f4c682b4e3bc0abe5c4aba7ce42)
    - [Making Things Happen During the Parse](#8409c9e2ffda1c59af131d49166f5af9)
        - [Embedding Arbitrary Actions in a Grammar](#993287912c88deb1c536a0cdfa6b986c)
    - [Cool Lexical Features](#dd0c712b3dd888f10c8d002c78fd86f1)
        - [Island Grammars: Dealing with Different Formats in the Same File](#e2dda0a9000b06f1fe391c2e56980f3b)
        - [Rewriting the Input Stream](#668eb3905506ca0d643daf390a1306f4)
        - [Sending Tokens on Different Channels](#4475860fa6324867936f24300f027790)

...menuend


<h2 id="c120884bab20a4738205e724e2b9d501"></h2>


# Antlr

<h2 id="19ad89bc3e3c9d7ef68b89523eff1987"></h2>


# install



<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>


# Example

 - 在 Anltr 中，算法的优先级需要通过文法规则的嵌套定义来体现
 - Antlr 中语法定义和词法定义通过规则的第一个字符来区别， 规定语法定义符号的第一个字母小写，而词法定义符号的第一个字母大写。
    - skip() 是词法分析器类的一个方法 ?
 - Antlr 支持多种目标语言，可以把生成的分析器生成为 Java，C#，C，Python，JavaScript 等多种语言，默认目标语言为 Java
    - 通过 options {language=?;} 来改变目标语言

```
antlr4 Expr.g4
javac Expr*.java
# show parser tree in GUI
grun Expr prog -gui 
4+2
^D

# or output parser tree in LISP format
grun Expr prog -tree
```

<h2 id="4564981cafbb7b9957cbeba1a42df75f"></h2>


# 表达式求值

```
// target: a simple language
begin
    let a be 5
    let b be 10
    add 3 to b
    add b to a
    add a to b
    print b
    print 3
end
```

```
grammar GYOO;
program   : 'begin' statement+ 'end';

statement : assign | add | print ;

assign    : 'let' ID 'be' (NUMBER | ID) ;
print     : 'print' (NUMBER | ID) ;
add       : 'add' (NUMBER | ID) 'to' ID ;

ID     : [a-z]+ ;
NUMBER : [0-9]+ ;
WS     : [ \n\t]+ -> skip;
```

- create a new Java class that is a subclass of the GYOOBaseListener class.
- Inside MyListener, you need to tell ANTLR’s parser what it should do every time it encounters a specific type of token.
    - For example, every time it encounters an assign statement, it must assign a value to a variable. 
    - You can do so by overriding the enterAssign() and exitAssign() methods.

- Run the Parser
    - you must first create an ANTLRInputStream object and pass a FileInputStream to it. 
    - Next, you must create a GYOOLexer object based on the InputStream.
    - You can now create a stream of tokens using the lexer, and pass it as an input to a GYOOParser object.
    - You must, of course, not forget to add the MyListener class as a listener to the GYOOParser object.
    - At this point, you can call the program() method to start the parsing.

```java
public static void main(String[] args) {
    try {
        ANTLRInputStream input = new ANTLRInputStream(
            new FileInputStream(args[0]));    

        GYOOLexer lexer = new GYOOLexer(input);
        GYOOParser parser = new GYOOParser(new CommonTokenStream(lexer));
        parser.addParseListener(new MyListener());

        // Start parsing
        parser.program(); 
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

<h2 id="bb02524b3a160a2990a57229f860e16f"></h2>


# The Definitive ANTLR 4 Reference : Part I 

 - `ALL(*)`  

```
expr : expr '*' expr // match subexpressions joined with '*' operator 
    | expr '+' expr // match subexpressions joined with '+' operator 
    | INT // matches simple integer atom
;
```

 - ANTLR v4 automatically generates parse-tree walkers in the form of *listener* and *visitor* pattern implementations. 

<h2 id="bc400908d979a205604e4010630b4f6b"></h2>


# CHAPTER 1. Meet ANTLR

<h2 id="93164cfae6b8aa76e5b75cf93496064b"></h2>


## 1.1 Install

http://www.antlr.org/

```
OS X
$ cd /usr/local/lib
$ sudo curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.7-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```

<h2 id="0dec518672c3eef4cf20bf32e552c95b"></h2>


## 1.2 Executing ANTLR and Testing Recognizers

 - list token
    - `grun Hello r -tokens`
    - start the TestRig on grammar Hello at rule r
 - print parse tree
    - `grun Hello r -tree`

options | desc
--- | ---
-tokens | prints out the token stream.
-tree | prints out the parse tree in LISP form.
-gui | displays the parse tree visually in a dialog box.
-ps | file.ps generates a visual representation of the parse tree in PostScript and stores it in file.ps. 
-encoding encodingname | specifies the test rig input file encoding if the current locale would not read the input properly.
-trace | prints the rule name and current token upon rule entry and exit.
-diagnostics | turns on diagnostic messages during parsing. This generates messages only for unusual situations such as ambiguous input phrases.
-SLL | uses a faster but slightly weaker parsing strategy.


<h2 id="2f3e2a80e82065ea6587c0af3e180bb1"></h2>


# Chapter 4. A Quick Tour

<h2 id="db53b037af7f9dc70111a66512e3f27c"></h2>


## Importing Grammars

```
// tour/CommonLexerRules.g4
lexer grammar CommonLexerRules; // note "lexer grammar"
ID : [a-zA-Z]+ ;    
INT : [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS : [ \t]+ -> skip ; // toss out whitespace
```

```
// tour/LibExpr.g4
grammar LibExpr; // Rename to distinguish from original
import CommonLexerRules; // includes all rules from CommonLexerRules.g4 /** The start rule; begin parsing here. */
prog: stat+ ;
...
```

<h2 id="5da8502a515f881c0dab186a4e69ba5d"></h2>


## Building a Calculator Using a Visitor

 - First, we need to label the alternatives of the rules.
    - The labels can be any identifier that doesn’t collide with a rule name
 - Without labels on the alternatives, ANTLR generates only one visitor method per rule
 - In our case, we’d like a different visitor method for each alternative so that we can get different “events” for each kind of input phrase. 
 - Labels appear on the right edge of alternatives and start with the # symbol 

```
// LabeledExpr.g4
stat:   expr NEWLINE            # printExpr
    | ID '=' expr NEWLINE       # assign
    | NEWLINE                   # blank
    ;
expr: expr op=('*'|'/') expr    # MulDiv 
    | expr op=('+'|'-') expr    # AddSub 
    | INT                       # int 
    | ID                        # id 
    | '(' expr ')'              # parens 
    ;
```

 - Next, let’s define some token names for the operator literals so that, later, we can reference token names as Java constants in the visitor.

```
// LabeledExpr.g4
MUL :'*' ; // assigns token name to '*' used above in grammar 
DIV :'/' ;
ADD :'+' ;
SUB :'-' ;
```

```base
antlr4 -no-listener -visitor LabeledExpr.g4
```

```java
// example , p56
/** ID '=' expr NEWLINE */
@Override
public Integer visitAssign(LabeledExprParser.AssignContext ctx) {
    String id = ctx.ID().getText(); // id is left-hand side of '='
    int value = visit(ctx.expr()); // compute value of expression on right memory.put(id, value); // store it in our memory
    return value;
}
```

<h2 id="29ca8f4c682b4e3bc0abe5c4aba7ce42"></h2>


## Building a Translator with a Listener 

 - Imagine your boss assigns you to build a tool that generates a Java interface file from the methods in a Java class definition.
 - Preserve whitespace and comments within the bounds of the method signature.

<h2 id="8409c9e2ffda1c59af131d49166f5af9"></h2>


## Making Things Happen During the Parse

<h2 id="993287912c88deb1c536a0cdfa6b986c"></h2>


### Embedding Arbitrary Actions in a Grammar

 - We can compute values or print things out on-the-fly during parsing if we don’t want the overhead of building a parse tree. 
 - p63

<h2 id="dd0c712b3dd888f10c8d002c78fd86f1"></h2>


## Cool Lexical Features

<h2 id="e2dda0a9000b06f1fe391c2e56980f3b"></h2>


### Island Grammars: Dealing with Different Formats in the Same File

 - All the sample input files we’ve seen so far contain a single language, but there are common file formats that contain multiple languages. 
 - For example, the @author tags and so on inside Java document comments follow a mini language; everything outside the comment is Java code. 
 - These are often called **island grammars**.
 - ANTLR provides a well-known lexer feature called *lexical modes* that lets us deal easily with files containing mixed formats.
    - The basic idea is to have the lexer switch back and forth between modes when it sees special sentinel character sequences.
 - XML is a good example.
    - An XML parser treats everything other than tags and entity references (such as &pound;) as text chunks.
    - When the lexer sees <, it switches to “inside” mode and switches back to the default mode when it sees > or />.


```
OPEN: '<' -> pushMode(INSIDE) ;
COMMENT : '<!--' .*? '-->'  -> skip ;
...

// ----------------- Everything INSIDE of a tag ---------------------
mode INSIDE;

CLOSE : '>'             -> popMode ; // back to default mode 
SLASH_CLOSE : '/>'      -> popMode ;
EQUALS : '=';                       
STRING : '"' .*? '"' ;
...
```

<h2 id="668eb3905506ca0d643daf390a1306f4"></h2>


### Rewriting the Input Stream

 - Let’s build a tool that processes Java source code to insert serialization identifiers, serialVersionUID, for use with java.io.Serializable
    -  (like Eclipse does automatically). 
 - We want to avoid implementing every listener method in a JavaListener interface, generated from a Java grammar by ANTLR, just to capture the text and print it back out.
 - p68

<h2 id="4475860fa6324867936f24300f027790"></h2>


### Sending Tokens on Different Channels

 - The secret to preserving but ignoring comments and whitespace is to send those tokens to the parser on a “hidden channel.”


```
COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN) // match anything between /* and */ 
    ;
WS  :   [ \r\t\u000C\n]+ -> channel(HIDDEN)
    ;
```

 - The -> channel(HIDDEN) is a lexer command like the -> skip we discussed before.
 - In this case, it sets the channel number of these tokens so that it’s ignored by the parser. 




