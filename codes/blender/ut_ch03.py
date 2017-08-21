import bpy
import bmesh

# Function for selecting objects by name
def select(objName):
    bpy.ops.object.select_all(action = 'DESELECT')
    bpy.data.objects[objName].select = True

# Function for activating objects by name
def activate(objName):
    bpy.context.scene.objects.active = bpy.data.objects[objName]

# Function for entering Edit Mode with no vertices selected,
# or entering Object Mode with no additional processes
def mode(mode_name):
    bpy.ops.object.mode_set(mode = mode_name)
    if mode_name == "EDIT":
        bpy.ops.mesh.select_all(action="DESELECT")


def selection_mode(type):
    bpy.ops.mesh.select_mode(type = type)        
        

def coords(objName, space = 'GLOBAL'):
    
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
    
    
def in_bbox(lbound, ubound, v, buffer = 0.0001):
    return lbound[0] - buffer <= v[0] <= ubound[0] + buffer and \
            lbound[1] - buffer <= v[1] <= ubound[1] + buffer and \
            lbound[2] - buffer <= v[2] <= ubound[2] + buffer
    
        
class sel:
    """Function Class for operating on SELECTED objects"""

    def transform_apply():
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
    # Differential    
    def translate(v):
        bpy.ops.transform.translate(value = v, constraint_axis = (True, True, True))

    # Differential           
    def scale(v):
        bpy.ops.transform.resize(value = v, constraint_axis = (True, True, True))

    # Differential    
    def rotate_x(v):
        bpy.ops.transform.rotate(value = v, axis = (1, 0, 0))

    # Differential    
    def rotate_y(v):
        bpy.ops.transform.rotate(value = v, axis = (0, 1, 0))
        
    # Differential    
    def rotate_z(v):
        bpy.ops.transform.rotate(value = v, axis = (0, 0, 1))        

    def transform_apply():
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


    

    
# Add in body of script, outside any class declarations
def in_bbox(lbound, ubound, v, buffer = 0.0001):
    return lbound[0] - buffer <= v[0] <= ubound[0] + buffer and \
            lbound[1] - buffer <= v[1] <= ubound[1] + buffer and \
            lbound[2] - buffer <= v[2] <= ubound[2] + buffer

## Transformations with bpy
class act:
    
    def select_by_loc(lbound = (0, 0, 0), ubound = (0, 0, 0),
                        select_mode = 'VERT', coords = 'GLOBAL'):
        
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
        
        return sum([1 for s in to_select if s])
        
    # Declarative
    def location(v):
        bpy.context.object.location = v
        
    # Declarative
    def scale(v):
        bpy.context.object.scale = v
        
    # Declarative
    def rotation(v):
        bpy.context.object.rotation_euler = v
        
    # Rename the active object
    def rename(objName):
        bpy.context.object.name = objName

    def register_bmesh():
        return bmesh.from_edit_mesh(bpy.context.object.data)
        
    def select_vert(bm, i):
        bm.verts.ensure_lookup_table()
        bm.verts[i].select = True

    def select_edge(bm, e):
        bm.edges.ensure_lookup_table()
        bm.edges[e].select = True
        
    def select_face(bm, f):
        bm.faces.ensure_lookup_table()
        bm.faces[f].select = True
        
    def deselect_all():
        bpy.ops.mesh.select_all(action="DESELECT")
    
    def extrude(v):
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate = 
              {"value":v,
               "constraint_axis": (True, True, True),
               "constraint_orientation":'NORMAL'})
               
    def subdivide(cuts = 1):
        bpy.ops.mesh.subdivide(number_cuts = cuts)
        
    def randomize(intensity = 0.1):
        bpy.ops.transform.vertex_random(offset = intensity)

    def select_all():
        bpy.ops.mesh.select_all(action="SELECT")       



class spec:
    """Function Class for operating on SPECIFIED objects"""

    # Declarative
    def scale(objName, v):
        bpy.data.objects[objName].scale = v
            
    # Declarative
    def location(objName, v):
        bpy.data.objects[objName].location = v
            
    # Declarative
    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
        

class create:
    """Function Class for CREATING Objects"""
    
    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(radius = 0.5, location = (0, 0, 0))
        act.rename(objName)
        
    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(size = 0.5, location = (0, 0, 0))
        act.rename(objName)        
        
    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(radius1 = 0.5, location = (0, 0, 0))
        act.rename(objName)

    def plane(objName):
        bpy.ops.mesh.primitive_plane_add(radius = 0.5, location = (0, 0, 0))
        act.rename(objName)              


def delete(objName):
    
    select(objName)
    bpy.ops.object.delete(use_global=False)
    
    
def delete_all():
    
    if( len(bpy.data.objects) != 0 ):
        bpy.ops.object.select_all(action = 'SELECT')
        bpy.ops.object.delete(use_global=False)
        

if __name__ == "__main__":
    
    # Create a cube
    create.cube('PerfectCube')
    
    # Differential transformations combine
    sel.translate((0, 1, 2))
    
    sel.scale((1, 1, 2))
    sel.scale((0.5, 1, 1))
    
    sel.rotate_x(3.1415/8)
    sel.rotate_x(3.1415/7)
    
    sel.rotate_z(3.1415/3)
    
    
    # Create a cone
    create.cone('PointyCone')
    
    # Declaractive transformations overwrite
    act.location((-2, -2, 0))
    spec.scale('PointyCone', (1.5, 2.5, 2))
    
    
    # Create a Sphere
    create.sphere('SmoothSphere')
    
    # Declaractive transformations overwrite
    spec.location('SmoothSphere', (2, 0, 0))
    act.rotation((0, 0, 3.1415/3))
    act.scale((1, 3, 1))