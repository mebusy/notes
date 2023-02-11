[](...menustart)

- [VIM](#d53cfc4bdeb96eaee47dd710b3c2ed21)
    - [Plugin Installation](#431e27fdb6a4c378a592fb761c7e5519)
    - [YouCompleteMe Configuaration Tips](#72aef9272e534c2840a7b9f5e4899694)
    - [C-Family \[ycm_extra_conf.py\]](#e70cbc3e7d4a60990580571997e5e3a5)
        - [YCMD Troubleshoot](#fab255294e7b3b58a06c83405029a7c0)
    - [Markdown](#2182a74bab7188d959e795d9301e87ff)
    - [viminspect](#05792acc8846850d5650256c2f89d097)
        - [debug nodejs](#a76b761a3f63c8a3aca6fa66777741fa)
    - [vim Mark](#ac4aee7e186902860d64dcf2a6065905)
    - [VIM tips](#a1c1a23da31214c88d29928e14c64ef0)
        - [文件夹内容替换 args/argdo](#d97b62cc38ac0f48ee2ef1675eceb014)
        - [搜索 (lookahead, lookbehind, contains `/`)](#0b4ec6e4487065d67922bc151a3fe175)
        - [文件夹搜索 vimgrep](#54afc9723e7bdaa4cf548df28b7e9541)
        - [多行 行首插入字符](#4b0c82f3072a7a2d205d934ca7413367)
        - [多行 行尾插入字符](#facc78c7266b3fe0364882da91e214b8)
        - [duplicate column, then paste it next to it](#4bfa29dd5fb09c6b1e51c19cadea0e12)
        - [Remove unwanted empty lines](#67c5f9b419ed15a16a0cb4786a4a6552)
        - [make multiple line word into java string](#fe7fb0107de52ad2a0bca9917a32301a)
        - [复制/移动 行](#87b0406cc2b93c7df74c3cfc9b2e690b)
        - [Advance g](#b492b625b61dc9e4718c98561d7b0296)
- [grok VIM](#fc1f1e8c6d70d860957c66f735e60e2b)
    - [A sampling of more advanced tricks:](#a5787082a16f14e8db2acbf78497ee99)
- [VIM Regular Expressions](#97786adcbde368256fe1cb51b6339c7e)
    - [Why magic mode ?](#63c1835cfbf1719dd2ddb81b3f922a29)
    - [Compare with Perl patterns](#20cccd93ecd64a6cdd4d70b646c9803c)

[](...menuend)


<h2 id="d53cfc4bdeb96eaee47dd710b3c2ed21"></h2>

# VIM 

<h2 id="431e27fdb6a4c378a592fb761c7e5519"></h2>

## Plugin Installation


- Install `vundle` first
    ```bash
    git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
    ```

- Configure your .vimrc to add support for vundle
    ```vim
    filetype off
    set rtp+=~/.vim/bundle/vundle/
    call vundle#rc()
    ```

- Configure plugins
    - Bundles are in three categories, the more commonly used is the 2nd one
        1. For repos under the Github user vim-scripts , just write the repo name
        2. For repos under other users on Github, you need to write "username/repo-name"
        3. For plugins not on Github, you need to write out the full path of git
    - Add the plugins that need to be installed to ~/.vimrc
        ```vim
        " user Vundle to manage Bundles
        Bundle 'gmarik/vundle'
         
        " Define bundles via Github repos
        Bundle 'christoomey/vim-run-interactive'
        Bundle 'croaky/vim-colors-github'
        Bundle "Valloric/YouCompleteMe"
        ...
        ```

- Install the plugins
    - Open vim, run `:BundleInstall` or directly run in the shell
        ```bash
        vim +BundleInstall +qall
        ```
    - To update plugins :
        ```bash
        vim +PluginUpdate
        ```

<h2 id="72aef9272e534c2840a7b9f5e4899694"></h2>

## YouCompleteMe Configuaration Tips

- for C family support:  `./install.py --clang-completer`
    - optional `--system-libclang` Use the libclang that comes with mac, but generally the version is relatively old and there will be problems
- C# support: install Mono and add `--cs-completer` 
- Go support: install Go and add `--go-completer` 
- JavaScript and TypeScript support: install nodejs and add `--ts-completer` 
    - NOTE: TSServer need a `.tern-project`
        ```json
        {
          "plugins": {
            "node": {},
            "es_modules": {}
          },
          "libs": [
            "ecma5",
            "ecma6"
          ],
          "ecmaVersion": 6
        }
        ```
    - NOTE: TSServer relies on the  [jsconfig.json](https://code.visualstudio.com/docs/languages/jsconfig) for javascript and  [tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) for typescript  to analyze your project. Ensure the file exists at the root of your project.
        - **PS**: ycm will look up `jsconfig.json` up to the top parent directory, and think the final directory as `root` and parse all .js files under it, it may break ycm ... So do **NOT** put a `jsconfig.json` file outside of your project.
    - Example: To get diagnostics in JavaScript, set the checkJs option to true in your jsconfig.json file:
        ```json
        {
            "compilerOptions": {
                "checkJs": true
            }
        }
        ```
- Rust support: install Rust and add `--rust-completer`
    - put `~/.cargo/bin`   in you $PATH ?
        ```bash
        # rust
        export PATH=$HOME/.cargo/bin:$PATH
        ```
- Java support: install JDK8 (version 8 required) and add `--java-completer` 
- for common using
    ```bash
    ./install.py --clang-completer --cs-completer  --go-completer \
                    --ts-completer --java-completer --rust-completer
    ```
    - or
    ```bash
    ./install.py --all
    ```
    - for Ubuntu, `sudo apt install build-essential` is needed


<h2 id="e70cbc3e7d4a60990580571997e5e3a5"></h2>

## C-Family [ycm_extra_conf.py]

- YCM will look up the .ycm_extra_conf.py configuration file layer by layer
- official example: https://github.com/ycm-core/ycmd/blob/master/.ycm_extra_conf.py
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


<h2 id="fab255294e7b3b58a06c83405029a7c0"></h2>

### YCMD Troubleshoot

- Tagbar requires ctags to be installed
    - `brew install ctags`
    - for golang, you also need gotags `brew install gotags`
- python syntax check
    - `pip install flake8`
- vim diagnosis
    - `:YcmDebugInfo`
- vim check logs
    - `YcmToggleLogs`
- output log to file
    - running vim with the -V[N] option will do a pretty hefty runtime log, here N is the debug level.
        ```bash
        vim -V9myVim.log
        ```
    - would create a log of debug level 9 in the current directory with the filename myVim.log
- pyenv : ERROR: found static Python library … but a dynamic one is required.
    ```bash
    $ export PYTHON_CONFIGURE_OPTS="--enable-framework"
    $ pyenv install 3.10.3
    ```


<h2 id="2182a74bab7188d959e795d9301e87ff"></h2>

## Markdown 

- chrome plugin  :  [Markdown Preview Plus](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl)
- visit `chrome://extensions/` ， Check  “Allow access to file URLs” in the settings page


<h2 id="05792acc8846850d5650256c2f89d097"></h2>

## viminspect

- see `.vimspector.json` examples 
    - in ` ~/.vim/bundle/vimspector/support/test/`
    - or [official page](https://puremourning.github.io/vimspector/configuration.html#predefined-variables)


<h2 id="a76b761a3f63c8a3aca6fa66777741fa"></h2>

### debug nodejs

- launch app in inspect mode
    ```bash
    node --inspect app.js
    
    # if you're using nodemon
    nodemon --config nodemon.json --async-stack-traces --exec 'node --inspect app.js'
    ```




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


<h2 id="4bfa29dd5fb09c6b1e51c19cadea0e12"></h2>

### duplicate column, then paste it next to it

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
qa0I"escA",esc0jq   // ( 0I 0j to correct position )
@a
8@@
```

<h2 id="87b0406cc2b93c7df74c3cfc9b2e690b"></h2>

###  复制/移动 行

```vim
:6t.  // 复制第6行 到当前位置
:6,8t. // 复制6-8行 到当前位置
:6m.   // 移动 第6行 到当前位置
;6,8m. // 移动 6-8行 到当前位置
```


<h2 id="b492b625b61dc9e4718c98561d7b0296"></h2>

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
        - > **markdown tips**:  use a space infront and surrounded by doulbe backquote to display single backquote.
        - > similarly, use space infront and surrounded by single backquote to display double backquote.  ` ``a`
    - more special mark jumping
        - ` `` ` , `''` , to **jump back to where jumped from**
        - `` `0`` , jump to position in last file edited (when exited Vim)
        - `` `1`` , like `` `0`` ,  but the previous file (also `` `2`` etc)
    - Because these are "movements" they can also be used as subjects for other "statements."
        - ``d`a`` to delete the content from current location to 'a' mark
- So, one way to cut an arbitrary selection of text would be to drop a mark.
    - this is one way to cut or copy text. However, it is only one of many.
    - Frequently we can more succinctly describe the range of text without moving our cursor around and dropping a mark.
    - For example if I'm in a paragraph of text I can use { and } movements to the beginning or end of the paragraph respectively.
    - So, to move a paragraph of text I cut it using `{ d}` (4 keystrokes).
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

<h2 id="97786adcbde368256fe1cb51b6339c7e"></h2>

# VIM Regular Expressions

<h2 id="63c1835cfbf1719dd2ddb81b3f922a29"></h2>

## Why magic mode ?

- Common editors can generally specify whether to use a normal search or a regular expression search. 
- But the vim use a mixed search, magic (\m) mode
    - For example, the `/foo(1)` command, which most people use to find the string `foo(1)`.
    - Therefore, vim stipulates that the metacharacters of regular expressions must be escaped with backslashes. As in the above example, if you really want to use regular expressions, you should write `/foo\(1\)`
    - However, it is inconvenient to add backslashes to extremely common metacharacters like `.` `*`. 
- To solve this problem, vim sets the magic:
    - magic (\m): all metacharacters except `* . ^ $ []` need backslashing
- But if you are strongly prefer normal regular expression, you can use very magic mode (\v), it is **Perl-regex-compatible**
    - but you can NOT set it as default, it will lead to plugin's compatibility problems
- There are 2 more modes you can use
    mode | metacharacters need backslashing | activated by  | comments
    --- | --- | ---  | ---
    Magic | all except `* . ^ $ []` | `\m` | **default** modifier
    Very Magic | N/A, Perl-regex-compatible | `\v`  | 
    No Magic | all except `^ $` | `\M` |
    Very No Maigc | all |  `\V` |  normal text search


<h2 id="20cccd93ecd64a6cdd4d70b646c9803c"></h2>

## Compare with Perl patterns

Capability                     |  in Vimspeak    |  in Perlspeak
------------------------------ | --------------- | ------------------
force case insensitivity       |  `\c`             |  `(?i)`
force case sensitivity         |  `\C`             |  `(?-i)`
backref-less grouping          |  `\%(atom\)`      |  `(?:atom)`
conservative quantifiers       |  `\{-n,m}`        |  `*?, +?, ??, {}?`
0-width match                  |  `atom\@=`        |  `(?=atom)`
0-width non-match              |  `atom\@!`        |  `(?!atom)`
0-width preceding match        |  `atom\@<=`       |  `(?<=atom)`
0-width preceding non-match    |  `atom\@<!`       |  `(?<!atom)`
match without retry            |  `atom\@>`        |  `(?>atom)`



- Capture group notation is slightly different from perl, use **`@`** instead of `(?`
- The location of the pattern for capturing groups in vim differs from perl
    - For example, to find *bar* immediately after *foo*, 
        - perl writes the pattern *foo* inside the lookaround (`?<=`) brackets, `(?<=foo)bar`
    - while vim writes the pattern before the lookaround metacharacter , `(foo)@<=bar` 
- vim matches the beginning and end of words using `<` , `>` , 
    - `\b` is used to match `<BS>`



# VIM Script

- [5 minutes vim script](http://andrewscala.com/vimscript/)
- [VIM9 用户手册](https://vimcdoc.sourceforge.net/doc/usr_41.html)

