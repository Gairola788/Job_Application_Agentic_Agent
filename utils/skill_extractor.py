import json
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.skill_extraction_prompt import SKILL_EXTRACTION_PROMPT

# Load environment variables
load_dotenv()

# Initialize the LLM only once
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_skills_from_text(text: str) -> list[str]:
    """
    Extracts technical skills from any given text using a Groq LLM.

    Args:
        text (str): Resume text, JD text, or any technical document.

    Returns:
        list[str]: List of extracted technical skills.
    """

    prompt = SKILL_EXTRACTION_PROMPT.format(text=text)

    try:
        response = llm.invoke(prompt)

        # Extract the actual text from AIMessage
        content = response.content.strip()

        # Convert JSON string into Python list
        skills = json.loads(content)

        return skills

    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []