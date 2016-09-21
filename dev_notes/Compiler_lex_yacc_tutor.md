
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










