# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel


class RegExRenamePanel(BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_regex_rename"
    bl_label   = "lab. 04 - RegEx Rename VTX-Grp."
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        layout = self.layout
        col    = layout.column()

        col.label(text="RegEx")
        col.prop(bpy.context.scene.wpu_regex_rename, "regex", text="")
        col.label(text="Replace to:")
        col.prop(bpy.context.scene.wpu_regex_rename, "text", text="")
        col.operator("lab04.regex_rename", text="Rename vtx_groups")

