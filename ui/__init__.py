if "bpy" not in locals():
    import bpy
    from . import util
else:
    import importlib
    importlib.reload(util)

