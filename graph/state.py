from typing import TypedDict

class JobApplicationState(TypedDict):
    # Input Paths
    resume_path: str
    jd_path: str

    # Extracted Text
    resume_text: str
    jd_text: str

    # Extracted Skills
    resume_skills: list[str]
    jd_skills: list[str]

    # Output
    match_score: float
    match_reason: str
    strengths : list[str]
    missing_skills: list[str]