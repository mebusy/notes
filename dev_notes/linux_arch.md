
# Something About Arch Linux + i3-wm

## change mirror

https://archlinux.org/mirrorlist/


## Chinese Support


### Show Chinese in Brower, Terminal, etc.

```bash
sudo pacman -S noto-fonts-cjk wqy-zenhei adobe-source-han-sans-otc-fonts

# not necessary
sudo fc-cache -fv
```

for i3-wm:

```bash
vi ~/.config/i3/config
```

replace the `font` line with `font pango:Noto Sans CJK SC 10`


restart i3:  `Mod + Shift + R`


### Chinese Input

```bash
sudo pacman -S fcitx fcitx-googlepinyin fcitx-configtool
```

run `fcitx-configtool` to config


## ~/.bash_profile  not sourced in i3-terminal

In Arch Linux, when using i3 with a terminal (like i3-terminal), the ~/.bash_profile file may not be sourced because, by default, it only gets loaded for login shells, not interactive non-login shells.


To Configure i3 to Launch a Login Shell in i3-terminal:

```bash
vi ~/.config/i3/config
```

Find the terminal command, replace with

```bash
bindsym $mod+Return exec i3-sensible-terminal -e "bash -l"
```



