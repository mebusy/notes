
# Building 

```
yacc –d bas.y 	# create y.tab.h, y.tab.c
lex bas.l 		# create lex.yy.c
cc lex.yy.c y.tab.c –obas.exe  # compile/link
```

# Lex

```
... definitions ...
%%
... rules ...
%%
... subroutines ...

```

 - The first %% is always required, as there must always be a rules section.
 	- if we don’t specify any rules then the default action is to match everything and copy it to output
 	- Defaults for input and output are stdin and stdout


Here is the same example with defaults explicitly coded:

```
%%

    /* match everything except newline */
.   ECHO;
    /* match newline */
\n  ECHO;

%%

int yywrap(void) {
	return 1;
}

int main(void) {
    yylex();
	return 0;
}
```


 - Two patterns have been specified in the rules section.  “.” and “\n”
	- Each pattern must begin in column one
		- Anything not starting in column one is copied verbatim to the generated C file
		- 比如 上边的注释都会 copy 到 源文件中
 	- followed by whitespace (space, tab or newline) and an optional action associated with the pattern. (eg, **ECHO** )
 	- The action may be a single C statement, or multiple C statements, enclosed in braces.
 - Several macros and variables are predefined by lex. 
 	- **ECHO** is a macro that writes code matched by the pattern. 
 	- This is the default action for any unmatched strings. 
 	- Typically, ECHO is defined as:
 		```
 		#define ECHO fwrite(yytext, yyleng, 1, yyout)
 		```
 	- Variable **yytext** is a pointer to the matched string (NULL-terminated) 
 	- **yyleng** is the length of the matched string. 
 	- Variable **yyout** is the output file and defaults to stdout.
 	- Function **yywrap** is called by lex when input is exhausted.
 		- Return 1 if you are done or 0 if more processing is required.
 	- In this case we simply call **yylex** that is the main entry point for lex. 
 		- Some implementations of lex include copies of main and yywrap in a library thus eliminating the need to code them explicitly. 

 
Here is a program that does nothing at all. All input is matched but no action is associated with any
pattern so there will be no output.

```
%%
.\n
```

The following example prepends line numbers to each line in a file. The input file for lex is **yyin** and defaults to **stdin**.

```
%{
	int yylineno;
%}

%%

^(.*)\n 	{ printf("%4d\t%s", yylineno, yytext); ++yylineno; }

%%

int yywrap(void) {
	return 1;
}

int main(int argc, char *argv[]) {
	yyin = fopen(argv[1], "r");
	yylex();
	fclose(yyin);
}

```

> Some implementations of lex predefine and calculate **yylineno**. 

 - The definitions section is composed of substitutions, code, and start states.
 	- Code in the definitions section is simply copied as-is to the top of the generated C file and must be bracketed with **“%{“** and **“%}”** markers
 	- Substitutions simplify pattern-matching rules , For example, we may define digits and letters:
 		```
 		digit    [0-9]
		letter   [A-Za-z]
		%%
		{letter}({letter}|{digit})*
 		```
 		- surrounded by braces **{letter}** to distinguish them from literals


# Yacc

```
... definitions ...
%%
... rules ...
%%
... subroutines ...
```

 - The definitions section consists of token declarations and C code bracketed by “%{“ and “%}”. 
 - The BNF grammar is placed in the rules section and 
 - user subroutines are added in the subroutines section. 

Here is the definitions section for the yacc input file:

```
%token INTEGER
```

- This definition declares an **INTEGER** token
- Yacc generates a parser in file **y.tab.c** and an include file, **y.tab.h**:
	- Lex includes this file and utilizes the definitions for token values
- To obtain tokens yacc calls **yylex**
	- Function **yylex** has a return type of int that returns a token
	- Values associated with the token are returned by lex in variable **yylval**. For example , in xx.l file
		```
		[0-9]+ {
					yylval = atoi(yytext); 
					return INTEGER;
			   }
		```
		- would store the value of the integer in **yylval**
		- return token **INTEGER** to yacc
- Token values 0-255 are reserved for character values
	- For example, if you had a rule such as
	- `[-+]         return *yytext;        /* return operator */`
	- the character value for minus or plus is returned

Here is the complete lex input specification for our calculator:

```
%{
#include <stdlib.h>
void yyerror(char *);
#include "y.tab.h"
%}

%% 

[0-9]+	{
			yylval = atoi(yytext);
    		return INTEGER;
		}		
[-+\n]	return *yytext;
[ \t]	; /* skip whitespace */
.		yyerror("invalid character");

%%

int yywrap(void) {
       return 1;
}
```

> 只匹配 数字, +/-, 空白， 换行， 其他字符报错

 - Internally yacc maintains two stacks in memory; a parse stack and a value stack. 
 - The parse stack contains terminals and nonterminals that represent the current parsing state. 
 - The value stack is an array of YYSTYPE elements and associates a value with each element in the parse stack. 

For example when lex returns an INTEGER token yacc shifts this token to the parse stack. At the same time the corresponding yylval is shifted to the value stack. The parse and value stacks are always synchronized so finding a value related to a token on the stack is easily accomplished. Here is the yacc input specification for our calculator:

```

%{
    #include <stdio.h>
    int yylex(void);
    void yyerror(char *);
%}
%token INTEGER

%%

program:
        program expr '\n'	{ printf("%d\n", $2); }
        |
        ;
expr:	
		INTEGER				{ $$ = $1; }
		| expr '+' expr		{ $$ = $1 + $3; }
		| expr '-' expr		{ $$ = $1 - $3; }
		;
%%
void yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
}
int main(void) {
    yyparse();
	return 0; 
}


```

The rules section resembles the BNF grammar. 

The left-hand side of a production, or nonterminal, is entered left-justified and followed by a colon. 
This is followed by the right-hand side of the production. Actions associated with a rule are entered in braces.

With left-recursion, we have specified that a program consists of zero or more expressions. Each expression terminates with a newline. When a newline is detected we print the value of the expression. When we apply the rule

```
expr: expr '+' expr { $$ = $1 + $3; }
```

we replace the right-hand side of the production in the parse stack with the left-hand side of the same production. 

In this case we pop “expr '+' expr” and push “expr”. We have reduced the stack by popping three terms off the stack and pushing back one term. 

We may reference positions in the value stack in our C code by specifying “$1” for the first term on the right-hand side of the production, “$2” for the second, and so on. “$$” designates the top of the stack after reduction has taken place. The above action adds the value associated with two expressions, pops three terms off the value stack, and pushes back a single sum. As a consequence the parse and value stacks remain synchronized.

Numeric values are initially entered on the stack when we reduce from INTEGER to expr. After INTEGER is shifted to the stack we apply the rule

```
expr: INTEGER        { $$ = $1; }
```

The **INTEGER** token is popped off the parse stack followed by a push of **expr**.  For the value stack we pop the integer value off the stack and then push it back on again.  Finally, when a newline is encountered, the value associated with **expr** is printed. 

In the event of syntax errors yacc calls the user-supplied function **yyerror**. 

This example still has an ambiguous grammar. Although yacc will issue shift-reduce warnings it will still process the grammar using shift as the default operation.

# Practice, Part II

 - + arithmetic operators multiply and divide. 
 - + Parentheses may be used to over-ride operator precedence, 
 - + single-character variables may be specified in assignment statements.


The lexical analyzer returns **VARIABLE** and **INTEGER** tokens. 

For variables **yylval** specifies an index to the symbol table ***sym***. When **INTEGER** tokens are returned, **yylval** contains the number scanned. Here is the input specification for lex:

```
%{
       #include <stdlib.h>
       void yyerror(char *);
       #include "y.tab.h"
%}

%%

   /* variables */
[a-z]       {
               yylval = *yytext - 'a';
               return VARIABLE;
           }
   /* integers */
[0-9]+      {
               yylval = atoi(yytext);
               return INTEGER;
           }
   /* operators */
[-+()=/*\n] { return *yytext; }
   /* skip whitespace */
[ \t]        ;
   /* anything else is an error */
.               yyerror("invalid character");

%%

int yywrap(void) {
       return 1;
}
```

> 3.l

The input specification for yacc follows. 

 - We may specify %left, for left-associative or %right for right associative. 
 - The last definition listed has the highest precedence. 
 	- Using this simple technique we are able to disambiguate our grammar.

```

%token INTEGER VARIABLE
%left '+' '-'
%left '*' '/'
%{
	#include <stdio.h>
    void yyerror(char *);
    int yylex(void);
    int sym[26];
%}
%%
program:
		program statement '\n'
				|
				;
statement:
        expr					{ printf("%d\n", $1); }
        | VARIABLE '=' expr		{ sym[$1] = $3; }
        ;
expr:
        INTEGER
		| VARIABLE		{ $$ = sym[$1]; }
		| expr '+' expr	{$$=$1+$3;}
		| expr '-' expr	{$$=$1-$3;}
		| expr '*' expr	{$$=$1*$3;}
		| expr '/' expr {$$=$1/$3;}		
		| '(' expr ')'	{$$=$2;} 
		;
%%
void yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
}
int main(void) {
    yyparse();
	return 0; 
}
```

> 3.y


# Calculator

This version of the calculator is substantially more complex than previous versions. Major changes include control constructs such as **if-else** and **while**. 

In addition a syntax tree is constructed during parsing. After parsing we walk the syntax tree to produce output. Three versions of the tree walk routine are supplied:

 - an interpreter that executes statements during the tree walk
 - a compiler that generates code for a hypothetical stack-based machine
 - a version that generates a syntax tree of the original program

To make things more concrete, here is a sample program,

```
x = 0;
while (x < 3) {
	print x;
	x = x + 1; 
}
```

The include file contains declarations for the syntax tree and symbol table. 

 - Symbol table (**sym**) allows for single-character variable names. 
 - A node in the syntax tree may hold a constant (**conNodeType**), an identifier (**idNodeType**), or an internal node with an operator (**oprNodeType**). 

A union encapsulates all three variants and **nodeType.type** is used to determine which structure we have.

The lex input file contains patterns for **VARIABLE** and **INTEGER** tokens. In addition, tokens are defined for 2-character operators such as **EQ** and **NE**. Single-character operators are simply returned as themselves.

The yacc input file defines **YYSTYPE**, the type of **yylval**, as

```
%union {
       int iValue;
       char sIndex;
       nodeType *nPtr;
};
```

This causes the following to be generated in y.tab.h:

```
typedef union {
    int iValue;
	char sIndex;
    nodeType *nPtr;
} YYSTYPE;
extern YYSTYPE yylval;

/* integer value */
/* symbol table index */
/* node pointer */
```










