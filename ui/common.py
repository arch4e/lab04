import bpy


class BasePanel(object):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "Tool"

    @classmethod
    def poll(cls, context):
        return True


class UI_SharedPanel(BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_ui_util"
    bl_label   = "Lab. 04"
    bl_context = ""
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()
        col.operator("lab04.sync_name_object_to_mesh", text="sync name (obj. to mesh)")

