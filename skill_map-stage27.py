# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SkillMap
def reset_demo_data():
    """Сбрасывает все данные в состояние демо-запуска."""
    global _skills, _exercises, _schedule, _progress, _levels
    _skills = [Skill("Python", "Основа программирования", 1)]
    _exercises = {}
    for skill in _skills:
        _exercises[skill.name] = {f"drill_{i}" for i in range(3)}
        _progress[skill.name] = {"drill_0": 0, "drill_1": 0, "drill_2": 0}
    _schedule = {}
    _levels = {}

def clear_state():
    """Полностью очищает все данные приложения."""
    global _skills, _exercises, _schedule, _progress, _levels
    _skills = []
    _exercises = {}
    _schedule = {}
    _progress = {}
    _levels = {}
