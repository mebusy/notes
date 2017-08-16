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


    



