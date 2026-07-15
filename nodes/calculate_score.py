from utils.match_score import calculate_match_score

def calculate_score(state):
    
    result = calculate_match_score(
        resume_text=state["resume_text"],
        resume_skills=state["resume_skills"],
        jd_text=state["jd_text"],
        jd_skills=state["jd_skills"]
    )
   
    return {
        
     "match_score":  result["score"],
     "match_reason": result["reason"],
     "missing_skills":  result["missing_skills"],
    "strengths": result["strengths"]
    }
    

