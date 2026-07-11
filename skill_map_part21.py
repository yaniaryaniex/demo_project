# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SkillMap
from datetime import date, timedelta


def parse_reminder_line(line: str) -> dict | None:
    """Парсит строку напоминания вида 'Название навыка | 2024-12-31' и возвращает словарь."""
    if "|" not in line or len(line.split("|")) != 2:
        return None
    name, day_str = [s.strip() for s in line.split("|")]
    try:
        dt = date.fromisoformat(day_str)
    except ValueError:
        return None
    return {"name": name, "due_date": dt}


def check_reminders(reminders: list[dict], today: date | None = None):
    """Проверяет список напоминаний и возвращает пропущенные сегодня."""
    if today is None:
        today = date.today()
    overdue = [r for r in reminders if r["due_date"] <= today]
    return overdue


def add_reminder(reminders: list[dict], name: str, due_date_str: str) -> dict:
    """Добавляет напоминание и возвращает его."""
    parsed = parse_reminder_line(f"{name} | {due_date_str}")
    if not parsed:
        raise ValueError("Неверный формат напоминания. Используйте 'Название навыка | YYYY-MM-DD'.")
    reminders.append(parsed)
    return parsed


def show_reminders(reminders: list[dict]) -> str:
    """Отображает все напоминания."""
    if not reminders:
        return "Нет запланированных напоминаний."
    lines = [f"{r['due_date']} — {r['name']}" for r in sorted(reminders, key=lambda x: x["due_date"])]
    return "\n".join(lines)


# Пример использования:
if __name__ == "__main__":
    reminders = []
    add_reminder(reminders, "Практика Python", "2025-01-15")
    add_reminder(reminders, "Решение задач на CodeWars", "2025-01-20")
    print(show_reminders(reminders))
