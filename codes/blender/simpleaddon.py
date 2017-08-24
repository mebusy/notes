# Listing 5-1. Simple Add-On Template

bl_info = {
    "name": "Simple Add-on Template",
    "author": "Chris Conlan",
    "location": "View3D > Tools > Simple Addon", "version": (1, 0, 0),
    "blender": (2, 7, 8),
    "description": "Starting point for new add-ons.", "wiki_url": "http://example.com",
    "category": "Development"
}

# Custom modules are imported here
# See end of chapter example for suggested protocol
import bpy

# Panels, buttons, operators, menus, and
# functions are all declared in this area
# A simple Operator class

class SimpleOperator(bpy.types.Operator): 
    bl_idname = "object.simple_operator" 
    bl_label = "Print an Encouraging Message"

    def execute(self, context): 
        print("\n\n####################################################") 
        print("# Add-on and Simple Operator executed successfully!") 
        print("# " + context.scene.encouraging_message) 
        print("####################################################") 
        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        
        # Register properties related to the class here
        bpy.types.Scene.encouraging_message = bpy.props.StringProperty(
            name="",
            description="Message to print to user",
            default="Have a nice day!")

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
        
        # Delete parameters related to the class here
        del bpy.types.Scene.encouraging_message

# A simple button and input field in the Tools panel
class SimplePanel(bpy.types.Panel): 
    bl_space_type = "VIEW_3D" 
    bl_region_type = "TOOLS" 
    bl_category = "Simple Addon" 
    bl_label = "Call Simple Operator" 
    bl_context = "objectmode"

    def draw(self, context): 
        self.layout.operator("object.simple_operator",
                             text="Print Encouraging Message")
        self.layout.prop(context.scene, 'encouraging_message')

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        # Register properties related to the class here.

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
        # Delete parameters related to the class here


def register():
    # Implicitly register objects inheriting bpy.types in current file and scope
    #bpy.utils.register_module(__name__)
    
    # Or explicitly register objects
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)

    print("%s registration complete\n" % bl_info.get('name')) 

def unregister():
    # Always unregister in reverse order to prevent error due to
    # interdependencies
    
    # Explicitly unregister objects
    # bpy.utils.unregister_class(SimpleOperator)
    # bpy.utils.unregister_class(SimplePanel)
    
    # Or unregister objects inheriting bpy.types in current file and scope
    bpy.utils.unregister_module(__name__)
    print("%s unregister complete\n" % bl_info.get('name'))

# Only called during development with 'Text Editor -> Run Script' 
# When distributed as plugin, Blender will directly
# and call register() and unregister()
if __name__ == "__main__":
    try: 
        unregister()
    except Exception as e:
        # Catch failure to unregister explicitly print(e)
        pass

    register()
