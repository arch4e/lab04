# -*- coding: utf-8 -*-
import bpy
import re


class OPR_RegExRename(bpy.types.Operator):
    bl_idname      = "lab04.regex_rename"
    bl_label       = "RegEx Rename"
    bl_description = ""

    def execute(self, context):
        props = context.scene.wpu_regex_rename
        for obj in bpy.context.selected_objects:
            for vtx in obj.vertex_groups.values():
                vtx.name = re.sub(r"{}".format(props.regex), props.text, vtx.name)


        return { "FINISHED" }

