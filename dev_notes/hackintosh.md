...menustart

- [NUC8i5BEK Hackintosh](#da39d68f2cf6c3c46123458cd98bd79d)
    - [NUC8i5BEK BISO setting](#90b4244131823d7d8c05f4f1c274183e)
    - [Hackintosh USB Creation](#3144f57f7c88cbc932e24094440b99d8)
- [PMSET](#4aef377d2268514c138fb8df812de501)
    - [Catalina 10.5.2 Sleep problem](#bcbe6e609bff0627e2e3654d1a1123e8)
    - [Big Sur Sleep problem](#8793db1e9550cee531b14bcf6086ff68)
- [Misc](#74248c725e00bf9fe04df4e35b249a19)
    - [Centos bootable USB installer on OSX](#e529594e6b7af1bbc305ae37bca03507)
    - [Iris Plus 655  Without WhatEverGreen](#b629a48f87baa1255d141a0d31957405)
    - [check your opencore plist](#f9a1aa084270d908f100a833ffc5f42d)

...menuend


<h2 id="da39d68f2cf6c3c46123458cd98bd79d"></h2>


# NUC8i5BEK Hackintosh

<h2 id="90b4244131823d7d8c05f4f1c274183e"></h2>


## NUC8i5BEK BISO setting

<details>
<summary>
BIOS 077
</summary>

- « Intel VT for directed I/VO (VT-d) » ： disabled
    - **can be enabled if you set DisableIoMapper to YES**
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




<h2 id="3144f57f7c88cbc932e24094440b99d8"></h2>


## Hackintosh USB Creation

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
    diskutil partitionDisk /dev/disk1 3 MBR FAT32 "OpenCore EFI" 200Mi HFS+J "install_osx" 12000Mi ExFat "ExFat" R
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
- OSX installation
    - 
    ```bash
    sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/install_osx/ --nointeraction --downloadassets
    ```


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

<h2 id="8793db1e9550cee531b14bcf6086ff68"></h2>


## Big Sur Sleep problem

```bash
launchctl unload -w  /System/Library/LaunchAgents/com.apple.triald.plist
launchctl unload -w  /System/Library/LaunchAgents/com.apple.proactiveeventtrackerd.plist

rm -R com.apple.proactive.eventtracker
```

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


# Misc 


<h2 id="e529594e6b7af1bbc305ae37bca03507"></h2>


## Centos bootable USB installer on OSX

https://cloudwrk.com/create-centos-7-bootable-usb-on-osx/

1. Format a USB drive as **MBR**/eFAT with Disk Utility
2. Download CentOS 7 Full or Minimal iso file
3. Open terminal and find USB drive partition name with command “diskutil list“
4. In terminal, use dd command to copy CentOS iso to usb
5. Test usb drive in Parallels virtual machine

```bash
sudo dd if=./Downloads/CentOS-7-x86_64-DVD-1611.iso of=/dev/rdisk2 bs=1m
```

- **Note** the additional ***r*** prepended to the usb partition name rdisk2 instead of disk2**, but more faster



<h2 id="b629a48f87baa1255d141a0d31957405"></h2>


## Iris Plus 655  Without WhatEverGreen

1. Add SSDT for Iris Plus 655 iGPU
    - a) find it from network
    - or b) Hackintool / PCIe / update & export 
    - **PS: no more needed !!!, just renaming & patching !!!**
2. rename  GFX0 to IGPU , HECI to IMEI ( whatever once take over it )
    ```plist
            <dict>
                <key>Comment</key>
                <string>change GFX0 to IGPU</string>
                <key>Enabled</key>
                <true/>
                <key>Find</key>
                <data>R0ZYMA==</data>
                <key>Replace</key>
                <data>SUdQVQ==</data>
            </dict>
            <dict>
                <key>Comment</key>
                <string>change HECI to IMEI</string>
                <key>Enabled</key>
                <true/>
                <key>Find</key>
                <data>SEVDSQ==</data>
                <key>Replace</key>
                <data>SU1FSQ==</data>
            </dict>
    ```
3. Add patch to DeviceProperties


<details>
<summary>
Iris Plus 655  platform-id / device-id
</summary>

```text
1. Bios   gpu memory setting
    - Allocation : depending on the frame buffer ( look value TOTAL_STOLEN in frame buffer list )
    - DVMT total memory size: max
    - https://github.com/acidanthera/WhateverGreen/blob/master/Manual/FAQ.IntelHD.en.md
    - 但是 似乎没什么问题。。。

To inject DeviceProperties

Only these properties may be added:
— AAPL,ig-platform-id or AAPL,snb-platform-id framebuffer
— device-id for IGPU (if faking is necessary)
— device-id for IMEI (if faking is necessary)
— properties for patches (if necessary)


### AAPL,ig-platform-id

Iris Plus 655

ID: 3EA50005, STOLEN: 57 MB, FBMEM: 0 bytes, VRAM: 1536 MB, Flags: 0x00E30B0A
TOTAL STOLEN: 58 MB, TOTAL CURSOR: 1 MB (1572864 bytes), MAX STOLEN: 172 MB, MAX OVERALL: 173 MB (181940224 bytes)
Model name: Intel Iris Plus Graphics 655


Recommended framebuffers:

Laptop:
0x3EA50009 (default)


# And now you have your final framebuffer profile
0900A53E = AAPL,ig-platform-id


#### device-id

https://ark.intel.com/content/www/us/en/ark/products/135935/intel-core-i5-8259u-processor-6m-cache-up-to-3-80-ghz.html


Device ID
0x3EA5   // lucky

# And voila, you have your device-id
A53E0000 = device-id


DeviceProperties
  Add
    PciRoot(0x0)/Pci(0x2,0x0)
      AAPL,ig-platform-id  Data <>
      device-id            Data <>
      ...
```

</details>


<h2 id="f9a1aa084270d908f100a833ffc5f42d"></h2>


## check your opencore plist

https://opencore.slowgeek.com/


