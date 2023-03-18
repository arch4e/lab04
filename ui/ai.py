import bpy

from .common                 import _BasePanel
from ..operators.register    import registerdcr

@registerdcr
class AiPanel(_BasePanel, bpy.types.Panel):
    bl_idname  = "VIEW3D_PT_lab04_ai"
    bl_label   = "AI"
    bl_context = ""
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        col = self.layout.column()

        col.label(text="API Key")
        col.prop(bpy.context.scene.lab04_ai, "api_key", text="")

        col.separator(factor=1.0)

        col.label(text="Prompt")
        col.prop(bpy.context.scene.lab04_ai, "prompt", text="", slider=True)
        col.operator("lab04.post_message_to_ai", text="post")
