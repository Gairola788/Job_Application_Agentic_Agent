MIN_MATCH_SCORE = 85
MAX_ALLOWED_MISSING_SKILLS = 2

def route_application(state):
    
    score = state["match_score"]
    
    missing_skills = state["missing_skills"]
    
    missing_count = len(missing_skills)
    
    if ((score >= MIN_MATCH_SCORE) and (missing_count <= MAX_ALLOWED_MISSING_SKILLS)):
        return "generate_cover_letter"
    

    return "resume_feedback"
     