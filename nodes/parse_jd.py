
from utils.file_reader import read_txt

def parse_jd(state):
    jd_path = state["jd_path"]

    jd_text = read_txt(jd_path)

    return {
        "jd_text": jd_text
    }