# -*- coding: utf-8 -*-
import bpy


class PRP_RegExRenameVG(bpy.types.PropertyGroup):
    regex: bpy.props.StringProperty(default="") # noqa: F722
    text : bpy.props.StringProperty(default="") # noqa: F722

