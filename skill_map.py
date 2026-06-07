# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SkillMap
import datetime

class SkillMap:
    def __init__(self):
        self.skills = {}
        self.schedule = []
        self.progress_log = []

    def add_skill(self, name, level=1, exercises=[]):
        if name not in self.skills:
            self.skills[name] = {'level': level, 'exercises': exercises}
        return True

    def log_progress(self, skill_name, exercise_index, status='completed'):
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'skill': skill_name,
            'exercise': exercise_index,
            'status': status
        }
        self.progress_log.append(entry)
        return True

    def get_next_task(self):
        if not self.schedule:
            return None
        task = self.schedule.pop(0)
        return task

    def set_daily_schedule(self, tasks):
        self.schedule.extend(tasks)
        return True

# --- Демонстрационные данные и точка входа ---
if __name__ == "__main__":
    app = SkillMap()
    
    # Добавляем навыки
    app.add_skill("Python", level=1, exercises=["Основы синтаксиса", "Типы данных", "Условия"])
    app.add_skill("Git", level=1, exercises=["Инициализация репозитория", "Коммиты и пулы", "Разрешение конфликтов"])
    
    # Устанавливаем расписание на сегодня
    today = datetime.datetime.now().date()
    app.set_daily_schedule([
        {"skill": "Python", "exercise": 0, "time": "10:00"},
        {"skill": "Git", "exercise": 0, "time": "14:00"}
    ])
    
    # Выполняем первое задание и логируем прогресс
    task = app.get_next_task()
    if task:
        print(f"Текущая задача: {task['skill']} - {task['exercise']}")
        app.log_progress(task['skill'], task['exercise'])
        print("Задача выполнена. Прогресс сохранен.")
    
    # Вывод текущего уровня навыков
    for skill, data in app.skills.items():
        print(f"Навык: {skill}, Уровень: {data['level']}")
