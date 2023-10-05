import bpy

from .common import BasePanel


class WeightSetterPanel(BasePanel, bpy.types.Panel):
    bl_category = "Item"
    bl_idname   = "VIEW3D_PT_lab04_weight_setter"
    bl_label    = "Lab. 04"
    bl_context  = ""
    bl_options  = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()

        #
        # Vertex Groups
        #
        col.label(text="Vertex Groups")

        rows = 3
        if context.object.vertex_groups.active:
            rows = 5

        row = col.row()
        row.template_list("MESH_UL_vgroups", "", context.object, "vertex_groups", context.object.vertex_groups, "active_index", rows=rows)

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
        row.operator("lab04.set_vtxg_weight", text="0.1").weight = 0.1
        row.operator("lab04.set_vtxg_weight", text="0.3").weight = 0.3
        row.operator("lab04.set_vtxg_weight", text="0.5").weight = 0.5
        row.operator("lab04.set_vtxg_weight", text="0.7").weight = 0.7
        row.operator("lab04.set_vtxg_weight", text="1.0").weight = 1.0
        row = col.row()
        row.operator("lab04.change_vtxg_weight", text="- 0.05").value = -0.05
        row.operator("lab04.change_vtxg_weight", text="- 0.1").value = -0.1
        row.operator("lab04.change_vtxg_weight", text="+ 0.1").value = 0.1
        row.operator("lab04.change_vtxg_weight", text="+ 0.05").value = 0.05

