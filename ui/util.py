import bpy

from .common                 import _BasePanel
from ..operators.register    import registerdcr

@registerdcr
class UtilPanel(_BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_util"
    bl_label   = "util"
    bl_context = ""
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()
        col.operator("lab04.match_mesh_name_with_outliner", text="match mesh name")

