

## dungeon grid:  short[][]

CELL VALUE | TYPE
--- | ---
0 | granite
1 | floor
2 | possible door site
-1 | 禁止区域,房间不能放在那里，也不能在那里发芽



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


## designRandomRoom

 - 把一个随机的房间形 放在在网格的某个地方
 - (可选)记录最多4个 门的位置
 - (可选)如果 attachHallway is true, 将会在4个标准门站之一 上添加一个垂直的走廊, 
 	- 并且从走廊尽头 重新安置3个门
 - RoomTypeFrequencies  指定每个房间类型的概率






