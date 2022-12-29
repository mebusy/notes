
# mvn

compile

```bash
mvn compile
```

pacakge 

```bash
mvn package
```

## Proxy

~/.m2/settings.xml

```xml
<settings>
  <proxies>
    <proxy>
      <id>genproxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>proxyHost</host>
      <port>3128</port>
      <username>username</username>
      <password>password</password>
    </proxy>
 </proxies>
</settings>
```


## download all dependency jars to local directory

```bash
mvn dependency:copy-dependencies -DoutputDirectory="`pwd`/jars"
```



# codingame

## set environment
0. JDK 1.8
1. build core engine
    - https://github.com/CodinGame/codingame-game-engine.git
    - `mvn compile && mvn build`
    - copy 3 jars from  ./runner/target
2. build event
    - `mvn compile && mvn build`
    - copy 1 jar from /target
3. extra dependency jars from event repo
    ```bash
    mvn dependency:copy-dependencies -DoutputDirectory="`pwd`/jars"
    ```

