# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SkillMap
def print_metrics():
    total_exercises = sum(len(ex) for ex in exercises.values())
    completed = sum(1 for level in levels.values() for ex in level.get('exercises', []) if ex['status'] == 'done')
    avg_level = sum(level.get('level', 0) for level in levels.values()) / len(levels) if levels else 0
    schedule_days = sum(s['days_left'] for s in schedules.values()) if schedules else 0
    print(f"Total exercises: {total_exercises}")
    print(f"Completed: {completed} ({100*completed/total_exercises:.1f}%)" if total_exercises else "No exercises yet")
    print(f"Avg level reached: {avg_level:.1f}" if avg_level else "Not started")
    print(f"Scheduled days remaining: {schedule_days}" if schedule_days else "Nothing scheduled")
