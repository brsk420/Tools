import bpy
import os

# Путь к папке, где будут сохранены FBX файлы
output_dir = "/Users/brsk_/Documents/_Asterman/slot-machine/Assets/BIV/Art/Avatar/Male/Animations"

# Имя вашего скелета (арматуры)
armature_name = "root_arpbob"

# Убедитесь, что вы находитесь в Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

# Получаем арматуру
armature = bpy.data.objects[armature_name]

# Сохраняем оригинальное имя сцены
original_scene_name = bpy.context.scene.name

# Экспортируем каждую анимацию в отдельный FBX файл
for action in bpy.data.actions:
    # Присваиваем текущую анимацию арматуре
    armature.animation_data.action = action

    # Устанавливаем правильный диапазон кадров для текущей анимации
    start_frame, end_frame = action.frame_range
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    bpy.context.scene.frame_start = start_frame
    bpy.context.scene.frame_end = end_frame

    # Переименовываем сцену временно для экспорта
    bpy.context.scene.name = action.name

    # Обновляем сцену, устанавливая первый кадр
    bpy.context.scene.frame_set(start_frame)

    # Имя файла соответствует имени анимации
    filename = "SK_Body_M_001@" + f"{action.name}.fbx"
    filepath = os.path.join(output_dir, filename)

    # Экспортируем FBX с текущей активной анимацией
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        use_selection=True,
        object_types={'ARMATURE'},
        bake_anim=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_force_startend_keying=True,
        bake_anim_simplify_factor=1,
        add_leaf_bones=False,
        armature_nodetype='NULL',
        use_armature_deform_only=True,
        bake_space_transform=False
    )

# Восстанавливаем оригинальное имя сцены после экспорта
bpy.context.scene.name = original_scene_name

print("Экспорт завершен.")
