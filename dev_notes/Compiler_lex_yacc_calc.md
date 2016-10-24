...menustart

 - [Yacc](#f4892ae9e5ea764a416fcc3b54a5bad9)
	 - [A Yacc Parser](#04c3eaf154277491767399176f9e1cab)
	 - [The Lexer](#9186d80d21b4c0a934c9a685bf9b3e78)
	 - [Arithmetic Expressions and Ambiguity](#c22bb56c30e059edbf2ee5f6a7177e48)
	 - [Variables and Typed Tokens](#f30b224b5f5b850b587e0d7b3e6ce825)
	 - [Symbol Tables](#743974c76894dcbff127f41b4dcaa71b)
	 - [Functions and Reserved Words](#8c439d47137d2b02b587a9cb733a993a)
	 - [Reserved Words in the Symbol Table](#3ffc9c6bc2ffcb3c6cd4ac1be2b51ae4)

...menuend




<h2 id="f4892ae9e5ea764a416fcc3b54a5bad9"></h2>
## Yacc

<h2 id="04c3eaf154277491767399176f9e1cab"></h2>
### A Yacc Parser

```
%token NAME NUMBER

%{
#include <stdio.h>
void yyerror(char *s) ;
%}

%%

statment: 	NAME '=' expression
		|	expression	{ printf("= %d\n" , $1); }
		;

expression:	expression '+' NUMBER	{ $$ = $1 + $3; }
		|	expression '-' NUMBER	{ $$ = $1 - $3; }
		|	NUMBER					{ $$ = $1; }
		;

%%

	/* needed for MacOSX */
void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}

int main(void) {
    yyparse();
	return 0; 
}
```


<h2 id="9186d80d21b4c0a934c9a685bf9b3e78"></h2>
### The Lexer

Here is is a simple lexer to provide tokens for our parser:

```
%{
#include "y.tab.h"
extern int yylval ;
%}

%%

[0-9]+	{ yylval = atoi(yytext); return NUMBER; }
[ \t]	;    /* ignore whitespace */
\n		return 0 ; /* logical EOF  */
. 		return yytext[0] ;  /*very common catch-all */

%%

	/* needed for MacOSX */
int yywrap(void) {
	return 1 ;
}
```

Wheneverthe lexer returns a token to the parser, if the token has an associated value, the lexer must store the value in **yylval** before returning. 

In this first example, we explicitly declare **yylval**. In more complex parsers, yacc defines **yylval** as a union and puts the definition in *y.tab.b* .



<h2 id="c22bb56c30e059edbf2ee5f6a7177e48"></h2>
### Arithmetic Expressions and Ambiguity

> calc.y

```

%{
#include <stdio.h>
void yyerror(char *s) ;
%}

%token NAME NUMBER
%left '-' '+'
%left '*' '/'
%nonassoc UMINUS

%%

statment: 	NAME '=' expression
		|	expression	{ printf("= %d\n" , $1); }
		;

expression:	expression '+' expression	{ $$ = $1 + $3; }
		|	expression '-' expression	{ $$ = $1 - $3; }
		|	expression '*' expression	{ $$ = $1 * $3; }
		|	expression '/' expression	{ if ($3==0)
										yyerror("divide by 0");
									  else
									  	$$ = $1 / $3; 
									}
		|	'-' expression	%prec UMINUS		{ $$ = -$2; }
		|	'(' expression	')'		{ $$ = $2; }
		|	NUMBER					{ $$ = $1; }
		;

%%

	/* needed for MacOSX */
void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}

int main(void) {
    yyparse();
	return 0; 
}
```

here, we use '%prec UMINUS' to tell yacc to use the precedence of UMINUS   for this production .




<h2 id="f30b224b5f5b850b587e0d7b3e6ce825"></h2>
### Variables and Typed Tokens

to handle variables with single letter names.

Since there are only 26 single letters (lowercase only for the moment) we can simply store the variables in a 26 entry array, which we call **vbItable**.

We also extend it to handle multiple expressions, one per line, and to use floating point values


> calc.y

```
%{
#include <stdio.h>
void yyerror(char *s) ;

double vbltable [26] ;   /* 1 */
%}


%union {				/* 2 */
	double dval;
	int vblno;
}

%token <vblno> 	NAME			/* 3 */
%token <dval>	NUMBER
%left '-' '+'
%left '*' '/'
%nonassoc UMINUS

%type <dval> expression		/* 4 */

%%

	
statement_list:	statement '\n'		/* 5 */
		| 		statement_list statement '\n'
		;

statement: 	NAME '=' expression		{ vbltable[$1] = $3;  }   /* 6 */
		|	expression	{ printf("= %g\n" , $1); }
		;

expression:	expression '+' expression	{ $$ = $1 + $3; }
		|	expression '-' expression	{ $$ = $1 - $3; }
		|	expression '*' expression	{ $$ = $1 * $3; }
		|	expression '/' expression	{ if ($3==0.0)		/* 7 */
										yyerror("divide by 0");
									  else
									  	$$ = $1 / $3; 
									}
		|	'-' expression	%prec UMINUS		{ $$ = -$2; }
		|	'(' expression	')'		{ $$ = $2; }
		|	NUMBER					{ $$ = $1; }
		|	NAME					{ $$ = vbltable[$1]; }		/* 8 */
		;
%%

	/* needed for MacOSX */
void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}

int main(void) {
    yyparse();
	return 0; 
}
```


> calc.l

```

%{
#include "y.tab.h"
#include "math.h"
	/*extern int yylval ;*/
extern double vbltable[26];
%}

%%

([0-9]+|([0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?)  	{ yylval.dval = atof(yytext); return NUMBER; }

[ \t]	;    /* ignore whitespace */

[a-z]	{yylval.vblno = yytext[0] - 'a' ; return NAME; }

"$" 	{return 0;  /* logical EOF  end of input */}

\n		|
. 		return yytext[0] ;  /*very common catch-all */

%%

	/* needed for MacOSX */
int yywrap(void) {
	return 1 ;
}
```



To define the possible symbol types , we add a **%union** declaration:

```
%union { 
	double dval;
	int vblno;
}
```

It will be copied to *y.tab.h* as the type **YYSTYPE** , to define ***yylval***.

```
#define NAME 258
#define NUMBER 259
#define UMINUS 260

typedef union  
{
	double dval;
	int vblno;
} YYSTYPE;

extern YYSTYPE yylval;
```

We have to tell the parser which symbols use which type of value.

```
%token <vblno> 	NAME			
%token <dval>	NUMBER
```


The new declaration **%type** sets the type for non-terminals which otherwise need no declaration.

```
%type <dval> expression	
```


<h2 id="743974c76894dcbff127f41b4dcaa71b"></h2>
### Symbol Tables

Now we add the ability to use longer variable names.

This means we need a *symbol table*, a structure that keeps track of the names in use.

Since the symbol table requires a data structure shared between the lexer and parser, we created a header file *ch3hdr.h* .

This symbol table is an array of structures each containing the name of the variable and its value. We also declare a routine **symlook()** which takes a name as a text string and returns a pointer to the appropriate symbol table entry, adding it if it is not alreadythere.


> ch3hdr.h :

```c
#define NSYMS	20 /* maximum number of symbols */
struct symtab {
	char *name;
	double value; 
} symtab[NSYMS];

struct symtab *symlook( ) ;
```


The parser changes only slightly to use the symbol table . The value for a **NAME** token is now a pointer into the symbol table rather than an index as before.

 - We change the **%union** and call the pointer field **symp**.
 - We use **strdup()** to make a permanent copy of the name string.
 	- Since each subsequent token overwrites **yytext**, we need to make a copy ourselves here.
 - Sequential search is too slow for symbol tables of appreciable size, so use hashing or some other faster search function.


> calc.y

```



%{
#include "ch3hdr.h"  /* 1 */
#include <stdio.h>		
void yyerror(char *s) ;

double vbltable [26] ;   
%}


%union {				 
	double dval;
	/*int vblno;*/
	struct symtab *symp;	/* 2 */
}

%token <symp> NAME			 /* 3 */
%token <dval>	NUMBER
%left '-' '+'
%left '*' '/'
%nonassoc UMINUS

%type <dval> expression		 

%%

	
statement_list:	statement '\n'		 
		| 		statement_list statement '\n'
		;

statement: 	NAME '=' expression		{ $1->value = $3; }   /* 4 */
		|	expression	{ printf("= %g\n" , $1); }
		;

expression:	expression '+' expression	{ $$ = $1 + $3; }
		|	expression '-' expression	{ $$ = $1 - $3; }
		|	expression '*' expression	{ $$ = $1 * $3; }
		|	expression '/' expression	{ if ($3==0.0)		  
										yyerror("divide by 0");
									  else
									  	$$ = $1 / $3; 
									}
		|	'-' expression	%prec UMINUS		{ $$ = -$2; }
		|	'(' expression	')'		{ $$ = $2; }
		|	NUMBER					{ $$ = $1; }
		|	NAME					{ $$ = $1->value; }	 /* 5 */	 
		;

%%

	/* needed for MacOSX */
void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}

int main(void) {
    yyparse();
	return 0; 
}


/* 6 */
/* look up a symbol table entry, add if not present */ 
struct symtab * symlook(s)
char *s;
{
	char *p; 
	struct symtab *sp;

	for(sp = symtab; sp < &symtab[NSYMS]; sp++) { 
		/* is it already here? */
		if(sp->name && ! strcmp(sp->name, s))
			return sp;

		/* is it free */ 
		if(!sp->name) {
			sp->name = strdup(s); 
			return sp;
		}
		/* otherwise continue to next */
	}
	yyerror("Too many symbols");
	exit(1);   /* cannot continue */ 
	
} /* symlook */


```

> calc.l

```
%{
#include "ch3hdr.h"  /* 1 */
#include "y.tab.h"
#include "math.h"
	/*extern int yylval ;*/
	/*extern double vbltable[26];*/		/* 2 */
%}

%%

([0-9]+|([0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?)  	{ yylval.dval = atof(yytext); return NUMBER; }

[ \t]	;    /* ignore whitespace */

[A-Za-z][A-Za-z0-9]*	{yylval.symp = symlook(yytext) ;  /* 3 */
						 return NAME; }	

"$" 	{return 0;  /* logical EOF  end of input */}

\n		|
. 		return yytext[0] ;  /*very common catch-all */

%%

	/* needed for MacOSX */
int yywrap(void) {
	return 1 ;
}
```

<h2 id="8c439d47137d2b02b587a9cb733a993a"></h2>
### Functions and Reserved Words

Now we will adds mathematical functions for square root, exponential, and logarithm.

The brute force approach makes the function names separate tokens, and adds separate rules for each function:

```
%token SQRT LOG EXP
...
expression: ...
	| 	SQRT '(' expression ')' { $$ = sqrt($3); }
	| 	LOG '(' expression ')' { $$ = log($3); }
	| 	EXP '(' expression ')' { $$ = exp($3); }
```

In the scanner, we have to return a **SQRT** token for “sqrt” input and so forth:

```
sqrt 	return SQRT ;
log 	return LOG ;
exp 	return EXP ;

[A-Za-z][A-Za-z0-9]* 	...
```

The specific patterns come first so they match before than the general symbol pattern.

This works, but it has problems. 

 - One is that you must hard-code every function into the parserand the lexer, which is tedious and makes it hard to add more functions.
 - Another is that function names are reserved words,
	- i.e., you cannot use **sqrt** as a variable name. This may or may not be a problem, depending on your intentions.


<h2 id="3ffc9c6bc2ffcb3c6cd4ac1be2b51ae4"></h2>
### Reserved Words in the Symbol Table

 - take the specific patterns for function names out of the lexer and put them in the symbol table
 - add a new field to each symbol table entry: **funcptr**, a pointer to the C function to call if this entry is a function name.
 ```
 struct symtab {
	char *name;
	double (*funcptr) (); 	/* 1 */
	double value;
 } symtab[NSYMS];
 ```
 - calls the new routine **addfunc()** in **main()** to add each of the function names to the symbol table, then calls yyparse().







