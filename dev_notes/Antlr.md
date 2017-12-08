
# Antlr

# install

http://www.antlr.org/

```
OS X
$ cd /usr/local/lib
$ sudo curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.7-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```

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


