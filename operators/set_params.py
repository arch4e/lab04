import bpy
import bmesh

from .register import registerdcr

@registerdcr
class SetParams(bpy.types.Operator):
    bl_idname = "lab04.set_params"
    bl_label  = "set parameters"

    tag: bpy.props.StringProperty()

    def execute(self, context):
        if self.tag == "set_sharp":
            set_sharp()
        else:
            return { "CANCELLED" }

        return {'FINISHED'}

def set_sharp():
    try:
        bpy.ops.transform.edge_crease(value=1, snap=False)
        bpy.ops.mesh.mark_sharp()
    except Exception as e:
        print(e)

