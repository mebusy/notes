[](...menustart)

- [mvn](#67c9500deb0863c5a8faa70b245d939d)
    - [Proxy](#f56ec2ab97d604832d90f6394e3f341f)
    - [download all dependency jars to local directory](#e042c2dceb644e0011dadcebdee7d5ca)
- [codingame](#2493f542e5fd965bb3eae545ed75a93f)
    - [set environment](#97e576d6033c8d1ede04911d1722cb4e)

[](...menuend)


<h2 id="67c9500deb0863c5a8faa70b245d939d"></h2>

# mvn

compile

```bash
mvn compile
```

pacakge 

```bash
mvn package
```

<h2 id="f56ec2ab97d604832d90f6394e3f341f"></h2>

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


<h2 id="e042c2dceb644e0011dadcebdee7d5ca"></h2>

## download all dependency jars to local directory

```bash
mvn dependency:copy-dependencies -DoutputDirectory="`pwd`/jars"
```



<h2 id="2493f542e5fd965bb3eae545ed75a93f"></h2>

# codingame

<h2 id="97e576d6033c8d1ede04911d1722cb4e"></h2>

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

