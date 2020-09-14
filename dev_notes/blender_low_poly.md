...menustart

- [Blender Low Polygon Modeling](#014f19a3d96b43cc1200682c7c2f7a79)
    - [UI](#71ff71526d15db86eb50fcac245d183b)
    - [Mirror](#2403def5083f02105e7802b3b315681e)
    - [Head](#98921133d10fbdb0fb6dbb7b2648befe)
    - [UV](#deaa2adbeb26802ae61609c3f3642d82)
    - [Helm](#152090ff5e9a05ea7e1cf0c248449638)
    - [Mace](#17d2c299e4d02f7b375eec3f057a5b50)
    - [Armature](#03908bf22d3b0082ebc42831dd082b3a)
    - [Paint Weights](#fef75a1d83f32588ac72f338e0ecd077)
    - [Inverse Kinematics](#dfcf9dd022ec7d7f4548e411e3667700)
    - [Animation](#d6b6b668dbca9d4fe774bb654226ebe3)
    - [Attach a weapon](#11c6b8a0ea0ed031c6acb4536ff0f3ca)
    - [Copy Transformation Properties to other weapons](#c577c7dc58bc18f9008d10465b2d268a)

...menuend


<h2 id="014f19a3d96b43cc1200682c7c2f7a79"></h2>


# Blender Low Polygon Modeling 

<h2 id="71ff71526d15db86eb50fcac245d183b"></h2>


## UI

- Move object
    - G + x/y/z or "middle mouse button"
    - S + shift-x means to scale in y-z plane
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
    - ctrl + `num pad +`  grow the selection
        - for example,  选中鞋底的面，然后 一点一点往上增加选中的面, 直至选中完整的鞋子。
- model
    - subdivide: CTRL+R  [ +mouse wheel ]
        - **You will break the ability to do subdivide if you start making triangles**.
    - cut: k 
    - remove doubles:  editor mode, a to select all, then
        - ![](../imgs/blender_model_1.png)
    - inset faces
        - ![](../imgs/blender_model_2.png)

- Cursor
    - shift+s / cursor to seledtion





<h2 id="2403def5083f02105e7802b3b315681e"></h2>


## Mirror

- unselect this 
    - ![](../imgs/blender_mirror.png)
- b  boxing select 
- delete vertex 
    - ![](../imgs/blender_mirror_2.png)
- add Mirror modifier
    - ensure the Clipping is checked
    - ![](../imgs/blender_mirror_3.png)


<h2 id="98921133d10fbdb0fb6dbb7b2648befe"></h2>


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


<h2 id="deaa2adbeb26802ae61609c3f3642d82"></h2>


## UV

1. obj -> edit mode -> shading / UV tab
2. load texture, a to select a , scale the selector to a reasonable size
3. obj -> N to show property panel -> check "Shading/Textured solid"

<h2 id="152090ff5e9a05ea7e1cf0c248449638"></h2>


## Helm 

1. select faces
2. shift-D to duplicate
3. seprate by select ,  to make a separated object

<h2 id="17d2c299e4d02f7b375eec3f057a5b50"></h2>


## Mace

1. cube to create the handle, and then
1. add a Ico sphere for the mace
2. random select face
3. e to extrude , escape,  then scale 
    - ![](../imgs/blender_mice_1.png)
4. how to modle spikes?
    - use individual pivot point 
    - ![](../imgs/blender_mice_3.png)
    - and then scale to 0 to make spikes
    - ![](../imgs/blender_mice_4.png)


<h2 id="03908bf22d3b0082ebc42831dd082b3a"></h2>


## Armature

- check "X-ray" in object panel to see all bone
- 2 bones
    - ctrl P :  connected,  or make offset
        - make offset: ![](../imgs/blender_bone_1.png)
            - note: order of bone added matters
    - alt P : clear parant , or disconnect bone
- symmetrize Armature
    - search `symmetrize`
    - if you named your bone as `xxx.L` , then the symmetrized bone will be names as `xxx.R`
- one thing is very useful to do is 
    - in edit mode, select all bones, and CTRL-N , select 'View axis'
    - ![](../imgs/blender_bone_2.png)
    - if in post mode you animate some bone like this
    - ![](../imgs/blender_bone_3.png)
    - and the select all bone, CTRL-C,  SHIFT-CTRL-V, I can perfectly flip x.
    - ![](../imgs/blender_bone_4.png)
- restore post
    - ALT-G : clear pose location
    - + ALT-R : clear pose rotation
- connect armature and your character
    1. select character (object mode)
    2. shift select bones ( pose mode )
    3. CTRL+P, you can choose "With Automatic Weights".


<h2 id="fef75a1d83f32588ac72f338e0ecd077"></h2>


## Paint Weights

1. pose mode, choose bone
2. select you character, now you are in object mode, change to "Weight Paint"
    - ![](../imgs/blender_bone_5.png)
    - since the character is mirrored, and the bone are symmetric, so we just need do weight changs on half side.


<h2 id="dfcf9dd022ec7d7f4548e411e3667700"></h2>


## Inverse Kinematics

- bone, edit mode, extrude extra bone.
- ALT-P, clear parent, move to this postion
    - ![](../imgs/blender_ik_1.png)
    - this is going to be a bone that the knee is going to be aimed towards at all times
- selec foot bone, SHIFT-A to add a bone , adjust the position
    - ![](../imgs/blender_ik_2.png)
    - ![](../imgs/blender_ik_3.png)
- symmertized control bones
- select lowerLeg bone, add *bone constrait* -- inverse kinematics
    - ![](../imgs/blender_ik_4.png)
    - ![](../imgs/blender_ik_5.png)
    - change chain length to 2
    - ![](../imgs/blender_ik_6.png)
    - set target and pole target
        - ![](../imgs/blender_ik_8.png)
        - target -> Armature , bone -> 脚后跟的控制骨骼
        - pole target -> Armature , bone -> Leg pole 膝盖前方的控制骨骼
    - ![](../imgs/blender_ik_7.png)
- parent the top 2 bone respectively to the bottom FootControl bone
    - ![](../imgs/blender_ik_9.png)
    - there is still a problem, foot bone may detach from the LowerLeg bone
    - ![](../imgs/blender_ik_10.png)
    - so we need to a copy location of foot joint, add constraints *Copy Location*
        - set Target to LowerLeg bone
        - set Bone to LowerLeg
        - set Head/Tail to *Tail*
        - ![](../imgs/blender_ik_11.png)
        - ![](../imgs/blender_ik_12.png)
- move the leg control bone upper , 否则膝盖无法抬得很高
    - ![](../imgs/blender_ik_13.png)


<h2 id="d6b6b668dbca9d4fe774bb654226ebe3"></h2>


## Animation

- In Animation Editor,  select *Action Edtor* Mode
    - ![](../imgs/blender_anim_1.png)
- then click "New" , and name your action
    - this it important you need to click this *F* to save this data-block even if it has no users. So it saves this to the file line. 
    - ![](../imgs/blender_anim_2.png)
- **Insert Key Frames**
    - in Action Editor
        - select all bones, I ,  for all channel
    - in Scene editor
        - I ,  Loc and Rot
        - ![](../imgs/blender_anim_3.png)
        - ![](../imgs/blender_anim_4.png)
- automatically insert key frames
    - ![](../imgs/blender_anim_5.png)
- **Copy/Paste** key frame
    1. in action editor , select a frame line
    2. in pose mode editor, select all bone , CTRL-C
    3. back to action editor, select target frame line
    4. **Back 2 Pose Mode** , CTRL-V
- walk tips
    - for the key frames in 2nd half cycle 
    - select any bones which is recorded in the key frames
    - use CTRL-C / SHIFT-CTRL-V to copy


<h2 id="11c6b8a0ea0ed031c6acb4536ff0f3ca"></h2>


## Attach a weapon

1. select weapon object,  add object constrait *Child Of*
    - ![](../imgs/blender_anim_weapon_1.png)
    - we don't want any scale
2. reset the position of weapon to 0,0,0, and adjust the rotaion
    - may need go back to action editor to adjust the weapon position to perfectly grab it.
    - you'd betten to turn *automatically insert key frame* to off.


<h2 id="c577c7dc58bc18f9008d10465b2d268a"></h2>


## Copy Transformation Properties to other weapons

1. select the object you want to transform
2. shift-select the target object
3. click object tab
4. In transformation, right click the Location X/Y/Z property 
5. in the pop-up list, choose *Copy All To Select*
    - ![](../imgs/blender_prop_copy.png)
6. do the same for rotaion and scale





