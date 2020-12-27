...menustart

- [AirDrop/Continuity for those unsupported Mac device](#8578ff6a91accdcff6d3de6a3b278a69)
    - [use Air Drop with ethernet](#7f77ab6117c55a32468b643b1cc6cf31)
    - [Catalina Continuity Activation](#c544b3043a75d36024e96b058bfd617f)
- [NUC8i5BEK Hackintosh](#da39d68f2cf6c3c46123458cd98bd79d)
    - [NUC8i5BEK BISO setting](#90b4244131823d7d8c05f4f1c274183e)
    - [Clover USB Creation](#fca6772f09655f60d2a1571eb468f4b5)
    - [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [改3码](#41fcd485d3c9d5dbc0a06851ea1cda21)
    - [Clover 自动启动](#584ee5f9f8b24f6f275547b4d05d20e4)
    - [Clover 目录结构](#80aa301beb5576eafb123ce4f8d0536d)
    - [Clover 引导界面快捷键](#41f234410b778a2c38d3ad364d2f32dd)
    - [active native bluetooth , not work since 10.15.4](#8097784a066a6a0cad28895ddd08926d)
    - [update Clover](#b661467e7a885061e79bcd1aff928d46)
- [PMSET](#4aef377d2268514c138fb8df812de501)
    - [Catalina 10.5.2 Sleep problem](#bcbe6e609bff0627e2e3654d1a1123e8)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [Centos bootable USB installer on OSX](#e529594e6b7af1bbc305ae37bca03507)
    - [Create a normal bootable usb installer](#e4b093a32d54db737e399188ce596791)
    - [Intel Blueteeth-Wifi card](#d65ecd37b6aeebc52147b6f8b23404ed)

...menuend


<h2 id="8578ff6a91accdcff6d3de6a3b278a69"></h2>


# AirDrop/Continuity for those unsupported Mac device 

<h2 id="7f77ab6117c55a32468b643b1cc6cf31"></h2>


## use Air Drop with ethernet

```bash
defaults write com.Apple.NetworkBrowser BrowseAllInterfaces 1
```



<h2 id="c544b3043a75d36024e96b058bfd617f"></h2>


## Catalina Continuity Activation 

For earlier mac device which has replaced with newer wifi-bluetooth moudle:

https://github.com/dokterdok/Continuity-Activation-Tool/issues/463


```bash
// 重要
sudo mount -uw /
```

```bash
// 另一个，不确定是否需要
$ ioreg -l | grep "board-id" | awk -F\" '{print $4}'
Mac-*YourBoardID*


sudo /usr/libexec/PlistBuddy -c "Set:Mac-*YourBoardID*:ContinuitySupport true" "/System/Library/Frameworks/IOBluetooth.framework/Versions/A/Resources/SystemParameters.plist"


sudo -E perl -pi -e "s/\Mac-00BE6ED71E35EB86/\Mac-*YourBoardID*/" /System/Library/Extensions/IO80211Family.kext/Contents/PlugIns/AirPortBrcm4360.kext/Contents/MacOS/AirPortBrcm4360

sudo -E perl -pi -e "s/\Mac-00BE6ED71E35EB86/\Mac-*YourBoardID*/" /System/Library/Extensions/IO80211Family.kext/Contents/PlugIns/AirPortBrcmNIC.kext/Contents/MacOS/AirPortBrcmNIC
```

<h2 id="da39d68f2cf6c3c46123458cd98bd79d"></h2>


# NUC8i5BEK Hackintosh

<h2 id="90b4244131823d7d8c05f4f1c274183e"></h2>


## NUC8i5BEK BISO setting

<details>
<summary>
BIOS 077
</summary>

- « Intel VT for directed I/VO (VT-d) » ： disabled
- « Secure Boot » ： disabled
- « Fast Boot » ： disabled
- UEFI boot enalbe /   Legacy Boot disable
- SATA mode ： AHCI
- Boot->Boot Configuration-> « Boot Network Devices Last » ： disabled
- Power->Secondary Power Settings, « Wake on LAN from S4/S5 », set to « Stay Off »
- Devices->Video, « IGD Minimum Memory » set to 64mb
- Devices->Video, « IGD Aperture Size » set to MAX
- disable reader-card

</details>


<details>
<summary>
BIOS 085
</summary>

https://github.com/zearp/Nucintosh

- Devices -> USB -> Port Device Charging Mode: off
    - wifi -> disable
    - readcard -> disable
- Security -> Thunderbolt Security Level: Legacy Mode
- Power -> Wake on LAN from S4/S5: Stay Off
- Boot -> Boot Configuration -> Network Boot: Disable
- Boot -> Secure Boot -> Disable

</details>


<h2 id="fca6772f09655f60d2a1571eb468f4b5"></h2>


## Clover USB Creation

- [post on tonymac86](https://www.tonymacx86.com/threads/guide-booting-the-os-x-installer-on-laptops-with-clover.148093/#post-917900)

- Recommend: MBR with a FAT32 partition for Clover and a separate HFS+J partition for the OS X installer.
    - most computers can boot from it (even with UEFI), and it is convenient that the EFI partition will mount automatically when the USB is inserted.

- step 1,find your USB disk, in this case its /dev/disk1
    - 
    ```bash
    diskutil list
    /dev/disk0 (internal, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *500.1 GB   disk0
       1:                        EFI EFI                     209.7 MB   disk0s1
       2:                  Apple_HFS 10.10.x                 80.0 GB    disk0s2
       3:                  Apple_HFS 10.11.gm1               80.0 GB    disk0s3
       4:       Microsoft Basic Data Win10_TP                79.4 GB    disk0s4
       5:                  Apple_HFS 10.10.test              80.0 GB    disk0s5
    /dev/disk1 (external, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:                                                   *8.0 GB     disk1[/B]
    ```
- step 2, partion , in this example, it create 3 partions 
    - 
    ```bash
    diskutil partitionDisk /dev/disk1 3 MBR FAT32 "CLOVER EFI" 200Mi HFS+J "install_osx" 12000Mi ExFat "ExFat" R
    Finished partitioning on disk1
    /dev/disk1 (external, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *31.0 GB    disk1
       1:                 DOS_FAT_32 CLOVER EFI              209.7 MB   disk1s1
       2:                  Apple_HFS install_osx             12.6 GB    disk1s2
       3:               Windows_NTFS ExFat                   18.2 GB    disk1s3
    ```
    - Note: If you're using Clover legacy, the USB should must be MBR.
    - Note: Some BIOS implementations require GPT, some require MBR (many allow both). If you can't get BIOS to recognize your USB for booting, try GPT instead of MBR.
- Clover
    1. download [Clover installer](https://github.com/CloverHackyColor/CloverBootloader/releases) 
    2. run Clover installer
        - if using MBR, select the target of the install to "CLOVER EFI" using "Change Install Location"
        - select "Customize" (the default is a legacy install -- we need to change it)
            - check "Install for UEFI booting only", "Install Clover in the ESP" will automatically select
            - 
- OSX installation
    - 
    ```bash
    sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/install_osx/ --nointeraction --downloadassets
    ```

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


## Misc

```
DataHubDxe-64.efi = DataHub protocol and mandatory for macOS.
FSInject-64.efi = Driver responsible for Clover kext injection into kernel cache.
SMCHelper-64.efi = Restore SMC keys left in NVRAM by FakeSMC (VirtualSMC.efi incompatible)
VBoxHfs-64.efi = Open source EFI file-system driver for HFS+ file system.
+
ApfsDriverLoader-64.efi = Recognize and boot from APFS volumes needed by Mojave.
AptioMemoryFix-64.efi = Needed for Afps driver; includes NVRAM fixes and better memory management.
EmuVariableUefi-64.efi = Support for NVRAM variables if hardware NVRAM is not supported.
NvmExpressDxe-64.efi = Driver support for NVM Express devices.
```


<h2 id="41fcd485d3c9d5dbc0a06851ea1cda21"></h2>


## 改3码

0. Hackintool 查看 System ID,  Gq3489ugfi 等一堆信息...
1. 挂载硬盘的EFI分区用Clover Configurator打开config.plist..
2. System Parameters /  从系统中获取
3. RT Variable  / 依次点击 from SMBIOS 获取 然后 from system /  hack 获取。command+s  保存

> 有同学说不是三码吗，怎么才改了两个地方？其实还有一个最重要的序列号没改，这就是为什么安装后序列号搜是一样的原因。主要是因为我们是黑苹果，只需要iMessage info就够了，尽量避免污染其他的序列号。改动方式是，选择SMBIOS，然后点击生成新的（generate）。

> 需要 EmuVariableUefi-64.efi


<h2 id="584ee5f9f8b24f6f275547b4d05d20e4"></h2>


## Clover 自动启动

use volume name of your OSX volume.

<h2 id="80aa301beb5576eafb123ce4f8d0536d"></h2>


## Clover 目录结构

- BOOT   clover引导文件
- CLOVER 
    1. ACPI/
        - origin  提取/储存 DSDT/SSDT 的问题， 如果你需要修改你的 DSDT/SSDT, 可以在4叶草引导界面下 直接按F4进行提取，提取的DSDT/SSDT 就会存放到这里。
        - patched  提取的DSDT/SSDT 修改好后，放到这个文件夹中，它会被自动加载。
    2. CLOVERX64.efi  引导clover最主要的文件之一
    3. config.plist   clover引导配置文件. 通过它的配置，可以驱动你的声卡 显卡 睡眠，等等.
    4. doc  clover 帮助文档
    5. driver   驱动 legacy boot
    6. driver64-UEFI  驱动 for UEFI boot
    7. kerts   可以配置各个OS版本的驱动，一般只留下Other 一个文件夹
        - Other
            - Lilu.kext  补丁驱动，多用于配合其他驱动使用
            - AppleALC.kext  Realtek onboard audio  需要配合lilu.kext使用，主要的作用就是加载原生AppleHDA声卡驱动。
                - 目前AppleACL 已经能够进行很好的仿冒声卡
            - VoodooHDA-2.9.1.kext黑苹果万能声卡驱动
                - 万能声卡，适用于很少一部分人。万能声卡是个玄学驱动，但对hdmi音频输出却基本能做到
            - CodecCommander.kext   解决耳机有杂音和睡眠唤醒无法自动切换或无声的问题
            - CPUFriend.kextCPU  变频动态注入 CPU 电源管理数据
            - Fake-PCI-ID.kext  牛逼
            - USBInjectAll.kext  In 10.11+ Apple has changed significantly the way the USB drivers work.
            - WhateverGreen.kext  Lilu plugin providing patches to select GPUs on macOS. 显卡驱动补丁集
                - 对于集显，A/N卡显示的补丁驱动，解决黑屏，花屏等问题。
            - XHCI-unsupported.kext： 英特X99系列主板驱动
    8. misc  主要存放日志，用于排错
    9. OEM   存放不同主板电脑型号的一个配置文件. OEM可以包含整个clover文件夹下面的所有文件(除了OEM). 除了你希望用一个引导去引导多台电脑，否则没什么用
    10. ROM  一般用于存放显卡提取
    11. themes 开机引导界面主题
    12. tools  没什么用, 一般可以忽略


<h2 id="41f234410b778a2c38d3ad364d2f32dd"></h2>


## Clover 引导界面快捷键

- F4 如上
- F5 保存初步修复的 DSDT
- F6 保存显卡 BIOS 文件


<h2 id="8097784a066a6a0cad28895ddd08926d"></h2>


## active native bluetooth , not work since 10.15.4

<details>
<summary>
deprecated
</summary>

- brew install libusb
- firmware source:  https://github.com/wulf7/iwmbt-firmware
- firmware download: https://www.tonymacx86.com/attachments/bluetooth_fix-zip.439550/
- thread: https://www.tonymacx86.com/threads/guide-intel-nuc7-nuc8-using-clover-uefi-nuc7i7bxx-nuc8i7bxx-etc.261711/page-207

```bash
sudo launchctl load -w /Library/LaunchDaemons/iwmbtfw.plist

iwmbtfw.plist
---------------------------------------------------------------------------------
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.iwmbtfw.firmwares</string>
    <key>ProgramArguments</key>
    <array>
        <string>/etc/rc.boot.d/30.fix_bluetooth.local</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

Does it need specifiy root user ?

```xml
<key>UserName</key>
<string>root</string>
```

</details>





<h2 id="b661467e7a885061e79bcd1aff928d46"></h2>


## update Clover

1. colver configurator
    - Install/Update Clover
    - click "Save to desktop"
2. 安装
    - 不要勾选。 安装Clover 到 EFI系统区
    - 不要勾选。安装Clover系统偏好设置面板
    - 会安装到 root 目录 /
        - EFI
        - EFI_backup   删除
3. 升级
    - EFI/BOOT/BOOTX64.efi
    - EFI/CLOVER/CLOVERX64.efi
    - EFI/CLOVER/driver64UEFI/
    - EFI/CLOVER/tools/

<h2 id="4aef377d2268514c138fb8df812de501"></h2>


# PMSET

https://eclecticlight.co/2017/01/20/power-management-in-detail-using-pmset/

1. Sleep
2. displaysleep is the time in minutes before the display is put to sleep
3. disksleep is the time in minutes before hard disks are spun down and put to sleep; 
4. gpuswitch sets GPU behaviour during sleep, and appears to be undocumented;
5. hibernatefile sets the location of the cache to be used when going into standby mode, which must be on the boot disk; 
6. hibernatemode is set to 0 for plain sleep (desktops), 3 to store a copy of memory to disk and keep memory powered up (laptops), or 25 for full hibernation in which memory is powered down too;
7. highstandbythreshold, which is set to 50 by default (i.e. 50 percent battery capacity). Instead of one standbydelay argument you now have two: standbydelayhigh and standbydelaylow. If you’re above 50, the high delay is used, if you’re below 50 percent battery, the low delay kicks in.
8. networkoversleep - this setting affects how OS X networking presents shared network services during system sleep. This setting is not used by all platforms; changing its value is unsupported.
9. powernap sets whether your Mac will take Power Naps, where supported;
10. proximitywake - On supported systems, this option controls system wake from sleep based on proximity of devices using same iCloud id. (value = 0/1)
11. sleep is the time in minutes to system sleep; 0 means never;
12. standby sets whether to hibernate when a Mac has been asleep for a set period; this writes memory to disk and powers down memory;
13. standbydelay
14.     is the delay in seconds between going to sleep and switching to standby mode;
15. tcpkeepalive
16. ttyskeepawake can prevent sleep when a text input, such as a remote login session, is active;
17. womp is 1 if you want your Mac to wake when it receives a ‘magic’ network packet, which is the same as wake for network access in the pane;


<h2 id="bcbe6e609bff0627e2e3654d1a1123e8"></h2>


## Catalina 10.5.2 Sleep problem

```bash
launchctl unload -w /System/Library/LaunchAgents/com.apple.parsec-fbf.plist
```

As parsec-fbf sends analytical data to Apple and flushes which is sent from local machine, then probably there is no any serious drawbacks on disabling parsec.fbf agent, except that data collected by Siri is not flushed. Data is collected in users Cashes into com.apple.parsecd folder.

Data can be flushed manually if needed:

```bash
cd ~/Library/Caches
rm -R com.apple.parsecd
```

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


# Misc 


<h2 id="e529594e6b7af1bbc305ae37bca03507"></h2>


## Centos bootable USB installer on OSX

https://cloudwrk.com/create-centos-7-bootable-usb-on-osx/

1. Format a USB drive as eFAT with Disk Utility
2. Download CentOS 7 Full or Minimal iso file
3. Open terminal and find USB drive partition name with command “diskutil list“
4. In terminal, use dd command to copy CentOS iso to usb
5. Test usb drive in Parallels virtual machine

```bash
sudo dd if=./Downloads/CentOS-7-x86_64-DVD-1611.iso of=/dev/rdisk2 bs=1m
```

**Note the additional “r” prepended to the usb partition name rdisk2 instead of disk2**.

<h2 id="e4b093a32d54db737e399188ce596791"></h2>


## Create a normal bootable usb installer

1. Usb format to **Mac OS Extended**, at least 12G
2. *MyVolume* is the name of the USB flash drive 

```bash
# Catalina:*
sudo /Applications/Install\ macOS\ Catalina.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
```


<h2 id="d65ecd37b6aeebc52147b6f8b23404ed"></h2>


## Intel Blueteeth-Wifi card

- [wifi](https://github.com/OpenIntelWireless/itlwm)
    - itlwm 
- [blueteeth](https://github.com/zxystd/IntelBluetoothFirmware)





