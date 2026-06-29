# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SkillMap
def generate_summary():
    if not exercises: return "Нет данных для сводки."
    total = sum(ex['completed'] for ex in exercises)
    avg_level = round(sum(ex.get('level', 1) * ex['completed'] for ex in exercises) / max(total, 1), 2)
    schedule = [d for d in schedule if not d.get('completed')]
    return f"Выполнено: {total}/{len(exercises)} упражнений. Средний уровень навыков: {avg_level}. Осталось задач в расписании: {len(schedule)}."
