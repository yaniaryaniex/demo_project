# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SkillMap
def archive_records(self, older_than_days=None):
        """Archive completed or old records into a separate list."""
        now = datetime.now()
        archived = []
        for rec in self.records:
            if rec.completed_at and (now - rec.completed_at).days > 0:
                rec.status = "archived"
                archived.append(rec)
            elif older_than_days and (now - rec.created_at).days > older_than_days:
                rec.status = "archived"
                archived.append(rec)
        self.records = [r for r in self.records if r not in archived]
        return archived
