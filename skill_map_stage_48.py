# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SkillMap
def _format_skill_summary(skill):
    """Compact human-readable summary for a single skill."""
    if not skill:
        return "(нет навыков)"
    parts = []
    for s in skill:
        level = s.level if s.level else 0
        parts.append(f"{s.name} [{level}/5]")
    return " | ".join(parts)
