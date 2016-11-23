# MacOSX 

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

## 设置 目录访问权限(禁止别的用户浏览)

```
sudo chmod 700 文件夹
```


rwx           |         rwx          |         rwx
--- | --- | ---
文件主权限  |    组用户权限      |        其他用户权限

700 ＝  111 000 000


## sidebar 丢失

OPTION/Alt+COMMAND+S

## openofficer error

```bash
rm -rf ~/Library/Saved Application State/org.openoffice.script.savedState
```

## Useful Commands

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

### mdfind

 - `mdfind -name <xxxxx>`   快速查找文件

### alias 

```bash
alias blender='/Volumes/WORK/Tools/Blender/blender.app/Contents/MacOS/blender'
```

 - 可放入 .profile  中
 - alias 
    - 查看所有别名

### man ascii  字符表

```
 The hexadecimal set:

 00 nul   01 soh   02 stx   03 etx   04 eot   05 enq   06 ack   07 bel
 08 bs    09 ht    0a nl    0b vt    0c np    0d cr    0e so    0f si
 ...
```

### cal 日历

 - `cal` 当月
 - `cal -y` 当年
 - `-j` 参数, day 显示为 当年的第几天


## TODO

