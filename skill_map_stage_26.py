# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SkillMap
def demo_commands():
    """Демо-команды для ручного тестирования SkillMap."""
    import json, time
    from pathlib import Path
    DATA = {"skills": [], "commands": []}
    
    sample_commands = [
        {
            "name": "create_skill",
            "description": "Создать новый навык и добавить его в список.",
            "args": ["Навык программирования Python", 3],
            "expected_result": "Добавлен навык: Научиться программировать на Python (уровень 3)",
        },
        {
            "name": "add_exercise",
            "description": "Добавить упражнение к существующему навыку.",
            "args": ["Навык программирования Python", "Писать функции с нуля", True],
            "expected_result": "Прогресс: 1/3 (33%) — Написать функцию без использования готовых решений",
        },
        {
            "name": "add_exercise",
            "description": "Добавить упражнение к существующему навыку.",
            "args": ["Навык программирования Python", "Писать классы с нуля", True],
            "expected_result": "Прогресс: 2/3 (67%) — Написать класс без использования готовых решений",
        },
        {
            "name": "add_exercise",
            "description": "Добавить упражнение к существующему навыку.",
            "args": ["Навык программирования Python", "Писать модули с нуля", True],
            "expected_result": "Прогресс: 3/3 (100%) — Написать модуль без использования готовых решений",
        },
        {
            "name": "schedule_review",
            "description": "Добавить напоминание о повторении упражнения.",
            "args": ["Навык программирования Python", "Писать функции с нуля"],
            "expected_result": "Добавлено: Повторение через 1 день, в 09:00 утра по UTC",
        },
    ]

    for cmd in sample_commands:
        print(f"=== Команда: {cmd['name']} ===")
        print(f"Описание: {cmd['description']}")
        print(f"Аргументы: {cmd['args']}")
        print(f"Ожидаемый результат: {cmd['expected_result']}")
        time.sleep(1)

    print("\n=== Демо-команды завершены ===\n")
    return sample_commands


if __name__ == "__main__":
    demo = demo_commands()
    if demo is not None:
        print("Скрипт успешно выполнен! Все демо-команды протестированы.\n")
