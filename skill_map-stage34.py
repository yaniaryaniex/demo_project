# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SkillMap
class TemplateManager:
    def __init__(self, templates):
        self.templates = {}
        for name, fields in templates.items():
            self.templates[name] = {'fields': fields}

    def create_from_template(self, template_name, **overrides):
        tpl = self.templates[template_name]
        entry = {f: '' if f not in overrides else overrides[f] for f in tpl['fields']}
        return entry
