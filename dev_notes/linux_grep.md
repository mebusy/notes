[](...menustart)

- [GREP](#2e3c6549274df5124474188e6ecdf946)
    - [Search Files Contain Specify Text](#f5288477170f1bbf987c63d9f6eb9646)
        - [Searched for as a word :  -w, --word-regexp](#18b17f53fd730635aa282a78bda26cd3)
        - [Ignore Case Sensitive : -i, --ignore-case](#c29e07949c8112e7467b6ae4b870f306)
        - [Print Line Number : -n, --line-number](#87faee44c10595068bc1f4f9430046e3)
        - [Print Extra Lines After/Before/Surround  each Match : -A/-B/-C](#90cd8844042f6ea867ca08d4feec727c)
        - [Find In Directory](#fc6c3ac3c6cdc3d7cc1f90ceb12ed74c)
        - [Recursive Serach (Most Common Usage)](#824f25bf4142c25228fdb263e1ab135c)
        - [Ignore Binary Files : -I](#ba2c03c5ca59895837aa4700676b804a)
        - [Print File Name Only : -l, --files-with-matches](#868f184aaaf9fc3641367296c19e659b)
        - [Multiple Pattern : -e pattern, --regexp=pattern](#ee97868fe3c5683b61bdae5870097767)
        - [Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`):  -E, --extended-regexp](#33f6321fe9d0b056d5438f5542973fa4)
        - [Include / Exclude](#c372ce68f746709e625ff6a439caabb9)
    - [Pipe output of Other Commands Into GREP](#658f8a592ea5feae877420d94058847b)

[](...menuend)


<h2 id="2e3c6549274df5124474188e6ecdf946"></h2>

# GREP 

Global Regular Expression Print

- Most Common Usage
    ```bash
    grep -rinI "Pattern" path
    ```



<h2 id="f5288477170f1bbf987c63d9f6eb9646"></h2>

## Search Files Contain Specify Text

- most simple case: Print all lines which contains specific pattern in a file
    ```bash
    $ grep "const TState" astar.hpp
     IProblem(const TState &startState, const TState &goalState) : startState_(startState), goalState_(goalState) {}
     const TState &getStartState() const { return startState_; }
     const TState &getGoalState() const { return goalState_; }
    ```


<h2 id="18b17f53fd730635aa282a78bda26cd3"></h2>

### Searched for as a word :  -w, --word-regexp

```bash
$ grep GoalState astar.hpp
 const TState &getGoalState() const { return goalState_; }
 virtual bool isGoalState(const TState &state) const = 0;
        if (problem.isGoalState(state)) {
            
$ grep -w GoalState astar.hpp
# nothing
```


<h2 id="c29e07949c8112e7467b6ae4b870f306"></h2>

### Ignore Case Sensitive : -i, --ignore-case

```bash
$ grep goalstate astar.hpp
# nothing

$ grep -i goalstate astar.hpp
 IProblem(const TState &startState, const TState &goalState) : startState_(startState), goalState_(goalState) {}
 const TState &getGoalState() const { return goalState_; }
 virtual bool isGoalState(const TState &state) const = 0;
 const TState &goalState_;
         if (problem.isGoalState(state)) {
```

<h2 id="87faee44c10595068bc1f4f9430046e3"></h2>

### Print Line Number : -n, --line-number

Each output line is preceded by its relative line number in the file, starting at line 1.

```bash
$ grep -n "const TState &get" astar.hpp
20:    const TState &getStartState() const { return startState_; }
21:    const TState &getGoalState() const { return goalState_; }
```

<h2 id="90cd8844042f6ea867ca08d4feec727c"></h2>

### Print Extra Lines After/Before/Surround  each Match : -A/-B/-C

- `-A num, --after-context=num`
    - Print num lines of trailing context after each match. 
- `-B num, --before-context=num`
    - Print num lines of leading context before each match.
- `-C[num], --context[=num]`
    - Print num lines of leading and trailing context surrounding each match.
    - The default value of num is “2” and is equivalent to “-A 2 -B 2”.


```bash
grep -n -A 3 "const TState &get" astar.hpp
20:    const TState &getStartState() const { return startState_; }
21:    const TState &getGoalState() const { return goalState_; }
22-
23-  public: // interface
24-    virtual bool isGoalState(const TState &state) const = 0;
```

```bash
$ grep -n -B 3 "const TState &get" astar.hpp
17-    IProblem(const TState &startState, const TState &goalState) : startState_(startState), goalState_(goalState) {}
18-
19-  public:
20:    const TState &getStartState() const { return startState_; }
21:    const TState &getGoalState() const { return goalState_; }
```

```bash
$ grep -n -C 2 "StartState" astar.hpp
18-
19-  public:
20:    const TState &getStartState() const { return startState_; }
21-    const TState &getGoalState() const { return goalState_; }
22-
--
66-
67-        // push start state to fringe
68:        auto startState = problem.getStartState();
69-
70-        // record cost before push to fringe
```

<h2 id="fc6c3ac3c6cdc3d7cc1f90ceb12ed74c"></h2>

### Find In Directory

```bash
$ grep -in  "const TState &get" ./*
grep: ./a.out.dSYM: Is a directory
./astar.hpp:20:    const TState &getStartState() const { return startState_; }
./astar.hpp:21:    const TState &getGoalState() const { return goalState_; }
grep: ./test: Is a directory
grep: ./tests: Is a directory
```

Not print directory info

```bash
grep -in  "const TState &get" ./*.*
grep: ./a.out.dSYM: Is a directory
./astar.hpp:20:    const TState &getStartState() const { return startState_; }
./astar.hpp:21:    const TState &getGoalState() const { return goalState_; }
```

<h2 id="824f25bf4142c25228fdb263e1ab135c"></h2>

### Recursive Serach (Most Common Usage)

```bash
grep -rin  "const TState &get" ..
../cpp_alg/astar.hpp:20:    const TState &getStartState() const { return startState_; }
../cpp_alg/astar.hpp:21:    const TState &getGoalState() const { return goalState_; }
```


<h2 id="ba2c03c5ca59895837aa4700676b804a"></h2>

### Ignore Binary Files : -I

```bash
grep -rinI  "const TState &get" ..
```


<h2 id="868f184aaaf9fc3641367296c19e659b"></h2>

### Print File Name Only : -l, --files-with-matches

```bash
grep -ril  "const TState &get" .. 
../cpp_alg/astar.hpp
```


<h2 id="ee97868fe3c5683b61bdae5870097767"></h2>

### Multiple Pattern : -e pattern, --regexp=pattern

This option is most useful when multiple `-e` options are used to specify multiple patterns, or when a pattern begins with a dash (‘-’).


```bash
$ grep -rinI -e "getCount" -e "getPriority" .
./priorityqueue.hpp:33:    size_t getCount() const { return count_; }
./priorityqueue.hpp:34:    double getPriority() const { return priority_; }
```


<h2 id="33f6321fe9d0b056d5438f5542973fa4"></h2>

### Use extended regular expressions (supports `?`, `+`, `{}`, `()` and `|`):  -E, --extended-regexp


Interpret pattern as an extended regular expression (i.e., force grep to behave as egrep).

**CAUTION 1:** `-E ` will normally be slow.


```bash
$ grep -rinI -E "get(Count|Priority)"  .
./priorityqueue.hpp:33:    size_t getCount() const { return count_; }
./priorityqueue.hpp:34:    double getPriority() const { return priority_; }
```

- along with `-o, --only-matching` , you can limit the length of matching context
    ```bash
    $ grep -rinI -E -o ".{0,6}get(Count|Priority).{0,12}"  .
    ./priorityqueue.hpp:33:ize_t getCount() const { r
    ./priorityqueue.hpp:34:ouble getPriority() const { r
    ```

Grep is not using POSIX regular expression.  If you wanna use perl compatible RE, you can use GNU grep and `-P` option.


### Limit Match Times :  -m num, --max-count=num

Stop reading the file after num matches.

```bash
grep -rinI -e "getCount" -e "getPriority" -m 1 .
./priorityqueue.hpp:33:    size_t getCount() const { return count_; }
```


<h2 id="c372ce68f746709e625ff6a439caabb9"></h2>

### Include / Exclude

- This will only search through those files which have .c or .h extensions:
    ```bash
    grep --include=\*.{c,h} -rnw "pattern"  path
    ```
- This will exclude searching all the files ending with .o extension:
    ```bash
    grep --exclude=\*.o  -rnw "pattern"  path
    ```
- It's possible to exclude one or more directories. For example, this will exclude the dirs `dir1/`, `dir2/` and all of them matching `*.dst/`:
    ```bash
    # single directory
    grep --exclude-dir=oneDirOnly -rnw "pattern"  path

    # multiple directory
    grep --exclude-dir={dir1,dir2,*.dst}  -rnw "pattern"  path
    ```


<h2 id="658f8a592ea5feae877420d94058847b"></h2>

## Pipe output of Other Commands Into GREP

```bash
$ history | grep "git commit"
   10  git commit -a -mm
   75  git commit -a -mm
   89  git commit -a -m"python tips: remove comments in source file"
    ...
```


