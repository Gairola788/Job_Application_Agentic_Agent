from langgraph.graph import StateGraph, START, END

from graph.state import JobApplicationState

from nodes.parse_jd import parse_jd
from nodes.parse_resume import parse_resume
from nodes.extract_resume_skills import extract_resume_skills
from nodes.extract_jd_skills import extract_jd_skills

builder = StateGraph(JobApplicationState)

builder.add_node(
    "parse_resume",
    parse_resume
)

builder.add_node(
    "parse_jd",
    parse_jd
)

builder.add_node(
    "extract_resume_skills",
     extract_resume_skills
)

builder.add_node(
    "extract_jd_skills",
     extract_jd_skills
)

builder.add_edge(
    START,
    "parse_resume"
)

builder.add_edge(
    START,
    "parse_jd"
)

builder.add_edge(
    "parse_resume",
    "extract_resume_skills"
)

builder.add_edge(
    "parse_jd",
    "extract_jd_skills"
)

builder.add_edge(
    "extract_resume_skills",
    END
)

builder.add_edge(
    "extract_jd_skills",
    END
)

graph = builder.compile()

