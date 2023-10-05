# -*- coding: utf-8 -*-
import bpy


class PRP_RegExRename(bpy.types.PropertyGroup):
    regex: bpy.props.StringProperty(default="") # noqa: F722
    text : bpy.props.StringProperty(default="") # noqa: F722

