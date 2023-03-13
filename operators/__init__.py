if "bpy" not in locals():
    import bpy
    from . import instant_sc
    from . import match_mesh_name_with_outliner
    from . import switch_uv_select_sync
else:
    import importlib
    importlib.reload(instant_sc)
    importlib.reload(match_mesh_name_with_outliner)
    importlib.reload(switch_uv_select_sync)
