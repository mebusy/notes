
# Procedural level design in Brogue and beyond

## Create a Room

- A bunch of different ways to create a room
    - Overlapping rectangles
        - you just come up with 2 rectangles, and you place them on top of each other, maybe symmetrically maybe not.
    - Cellular automata blob
        - you take a grid of cells, you fill it randomly, each one maybe 50% chance of being wall or floor, and then any floor that's surrounded by a majority of walls becomes a wall, and vice versa.
        - you can play with the thresholds to get different levels of density and smoothness, but it kind of causes sort of coherent organic shapes to kind of merge from the static that you start with.
    - Big circle
    - Multiple overlaid smaller circles
    - Sometimes with hallway

- ![](../imgs/pcg_brogue_1.png)
    - these green cells it picks out some door candidates from each direction for each room and that's basically how it comes up with rooms. 


## Room Accretion

- Start with a room
- Add another room to it
- Repeat until level is full

So it starts by placing one room randomly and then it just starts generating rooms sometimes with hallways, sometimes not,  and it scans through all the locations on the level one at a time in random order until it finds one where the room fits snugly against another room where the door links it up and where it doesn;t overlap any other rooms.

- ![](../imgs/pcg_brogue_2.png)
    - add rooms

So that's like the basic practice to come up with the skeleton level design. There is a fatal flaw to it which is that it's like a perfect tree. Each room has exactly one parent (except the first room which has no parents) and any number of children. Which means that if you pick any 2 points on that level, there's exactly one path that doesn't backtrack to get between those 2 points. It looks nice on a screen but it's  not that fun because it's easy to get cornered, it causes a lot of backtracking when you play it.

So the next step is we basically go through again in random order and find wall tiles that have a floor on each of the 2 opposite sides, and if the pathing distance between those 2 floor tiles is large enough then we just turn it into a **door**.  And you just do that until you've found all the candidates.

- ![](../imgs/pcg_brogue_3.png)
    - add secondary connections

It looks like this when you carve it into the game assets, 

- ![](../imgs/pcg_brogue_4.png)

If you play this kind of a level, the rooms are interesting in terms of their shape and connectivity but they're all kind of samey like it's amazing to see passages. I thinks it's cool to give a level kind of a coherent global scale to the features where you can see across the level, you can affect things that aren't just in your local vicinity, things can affect you and when they're not in your local vicinity. And sometimes you can see like secret doors on the other side of the level but not necessarily know how to get to them. So to accomplish that we put in lakes.

- ![](../imgs/pcg_brogue_5.png)

And these are again just cellular automata blobs that we create and then again find all the different places on the level where they could be placed, and only place it if it doesn't block the level. And by that I mean "it blocks the level" if you put it somewhere and that makes any pair of walkable tiles inaccessible to one another. So we just scan through kind of brute force see if it blocks, and if not ou just place it. Let them overlap and then kind of assign media type afterward.

- ![](../imgs/pcg_brogue_6.png)



