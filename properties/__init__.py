import bpy

from .ai import Ai

__properties = {
    bpy.types.Scene: {
        "lab04_ai": bpy.props.PointerProperty(type=Ai)
    }
}

def register():
    for _type, t in __properties.items():
        for attr, prop in t.items():
            if hasattr(_type, attr):
                logging.warning(f"WARN: overwrite {_type} {attr}")
            try:
                setattr(_type, attr, prop)
            except Exception as e:
                print(e)

def unregister():
    for _type, t in __properties.items():
        for attr in t.keys():
            if hasattr(_type, attr):
                delattr(_type, attr)
