# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SkillMap
def delete_skill(skill_id: int) -> bool:
    """Удалить навык по ID, если он существует."""
    if skill_id not in SKILLS:
        print(f"Ошибка: Навык с id={skill_id} не найден.")
        return False
    
    del SKILLS[skill_id]
    
    # Удаляем связанные упражнения и прогресс для этого навыка
    for exercise_id, data in list(EXERCISES.items()):
        if data.get('skill_id') == skill_id:
            del EXERCISES[exercise_id]
            
    return True

def delete_exercise(exercise_id: int) -> bool:
    """Удалить упражнение по ID."""
    if exercise_id not in EXERCISES:
        print(f"Ошибка: Упражнение с id={exercise_id} не найдено.")
        return False
    
    del EXERCISES[exercise_id]
    
    # Удаляем прогресс, если он был привязан к этому упражнению
    if exercise_id in PROGRESS_LOG:
        del PROGRESS_LOG[exercise_id]
        
    return True

def delete_schedule_entry(schedule_id: int) -> bool:
    """Удалить запись расписания по ID."""
    if schedule_id not in SCHEDULE_ENTRIES:
        print(f"Ошибка: Запись расписания с id={schedule_id} не найдена.")
        return False
    
    del SCHEDULE_ENTRIES[schedule_id]
    
    # Удаляем связанные прогресс-логи, если они привязаны к этой записи (опционально)
    for log_id in list(PROGRESS_LOG.keys()):
        if PROGRESS_LOG[log_id].get('schedule_id') == schedule_id:
            del PROGRESS_LOG[log_id]
            
    return True

def delete_user_progress(user_id: int, exercise_id: int) -> bool:
    """Удалить запись прогресса пользователя."""
    log_key = f"{user_id}_{exercise_id}"
    
    if log_key not in PROGRESS_LOG:
        print(f"Ошибка: Запись прогресса {log_key} не найдена.")
        return False
    
    del PROGRESS_LOG[log_key]
    
    # Если упражнение больше не имеет активных записей, можно удалить само упражнение (опционально)
    if exercise_id in EXERCISES and not any(p.get('user_id') == user_id for p in get_exercise_progress(exercise_id)):
        del EXERCISES[exercise_id]
        
    return True
