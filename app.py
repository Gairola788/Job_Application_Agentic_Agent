from graph.builder import graph
from graph.state import JobApplicationState
from pprint import pprint

# initial_state = {
#     "resume_path": "data/AkshatResume.pdf",
#     "jd_path": "data/JD.txt",

#     "resume_text": "",
#     "jd_text": "",

#     "resume_skills": [],
#     "jd_skills": [],

#     "match_score": 0.0
# }
  
# """->Better autocomplete in VS Code
# ->Type checking"""

initial_state: JobApplicationState = {
    "resume_path": "data/AkshatResume.pdf",
    "jd_path": "data/JD.txt",

    "resume_text": "",
    "jd_text": "",

    "resume_skills": [],
    "jd_skills": [],

    "match_score": 0.0
}


result = graph.invoke(initial_state)

# # pprint(result)

# print("=" * 50)
# print("Resume Preview")
# print("=" * 50)

# print(result["jd_text"][:800])






# from utils.skill_extractor import extract_skills_from_text

# //testing skill extraction
# sample_text = """

# hey de72e8ysicnsjcnsmcscmsmc  hzzhgd
# """

# skills = extract_skills_from_text(sample_text)

print(result["jd_skills"])
print(result["resume_skills"])

# Experienced Python developer with expertise in FastAPI,
# LangGraph, Docker, SQL, Git, TensorFlow and AWS.