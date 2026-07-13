SKILL_EXTRACTION_PROMPT = """You are an expert resume analyzer.

Your task is to extract only the technical skills mentioned in the given text.

Instructions:

1. Extract programming languages.
2. Extract frameworks.
3. Extract libraries.
4. Extract databases.
5. Extract cloud platforms.
6. Extract AI/ML tools and frameworks.
7. Extract DevOps and software tools.
8. Ignore communication skills, leadership, teamwork, education, certifications, company names, and project titles unless they are actual technologies.
9. Return ONLY a valid JSON array of strings.
10. If no technical skills are found, return [].

Text:
{text}"""