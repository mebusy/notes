...menustart

 - [VIM](#d53cfc4bdeb96eaee47dd710b3c2ed21)
     - [插件安装](#78d0b83eb54eb1aa949d4600958cb397)
         - [插件管理工具vunble](#5a8a69602edd805333aea10c2817e37e)
             - [安装vundle](#f1c28a7da5182846402b968966299c4c)
             - [在.vimrc配置文件中添加vundle支持](#88320719ea4a6c706aeaa3ae1d8c133d)
         - [配置插件](#7a886abbb5da4373ffcfd88df9575954)
         - [安装](#e655a410ff21cd07e7a0150491e04371)
         - [安装排错](#154a11cd7a6e424863c28aa29ad576d1)
     - [Markdown](#2182a74bab7188d959e795d9301e87ff)
     - [install VIM8 on Centos7](#a80bb46a45ac01cfeecb23364ec0bb63)
     - [install YouCompleteMe on Centos7](#e452f90f1770e33615e0eb6ee4a22953)
     - [check vim compile features](#95cec38eef2cf37c01f98f869cb8e4bc)
 - [VIM 正则表达式](#072db16a2fab851f315188d28a992133)
     - [关于magic](#9e8ec078a153381638b723f644bc0f67)
     - [捕获组](#1ca7c638c2ce8ef41b651ccf8e827bf3)
     - [Misc](#74248c725e00bf9fe04df4e35b249a19)
 - [参数列表](#cba8744406ca022515965ad373474f74)
 - [Mark](#b82a9a13f4651e9abcbde90cd24ce2cb)
 - [VIM 常用操作](#508b03ab799d17da8b37eb7801c05c8b)
     - [搜索](#e5f71fc31e7246dd6ccc5539570471b0)
         - [反向肯定搜索 lookahead](#32b92ada221fd37f58c6db5897bd605c)
         - [前向肯定搜索 lookahead](#852639e354e873ce19ce571888957160)
         - [文件夹搜索](#4d36d00db257fed5fe7d2a2036ad930f)
     - [文件夹 替换](#476949b7922fe3e5ea39c034861527d8)
     - [多行 行首插入字符](#4b0c82f3072a7a2d205d934ca7413367)
     - [多行 行尾插入字符](#facc78c7266b3fe0364882da91e214b8)
     - [replace all tab with 4 space](#72ec54ea94cad51a12851d38a51ea25f)

...menuend


<h2 id="d53cfc4bdeb96eaee47dd710b3c2ed21"></h2>

# VIM 

<h2 id="78d0b83eb54eb1aa949d4600958cb397"></h2>

## 插件安装

<h2 id="5a8a69602edd805333aea10c2817e37e"></h2>

### 插件管理工具vunble

<h2 id="f1c28a7da5182846402b968966299c4c"></h2>

#### 安装vundle

```
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```


<h2 id="88320719ea4a6c706aeaa3ae1d8c133d"></h2>

#### 在.vimrc配置文件中添加vundle支持

```
filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
```

<h2 id="7a886abbb5da4373ffcfd88df9575954"></h2>

### 配置插件

bundle分为三类，比较常用就是第二种：

 1. 在Github vim-scripts 用户下的repos,只需要写出repos名称
 2. 在Github其他用户下的repos, 需要写出”用户名/repos名” 
 3. 不在Github上的插件，需要写出git全路径


将安装的插件在~/.vimrc配置最后

```
" 使用Vundle来管理Vundle
Bundle 'gmarik/vundle'
 
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
Bundle "Valloric/YouCompleteMe"
```

<h2 id="e655a410ff21cd07e7a0150491e04371"></h2>

### 安装

打开vim，运行 `:BundleInstall` 或在shell中直接运行


```
vim +BundleInstall +qall
```

<h2 id="154a11cd7a6e424863c28aa29ad576d1"></h2>

### 安装排错

 - python 报错
     - brew unlink python
 - `YouCompleteMe unavailable: No module named future`
     - 进入YouCompleteMe目录，执行 `./install.py --all`
     - 这时提示你一些第三方依赖缺失，执行下面的命令
         - `git submodule update --init --recursive`
 - add suport for C family
     - `./install.py --clang-completer --system-libclang`
     - using `--system-libclang` here because on MacOSX, it report error "NOT using libclang, no semantic completion for C/C++/ObjC will be available"
 - addd c# support
    - `./install.py --omnisharp-completer`
 - add go support
    - `./install.py --gocode-completer`
 - add rust support
    - `./install.py --rust-completer` 
    - get rust source code from https://www.rust-lang.org/en-US/other-installers.html#source
    - vi ~/.vimrc
        - `let g:ycm_rust_src_path = '/usr/local/rust/rustc-1.20.0/src'`
        - note: you should give the src folder which has .lock / .toml file in the root.

```
# carge under proxy 
vi ~/.cargo/config

[http]
proxy = "http://user:password@host:port"
```

 - reinstall : 
    - `vim +PluginInstall`
 - update :
    - `vim +PluginUpdate`
 - `msbuild or xbuild is required to build Omnisharp`
    - You used `--all`, so you need to install mono for C sharp completion. If you don't want C sharp completion, use different flags.
    - install MonoFrameWork
 - `vim +PluginInstall` YouCompleteMe 有时 helptags 会报错
    - 修复报错 目录权限 `chmod -R 777 xxx` 
 - Tagbar 需要安装 ctags 
    - `brew install ctags`
    - use : `TagbarToggle`
 - python 语法检查
    - `pip install flake8`
 - use older YouCompleteMe in case of lower version of vim 
    - enter YouCompleteMe plugin foler 
    - git reset --hard 68d78719a45ee8e9e86a2effb99c80842ccadada
    - or to install vim 7.4.2356
        - vim 7.4.2358 git hash: d47d83745ff450232328ca7a4b8b00b31bad22fc
 
 - vim 诊断
    - `:YcmDebugInfo`
 
 - vim check logs
    - `YcmToggleLogs`
 
 - uninstall mono framework on OSX 
    - https://gist.githubusercontent.com/powerumc/e80bb475117582d7e842/raw/ed8a29bed15655492109c91df118f22b147f025c/remove-mono.sh
 - snipmate <TAB> YouCompleteMe 冲突
    - `~/.vim/bundle/snipmate.vim/after/plugin/snipMate.vim`

```
change 

" You can safely adjust these mappings to your preferences (as explained in
" :help snipMate-remap).
ino <silent> <tab> <c-r>=TriggerSnippet()<cr>
snor <silent> <tab> <esc>i<right><c-r>=TriggerSnippet()<cr>

to 

ino <silent> <C-\> <c-r>=TriggerSnippet()<cr>
snor <silent> <C-\> <esc>i<right><c-r>=TriggerSnippet()<cr>
```

<h2 id="2182a74bab7188d959e795d9301e87ff"></h2>

## Markdown 

 - chrome 安装插件 :  [Markdown Preview Plus](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl)
 - 打开 `chrome://extensions/` ， 在设置页中勾选 “Allow access to file URLs”

<h2 id="a80bb46a45ac01cfeecb23364ec0bb63"></h2>

## install VIM8 on Centos7

```
1. install the necessary package.
yum install gcc-c++ ncurses-devel python-devel lua-devel -y

2. Get the source code of Vim.
git clone https://github.com/vim/vim.git

# Use the version like my MacVim.
cd vim/src && git checkout v8.0.1350

3. Configure it !
./configure --with-features=huge --enable-pythoninterp=dynamic  --enable-luainterp=dynamic


4. compile
make
make install
```

```
./configure 后面的配置选项
–with-features=huge：支持最大特性
–enable-rubyinterp：打开对ruby编写的插件的支持
–enable-pythoninterp：打开对python编写的插件的支持
–enable-python3interp：打开对python3编写的插件的支持
–enable-luainterp：打开对lua编写的插件的支持
–enable-perlinterp：打开对perl编写的插件的支持
–enable-multibyte：打开多字节支持，可以在Vim中输入中文
–enable-cscope：打开对cscope的支持
–with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ 指定python 路径
–with-python-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/ 指定python3路径
–prefix=/usr/local/vim：指定将要安装到的路径(自行创建)
```


<h2 id="e452f90f1770e33615e0eb6ee4a22953"></h2>

## install YouCompleteMe on Centos7

 1. yum 安装 clang
 2. build YCME

```
CC=`which clang` CXX=`which clang++`  ./install.py ......
```

<h2 id="95cec38eef2cf37c01f98f869cb8e4bc"></h2>

## check vim compile features

```bash
vim --version
```
   
---

<h2 id="072db16a2fab851f315188d28a992133"></h2>

# VIM 正则表达式

<h2 id="9e8ec078a153381638b723f644bc0f67"></h2>

## 关于magic

 - 常见的编辑器，一般都可以指定是 普通搜索还是使用正则表达式搜索
 - 但vim模式的是混合搜索，既 magic (\m)模式
    - 比如 `/foo(1)` 命令， 大多数人都是用它来查找foo(1)这个字符串.
    - 于是，vim就规定，正则表达式的元字符必须用反斜杠进行转义才行， 如上面的例子，如果确实要用正则表达式，就应当写成 `/foo\(1\)`
    - 但是，像 `.` `*` 这种极其常用的元字符，都加上反斜杠就太麻烦了。 而且，众口难调，有些人喜欢用正则表达式，有些人不喜欢用……
 - 为了解决这个问题，vim设置了 magic 这个东西。简单地说， magic就是设置哪些元字符要加反斜杠哪些不用加的。 简单来说：
    - magic (\m): 除了 `$ . * ^` 之外其他元字符都要加反斜杠
    - nomagic (\M): 除了 `$ ^` 之外其他元字符都要加反斜杠。
    - `/\m.*` # 查找任意字符串
    -  `/\M.*` # 查找字符串 `.*` 
 - 另外还有更强大的 \v 和 \V。
    - \v （即 very magic 之意）: 任何元字符都不用加反斜杠 
    - \V （即 very nomagic 之意）: 任何元字符都必须加反斜杠



<h2 id="1ca7c638c2ce8ef41b651ccf8e827bf3"></h2>

## 捕获组

 - 捕获组符号和perl 略有不同，使用 `@` 而不是 `(?`
 - TODO: 确认 是否真的不支持 perl 模式？ (比如 非贪婪匹配 就同时支持)

Perl | vim
--- | ---
(?= | @=
(?! | @!
(?<= | @<=
`(?<!` | `@<!`
(?> | @> 
(?: |  `%(atom\)`

 - vim中的捕获组的模式的位置与perl不同
    - 例如，查找紧跟在 foo 之后的 bar，perl将模式(这里是foo)写在环视(`?<=`)的括号内, 而vim将模式写在环视的元字符之前。
    - Perl的写法 `(?<=foo)bar`
    - vim的写法 `(foo)@<=bar` 

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

## Misc

 - vim 没有 \b, 匹配单词词首词尾使用 `<` , `>`


---

<h2 id="cba8744406ca022515965ad373474f74"></h2>

# 参数列表

 - 每一个通过 shell 命令传递给 Vim 的文件名都被记录在一个参数列表中。
 - 可以有多个参数列表：
    - 默认情况下所有参数都被放在全局参数列表下，但是你可以使用 :arglocal 命令去创建一个新的本地窗口的参数列表。
 - 使用 :args 命令可以列出当前参数
 - 参数列表在有些情况下被大量使用：批处理 
 - 使用 :argdo！ 一个简单的重构例子：

```
:args **/*.[ch]
:argdo %s/foo/bar/ge | update
```

 - 这条命令将替换掉当前目录下以及当前目录的子目录中所有的 C 源文件和头文件中的“foo”，并用“bar”代替。

----

<h2 id="b82a9a13f4651e9abcbde90cd24ce2cb"></h2>

# Mark 

 - 设置mark
    - `mX`
    - `X` 的说明：


mark | 设置者  | 使用
--- | --- | --- 
a-z | 用户 | 仅对当前的一个文件生效，也就意味着只可以在当前文件中跳转
A-Z | 用户 | 全局标注，可以作用于不同文件。大写标注也称为「文件标注」。跳转时有可能会切换到另一个缓冲区
0-9 | viminfo | 0 代表 viminfo 最后一次被写入的位置。实际使用中，就代表 Vim 进程最后一次结束的位置。1 代表 Vim 进程倒数第二次结束的位置，以此类推

 - 跳转到 mark
    - `'X` 或 ``X`





---

<h2 id="508b03ab799d17da8b37eb7801c05c8b"></h2>

# VIM 常用操作

<h2 id="e5f71fc31e7246dd6ccc5539570471b0"></h2>

## 搜索

<h2 id="32b92ada221fd37f58c6db5897bd605c"></h2>

### 反向肯定搜索 lookahead

```
\(exp1\)\@<=exp2
```

搜索 exp2， start with exp1 .

固定模式：  `\(exp\)` + `pattern` 


<h2 id="852639e354e873ce19ce571888957160"></h2>

### 前向肯定搜索 lookahead

搜索 exp1, followed by exp2

```
exp1\(exp2\)\@=
```

<h2 id="4d36d00db257fed5fe7d2a2036ad930f"></h2>

### 文件夹搜索

```
vimgrep /pattern/gj path
```

 - 参数:
    - g: 一行中出现多次，只显示一次
    - j: 只列出匹配的行
 - path
    - `./*.c`  当前文件夹下 c 文件中查找
    - `**/*.*`  包括子文件夹下 所有文件


搜索完毕 copen 或 cw 查看搜索列表

<h2 id="476949b7922fe3e5ea39c034861527d8"></h2>

## 文件夹 替换

查找

```
:args *.cpp
:argdo /word
```

替换

```
:args *.cpp
:argdo %s/word/NEW/eg | update
```

 - 见[参数列表]

<h2 id="4b0c82f3072a7a2d205d934ca7413367"></h2>

## 多行 行首插入字符

 1. 光标置与第一行行首, ctrl-v 进入  VISUAL BLOCK
 2. 向下移动光标 选中所有行
 3. shift i 进入多行插入模式， 编辑 , esc 
 4. 等 1秒钟， 修改完成

<h2 id="facc78c7266b3fe0364882da91e214b8"></h2>

## 多行 行尾插入字符

 - 对多行行首插入的 第三步进行修改
    1. Press $ to extend the visual block to the end of each line.
    2. Press A ，进入行尾编辑
    3. 编辑 , esc


<h2 id="72ec54ea94cad51a12851d38a51ea25f"></h2>

## replace all tab with 4 space

```
:%!expand -t4
```

---




