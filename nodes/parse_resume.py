from utils.file_reader import read_pdf

def parse_resume(state):
    resume_path = state["resume_path"]

    resume_text = read_pdf(resume_path)
    
    return {
        "resume_text": resume_text
    }