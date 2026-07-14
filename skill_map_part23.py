# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SkillMap
def show_skill_map_table(skills):
    """Compact console table for SkillMap progress."""
    if not skills:
        print("No data.")
        return
    header = f"{'Skill':<20} {'Level':>6} {'Exp':>5} {'Goal':>8}"
    row_fmt = "{:<20} {:>6} {:>5} {:>8}"
    lines = [header, "-" * len(header)]
    for s in skills:
        lines.append(row_fmt.format(s['name'], s['level'], s.get('xp', 0), s['goal']))
    print("\n".join(lines))

show_skill_map_table(skill_list)
