# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SkillMap
def export_state():
    import json
    state = {
        "skills": skills,
        "exercises": exercises,
        "levels": levels,
        "schedule": schedule,
        "progress": progress,
        "settings": settings
    }
    return json.dumps(state, indent=2)
