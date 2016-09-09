
# GO 实战

## GOPATH 设置

```
export GO_3rd=/Volumes/WORK/WORK/mebusy_git_codeLib/go_3rd_lib
export GOPATH=${GO_3rd}
export PATH=$PATH:${GO_3rd}/bin
```

## install GOCODE

```
go get -u github.com/nsf/gocode
```

will download source and generate an executable file

used for Vim ?


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