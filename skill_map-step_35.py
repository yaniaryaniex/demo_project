# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: SkillMap
def get_next_action(user: User, skills: list[Skill], progress: dict[str, Progress]) -> str:
    """Generate a recommendation based on current state."""
    if not user.scheduled_tasks and not any(p.completed > 0 for p in progress.values()):
        return "Start with SkillMap basics — complete the first exercise of each skill."

    pending = [s for s in skills if p.completed == 0 for p in progress.values() if p.skill_name == s.name]
    if pending:
        best = min(pending, key=lambda s: next((p.completed for p in progress.values() if p.skill_name == s.name), 0) or float('inf'))
        return f"Next: {best.name} — complete its first exercise."

    completed_skills = [s for s in skills if any(p.completed > 0 for p in progress.values() if p.skill_name == s.name)]
    if len(completed_skills) < len(skills):
        next_skill = min(set(skills) - set(completed_skills), key=lambda s: s.priority or 1)
        return f"Move to {next_skill.name} — it's the highest priority skill you haven't started."

    overdue = [t for t in user.scheduled_tasks if datetime.now() > t.deadline]
    if overdue:
        next_task = max(overdue, key=lambda t: (datetime.now() - t.deadline).total_seconds())
        return f"Overdue task: {next_task.title} — complete it now."

    today_tasks = [t for t in user.scheduled_tasks if t.date == datetime.today().date()]
    if not today_tasks and user.scheduled_tasks:
        tomorrow = min(user.scheduled_tasks, key=lambda t: (datetime.now() - t.deadline).total_seconds())
        return f"Prepare for tomorrow: {tomorrow.title} — review its prerequisites."

    return "You're up to date! Consider reviewing your progress and setting new goals."
