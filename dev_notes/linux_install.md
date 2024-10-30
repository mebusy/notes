
# Ubuntu

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

## install ssh server

```bash
sudo apt update
sudo apt install openssh-server

# If firewall blocked...
sudo ufw allow ssh
```

> ubuntu server shipped with ssh server, so no need to install it.

## essential tools

```bash
sudo apt update
sudo apt install build-essential
```


## Install Docker

https://docs.docker.com/engine/install/ubuntu/

## Install Nvidia Toolkit

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html


## Open WebUI It supports various LLM runners, including Ollama and OpenAI-compatible APIs.  

https://github.com/open-webui/open-webui

Installing Open WebUI with Bundled Ollama Support  / With GPU Support


## check battery status

1. `upower -i $(upower -e | grep 'BAT') | grep -E "state|to\ full|percentage"`
2. `sudo apt-get install acpi` then `acpi`


## hardwaer info

### Nvidia GPU

install nvtop  (to show nvidia GPU usage)

```bash
sudo snap install nvtop
nvtop
```

### Other hardware info

```bash
lspci # 列出系统中的 PCI 设备信息：
# or
sudo lshw -short
# or 
sudo apt install neofetch
neofetch
```

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



## driver update

### 1

- 查看可用的驱动更新：
    - `sudo ubuntu-drivers list`
- 自动安装推荐的驱动：
    - `sudo ubuntu-drivers autoinstall`
    - 这将安装系统检测到的推荐驱动，适用于大多数情况，特别是显卡驱动（如 NVIDIA 驱动）。

### 2

- 安装硬件固件（firmware）
- 某些驱动依赖于额外的固件，Ubuntu 提供了一个叫 linux-firmware 的包，包含了许多硬件的固件：
- `sudo apt install linux-firmware`


## install DWM

```bash
# build-essential
sudo apt install --no-install-recommends xorg
sudo apt install libxcb-xinerama0-dev libxinerama-dev libxft-dev suckless-tools mesa-utils network-manager feh wget cu

$ mkdir .suckless
$ cd .suckless/

$ wget https://dl.suckless.org/dwm/dwm-6.5.tar.gz

# simple terminal
$ wget https://dl.suckless.org/st/st-0.9.2.tar.gz

$ wget https://dl.suckless.org/tools/dmenu-5.3.tar.gz

tar -xzf <all>


# cd && make all 3

# the following is not not necessary, yon can just sudo make install
cd ~
mkdir bin

ln -s ~/.suckless/dwm-6.5/dwm ~/bin
ln -s ~/.suckless/st-0.9.2/st  ~/bin
ln -s ~/.suckless/dmenu-5.3/dmenu  ~/bin
# ===============

$ cat ~/.xsessionrc
exec dwm
```
