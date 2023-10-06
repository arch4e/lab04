# -*- coding: utf-8 -*-
import bpy

from .common import BasePanel


class UI_RegExRenameVG(BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_ui_regex_rename_vg"
    bl_label   = "Lab. 04 - RegEx Rename VG"
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        layout = self.layout
        col    = layout.column()

        col.label(text="Find ( RegEx ):")
        col.prop(bpy.context.scene.lab04_regex_rename, "regex", text="")
        col.label(text="Replace:")
        col.prop(bpy.context.scene.lab04_regex_rename, "text", text="")
        col.operator("lab04.regex_rename_vg", text="Rename V-Groups")


class UI_VertexGroups(BasePanel, bpy.types.Panel):
    bl_category = "Item"
    bl_idname   = "VIEW3D_PT_lab04_ui_vertex_group"
    bl_label    = "Lab. 04 - Vertex Group"
    bl_context  = ""
    bl_options  = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()

        #
        # Vertex Groups
        #
        _rows = 3
        if context.object.vertex_groups.active:
            _rows = 5

        row = col.row()
        row.template_list("MESH_UL_vgroups", "", context.object, "vertex_groups", context.object.vertex_groups, "active_index", rows=_rows)

        row = col.row(align=True)
        row.operator("object.vertex_group_assign", text="Assign")
        row.operator("object.vertex_group_remove_from", text="Remove")

        row = col.row(align=True)
        row.operator("object.vertex_group_select", text="Select")
        row.operator("object.vertex_group_deselect", text="Deselect")

        col.separator()

        #
        # Weight Settings
        #
        col.prop(context.tool_settings, "vertex_group_weight", text="Weight")

        col.separator()

        row = col.row()
        row.operator("lab04.set_vg_weight", text="0.1").weight = 0.1
        row.operator("lab04.set_vg_weight", text="0.3").weight = 0.3
        row.operator("lab04.set_vg_weight", text="0.5").weight = 0.5
        row.operator("lab04.set_vg_weight", text="0.7").weight = 0.7
        row.operator("lab04.set_vg_weight", text="1.0").weight = 1.0
        row = col.row()
        row.operator("lab04.change_vg_weight", text="- 0.05").value = -0.05
        row.operator("lab04.change_vg_weight", text="- 0.1").value = -0.1
        row.operator("lab04.change_vg_weight", text="+ 0.1").value = 0.1
        row.operator("lab04.change_vg_weight", text="+ 0.05").value = 0.05

