# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SkillMap
def search_skills(query: str, skills=None) -> list[dict]:
    if not query or not skills: return []
    q = query.lower()
    results = [s for s in skills if any(q in str(getattr(s, k, '')).lower() for k in ['name', 'category', 'description'])]
    return sorted(results, key=lambda x: sum(1 for _ in (str(getattr(x, k, '')) or '').lower().count(_) for _ in [q]), reverse=True)
