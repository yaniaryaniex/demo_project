# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SkillMap
import json, os, shutil, datetime

BACKUP_DIR = "skillmap_backups"

def ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)

def save_backup(source_path, label="latest"):
    ensure_backup_dir()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{label}_{timestamp}.json"
    dest = os.path.join(BACKUP_DIR, filename)
    shutil.copy2(source_path, dest)
    return dest

def restore_backup(backup_path):
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    return shutil.copy2(backup_path, "skillmap.json")
