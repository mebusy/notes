[](...menustart)

- [Check OSX/Linux Disk Usage](#16309df300bdf0d160ce0d2c3ba81760)
    - [show disk statistics](#43966914cb91fad4e91935063f885044)
    - [Quick find largest files](#738abd9a763d86132b17a478f1a858d4)
    - [dive in deep](#9e34b361cb37f29a1853787b7b35032b)

[](...menuend)


<h2 id="16309df300bdf0d160ce0d2c3ba81760"></h2>

# Check OSX/Linux Disk Usage


<h2 id="43966914cb91fad4e91935063f885044"></h2>

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


<h2 id="738abd9a763d86132b17a478f1a858d4"></h2>

## Quick find largest files

```bash
$ ls -Sl  # -S means Sort by size

drwx------@  3 user  staff    96 Aug 13  2020 Applications
drwx------@ 11 user  staff   352 Oct 14 12:02 Desktop
drwx------@  5 user  staff   160 Oct  7 14:01 Documents
drwx------@ 24 user  staff   768 Oct 18 11:27 Downloads
drwx------@ 91 user  staff  2912 Oct 18 10:35 Library
drwx------+  5 user  staff   160 Aug  1 15:19 Movies
drwx------+  4 user  staff   128 Aug 13  2020 Music
```

<h2 id="9e34b361cb37f29a1853787b7b35032b"></h2>

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


