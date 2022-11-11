<h2 id="c75625dccf148721245b46b1e3e6c79f"></h2>

### 文章

 1. [语言](GOLANG%20%E5%A4%87%E5%BF%981-%E8%AF%AD%E8%A8%80.md)   
 2. [表达式](GOLANG%20%E5%A4%87%E5%BF%982-%E8%A1%A8%E8%BE%BE%E5%BC%8F.md) 
 3. [函数 ](GOLANG%20%E5%A4%87%E5%BF%983-%E5%87%BD%E6%95%B0.md) 
 4. [数据 ](GOLANG%20%E5%A4%87%E5%BF%984-%E6%95%B0%E6%8D%AE.md)
 5. [方法和接口](GOLANG%20%E5%A4%87%E5%BF%985-%E6%96%B9%E6%B3%95%E5%92%8C%E6%8E%A5%E5%8F%A3.md)  
 7. [并发](GOLANG%20%E5%A4%87%E5%BF%987-%E5%B9%B6%E5%8F%91.md)  
 8. [包](GOLANG%20%E5%A4%87%E5%BF%988-%E5%8C%85.md)    
 9. [反射](GOLANG%E5%A4%87%E5%BF%989-%E5%8F%8D%E5%B0%84.md)  
 10. [工具](GOLANG%E5%A4%87%E5%BF%98A-%E5%B7%A5%E5%85%B7.md) ||  [go命令详解](https://www.ctolib.com/docs-go-command-tutorial-c-0-0.html)
 11. [测试](GOLANG%E5%A4%87%E5%BF%98B-%E6%B5%8B%E8%AF%95.md)
 12. [go格式化输出 ](GOLANG-fmt%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BE%93%E5%87%BA.md)
 13. [go源码剖析笔记](GOLANG_src_profile.md)
 14. [learn Go in Y minutes](learnGoInYMinutes.md)
 15. [A Tour of GO](ATourOfGo.md)
 16. [cheat sheet](golang_cheatsheet.md)
 17. [GoInPractice70Tech](GoInPractice70Tech.md), [6 template](GoIn70_6.md), [7 web form](GoIn70_7.md), [8 with web service](GoIn70_8.md), [9 cloud, 10 micro service](GoIn70_9.md), [11 reflection & code generation](GoIn70_11.md)
 18. [go tips](go_tips.md)
 19. [godoc](godoc.md)
 20. [go pprof](golang_pprof.md)
 21. [ways to sort in go](go_sort.md)
 22. [go encrypt](go_encrypt.md)
 23. [goroutine调度器](go_routine_schedule.md)
 24. [cgo](cgo.md)
 25. [gorilla websocket](websocket.md)
 26. [go template cheatsheet](https://curtisvermeeren.github.io/2017/09/14/Golang-Templates-Cheatsheet)

---------

<h2 id="0a924bf17d1b7242d5600e9b537b969f"></h2>

### 国内获取 golang.org/x 包失败的方法

- 其实 golang 在 github 上建立了一个[镜像库](https://github.com/golang)，如 https://github.com/golang/net 即是 https://golang.org/x/net 的镜像库
- 获取 golang.org/x/net 包，其实只需要以下步骤

```
mkdir -p $GOPATH/src/golang.org/x
cd $GOPATH/src/golang.org/x
git clone https://github.com/golang/net.git
```
 
```
mkdir -p $GOPATH/src/golang.org/x
cd $GOPATH/src/golang.org/x
git clone https://github.com/golang/tools.git
```

<h2 id="592aa5aafd64f18a5b4759ec0820ef33"></h2>

### get get update multiple pacakge 

```
go get -u all
```

or 

```
go get -u github.com/...
go get -u gopkg.in/...
```

<h2 id="e8db5cfdd7d47c516453db67161e7537"></h2>

### list all package 

```
go list ...
```

<h2 id="e761880bea8f1f8b4c77ba1e0662b258"></h2>

### list all GOOS/GOARCH

```
go tool dist list
```
