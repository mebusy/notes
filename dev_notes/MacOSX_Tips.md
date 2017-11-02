...menustart

 - [MacOSX](#5dad7f6f2d7af4cc1196128ec251af8a)
	 - [vim 设置](#c585405730fcd92667781471df41f4fb)
	 - [设置 目录访问权限(禁止别的用户浏览)](#d1b5bbfe80897599d07253429886f700)
	 - [sidebar 丢失](#2921868f08055ef268441139489a6130)
	 - [openofficer error](#1c305ad1fad7ba14dd448d08a73f3ab8)
	 - [Useful Commands](#ec69fb46be4996fda376dcb4054c528b)
		 - [xxd](#25c04b9b782789c092a38c06cc87632a)
		 - [mdfind](#0968ea4dc36ecbcdc0810a8ca0f674c8)
		 - [alias](#724874d1be77f450a09b305fc1534afb)
		 - [man ascii  字符表](#726e07a4bf9abb9ebcdce89b16eb7807)
		 - [cal 日历](#e1bde9f80b42328020cb6b0a4c7d26ab)
		 - [find files to rm](#a21d96fb754b9ce8455858e14ed36571)
		 - [in terminal, show git branch in path](#394dd2658e932bd638e3017ac1a98c39)
	 - [TODO](#b7b1e314614cf326c6e2b6eba1540682)

...menuend


<h2 id="5dad7f6f2d7af4cc1196128ec251af8a"></h2>

# MacOSX 

<h2 id="c585405730fcd92667781471df41f4fb"></h2>

## vim 设置

 - `cp /usr/share/vim/vimrc ~/.vimrc`
 - `编辑 ~/.vimrc`

```bash
syntax enable
syntax on

set number
set relativenumber

set ts=4  # table 4 bytes
```

<h2 id="d1b5bbfe80897599d07253429886f700"></h2>

## 设置 目录访问权限(禁止别的用户浏览)

```
sudo chmod 700 文件夹
```


rwx           |         rwx          |         rwx
--- | --- | ---
文件主权限  |    组用户权限      |        其他用户权限

700 ＝  111 000 000


<h2 id="2921868f08055ef268441139489a6130"></h2>

## sidebar 丢失

OPTION/Alt+COMMAND+S

<h2 id="1c305ad1fad7ba14dd448d08a73f3ab8"></h2>

## openofficer error

```bash
rm -rf ~/Library/Saved Application State/org.openoffice.script.savedState
```

<h2 id="ec69fb46be4996fda376dcb4054c528b"></h2>

## Useful Commands

<h2 id="25c04b9b782789c092a38c06cc87632a"></h2>

### xxd 

 - `xxd  <filename>`   以16进制显示文件内容
 - `xxd -i <filename>`   转成c数组

```
unsigned char note_txt[] = {
  0x0a, 0x0a, 0x0a, 0x35, 0x30, 0x30, 0x30, 0x20, 0x2b, 0x20, 0x37, 0x35,
  0x30, 0x20, 0x70, 0x68, 0x6f, 0x74, 0x6f, 0x0a, 0x31, 0x32, 0x30, 0x20,
  0x20, 0xe5, 0x96, 0x9c, 0xe7, 0xb3, 0x96, 0xe9, 0xa2, 0x84, 0xe4, 0xbb,
  0x98, 0x0a, 0x35, 0x30, 0x30, 0x30, 0x20, 0xe5, 0xb0, 0x8f, 0xe5, 0x8d,
  0x97, 0xe5, 0x9b, 0xbd, 0x20, 0xe5, 0xae, 0x9a, 0xe9, 0x87, 0x91, 0x0a,
  0x0a
};
unsigned int note_txt_len = 61;
```

<h2 id="0968ea4dc36ecbcdc0810a8ca0f674c8"></h2>

### mdfind

 - `mdfind -name <xxxxx>`   快速查找文件

<h2 id="724874d1be77f450a09b305fc1534afb"></h2>

### alias 

```bash
alias blender='/Volumes/WORK/Tools/Blender/blender.app/Contents/MacOS/blender'
```

 - 可放入 .profile  中
 - alias 
    - 查看所有别名

<h2 id="726e07a4bf9abb9ebcdce89b16eb7807"></h2>

### man ascii  字符表

```
 The hexadecimal set:

 00 nul   01 soh   02 stx   03 etx   04 eot   05 enq   06 ack   07 bel
 08 bs    09 ht    0a nl    0b vt    0c np    0d cr    0e so    0f si
 ...
```

<h2 id="e1bde9f80b42328020cb6b0a4c7d26ab"></h2>

### cal 日历

 - `cal` 当月
 - `cal -y` 当年
 - `-j` 参数, day 显示为 当年的第几天


<h2 id="a21d96fb754b9ce8455858e14ed36571"></h2>

### find files to rm 

```
find . -name '.DS_Store' -path '*/.*' | xargs  rm
```

<h2 id="394dd2658e932bd638e3017ac1a98c39"></h2>

### in terminal, show git branch in path

```
# Git branch in prompt.
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
```

### find all json file , and remove all `\r` 

```
ls *.json | xargs -I {}  sh -c  "cat {} | tr -d '\r' > {}2 && mv {}2 {} "
or
ls *.json | xargs -I {}  sh -c  " tr -d '\r' < {}  > {}2 && mv {}2 {} "
```
 
  - `{}` :  handle every file
  - `sh -c`  : directly use `{}` in redirection `>` not works, put them in a shell command
  - you can not do that by sed  , remember  sed delimits on `\n` newlines - they are always removed on input and reinserted on output.   you may need `-z` mode 
 


<h2 id="b7b1e314614cf326c6e2b6eba1540682"></h2>

## TODO

