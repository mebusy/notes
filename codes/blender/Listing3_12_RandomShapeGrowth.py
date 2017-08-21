#Listing 3-12. Random Shape Growth
import ut
import importlib
importlib.reload(ut)

import bpy

from random import randint
from math import floor

# Must start in object mode
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(0, 0, 0))
bpy.context.object.name = 'Cube-1'

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")

for i in range(0, 100):
    
    # Grab the local coordinates
    coords = ut.coords('Cube-1', 'LOCAL')
    
    # Find the bounding box for the object
    lower_bbox = [floor(min([v[i] for v in coords])) for i in [0, 1, 2]] 
    upper_bbox = [floor(max([v[i] for v in coords])) for i in [0, 1, 2]]
    
    # Select a random face 2x2x1 units wide, snapped to integer coordinates
    lower_sel = [randint(l, u) for l, u in zip(lower_bbox, upper_bbox)] 
    upper_sel = [l + 2 for l in lower_sel]
    upper_sel[randint(0, 2)] -= 1
    
    ut.act.select_by_loc(lower_sel, upper_sel, 'FACE', 'LOCAL')
    
    # Extrude the surface along it aggregate vertical normal
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate =
          {"value": (0, 0, 1), "constraint_axis": (True, True, True), 
          "constraint_orientation" :'NORMAL'})