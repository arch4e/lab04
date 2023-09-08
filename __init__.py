# -*- coding: utf-8 -*-
import bpy

#
# import local modules
#
from .operator.instant_sc import InstantSC_1, InstantSC_2, InstantSC_3
from .operator.match_data_names_with_obj_names import MatchDataNameWithObjNames
from .operator.switch_uv_select_sync import SwitchUVSelectSync
from .ui.common import Lab04Panel

#
# addon information
#
bl_info = {
    "name"    : "Lab. 04",
    "category": "3D View",
    "location": "",
    "version" : (0,5,0),
    "blender" : (3,0,0),
    "author"  : "arch4e"
}


classes = [
    # Operator
    InstantSC_1,
    InstantSC_2,
    InstantSC_3,
    MatchDataNameWithObjNames,
    SwitchUVSelectSync,
    # UI
    Lab04Panel
]


def check_blender_version():
    if bpy.app.version < bl_info.get("blender"):
        unregister()
        raise ImportError("error: unsupported version")


def register():
    # Returns an exception current Blender version is not supported
    check_blender_version()

    try:
        for cls in classes:
            bpy.utils.register_class(cls)
    except Exception as e:
        print("error: registration failed")
        print(repr(e))
        pass


def unregister():
    try:
        for cls in classes:
            bpy.utils.unregister_class(cls)
    except Exception:
        print("error: unregistration failed")
        pass


if __name__ == "__main__":
    register()

