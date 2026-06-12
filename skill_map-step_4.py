# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SkillMap
def edit_skill_entry(skill_id: int, updates: dict) -> bool:
    if not isinstance(updates, dict):
        raise ValueError("Updates must be a dictionary")
    
    for key in ["name", "description", "level", "schedule"]:
        if key in updates and updates[key] is None:
            del updates[key]
    
    try:
        index = next((i for i, s in enumerate(all_skills) if s["id"] == skill_id), -1)
        if index == -1:
            return False
        
        all_skills[index].update({k: v for k, v in updates.items() if k in all_skills[index]})
        
        # Сохранение в файл (предполагается существование функции save_to_file или глобальной переменной)
        with open("skillmap_data.json", "w", encoding="utf-8") as f:
            json.dump(all_skills, f, ensure_ascii=False, indent=2)
        
        print(f"Skill #{skill_id} updated successfully.")
        return True
        
    except Exception as e:
        print(f"Error updating skill: {e}")
        return False
