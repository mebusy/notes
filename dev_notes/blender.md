...menustart

- [API](#db974238714ca8de634a7ce1d083a14f)
    - [2 The bpy Module](#b8836758104839a89ea645e997c6f8cb)
        - [Selection, Activation, and Specification](#f1189fbbb6cb319df8b3a5ad5b3faaef)
        - [Pseudo-Circular Referencing and Abstraction](#aae5d1dbc8e73ac2f63b54ea0689e13a)
        - [Transformations with bpy](#8b118df4b9feadc9623a9631a0a28cd9)
        - [Visualizing Multivariate Data with the Minimal Toolkit](#a19e15baa68da51e5410e5ccbfeab6c8)
    - [3 The bmesh Module](#2ff9402531c1c81679616dd97d7ffebd)
        - [Edit Mode](#23ff99157dafd3dae7a102d9962633d0)
        - [Selecting Vertices, Edges, and Planes](#937ef209bdb65d8a0c0e8115d91d6163)
        - [Edit Mode Transformations](#21663d15cd5189b65dfe739436734241)
        - [Note on Indexing and Cross-Compatibility](#6f2549eaa05b0785e4a601dc699c6713)
        - [Global and Local Coordinates](#7b2e81f38f3bd2a976241c54eba419f6)
        - [Selecting Vertices, Edges, and Faces by Location](#b0e5d5ae447a82512beebd3541059216)
        - [Checkpoint and Examples](#999a8926e65d99669139ce8008f96928)
    - [4 Topics in Modeling and Rendering](#1344c95436d6a0d0776ad7223043de0f)
        - [Specifying a 3D Model](#c5aef292e11961f2493f084ee2dc220e)
        - [Common File Formats](#e6a63b58cf42997d218a6fb856cb4a1f)
        - [Minimal Specification of Basic Objects](#fa11cb7e3dbec33afd8b0c8194461c6a)
        - [Common Errors in Procedural Generation](#a1d35d6a2aa25a58ffb4a9380be01bd7)
    - [5 Introduction to Add-On Development](#a21021ed4077220d8ee7a7b1af522450)
        - [A Simple Add-On Template](#0c04eb9875bdfd13027dc08199c22c17)
        - [Components of Blender Add-Ons](#0f5b9e16e0b4087f80a42c079e0a9b0a)
    - [6 The bgl and blf Modules](#f28b2e33b807755dbe782179fdfc963d)
        - [Instantaneous Drawing](#e6878da0a2f708ad2a8ce73b2a4acb33)
        - [Handlers Overview](#629dc07d3baa953d521a2ad76c0b27a7)
    - [7 Advanced Add-On Development](#a810cbc3a6b48acd8619759085c02700)
    - [8 Textures and Rendering](#c536c9f406f7dcd6d1ea8c650091066f)
        - [Vocabulary of Textures](#1e8b0c856db239dd8faf78f4d33f616a)
        - [Adding and Configuring Textures](#afd66c77848678b6a7739a9cd7b1d0a8)
        - [Removing Unused Textures and Materials](#a502b860b196506a8403c1a490c8ecbe)
        - [Rendering Using Blender Render](#a8b825472bcda46b7a889fa2e79ea33e)

...menuend


<h2 id="db974238714ca8de634a7ce1d083a14f"></h2>


# API

- `http://www.blender.org/api`
- `http://www.blender.org/api/blender_python_api_2_78c_release`
- [command line arguments](https://docs.blender.org/manual/en/dev/advanced/command_line/arguments.html)
    ```bash
    # run script
    blender --background --python myscript.py
    # rendering from the cli without a script
    blender -b mymodel.blend --render-frame 1
    # or render an animation
    blender -b mymodel.blend --frame-start 1 --frame-end 100 --render-anim
    # use blenders built-in python console
    blender -b --python-console
    ```

<h2 id="b8836758104839a89ea645e997c6f8cb"></h2>


## 2 The bpy Module

- bpy.ops:  primarily functions for manipulating objects
    - bpy.ops.object: manipulating multiple selected objects at the same time
    - bpy.ops.mesh: manipulating vertices, edges, and faces of objects one at a time, typically in Edit Mode

```
Note: To accesse directly by appending the Pythonic path to the object and .html
e.g.
www.blender.org/api/blender_python_ api_2_78c_release/bpy.ops.mesh.html
```

- bpy.context:  access objects and areas access objects and areas
    - give Python developers a means of accessing the *current* data that a user is working with
    - bpy.context.object: last selected object
    - bpy.context.select_objects
    - bpy.context.scene
- bpy.data: access Blender’s internal data
    - bpy.data.objects 
        - bpy.context will generate references to datablocks of the bpy.data
- bpy.app
    - The handlers submodule contains special functions for triggering custom functions in response to events in Blender
- bpy.types, bpy.utils, and bpy.props
- bpy.path: essentially the same as the os.path submodule that ships natively with Python
    
<h2 id="f1189fbbb6cb319df8b3a5ad5b3faaef"></h2>


### Selection, Activation, and Specification

- Selection: One, many, or zero objects can be selected at once.
    - `bpy.context.selected_objects`
    - `[k.name for k in bpy.context.selected_objects]`
    - `[k.location for k in bpy.context.selected_objects]`
- Activation: Only a single object can be active at any given time ( Editor mode ?)
- Specification: (Python only) Python scripts can access objects by their names and write directly to their datablocks.


```python
# 2-3 creates a function that takes an object name as an argument and selects it, 
# clearing all other selections by default. 
# If the user specifies additive = True, 
# the function will not clear other selections beforehand.

import bpy
def mySelector(objName, additive=False):
    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')
    # Set the 'select' property of the datablock to True
    bpy.data.objects[objName].select = True


# Select only 'Cube'
mySelector('Cube')

# Select 'Sphere', keeping other selections 
mySelector('Sphere', additive=True)

# Translate selected objects 1 unit along the x-axis
bpy.ops.transform.translate(value=(1, 0, 0))
```


Listing 2-4. Accessing the Active Object

```python

bject
bpy.data.objects['Cube']

>>> bpy.context.active_object
bpy.data.objects['Cube']
```    


Listing 2-5. Programmatically Activating an Object

```python
import bpy
def myActivator(objName):
    # Pass bpy.data.objects datablock to scene class
    bpy.context.scene.objects.active = bpy.data.objects[objName]

# Activate the object named 'Sphere' 
myActivator('Sphere')

# Verify the 'Sphere' was activated 
print("Active object:", bpy.context.object.name)

# Selected objects were unaffected
print("Selected objects:", bpy.context.selected_objects)
```

---

**Specifying an Object (Accessing by Name)**

Listing 2-6. Accessing an Object by Specification

```python
# bpy.data.objects datablock for an object named 'Cube'
bpy.data.objects['Cube']
```

Listing 2-7. Programmatically Accessing an Object by Specification

```python
def mySpecifier(objName):
    # Return the datablock
    return bpy.data.objects[objName]
```

---

<h2 id="aae5d1dbc8e73ac2f63b54ea0689e13a"></h2>


### Pseudo-Circular Referencing and Abstraction

- bpy.data.objects datablocks were built to nest infinitely

```python
# Each line will return the same object type and memory address
bpy.data
bpy.data.objects.data
bpy.data.objects.data.objects.data
bpy.data.objects.data.objects.data.objects.data

# References to the same object can be made across datablock types
bpy.data.meshes.data
bpy.data.meshes.data.objects.data
bpy.data.meshes.data.objects.data.scenes.data.worlds.data.materials.data

# Different types of datablocks also nest
# Each of these lines returns the bpy.data.meshes datablock for 'Cube'
bpy.data.meshes['Cube']
bpy.data.objects['Cube'].data 
bpy.data.objects['Cube'].data.vertices.data 
bpy.data.objects['Cube'].data.vertices.data.edges.data.materials.data
```

- showcases a powerful feature of the Blender Python API.
- **When we append .data to an object, it returns a reference to the parent datablock**

<h2 id="8b118df4b9feadc9623a9631a0a28cd9"></h2>


### Transformations with bpy

- bpy.ops.transorm

Listing 2-9. Minimal Toolkit for Creation and Transformation (ut.py)

[ut.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/ut.py)

<h2 id="a19e15baa68da51e5410e5ccbfeab6c8"></h2>


### Visualizing Multivariate Data with the Minimal Toolkit

Visualizing 3/4 Dimensions of Data 

[visualize3d.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/visualize3d.py)

- for 4th Dimension , we use scale to represent it
- for 5th Dimension, we can use different shapes

---

<h2 id="2ff9402531c1c81679616dd97d7ffebd"></h2>


## 3 The bmesh Module

<h2 id="23ff99157dafd3dae7a102d9962633d0"></h2>


### Edit Mode

Listing 3-1. Switching Between Object and Edit Mode

```python
# Set mode to Edit Mode
bpy.ops.object.mode_set(mode="EDIT")

# Set mode to Object Mode
bpy.ops.object.mode_set(mode="OBJECT")

```

<h2 id="937ef209bdb65d8a0c0e8115d91d6163"></h2>


### Selecting Vertices, Edges, and Planes

**Switching Between Edit and Object Modes Consistently**

Listing 3-2. Wrapper Function for Switching Between Object and Edit Mode

```python
# Function for entering Edit Mode with no vertices selected,
# or entering Object Mode with no additional processes

def mode(mode_name): 
    bpy.ops.object.mode_set(mode=mode_name) 
    if mode_name == "EDIT":
        bpy.ops.mesh.select_all(action="DESELECT")
```


**reload python module**

```python
# python 3
import ut
import importlib
importlib.reload(ut)
```

**Instantiating a bmesh Object**

- In general, instantiating a bmesh object requires us to pass a bpy.data.meshes datablock to bmesh.from_edit_mesh() while in Edit Mode.


Listing 3-4. Instantiating a bmesh Object 

```python
import bpy
import bmesh

# Must start in object mode
# Script will fail if scene is empty 
bpy.ops.object.mode_set(mode='OBJECT') 
bpy.ops.object.select_all(action='SELECT') 
bpy.ops.object.delete()

# Create a cube and enter Edit Mode
bpy.ops.mesh.primitive_cube_add(radius=1, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')

# Store a reference to the mesh datablock
mesh_datablock = bpy.context.object.data

# Create the bmesh object (named bm) to operate on
bm = bmesh.from_edit_mesh(mesh_datablock)

# Print the bmesh object
print(bm)

<BMesh(0x10b2f5a08), totvert=8, totedge=12, totface=6, totloop=24>
```

**Selecting Parts of a 3D Object**

- BMesh.verts 
- BMesh.edges 
- BMesh.faces

- Notice the numerous calls to  ensure_lookup_table()
    - these functions to remind Blender to keep certain parts of the BMesh object from being garbage-collected between operations

Listing 3-5. Selecting Parts of 3D Objects

```python
# Set to "Face Mode" for easier visualization
bpy.ops.mesh.select_mode(type = "FACE")

# Register bmesh object and select various parts
bm = bmesh.from_edit_mesh(bpy.context.object.data)

# Deselect all verts, edges, faces
bpy.ops.mesh.select_all(action="DESELECT")

# Select a face
bm.faces.ensure_lookup_table()
bm.faces[0].select = True

# Select an edge
bm.edges.ensure_lookup_table()
bm.edges[7].select = True

# Select a vertex
bm.verts.ensure_lookup_table()
bm.verts[5].select = True
```

<h2 id="21663d15cd5189b65dfe739436734241"></h2>


### Edit Mode Transformations

**Basic Transformations**

- Conveniently enough, we can use the same functions we used for Object Mode transformations to operate on individual parts of a 3D object

```python
# Must start in object mode
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube and rotate a face around the y-axis
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(-3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

# above is all same as Object mode

# Set to face mode for transformations
bpy.ops.mesh.select_mode(type = "FACE")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
bm.faces[1].select = True
bpy.ops.transform.rotate(value = 0.3, axis = (0, 1, 0))

bpy.ops.object.mode_set(mode='OBJECT')

# Create a cube and pull an edge along the y-axis
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.edges.ensure_lookup_table()
bm.edges[4].select = True
bpy.ops.transform.translate(value = (0, 0.5, 0))

bpy.ops.object.mode_set(mode='OBJECT')

# Create a cube and pull a vertex 1 unit
# along the y and z axes
# Create a cube and pull an edge along the y-axis 
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(3, 0, 0)) 
bpy.ops.object.mode_set(mode='EDIT') 
bpy.ops.mesh.select_all(action="DESELECT")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.verts.ensure_lookup_table()
bm.verts[3].select = True
bpy.ops.transform.translate(value = (0, 1, 1))
bpy.ops.object.mode_set(mode='OBJECT')
```

**Advanced Transformations** 

Listing 3-7. Extrude, Subdivide, and Randomize Operators

```python
...
# Set to face mode for transformations
bpy.ops.mesh.select_mode(type = "FACE")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
bm.faces[5].select = True
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate =
{"value": (0.3, 0.3, 0.3), "constraint_axis": (True, True, True), "constraint_orientation" :'NORMAL'})

bpy.ops.object.mode_set(mode='OBJECT')

# Create a cube and subdivide the top face
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
bm.faces[5].select = True
bpy.ops.mesh.subdivide(number_cuts = 1)

bpy.ops.mesh.select_all(action="DESELECT")
bm.faces.ensure_lookup_table()
bm.faces[5].select = True
bm.faces[7].select = True
bpy.ops.transform.translate(value = (0, 0, 0.5))

bpy.ops.object.mode_set(mode='OBJECT')

# Create a cube and add a random offset to each vertex
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.transform.vertex_random(offset = 0.5)

bpy.ops.object.mode_set(mode='OBJECT')
```

<h2 id="6f2549eaa05b0785e4a601dc699c6713"></h2>


### Note on Indexing and Cross-Compatibility

- 使用硬编码数字下标 访问 vertex, edge , face 会导致 预期外的结果
- 不同版本的blender 的相同的操作，索引会有差异

<h2 id="7b2e81f38f3bd2a976241c54eba419f6"></h2>


### Global and Local Coordinates

- Within the 3D Viewport, we view global coordinates G = T * L always.
- We can control when Blender applies transformations with bpy.ops.object.transform_apply()
- This will not change the appearance of the objects, rather it will set L equal to G and set T equal to the identity
- If we delay execution of bpy. ops.object.transform_apply() by not running it and not exiting Edit Mode, we can maintain two data sets G and L
    - In practice, G is very useful for positioning objects relative to others
    - and L is very easy to loop through to fetch indices.
- We will build mode-independent functions for accessing these coordinates

Listing 3-8. Fetching Global and Local Coordinates

```python
def coords(objName, space='GLOBAL'):
    # Store reference to the bpy.data.objects datablock
    obj = bpy.data.objects[objName]

    # Store reference to bpy.data.objects[].meshes datablock
    if obj.mode == 'EDIT':
        v = bmesh.from_edit_mesh(obj.data).verts
    elif obj.mode == 'OBJECT': 
        v = obj.data.vertices
        
    if space == 'GLOBAL':
        # Return T * L as list of tuples
        return [(obj.matrix_world * v.co).to_tuple() for v in v]
    elif space == 'LOCAL':
        # Return L as list of tuples
        return [v.co.to_tuple() for v in v]
    
class sel:
    # Add this to the ut.sel class, for use in object mode
    def transform_apply(): 
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

```

Listing 3-9. Behavior of Global and Local Coordinates and Transform Apply

- After translating the cube, readers will see the cube move, but the local coordinates will remain the same.
- After running transform_apply(), the cube will not move, but the local coordinates will update to match the global coordinates.


```python
############################ Output ###########################
# Before transform:
# Global: [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
# Local: [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
#
# After transform, unapplied:
# Global: [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
# Local: [(-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)]
#
# After transform, applied:
# Global: [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
# Local: [(2.5, 2.5, 2.5), (2.5, 2.5, 3.5)]
###############################################################
```

<h2 id="b0e5d5ae447a82512beebd3541059216"></h2>


### Selecting Vertices, Edges, and Faces by Location

Listing 3-10. Function for Selecting Pieces of Objects by Location

```python
# Add in body of script, outside any class declarations
def in_bbox(lbound, ubound, v, buffer=0.0001):
    return lbound[0] - buffer <= v[0] <= ubound[0] + buffer and \
        lbound[1] - buffer <= v[1] <= ubound[1] + buffer and \
        lbound[2] - buffer <= v[2] <= ubound[2] + buffer
class act:
    # Add to ut.act class
    def select_by_loc(lbound=(0, 0, 0), ubound=(0, 0, 0), select_mode='VERT', coords='GLOBAL'):
        # Set selection mode, VERT, EDGE, or FACE
        selection_mode(select_mode)
        
        # Grab the transformation matrix
        world = bpy.context.object.matrix_world

        # Instantiate a bmesh object and ensure lookup table
        # Running bm.faces.ensure_lookup_table() works for all parts 
        bm = bmesh.from_edit_mesh(bpy.context.object.data) 
        bm.faces.ensure_lookup_table()
        
        # Initialize list of vertices and list of parts to be selected
        verts = []
        to_select = []

        # For VERT, EDGE, or FACE ...
        # 1. Grab list of global or local coordinates
        # 2. Test if the piece is entirely within the rectangular
        #    prism defined by lbound and ubound
        # 3. Select each piece that returned True and deselect
        #    each piece that returned False in Step 2
        
        if select_mode == 'VERT': 
            if coords == 'GLOBAL':
                [verts.append((world * v.co).to_tuple()) for v in bm.verts] 
            elif coords == 'LOCAL':
                [verts.append(v.co.to_tuple()) for v in bm.verts]

            [to_select.append(in_bbox(lbound, ubound, v)) for v in verts] 
            for vertObj, select in zip(bm.verts, to_select):
                vertObj.select = select

        if select_mode == 'EDGE': 
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple() for v in e.verts]) for e in bm.edges]
            elif coords == 'LOCAL': 
                [verts.append([v.co.to_tuple() for v in e.verts]) for e in bm.edges]

            [to_select.append(all(in_bbox(lbound, ubound, v) for v in e)) for e in verts]
            for edgeObj, select in zip(bm.edges, to_select): 
                edgeObj.select = select

        if select_mode == 'FACE': 
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple() for v in f.verts]) for f in bm.faces]
            elif coords == 'LOCAL': 
                [verts.append([v.co.to_tuple() for v in f.verts]) for f in bm.faces]

            [to_select.append(all(in_bbox(lbound, ubound, v) for v in f)) for f in verts]
            for faceObj, select in zip(bm.faces, to_select): 
                faceObj.select = select

```

Example:

```python
# Selects upper right quadrant of sphere
ut.act.select_by_loc((0, 0, 0), (1, 1, 1), 'VERT', 'LOCAL')

# Selects nothing
ut.act.select_by_loc((0, 0, 0), (1, 1, 1), 'VERT', 'GLOBAL')

# Selects upper right quadrant of sphere
ut.act.select_by_loc((0, 0, 0), (5, 5, 5), 'VERT', 'LOCAL')

# Mess with it
bpy.ops.transform.translate(value = (1, 1,1))
bpy.ops.transform.resize(value = (2, 2, 2))

# Selects lower half of sphere
ut.act.select_by_loc((-5, -5, -5), (5, 5, -0.5), 'EDGE', 'GLOBAL')

# Mess with it
bpy.ops.transform.translate(value = (0, 0, 3))
bpy.ops.transform.resize(value = (0.1, 0.1, 0.1))
bpy.ops.object.mode_set(mode='OBJECT')
```

<h2 id="999a8926e65d99669139ce8008f96928"></h2>


### Checkpoint and Examples 

source code so far: [ut_ch03.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/ut_ch03.py)

Listing 3-12 for a random shape growth algorithm.

A brief algorithm randomly (and sloppily) selects a chunk of space in which the object resides, then extrudes the selected portion along the vertical normal of the selected surface.


[random shape](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/Listing3_12_RandomShapeGrowth.py)

---

<h2 id="1344c95436d6a0d0776ad7223043de0f"></h2>


## 4 Topics in Modeling and Rendering

<h2 id="c5aef292e11961f2493f084ee2dc220e"></h2>


### Specifying a 3D Model

- 3D models are complex digital assets that can be made up of many different components
- we typically think of the *mesh* as the most important structure that constitutes the shape of the asset
    - meshes are made of *faces*, which consist of *vertices* arranged by *indices*
    - mesh can contain *normal vectors* or *normals*, which can be specified with the vertices or faces, depending on the file format. 


**Specifying Meshes**

For the purpose of this chapter, we consider that a basic mesh is defined by its faces and normal vectors

- *Vertices* are real-valued triplets specifying a location in 3D space, typically represented as (x, y, z).
    - In Blender, the z-axis is the vertical axis
- *Indices* are positive integer-valued triplets that specify faces using a series of vertices, typically represented as (i, j, k). 
    - Given a list of N vertices indexed as 1, ..., N, a face in 3D space can be specified by a triplet of any three unique integers in 1, ..., N.  
    - the order of the integers is important in determining the direction in which the face is visible. 
    - The concept of indexing reused tuple values is often extended to other tuples such as normals and UVs in practice.
- **Faces** are determined by integer triplets of indices referencing some three vertices.
    - a three-vertex face in 3D space requires a total of nine real-valued data points
    - It is important to note that faces in 3D space are only visible in a single direction. 
    - Note that Blender does not exhibit this single-direction behavior by default, but Blender will not automatically control or correct for it when exporting to other file formats.
- *Normal Vectors* are real-valued triplets that define how the mesh interacts with lights and cameras in a scene
    - At the moment, we are concerned only with normals as they are directly assigned to points rather than normal maps that 3D artists may already by familiar with. 
    - As the name implies, the camera and lighting in a scene interacts with the mesh under the assumption that the normal vectors *lie normal* to the faces it is illuminating.

**Specifying Textures**

- The purpose of textures in 3D models is to map a 2D image onto a 3D surface, typically using an existing
 2D art asset
    - The coordinate convention we use for this is the (u, v) coordinate system.
    
<h2 id="e6a63b58cf42997d218a6fb856cb4a1f"></h2>


### Common File Formats

**Wavefront (.obj and .mtl)**

- The Wavefront geometric (.obj) and materials (.mtl) specification formats work in conjunction to specify meshes and textures. 
- the .obj file can stand on its own to specify solely geometry.
- The .obj file is very minimal and easy to understand, making it ideal for use as a standard notation for discussing the shapes of 3D objects.

**STL (STereoLithography)**

- The STL file format is commonly used by engineers and CAD software
- It is verbose when compared to the .obj format, but comes with a binary specification to compensate for its inefficiency
- STL supports normal vectors and faces, but does not use indices or support texture coordinates
- In addition, STL does not support specification of more than three coplanar points
- Curiously, where most 3D file formats allow normal vectors to be assigned to points, STL only allows normal vectors to be assigned on the face level.


**PLY (Polygon File Format)**

- This file format was built by Stanford to work with 3D scanning software.
- The PLY format is essentially a stripped-down version of .obj with additional metadata that only supports vertices and faces, not normal vectors or textures.
 
**Blender (.blend) Files and Interchange Formats**

- Blender’s native file format and in-memory data structures are very complex
- Blender supports operations on vertices, edges, and faces with noncoplanar vertices
- All the while, Blender manages complex data related to textures, sounds, animations, rigs, lights, and more. 
 

<h2 id="fa11cb7e3dbec33afd8b0c8194461c6a"></h2>


### Minimal Specification of Basic Objects

**Definition of a Cube**

- A cube is a three-dimensional object with six faces consisting of squares of equal lengths. A cube contains
 6 faces, 12 edges, and 8 vertices. 
- The square faces of a cube can be treated as compositions of two right triangles with leg lengths equal to the square length
- Note that any object in 3D space can be defined by float and integer values
    - where floats specify locations and directions in 3D space and integers specify related indices
- 3D objects also require normal vectors, which can be assigned to vertices or faces

**Naive Specification**

- To naively specify a 3D cube, we will specify each of the 6 * 2 = 12 required triangular faces independently of one another 
    - as well as assign an independent normal vector to each point.
    - This should result in 12 * 3 = 36 vertices and 12 * 3 = 36 normal vectors.
- The naivety of this model is defined by:
    - Needless repetition of vertex coordinates
    - Needless repetition of normal vector directions
    - Needless use of vertex normals in place of face normals
- In other words, naive 3D specifications do not reuse vertices or normals through indexing by treating every face as a wholly independent triangle.
- In addition, using vertex normals rather than face normals in simple cases such as a cube can increase waste. 
- This model would benefit greatly from:
    - Removing repeated vertices
    - Specifying triangular faces as square faces
    - Removing repeated normals and/or using face normals
    - Properly utilizing indices to organize vertices and normals

**Using Indices to Share Vertices and Normals**

reduced to 8 vertices and 6 normals (1 per face )

```
...
f 1//1 3//1 4//1
f 8//2 6//2 5//2
f 5//3 2//3 1//3
f 6//4 3//4 2//4
...
```

![](../imgs/blender_f4.3.png)

**Using Coplanar Vertices to Reduce Face Count**

reduce to 6 faces 

```
...
f 1//1 2//1 4//1 3//1
f 3//2 4//2 8//2 7//2
...
```

![](../imgs/blender_f4.4.png)

**Using Face Vertices to Simplify Indices**

The last repetitive characteristic is specification of the normal vector index at each point of each face. 

- this is “theoretical”
- because .obj files do not actually support face normals, although other common file formats do.
- We will continue to use the .obj format in this example for sake of consistency, but note that this file with not import

```
# Face and normals defined as:
# f (v_1, v_2, v_3, v_4)//n_1
f (1 2 4 3)//1
f (3 4 8 7)//2
f (7 8 6 5)//3
f (5 6 2 1)//4
f (3 7 5 1)//5
f (8 4 2 6)//6
```

---

<h2 id="a1d35d6a2aa25a58ffb4a9380be01bd7"></h2>


### Common Errors in Procedural Generation

**Concentric Normals**

- When generating models and exporting to various interchange and rendering formats, it is very easy for normal vectors to be ignored or misassigned
- One very common bug we encounter is unexplainable wonky lighting
    - The issue typically comes down to normal management and can be solved with a few function calls or button clicks in Blender itself

![](../imgs/blender_cocentric_normal.png)

The left side is a cube’s .obj file , which has been improperly given concentric normals.

while the right side is correctly exported with planar normals. 

![](../imgs/blender_cocentric_normal_render.png)

> Figure 4-6. Concentric normals (smooth shading) in WebGL

![](../imgs/blender_coplanar_render.png)

> Figure 4-7. Planar normals (flat shading) in WebGL

The concentric cube is lit and shaded as though it were a sphere, whereas the planar cube is lit and shaded logically, treating the top side as a sort of tabletop. 

Looking the left side , we see that each vertex in the cube is matched to a normal vector that is equal to the vertex scaled by 1/√3 ≈ 0.5773.  

This is a dangerous behavior in some exporters where, if explicit normal information is not found, it will default to creating unit vectors out of scaled vertices. 

This prevents the exporter from failing, but results in a poorly lit and often unrecognizable object.

This problem can be solved in a few ways depending on the specific exporter. 

In many cases, the target file format does not support face-level normals or face normals, so we must force Blender to work with vertex-level normals or vertex normals. 

In this case, we have Blender create multiple instances of each vertex, so that it can assign a separate normal to each. In our cube example, each vertex of a cube is connected to three separate faces, so needs three separate vertex normals.

We can use the Edge Split modifier to accomplish this. This can be found in Properties ➤ Modifiers ➤ Add Modifier ➤ Edge Split.  Adjust the split threshold to your liking and choose Apply. 

See Listing 4-10 for a Blender Python method of accessing this modifier. This can easily be wrapped in a function and would fit well in the ut.sel function class established in previous chapters.

```python
# Add modifier to selected objects
bpy.ops.object.modifier_add(type='EDGE_SPLIT')

# Set split threshold in radians
bpy.context.object.modifiers["EdgeSplit"].split_angle = (3.1415 / 180) * 5

# Apply modifier
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='EdgeSplit')
```

![](../imgs/blender_before_edge_split.png)

> Figure 4-8. Normal vectors before edge split (smooth shaded)


![](../imgs/blender_after_edge_split.png)

> Figure 4-9. Normal vectors after edge split (flat shaded)


**Flipped Normals**

Another common problem is unintentionally flipped normals.

This issue can sneak up on Blender Python programmers because of certain behaviors of Blender’s 3D Viewport. 

As previously mentioned, flipped normals can make planes appear transparent. This is often hard to diagnose in Blender because Blender treats all planes as two-sided in the 3D Viewport. 

This is unintuitive because common renderers treat planes as one-sided for sake of performance and consistency

![](../imgs/blender_flipped_normal.png)

Mathematically, this can be remedied by scaling each flipped normal vector by −1. 

Within Blender, this can be performed fairly easily by entering Edit Mode and navigating to Tool Shelf ➤ Shading / UVs ➤ Shading ➤ Normals ➤ Flip Direction. 

This button will flip the normals of all selected, vertices, edges, or faces depending on the selected parts.

In Blender’s Python API, we can perform the same function by calling bpy.ops.mesh.flip_normals() while in Edit Mode with some parts of the object selected.

The Tool Shelf ➤ Shading / UVs ➤ Shading ➤ Normals ➤ Recalculate command, which calls bpy.ops.mesh.normals_make_consistent(), will tell Blender to recalculate normals of well-defined objects to the best of its ability. 

This does not behave well for every object but can be useful nonetheless.

**Z-Fighting**

Z-fighting is a common rendering issue that produces glitchy objects without throwing errors or crashing the renderer. 

See Figure 4-12 for an example of Z-fighting among four cubes in Blender in Rendered view.

![](../imgs/blender_z_fighting.png)

> Figure 4-12. Z-fighting of cubes with coplanar faces

To understand why Z-fighting occurs, we must understand how depth buffers function in renderers.

In almost every case, the computations involved in rendering an object occur on graphics processing units (GPUs) with very standardized graphics APIs (e.g., OpenGL and DirectX). 

The standard protocol in these rendering APIs is to use the camera’s position relative to the meshes to determine which objects are visible and invisible to the user. 

This information is stored in the depth buffer. 

Before presenting a 2D image on the screen, the depth buffer tells the renderer which mesh pixel is closest to the camera and therefore visible to the user.

Given this information, why does the depth buffer not favor one mesh over another to prevent the glitchy Z-fighting effect?

The depth buffer stores high-precision floating-point values, and renderers do not make adjustments to assess the equality of floating-point numbers. 

Low-level languages that drive graphics APIs maintain efficiency by making naive floating-point number comparisons. For the same reason that
0.1 * 0.1 > 0.01 returns True in Python, floating-point number comparisons behave inconsistently in renderers.

The problems associated with floating-point arithmetic are well-studied in computer science, and floating-point equality is one of its most significant challenges.

How does one solve this problem given the tools in Blender and its Python API? There are a number of solutions, depending on the particular situation.

- Translate each object by a small and unnoticeable amount (around 0.000001 Blender units) such that the surfaces are no longer coplanar. If the translation has no effect, try translating it by a slightly larger distance.
- Delete interior faces in Edit Mode.
- Retool your algorithm to generate non-overlapping surfaces.
- Use the dissolve and limit dissolve tools in Edit Mode.

Ultimately, there are many methods for dealing with Z-fighting that all amount to making sure coplanar surfaces no longer exist in your model. We refrain from detailing all of the potential methods.

---

<h2 id="a21021ed4077220d8ee7a7b1af522450"></h2>


## 5 Introduction to Add-On Development

<h2 id="0c04eb9875bdfd13027dc08199c22c17"></h2>


### A Simple Add-On Template

For this section, enter the scripting view in Blender and go to Text Editor ➤ New to create a new script.

Give it a name, for example, simpleaddon.py. 

See [simpleaddon.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/simpleaddon.py) for a simple template from where we can start building our add-on.

Running this script will create a new tab in the Tools panel called “Simple Addon” that has a simple text input field and a button. 

The button will print a message to the console verifying that the plugin works, then parrot back the string in the text input field. 

![](../imgs/blender_simpleaddon.png)

The template presented here is fairly minimal, but we also included a handful of optional quality controls. 

We discuss each component before proceeding to more advanced add-ons.

<h2 id="0f5b9e16e0b4087f80a42c079e0a9b0a"></h2>


### Components of Blender Add-Ons

Blender add-ons rely on many different and specifically named variables and class functions to operate properly. We detail them by category here.

**The bl_info Dictionary**

The first thing to appear in a Blender add-on should be the bl_info dictionary. 

This dictionary is parsed from the first 1024 bytes of the source file so it is imperative that bl_info appear at the top of the file.

Blender’s internal engine uses data in this dictionary to populate various metadata related to the add-on itself. 

If we navigate to Header Menu ➤ File ➤ User Preferences ➤ Add-ons, we can see various official and community add-ons already in Blender.

The detailed of bl_info description here:

- name
- author
- location -- The primary location of the add-on’s GUI
    - Common syntax is Window ➤ Panel ➤ Tab ➤ Section for add-ons in the Tools, Properties, and Toolshelf panels
    - When in doubt, follow conventions established by other add-ons.
- version -- The version number of the add-on as a tuple.
- blender -- minimum Blender version numberrequiredtoruntheadd-on
- description
- wiki_url -- An URL pointing to the handbook or guide for the add-on specified as a single string.
- category -- A string specifying one the categories listed in Table 5-1.

Table 5-1. The bl-info Category Options

![](../imgs/blender_tab5.1.png)

There are a few remaining bl_info options that are less often seen.

- support -- OFFICIAL, COMMUNITY, or TESTING. 
- tracker_url -- URL pointing to a bug tracker (e.g., GitHub issues or similar).
- warning -- String specifying some warning that will appear in the user preferences window.

---

**Operators and Class Inheritance (bpy.types.Operator)**

In the simplest sense, add-ons allow us to call Blender Python functions by clicking a button in the standard Blender GUI.

Functions called by the Blender GUI must first be registered as operators of class bpy.types.Operator.

- Take for example SimpleOperator. When we register this class, the call to SimpleOperator.execute() is mapped to a function object in `bpy.ops`. 
- The function is `bpy.ops`  that it is mapped to is determined by the bl_idname value at the head of the class.
- Thus, after you run the script in Listing 5-1, you can print an encouraging message by calling `bpy.ops.object.simple_operator()` 
- The following are the steps to declare an operator in Blender. Refer to the SimpleOperator class definition in Listing 5-1 throughout.
    1. Declare a class that inherits bpy.types.Operator. This will appear in our code as:
        - `class MyNewOperator(bpy.types.Operator):`
    2. Declare `bl_idname` as a string with class and function name of your choice, separated by a period 
        - e.g., `object.simple_operator` or `simple.message`.
        - The class and function names can only contain lowercase characters and underscores. The execute function will later be accessible at `bpy.ops.my_bl_ idname`.
    3. (Optional) Declare a `bl_label`  as any string describing the function of the class. 
        - This will appear in function documentation and metadata automatically generated by Blender.
    4. Declare an execute function.
        - This function will act as a normal class function and will always accept a reference to bpy.context as a parameter.
        - `def execute(self, context):`
        - It is best practice to return `{"FINISHED"}` for a successful call to execute() within
an operator class.
    5. (Optional) Declare class methods for registering and unregistering the class.
        - The register and unregister functions will always require the @classmethod decorator and take cls as an argument. 
        - These functions are run whenever Blender attempts to register or unregister the operator class.
        - It is helpful during development to include a print statement about class registration
and deregistration  to check that Blender is not mistakenly reregistering existing classes.
        - It is also important to note that we can declare and delete scene properties in these functions. We discuss this in later sections.

---

**Panels and Class Inheritance (bpy.types.Panel)**

Here are the requirements to register a panel. Reference the SimplePanel class in Listing 5-1 throughout.
 
 1. Declare a class that inherits bpy.types.Panel. This will appear as 
    - `class MyNewPanel(bpy.types.Panel):`
 2. Declare `bl_space_type, bl_region_type, bl_category, and bl_label`. 
    - page 86

TODO

---

<h2 id="f28b2e33b807755dbe782179fdfc963d"></h2>


## 6 The bgl and blf Modules

- The bgl module is a wrapper for OpenGL functions commonly used by Blender in the 3D Viewport and Blender Game Engine. 
- The blf module is a small set of functions for displaying text and drawing fonts. 
 
<h2 id="e6878da0a2f708ad2a8ce73b2a4acb33"></h2>


### Instantaneous Drawing

- The bgl and blf modules cannot be taught in the same way that other Blender Python modules can.
- When a line or character is drawn on the 3D Viewport by either of these modules, it is only visible for a single frame.
- To effectively use the bgl and blf modules, we must use them within a handler function that is set to update at every frame change. 
    - Thus, we start with a handler example using non-OpenGL concepts.

<h2 id="629dc07d3baa953d521a2ad76c0b27a7"></h2>


### Handlers Overview

**Clock Example**

Listing 6-1. Blender Clock Handler Example

```python
import bpy
import datetime

# Clear the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create an object for our clock
bpy.ops.object.text_add(location=(0, 0, 0))
bpy.context.object.name = 'MyTextObj'

# Create a handler function
def tell_time(dummy):
    current_time = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] 
    bpy.data.objects['MyTextObj'].data.body = current_time

# Add to the list of handler functions "scene_update_pre"
bpy.app.handlers.scene_update_pre.append(tell_time)
```

![](../imgs/blender_clock_example.png)

- To instantiate a handler, we declare a function 
    - `def tell_time(dummy):`
- then add it to one of the possible lists of handlers in Blender
    - `bpy.app.handlers.scene_update_pre`
- In actuality, it is a text mesh that is updating many times per second

**Managing Handlers**

- `bpy.app.handlers.scene_update_pre`  is a list 
- so we can use methods such as `append(), pop(), remove(), and clear() ` to manage our handler functions

```python
# Will only work if 'tell_time' is in scope
bpy.app.handlers.scene_update_pre.remove(tell_time)

# Useful in development for a clean slate
bpy.app.handlers.scene_update_pre.clear()

# Remove handler at the end of the list and return it
bpy.app.handlers.scene_update_pre.pop()
``` 
 
**Types of Handlers**

Table 6-1. Types of Handlers

Handler | Called On
--- | ---
frame_change_post | After frame change during rendering or playback 
frame_change_pre | Before frame change during rendering or playback 
render_cancel | Canceling a render job
render_complete | Completing a render job
render_init | Initializing a render job
render_post | After render
render_pre | Before render
render_stats | Printing render statistics
render_write | Directly after frame is written in rendering 
load_post | After loading a .blend file
load_pre | Before loading a .blend file
save_post | After saving a .blend file
save_pre | Before saving a .blend file
scene_update_post | After updating scene data (e.g., 3D Viewport) 
scene_update_pre  | Before updating scene data (e.g. ,3D Viewport) 
game_pre  | Starting the game engine
game_post  | Ending the game engine

**Persistent Handlers**

- If we want handlers to persist after loading a .blend file, we can add the @persistent decorator
- Normally, handlers are freed when loading a .blend file
- so certain handlers like bpy.app.handlers.load_post necessitate this decorator
 

Listing 6-3. Printing File Diagnostics on Load

```python
import bpy
from bpy.app.handlers import persistent

@persistent
def load_diag(dummy):
    obs = bpy.context.scene.objects
    print('\n\n### File Diagnostics ###') 
    print('Objects in Scene:', len(obs)) 
    for ob in obs:
        print(ob.name, 'of type', ob.type)

bpy.app.handlers.load_post.append(load_diag)

# After reloading startup file:
#
# ### File Diagnostics ###
# Objects in Scene: 3
# Cube of type MESH
# Lamp of type LAMP
# Camera of type CAMERA
```

**Handlers in blf and bgl**

- Now that we have a basic understanding of handlers, we will detail how to draw with OpenGL tools directly on the 3D Viewport. 
- The handlers used for drawing on the 3D Viewport are not part of `bpy.app.handlers`
    - rather they are undocumented member functions of `bpy.types.SpaceView3D`.

Listing 6-4. Drawing the Name of an Object

```python
import bpy
from bpy_extras import view3d_utils
import bgl
import blf

# Color and font size of text
rgb_label = (1, 0.8, 0.1, 1.0)
font_size = 16
font_id = 0

# Wrapper for mapping 3D Viewport to OpenGL 2D region

def gl_pts(context, v):
    return view3d_utils.location_3d_to_region_2d( context.region, context.space_data.region_3d,v)

# Get the active object, find its 2D points, draw the name

def draw_name(context):
    ob = context.object
    v = gl_pts(context, ob.location)
    bgl.glColor4f(*rgb_label)
    blf.size(font_id, font_size, 72)
    blf.position(font_id, v[0], v[1], 0)
    blf.draw(font_id, ob.name)

# Add the handler
# arguments:
# function = draw_name,
# tuple of parameters = (bpy.context,), # constant1 = 'WINDOW',
# constant2 = 'POST_PIXEL'
bpy.types.SpaceView3D.draw_handler_add( draw_name, (bpy.context,), 'WINDOW', 'POST_PIXEL')
```

- Handlers created with bpy.types.SpaceView3D are not as easily accessible, handlers and are persistent by default. 
- Unless we create better controls for flicking these handlers on and off, we will have to restart Blender to detach this handler.
- In the next section, we place this handler in an add-on that allows us to flick it on and off with a button. Also, we store the handler in a bpy.types.Operator so we will not lose our reference to the function after adding it to the handler

TODO

---

<h2 id="a810cbc3a6b48acd8619759085c02700"></h2>


## 7 Advanced Add-On Development

TODO

<h2 id="c536c9f406f7dcd6d1ea8c650091066f"></h2>


## 8 Textures and Rendering

<h2 id="1e8b0c856db239dd8faf78f4d33f616a"></h2>


### Vocabulary of Textures

**Types of Influence in Blender**

- Properties ➤ Materials ➤ Influence.
- Diffuse textures are for coloring the object
    - Diffuse textures can describe the color, intensity, alpha levels, and translucency of objects in Blender
- Shading textures describe how the object interacts with others in the scene
    - If we want the object to mirror another, to emit color onto another, or spill ambient light into the scene, we specify the requisite shading properties in Blender.
- Specular textures describe how the object reacts to light
- Geometry textures allows the object to affect the geometric appearance of the object.
    - For example, if we supplied black and white stripes to a geometric map and specified a normal map, we would see 3D ridges in our model. 
    - It is important to note that these effects are realized only in rendering, not in the mesh data itself.


**Types of Textures in Blender**

- Properties ➤ Materials ➤ Type
- The Image and Video and Environment Map options can import image and video files.
- The remaining textures can be parameterized in Blender to achieve the desired result.

<h2 id="afd66c77848678b6a7739a9cd7b1d0a8"></h2>


### Adding and Configuring Textures

- To map a square image as a texture to a square face of a mesh, wespecifyuvcoordinates[(0, 0), (1, 0), (0, 1), (1, 1)]tothebottom-left,bottom-right,top-left,and top-right points of the mesh, respectively.
- As shapes of faces become more complicated, so do the processes required to achieve the desired texture mappings.

**Loading Textures and Generating UV Mappings**

Listing 8-1. Loading Textures and Generating UV Maps


[uv_texture.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/ut_texture.py)

Note: after running this script, view the results by selecting rendered view in the 3d Viewport header

**Textures Versus Materials in Blender**

- Texture is a broad term in 3D modeling. It can refer to diffuse textures, color textures, gradient textures, bump maps, and more. 
    - It is important to note that we can map all of these forms of textures to an object simultaneously.
    - For example, a set of shingles on the roof of a house may require an image texture, a diffuse map, and a bump map in order to appear realistic when rendered.
- A material in Blender is a collection of texture-related data. 
    - It may include any of the images and maps mentioned previously, and it may include others like normal and alpha maps. 
    - So, we must first build the material from its constituent textures, then assign the material to the object. 
    - Regardless of whether we have one or many textures comprising a material, texture data must be assigned to the material.
    - Then, materials must be assigned to the object.
 
**UV Coordinates and Loops**

- The uv coordinate data layer we aim to access is contained within a loops object
- Loops can be thought of as 3D polygons that trace a set of vertices of a 3D object.
- Loops can span multiple faces, but must start and end on the same point.
- When loops span multiple faces, they are intended to capture a localized set of adjacent faces.
- Fortunately, loops data objects in Blender have a 1-to-1 correspondence with bmesh.faces[].verts[] objects, which we are used to working with.
  - In other words, the (u, v) coordinates accessed by bm.faces[f]. loops[v][uv_layer].uv correspond to the (x, y, z) coordinates accessed by bm.faces[f].verts[v].co for any two integers, f and v.
  - It is important to note that two integers f and v may not specify a unique point in 3D space. In a default Blender 2.78c cube, as it appears in the startup file, f:v pairs 0:2, 3:3, and 4:0 all correspond to the point (-1.0, -1.0, -1.0) in 3D space. When the cube is textured, these uv coordinates will typically be unique, because they will all correspond to different parts of the texture map.

<h2 id="a502b860b196506a8403c1a490c8ecbe"></h2>


### Removing Unused Textures and Materials

- As we continually test scripts, our materials and textures data can quickly become cluttered without our realizing.
- Blender will rename textures to my_texture.001, my_texture.002, etc. when we neglect to delete them.
- Textures and materials must have no users in order to be eligible for deletion. In this case, users refers to the number of objects that currently have it assigned. 
- To delete textures and materials, we loop through our bpy.data.materials and bpy.data.textures datablocks and call .remove() on those that are not in use.

```python
import bpy

mats = bpy.data.materials 
for dblock in mats:
    if not dblock.users: 
        mats.remove(dblock)

texs = bpy.data.textures 
for dblock in mats:
    if not dblock.users: 
        texs.remove(dblock)
```

<h2 id="a8b825472bcda46b7a889fa2e79ea33e"></h2>


### Rendering Using Blender Render

We introduce and explain how to position lights and cameras in a scene, then call the rendering function to create an image.

**Adding Lights**

- In the 3D Viewport Header, we can navigate to Add ➤ Lamp to select any of Blender’s built-in lights.
- Using Python tooltips, we can see that they all rely on the function bpy.ops.object.lamp_add(), with the type= parameter determining the type of light. 
- We have the options SUN, POINT, SPOT, HEMI, and AREA. Each of these types has its own sets of parameters to configure.

Table 8-1. Types of Lights

Type | Description
--- | ---
Point | Emits lights equally in all directions; rotation has no effect
Spot | Emits a cone of light in a particular direction
Area | Emits light from a rectangular area; follows a Lambert distribution 
Hemispheric | Similar to area, but has spherical curvature
Sun | Emits orthogonal light in a particular direction; position has no effect

**Adding Cameras**

Rendering a scene requires a camera. To procedurally add a camera, we must position it, adjust its direction, and modify its parameters. We will use the functions in Listing 8-3 to position and direct the cameras as well as lights.


The biggest problem we must solve when procedurally generating cameras is determining the distance and field of view such that the entire scene will be captured without appearing too small in the rendering.

- The field of view (FoV) is a pair of two angles (θx , θy) projecting outward from a camera that defines an infinitely extending rectangular pyramid. 
- To give some perspective, an iPhone 6 camera has a FoV of about (63°, 47°) degrees when in landscape mode. 


![](../imgs/blender_fov.png)

> Figure 8-5. Field of view along the y-axis

Listing 8-3. Utilities for Lights and Cameras

```python
# Point a light or camera at a location specified by "target"
def point_at(ob, target): 
    ob_loc = ob.location
    dir_vec = target - ob.location
    ob.rotation_euler = dir_vec.to_track_quat('-Z', 'Y').to_euler()

# Return the aggregate bounding box of all meshes in a scene
def scene_bounding_box():
    # Get names of all meshes
    mesh_names = [v.name for v in bpy.context.scene.objects if v.type == 'MESH']
    
    # Save an initial value
    # Save as list for single-entry modification 
    co = coords(mesh_names[0])[0]
    bb_max = [co[0], co[1], co[2]]
    bb_min = [co[0], co[1], co[2]]

    # Test and store maxima and minima
    for i in range(0, len(mesh_names)): 
        co = coords(mesh_names[i])
        for j in range(0, len(co)):
            for k in range(0, 3):
                if co[j][k] > bb_max[k]:
                    bb_max[k] = co[j][k] 
                if co[j][k] < bb_min[k]: 
                    bb_min[k] = co[j][k]

    # Convert to tuples
    bb_max = (bb_max[0], bb_max[1], bb_max[2])
    bb_min = (bb_min[0], bb_min[1], bb_min[2])
    
    return [bb_min, bb_max]
```

**Rendering an Image**

- Rendering is the process of computing high-resolution imagery and video given 3D data
- The 3D Viewport is an instantaneous rendering of the 3D data, but it does not represent the same level of quality or definition as a traditional rendering.
- In Listing 8-4, we render the output of Listing 8-1 using both Blender Render and OpenGL render. 
    - This example assumes positions the camera to point upward along the x-axis at the median of the scene, from the yz-median of the scene, such that it will capture the whole scene

![](../imgs/blender_render_img.png)

> Figure 8-6. Blender Render

- We can also render a snapshot of the 3D Viewport using OpenGL render. This will capture basic features of the scene similar to how we see the 3D Viewport in Object Mode with Solid view. 
    - Note that we can see both the lights and camera, but not the materials, in this view. 
    - When we call bpy.ops.render.opengl(), setting `view_context = True` will cause Blender to use the 3D Viewport camera (the user’s view) rather than the scene camera.
    - ![](../imgs/opengl_render.png)

Listing 8-4. Rendering Using Blender Render and OpenGL Render

> ### Assumes output of Listing 8-1 is in scene at runtime ###


[uv_texture_render.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/uv_texture_render.py)



