import bpy


class BasePanel(object):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "Tool"

    @classmethod
    def poll(cls, context):
        return True


class Lab04Panel(BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_util"
    bl_label   = "Lab. 04"
    bl_context = ""
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()
        col.operator("lab04.match_data_names_with_obj_names", text="match data names")

