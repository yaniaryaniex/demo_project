# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SkillMap
import json, os, uuid

class Profile:
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.name = input("Имя профиля: ")
        self.skills = {}
        self.schedule = []
        
    def save(self, path='profiles.json'):
        with open(path, 'w') as f:
            json.dump({self.id: {'name': self.name, 'skills': self.skills}}, f)

def load_profile(path='profiles.json'):
    if not os.path.exists(path): return None
    with open(path) as f: return json.load(f)
