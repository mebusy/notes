...menustart

 - [github](#bf215181b5140522137b3d4f6b73544a)
     - [github update fork](#f6b73a9a864f02b2d14ad454c6b09e68)
     - [run html on github](#606e5c37337c2f05305ab4a4a0dc2691)
     - [git status -s ignore file mode](#ecf2b9ae77e1b9272d6716ab8337c37e)
     - [merge specific commit](#a6c7b8bc87e837e643f48e27b843d648)
     - [show file change of a commit](#e35fc6dbd7673d56c0824c31ff378241)
     - [get a file with specific revision](#6f4311248df3ab2115e904e14c7836c9)
     - [git show/diff 乱码问题](#aafd38d2cb2288571bb67fc78e3a18f7)
     - [how to set up username and passwords for different git repos](#a3aecaf26f7ec612b34f4d9ed6c6532d)

...menuend


<h2 id="bf215181b5140522137b3d4f6b73544a"></h2>

# github 

<h2 id="f6b73a9a864f02b2d14ad454c6b09e68"></h2>

## github update fork

 - 给fork配置远程上游仓库 
    - `git remote add upstream xxxx.git`
 - 同步fork
    - 从上游仓库 fetch 分支和提交点，提交给本地 master，并会被存储在一个本地分支 upstream/master 
        - `git fetch upstream` 
    - 切换到本地主分支(如果不在的话) 
        - `git checkout master` 
    - 把 upstream/master 分支合并到本地 master 上，这样就完成了同步，并且不会丢掉本地修改的内容。
        - `git merge upstream/master` 
    - 提交 
        - `git push origin master`

        
<h2 id="606e5c37337c2f05305ab4a4a0dc2691"></h2>

## run html on github

 - visit `http://rawgit.com/`
 - 输入你需要执行的 html 网页，会给出两个链接
    - https://rawgit.com/mebusy/html5_examples/master/XXXX.html
        - url for production
    - https://cdn.rawgit.com/mebusy/html5_examples/master/XXXX.html
        - url for dev/testing
 - 注意： cdn.rawgit.com 上的文件，第一次访问后会被 永久cache，从而导致 拉取不到最新的文件。
    - 所以一般访问的时候，会指定 某个 commit hash  ， 或使用最新的 HEAD
    - `https://cdn.rawgit.com/mebusy/html5_examples/a12340a5d32b0c760ef138301b067fb1153ef94b/00_marchingSquare.html`
    - or `https://cdn.rawgit.com/mebusy/html5_examples/HEAD/00_marchingSquare.html`


<h2 id="ecf2b9ae77e1b9272d6716ab8337c37e"></h2>

## git status -s ignore file mode

```bash
git config core.filemode false
```

<h2 id="a6c7b8bc87e837e643f48e27b843d648"></h2>

## merge specific commit 

```
git cherry-pick [-n] <commit> 
```

 - `-n` means `no commit `

<h2 id="e35fc6dbd7673d56c0824c31ff378241"></h2>

## show file change of a commit 

```
git diff-tree <commit>
```

<h2 id="6f4311248df3ab2115e904e14c7836c9"></h2>

## get a file with specific revision

```
git show REVISION:filePath > outFilePath
```


<h2 id="aafd38d2cb2288571bb67fc78e3a18f7"></h2>

## git show/diff 乱码问题

```
git diff | less -r
```

 - `-r` means `Output "raw" control characters`.


<h2 id="a3aecaf26f7ec612b34f4d9ed6c6532d"></h2>

## how to set up username and passwords for different git repos

 1. Using SSH 
    - `ssh-agent`  and `ssh-add`
 2. Using gitcredentials
    - https://git-scm.com/docs/gitcredentials

```
git config --global credential.${remote}.username yourusername
git config --global credential.helper store
```

 - here, `{remote}` is something like `https://github.com`
 - 仓库 pull 下来后， 把上面两条指令 去掉 `--global` 再执行一次， 同时 删除`~/.gitconfig ` 中的 credential 设置，以避免影响其他的仓库冲突

```
$ cat ~/.gitconfig
[credential "https://github.com"]
    username = xxxxx
[credential]
    helper = store
```

## provide username when clone private repos

```
git clone https://username:password@github.com/username/repository.git
```


