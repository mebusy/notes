# Procedual Dungeon by Unity lua

    PS: All codes are written in Lua, developed on Unity5.
    The code are used only to explain how the algorithm work, I do not guarantee it can run correctly.
    
    author: golden_slime@hotmail.com    <Mebusy>

Ok, lets start to generate a procedural dungeon cave .

The algorithm to create the map is called "Cellular Automata".

## step 1: create a random map

At first , we create a 2 dimension map. We use number **1 to represent wall** while **0 represent floor**.

The following codes create the map which has a 60x40 dimension.

```lua
local width =  60
local height = 40

local function RandomFillMap()  
	map = {}
    for x = 1 ,  width do
    	map[x] = {}
        for  y = 1 ,  height do 
            if (x == 1 or x == width  or y == 1 or y == height ) then
                map[x][y] = 1
            else 
                map[x][y] = (math.random() < 0.45) and 1 or 0 
            end
        end
    end
end
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Random_Cave_1.png)

The map is still very rough , just like a black image with many many white noise on it.  

Next we will make it smooth .

## step 2: smooth the map

The core algorithm to smooth the map is : 

For each map cell , calculate the wall number within 8 neighbour cells surrounding it . If the wall count > 4 then turn the cell into wall(1) , if the wall count < 4 then turn the cell into floor(0). 

Repeat 4-5 times.

```lua
local function SmoothMap()  
	for x = 1 ,  width do
        for  y = 1 ,  height do 
            local neighbourWallTiles = GetSurroundingWallCount(x,y)
            if (neighbourWallTiles > 4) then
                map[x][y] = 1
            elseif (neighbourWallTiles < 4) then
                map[x][y] = 0
            end
        end
    end
end
```

### step 3: show it
Ok, we almost done it. Let's show the map on gizmos and check it.

```lua
function OnDrawGizmos()
    local Gizmos = UnityEngine.Gizmos
    if map then
        for x = 1 ,  width do
            for  y = 1 ,  height do 
                Gizmos.color = (map[x][y] == 1) and Color.black or Color.white
                local  pos = Vector3(-width/2 + x + 0.5, 0 , -height/2 + y+ 0.5 )
                Gizmos.DrawCube(pos,Vector3.one)      
            end
        end
    end -- end map
end
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Random_Cave_2.png)

Now, it looks much better. 

## step 4: Marching Square

Let's image that we shink the map cell . Every 4 cells form a square , we call those square vertexes "Control Node" while call the nodes at middle of edge "Common Node".

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Random_Cave_2.1.png)

Those 8 nodes (4 control nodes + 4 common node) will be used to triangulate the Square.

```lua
--contruct triangles according to control node config
local function TriangulateSquare(square) 
    --0 no triangle

    --1 control node
    if square.configuration == 1 then
        MeshFromPoints(square.centreLeft ,square.centreBottom, square.bottomLeft )
    elseif square.configuration == 2 then
        MeshFromPoints(square.bottomRight, square.centreBottom , square.centreRight )
    elseif square.configuration == 4 then
        MeshFromPoints(square.topRight, square.centreRight , square.centreTop )
    elseif square.configuration == 8 then
        MeshFromPoints(square.topLeft, square.centreTop, square.centreLeft)

    --2 control node
    elseif square.configuration == 3 then
        MeshFromPoints(square.centreRight, square.bottomRight, square.bottomLeft, square.centreLeft)
    elseif square.configuration == 6 then
        MeshFromPoints(square.centreTop, square.topRight, square.bottomRight, square.centreBottom)
    elseif square.configuration == 9 then
        MeshFromPoints(square.topLeft, square.centreTop, square.centreBottom, square.bottomLeft)
    elseif square.configuration == 12 then
        MeshFromPoints(square.topLeft, square.topRight, square.centreRight, square.centreLeft) 


    elseif square.configuration == 5 then
        MeshFromPoints(square.centreTop, square.topRight, square.centreRight, square.centreBottom, square.bottomLeft, square.centreLeft)
    elseif square.configuration == 10 then
        MeshFromPoints(square.topLeft, square.centreTop, square.centreRight, square.bottomRight, square.centreBottom, square.centreLeft)

    --3 control node            
    elseif square.configuration == 7 then
        MeshFromPoints(square.centreTop, square.topRight, square.bottomRight, square.bottomLeft, square.centreLeft)
    elseif square.configuration == 11 then
        MeshFromPoints(square.topLeft, square.centreTop, square.centreRight, square.bottomRight, square.bottomLeft)
    elseif square.configuration == 13 then
        MeshFromPoints(square.topLeft, square.topRight, square.centreRight, square.centreBottom, square.bottomLeft)
    elseif square.configuration == 14 then
        MeshFromPoints(square.topLeft, square.topRight, square.bottomRight, square.centreBottom, square.centreLeft)

    --4 control node    
    elseif square.configuration == 15 then
        MeshFromPoints(square.topLeft, square.topRight, square.bottomRight, square.bottomLeft)
    end

end
```

#### create a gameobject to display the mesh.

```lua
    local objMapGenerator = GameObject.Find("objMapGenerator")    
    if not objMapGenerator then
        objMapGenerator = GameObject("objMapGenerator")
        
        --create a meshfilter , then apply it to gameobject
        local mfilter = objMapGenerator:AddComponent( MeshFilter.GetClassType() )
        --create a MeshRenderer
        local mrder = objMapGenerator:AddComponent( MeshRenderer.GetClassType() )
        --fetch the material, if its not assigned, 
        --unity will use a default material instance
        local material = mrder.material
        --set material color
        material.color = Color.black
    end
    
    --create new mesh
    local mesh = UnityEngine.Mesh()
    mesh.vertices = vertices
    mesh.triangles = triangles
    mesh:RecalculateNormals()
    --apply the mesh to MeshFilter component
    local mfilter = objMapGenerator:GetComponent( MeshFilter.GetClassType() )
    mfilter.mesh = mesh 
    --]]
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Random_Cave_3.png)

Yeah, pretty cool.

