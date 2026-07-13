from utils.skill_extractor import extract_skills_from_text

def extract_resume_skills(state):
    
    resume_Text = state["resume_text"]
    
    resumeSkills = extract_skills_from_text(resume_Text)
    
    return {
        "resume_skills" : resumeSkills
    }
    
