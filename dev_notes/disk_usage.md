
# Check OSX/Linux Disk Usage


## show disk statistics

df - Display Free disk space

```bash
$ df | less

Filesystem     512-blocks       Used Available Capacity iused      ifree %iused  Mounted on
/dev/disk1s2s1  500000000   30100528  84283120    27%  502068  421415600    0%   /
devfs                 393        393         0   100%     680          0  100%   /dev
/dev/disk1s5    500000000   37751352  84283120    31%      20  421415600    0%   /System/Volumes/VM
/dev/disk1s3    500000000    1664688  84283120     2%    5506  421415600    0%   /System/Volumes/Preboot
/dev/disk1s6    500000000       9456  84283120     1%      23  421415600    0%   /System/Volumes/Update
/dev/disk1s1    500000000  343730552  84283120    81% 2096587  421415600    0%   /System/Volumes/Data
/dev/disk2s1   1453595632 1066505080 386732136    74% 1873260 1933660680    0%   /Volumes/WORK
map auto_home           0          0         0   100%       0          0  100%   /System/Volumes/Data/home
```


## Quick find largest files

```bash
$ ls -Sl  # -S means Sort by size

drwx------@  3 qibinyi  staff    96 Aug 13  2020 Applications
drwx------@ 11 qibinyi  staff   352 Oct 14 12:02 Desktop
drwx------@  5 qibinyi  staff   160 Oct  7 14:01 Documents
drwx------@ 24 qibinyi  staff   768 Oct 18 11:27 Downloads
drwx------@ 91 qibinyi  staff  2912 Oct 18 10:35 Library
drwx------+  5 qibinyi  staff   160 Aug  1 15:19 Movies
drwx------+  4 qibinyi  staff   128 Aug 13  2020 Music
```

## dive in deep

du – display disk usage statistics


- Display top 10 disk usage, in (1 MiB) blocks.
    - **most useful to find the most disk-usage files**
    - `du -m <path> | sort -nr | head -n 10`
    ```bash
    $ du -m .  | sort -nr | head -n 10                                                                                                                              130 ↵

    64259	.
    37771	./Library
    13896	./Library/Developer
    8527	./Library/Developer/CoreSimulator
    7202	./Library/Containers
    6767	./Library/Containers/com.tencent.xinWeChat/Data/Library
    6767	./Library/Containers/com.tencent.xinWeChat/Data
    6767	./Library/Containers/com.tencent.xinWeChat
    ```
- some times you may just want the top level directory instead of levels
    ```bash
    du -sm *  | sort -nr | head -n 10                                                                                                                             130 ↵

    37769	Library
    6191	VirtualBox VMs
    5817	Downloads
    3149	go
    1008	nltk_data
    39	volumes
    4	Pictures
    1	Music
    1	Movies
    1	Documents  
    ```


