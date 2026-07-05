# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SkillMap
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: count}
    
    def add_tag(self, tag_name: str) -> bool:
        if not tag_name.strip():
            return False
        self.tags[tag_name] = self.tags.get(tag_name, 0) + 1
        return True
    
    def remove_tag(self, tag_name: str) -> int:
        count = self.tags.pop(tag_name, None)
        return count if count is not None else -1
