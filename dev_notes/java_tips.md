# Java Tips

## check directly string compare in source code 

```bash
$ mvn spotbugs:check | grep ES_COMPARING_STRINGS_WITH_EQ 
```

see `working_settings/myProfileLSP`


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


