
# Tips

## 符号化crash 日志

```shell
# ios Debug
export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer"
alias symbolicatecrash="/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash"

把你的.crash文件.app文件和.dSYM文件放在同一个目录下然后运行：
symbolicatecrash -v ScaryCrash.crash > Symbolicated.crash
```
