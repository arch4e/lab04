import bpy


class OPR_SyncNameObjToMesh(bpy.types.Operator):
    bl_idname = "lab04.sync_name_object_to_mesh"
    bl_label  = "sync name object to mesh"

    def execute(self, context):
        try:
            for obj in bpy.data.objects:
                if hasattr(obj.data, "name") and hasattr(obj, "name"):
                    obj.data.name = obj.name
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }

