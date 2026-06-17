# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SkillMap
def sort_records(records, key='date'):
    if not records: return []
    reverse = {'date': False, 'priority': True, 'name': False}.get(key, False)
    def _sort_key(r):
        val = r.get(key, '')
        if isinstance(val, str): return (0, len(val), val.lower())
        if key == 'priority': return (-val, 0, '')
        return (1, 0, '')
    return sorted(records, key=_sort_key, reverse=reverse)
