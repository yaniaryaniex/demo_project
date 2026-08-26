# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SkillMap
def test_skillmap_edge_cases():
    from skillmap import SkillMap, Exercise, SkillLevel, Schedule, Progress

    sm = SkillMap()

    # 1. Тест на создание с невалидным уровнем
    try:
        sm.add_skill("test", Exercise("test", "desc", 0, 0))
        sm.add_skill_level("test", SkillLevel(0))
        sm.add_schedule("test", Schedule("invalid"))
        sm.add_progress("test", Progress("invalid"))
    except ValueError:
        pass

    # 2. Тест на создание с невалидным временем
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("25:00"))
    sm.add_progress("test", Progress(0, 0, 0, 0))
    assert sm.get_schedule("test") == Schedule("23:00")

    # 3. Тест на создание с невалидным прогрессом
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("12:00"))
    sm.add_progress("test", Progress(0, -1, 0, 0))
    assert sm.get_progress("test") == Progress(0, 0, 0, 0)

    # 4. Тест на создание с невалидным расписанием
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("12:00"))
    sm.add_progress("test", Progress(0, 0, 0, 0))
    assert sm.get_schedule("test") == Schedule("12:00")

    # 5. Тест на создание с невалидным уровнем
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("12:00"))
    sm.add_progress("test", Progress(0, 0, 0, 0))
    assert sm.get_skill_level("test") == SkillLevel(0)

    # 6. Тест на создание с невалидным упражнением
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("12:00"))
    sm.add_progress("test", Progress(0, 0, 0, 0))
    assert sm.get_skill("test") == Exercise("test", "desc", 0, 0)

    # 7. Тест на создание с невалидным навыком
    sm.add_skill("test", Exercise("test", "desc", 0, 0))
    sm.add_skill_level("test", SkillLevel(0))
    sm.add_schedule("test", Schedule("12:00"))
    sm.add_progress("test", Progress(0, 0, 0, 0))
    assert sm.get_progress("test") == Progress(0, 0, 0, 0)
