# Tool: 

Roguelike Dungeon Comparsion

# Books 
Procedural Generation in Game Design 
		 Tanya X.Short and Tarn Adams

Game Programming Patterns
	Robert Nystrom 



[network ASCII](http://network-science.de/ascii/)

---

# Tutorial

## Tiles and Maps

 - tile
    - block path = boolean
    - block sight = boolean
    - type = Sand , Dirt ?

# Advanced 

## auto tile

bitmasking tiling : mathematically find out what every single tile is


## random walk

 - init whole room with wall 
 - start from center of room, set room center as floor
 - choose a initial direction
 - iteration for some  steps
    - 75% keep direction
    - 25% change direction
    - walk 1 step, set as floor


## BSP: Binary Space Partitioning 

http://roguecentral.org/doryen/articles/bsp-dungeon-generation/

 - We start with a rectangular dungeon filled with wall cells.
 - We are going to split this dungeon recursively until each sub-dungeon has approximately the size of a room.
 - The dungeon splitting uses this operation :
    - choose a random direction : horizontal or vertical splitting
    - choose a random position (x for vertical, y for horizontal)
    - split the dungeon into two sub-dungeons ( to all existing rooms )
 - When choosing the splitting position, we have to take care not to be too close to the dungeon border. 
    - for example, we would say all right for every room , choose a spot from 30% to 70% in percentage and make the cut there 


![](http://roguecentral.org/doryen/data/articles/dungeon_bsp1-medium.jpg)

![](http://roguecentral.org/doryen/data/articles/dungeon_bsp2-medium.jpg)

 - i.e. After 4 splitting iterations 

![](http://roguecentral.org/doryen/data/articles/dungeon_bsp3-medium.jpg)


### Building the dungeon

 - Now we create a room with random size in each leaf of the tree.
 - To build corridors, we loop through all the leafs of the tree, connecting each leaf in bottom level of tree to **its sister.**
    - If the two rooms have face-to-face walls, we can use a straight corridor. 
    - Else we have to use a Z shaped corridor.
 
![](http://roguecentral.org/doryen/data/articles/dungeon_bsp5-medium.jpg)

> Connecting the level 4 sub-dungeons

 - Now we get up one level in the tree and repeat the process for the father sub-regions. 
    - Now, we can connect two sub-regions with a link either between two rooms, or a corridor and a room or two corridors.

![](http://roguecentral.org/doryen/data/articles/dungeon_bsp6-medium.jpg)

> Connecting the level 3 sub-dungeons


 - We repeat the process until we have connected the first two sub-dungeons A and B :

![](http://roguecentral.org/doryen/data/articles/dungeon_bsp7-medium.jpg)






