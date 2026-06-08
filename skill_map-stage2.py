# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SkillMap
class Skill:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def validate(self):
        if not isinstance(self.name, str) or len(self.name.strip()) == 0:
            raise ValueError("Название навыка должно быть непустой строкой.")
        if not isinstance(self.level, int) or self.level < 1:
            raise ValueError("Уровень должен быть целым числом больше или равным 1.")

class Exercise:
    def __init__(self, skill_name, duration_minutes):
        self.skill_name = skill_name
        self.duration_minutes = duration_minutes

    def validate(self):
        if not isinstance(self.skill_name, str) or len(self.skill_name.strip()) == 0:
            raise ValueError("Название навыка для упражнения должно быть непустой строкой.")
        if not isinstance(self.duration_minutes, (int, float)) or self.duration_minutes <= 0:
            raise ValueError("Длительность упражнения должна быть положительным числом.")

class ScheduleItem:
    def __init__(self, exercise, day_of_week):
        self.exercise = exercise
        self.day_of_week = day_of_week

    def validate(self):
        if not isinstance(self.day_of_week, int) or not (1 <= self.day_of_week <= 7):
            raise ValueError("День недели должен быть целым числом от 1 до 7.")
