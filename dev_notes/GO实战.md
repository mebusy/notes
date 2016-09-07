
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

used for Vim ?


## GODEP

```
go get github.com/tools/godep
```

```
cd project_folder
godep save
```

