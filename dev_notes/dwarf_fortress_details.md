...menustart

- [path finding](#940dbcc8bedbede96c767701b4b9e4d1)
- [The World Generator](#306914f8c24cdc1289fef8a48fef588a)

...menuend


<h2 id="940dbcc8bedbede96c767701b4b9e4d1"></h2>


# path finding

- Q: Sometimes in commercial projects the developers do a bit of cheating, and predefine travel paths.
- A: Yeah, that's the hard part.
    - We can't really predefine areas beyond very basic notions because fluids can zip by and block them off, or they can mine a floor out.

<h2 id="306914f8c24cdc1289fef8a48fef588a"></h2>


# The World Generator

- The first overall goal of the world generator is to create enough information to produce a basic biome display
- A lot of initial attempts at a world generator will start with things like "I need to lay down some forests, and some mountains, and some rivers, and some deserts..." and then when you end up with a jungle next to a desert, or a desert next to a swamp in an unlikely way, it's difficult to fix.
- So the idea is to go down to basic elements. 
- The biomes are not the basics, they arise, at least in DF, from several factors: temperature, rainfall, elevation 海拔, drainage 排水？.
- First, it uses [midpoint displacement](http://www.gameprogrammer.com/fractal.html) to make an elevation map. 
- It also makes a temperature map (biased by elevation and latitude) 
- and a rainfall map (which it later biases with orographic precipitation 地形降水, rain shadows, that sort of thing). 
-  The drainage map is just another fractal, with values from 0 to 100. So we can now query a square and get rainfall, temp, elevation and drainage data.
- This is where the biome comes from. 
- There's an additional vegetation field so it can alter the amount (from logging for example), and there's also a "savagery" and a "good/evil" field. 
- So for instance, if rainfall is >=66/100 and drainage is less than 50, then you have a swamp.
- The nice thing about having the fractally-generated basic fields is that the biome boundaries all look natural. 
    - Part of the trick was to differentiate things like swamps and forests. 
    - There's also a salinity field, to differentiate fresh and saltwater marshes, etc
- Just lots of basic information, so you don't try to shoehorn anything into place. Just let it happen and these fields can all potentially be altered.

---

- You still get some artifacts from the midpoint displacement. It tends to like vertical and horizontal lines, so the next step is the erosion phase.
    - It picks out the bases of the mountains (mountains are all squares above a given elevation), then it runs temporary river paths out from there, preferring the lowest elevation and digging away at a square if it can't find a lower one, until it get to the ocean or gets stuck. 
    - This is the phase where you see the mountain being worn away during world creation. I have it intentionally center on a mountain at that point so you can watch. 
- This will generally leave some good channels to the ocean, so it runs the real rivers after this. 
    - However, some of them don't make it, so it forces paths to the ocean after that, and bulges out some lakes. T
- Then it loop-erases the rivers, and sends out (invisible on the world map) brooks out from them.
- During the loop-erase it also calculates flow amounts and decides which rivers are tributaries, and names the rivers.
- This gives us a world with biome data and rivers, but no actual life. 
- So now it actually looks at the general biome groups of each square (what I call a region type) and forms regions, giving them names.
    - So you can have the "Silvery Forest" which is taiga in the cold regions and a jungle in the warm region, as long as it is connected.
- At this point, it looks at the biomes available in each region and sets up plant and animal populations. This gives you a canvas for world history.

---

- Yeah, I'd like to do more with ranges for animals, so that it's not so scattered. 
- So that many of the northern forests have certain critters, and many of the western forests have others to kind of set up more of a geographical image. 
- Right now, it goes strictly by biome type. It also sets up all the seed information around this time. There are some additional structures it sets up, for features like cave rivers and so on. 
- So it could set up a non-local feature like a world-wide cave tunnel like this.
- It wouldn't be so complicated to have the computer generate the races itself, though the lack of familiarity could be jarring. *Armok*  did this.

--- 

the idea of there being unknown species to discover though

---

Fluid dynamics is one of those features that, to look at it, one can't help but wonder, how on earth did he do that? I think the answer to that question would be of great interest to the authors of falling sand game clones.

Ed's note: We're talking about the most recent versions of Dwarf Fortress, that use a three-dimensioned cellular automation system to manipulate water, much like a multi-plane version of falling sand. In it, each space is a cube that can contain from 0 to 7 levels of water. A "1" is the smallest amount of water possible in the game, and a "7" space is full of water.)

It's really not that complicated, just a specialized cellular automata.

Pressure is the thing I'm personally interested in seeing explained.

- The main problem was at waterfalls. The water would fall on to the river below, and just start clumping, forming a pyramid. This is because of the local behavior. It can't go down, so it goes over.
- ![](http://www.gamasutra.com/db_area/images/feature/3549/ilus2.jpg)
- ![](http://www.gamasutra.com/db_area/images/feature/3549/ilus3.jpg)
- ![](http://www.gamasutra.com/db_area/images/feature/3549/ilus4.jpg)



