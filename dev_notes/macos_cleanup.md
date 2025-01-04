[](...menustart)

- [Xcode](#a3b5ebd8a1e9ebf44a172e80d5a7d3a3)
- [Docker](#c5fd214cdd0d2b3b4272e73b022ba5c2)
- [Chrome](#986c37480b1f1c2e443504b38b6361b4)

[](...menuend)


<h2 id="a3b5ebd8a1e9ebf44a172e80d5a7d3a3"></h2>

## Xcode

```bash
$ xcrun simctl delete unavailable
```

it will remove the unavailable under `~/Library/Developer/CoreSimulator/Devices`


Also, you can remove files under following directories:


```bash
~/Library/Developer/Xcode/Archives
~/Library/Developer/Xcode/DerivedData
"~/Library/Developer/Xcode/iOS Device Logs"
```



<h2 id="c5fd214cdd0d2b3b4272e73b022ba5c2"></h2>

## Docker

```bash
docker system prune [-a]
```


<h2 id="986c37480b1f1c2e443504b38b6361b4"></h2>

## Chrome

`~/Library/Application Support/Google/Chrome/Default/Extensions/`

clean extension


