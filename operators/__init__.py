if "bpy" not in locals():
    import bpy
    from . import ai
    from . import instant_sc
    from . import match_data_names_with_obj_names
    from . import set_params
    from . import switch_uv_select_sync
else:
    import importlib
    importlib.reload(ai)
    importlib.reload(instant_sc)
    importlib.reload(match_data_names_with_obj_names)
    importlib.reload(set_params)
    importlib.reload(switch_uv_select_sync)
