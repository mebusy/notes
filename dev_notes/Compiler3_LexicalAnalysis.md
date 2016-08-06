
# Lexical Analysis

 - We begin the study of lexical-analyzer generators by introducing regular expressions. 
 - We show how this notation can be transformed, 
 	- first into nondeterministic automata and then into deterministic automata. 
 - The latter two notations can be used as input to a "driver", 
 	- that is, code which simulates these automata and uses them as a guide to determining the next token.
 - This driver and the specification of the automaton form the nucleus of the lexical analyzer.

---

## 3.1 The Role of the Lexical Analyzer

