# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SkillMap
def repair_data(data):
    """Check integrity and fix simple problems in the data structure."""
    if not isinstance(data, dict) or 'skills' not in data:
        return {'error': 'Invalid data format', 'data': {}}
    
    skills = data['skills']
    fixed_skills = 0
    
    for i, skill in enumerate(skills):
        if not isinstance(skill, dict):
            skill = {'name': f'Unknown Skill', 'level': 1, 'exercises': [], 'schedule': []}
        
        # Fix missing fields
        if 'level' not in skill:
            skill['level'] = 1
        
        if 'exercises' not in skill:
            skill['exercises'] = []
        
        # Fix exercise structure
        for j, ex in enumerate(skill['exercises']):
            if isinstance(ex, dict):
                if 'name' not in ex or 'completed' not in ex:
                    ex.update({'name': f'Repaired Exercise {j}', 'completed': False})
            
            elif isinstance(ex, str) and len(ex.strip()) == 0:
                skill['exercises'].pop(j)
        
        # Fix schedule entries
        if 'schedule' not in skill:
            skill['schedule'] = []
    
    data['skills'] = skills
    
    return {'status': 'repaired', 'fixed_count': fixed_skills, 'data': data}

# Test the repair function
test_data = {
    'skills': [
        {'name': 'Python Basics', 'level': 5, 'exercises': ['Variable declaration', '', 'Loop practice'], 'schedule': ['Monday']},
        None,
        {'name': 'Data Structures', 'level': 3, 'exercises': [{'name': 'Arrays', 'completed': True}]},
    ]
}

print(repair_data(test_data))
