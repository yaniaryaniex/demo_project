# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SkillMap
# SkillMap v2.0 — добавляем миграцию структуры данных

# Старая версия хранилища (v1)
OLD_SCHEMA = {
    "skills": [
        {"name": "Python", "levels": ["Novice", "Intermediate", "Advanced"], "current_level": 1},
        {"name": "JavaScript", "levels": ["Novice", "Intermediate", "Advanced"], "current_level": 1},
    ],
    "schedule": [
        {"day": "Monday", "skills": ["Python"]},
        {"day": "Tuesday", "skills": ["JavaScript"]},
    ],
    "progress": [
        {"skill": "Python", "completed_exercises": 5},
        {"skill": "JavaScript", "completed_exercises": 3},
    ],
}

# Новая версия хранилища (v2)
NEW_SCHEMA = {
    "skills": [
        {"name": "Python", "levels": ["Novice", "Intermediate", "Advanced", "Expert"], "current_level": 1, "badges": []},
        {"name": "JavaScript", "levels": ["Novice", "Intermediate", "Advanced", "Expert"], "current_level": 1, "badges": []},
    ],
    "schedule": [
        {"day": "Monday", "skills": ["Python"], "estimated_minutes": 60},
        {"day": "Tuesday", "skills": ["JavaScript"], "estimated_minutes": 45},
    ],
    "progress": [
        {"skill": "Python", "completed_exercises": 5, "streak_days": 7},
        {"skill": "JavaScript", "completed_exercises": 3, "streak_days": 4},
    ],
    "version": 2,
}

# Функция миграции
def migrate_old_to_new():
    """Мигрирует данные со старой версии (v1) на новую (v2)."""
    new_data = dict(NEW_SCHEMA)
    for skill in OLD_SCHEMA["skills"]:
        skill["levels"] = ["Novice", "Intermediate", "Advanced", "Expert"]
        skill["current_level"] = 1
        skill["badges"] = []
    for day_schedule in OLD_SCHEMA["schedule"]:
        day_schedule["estimated_minutes"] = 60
    for progress in OLD_SCHEMA["progress"]:
        progress["streak_days"] = 7
    new_data["version"] = 2
    return new_data

# Пример использования
migrated = migrate_old_to_new()
print(f"SkillMap v2 миграция завершена. Текущая версия: {migrated['version']}")
