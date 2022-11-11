[](...menustart)


[](...menuend)


[TWRP for Asus Nexus 7 2013 Wi-Fi](https://twrp.me/asus/asusnexus72013wifi.html)

[twrp 3.3.1](https://dl.twrp.me/flo/twrp-3.3.1-0-flo.img)

[谷歌官方刷机](https://developers.google.com/android/images?hl=zh-cn)

[SuperSU.zip](https://download.chainfire.eu/1220/SuperSU/SR5-SuperSU-v2.82-SR5-20171001224502.zip?retrieve_file=1)

1. unlock bootloader
    - adb reboot bootloader
    - fastboot oem unlock
2. fastboot flash recovery twrp.img
    - choose Recovery mode
    - adb push SuperSU.zip to /sdcard
    - install -> scroll down -> zip
        - wipe cache , and press 'reboot'


    


