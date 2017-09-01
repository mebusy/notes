import bpy
import bmesh
import ut

from math import pi, tan
from mathutils import Vector

# Get scene's bounding box (meshes only)
bbox = ut.scene_bounding_box()

# Calculate median of bounding box
bbox_med = ( (bbox[0][0] + bbox[1][0])/2,
             (bbox[0][1] + bbox[1][1])/2,
             (bbox[0][2] + bbox[1][2])/2 )


# Calculate size of bounding box
bbox_size = ( (bbox[1][0] - bbox[0][0]),
              (bbox[1][1] - bbox[0][1]),
              (bbox[1][2] - bbox[0][2]) )

# Add camera to scene
bpy.ops.object.camera_add(location=(0, 0, 0), rotation=(0, 0, 0))
camera_obj = bpy.context.object
camera_obj.name = 'Camera_1'

# Required for us to manipulate FoV as angles
camera_obj.data.lens_unit = 'FOV'

# Set image resolution in pixels
# Output will be half the pixelage set here 
scn = bpy.context.scene 
scn.render.resolution_x = 1800 
scn.render.resolution_y = 1200

# Compute FoV angles
aspect_ratio = scn.render.resolution_x / scn.render.resolution_y

if aspect_ratio > 1:
    camera_angle_x = camera_obj.data.angle 
    camera_angle_y = camera_angle_x / aspect_ratio
else:
    camera_angle_y = camera_obj.data.angle
    camera_angle_x = camera_angle_y * aspect_ratio

# Set the scene's camera to our new camera
scn.camera = camera_obj

# Determine the distance to move the camera away from the scene
camera_dist_x = (bbox_size[1]/2) * (tan(camera_angle_x / 2) ** -1)
camera_dist_y = (bbox_size[2]/2) * (tan(camera_angle_y / 2) ** -1)
camera_dist = max(camera_dist_x, camera_dist_y)


# Multiply the distance by an arbitrary buffer
camera_buffer = 1.10
camera_dist *= camera_buffer

# Position the camera to point up the x-axis
camera_loc = (bbox[0][1] - camera_dist, bbox_med[1], bbox_med[2])


# Set new location and point camera at median of scene
camera_obj.location = camera_loc
ut.point_at(camera_obj, Vector(bbox_med))

# Set render path
render_path = '/Users/qibinyi/Desktop/blender_render.png'
bpy.data.scenes['Scene'].render.filepath = render_path

# Render using Blender Render
bpy.ops.render.render( write_still = True )


# Set render path
render_path = '/Users/qibinyi/Desktop/opengl_render.png'
bpy.data.scenes['Scene'].render.filepath = render_path


# Render 3D viewport using OpenGL render
bpy.ops.render.opengl( write_still = True , view_context = True )


