...menustart

 - [API](#db974238714ca8de634a7ce1d083a14f)
	 - [2 The bpy Module](#b8836758104839a89ea645e997c6f8cb)
		 - [Selection, Activation, and Specification](#f1189fbbb6cb319df8b3a5ad5b3faaef)

...menuend


<h2 id="db974238714ca8de634a7ce1d083a14f"></h2>

# API

 - `http://www.blender.org/api`
 - `http://www.blender.org/api/blender_python_api_2_78c_release`

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

### Transformations with bpy

 - bpy.ops.transorm

Listing 2-9. Minimal Toolkit for Creation and Transformation (ut.py)

[ut.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/ut.py)

### Visualizing Multivariate Data with the Minimal Toolkit

Visualizing 3/4 Dimensions of Data 

[ut.py](https://raw.githubusercontent.com/mebusy/notes/master/codes/blender/visualize3d.py)

 - for 4th Dimension , we use scale to represent it
 - for 5th Dimension, we can use different shapes

---

## 3 The bmesh Module

### Edit Mode

Listing 3-1. Switching Between Object and Edit Mode

```python
# Set mode to Edit Mode
bpy.ops.object.mode_set(mode="EDIT")

# Set mode to Object Mode
bpy.ops.object.mode_set(mode="OBJECT")

```

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

### Note on Indexing and Cross-Compatibility

 - 使用硬编码数字下标 访问 vertex, edge , face 会导致 预期外的结果
 - 不同版本的blender 的相同的操作，索引会有差异

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
