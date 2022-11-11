[](...menustart)

- [FAdo Tutorial](#844c992587ad53d6fa24ff03c8921787)

[](...menuend)


<h2 id="844c992587ad53d6fa24ff03c8921787"></h2>

# FAdo Tutorial

```python
>>> import FAdo.fa as fa
>>> import FAdo.reex as reex
>>> import FAdo.fio as fio
>>>
>>> # case 3.14
>>> r = reex.str2regexp("(a+b)*abb")
>>> print r
(((a + b)* a) b) b
>>> nfa = r.nfaPD()
>>> nfa.dump()
(['NFA'], [concat(concat(concat(star(disj(atom(a),atom(b))),atom(a)),atom(b)),atom(b)), concat(atom(b),atom(b)), atom(b), epsilon()], ['a', 'b'], [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 1, 2), (2, 1, 3)], [0], [3])
>>> nfa.succintTransitions()
[('(((a + b)* a) b) b', 'a', 'b b'), ('b b', 'b', 'b'), ('(((a + b)* a) b) b', 'a, b', '(((a + b)* a) b) b'), ('b', 'b', '@epsilon')]

>>> m=nfa
>>> m.renameStates(xrange(len(m)))
NFA((['0', '1', '2', '3'], ['a', 'b'], ['0'], ['3'], "[(0, 'a', 0), (0, 'a', 1), (0, 'b', 0), (1, 'b', 2), (2, 'b', 3)]"))
>>> nfa.dump()
(['NFA'], [0, 1, 2, 3], ['a', 'b'], [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 1, 2), (2, 1, 3)], [0], [3])

>>> nfa.States
[0, 1, 2, 3]
>>> nfa.Sigma
set(['a', 'b'])
>>> nfa.Initial
set([0])
>>> nfa.Final
set([3])
>>> # case 3.15
>>> nfa.succintTransitions()
[('0', 'a', '1'), ('1', 'b', '2'), ('0', 'a, b', '0'), ('2', 'b', '3')]
```

