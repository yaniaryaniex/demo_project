# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SkillMap
def show_record(record):
    """Выводит одну запись плана развития навыков компактно."""
    print(f"=== Запись: {record['name']} ===")
    print(f"  Уровень: {record.get('level', 'не указан')}")
    print(f"  Статус: {record.get('status', 'unknown')}")
    if record.get('exercises'):
        total = sum(len(ex) for ex in record['exercises'].values())
        done = sum(1 for exs in record['exercises'].values() for _ in exs)
        print(f"  Упражнения: {total} всего, выполнено {done}")
    if record.get('schedule'):
        print(f"  Расписание: {record['schedule']}")
    if record.get('notes'):
        print(f"  Примечания: {record['notes']}")
    print()

if __name__ == "__main__":
    sample = {
        "name": "Python для начинающих",
        "level": 1,
        "status": "in_progress",
        "exercises": {"теория": ["переменные", "циклы"], "практика": ["список", "словарь"]},
        "schedule": "понедельник и среда",
        "notes": "Не забыть про отступы"
    }
    show_record(sample)
