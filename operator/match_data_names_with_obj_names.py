import bpy


class MatchDataNameWithObjNames(bpy.types.Operator):
    bl_idname = "lab04.match_data_names_with_obj_names"
    bl_label  = "match data names with object names"

    def execute(self, context):
        try:
            for obj in bpy.data.objects:
                if hasattr(obj.data, "name") and hasattr(obj, "name"):
                    obj.data.name = obj.name
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }

