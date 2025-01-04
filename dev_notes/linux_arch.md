[](...menustart)

- [Something About Arch Linux + i3-wm](#2b01560d0d559955f35c6f0b3f0aabee)
    - [Install Arch Linux](#a193e259b8223762b6d0e67651401dd0)
    - [change mirror](#aa1b405e688e650e0d8820dc650d601b)
    - [Chinese Support](#70df1833cae594ee437d74d5fdf920c8)
        - [Show Chinese in Brower, Terminal, etc.](#919acbd697cc37e840ef92a6bb862d80)
        - [Alacritty setting](#3f16b3dedd1de377102fa4d06f90e0e8)
        - [Chinese Input](#f97631860fcc7681892ed91e6b37b497)
    - [IF ONLY ~/.bash_profile  not sourced in i3-terminal](#fc756afc9ffc982cea38445ec61fe0d1)
    - [config i3-wm](#180e2c5ed883b898d5e40cb0022c1a98)
    - [ssh to archlinux sever and run gtk program](#0250b35cf47190e9d755c9b49f5b058a)
    - [mbpfan](#17a619241bc8f98a839dfbc931009f8b)
    - [HiDPI](#7fe62e51915c286c0cf4c72ab5307033)
    - [NVIDIA GPU](#1f14b1b0e6e7f15adc85beb49514c09e)
    - [paru:  packed AUR help](#7e150414eb9bd14e4769252dda140335)
    - [i3blocks](#d6b8ea18f9137882156a9d41fd989cd6)
    - [Laptop Battery Life](#b3fa013ae44a3d42e6cc8298c03951fc)
    - [Dev Tools](#f73a3dfcf8bbecf604228b1b8f4bbb15)
    - [headers](#4340fd73e75df7a9d9e45902a59ba3a4)
    - [Resize Partitions](#55b8c4a0eb572538a44c6c44511b00b3)

[](...menuend)


<h2 id="2b01560d0d559955f35c6f0b3f0aabee"></h2>

# Something About Arch Linux + i3-wm

- pacman upate: 
    - `sudo pacman -Syyu`


<h2 id="a193e259b8223762b6d0e67651401dd0"></h2>

## Install Arch Linux

Create USB bootable disk: https://wiki.archlinux.org/title/USB_flash_installation_medium#In_macOS_2

```bash
# before install, if you stuck on mirror choosing ...
systemctl mask reflector.service
```

<h2 id="aa1b405e688e650e0d8820dc650d601b"></h2>

## change mirror

https://archlinux.org/mirrorlist/


<h2 id="70df1833cae594ee437d74d5fdf920c8"></h2>

## Chinese Support


<h2 id="919acbd697cc37e840ef92a6bb862d80"></h2>

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

<h2 id="3f16b3dedd1de377102fa4d06f90e0e8"></h2>

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


<h2 id="f97631860fcc7681892ed91e6b37b497"></h2>

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


<h2 id="fc756afc9ffc982cea38445ec61fe0d1"></h2>

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

<h2 id="180e2c5ed883b898d5e40cb0022c1a98"></h2>

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

<h2 id="0250b35cf47190e9d755c9b49f5b058a"></h2>

## ssh to archlinux sever and run gtk program

in archlinux server,  

```bash
vi ~/.bash_profile

# add the following line
[ -n "$SSH_CONNECTION" ] && [ -z "$DISPLAY" ] && export DISPLAY=<your-ip:disp_num>
```


<h2 id="17a619241bc8f98a839dfbc931009f8b"></h2>

## mbpfan

```bash
makepkg -si

systemctl enable mbpfan
systemctl start mbpfan
```

<h2 id="7fe62e51915c286c0cf4c72ab5307033"></h2>

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

<h2 id="1f14b1b0e6e7f15adc85beb49514c09e"></h2>

## NVIDIA GPU

- pre-installed driver may conflict with nvidia driver
- check the wiki for more info:
    - https://wiki.archlinux.org/title/NVIDIA

<h2 id="7e150414eb9bd14e4769252dda140335"></h2>

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

<h2 id="d6b8ea18f9137882156a9d41fd989cd6"></h2>

## i3blocks

- `sudo pacman -S acpi i3blocks`   // acpi for battery info
- `paru mpstat`  // for cpu info
- `paru amixer`  // for volume control


<h2 id="b3fa013ae44a3d42e6cc8298c03951fc"></h2>

## Laptop Battery Life

check `auto-cpufreq` on github


<h2 id="f73a3dfcf8bbecf604228b1b8f4bbb15"></h2>

## Dev Tools

- tk (for python)
- rustup (rustup default stable)

<h2 id="4340fd73e75df7a9d9e45902a59ba3a4"></h2>

## headers

- `sudo pacman -S linux-headers`
- lts headers: `sudo pacman -S linux-lts-headers`


<h2 id="55b8c4a0eb572538a44c6c44511b00b3"></h2>

## Resize Partitions

1. boot from usb installer
2. `parted /dev/sda`
3. (parted) print
4. (parted) resizepart <your-partition number to resize>
5. (parted) <provide a END>
6. (parted) quit
7. `resize2fs /dev/sda2`


