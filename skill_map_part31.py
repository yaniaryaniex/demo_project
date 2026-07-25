# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SkillMap
import os, json, datetime

def load_json(path): return json.loads(open(path).read()) if os.path.exists(path) else {}
def save_json(path, data): open(path,'w').write(json.dumps(data))
SKILLS_DIR = 'skills'
PROFILES_DIR = 'profiles'

if not os.path.isdir(SKILLS_DIR): os.mkdir(SKILLS_DIR)
if not os.path.isdir(PROFILES_DIR): os.mkdir(PROFILES_DIR)

def get_active_profile():
    defaults = {
        "default": {"name":"Default","skill_id":None,"level":0,"xp":0},
        "student": {"name":"Student","skill_id":None,"level":0,"xp":0},
        "mentor": {"name":"Mentor","skill_id":None,"level":0,"xp":0}
    }
    state = load_json('state.json') if os.path.exists('state.json') else {}
    return defaults.get(state.get("active_profile","default"),defaults["default"])

def set_active_profile(profile_name):
    profiles_path = PROFILES_DIR + '/' + profile_name + '.json'
    if not os.path.exists(profiles_path): save_json(profiles_path, {})
    state = load_json('state.json') if os.path.exists('state.json') else {}
    state["active_profile"] = profile_name
    save_json('state.json', state)

def get_skill_data(skill_id):
    skill_path = SKILLS_DIR + '/' + str(skill_id) + '.json'
    return load_json(skill_path) if os.path.exists(skill_path) else {"skill_id":skill_id,"name":"Unknown","level":0,"xp":0}

def save_skill_data(skill_id, data): save_json(SKILLS_DIR+'/'+str(skill_id)+'.json', data)

def main():
    print('SkillMap v31 — переключение профиля')
    profiles = load_json(PROFILES_DIR + '/list.json') if os.path.exists(PROFILES_DIR+'/list.json') else {"default":True,"student":False,"mentor":False}
    active = get_active_profile()
    print(f'Active: {active["name"]} (profile={active.get("skill_id","?")})')
    for name in profiles:
        marker = ' [ACTIVE]' if name == active.get('skill_id') else ''
        print(f'{name}{marker}')

if __name__=='__main__': main()
