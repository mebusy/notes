
# Something About Arch Linux + i3-wm

- pacman upate: 
    - `sudo pacman -Syyu`
- basic dev tools
    - `sudo pacman -S base-devel`

## change mirror

https://archlinux.org/mirrorlist/


## Chinese Support


### Show Chinese in Brower, Terminal, etc.

```bash
sudo pacman -S noto-fonts-cjk wqy-zenhei adobe-source-han-sans-otc-fonts
# not necessary ?
sudo fc-cache -fv

# better suport unicode that i3-sensible-terminal
sudo pacman -S alacritty
```

for i3-wm:

```bash
vi ~/.config/i3/config
```

1. find the `font` line, comment `monospace`, and uncomment `deJavU`
2. find the `terminal` line, replace `i3-sensible-terminal` with `alacritty`


restart i3:  `Mod + Shift + R`


### Chinese Input

```bash
sudo pacman -S fcitx fcitx-googlepinyin fcitx-configtool
```

run `fcitx-configtool` to config


## IF ONLY ~/.bash_profile  not sourced in i3-terminal

In Arch Linux, when using i3 with a terminal (like i3-terminal), the ~/.bash_profile file may not be sourced because, by default, it only gets loaded for login shells, not interactive non-login shells.


To Configure i3 to Launch a Login Shell in i3-terminal:

```bash
vi ~/.config/i3/config
```

Find the terminal command, add `-e bash -l`, e.g. for `alacritty`

```bash
bindsym $mod+Return exec "alacritty -e bash -l"
```

## Other Config

```conf
# workspace
# use xprop to identify app's class(2nd value), e.g. chromium's class is Chromium
# now launch chromium in workspace 2
assign [class="Chromium"] $ws2

# use font for workspace icon: https://github.com/FortAwesome/Font-Awesome, download the web version, find the .ttf font file
# cd fontawesome-free-6.6.0-web/webfonts/
# mkdir -p ~/.fonts
# cp fa-v4compatibility.ttf ~/.fonts/
# select your icon from: https://fontawesome.com/v4/cheatsheet/, and copy to $ws identifier

# customize shortcut key
bindsym $mod+Shift+x exec i3lock

# lanuch program when login
exec chromium
# lanuch program everytime i3 restart
# exec_always chromium

# set backgroud
# exec_always feh --bg-scale <pic-path>

# monitor config
# config, then save to a file, copy the content
# sudo pacman -S arandr
exec_always xrandr --output Virtual1 --primary --mode 1440x900 --pos 0x0 --rotate normal --output Virtual2 --off --output Virtual3 --off --output Virtual4 --off --output Virtual5 --off --output Virtual6 --off --output Virtual7 --off --output Virtual8 --off
```

