[](...menustart)

- [Java Tips](#388422a8915fd2bfbe9b79f826fd3033)
    - [check directly string compare in source code](#65d6c889cd403ce04b4de0470efa7ca4)
    - [check Non-referential public method](#6bfa2f56c97c8c9dcc581c46063576fd)

[](...menuend)


<h2 id="388422a8915fd2bfbe9b79f826fd3033"></h2>

# Java Tips

<h2 id="65d6c889cd403ce04b4de0470efa7ca4"></h2>

## check directly string compare in source code 

```bash
$ mvn spotbugs:check | grep ES_COMPARING_STRINGS_WITH_EQ 
```

see `working_settings/myProfileLSP`


<h2 id="6bfa2f56c97c8c9dcc581c46063576fd"></h2>

## check Non-referential public method 

```bash
#!/bin/sh

# This script checks which public methods in the Source Class are not referenced by any class in some directory.
SOURCE_CLASS="game.api.GameAPI"
CHECK_DIR="target/classes/demo/robot"

for m in $(javap -classpath target/classes ${SOURCE_CLASS} | grep -E 'public [a-zA-Z]+ ' | awk '{print $3}' | awk -F'\\(' '{print $1}' ); do
     count=`grep -R "$m" ${CHECK_DIR} | wc -l`
     if [ $count -eq 0 ]; then
         echo $m, $count
     fi
done;
```


