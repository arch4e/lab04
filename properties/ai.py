import bpy

from ..operators.register import registerdcr

@registerdcr
class Ai(bpy.types.PropertyGroup):
    api_key: bpy.props.StringProperty(default="")
    prompt : bpy.props.StringProperty(default="")
