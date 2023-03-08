import bpy

from .register import registerdcr

@registerdcr
class SwitchUVSelectSync(bpy.types.Operator):
    bl_idname = "lab04.switch_uv_select_sync"
    bl_label  = "switch uv select sync"

    def execute(self, context):
        current_flag = bpy.context.scene.tool_settings.use_uv_select_sync
        try:
            if current_flag == True:
                bpy.ops.mesh.select_all(action="SELECT")
            bpy.context.scene.tool_settings.use_uv_select_sync = not current_flag

            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }
