
# GREP 

Global Regular Expression Print

- Most Common Usage
    ```bash
    grep -rinI "Pattern" path
    ```



## Search Files Contain Specify Text

- most simple case: Print all lines which contains specific pattern in a file
    ```bash
    $ grep "const TState" astar.hpp
     IProblem(const TState &startState, const TState &goalState) : startState_(startState), goalState_(goalState) {}
     const TState &getStartState() const { return startState_; }
     const TState &getGoalState() const { return goalState_; }
    ```


### Searched for as a word :  -w, --word-regexp

```bash
$ grep GoalState astar.hpp
 const TState &getGoalState() const { return goalState_; }
 virtual bool isGoalState(const TState &state) const = 0;
        if (problem.isGoalState(state)) {
            
$ grep -w GoalState astar.hpp
# nothing
```


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

### Print Line Number : -n, --line-number

Each output line is preceded by its relative line number in the file, starting at line 1.

```bash
$ grep -n "const TState &get" astar.hpp
20:    const TState &getStartState() const { return startState_; }
21:    const TState &getGoalState() const { return goalState_; }
```

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

### Recursive Serach (Most Common Usage)

```bash
grep -rin  "const TState &get" ..
../cpp_alg/astar.hpp:20:    const TState &getStartState() const { return startState_; }
../cpp_alg/astar.hpp:21:    const TState &getGoalState() const { return goalState_; }
```


### Ignore Binary Files : -I

```bash
grep -rinI  "const TState &get" ..
```


### Print File Name Only : -l, --files-with-matches

```bash
grep -ril  "const TState &get" .. 
../cpp_alg/astar.hpp
```


### Multiple Pattern : -e pattern, --regexp=pattern

This option is most useful when multiple `-e` options are used to specify multiple patterns, or when a pattern begins with a dash (‘-’).


```bash
$ grep -rinI -e "getCount" -e "getPriority" .
./priorityqueue.hpp:33:    size_t getCount() const { return count_; }
./priorityqueue.hpp:34:    double getPriority() const { return priority_; }
```


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

Grep is not using perl compatible regular expression.  If you wanna use perl compatible RE, you can use GNU grep and `-P` option.

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
    grep --exclude-dir={dir1,dir2,*.dst}  -rnw "pattern"  path
    ```


## Pipe output of Other Commands Into GREP

```bash
$ history | grep "git commit"
   10  git commit -a -mm
   75  git commit -a -mm
   89  git commit -a -m"python tips: remove comments in source file"
    ...
```


