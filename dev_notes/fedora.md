
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



## Home Brew

```bash
$ sudo dnf update
$ sudo dnf group install "C Development Tools and Libraries" "Development Tools"
$ sudo dnf install clang
```

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# after installation
$ (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> ~/.profile
$ brew install gcc
```

```bash
$ brew install vim ctags go gotags node@16 prettier black cpplint clang-format rust rustfmt cmake openjdk@17 mono

$ brew link  --overwrite  node@16
$ echo 'export PATH="/home/linuxbrew/.linuxbrew/opt/clang-format/bin:$PATH"' >>  ~/.profile
```

## ohmyzsh

```bash
$ sudo dnf install util-linux-user
$ sudo dnf install zsh -y
$ chsh -s $(which zsh)

$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

$ brew install romkatv/powerlevel10k/powerlevel10k
$ echo "source $(brew --prefix)/opt/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc
```

## VIM

copy .vimrc from somewhere...

```bash
$ git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
$ vim +BundleInstall
```


## HiDP

```bash
sudo dnf install gnome-tweak-tool
```

# Linux Misc


## Auto Mount

```bash
/etc/fstab

   set it up such that your volume will be automatically mounted on some server distribution
    use 'lsblk' to display block devices

   naive mount example:    /dev/sdb1  /mnt/mydisk  ext4 defaults  0 0
        ( the /mnt/disk folder should be created at first )

    the problem here is ,  the `/dev/sdb1` is no static, when you reboot your system, it may change. well, that is where the UUID comes to play.

    to get the UUID,  run command `sudo blkid`

    then, replace  blk device with uuid
	UUID=3255683f-53a2-4fdf-91cf-b4c1041e2a62 /mnt/mydisk  ext4 defaults  0 0
```
