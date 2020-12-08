import os
import bpy

bpy.ops.object.select_all(action="DESELECT")

for obj in bpy.data.objects:
    if obj.type == "MESH":
        obj.select_set(True)
 
bpy.ops.object.delete()

path = "curuthers.obj"
bpy.ops.import_scene.obj(filepath=path)
obj = bpy.context.selected_objects[0]

bpy.context.view_layer.objects.active = obj
obj.name = "Joined"
obj.data.name = "Joined"
bpy.ops.object.join()

if not os.path.exists("export)
    os.mkdir("export")

bpy.ops.export_scene.obj(
    filepath = "export/myfile.obj",
    use_selection = True,
    path_mode = "COPY")