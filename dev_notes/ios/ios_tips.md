...menustart

 - [Tips](#a0d4cc0f54602c3f247c72f15a7d2dbf)
	 - [符号化crash 日志](#f3339d94a6bf27a7a019412ed2bd3ba9)
	 - [IAP create , app -> ipa](#baf92b6a6a0ac6be9b16cf0d77c0a8c4)
	 - [mobile provision file 解码](#4b90af20d825ac9eb566c44390737682)

...menuend


<h2 id="a0d4cc0f54602c3f247c72f15a7d2dbf"></h2>
# Tips

<h2 id="f3339d94a6bf27a7a019412ed2bd3ba9"></h2>
## 符号化crash 日志

```shell
# ios Debug
export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer"
alias symbolicatecrash="/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash"

把你的.crash文件.app文件和.dSYM文件放在同一个目录下然后运行：
symbolicatecrash -v ScaryCrash.crash > Symbolicated.crash
```

<h2 id="baf92b6a6a0ac6be9b16cf0d77c0a8c4"></h2>
## IAP create , app -> ipa

```shell
#!/bin/bash  

APPNAME="justdance"  
ZIPNAME="${APPNAME}zip" 
IPANAME="${APPNAME}IPA" 
  
mkdir -p ./ipa/Payload  
cp -r ./${APPNAME}.app ./ipa/Payload  
cd ipa  
zip -r ${ZIPNAME} *  
mv ${ZIPNAME}.zip ${IPANAME}.ipa  
```

<h2 id="4b90af20d825ac9eb566c44390737682"></h2>
## mobile provision file 解码

```
security cms -D -i example.mobileprovision
```

