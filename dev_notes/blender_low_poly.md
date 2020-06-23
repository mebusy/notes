
# Blender Low Polygon Modeling 

## UI

- Move object
    - G + x/y/z or "middle mouse button"
- Move world
    - middle mouse botton to orbit
    - shift-middle mouse button to pan
    - (blender 2.8) if you don’t have a middle mouse button, use the hand icon in gizzard mode
- (2.8)Focus on selected object 
    - numpad .
    - or  \` + 3  (2.8 ?)
- Search
    - F3 (blender 2.8)
    - space ( 2.79)
- Vew
    - Numpad 1: front
    - Numpad 3: right
    - Numpad 7: top
    - Numpad 5: orthogonal
    - Humpad 9: user view
- select
    - ring edges :  ALT+SHIFT+ select edge
    - circle select: CTRL+ mouse-left draw
    - switch select mode(vertex/edge/face) CTRL+TAB [+1,2,3]
- model
    - subdivide: CTRL+R  [ +mouse wheel ]
        - **You will break the ability to do subdivide if you start making triangles**.
    - cut: k 
    - remove doubles:  editor mode, a to select all, then
        - ![](../imgs/blender_model_1.png)





## Mirror

- unselect this 
    - ![](../imgs/blender_mirror.png)
- b  boxing select 
- delete vertex 
    - ![](../imgs/blender_mirror_2.png)
- add Mirror modifier
    - ensure the Clipping is checked
    - ![](../imgs/blender_mirror_3.png)


## Head 

- Cube + Subdivison surface modifier  (apply it)
- perform "Mirror"
- select the back bottom face, extract it
    - ![](../imgs/blender_head_1.png)
- **Trick** flatten the face: s + z + 0
    - ![](../imgs/blender_head_2.png)
- **Trick** if you select snap to vertices
    - ![](../imgs/blender_head_3.png)
    - I'm gonna make that face square
    - ![](../imgs/blender_head_4.png)
    - g to move a vertex, then hold ctrl,  move vertex along x-axis, and move the cursor the this vertex,  they'll be perfectly aligned now with each other
    - ![](../imgs/blender_head_5.png)
    - do the same for the back nect 1
    - ![](../imgs/blender_head_6.png)
    - same for the front nect vertex, eventuall we got a perfect square.




