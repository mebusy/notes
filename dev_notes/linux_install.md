
# create Ubuntu Server USB Installer

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




