...menustart

 - [Procedual Dungeon by Unity lua , part 1](#43e65c30acbdf24696f10a6f143c27c0)
     - [step 1: Cellular Automata](#3e74269609b1bde9df6bc382ab44e8ca)
     - [step 2: smooth the map](#b8e64cb13c04f49bcd939e396573ba96)
         - [step 3: show it](#d98bd06ab1fed4ab8982111c42278c1e)
     - [step 4: Marching Square](#7baaaa63b8783cbfefac4bc92daca856)
     - [step 4: display the mesh.](#e5320da03725702c294687a92b03dfe1)

...menuend


<h2 id="43e65c30acbdf24696f10a6f143c27c0"></h2>


# Procedual Dungeon by Unity lua , part 1

    PS: All codes are written in Lua, developed on Unity5 with ULua.
    The code is used to explain how the algorithm works, I do not guarantee it can run correctly.
    
    author: golden_slime@hotmail.com    `<Mebusy>`

Ok, lets start to generate a procedural dungeon cave .

<h2 id="3e74269609b1bde9df6bc382ab44e8ca"></h2>


## step 1: Cellular Automata

The algorithm to create the map is called "Cellular Automata".

At first , we will create a 2 dimension map.  

We use number **1 to represent wall** while **0 represent floor**.

The following codes create the map 60 x 40 .

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

![](../imgs/Random_Cave_1.png)

It looks like a black image with many many white noise on it.  

Next we will make it looks like a map.

<h2 id="b8e64cb13c04f49bcd939e396573ba96"></h2>


## step 2: smooth the map

The core algorithm to smooth the map is : 

For each map cell , calculate the wall number within 8 neighbour cells surrounding it . 
If the wall count > 4 then turn the cell into wall(1) ,  
if the wall count < 4 then turn the cell into floor(0). 

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

<h2 id="d98bd06ab1fed4ab8982111c42278c1e"></h2>


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

![](../imgs/Random_Cave_2.png)

Now, it looks much better. 

<h2 id="7baaaa63b8783cbfefac4bc92daca856"></h2>


## step 4: Marching Square

So far , every block has only 2 status: full black or full white.

Let's image that we shrink those blocks towards there in the center.

![](../imgs/marching_square.png)


Now the blocks  was shrinked into those bigger white/black block ,  such that each block actually represents the corner of a square , we call those "Control Node". 


For any square , each corner is one of those function blocks which is acting as a switch : on means it's wall , off means it's not a wall. 

Each of these switches is representing one digit in a 4bit binary number bXXXX .

we also add some  extra  nodes at middle of edge  ( smaller grey one ), called them  "Common Node".

![](../imgs/Random_Cave_2.1.png)

each square actually repersents  the center quarter parts of adjacent 4 map blocks.

Those 8 nodes (4 control nodes + 4 common node) will be used to triangulate the Square.

For more algorithm details , you could check this illustration: **[Demo Marching Square](https://cdn.rawgit.com/mebusy/html5_examples/HEAD/00_marchingSquare.html)**

By clicking those 4 marked control-node , you will see how the triangles were generated.

The following codes are the core algorithm:

Class SquareGrid definition

```lua
local SquareGrid = class("SquareGrid")
function SquareGrid:create(  map,   squareSize )
    local node = SquareGrid:new()

    local nodeCountX = #map 
    local nodeCountY = #map[1]
    local mapWidth = nodeCountX * squareSize;
    local mapHeight = nodeCountY * squareSize;

    local controlNodes = {}
    for x = 1,  nodeCountX do
        controlNodes[x] = {}
        for y = 1, nodeCountY do
            local pos = Vector3( -mapWidth/2 + x * squareSize + squareSize/2, 0, -mapHeight/2 + y * squareSize + squareSize/2) 
            controlNodes[x][y] = Node:create( pos, map[x][y] == 1 )
        end
    end
    
    node.squares ={}
    for x = 1,  nodeCountX-1 do
        node.squares[x] = {}
        for y = 1 ,  nodeCountY-1 do 
            node.squares[x][y] = Square:create( controlNodes[x][y+1], controlNodes[x+1][y+1], controlNodes[x+1][y], controlNodes[x][y])
        end
    end

    return node 
end
```

Class Square definition
```lua
local Square = class("Square")
function Square:create(   _topLeft,   _topRight,   _bottomRight,   _bottomLeft )
    local node = Square:new()

    local control_nodes = { _topLeft,   _topRight,   _bottomRight,   _bottomLeft }  
    local common_nodes = { }

    for i=1, #control_nodes do
        local ctr_node_1 = control_nodes[ i ]
        local ctr_node_2 = control_nodes[ i%4 + 1] 
        common_nodes[i] = Node:create( ( ctr_node_1.position + ctr_node_2.position  )/2 , false )
    end

    for i , v in ipairs( control_nodes ) do
        if v.active then
            common_nodes[i].active = not common_nodes[i].active
            local another_node_index = i-1==0 and 4 or i-1 
            common_nodes[ another_node_index ].active = not common_nodes[ another_node_index ].active
        end
    end
    -------
    node.all_nodes = {}
    for i=1,4 do
        node.all_nodes[i*2-1] = control_nodes[i]
        node.all_nodes[i*2] = common_nodes[i]
    end

    return node 
end
```

Generate triangles for each square

```lua
local function TriangulateSquare(square) 
    local visibleNodes = {}
    for _,v in ipairs( square.all_nodes ) do
        if v.active then
            table.insert( visibleNodes, v  )
        end
    end
    MeshFromPoints( visibleNodes )
end
--======================
squareGrid =  SquareGrid:create( map, squareSize ) 

vertices = {}
triangles = {}

--以 square 为单位，构建 三角形
for x = 1, #squareGrid.squares do
    for y = 1, #squareGrid.squares[1] do
        TriangulateSquare(squareGrid.squares[x][y])
    end --end for x
end --end for y    

```

<h2 id="e5320da03725702c294687a92b03dfe1"></h2>


## step 4: display the mesh.

create a MeshFilter and MeshRenderer to display the mesh

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

![](../imgs/Random_Cave_3.png)

Yeah, pretty cool.

