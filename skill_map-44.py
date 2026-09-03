# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SkillMap
import shutil
from datetime import datetime

def backup_data_file(data_file="skills.json"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{data_file}.backup_{timestamp}"
    shutil.copy2(data_file, backup_file)
    print(f"Backup saved to {backup_file}")
    return backup_file
