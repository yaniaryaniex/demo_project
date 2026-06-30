# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SkillMap
def calculate_weekly_stats(stats_by_date):
    from datetime import date, timedelta
    if not stats_by_date: return {}
    min_d = min(stats_by_date.keys())
    max_d = max(stats_by_date.keys())
    week_start = (min_d - timedelta(days=min_d.weekday())).date()
    week_end = week_start + timedelta(days=6)
    weekly_totals = {d.date(): 0 for d in range(week_start, week_end+1)}
    for d_str, data in stats_by_date.items():
        try:
            d = date.fromisoformat(d_str)
            if week_start <= d <= week_end:
                for skill_name, count in data.get('completed_exercises', {}).items():
                    weekly_totals[d.date()] += int(count)
        except ValueError: continue
    return {str(k): v for k, v in sorted(weekly_totals.items())}
