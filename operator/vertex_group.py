# -*- coding: utf-8 -*-
import bpy
import re


class OPR_ChangeVGWeight(bpy.types.Operator):
    bl_idname = "lab04.change_vg_weight"
    bl_label  = "Change vertex group weight"

    value: bpy.props.FloatProperty()

    def execute(self, context):
        bpy.data.scenes["Scene"].tool_settings \
            .vertex_group_weight += self.value

        return {'FINISHED'}


class OPR_RegExRenameVG(bpy.types.Operator):
    bl_idname      = "lab04.regex_rename_vg"
    bl_label       = "RegEx Rename VG"
    bl_description = ""

    def execute(self, context):
        props = context.scene.lab04_regex_rename
        for obj in bpy.context.selected_objects:
            for vtx in obj.vertex_groups.values():
                vtx.name = re.sub(r"{}".format(props.regex), props.text, vtx.name)

        return { "FINISHED" }


class OPR_SetVGWeight(bpy.types.Operator):
    bl_idname = "lab04.set_vg_weight"
    bl_label  = "Set vertex group weight"

    weight: bpy.props.FloatProperty()

    def execute(self, context):
        bpy.data.scenes["Scene"].tool_settings \
            .vertex_group_weight = self.weight

        return {'FINISHED'}

