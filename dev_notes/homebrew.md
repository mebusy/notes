...menustart

 - [homebrew](#c922a641cc5dc03a497e540996d12198)
     - [Reset Homebrew Fomular](#a655cf4302df90e17053b41af734deb9)
     - [Manually download brew package](#31cfdc0a967e58b7447b2e9b456d0f2f)
     - [Homebrew 使用 清华索引](#387e3f4aa69662696cce11325cecc502)
         - [brew update 索引镜像](#2b4d5ebf708a8726acef8ace48915e9f)
         - [brew binary 安装包  镜像](#eacd77990df567221ae4eec63f170ef4)
         - [初次安装 homebrew 出问题...](#ecd6d4ba468480e8557dcc476348dc6b)

...menuend


<h2 id="c922a641cc5dc03a497e540996d12198"></h2>


# homebrew

<h2 id="a655cf4302df90e17053b41af734deb9"></h2>


## Reset Homebrew Fomular

```
$ cd $(brew --repo)/Library/Taps/homebrew/homebrew-core/
$ git reset --hard HEAD
```


<h2 id="31cfdc0a967e58b7447b2e9b456d0f2f"></h2>


## Manually download brew package 

 - use `brew --cache` to find the cache folder 
 - homebrew use `brew --cache`\downloads folder to keep downloaded files
    - and use `ln -s` to make a reference at `brew --cache` folder 
 - 目标文件 可以通过如下命令获得
    - `brew --cache [-s] <package_name>`  ( -s means from source , not bottle )

<h2 id="387e3f4aa69662696cce11325cecc502"></h2>


## Homebrew 使用 清华索引

<h2 id="2b4d5ebf708a8726acef8ace48915e9f"></h2>


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

<h2 id="eacd77990df567221ae4eec63f170ef4"></h2>


### brew binary 安装包  镜像

```bash
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
```


<h2 id="ecd6d4ba468480e8557dcc476348dc6b"></h2>


### 初次安装 homebrew 出问题...

1. 先下载 brew install 文件 ( 安装命令的 curl 那一段 ), 保存为 `brew_install`
2. 修改
    - 
    ```bash
    BREW_REPO = "https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git".freeze
    CORE_TAP_REPO="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git".freeze
    ```
3. `ruby brew_install` 安装
4. 安装完成后，替换homebrew源
5. `brew update`


