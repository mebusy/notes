...menustart

- [Inkscape](#f94c773ead613bd434392fcb74685a7e)
    - [Interface and Basic Drawing](#6c546416d94ec089c4686f1ec4c78a2c)
    - [Groups, Levels, and Object Selection](#5c74f7d0a5781996cdcdbd804ba6a0c2)
    - [Text and Fonts](#9ab84a8448ee6c390dc41477b364f2b3)
    - [Drawing Lines and Paths vs Objects](#ad660906612d8b3fef07e54b70d88690)
    - [Bezier Tool and Nodes](#17f95c6bc3b807798b7acdf63a60f391)
    - [Trace Bitmap Tool (Convert Raster to SVG)](#5b982918e0c8628311e23fb170b924db)
    - [12 Difference, Union, Intersection, Combination](#9b4dc60a782520206cbb06586e275a3f)
    - [13 Align and Distribute](#adb66e29613380734e6e61bcdfcdb868)

...menuend


<h2 id="f94c773ead613bd434392fcb74685a7e"></h2>


# Inkscape

<h2 id="6c546416d94ec089c4686f1ec4c78a2c"></h2>


## Interface and Basic Drawing

- move page : 
    - ctrl + right mouse button
    - or hold down middle mouse button
- scale UI:
    - ctrl + mouse whell
- set stroke color
    - shift + pick color
- Note: select & scale a shape will also scale its stroke.
- circle tool
    - style: 1. pacman (outside)  2. half moon (partial circle) (inside)
- select an object which is covered by another object
    - Alt + left-click x 2
    - if then you want drag that object, you must keep holding Alt key


<h2 id="5c74f7d0a5781996cdcdbd804ba6a0c2"></h2>


## Groups, Levels, and Object Selection

- ways to multi-select objects
    1. shift-click to select another object
    2. rect select 
- group objects ( join as one object permanently )
    - first, multi-select objects
    - menu/object/group
- change property of a single object in a group, without ungrouping it
    - double click the group object
    - select a single object
    - edit propery
    - escape ( or select other object that is not in this group)


<h2 id="9ab84a8448ee6c390dc41477b364f2b3"></h2>


## Text and Fonts

- modify positions of some specific characters in a text
    - selet those characters ( line wise by default ) , then hold Alt key  + arrow keys
- more tools
    - menu/Extensions/Text/
        - capitalize, lowercase, uppercase, split ...
    - menu/Text/Put on Path
        - then menu/Path/Object to path , to finalize it. ( you now can remove the object used to path )
    - how to put the text on the path inside a circle  ?
        - Put on Path
        - flip horizontally
        - but the letters are too close, choose the text tool, set the letter space.

<h2 id="ad660906612d8b3fef07e54b70d88690"></h2>


## Drawing Lines and Paths vs Objects

- FreeHand Drawing tool creates path, while tools like rectange, circle creating objects.
- Draw Line
    - Recommended way is to use `Bezier Curve Tools`
- We can convert a object to a path
    - menu/Path/Object to Path
    - We can also add node to path, by double clicking on the path (edge).


<h2 id="17f95c6bc3b807798b7acdf63a60f391"></h2>


## Bezier Tool and Nodes

- Mode: "Creating Regular Bezier Path"
    - single left click to create path with line segment
        - hold on shift-key can drag the handler out from node so as to make curve
            - or left-click(hold) on the line(curve) , to change its shape.
    - when create 2nd, 3rd, ... node, hold left mouse key and move mouse can make curve as well.
    - Choose different "Shape" to get additional effect
- Mode: "Creating Spiro Path"



<h2 id="5b982918e0c8628311e23fb170b924db"></h2>


## Trace Bitmap Tool (Convert Raster to SVG) 

- Path/Trace Bitmap..


<h2 id="9b4dc60a782520206cbb06586e275a3f"></h2>


## 12 Difference, Union, Intersection, Combination

- select both objects,  /path/union
    - it is no longer an object now, it is a path

<h2 id="adb66e29613380734e6e61bcdfcdb868"></h2>


## 13 Align and Distribute

- /Object/Align and Distribute , shift-cmd-A
- distribute:  setting distance between objects

## 14 Spray Tool, Copy, Clone

- how to do
    1. create any object
    2. choose 喷雾工具, draw as you want
- options
    - prevent overlaping objects ( right most icon in tool bar)


## 15 - Using Layers

- CMD-Shift-L , to open layer panel
    - and then , you can add/delete/hierarchy layers

## 16 - Using Filters

- Menu  Filter/


## 17 - Rendering Paths and Objects

- generate random shape
- Menu extension/render 

## 22










