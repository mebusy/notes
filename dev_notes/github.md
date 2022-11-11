[](...menustart)

- [github](#bf215181b5140522137b3d4f6b73544a)
    - [run html on github](#606e5c37337c2f05305ab4a4a0dc2691)
    - [merge specific commit](#a6c7b8bc87e837e643f48e27b843d648)
    - [show file change of a commit](#e35fc6dbd7673d56c0824c31ff378241)
    - [get a file with specific revision](#6f4311248df3ab2115e904e14c7836c9)
    - [git show/diff 乱码问题](#aafd38d2cb2288571bb67fc78e3a18f7)
    - [\[trick\] use git log to display the diffs while searching](#a9df5d1d20b4eb063767169d82151fdc)
    - [show files changed between 2 commit](#384d969c3957ddc0b7be9841ff3549a8)
    - [provide username when clone private repos](#366ee47209629dccbab3d2399247ea84)
    - [gitlab: git clone leads to "SSL certificate problem: unable to get local issuer certificate"](#8da880caa0ca98d1c46a028c0da79aac)
    - [Calling git clone using password with special character](#60f96f2175fb84d4839e67f2533a4c10)
    - [Copy branch from another repository](#9af7d00519ec3625b399242404c33af2)
    - [delete a branch locally and remotely](#65804564299051849847b74237b908e7)
    - [delete all commit history in github](#299ba8422f7eafd171b8c712b9319131)
    - [delete all tags, local & remote](#f2bba2dd74d36e3d71aed69d628f2346)
    - [partial commmit](#365a5d68e803e7cd517640176167c02b)
    - [handling conflict](#bcccf2d6eb0a519d64f1b86b59fe5db3)
        - [Undo a conflict and start over](#a44d692e0cfa312f2d01e7cc424f3531)
    - [Reset Submodule](#740e34f3f2acfa61cdf6a6d376b3510d)

[](...menuend)


<h2 id="bf215181b5140522137b3d4f6b73544a"></h2>

# github 


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


<h2 id="a9df5d1d20b4eb063767169d82151fdc"></h2>

## [trick] use git log to display the diffs while searching

```
git log -p -- path/to/file
```


<h2 id="384d969c3957ddc0b7be9841ff3549a8"></h2>

## show files changed between 2 commit 

```bash
git diff commit1  commit2 --name-only
```



<h2 id="366ee47209629dccbab3d2399247ea84"></h2>

## provide username when clone private repos

```
git clone https://username:password@github.com/username/repository.git
```


<h2 id="8da880caa0ca98d1c46a028c0da79aac"></h2>

## gitlab: git clone leads to "SSL certificate problem: unable to get local issuer certificate"

```
git config --global http.sslVerify false
git clone ...
git config --global http.sslVerify true
```


<h2 id="60f96f2175fb84d4839e67f2533a4c10"></h2>

## Calling git clone using password with special character

```
!   #   $    &   '   (   )   *   +   ,   /   :   ;   =   ?   @   [   ]
%21 %23 %24 %26 %27 %28 %29 %2A %2B %2C %2F %3A %3B %3D %3F %40 %5B %5D
```

- for example

```
$ git clone https://myuser:password%21@github.com/myuser/repo.git
```

<h2 id="9af7d00519ec3625b399242404c33af2"></h2>

## Copy branch from another repository

 1. git clone your repo , so your repo's repo is named `origin`
 2. add another remote repo , give it name `html5`
    - `git remote add html5 ...` 
 3. fetch remote repo data
    - `git fetch html5`
 4. checkout 1 branch `html5/develop` , to your local branch `develop`
    - `git checkout -b develop html5/develop`
 5. push you local branch `develop` to `origin`
    - `git push --set-upstream origin develop`

<h2 id="65804564299051849847b74237b908e7"></h2>

## delete a branch locally and remotely

```
$ git push --delete <remote_name> <branch_name>
$ git branch -d <branch_name>
```


<h2 id="299ba8422f7eafd171b8c712b9319131"></h2>

## delete all commit history in github

1. Checkout
    - `git checkout --orphan latest_branch`
2. Add all the files
    - `git add -A`
3. Commit the changes
    - `git commit -am "commit message"`
4. Delete the branch
    - `git branch -D master`
5. Rename the current branch to master
    - `git branch -m master`
6. Finally, force update your repository
    - `git push -f origin master`


<h2 id="f2bba2dd74d36e3d71aed69d628f2346"></h2>

## delete all tags, local & remote

```bash
# delete remote tags before deleting locals
git tag | xargs -L 1 | xargs git push origin --delete

# then delete local tags
git tag | xargs -L 1 | xargs git tag --delete
```

<h2 id="365a5d68e803e7cd517640176167c02b"></h2>

## partial commmit 

```bash
git commit -p <filename>
```

<h2 id="bcccf2d6eb0a519d64f1b86b59fe5db3"></h2>

## handling conflict

<h2 id="a44d692e0cfa312f2d01e7cc424f3531"></h2>

### Undo a conflict and start over

- dealing with a merge conflict doesn't necessarily mean you have to resolve it, you can also undo it.
    ```bash
    git merge --abort
    ```
    ```bash
    git rebase --abort
    ```



<h2 id="740e34f3f2acfa61cdf6a6d376b3510d"></h2>

## Reset Submodule

```bash
# reset a specified sub module
$ git submodule update -f <module name>

# reset all sub modules
$ git submodule foreach git reset --hard
# reset all sub modules recursively
$ git submodule foreach --recursive git reset --hard
```



