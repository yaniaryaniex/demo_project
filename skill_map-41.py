# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SkillMap
def dry_run(operation, *args, **kwargs):
    """Dry-run режим: выполняет операцию в памяти, не сохраняя."""
    if operation == "add_skill":
        return SkillMap._add_skill_dry(*args, **kwargs)
    elif operation == "add_exercise":
        return SkillMap._add_exercise_dry(*args, **kwargs)
    elif operation == "add_schedule":
        return SkillMap._add_schedule_dry(*args, **kwargs)
    elif operation == "add_level":
        return SkillMap._add_level_dry(*args, **kwargs)
    elif operation == "add_progress":
        return SkillMap._add_progress_dry(*args, **kwargs)
    elif operation == "add_streak":
        return SkillMap._add_streak_dry(*args, **kwargs)
    elif operation == "add_comment":
        return SkillMap._add_comment_dry(*args, **kwargs)
    elif operation == "add_starter":
        return SkillMap._add_starter_dry(*args, **kwargs)
    else:
        raise ValueError(f"Unknown dry-run operation: {operation}")
