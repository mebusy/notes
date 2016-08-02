
# Compiler Note

analysis / synthesis

lexical analysis ，or scanning 
    - tokens and symbol table

Syntax analysis ,  or parsing
    - syntax describes the proper form of its programs
    - use context-free grammars to specify the syntax of a language
        - CFG itself is specified by listing their productions.
    - Parser的任务是 find a parse tree for a given string of terminals

    - syntax tree : derivation过程
        - root  -- start symbol
        - interior node -- nonterminal
            - correspond to a production with its children
        - leaf  --  terminal or eps

Semantic analysis
    - semantic define what its programs mean
    - gather type info
    - type checking
    - coercions

Intermediate code generation
    - AST -> three-address code



--- analysis end ---

Code optimize

Code generation

---------


syntax-directed translator SDT

将输入的字符串翻译成一些列具有语义的动作，这是通过向 grammar 产生式 附加规则 或 程序片段来实现的。SDT 有两个重要概念：syntax-directed definition 和 syntax-directed translator scheme


syntax-directed definition
    SDD是特殊的CFG。特殊之处在于它为每个 grammar symbol 附加了属性,并且为这些 grammar symbol 构成的产生式附加了语义规则semantic rule。

syntax-directed translator scheme
    SDTS 也是一种特殊的CFG。其特殊之处在于它在产生式中 嵌入了 被称为semantic action 的程序片段，
    SDTS 和 SDD 相似，SDD指定语义动作，SDTS实现了这些语义动作。

----------

Concrete syntax tree
    CST 其实就是 parse tree。内部节点表示非终结符，叶子节点都是终结符，这些终结符构成了 可以由产生式 推导出来的 输入串。
    CST只是概念上的语法术，大部分编译器都使用AST。

Abstract syntax tree
   AST 是一种数据结构，在表达式的AST中，每个内部节点表示一个操作符，内部节点的子节点代表操作数。





 
