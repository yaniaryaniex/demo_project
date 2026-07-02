# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SkillMap
def generate_monthly_stats(data, current_date):
    from datetime import timedelta
    start = (current_date.replace(day=1) - timedelta(days=current_date.day)).replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=32).replace(day=1)
    stats = {}
    for d in range((end - start).days):
        date = start + timedelta(days=d)
        day_data = [item for item in data if item['date'] == date.strftime('%Y-%m-%d')]
        completed_count = sum(1 for item in day_data if item.get('completed', False))
        stats[date.strftime('%Y-%m-%d')] = {'total': len(day_data), 'completed': completed_count}
    return stats
