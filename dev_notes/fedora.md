[](...menustart)

- [Fedora Note](#40857e0ce61cedc7c1f5492555b311de)
    - [DNF](#c7b4cead11512ded46091df0eb6d21b0)
    - [Enable SSHD](#77b0f74f5eab657f8ce828634fd95700)
    - [VBOX guest access shared folder](#77518441c72db08577755590d031dc34)
    - [???](#0d1b08c34858921bc7c662b228acb7ba)
    - [ohmyzsh](#c800ccea31a78e9f16fa08fb53ea2581)
    - [VIM](#d53cfc4bdeb96eaee47dd710b3c2ed21)
    - [HiDP](#17b647d3c5ef5dcdc74bb1fd86fcb8af)
    - [install chrome](#d831661e45cf9f0f54645a3d01320f4a)
    - [key remapping](#630e5253279d402cfcb2b8294cdebaad)
- [Fedora On MacOSX](#27615516bd10296ed37d854f19763fbb)
    - [Fan Speed Control](#826d3a5d3aeba3ebdb5bd3dbba5b1b0c)
    - [RDP](#a66d0b3ece299ba53eafac86750cfb4a)
    - [Bluetooth keyboard](#6e67ece0f502a80f68b0afc07cf35dc2)
- [Linux Misc](#3f78f52517c554a490a5ca4eb80ec3e6)
    - [Auto Mount](#ca728e5c99926d124661d3a8eab19ca4)
    - [update kernel args](#4c8412aa37c9af30b09596ffd5455c36)

[](...menuend)


<h2 id="40857e0ce61cedc7c1f5492555b311de"></h2>

# Fedora Note

<h2 id="c7b4cead11512ded46091df0eb6d21b0"></h2>

## DNF

```bash
$ sudo vim /etc/dnf/dnf.conf

# add following lines
max_parallel_downloads=5
fastestmirror=True
```


<h2 id="77b0f74f5eab657f8ce828634fd95700"></h2>

## Enable SSHD

```bash
$ systemctl enable sshd
$ systemctl start sshd
```

<h2 id="77518441c72db08577755590d031dc34"></h2>

## VBOX guest access shared folder

```bash
$ sudo usermod --append --groups vboxsf $USER
```



<h2 id="0d1b08c34858921bc7c662b228acb7ba"></h2>

## ???

```bash
$ sudo dnf update
$ sudo dnf group install "C Development Tools and Libraries" "Development Tools"
$ sudo dnf install clang
```

```bash
~$ brew install~
  vim ctags go gotags node@16 prettier black cpplint clang-format rust rustfmt cmake openjdk@17 mono

~ $ echo 'export PATH="/home/linuxbrew/.linuxbrew/opt/clang-format/bin:$PATH"' >>  ~/.profile
```

<h2 id="c800ccea31a78e9f16fa08fb53ea2581"></h2>

## ohmyzsh

```bash
$ sudo dnf install util-linux-user
$ sudo dnf install zsh -y
$ chsh -s $(which zsh)

$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k
echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >> ~/.profile # ~/.zshrc
```

For gnome-terminal, `Preferences/Unnamed/Command`, Select “Run a custom command instead of my shell” then type `zsh`

<h2 id="d53cfc4bdeb96eaee47dd710b3c2ed21"></h2>

## VIM

copy .vimrc from somewhere...

```bash
$ git clone https://github.com/mebusy/vundle.git ~/.vim/bundle/vundle
$ vim +BundleInstall
```

sudo dnf install -y python3 python3-devel vim
sudo dnf install -y ctags go gotags
sudo dnf install -y nodejs black rust
sudo dnf install -y rustfmt cmake java-17-openjdk
sudo dnf install -y clang-tools-extra mono-core
(clang-format , mono )

pip install cpplint
npm install -g prettier


<h2 id="17b647d3c5ef5dcdc74bb1fd86fcb8af"></h2>

## HiDP

```bash
sudo dnf install gnome-tweak-tool
```

- Font -> Scale Factor : 2


<h2 id="d831661e45cf9f0f54645a3d01320f4a"></h2>

## install chrome

```bash
sudo dnf install -y fedora-workstation-repositories
sudo dnf config-manager --set-enabled google-chrome

sudo update-crypto-policies --set LEGACY
sudo dnf install -y google-chrome-stable
```

<h2 id="630e5253279d402cfcb2b8294cdebaad"></h2>

## key remapping

https://github.com/petrstepanov/gnome-macos-remap

```bash
$ sudo dnf install autokey autokey-gtk
```

```bash
git clone https://github.com/petrstepanov/gnome-macos-remap
cd gnome-macos-remap
chmod +x ./install.sh ./uninstall.sh
./install.sh
```

Last step:

Open `AutoKey` (autokey-gtk). In `Edit -> Preferences` menu make sure the `Automatically start AutoKey at login checkbox` is on.


---

<h2 id="27615516bd10296ed37d854f19763fbb"></h2>

# Fedora On MacOSX

<h2 id="826d3a5d3aeba3ebdb5bd3dbba5b1b0c"></h2>

## Fan Speed Control

https://github.com/linux-on-mac/mbpfan

```bash
$ sudo dnf install -y mbpfan chkconfig
$ chkconfig --level 2345 mbpfan on && chkconfig --level 016 mbpfan off
$ systemctl start mbpfan.service
```


<h2 id="a66d0b3ece299ba53eafac86750cfb4a"></h2>

## RDP

You can not access remote desktop if the host fedora screen is locked.

To unlock the it,

```bash
$ loginctl list-sessions
SESSION  UID USER   SEAT  TTY  
      2 1000 mebusy       pts/0
      6 1000 mebusy seat0 tty2
```


```bash
$ loginctl unlock-session 6
```

<h2 id="6e67ece0f502a80f68b0afc07cf35dc2"></h2>

## Bluetooth keyboard

if disconnect right after connect

```bash
sudo nano /etc/modprobe.d/bluetooth.conf

Add this line:
options bluetooth disable_ertm=Y
```


<h2 id="3f78f52517c554a490a5ca4eb80ec3e6"></h2>

# Linux Misc


<h2 id="ca728e5c99926d124661d3a8eab19ca4"></h2>

## Auto Mount

```bash
/etc/fstab

set it up such that your volume will be automatically mounted on some server distribution
use 'lsblk' to display block devices

naive mount example:    /dev/sdb1  /mnt/mydisk  ext4 defaults  0 0
    ( the /mnt/disk folder should be created at first )

the problem here is ,  the '/dev/sdb1' is no static, when you reboot your system, it may change. well, that is where the UUID comes to play.

to get the UUID,  run command 'sudo blkid'

then, replace  blk device with uuid
UUID=3255683f-53a2-4fdf-91cf-b4c1041e2a62 /mnt/mydisk  ext4 defaults  0 0
```

<h2 id="4c8412aa37c9af30b09596ffd5455c36"></h2>

## update kernel args

```bash
$ grubby --remove-args="acpi=strict noapic" --update-kernel=$(ls -t1 /boot/vmlinuz-*.x86_64 | head -1)
```


