import bpy
import bmesh
from mathutils import Color

# Clear scene
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create cube
bpy.ops.mesh.primitive_cube_add(radius = 1, location = (0, 0, 0))

bpy.ops.object.mode_set(mode = 'EDIT')

# Create material to hold textures
material_obj = bpy.data.materials.new('number_1_material')

### Begin configure the number one ###
# Path to image
imgpath = '/Users/qibinyi/Desktop/number_1.png' 
image_obj = bpy.data.images.load(imgpath)

# Create image texture from image
texture_obj = bpy.data.textures.new('number_1_tex', type='IMAGE')
texture_obj.image = image_obj

# Add texture slot for image texture
texture_slot = material_obj.texture_slots.add()
texture_slot.texture = texture_obj

### Begin configuring the number two ###
# Path to image
imgpath = '/Users/qibinyi/Desktop/number_2.png' 
image_obj = bpy.data.images.load(imgpath)

# Create image texture from image
texture_obj = bpy.data.textures.new('number_2_tex', type='IMAGE')
texture_obj.image = image_obj

# Add texture slot for image texture
texture_slot = material_obj.texture_slots.add()
texture_slot.texture = texture_obj

# Tone down color map, turn on and tone up normal mapping
texture_slot.diffuse_color_factor = 0.2
texture_slot.use_map_normal = True
texture_slot.normal_factor = 2.0

### Finish configuring textures ###
# Add material to current object 
bpy.context.object.data.materials.append(material_obj)

### Begin configuring UV coordinates ###
bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
bm.faces.ensure_lookup_table()

# Index of face to texture
face_ind = 0
bpy.ops.mesh.select_all(action='DESELECT')
bm.faces[face_ind].select = True

# Unwrap to instantiate uv layer
bpy.ops.uv.unwrap()

# Grab uv layer
uv_layer = bm.loops.layers.uv.active

# Begin mapping...
loop_data = bm.faces[face_ind].loops


# bottom right
uv_data = loop_data[0][uv_layer].uv
uv_data.x = 1.0
uv_data.y = 0.0


# top right
uv_data = loop_data[1][uv_layer].uv
uv_data.x = 1.0
uv_data.y = 1.0

# top left
uv_data = loop_data[2][uv_layer].uv
uv_data.x = 0.0
uv_data.y = 1.0

# bottom left
uv_data = loop_data[3][uv_layer].uv
uv_data.x = 0.0
uv_data.y = 0.0

# Change background color to white to match our example
bpy.data.worlds['World'].horizon_color = Color((1.0, 1.0, 1.0))

# Switch to object mode to add lights
bpy.ops.object.mode_set(mode='OBJECT')

# Liberally add lights
dist = 5
for side in [-1, 1]:
    for coord in [0, 1, 2]: 
        loc = [0, 0, 0]
        loc[coord] = side * dist
        bpy.ops.object.lamp_add(type='POINT', location=loc)

# Switch to rendered mode to view results






