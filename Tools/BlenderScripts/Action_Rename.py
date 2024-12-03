import bpy

# Строка, которую нужно удалить
remove_str = "SK_Body_F_001@|SK_Body_F_001@|"
# Префикс
prefix_str = "SK_Body_F_001@"

# Перебор всех Action в проекте
for action in bpy.data.actions:
    if remove_str in action.name:
        # Переименование Action
        new_name = action.name.replace(remove_str, "")
        new_name = prefix_str + new_name
        action.name = new_name
        print(f"Переименовано: {action.name}")

print("Готово!")