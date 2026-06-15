# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SkillMap
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record['status'] != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags:
            record_tags = set(record.get('tags', [])).intersection(tags)
            if not record_tags:
                continue
        filtered.append(record)
    return filtered

if __name__ == "__main__":
    print("Все записи:", records[:3])
    print("\nФильтр по статусу 'completed':", filter_records(status='completed'))
    print("\nФильтр по категории 'math':", filter_records(category='math'))
    print("\nФильтр по тегам {'hard', 'new'}:", filter_records(tags={'hard', 'new'}))
