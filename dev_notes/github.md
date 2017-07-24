...menustart

 - [github](#bf215181b5140522137b3d4f6b73544a)
	 - [github update fork](#f6b73a9a864f02b2d14ad454c6b09e68)
	 - [run html on github](#606e5c37337c2f05305ab4a4a0dc2691)

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


## git status -s ignore file mode

```bash
git config core.filemode false
```

## git diff ignore `^M`

```bash
git config --global core.autocrlf true
```

 - `--golbal` will create `~/.gitconfig` file


