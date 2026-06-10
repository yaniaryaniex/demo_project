# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SkillMap
class SkillMapState:
    def __init__(self):
        self.skills = {}  # {skill_name: {'level': int, 'progress': float}}
        self.exercises = []  # [{'skill': str, 'done': bool, 'date': str}]
        self.schedule = []  # [{'day': str, 'task': str, 'status': str}]

    def add_skill(self, name: str, level: int = 1):
        if name not in self.skills:
            self.skills[name] = {'level': level, 'progress': 0.0}
        else:
            self.skills[name]['level'] = max(self.skills[name]['level'], level)

    def add_exercise(self, skill_name: str, done: bool = False):
        self.exercises.append({
            'skill': skill_name,
            'done': done,
            'date': self._get_today()
        })

    def add_schedule_task(self, day: str, task: str, status: str = 'pending'):
        self.schedule.append({'day': day, 'task': task, 'status': status})

    def _get_today(self) -> str:
        import datetime
        return datetime.date.today().isoformat()

    def save_state(self):
        # В будущем можно заменить на сохранение в файл или БД
        print("Состояние сохранено в памяти.")

    def get_progress(self, skill_name: str) -> float:
        if skill_name in self.skills:
            return self.skills[skill_name]['progress']
        return 0.0
