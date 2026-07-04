# === Stage 17: Добавь группировку записей по категориям ===
# Project: SkillMap
from collections import defaultdict, Counter

def group_by_category(records: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    for record in records:
        cat = record.get("category", "Uncategorized")
        grouped[cat].append(record)
    
    # Сортируем категории по количеству записей (убывание), затем алфавитно
    sorted_categories = sorted(grouped.items(), key=lambda x: (-len(x[1]), x[0]))
    return dict(sorted_categories)

def get_category_stats(records: list[dict]) -> Counter:
    categories = [r.get("category", "Uncategorized") for r in records]
    return Counter(categories)
