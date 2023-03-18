if "bpy" not in locals():
    import bpy
    from . import ai
    from . import util
else:
    import importlib
    importlib.reload(ai)
    importlib.reload(util)
