

# 有线以太网实现 AirDrop 功能

```bash
defaults write com.Apple.NetworkBrowser BrowseAllInterfaces 1
```

- 黑苹果的话， 型号设置为 "MacPro5,1" ?


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



