
# Fedora Note

## DNF

```bash
$ sudo vim /etc/dnf/dnf.conf

# add following lines
max_parallel_downloads=5
fastestmirror=True
```


## Enable SSHD

```bash
$ systemctl enable sshd
$ systemctl start sshd
```

## VBOX guest access shared folder

```bash
$ sudo usermod --append --groups vboxsf $USER
```



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


## HiDP

```bash
sudo dnf install gnome-tweak-tool
```

- Font -> Scale Factor : 2


## install chrome

```bash
sudo dnf install -y fedora-workstation-repositories
sudo dnf config-manager --set-enabled google-chrome

sudo update-crypto-policies --set LEGACY
sudo dnf install -y google-chrome-stable
```

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

# Fedora On MacOSX

## Fan Speed Control

https://github.com/linux-on-mac/mbpfan

```bash
$ sudo dnf install -y mbpfan chkconfig
$ chkconfig --level 2345 mbpfan on && chkconfig --level 016 mbpfan off
$ systemctl start mbpfan.service
```

##  walk up after sleep

```bash
$ sudo dnf install -y acpid
$ systemctl enable --now acpid
```

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


# Linux Misc


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
