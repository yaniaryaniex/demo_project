# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SkillMap
def paginate(items, page_size=10):
    """Returns a generator yielding pages of items as lists of dicts with pagination metadata."""
    total = len(items)
    total_pages = max(1, (total + page_size - 1) // page_size)
    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        page = items[start:end]
        yield {
            "page": i + 1,
            "total_pages": total_pages,
            "total_items": total,
            "items": page,
            "has_next": i + 1 < total_pages,
            "has_prev": i > 0,
        }
