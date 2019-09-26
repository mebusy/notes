
# homebrew

## Reset Homebrew Fomular

```
$ cd $(brew --repo)/Library/Taps/homebrew/homebrew-core/
$ git reset --hard HEAD
```


## Manually download brew package 

 - use `brew --cache` to find the cache folder 
 - homebrew use `brew --cache`\downloads folder to keep downloaded files
    - and use `ln -s` to make a reference at `brew --cache` folder 
 - 目标文件 可以通过如下命令获得
    - `brew --cache [-s] <package_name>`  ( -s means from source , not bottle )

<h2 id="b7b1e314614cf326c6e2b6eba1540682"></h2>


## Homebrew 使用 清华索引

### brew update 索引镜像

替换现有上游:

```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git

brew update
```

恢复官方

```bash
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git

brew update
```

### brew binary 安装包  镜像

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
```
