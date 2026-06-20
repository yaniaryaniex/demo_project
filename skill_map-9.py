# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SkillMap
import json, uuid, datetime as dt

INITIAL_DATA = '''
{
  "skills": [
    {"id": "py", "name": "Python", "levels": [{"level": 1, "exercises": ["print()", "variables"]}]},
    {"id": "js", "name": "JavaScript", "levels": [{"level": 1, "exercises": ["console.log()", "functions"]}]}]
  },
  "schedule": {
    "monday": ["py"], "wednesday": ["js"], "friday": ["py", "js"]
  }
}'''

def load_initial_data(data_str: str) -> dict:
    try:
        return json.loads(data_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in initial data: {e}") from e

def generate_unique_id() -> str:
    return f"{uuid.uuid4().hex[:8]}"

def get_today_schedule(schedule_data: dict, current_date: dt.date) -> list[str]:
    day_name = current_date.strftime("%A").lower()
    if day_name in schedule_data:
        return [skill_id for skill_id in schedule_data[day_name] if skill_id in ["py", "js"]]
    return []

def get_current_level_progress(skill_id: str, levels_data: list) -> int:
    current_level = 0
    for level_info in levels_data:
        if level_info["level"] == 1 and len(level_info.get("exercises", [])) > 0:
            current_level += 1
    return current_level

def initialize_user_state(user_id: str, data: dict) -> dict:
    today = dt.date.today()
    schedule_for_today = get_today_schedule(data["schedule"], today)
    
    user_progress = {
        "user_id": user_id,
        "completed_exercises": [],
        "current_level": 1,
        "last_login": str(today),
        "today_tasks": []
    }
    
    for skill in data["skills"]:
        if skill["id"] in schedule_for_today:
            level_info = next((lvl for lvl in skill["levels"] if lvl["level"] == 1), None)
            if level_info and len(level_info.get("exercises", [])) > 0:
                user_progress["today_tasks"].append({
                    "skill_id": skill["id"],
                    "exercise_name": level_info["exercises"][0],
                    "status": "pending"
                })
    
    return {**data, "user_state": user_progress}

if __name__ == "__main__":
    data = load_initial_data(INITIAL_DATA)
    initialized_data = initialize_user_state(generate_unique_id(), data)
    print(json.dumps(initialized_data, indent=2))
