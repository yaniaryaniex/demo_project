# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SkillMap
def run_cli():
    menu = {
        "1": ("Показать прогресс", lambda: print("Прогресс загружен из файла."), False),
        "2": ("Добавить упражнение", lambda: input("Название упражнения: ") or None, True),
        "3": ("Удалить упражнение", lambda: input("ID упражнения для удаления: ") or None, True),
        "4": ("Показать расписание", lambda: print("Расписание загружено."), False),
        "5": ("Выйти", lambda: exit(0), False)
    }

    while True:
        print("\n=== SkillMap CLI ===")
        for key, (desc, _, _) in menu.items():
            print(f"{key}. {desc}")
        
        choice = input("Выберите действие (1-5): ")
        if choice not in menu:
            print("Неверный выбор.")
            continue
        
        action_desc, handler, modifies_state = menu[choice]
        result = handler()
        
        if result and modifies_state:
            try:
                with open("skillmap_data.json", "w") as f:
                    import json
                    json.dump(result, f)
                print(f"Данные сохранены.")
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
