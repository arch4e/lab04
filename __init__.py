# -*- coding: utf-8 -*-
import bpy


#
# import local modules
#
from .operator.instant_sc import OPR_InstantSC_1, OPR_InstantSC_2, OPR_InstantSC_3
from .operator.switch_uv_select_sync import OPR_SwitchUVSelectSync
from .operator.sync_name_obj_to_mesh import OPR_SyncNameObjToMesh
from .operator.vertex_group import OPR_ChangeVGWeight, OPR_RegExRenameVG, OPR_SetVGWeight
from .property.vertex_group import PRP_RegExRenameVG
from .ui.common import UI_SharedPanel
from .ui.vertex_group import UI_VertexGroups, UI_RegExRenameVG
from .util.props_register import register as props_register, unregister as props_unregister


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
    UI_RegExRenameVG,
    UI_SharedPanel,
    UI_VertexGroups,
    OPR_ChangeVGWeight,
    OPR_InstantSC_1,
    OPR_InstantSC_2,
    OPR_InstantSC_3,
    OPR_RegExRenameVG,
    OPR_SetVGWeight,
    OPR_SwitchUVSelectSync,
    OPR_SyncNameObjToMesh,
    PRP_RegExRenameVG,
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

        props_register()
    except Exception as e:
        print("error: registration failed")
        print(repr(e))
        pass


def unregister():
    try:
        for cls in classes:
            bpy.utils.unregister_class(cls)

        props_unregister()
    except Exception:
        print("error: unregistration failed")
        pass


if __name__ == "__main__":
    register()

