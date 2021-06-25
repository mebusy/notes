...menustart

- [Tool:](#1f36ce0c302c8d31f2c4ce8b927047ab)
- [Books](#6225eb5bf8a031f750a1b03f810ccc6a)
- [Tutorial](#368fe771261fcb18f7988833c9294a20)
    - [Tiles and Maps](#40b06c547952c7c5a66dd95a1d9c26f3)
- [Advanced](#9b6545e4cea9b4ad4979d41bb9170e2b)
    - [auto tile](#4d884e87dece8f6dbaa651d1b3a86ace)
    - [dungeon algorithms](#d6df0854ea8dc48b05be348b0271b37d)
    - [tunneling](#7575d40ff70f3d0146669d402ca47579)
    - [random walk](#396c9aa8a56ee3ea6e06423717b340b3)
    - [BSP: Binary Space Partitioning](#fd8334f88acc5ac4a4b89af90ce18c0c)
        - [Building the dungeon](#cf6432b1f365fe43ae2285cf70e002e0)
        - [lighting](#8e0cc612e58bb376328960e92c9b89e8)
        - [Tools](#8625e1de7be14c39b1d14dc03d822497)

...menuend


<h2 id="1f36ce0c302c8d31f2c4ce8b927047ab"></h2>


# Tool: 

Roguelike Dungeon Comparsion

<h2 id="6225eb5bf8a031f750a1b03f810ccc6a"></h2>


# Books 
Procedural Generation in Game Design 
		 Tanya X.Short and Tarn Adams

Game Programming Patterns
	Robert Nystrom 



[network ASCII](http://network-science.de/ascii/)

---

<h2 id="368fe771261fcb18f7988833c9294a20"></h2>


# Tutorial

<h2 id="40b06c547952c7c5a66dd95a1d9c26f3"></h2>


## Tiles and Maps

- tile
    - block path = boolean
    - block sight = boolean
    - type = Sand , Dirt ?

<h2 id="9b6545e4cea9b4ad4979d41bb9170e2b"></h2>


# Advanced 

<h2 id="4d884e87dece8f6dbaa651d1b3a86ace"></h2>


## auto tile

bitmasking tiling : mathematically find out what every single tile is


<h2 id="d6df0854ea8dc48b05be348b0271b37d"></h2>


## dungeon algorithms

- tunneling 
- BSP , 和 tunneling 有点像，但是更好的 填充整个空间
- random walk  一整个cave
- cellular automata   , beautiful cave
- room additon , cave + room
- city building  ,  building + doors
- maze with rooms , complicated corridors
- Messy BSP , sort of mixing  room addition and BSP, i'm not sure

<h2 id="7575d40ff70f3d0146669d402ca47579"></h2>


## tunneling 

- fill entire space with wall 
- randomly try to dig a room 
    - if it intersects with other rooms , skip this room
    - otherwise , place that room 
        - and now it need a tunnel to the other rooms (the previously added one)
        - it always tunnel from its center.

<h2 id="396c9aa8a56ee3ea6e06423717b340b3"></h2>


## random walk

- init whole room with wall 
- start from center of room, set room center as floor
- choose a initial direction
- iteration for some  steps
    - 75% keep direction
    - 25% change direction
    - walk 1 step, set as floor


<h2 id="fd8334f88acc5ac4a4b89af90ce18c0c"></h2>


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


<h2 id="cf6432b1f365fe43ae2285cf70e002e0"></h2>


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



<h2 id="8e0cc612e58bb376328960e92c9b89e8"></h2>


### lighting  

https://indienova.com/indie-game-development/tile-based-line-of-sight-explained/


<h2 id="8625e1de7be14c39b1d14dc03d822497"></h2>


### Tools

[Markov text generation](https://github.com/jsvine/markovify)





