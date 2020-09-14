...menustart

- [Building](#c39b56d4489fb2507289e7ae19567b80)
- [Lex](#976472a144efa6a4b849b24ac6b18867)
- [Yacc](#f4892ae9e5ea764a416fcc3b54a5bad9)
- [Practice, Part II](#1864a6324588032cee5adb1f75e62195)
- [Calculator](#cc84fa821011b93c1f935268e5560c2e)
- [More Lex](#786b674166922221e6eab655991c9fe3)
    - [Strings](#89be9433646f5939040a78971a5d103a)
    - [Reserved Words](#f6904aa41f71b6298d0a92fa1d4079e2)
    - [Debugging Lex](#acb2b044e25d475996404b6350ab88f5)
- [More Yacc](#8e775af853936e583371f2687a64ecd9)
    - [Recursion](#12fa464a36f8e5a187f5acfde99b7029)
    - [If-Else Ambiguity](#68c908bd98cb22a4b0150d6b09c01063)

...menuend


<h2 id="c39b56d4489fb2507289e7ae19567b80"></h2>


# Building 

```
yacc –d bas.y     # create y.tab.h, y.tab.c
lex bas.l         # create lex.yy.c
cc lex.yy.c y.tab.c –obas.exe  # compile/link
```

<h2 id="976472a144efa6a4b849b24ac6b18867"></h2>


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

^(.*)\n     { printf("%4d\t%s", yylineno, yytext); ++yylineno; }

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


<h2 id="f4892ae9e5ea764a416fcc3b54a5bad9"></h2>


# Yacc

 - To parse an expression
 - Instead of starting with a single nonterminal (start symbol) and generating an expression from a grammar
 - we need to reduce an expression to a single nonterminal.

This is known as bottom-up or shift-reduce parsing and uses a stack for storing terms.  



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

[0-9]+    {
            yylval = atoi(yytext);
            return INTEGER;
        }        
[-+\n]    return *yytext;
[ \t]    ; /* skip whitespace */
.        yyerror("invalid character");

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
        program expr '\n'    { printf("%d\n", $2); }
        |
        ;
expr:    
        INTEGER                { $$ = $1; }
        | expr '+' expr        { $$ = $1 + $3; }
        | expr '-' expr        { $$ = $1 - $3; }
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

<h2 id="1864a6324588032cee5adb1f75e62195"></h2>


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
        expr                    { printf("%d\n", $1); }
        | VARIABLE '=' expr        { sym[$1] = $3; }
        ;
expr:
        INTEGER
        | VARIABLE        { $$ = sym[$1]; }
        | expr '+' expr    {$$=$1+$3;}
        | expr '-' expr    {$$=$1-$3;}
        | expr '*' expr    {$$=$1*$3;}
        | expr '/' expr {$$=$1/$3;}        
        | '(' expr ')'    {$$=$2;} 
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


<h2 id="cc84fa821011b93c1f935268e5560c2e"></h2>


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

Constants, variables, and nodes can be represented by **yylval** in the parser’s value stack. A more accurate representation of decimal integers is given below. This is similar to C/C++ where integers that begin with 0 are classified as octal.

```
0               {
                   yylval.iValue = atoi(yytext);
                   return INTEGER;
                }
[1-9][0-9]*     {
                   yylval.iValue = atoi(yytext);
                   return INTEGER;
                }
```

Notice the type definitions

```
%token <iValue> INTEGER
%type <nPtr> expr
```

This binds **expr** to **nPtr**, and **INTEGER** to **iValue** in the **YYSTYPE** union. This is required so that yacc can generate the correct code. For example, the rule

```
expr: INTEGER { $$ = con($1); }
```

should generate the following code. Note that **yyvsp[0]** addresses the top of the value stack, or the value associated with **INTEGER**.

```
yylval.nPtr = con(yyvsp[0].iValue);
```

The unary minus operator is given higher priority than binary operators as follows:

```
%left GE LE EQ NE '>' '<'
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
```

The **%nonassoc** indicates no associativity is implied. It is frequently used in conjunction with %prec to specify precedence of a rule. Thus, we have

```
expr: '-' expr %prec UMINUS     { $$ = node(UMINUS, 1, $2); }
```

indicating that the precedence of the rule is the same as the precedence of token **UMINUS**. And **UMINUS** (as defined above) has higher precedence than the other operators. A similar technique is used to remove ambiguity associated with the if-else statement (see If-Else Ambiguity).

After the tree is built function **ex** is called to do a depth-first walk of the syntax tree. Three versions of **ex** are included: an interpretive version, a compiler version, and a version that generates a syntax tree.

**Include File: calc3.h**

```c
typedef enum { typeCon, typeId, typeOpr } nodeEnum;
/* constants */
typedef struct {
    int value;      /* value of constant */
} conNodeType;

/* identifiers */
typedef struct {
    int i;          /* subscript to sym array */
} idNodeType;

/* operators */
typedef struct {
    int oper;       /* operator */
    int nops;       /* number of operands */
    struct nodeTypeTag *op[1];  /* operands, extended at runtime */
} oprNodeType;

typedef struct nodeTypeTag {
    nodeEnum type;          /* type of node */
    union {
        conNodeType con;    /* constants */
        idNodeType id;      /* identifiers */
        oprNodeType opr;    /* operators */
    };
} nodeType;
extern int sym[26];                        
```



**Lex Input**

```
%{
#include <stdlib.h>
#include "calc3.h"
#include "y.tab.h"
void yyerror(char *);
%}

%%

[a-z]       {
                yylval.sIndex = *yytext - 'a';
                return VARIABLE;
            }
0           {
                yylval.iValue = atoi(yytext);
                return INTEGER;
            }
[1-9][0-9]* {
                yylval.iValue = atoi(yytext);
                return INTEGER;
            }
[-()<>=+*/;{}.] {
                        return *yytext;
                }
">="        return GE;
"<="        return LE;
"=="        return EQ;
"!="        return NE;
"while"     return WHILE;
"if"        return IF;
"else"      return ELSE;
"print"     return PRINT;

[ \t\n]+    ;       /* ignore whitespace */

.           yyerror("Unknown character");

%%

int yywrap(void) {
    return 1;
}                                          
```


**Yacc Input**

```
%{
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "calc3.h"

/* prototypes */
nodeType *opr(int oper, int nops, ...);
nodeType *id(int i);
nodeType *con(int value);
void freeNode(nodeType *p);
int ex(nodeType *p);
int yylex(void);

void yyerror(char *s);
int sym[26];            /* symbol table */
%}

%union {
    int iValue;            /* integer value */
    char sIndex;        /* symbol table index */
    nodeType *nPtr;        /* node pointer */
};

%token <iValue> INTEGER
%token <sIndex> VARIABLE
%token WHILE IF PRINT
%nonassoc IFX
%nonassoc ELSE

%left GE LE EQ NE '>' '<'
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS

%type <nPtr> stmt expr stmt_list

%%

program:
      function    { exit(0); }
    ;
function:
    function stmt        { ex($2); freeNode($2); }
    |                  /* NULL */ 
    ;
stmt: 
    ';'            {$$= opr(';', 2, NULL, NULL); } 
    | expr ';'        {$$= $1; }
    | PRINT expr ';'        {$$= opr(PRINT, 1, $2); }
    | VARIABLE '=' expr ';'        {$$= opr('=', 2, id($1), $3); }
    | WHILE '(' expr ')' stmt { $$ = opr(WHILE, 2, $3, $5); }
    | IF '(' expr ')' stmt %prec IFX     { $$ = opr(IF, 2, $3, $5); } 
    | IF '(' expr ')' stmt ELSE stmt    { $$ = opr(IF, 3, $3, $5, $7); } 
    | '{' stmt_list '}'                    { $$= $2; }
    ;

stmt_list:
    stmt                { $$=$1;}
  | stmt_list stmt        { $$ = opr(';', 2, $1, $2); }
  ;

expr:
    INTEGER            { $$ = con($1); }
    | VARIABLE        { $$ = id($1); }
    | '-' expr %prec UMINUS { $$ = opr(UMINUS, 1, $2); }
    | expr '+' expr            { $$ = opr('+', 2, $1, $3); }
    | expr '-' expr            { $$ = opr('-', 2, $1, $3); }
    | expr '*' expr            { $$ = opr('*', 2, $1, $3); }
    | expr '/' expr            { $$ = opr('/', 2, $1, $3); }
    | expr '<' expr            { $$ = opr('<', 2, $1, $3); }
    | expr '>' expr            { $$ = opr('>', 2, $1, $3); }
    | expr GE expr            { $$ = opr(GE, 2, $1, $3); }
    | expr LE expr            { $$ = opr(LE, 2, $1, $3); }
    | expr NE expr            { $$ = opr(NE, 2, $1, $3); }
    | expr EQ expr            { $$ = opr(EQ, 2, $1, $3); }
    | '(' expr ')'            { $$=$2;}
    ;

%%

#define SIZEOF_NODETYPE ((char *)&p->con - (char *)p)

nodeType *con(int value) {
    nodeType *p;
    
    /* allocate node */
    if ((p = malloc(sizeof(nodeType))) == NULL)
        yyerror("out of memory");
    
    /* copy information */
    p->type = typeCon;
    p->con.value = value;

    return p; 
}

nodeType *id(int i) {
    nodeType *p;

    /* allocate node */
    if ((p = malloc(sizeof(nodeType))) == NULL)
        yyerror("out of memory");

    /* copy information */
    p->type = typeId;
    p->id.i = i;
    return p; 
}

          
nodeType *opr(int oper, int nops, ...) {
    va_list ap;
    nodeType *p;
    int i;
    
    /* allocate node, extending op array */
    if ((p = malloc(sizeof(nodeType) +
            (nops-1) * sizeof(nodeType *))) == NULL)
        yyerror("out of memory");
    
    /* copy information */
    p->type = typeOpr;
    p->opr.oper = oper;
    p->opr.nops = nops;
    va_start(ap, nops);
    for (i = 0; i < nops; i++)
        p->opr.op[i] = va_arg(ap, nodeType*);
    va_end(ap);
    return p; 
}

void freeNode(nodeType *p) {
    int i;
    if (!p) return;
    if (p->type == typeOpr) {
        for (i = 0; i < p->opr.nops; i++)
            freeNode(p->opr.op[i]);
    }
    free (p); 
}

void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}

int main(void) {
    yyparse();
    return 0; 
}
```

**Interpreter**

```c
#include <stdio.h>
#include "calc3.h"
#include "y.tab.h"

int ex(nodeType *p) {
    if (!p) return 0;
    switch(p->type) {
    case typeCon:   return p->con.value;
    case typeId:    return sym[p->id.i];
    case typeOpr:
    switch(p->opr.oper) {
      case WHILE:   while(ex(p->opr.op[0]))
                        ex(p->opr.op[1]);
                    return 0;
      case IF:      if (ex(p->opr.op[0]))
                            ex(p->opr.op[1]);
                        else if (p->opr.nops > 2)
                            ex(p->opr.op[2]);
                    return 0;
      case PRINT:   printf("%d\n", ex(p->opr.op[0]));
                    return 0;
      case ';':     ex(p->opr.op[0]); return ex(p->opr.op[1]);
      case '=':     return sym[p->opr.op[0]->id.i] = ex(p->opr.op[1]);
      case UMINUS:  return -ex(p->opr.op[0]);
      case '+':     return ex(p->opr.op[0]) + ex(p->opr.op[1]);
      case '-':     return ex(p->opr.op[0]) - ex(p->opr.op[1]);
      case '*':     return ex(p->opr.op[0]) * ex(p->opr.op[1]);
      case '/':     return ex(p->opr.op[0]) / ex(p->opr.op[1]);
      case '<':     return ex(p->opr.op[0]) < ex(p->opr.op[1]);
      case '>':     return ex(p->opr.op[0]) > ex(p->opr.op[1]);
      case GE:      return ex(p->opr.op[0]) >= ex(p->opr.op[1]);
      case LE:      return ex(p->opr.op[0]) <= ex(p->opr.op[1]);
      case NE:      return ex(p->opr.op[0]) != ex(p->opr.op[1]);
      case EQ:      return ex(p->opr.op[0]) == ex(p->opr.op[1]);
    }
    }
    return 0;
}                                                                          
```


**Compiler**

```
#include <stdio.h>
#include "calc3.h"
#include "y.tab.h"

static int lbl;

int ex(nodeType *p) {
    int lbl1, lbl2;

    if (!p) return 0;
    switch(p->type) {
    case typeCon:
        printf("\tpush\t%d\n", p->con.value);
        break;
    case typeId:
        printf("\tpush\t%c\n", p->id.i + 'a');
        break;
    case typeOpr:
        switch(p->opr.oper) {
        case WHILE:
            printf("L%03d:\n", lbl1 = lbl++);
            ex(p->opr.op[0]);
            printf("\tjz\tL%03d\n", lbl2 = lbl++);
            ex(p->opr.op[1]);
            printf("\tjmp\tL%03d\n", lbl1);
            printf("L%03d:\n", lbl2);
            break;
        case IF:
            ex(p->opr.op[0]);
            if (p->opr.nops > 2) {
                /* if else */
                printf("\tjz\tL%03d\n", lbl1 = lbl++);
                ex(p->opr.op[1]);
                printf("\tjmp\tL%03d\n", lbl2 = lbl++);
                printf("L%03d:\n", lbl1);
                ex(p->opr.op[2]);
                printf("L%03d:\n", lbl2);
            } else {
                /* if */
                printf("\tjz\tL%03d\n", lbl1 = lbl++);
                ex(p->opr.op[1]);
                printf("L%03d:\n", lbl1);
            }
             break;
        case PRINT:
            ex(p->opr.op[0]);
            printf("\tprint\n");
            break;

        case '=':
            ex(p->opr.op[1]);
            printf("\tpop\t%c\n", p->opr.op[0]->id.i + 'a');
            break;
        case UMINUS:
            ex(p->opr.op[0]);
            printf("\tneg\n");
            break;
        default:
            ex(p->opr.op[0]);
            ex(p->opr.op[1]);
            switch(p->opr.oper) {
                    case '+':   printf("\tadd\n"); break;
                    case '-':   printf("\tsub\n"); break;
                    case '*':   printf("\tmul\n"); break;
                    case '/':   printf("\tdiv\n"); break;
                    case '<':   printf("\tcompLT\n"); break;
                    case '>':   printf("\tcompGT\n"); break;
                    case GE:    printf("\tcompGE\n"); break;
                    case LE:    printf("\tcompLE\n"); break;
                    case NE:    printf("\tcompNE\n"); break;
                    case EQ:    printf("\tcompEQ\n"); break;
            }
        }
    }
    return 0;
}
```

**Graph**

```

/* source code courtesy of Frank Thomas Braun */
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include "calc3.h"
#include "y.tab.h"

int del = 1; /* distance of graph columns */
int eps = 3; /* distance of graph lines */

/* interface for drawing (can be replaced by "real" graphic using GD or other) */
void graphInit (void);
void graphFinish();
void graphBox (char *s, int *w, int *h);
void graphDrawBox (char *s, int c, int l);
void graphDrawArrow (int c1, int l1, int c2, int l2);

/* recursive drawing of the syntax tree */
void exNode (nodeType *p, int c, int l, int *ce, int *cm);

/***********************************************************/
/* main entry point of the manipulation of the syntax tree */ 
int ex (nodeType *p) {
    int rte, rtm;
    graphInit ();
    exNode (p, 0, 0, &rte, &rtm);
    graphFinish();
    return 0;
}
/*c----cm---ce---->            drawing of leaf-nodes
 l leaf-info
 */

/*c---------------cm--------------ce----> drawing of non-leaf-nodes 
l                 node-info
*                    |
*         ------------- ...----
*        |        |            | 
*        v        v            v
*     child1     child2 ...     child-n
*     che     che           che 
*    cs         cs         cs         cs 
*
*/

void exNode(  
         nodeType *p,
        int c, int l,        /* start column and line of node */
        int *ce, int *cm          /* resulting end column and mid of node */
) 
{
    int w, h;      /* node width and height */
    char *s;         /* node text */
    int cbar;    /* "real" start column of node (centred above subnodes)*/
    int k;     /* child number */
    int che, chm;     /* end column and mid of children */
    int cs;     /* start column of children */
    char word[20];     /* extended node text */
    if (!p) return;

 
    strcpy (word, "???"); /* should never appear */
    s = word;
    switch(p->type) {
        case typeCon: sprintf (word, "c(%d)", p->con.value); break; 
        case typeId: sprintf (word, "id(%c)", p->id.i + 'A'); break; 
        case typeOpr:
        switch(p->opr.oper){
            case WHILE:        s = "while"; break;
            case IF:        s = "if";    break;
            case PRINT:        s = "print"; break;
            case ';':        s = "[;]";  break;
            case '=':        s = "[=]";  break;
            case UMINUS:    s = "[_]";  break;
            case '+':        s = "[+]";  break;
            case '-':        s = "[-]";  break;
            case '*':        s = "[*]";  break;
            case '/':        s = "[/]";  break;
            case '<':        s = "[<]";    break;
            case '>':        s = "[>]";  break;    
            case GE:        s = "[>=]"; break;
            case LE:        s = "[<=]"; break;
            case NE:        s = "[!=]"; break;
            case EQ:        s = "[==]"; break;
        }
        break;
    }
    /* construct node text box */
    graphBox (s, &w, &h);
    cbar = c;
    *ce = c + w;
    *cm = c + w / 2;

    /* node is leaf */
    if (p->type == typeCon || p->type == typeId || p->opr.nops == 0) {
        graphDrawBox (s, cbar, l);
        return; 
    }

    /* node has children */
    cs = c;
    for (k = 0; k < p->opr.nops; k++) {
        exNode (p->opr.op[k], cs, l+h+eps, &che, &chm);
        cs = che; 
    }
    /* total node width */
    if (w < che - c) {
        cbar += (che - c - w) / 2;
        *ce = che;
        *cm = (c + che) / 2;
    }    
    
    /* draw node */
    graphDrawBox (s, cbar, l);

    /* draw arrows (not optimal: children are drawn a second time) */ 
    cs = c;
    for (k = 0; k < p->opr.nops; k++) {
        exNode (p->opr.op[k], cs, l+h+eps, &che, &chm); 
        graphDrawArrow (*cm, l+h, chm, l+h+eps-1);
        cs = che;
    } 
}

/* interface for drawing */

#define lmax 200
#define cmax 200

char graph[lmax][cmax]; /* array for ASCII-Graphic */ 
int graphNumber = 0;

void graphTest (int l, int c)
{   
    int ok;
    ok = 1;
    if (l < 0) ok = 0;
    if (l >= lmax) ok = 0;
    if (c < 0) ok = 0;
    if (c >= cmax) ok = 0;
    if (ok) return;
    printf ("\n+++error: l=%d, c=%d not in drawing rectangle 0, 0 ... %d, %d" ,l, c, lmax, cmax); 
    exit (1); 
}

void graphInit (void) {
    int i, j;
    for (i = 0; i < lmax; i++) {
        for (j = 0; j < cmax; j++) {
            graph[i][j] = ' ';
        }
    } 
}

void graphFinish() {
    int i, j;
    for (i = 0; i < lmax; i++) {
        for (j = cmax-1; j > 0 && graph[i][j] == ' '; j--);
        graph[i][cmax-1] = 0;
        if (j < cmax-1) graph[i][j+1] = 0;
        if (graph[i][j] == ' ') graph[i][j] = 0;
    }
    for (i = lmax-1; i > 0 && graph[i][0] == 0; i--); 
    printf ("\n\nGraph %d:\n", graphNumber++);
    for (j = 0; j <= i; j++) printf ("\n%s", graph[j]); 
    printf("\n");
}

void graphBox (char *s, int *w, int *h) {
    *w = strlen (s) + del;
    *h = 1;
}

void graphDrawBox (char *s, int c, int l) {
    int i;
    graphTest (l, c+strlen(s)-1+del);
    for (i = 0; i < strlen (s); i++) {
        graph[l][c+i+del] = s[i];
    }
}



void graphDrawArrow (int c1, int l1, int c2, int l2) {
    int m;
    graphTest (l1, c1);
    graphTest (l2, c2);
    m = (l1 + l2) / 2;
    while (l1 != m) {
        graph[l1][c1] = '|'; if (l1 < l2) l1++; else l1--;
    }
    while (c1 != c2) {
        graph[l1][c1] = '-'; if (c1 < c2) c1++; else c1--;
    }
    while (l1 != l2) {
        graph[l1][c1] =    '|'; if (l1 < l2) l1++; else l1--;
    }
    graph[l1][c1] = '|';
}
```


<h2 id="786b674166922221e6eab655991c9fe3"></h2>


# More Lex 

<h2 id="89be9433646f5939040a78971a5d103a"></h2>


## Strings

Here is one way to match a string in lex:

```
%{
    char *yylval;
    #include <string.h>
%}

%%

\"[^"\n]*["\n] {
           yylval = strdup(yytext+1);  // value 不包括引号
           if (yylval[yyleng-2] != '"')
               warning("improperly terminated string");
           else
               yylval[yyleng-2] = 0;
           printf("found '%s'\n", yylval);
        }
```

If we wish to add escape sequences, such as \n or \", start states simplify matters:
    
```
%{
char buf[100];
char *s;
%}
%x STRING

%%

\"                { BEGIN STRING; s = buf; }
<STRING>\\n     { *s++ = '\n'; }
<STRING>\\t     { *s++ = '\t'; }
<STRING>\\\"     { *s++ = '\"'; }
<STRING>\"         {
                    *s = 0;
                    BEGIN 0;
                    printf("found '%s'\n", buf);
                }
<STRING>\n         { printf("invalid string"); exit(1); }
<STRING>.         { *s++ = *yytext; }
```

Exclusive start state **STRING** is defined in the definition section. When the scanner detects a quote the **BEGIN** macro shifts lex into the **STRING** state. Lex stays in the **STRING** state and recognizes only patterns that begin with **\<STRING\>** until another **BEGIN** is executed. Thus we have a mini-environment for scanning strings. When the trailing quote is recognized we switch back to initial state 0.

<h2 id="f6904aa41f71b6298d0a92fa1d4079e2"></h2>


## Reserved Words

If your program has a large collection of reserved words it is more efficient to let lex simply match a string and determine in your own code whether it is a variable or reserved word. 

For example, instead of coding

```
"if"            return IF;
"then"          return THEN;
"else"          return ELSE;
{letter}({letter}|{digit})*  {
                                yylval.id = symLookup(yytext);
                                return IDENTIFIER;
                            }
```

where **symLookup** returns an index into the symbol table, it is better to detect reserved words and identifiers simultaneously, as follows:

```
{letter}({letter}|{digit})*  {
            int i;
            if ((i = resWord(yytext)) != 0)
                return (i);
            yylval.id = symLookup(yytext);
            return (IDENTIFIER);
        }
```

This technique significantly reduces the number of states required, and results in smaller scanner tables.

<h2 id="acb2b044e25d475996404b6350ab88f5"></h2>


## Debugging Lex

The code generated by lex in file **lex.yy.c** includes debugging statements that are enabled by specifying command-line option “-d”. Debug output in flex (a GNU version of lex) may be toggled on and off by setting **yy_flex_debug**. Output includes the rule applied and corresponding matched text. If you’re running lex and yacc together then specify the following in your yacc input file:

```
extern int yy_flex_debug;
int main(void) {
    yy_flex_debug = 1;
    yyparse(); 
}
```

Alternatively, you may write your own debug code by defining functions that display information for the token value and each variant of the yylval union. This is illustrated in the following example. 

When **DEBUG** is defined the debug functions take effect and a trace of tokens and associated values is displayed.

```
%union {
       int ivalue;
       ... 
       };

%{
#ifdef DEBUG
    int dbgToken(int tok, char *s) {
        printf("token %s\n", s);
        return tok; 
    }
    int dbgTokenIvalue(int tok, char *s) {
        printf("token %s (%d)\n", s, yylval.ivalue);
        return tok; 
    }
    #define RETURN(x) return dbgToken(x, #x)
    #define RETURN_ivalue(x) return dbgTokenIvalue(x, #x) 
#else
    #define RETURN(x) return(x)
    #define RETURN_ivalue(x) return(x)
#endif
%}

%%

[0-9]+ {
                   yylval.ivalue = atoi(yytext);
                   RETURN_ivalue(INTEGER);
               }
"if"        RETURN(IF);
"else"      RETURN(ELSE);

```

<h2 id="8e775af853936e583371f2687a64ecd9"></h2>


# More Yacc

<h2 id="12fa464a36f8e5a187f5acfde99b7029"></h2>


## Recursion

A list may be specified with left recursion

```
list:
        item
         | list ',' item
         ;
```

or right recursion.

```
list:
        item
         | item ',' list

```

If right recursion is used then all items on the list are pushed on the stack. After the last item is pushed we start reducing. 

With left recursion we never have more than three terms on the stack since we reduce as we go along. For this reason it is advantageous to use left recursion.

<h2 id="68c908bd98cb22a4b0150d6b09c01063"></h2>


## If-Else Ambiguity

A shift-reduce conflict that frequently occurs involves the if-else construct. Assume we have the following rules:

```
stmt:
      IF expr stmt
      | IF expr stmt ELSE stmt
      ...
```

and the following state:

```
IF expr stmt IF expr stmt . ELSE stmt
```

We need to decide if we should shift the ELSE or reduce the IF expr stmt at the top of the stack. If we shift then we have

