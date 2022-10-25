...menustart

- [VIM](#d53cfc4bdeb96eaee47dd710b3c2ed21)
    - [插件安装](#78d0b83eb54eb1aa949d4600958cb397)
    - [YouCompleteMe 配置](#95e1e8a5d4d20276318a364f9428f879)
    - [C-Family 补全配置文件](#6c21b0240dca1c94dbf59f8b1ab1f1af)
        - [YCMD 排错](#f7abfec0b5984a0314616bd13f7ae8c3)
    - [Markdown](#2182a74bab7188d959e795d9301e87ff)
    - [viminspect](#05792acc8846850d5650256c2f89d097)
        - [debug nodejs](#a76b761a3f63c8a3aca6fa66777741fa)
    - [VIM 正则表达式](#072db16a2fab851f315188d28a992133)
    - [vim Mark](#ac4aee7e186902860d64dcf2a6065905)
    - [VIM tips](#a1c1a23da31214c88d29928e14c64ef0)
        - [文件夹内容替换 args/argdo](#d97b62cc38ac0f48ee2ef1675eceb014)
        - [搜索 (lookahead, lookbehind, contains `/`)](#0b4ec6e4487065d67922bc151a3fe175)
        - [文件夹搜索 vimgrep](#54afc9723e7bdaa4cf548df28b7e9541)
        - [多行 行首插入字符](#4b0c82f3072a7a2d205d934ca7413367)
        - [多行 行尾插入字符](#facc78c7266b3fe0364882da91e214b8)
        - [duplicated column, paste next to it](#11cc6cd769420b9372c1b33a98a38d5e)
        - [Remove unwanted empty lines](#67c5f9b419ed15a16a0cb4786a4a6552)
        - [make multiple line word into java string](#fe7fb0107de52ad2a0bca9917a32301a)
        - [复制/移动 行](#87b0406cc2b93c7df74c3cfc9b2e690b)
- [grok VIM](#fc1f1e8c6d70d860957c66f735e60e2b)
    - [A sampling of more advanced tricks:](#a5787082a16f14e8db2acbf78497ee99)

...menuend


<h2 id="d53cfc4bdeb96eaee47dd710b3c2ed21"></h2>


# VIM 

<h2 id="78d0b83eb54eb1aa949d4600958cb397"></h2>


## 插件安装


- 安装vundle
    ```
    git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
    ```

-  在.vimrc配置文件中添加vundle支持
    ```
    filetype off
    set rtp+=~/.vim/bundle/vundle/
    call vundle#rc()
    ```

- 配置插件
    - bundle分为三类，比较常用就是第二种：
        1. 在Github vim-scripts 用户下的repos,只需要写出repos名称
        2. 在Github其他用户下的repos, 需要写出”用户名/repos名” 
        3. 不在Github上的插件，需要写出git全路径
    - 将其他需要 安装的插件 加入到 ~/.vimrc
        ```
        " 使用Vundle来管理Vundle
        Bundle 'gmarik/vundle'
         
        " Define bundles via Github repos
        Bundle 'christoomey/vim-run-interactive'
        Bundle 'croaky/vim-colors-github'
        Bundle "Valloric/YouCompleteMe"
        ...
        ```

- 安装插件
    - 打开vim，运行 `:BundleInstall` 或在shell中直接运行
        ```
        vim +BundleInstall +qall
        ```
    - update :
        ```
        vim +PluginUpdate
        ```

<h2 id="95e1e8a5d4d20276318a364f9428f879"></h2>


## YouCompleteMe 配置

- for C family support:  `./install.py --clangd-completer`
    - 加上 `--system-libclang` 则使用mac 自带的libclang，但是一般版本比较旧，会有问题
- C# support: install Mono and add `--cs-completer` 
- Go support: install Go and add `--go-completer` 
- JavaScript and TypeScript support: install Node.js and npm and add `--ts-completer` 
    - NOTE: TSServer relies on the  [jsconfig.json](https://code.visualstudio.com/docs/languages/jsconfig) for javascript and  [tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) for typescript  to analyze your project. Ensure the file exists at the root of your project.
        - **PS**: ycm will look up `jsconfig.json` up to the top parent directory, and think the final directory as `root` and parse all .js files under it, it may break ycm ... So do **NOT** put a `jsconfig.json` file outside of your project.
    - To get diagnostics in JavaScript, set the checkJs option to true in your jsconfig.json file:
        ```json
        {
            "compilerOptions": {
                "checkJs": true
            }
        }
        ```
- Rust support: install Rust and add `--rust-completer` when calling ./install.py.
    - put `~/.cargo/bin`   in you $PATH ?
        ```bash
        # rust
        export PATH=$HOME/.cargo/bin:$PATH
        ```
- Java support: install JDK8 (version 8 required) and add `--java-completer` 
- for common using
    ```bash
    ./install.py --clangd-completer --cs-completer  --go-completer --ts-completer --java-completer
    ```
    ```bash
    # --clang-completer --system-libclang
    ```
    - for Ubuntu, `sudo apt install build-essential` is needed


<h2 id="6c21b0240dca1c94dbf59f8b1ab1f1af"></h2>


## C-Family 补全配置文件

- YCM 会一层一层目录往上查找 .ycm_extra_conf.py 配置文件
- example: https://github.com/ycm-core/ycmd/blob/master/.ycm_extra_conf.py
- and you normally need do some modification for c-project
	```python
		# THIS IS IMPORTANT! Without the '-x' flag, Clang won't know which language to
		# use when compiling headers. So it will guess. Badly. So C++ headers will be
		# compiled as C headers. You don't want that so ALWAYS specify the '-x' flag.
		# For a C project, you would set this to 'c' instead of 'c++'.
		'-x',
		'c',
		'-std=c99',
		'-isystem', # OSX c headers
		'/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/',  
		'-isystem', 
		'./program/include/' , # you project headers
		...
	```


<h2 id="f7abfec0b5984a0314616bd13f7ae8c3"></h2>


### YCMD 排错

- Tagbar 需要安装 ctags 
    - `brew install ctags`
    - for golang, you also need gotags `brew install gotags`
- python 语法检查
    - `pip install flake8`
- vim 诊断
    - `:YcmDebugInfo`
- vim check logs
    - `YcmToggleLogs`
- output log to file
    - running vim with the -V[N] option will do a pretty hefty runtime log, here N is the debug level.
        ```bash
        vim -V9myVim.log
        ```
    - would create a log of debug level 9 in the current directory with the filename myVim.log


<h2 id="2182a74bab7188d959e795d9301e87ff"></h2>


## Markdown 

- chrome 安装插件 :  [Markdown Preview Plus](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl)
- 打开 `chrome://extensions/` ， 在设置页中勾选 “Allow access to file URLs”


<h2 id="05792acc8846850d5650256c2f89d097"></h2>


## viminspect

<h2 id="a76b761a3f63c8a3aca6fa66777741fa"></h2>


### debug nodejs

- launch app in inspect mode
    ```bash
    node --inspect app.js
    
    # if you're using nodemon
    nodemon --config nodemon.json --async-stack-traces --exec 'node --inspect app.js'
    ```

- .vimspector.json 
    <details>
    <summary>
    for nodejs app, both attach processID and run
    </summary>

    ```json
    {
      "configurations": {
        "attach": {
          "adapter": "vscode-node",
          "default": true,
          "breakpoints": {
            "exception": {
              "all": "N",
              "uncaught": "N"
            }
          },
          "configuration": {
            "name": "Attaching to a process ID",
            "type": "node",
            "request": "attach",
            "skipFiles": ["node_modules/**/*.js", "<node_internals>/**/*.js"],
            "processId": "${processId}"
          }
        },
        "run": {
          "adapter": "vscode-node",
          "default": true,
          "breakpoints": {
            "exception": {
              "all": "N",
              "uncaught": "N"
            }
          },
          "configuration": {
            "name": "Launch Program",
            "type": "node",
            "request": "launch",
            "stopOnEntry": true,
            "skipFiles": ["node_modules/**/*.js", "<node_internals>/**/*.js"],
            "program": "${workspaceRoot}/app.js"
          }
        }
      }
    }
    ```

    </details>

- you can also customize debugging port
    ```bash
    node --inspect=5678 app.js 
    ```
    ```json
          "configuration": {
            "name": "Attaching to a process ID",
            "type": "node",
            "port": "5678",
            "request": "attach",
            "skipFiles": ["node_modules/**/*.js", "<node_internals>/**/*.js"],
            "processId": "${processId}"
          }
    ```


<h2 id="072db16a2fab851f315188d28a992133"></h2>


## VIM 正则表达式


<details>
<summary>
关于Magic
</summary>

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

</details>


<details>
<summary>
捕获组
</summary>

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

</details>

- vim 没有 \b, 匹配单词词首词尾使用 `<` , `>`



<h2 id="ac4aee7e186902860d64dcf2a6065905"></h2>


## vim Mark 

- 设置mark
    - `mX`
    - `X` 的说明：

mark | 设置者  | 使用
--- | --- | --- 
a-z | 用户 | 仅对当前的一个文件生效，也就意味着只可以在当前文件中跳转
A-Z | 用户 | 全局标注，可以作用于不同文件。大写标注也称为「文件标注」。跳转时有可能会切换到另一个缓冲区
0-9 | viminfo | 0 代表 viminfo 最后一次被写入的位置。实际使用中，就代表 Vim 进程最后一次结束的位置。1 代表 Vim 进程倒数第二次结束的位置，以此类推


- mark 命令小结
    ```txt
    m ——创建标记
    ' ——移动到标记的文本行首
    ` ——移动到标记的光标位置
    :marks ——列示所有标记
    :delmarks ——删除指定标记
    :delmarks! ——删除所有标记
    ```

<h2 id="a1c1a23da31214c88d29928e14c64ef0"></h2>


## VIM tips

- check vim compile features
    ```bash
    vim --version
    ```

- clear a register
    ```vim
    # set register `i`  empty
    qiq

    # or remove register `i`
    :exec setreg('i', [])
    ```

<h2 id="d97b62cc38ac0f48ee2ef1675eceb014"></h2>


### 文件夹内容替换 args/argdo

- 每一个通过 shell 命令传递给 Vim 的文件名都被记录在一个参数列表中。
- 可以有多个参数列表：
    - 默认情况下所有参数都被放在全局参数列表下，但是你可以使用 :arglocal 命令去创建一个新的本地窗口的参数列表。
- 使用 :args 命令可以列出当前参数
- 参数列表在有些情况下被大量使用：批处理 
- 使用 :argdo！ 一个简单的重构例子：
    ```vim
    :args **/*.[ch]
    :argdo /word   # 查找
    :argdo %s/foo/NEW/ge | update  # 查找“foo”，并用“bar”代替
    ```

<h2 id="0b4ec6e4487065d67922bc151a3fe175"></h2>


### 搜索 (lookahead, lookbehind, contains `/`)

- 反向肯定搜索 lookbehind
    - 搜索 exp2， start with exp1 .
    ```vim
    \(exp1\)\@<=exp2
    ```
- 前向肯定搜索 lookahead
    - 搜索 exp1, followed by exp2
    ```vim
    exp1\(exp2\)\@=
    ```
- 搜索 带`/` 的字符串，比如 URL
    ```
    :?URL
    ```

<h2 id="54afc9723e7bdaa4cf548df28b7e9541"></h2>


### 文件夹搜索 vimgrep

```vim
vimgrep /pattern/gj path
```

- 参数:
    - g: 一行中出现多次，只显示一次
    - j: 只列出匹配的行
- path
    - `./*.c`  当前文件夹下 c 文件中查找
    - `**/*.*`  包括子文件夹下 所有文件
- 搜索完毕 copen 或 cw 查看搜索列表



<h2 id="4b0c82f3072a7a2d205d934ca7413367"></h2>


###  多行 行首插入字符

1. 光标置与第一行行首, ctrl-v 进入  VISUAL BLOCK
2. 向下移动光标 选中所有行
3. shift i 进入多行插入模式， 编辑 , esc 
4. 等 1秒钟， 修改完成
- note: v 以字元为单位，V 以行为单位，ctrl-v 以列为单位


<h2 id="facc78c7266b3fe0364882da91e214b8"></h2>


###  多行 行尾插入字符

- 和上边的 多行行首插入 类似，只是 第三步进行修改
1. Press $ to extend the visual block to the end of each line.
2. Press A ，进入行尾编辑
3. 编辑 , esc


<h2 id="11cc6cd769420b9372c1b33a98a38d5e"></h2>


### duplicated column, paste next to it

```vim
:%s/.*/& &/
```

- `.*` means everything
- & copies everything that was matched  `& &` means whole line twice, separate by a space



<h2 id="67c5f9b419ed15a16a0cb4786a4a6552"></h2>


###  Remove unwanted empty lines

- use `v` to select the range of lines you want to work on 
- useing either of the following command to delete all empty lines:
    ```vim
    :g/^$/d
    :v/./d
    ```

<h2 id="fe7fb0107de52ad2a0bca9917a32301a"></h2>


###  make multiple line word into java string

```vim
# record
qq0I"escA",esc0jq   // ( 0I 0j 校正位置 )
@q
8@@
```

<h2 id="87b0406cc2b93c7df74c3cfc9b2e690b"></h2>


###  复制/移动 行

```vim
:6t.  // 复制第6行到当前位置
:6,8t. // 复制6-8行到当前位置
:6m.   // 移动 第6行
;6,8m. // 移动 6-8行
```


### Advance g

- gj/gk/... g$,g0 
    - move on a visual line, not vim line
- gq  (useful when you work with markdown )
    - format whole line in sperate lines
- gu, gU, g~
    - cap, uncap 
- gf
    - open file (filename where your cursor on )
- gv
    - go back to you last visual selection
- gJ
    - conjoin lines, but without leaving space between them ( unlike J )



<h2 id="fc1f1e8c6d70d860957c66f735e60e2b"></h2>


# grok VIM

- The "Zen" of **vi** is that you're speaking a language. 
    - `yy`
        - The initial *y* is a verb. 
        - The statement *yy* is a synonym for *y_*. The y is doubled up to make it easier to type.
        - the verb can take any movements as their "subject." 
- vi has 26 "marks" and 26 "registers."  ( lower case characters)
    - `ma` sets the 'a' mark to the current location
    - use `'a`  (single quote) to jump the beginning of the **LINE** has 'a' mark
    - use `` `a`` (backquote)  to jump the precise location of the 'a' mark.
        - > markdown tips:  use a space infront and surrounded by doulbe backquote to display single backquote.
        - > similarly, use space infront and surrounded by single backquote to display double backquote.
    - more special mark jumping
        - ` `` ` , `''` , to jump back to where jumped from
        - `` `0`` , jump to position in last file edited (when exited Vim)
        - `` `1`` , like `` `0`` ,  but the previous file (also `` `2`` etc)
    - Because these are "movements" they can also be used as subjects for other "statements."
        - ``d`a`` to delete the content from current location to 'a' mark
- So, one way to cut an arbitrary selection of text would be to drop a mark.
    - this is one way to cut or copy text. However, it is only one of many.
    - Frequently we can more succinctly describe the range of text without moving our cursor around and dropping a mark.
    - For example if I'm in a paragraph of text I can use { and } movements to the beginning or end of the paragraph respectively.
    - So, to move a paragraph of text I cut it using `{ d}` (3 keystrokes).
- Searching forwards or backwards are movements in vi. Thus they can also be used as "subjects" in our "statements." 
    - `d/abc` , delete the content from current location to the next matched `abc`
    - `y?abc` , yark the content from current locationthe most recent (previous) matched `abd`

----

- In addition to "verbs" and "subjects" vi also has "objects".
    - So far I've only described the use of the anonymous register. 
    - However, I can use any of the 26 "named" registers by *prefixing* the "object" reference with " (the double quote modifier).
    - Thus if I use `"add` I'm cutting the current line into the 'a' register.
    - To paste from a register I simply prefix the paste with the same modifier sequence: `"ap`  pastes a copy of the 'a' register's contents.
    - This notion of "prefixes" is something like "adjectives" / "adverbs".
    - Most commands (verbs) and movement (verbs or objects, depending on context) can also take numeric prefixes.
        - Thus `3J` means "join the next three lines" 
        - and `d5}` means "delete from the current line through the end of the fifth paragraph down from here."
- **This is all intermediate level vi.**

---

<h2 id="a5787082a16f14e8db2acbf78497ee99"></h2>


## A sampling of more advanced tricks:

- There are a number of `:` commands, most notably the `:% s/foo/bar/g` global substitution technique
    - `:` commands normally operate over lines of text. The whole : set of commands was historically inherited by vi's previous incarnations ,ed and ex, very elder.
    - So the syntax of most `:` commands includes an address or range of addresses (line number) followed by a command.
    - `:127,215 s/foo/bar` to change the first occurrence of "foo" into "bar" on each line between 127 and 215
    - One could also use some abbreviations such as `.` or `$` for current and last line respectively
    - One could also use relative prefixes `+` and `-` to refer to offsets after or before the curent line, 
    - Thus, `:.,$j` meaning "from the current line to the last line, join them all into one line".
    - `:%` is synonymous with `:1,$` (all the lines).
- The `:...g` and `:...v` commands are incredibly powerful.
    - `:...g` is a prefix for "globally" applying a subsequent command to current line which match a pattern (regular expression) 
    - while `:...v` applies such a command to current line which do NOT match the given pattern ("v" from "conVerse").
    - Thus `:.,+21g/foo/d` means "delete any lines containing the string "foo" from the current one through the next 21 lines"
    - while `:.,$v/bar/d` means "from here to the end of the file, delete any lines which DON'T contain the string "bar."
    - > It's interesting that the common Unix command **grep** is named after this way. The command `:g/re/p` was the way how to "globally" "print" lines containing a "regular expression" (re). 
    - Note that `:% g/.../d` or (its reVerse/conVerse counterpart: `:% v/.../d` are the most common usage patterns.
        - `:g/.../d` 同样效果？
    - In `:` command,  we can use `m` to move lines around, and `j` to join lines. 
        - if you have a list and you want to separate all the stuff matching without deleting them, (or conversely NOT matching some pattern) 
            - then you can use something like: `:% g/foo/m$ ...` and all the "foo" lines will have been moved to the end of the file.
            - **Note the other tip about using the end of your file as a scratch space**
        - `:% g/Another/-1j` , for every matching line, go up one line and join them.
    - Almost needless to mention you can use our old friend s (substitute) with the g and v.
        - `:% g/foo/s/bar/zzz/g`   for every line containing "foo" substitute all "bar" with "zzz." 
- The `:` addresses can also refer to marks. 
    - Thus you can use: `:'a,'bg/foo/j` to join any line containing the string *foo* to its subsequent line, if it lies between the lines between the 'a' and 'b' marks. 
- Another very useful vi or ex command is `:r` to read in the contents of another file. 
    - Thus: :r foo inserts the contents of the file named "foo" at the current line.
    - More powerful is the `:r!` command.  This reads the results of a command , and insert it at the current line.
- Even more powerful are the `!` (bang) and `:... !` (ex bang) commands.
    - These also execute external commands and read the results into the current text.
    - However, they also filter selections of **our text** through the command! 
        - This we can sort all the lines in our file using `1G!Gsort`. This is equivalent to the ex variant `:1,$!sort`.
        - > Writers often use ! with the Unix fmt or fold utilities for reformating or "word wrapping" selections of text. 
        - A very common macro is `{!}fmt` (reformat the current paragraph). 
- Another useful ex command is `:so` (short for `:source`). 
    - This reads the contents of a file as *a series of commands*. 
- The @ command is probably the most obscure vi command. 
    - @ executes the contents of a register as if it were a *vi* or *ex* command.


---




