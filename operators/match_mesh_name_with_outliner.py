import bpy

from .register import registerdcr

@registerdcr
class MatchMeshNameWithOutliner(bpy.types.Operator):
    bl_idname = "lab04.match_mesh_name_with_outliner"
    bl_label  = "match mesh name with outliner"

    def execute(self, context):
        try:
            for obj in bpy.data.objects:
                obj.data.name = obj.name
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }

