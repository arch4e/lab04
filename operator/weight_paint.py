import bpy


class SetVTXGWeight(bpy.types.Operator):
    bl_idname = "lab04.set_vtxg_weight"
    bl_label  = "Set vertex group weight"

    weight: bpy.props.FloatProperty()

    def execute(self, context):
        bpy.data.scenes["Scene"].tool_settings \
            .vertex_group_weight = self.weight

        return {'FINISHED'}


class ChangeVTXGWeight(bpy.types.Operator):
    bl_idname = "lab04.change_vtxg_weight"
    bl_label  = "Change vertex group weight"

    value: bpy.props.FloatProperty()

    def execute(self, context):
        bpy.data.scenes["Scene"].tool_settings \
            .vertex_group_weight += self.value

        return {'FINISHED'}

