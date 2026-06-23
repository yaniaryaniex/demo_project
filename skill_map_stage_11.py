# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SkillMap
import json, os

DATA_FILE = "skillmap_data.json"

def save_state(state):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Error] Failed to save data: {e}")
        return False

def load_state():
    if not os.path.exists(DATA_FILE):
        return None
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error] Failed to load data: {e}")
        return None

def init_default_state():
    default = {
        "skills": {},
        "schedule": [],
        "completed_exercises": []
    }
    save_state(default)
    return default
