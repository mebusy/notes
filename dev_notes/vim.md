
# VIM 

## 插件安装

### 插件管理工具vunble

#### 安装vundle

```
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```


#### 在.vimrc配置文件中添加vundle支持

```
filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
```

### 配置插件

bundle分为三类，比较常用就是第二种：

 1. 在Github vim-scripts 用户下的repos,只需要写出repos名称
 2. 在Github其他用户下的repos, 需要写出”用户名/repos名” 
 3. 不在Github上的插件，需要写出git全路径


将安装的插件在~/.vimrc配置最后

```
" Define bundles via Github repos
Bundle 'christoomey/vim-run-interactive'
Bundle 'croaky/vim-colors-github'
Bundle 'danro/rename.vim'
Bundle 'majutsushi/tagbar'
Bundle 'kchmck/vim-coffee-script'
Bundle 'kien/ctrlp.vim'
Bundle 'pbrisbin/vim-mkdir'
Bundle 'scrooloose/syntastic'
Bundle 'slim-template/vim-slim'
Bundle 'thoughtbot/vim-rspec'
Bundle 'tpope/vim-bundler'
Bundle 'tpope/vim-endwise'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-rails'
Bundle 'tpope/vim-surround'
Bundle 'vim-ruby/vim-ruby'
Bundle 'vim-scripts/ctags.vim'
Bundle 'vim-scripts/matchit.zip'
Bundle 'vim-scripts/tComment'
Bundle "mattn/emmet-vim"
Bundle "scrooloose/nerdtree"
Bundle "Lokaltog/vim-powerline"
Bundle "godlygeek/tabular"
Bundle "msanders/snipmate.vim"
Bundle "jelera/vim-javascript-syntax"
Bundle "altercation/vim-colors-solarized"
Bundle "othree/html5.vim"
Bundle "xsbeats/vim-blade"
Bundle "Raimondi/delimitMate"
Bundle "groenewege/vim-less"
Bundle "evanmiller/nginx-vim-syntax"
Bundle "Lokaltog/vim-easymotion"
Bundle "tomasr/molokai"
Bundle "klen/python-mode"
Bundle "Valloric/YouCompleteMe"
```

### 安装

打开vim，运行 `:BundleInstall` 或在shell中直接运行


```
vim +BundleInstall +qall
```

### 安装排错

 - python 报错
 	- brew unlink python
 - `YouCompleteMe unavailable: No module named future`
 	- 进入YouCompleteMe目录，执行 `./install.py --all`
 	- 这时提示你一些第三方依赖缺失，执行下面的命令
 		- `git submodule update --init --recursive`
  - `sudo ./install.py --system-libclang --clang-completer --omnisharp-completer --gocode-completer --tern-completer`
 	- reinstall : 
   - `vim +PluginInstall`
 - `msbuild or xbuild is required to build Omnisharp`
  - You used --all, so you need to install mono for C sharp completion. If you don't want C sharp completion, use different flags.
  - install MonoFrameWork
  



