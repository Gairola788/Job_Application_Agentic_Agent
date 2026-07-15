from langgraph.graph import StateGraph, START, END

from graph.state import JobApplicationState

from nodes.parse_jd import parse_jd
from nodes.parse_resume import parse_resume
from nodes.extract_resume_skills import extract_resume_skills
from nodes.extract_jd_skills import extract_jd_skills
from nodes.calculate_score import calculate_score
from graph.routing import route_application

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

builder.add_node(
    "calculate_score",
     calculate_score         
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
    "calculate_score"
)

builder.add_edge(
    "extract_jd_skills",
    "calculate_score"
)


builder.add_conditional_edges(
    "calculate_score",
    route_application,
    {
        "generate_cover_letter": "generate_cover_letter",
        "resume_feedback": "resume_feedback",
    }
)

graph = builder.compile()

