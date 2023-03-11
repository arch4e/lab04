import bpy
import bmesh

from .register import registerdcr

@registerdcr
class SwitchUVSelectSync(bpy.types.Operator):
    bl_idname = "lab04.switch_uv_select_sync"
    bl_label  = "switch uv select sync"

    def execute(self, context):
        try:
            backup_data = []

            if bpy.context.scene.tool_settings.use_uv_select_sync:
                # backup selected loops
                bpy.ops.object.mode_set(mode='EDIT')
                backup_data = backup_selected_loops_from_bmesh()

                # select all vertex
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action="SELECT")

                # disable uv select sync
                bpy.context.scene.tool_settings.use_uv_select_sync = False

                # restore selected loops
                # ! getting uv_layers.active.data only works in object mode
                bpy.ops.object.mode_set(mode='OBJECT')
                restore_selected_loops_to_uv_layer(backup_data)
                bpy.ops.object.mode_set(mode='EDIT')
            elif not bpy.context.scene.tool_settings.use_uv_select_sync:
                # backup selected loops
                # ! getting uv_layers.active.data only works in object mode
                bpy.ops.object.mode_set(mode='OBJECT')
                backup_data = backup_selected_loops_from_uv_layer()

                # enable uv select sync
                bpy.context.scene.tool_settings.use_uv_select_sync = True

                # restore selected loops
                bpy.ops.object.mode_set(mode='EDIT')
                restore_selected_loops_to_bmesh(backup_data)

            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }

def backup_selected_loops_from_bmesh():
    backup_data = []
    for i in range(len(bpy.context.selected_objects)):
        backup_data.append([])
        obj = bpy.context.selected_objects[i]
        bm = bmesh.new()
        bm = bmesh.from_edit_mesh(obj.data)
        loops = [loop for face in bm.faces for loop in face.loops]

        for l in loops:
            backup_data[i].append(l.vert.select)

    return backup_data

def backup_selected_loops_from_uv_layer():
    backup_data = []
    for i in range(len(bpy.context.selected_objects)):
        backup_data.append([])
        obj = bpy.context.selected_objects[i]

        for j in range(len(obj.data.uv_layers.active.data.items())):
            backup_data[i].append(obj.data.uv_layers.active.data[j].select)

    return backup_data

def restore_selected_loops_to_bmesh(source_data):
    for i in range(len(bpy.context.selected_objects)):
        obj = bpy.context.selected_objects[i]
        bm = bmesh.new()
        bm = bmesh.from_edit_mesh(obj.data)
        loops = [loop for face in bm.faces for loop in face.loops]

        # deselect loops
        for j in range(len(loops)):
            loops[j].vert.select_set(False)

        # only the loop selected in the uv layer are made selected
        # ! because when a loop on the same vertex is deselected,
        #   the previously selected loop is deselected
        for j in range(len(loops)):
            if source_data[i][j]:
                loops[j].vert.select_set(True)

        bm.select_flush_mode()

def restore_selected_loops_to_uv_layer(source_data):
    for i in range(len(bpy.context.selected_objects)):
        obj = bpy.context.selected_objects[i]

        for j in range(len(obj.data.uv_layers.active.data.items())):
            obj.data.uv_layers.active.data[j].select = source_data[i][j]
