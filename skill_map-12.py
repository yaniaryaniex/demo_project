# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SkillMap
def load_skills_from_file(file_path: str) -> list[dict]:
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON должен содержать массив навыков")
            return [skill for skill in data if isinstance(skill, dict)]
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла {file_path}: {type(e).__name__}")
        return []
