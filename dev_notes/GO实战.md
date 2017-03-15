...menustart

 - [GO 实战](#d377ec978809d67b7948b261487ba02b)
	 - [GOPATH 设置](#6481ce3fb6b328bb1e82e6e522b210dc)
	 - [install GOCODE](#2022e82706466d8b15058a5027a0bc37)
	 - [GODEP](#a6d1abc102144483fec13090f9b679d0)
	 - [Beego](#9a67bfaa06e4cf023ca0f3a9bf491e97)

...menuend


<h2 id="d377ec978809d67b7948b261487ba02b"></h2>
# GO 实战

<h2 id="6481ce3fb6b328bb1e82e6e522b210dc"></h2>
## GOPATH 设置

```
export GO_3rd=/Volumes/WORK/WORK/mebusy_git_codeLib/go_3rd_lib
export GOPATH=${GO_3rd}
export PATH=$PATH:${GO_3rd}/bin
```

<h2 id="2022e82706466d8b15058a5027a0bc37"></h2>
## install GOCODE

```
go get -u github.com/nsf/gocode
```

will download source and generate an executable file

used for Vim ?


<h2 id="a6d1abc102144483fec13090f9b679d0"></h2>
## GODEP

```
go get -u github.com/tools/godep
```

 - src code
 - pkg
 - executable file

```
cd project_folder
godep save
```

<h2 id="9a67bfaa06e4cf023ca0f3a9bf491e97"></h2>
## Beego

```
go get -u github.com/astaxie/beego
```

 - src code
 - pkg


```
go get -u github.com/beego/bee
```

 - massive src code
 - pkg
 - bee executable file