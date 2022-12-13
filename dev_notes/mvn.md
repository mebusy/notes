
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


