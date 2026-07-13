from utils.skill_extractor import extract_skills_from_text

def extract_jd_skills(state):
    
    jd_Text = state["jd_text"]
    
    jdSkills = extract_skills_from_text(jd_Text)
    
    return {
        "jd_skills" : jdSkills
    }
    
