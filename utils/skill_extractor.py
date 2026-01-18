# utils/skill_extractor.py

SKILLS_DB = [
    "python", "java", "c++", "javascript", "html", "css",
    "sql", "git", "api", "flask", "django", "react",
    "node", "mongodb", "machine learning", "data analysis"
]

def extract_skills(text):
    if not text:
        return []

    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def format_skills(skills):
    return [skill.title() for skill in skills]
