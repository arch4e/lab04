class _BasePanel(object):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_category    = "Lab. 04"

    @classmethod
    def poll(cls, context):
        return True

