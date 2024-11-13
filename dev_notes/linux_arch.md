
# Something About Arch Linux + i3-wm

- pacman upate: 
    - `sudo pacman -Syyu`


## Install Arch Linux

Create USB bootable disk: https://wiki.archlinux.org/title/USB_flash_installation_medium#In_macOS_2

```bash
# before install, if you stuck on mirror choosing ...
systemctl mask reflector.service
```

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

### Alacritty setting

```bash
# vi ./config/alacritty/alacritty.toml

# https://alacritty.org/config-alacritty.html#s12
# config change will affect UI right now
[font]
size=8

[window]
opacity=0.9
```

```bash
# picom
sudo pacman -S picom

# vi ~/.config/i3/config
exec --no-startup-id picom -f --xrender-sync-fence
```


### Chinese Input

```bash
sudo pacman -S fcitx fcitx-googlepinyin fcitx-configtool
```

```bash
# vi ~/.xprofile
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx

fcitx &

# reboot
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

## config i3-wm

https://i3wm.org/docs/userguide.html

```conf
# workspace
# use xprop + mouse click on app window 
#   to identify app's class(2nd value), e.g. chromium's class is Chromium
# now launch chromium in workspace 2
assign [class="Chromium"] $ws2
# lanuch program when login
exec chromium
# lanuch program everytime i3 restart
# exec_always chromium


# use font for workspace icon: https://github.com/FortAwesome/Font-Awesome, download the web version, find the .ttf font file
# we use 4.x version: 
#   wget https://raw.githubusercontent.com/FortAwesome/Font-Awesome/refs/heads/4.x/fonts/fontawesome-webfont.ttf
# sudo mv fontawesome-webfont.ttf /usr/share/fonts/
# sudo fc-cache -fv
#
# select your icon from: https://fontawesome.com/v4/cheatsheet/, and copy to $ws identifier

# customize shortcut key, like MacOS
bindsym $mod+Ctrl+q exec i3lock --color=000000


# set wallpaper
# sudo pacman -S feh
# wget blob:https://github.com/6848b5c7-96e6-4fc4-bbcd-c5adab933e92
# mkdir ~/.wallpapers
exec_always feh --bg-scale ~/.wallpapers/<pic-name>

# monitor config
# config, then save to a file, copy the content
# sudo pacman -S arandr
exec_always xrandr --output Virtual1 --primary --mode 1440x900 --pos 0x0 --rotate normal --output Virtual2 --off --output Virtual3 --off --output Virtual4 --off --output Virtual5 --off --output Virtual6 --off --output Virtual7 --off --output Virtual8 --off

# ~title font & bar font~ NOT necessary
# https://github.com/supermarin/YosemiteSanFranciscoFont
# clean up the files, leave 4 .ttf files
# sudo mv YosemiteSanFranciscoFont-master /usr/share/fonts/
# sudo fc-cache -fv
# $ fc-list | grep "San Francisco"
# ... System San Francisco Display Ultralight.ttf: SFNS Display:style=UltraLight
font pango:System San Francisco Display 14

# gkt font
# sudo pacman -S lxappearance
# run lxappearance, change current font size, then apply. 
# 2 files ~/.gtkrc-2.0 and  ~/.config/gtk-3.0/settings.ini will be generated
# manually change the font name to "System San Francisco Display 14"
# Optional: use infinality to improve font rendering

# file explorer
# sudo pacman -S thunar

# gtk-theme
# sudo pacman -S arc-gtk-theme
# use lxappearance to change theme

# replace d-menu
# $ sudo pacman -S rofi
# $ rofi -show run
# in i3 config file, replace dmenu with rofi (rofi already in config file, just uncomment it)

# sould control
# sudo pacman -S pavucontrol
```

## ssh to archlinux sever and run gtk program

in archlinux server,  

```bash
vi ~/.bash_profile

# add the following line
[ -n "$SSH_CONNECTION" ] && [ -z "$DISPLAY" ] && export DISPLAY=<your-ip:disp_num>
```


## mbpfan

```bash
makepkg -si

systemctl enable mbpfan
systemctl start mbpfan
```

## HiDPI

https://wiki.archlinux.org/title/HiDPI


1. xrandr
    - ~/.config/i3/config
    ```bash
    # default dpi is 96, change to 192
    exec_always xrandr --dpi 192
    ```
2. terminal
    - e.g. alacritty: chang font size *=2
3. gtk app
    - **PS: not necessary !!!!**
    - ~/.bash_profile
    ```bash
    export GDK_SCALE=2
    ```
4. more apps ...

## NVIDIA GPU

- pre-installed driver may conflict with nvidia driver
- check the wiki for more info:
    - https://wiki.archlinux.org/title/NVIDIA

## paru:  packed AUR help

1. install rust
    - sudo pacman -S rustup
    - rustup default stable
2. install paru
    - https://github.com/Morganamilo/paru


Now you can use paru to install AUR packages, e.g. envycontrol (hybrid GPU control)

```bash
paru envycontrol
```

## i3blocks

- `sudo pacman -S acpi i3blocks`   // acpi for battery info
- `paru mpstat`  // for cpu info
- `paru amixer`  // for volume control


## Laptop Battery Life

check `auto-cpufreq` on github


## Dev Tools

- tk (for python)
- rustup (rustup default stable)

## headers

- `sudo pacman -S linux-headers`
- lts headers: `sudo pacman -S linux-lts-headers`


## Resize Partitions

1. boot from usb installer
2. `parted /dev/sda`
3. (parted) print
4. (parted) resizepart <your-partition number to resize>
5. (parted) <provide a END>
6. (parted) quit
7. `resize2fs /dev/sda2`


