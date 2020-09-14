...menustart

- [dungeon grid:  short\[\]\[\]](#10df90b45c7197ec6a3b41830e711272)
- [8 种 room type](#613d5eda83a93341aa4af1d532915ace)
- [4 种 dungeon Profile](#31c4a6f18acb8397634b67978b7b6398)
- [designRandomRoom](#20ebe4265fa72799ee79717e0be19438)
- [ROOM 构建流程](#bb168d2d6231793ce94f3c1ff263d3f6)

...menuend


<h2 id="10df90b45c7197ec6a3b41830e711272"></h2>


## dungeon grid:  short[][]

CELL VALUE | TYPE
--- | ---
0 | granite
1 | floor
2 | possible door site
-1 | 禁止区域,房间不能放在那里，也不能在那里发芽



<h2 id="613d5eda83a93341aa4af1d532915ace"></h2>


## 8 种 room type 

 INDEX | ROOM KIND | desc
 --- | --- | ---
 0 | Cross room
 1 | Small symmetrical cross room
 2 | Small room
 3 | Circular room | 圆形房间?
 4 | Chunky room  | 
 5 | Cave     
 6 | Cavern (the kind that fills a level)
 7 | Entrance room (the big upside-down T room at the start of depth 1)



<h2 id="31c4a6f18acb8397634b67978b7b6398"></h2>


## 4 种 dungeon Profile

 1. 基本地牢
 2. 基本的 first room 地牢
 3. goblin warren
     - A Goblin Warren is a special area of the dungeon comprised of a complex of small rooms and hallways.
     - Each warren is under the command of a goblin warlord who protects a special reward
 4. SENTINEL SANCTUARY
     - ß

每种 dungeon Profile 属性如下 , 并且随 level deep 发生修改 :

 - 8 种 room type 出现的频率
 - 有走廊的几率


<h2 id="20ebe4265fa72799ee79717e0be19438"></h2>


## designRandomRoom

 - 把一个随机的房间形 放在在网格的某个地方
 - (可选)记录最多4个 门的位置
     - chooseRandomDoorSites
         - 房间的墙，是可能的门的位置，除了墙角
        - 所以，符合这个要求的 tile, 它的上下左右，必然只有 1个 是 floor, 其他都是 花岗岩
        - 检测是否是 可能的门的放置点 的方法 : directionOfDoorSite
        - directionOfDoorSite 返回合法的门朝向后，在这个方向上 检测10个tile, 确保不会和房间本身相交
            - E 形房间 可能出现这个问题
        - 在所有的合法的 门位置上，随机选取4个门，每个方向一个， 保存到 doorSites[dir]

 - (可选)如果 attachHallway is true, 将会在4个标准门站之一 上添加一个垂直的走廊, 
     - 并且从走廊尽头 重新安置3个门
         - 一般来说 ，带走廊的room， 只有走廊尽头 一个门
         - 但是如果允许 Oblique Hallway Exit，可以有最多3个门
 - RoomTypeFrequencies  指定每个房间类型的概率


<h2 id="bb168d2d6231793ce94f3c1ff263d3f6"></h2>


## ROOM 构建流程

 1. 建立 反 T 形的 first room
 2. attach 标准 BASIC room , 最多搭建 35个room，最多尝试 35次
     - 最后5次尝试 不生成走廊
     - room 生成后, 随机测试 主地图的cell，看是否能放下生成的room
 3. 








