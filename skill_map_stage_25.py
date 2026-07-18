# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SkillMap
def validate_date(date_str, fmt="%Y-%m-%d"):
    """Проверяет корректность даты по шаблону и возвращает дату или сообщение об ошибке."""
    if not date_str or not isinstance(date_str, str):
        return "Ошибка: дата должна быть строкой"
    try:
        year, month, day = map(int, date_str.split("-"))
        import datetime as dt
        dt.date(year, month, day)
        return f"{year}-{month}-{day}"
    except (ValueError, AttributeError):
        return "Ошибка: некорректный формат даты. Используйте YYYY-MM-DD"

# Пример использования:
test_dates = ["2024-13-01", "abc-def-ghi", "", "2024-05-15"]
for d in test_dates:
    print(validate_date(d))
