# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SkillMap
def demo():
    print("=" * 60)
    print("SkillMap — Демо: план развития навыков")
    print("=" * 60)

    # Создаем навыки
    skills = [
        Skill("Python", "Основы", 3, 60),
        Skill("Git", "Основы", 2, 45),
        Skill("SQL", "Средний", 4, 90),
        Skill("Docker", "Продвинутый", 5, 120),
    ]

    # Создаем упражнения для каждого навыка
    exercises = {
        "Python": [
            Exercise("Переменные и типы", 10, "Easy"),
            Exercise("Функции", 25, "Medium"),
            Exercise("ООП", 40, "Hard"),
        ],
        "Git": [
            Exercise("Базовые команды", 15, "Easy"),
            Exercise("Branches и merges", 30, "Medium"),
            Exercise("Rebase и cherry-pick", 45, "Hard"),
        ],
        "SQL": [
            Exercise("SELECT и WHERE", 20, "Easy"),
            Exercise("JOIN", 35, "Medium"),
            Exercise("Подзапросы и оконные функции", 50, "Hard"),
        ],
        "Docker": [
            Exercise("Image и Container", 25, "Easy"),
            Exercise("Dockerfile и multi-stage", 40, "Medium"),
            Exercise("Docker Compose и сети", 55, "Hard"),
        ],
    }

    # Создаем расписание
    schedule = Schedule("2024-03-01", "2024-03-31", "2024-03-01 10:00", "2024-03-01 11:00")

    # Создаем прогресс
    progress = Progress()

    # Проверяем, может ли пользователь начать
    if not schedule.can_start():
        print("❌ Расписание не может быть начато.")
        return

    if not schedule.can_end():
        print("❌ Расписание не может быть завершено.")
        return

    # Проверяем, что все навыки готовы
    for skill in skills:
        if not skill.is_complete():
            print(f"❌ Навык '{skill.name}' не завершён.")
            return

    # Проверяем, что все упражнения готовы
    for skill_name, exercises_list in exercises.items():
        for ex in exercises_list:
            if not progress.is_exercise_complete(skill_name, ex.name):
                print(f"❌ Упражнение '{ex.name}' не завершено.")
                return

    # Всё готово, показываем результат
    print("✅ Все навыки и упражнения завершены!")
    print(f"\n📊 Итого навыков: {len(skills)}")
    print(f"📊 Итого упражнений: {sum(len(exercises[s]) for s in exercises)}")
    print(f"📅 Период расписания: {schedule.start_date} — {schedule.end_date}")
    print(f"⏱️  Общее время: {schedule.total_duration}")
    print("\n🎉 Поздравляю! Вы прошли SkillMap!")
