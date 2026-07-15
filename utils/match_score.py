from prompts.score_eval_prompt import MATCH_SCORE_PROMPT
import json
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def calculate_match_score(
    resume_text: str,
    resume_skills: list[str],
    jd_text: str,
    jd_skills: list[str]
) -> dict:

    prompt = MATCH_SCORE_PROMPT.format(
        resume_text=resume_text,
        resume_skills=", ".join(resume_skills),
        jd_text=jd_text,
        jd_skills=", ".join(jd_skills)
    )

    try:

        response = llm.invoke(prompt)

        content = response.content.strip()

        # Remove markdown code fences if present
        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        result = json.loads(content)

        return result

    except Exception as e:

        print(f"[Match Score] Error: {e}")

        return {
            "score": 0,
            "reason": "Unable to calculate match score.",
            "strengths": [],
            "missing_skills": []
        }