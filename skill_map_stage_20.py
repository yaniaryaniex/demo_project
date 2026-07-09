# === Stage 20: Добавь восстановление записей из архива ===
# Project: SkillMap
import json, os

ARCHIVE_FILE = "skillmap_archive.json"

def restore_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        print("Archive file not found.")
        return False
    with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    if isinstance(archive, list):
        for entry in archive:
            _merge_entry(entry)
        print("Restored entries from archive.")
        return True
    elif isinstance(archive, dict) and "entries" in archive:
        for entry in archive["entries"]:
            _merge_entry(entry)
        print("Restored entries from archive.")
        return True
    else:
        print("Invalid archive format.")
        return False

def _merge_entry(entry):
    if "id" not in entry:
        import uuid
        entry["id"] = str(uuid.uuid4())
    for key, value in entry.items():
        if key not in ("_restored", "_archived_at"):
            if key in SKILL_MAP_DATA and isinstance(SKILL_MAP_DATA[key], list):
                if not any(e.get("id") == entry["id"] for e in SKILL_MAP_DATA[key]):
                    SKILL_MAP_DATA[key].append(entry)
            else:
                existing = SKILL_MAP_DATA.setdefault(key, {})
                merged = {**existing, **value}
                SKILL_MAP_DATA[key] = merged
