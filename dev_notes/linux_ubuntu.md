[](...menustart)

- [Ubuntu](#3d945423f8e9496c429a5d8c65b4604f)
    - [create Ubuntu Server USB Installer](#5a69e7f6a9934e94a18908bd24acd99c)
    - [install ssh server](#da61b0b64c81f44435a06dbb72effa6b)
    - [essential tools](#255d9de101876e6cd66d81243169c00e)
    - [Install Docker](#d2e76c80cf106b0ec7857ece4367a212)
    - [Install Nvidia Toolkit](#d94fd9201df2ca2f909e0a13921f13cb)
    - [Open WebUI It supports various LLM runners, including Ollama and OpenAI-compatible APIs.](#54fa549e4ede2bbd61c40846772de47f)
    - [check battery status](#228fc2a74d61d934352e28886efb21b7)
    - [hardwaer info](#c9054986f09441b158dbb2171abd32b4)
        - [Nvidia GPU](#08ba5c7bec96f0f5892bcbf3bfc8e151)
        - [Other hardware info](#c74a13adc9961413e00b935d5e8a006a)
        - [CPU/GPU 温度](#2ca676cc2305b44c5b94ee023efa6489)
    - [driver update](#1955f8c7ae727667a73b18fa365b8523)
        - [1](#c4ca4238a0b923820dcc509a6f75849b)
        - [2](#c81e728d9d4c2f636f067f89cc14862c)
    - [install DWM](#3a26231a28624e2f6db483c7c0423512)

[](...menuend)


<h2 id="3d945423f8e9496c429a5d8c65b4604f"></h2>

# Ubuntu

<h2 id="5a69e7f6a9934e94a18908bd24acd99c"></h2>

## create Ubuntu Server USB Installer

1. download ubuntu server
2. convert .iso to image (.dmg)
    ```bash
	hdiutil convert -format UDRW -o ubuntu-server-img  ubuntu-24.04.1-live-server-amd64.iso
    ```
3. unmount the USB device(say /dev/disk4) you want to make it installer
    ```bash
	diskutil unmountDisk  diskN
    ```
4. write data to USB partition (say /dev/disk4s4)
    ```bash
	sudo dd if=./ubuntu-server-img.dmg of=/dev/disk4s4 bs=1m
    ```

<h2 id="da61b0b64c81f44435a06dbb72effa6b"></h2>

## install ssh server

```bash
sudo apt update
sudo apt install openssh-server

# If firewall blocked...
sudo ufw allow ssh
```

> ubuntu server shipped with ssh server, so no need to install it.

<h2 id="255d9de101876e6cd66d81243169c00e"></h2>

## essential tools

```bash
sudo apt update
sudo apt install build-essential
```


<h2 id="d2e76c80cf106b0ec7857ece4367a212"></h2>

## Install Docker

https://docs.docker.com/engine/install/ubuntu/

<h2 id="d94fd9201df2ca2f909e0a13921f13cb"></h2>

## Install Nvidia Toolkit

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html


<h2 id="54fa549e4ede2bbd61c40846772de47f"></h2>

## Open WebUI It supports various LLM runners, including Ollama and OpenAI-compatible APIs.  

https://github.com/open-webui/open-webui

Installing Open WebUI with Bundled Ollama Support  / With GPU Support


<h2 id="228fc2a74d61d934352e28886efb21b7"></h2>

## check battery status

1. `upower -i $(upower -e | grep 'BAT') | grep -E "state|to\ full|percentage"`
2. `sudo apt-get install acpi` then `acpi`


<h2 id="c9054986f09441b158dbb2171abd32b4"></h2>

## hardwaer info

<h2 id="08ba5c7bec96f0f5892bcbf3bfc8e151"></h2>

### Nvidia GPU

install nvtop  (to show nvidia GPU usage)

```bash
sudo snap install nvtop
nvtop
```

<h2 id="c74a13adc9961413e00b935d5e8a006a"></h2>

### Other hardware info

```bash
lspci # 列出系统中的 PCI 设备信息：
# or
sudo lshw -short
# or 
sudo apt install neofetch
neofetch
```

<h2 id="2ca676cc2305b44c5b94ee023efa6489"></h2>

### CPU/GPU 温度

```bash
# error !!
curl -L https://bit.ly/glances | /bin/bash
glances # and press `f`
glances -s # 显示隐藏的传感器信息
```

glances will install `lm-sensors`

```bash
sudo sensors-detect
sensors  # or `watch sensors`
```



<h2 id="1955f8c7ae727667a73b18fa365b8523"></h2>

## driver update

<h2 id="c4ca4238a0b923820dcc509a6f75849b"></h2>

### 1

- 查看可用的驱动更新：
    - may need `sudo apt install alsa-utils`
    - `sudo ubuntu-drivers list`
- 自动安装推荐的驱动：
    - `sudo ubuntu-drivers autoinstall`
    - 这将安装系统检测到的推荐驱动，适用于大多数情况，特别是显卡驱动（如 NVIDIA 驱动）。

<h2 id="c81e728d9d4c2f636f067f89cc14862c"></h2>

### 2

- 安装硬件固件（firmware）
- 某些驱动依赖于额外的固件，Ubuntu 提供了一个叫 linux-firmware 的包，包含了许多硬件的固件：
- `sudo apt install linux-firmware`


<h2 id="3a26231a28624e2f6db483c7c0423512"></h2>

## install DWM

```bash
# build-essential
sudo apt install -y --no-install-recommends xorg
sudo apt install -y libxcb-xinerama0-dev libxinerama-dev libxft-dev suckless-tools mesa-utils network-manager feh wget cu
```


```bash
#bash

set -e

# array of elements  dwm, st, dmenu
tools=(dwm st dmenu)
# url path
pathes=(dwm st tools)

mkdir -p .suckless
cd .suckless

mkdir -p ~/bin

for i in ${!tools[@]}; do
    # sort and print the last line
    fname=`curl -sL https://dl.suckless.org/${pathes[$i]} | grep "${tools[$i]}-" | sort | tail -n 1 | cut -d '"' -f 2` 
    echo $fname

    # download the file
    rm -f $fname
    wget https://dl.suckless.org/${pathes[$i]}/$fname
    tar -xvf $fname
    
    # remove suffix .tar.gz from the file name
    dirname=`echo $fname | sed 's/.tar.gz//'`
    echo $dirname

    cd $dirname
    # if is Linux
    if [ "$(uname)" == "Linux" ]; then
        make clean && make
    fi

    ln -sf `pwd`/${tools[$i]} ~/bin/

    cd ..
done

echo "exec dwm" > ~/.xinitrc
# echo "exec dwm" > ~/.xsessionrc

```
