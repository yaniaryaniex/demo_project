# === Stage 32: Добавь журнал действий пользователя ===
# Project: SkillMap
class ActionLog:
    """Compact user action journal for SkillMap."""

    def __init__(self):
        self._entries = []

    @property
    def entries(self):
        return list(self._entries)

    def log(self, action_type, detail="", timestamp=None):
        from datetime import datetime
        if timestamp is None:
            timestamp = datetime.now()
        entry = {
            "timestamp": timestamp.isoformat(),
            "type": action_type,
            "detail": detail,
            "id": len(self._entries) + 1,
        }
        self._entries.append(entry)
        return entry

    def get_recent(self, count=10):
        return list(reversed(self._entries[-count:])) if self._entries else []

    def clear(self):
        self._entries.clear()

    def summary(self):
        types = {}
        for e in self._entries:
            t = e["type"]
            types[t] = types.get(t, 0) + 1
        return dict(sorted(types.items()))
