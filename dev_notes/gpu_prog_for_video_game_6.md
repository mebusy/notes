# GPU Programming for Video Games, Summer 2020, Georgia Tech

# 6 Backface Culling

- Determin "facing direction"
- Triangle order matters
- How to compute a normal vector for 2 given vectors ?
    - Using **cross product** , depends on LHS/RHS you are actually using.
    - so if you load in the 3d model, and you have back face culling activated in your game engine, and the object disappears, then that probably is a suggestion that there's a different convention (LHS/RHS) being used by the model than what the softward rendering it is expecting it to be.
    - again, the face normal is not the normals exported by the 3d modeling software.


