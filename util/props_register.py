# -*- coding: utf-8 -*-
import bpy

from ..property.vertex_group import PRP_RegExRenameVG


properties = {
    bpy.types.Scene: {
        "lab04_regex_rename": bpy.props.PointerProperty(type=PRP_RegExRenameVG)
    }
}


def register():
    for _type, data in properties.items():
        for attr, prop in data.items():
            if hasattr(_type, attr):
                print(f'WARN: overwrite {_type} {attr}')

            try:
                setattr(_type, attr, prop)
            except Exception as e:
                print(e)


def unregister():
    for _type, data in properties.items():
        for attr in data.keys():
            if hasattr(_type, attr):
                delattr(_type, attr)

