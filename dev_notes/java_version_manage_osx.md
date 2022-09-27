...menustart

- [Multiple Java Version on Mac OSX](#4fc9e2892b33aea308c94ae8c0aba2f3)
    - [Which java version you have ?](#4be002648b436bac96f90f38babf3f01)
    - [Install another JDK@11 via homebrew](#bc82ebd5b0ee12cf8a564e3995e76def)
    - [Get JAVA_HOME via `java_home`](#659d2e232157f2266f77cc65608b8953)
    - [Manage Your Jave Environment](#a979f66a93de96055f706d8826b62f51)
    - [if only you need java7...](#3e4389c4ca27e9e6951f00cbe9f48594)

...menuend


<h2 id="4fc9e2892b33aea308c94ae8c0aba2f3"></h2>


# Multiple Java Version on Mac OSX

Since MacOSX 10.5, Apple deliver `/usr/libexec/java_home` to manage JAVA_HOME

<h2 id="4be002648b436bac96f90f38babf3f01"></h2>


## Which java version you have ?

```bash
$ /usr/libexec/java_home  -V
Matching Java Virtual Machines (3):
    1.8.291.10 (x86_64) "Oracle Corporation" - "Java" /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home
    1.8.0_231 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
    1.7.0_292 (x86_64) "UNDEFINED" - "Zulu 7.44.0.11" /Library/Java/JavaVirtualMachines/zulu-7.jdk/Contents/Home
```

<h2 id="bc82ebd5b0ee12cf8a564e3995e76def"></h2>


## Install another JDK@11 via homebrew

```bash
$ brew install openjdk@11
# soft link to /Library/Java/JavaVirtualMachines
# so that `java_home` cmd can detect it
$ sudo ln -sfn /usr/local/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
```

now jdk11 are available

```bash
$ /usr/libexec/java_home  -V
Matching Java Virtual Machines (4):
    11.0.16.1 (x86_64) "Homebrew" - "OpenJDK 11.0.16.1" /usr/local/Cellar/openjdk@11/11.0.16.1/libexec/openjdk.jdk/Contents/Home
    1.8.291.10 (x86_64) "Oracle Corporation" - "Java" /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home
    1.8.0_231 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
    1.7.0_292 (x86_64) "UNDEFINED" - "Zulu 7.44.0.11" /Library/Java/JavaVirtualMachines/zulu-7.jdk/Contents/Home
```

<h2 id="659d2e232157f2266f77cc65608b8953"></h2>


## Get JAVA_HOME via `java_home`

```bash
$ /usr/libexec/java_home -v11   
/usr/local/Cellar/openjdk@11/11.0.16.1/libexec/openjdk.jdk/Contents/Home
$ /usr/libexec/java_home -v1.8.0
/Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
$ /usr/libexec/java_home -v1.7  
/Library/Java/JavaVirtualMachines/zulu-7.jdk/Contents/Home
```

<h2 id="a979f66a93de96055f706d8826b62f51"></h2>


## Manage Your Jave Environment


```bash
# ~/.profile
export JAVA_7_HOME=$(/usr/libexec/java_home -v1.7)
export JAVA_8_HOME=$(/usr/libexec/java_home -v1.8.0)
export JAVA_11_HOME=$(/usr/libexec/java_home -v11)

alias java7='export JAVA_HOME=$JAVA_7_HOME'
alias java8='export JAVA_HOME=$JAVA_8_HOME'
alias java11='export JAVA_HOME=$JAVA_11_HOME'

#default java11
export JAVA_HOME=$JAVA_11_HOME
```

switch java version

```bash
$ java8
$ java -version
openjdk version "1.8.0_312"
$ java11
$ java -version
openjdk version "11.0.12" 2021-07-20
```



<h2 id="3e4389c4ca27e9e6951f00cbe9f48594"></h2>


## if only you need java7...

```bash
# 1 install java7
brew tap homebrew/cask-versions
brew cask install homebrew/cask-versions/zulu7
```

