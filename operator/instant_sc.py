import bpy


class OPR_InstantSC_1(bpy.types.Operator):
    bl_idname = "lab04.instant_sc_1"
    bl_label  = "instant short cut - 1"

    def execute(self, context):
        try:
            instant_sc_1()
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }


class OPR_InstantSC_2(bpy.types.Operator):
    bl_idname = "lab04.instant_sc_2"
    bl_label  = "instant short cut - 2"

    def execute(self, context):
        try:
            instant_sc_2()
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }


class OPR_InstantSC_3(bpy.types.Operator):
    bl_idname = "lab04.instant_sc_3"
    bl_label  = "instant short cut - 3"

    def execute(self, context):
        try:
            instant_sc_3()
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }


def instant_sc_1():
    print("instant_sc_1")
    # edit here


def instant_sc_2():
    print("instant_sc_2")
    # edit here


def instant_sc_3():
    print("instant_sc_3")
    # edit here

