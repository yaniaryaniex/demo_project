# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SkillMap
def check_overdue_reminders():
    """Проверяет просроченные напоминания и возвращает список."""
    overdue = []
    now = datetime.now()
    for reminder in reminders:
        if reminder["time"] < now and not reminder["delivered"]:
            overdue.append(reminder)
    return overdue

reminders = [
    {"task": "Практика Python", "time": datetime(2024, 1, 15), "delivered": False},
    {"task": "Изучение Git", "time": datetime(2024, 1, 20), "delivered": True},
]

print("Просроченные напоминания:", check_overdue_reminders())
