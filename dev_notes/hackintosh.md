

# 有线以太网实现 AirDrop 功能

```bash
defaults write com.Apple.NetworkBrowser BrowseAllInterfaces 1
```

- 黑苹果的话， 型号设置为 "MacPro5,1" ?


# Catalina 下 CAT 激活 

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


# Clover USB Creation

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
    1. download [Clover installer](http://sourceforge.net/projects/cloverefiboot) 
        - or [CloverHackyColor](https://github.com/CloverHackyColor/CloverBootloader/releases)
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

# Misc

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


# 改3码

0. Hackintool 查看 System ID,  Gq3489ugfi 等一堆信息...
1. 挂载硬盘的EFI分区用Clover Configurator打开config.plist..
2. System Parameters /  从系统中获取
3. RT Variable  / 依次点击从SMBIOS获取 然后 hack 获取。command+s  保存

> 有同学说不是三码吗，怎么才改了两个地方？其实还有一个最重要的序列号没改，这就是为什么安装后序列号搜是一样的原因。主要是因为我们是黑苹果，只需要iMessage info就够了，尽量避免污染其他的序列号。改动方式是，选择SMBIOS，然后点击生成新的（generate）。

> 可能需要 EmuVariableUefi-64.efi




# Centos bootable USB installer on OSX

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






