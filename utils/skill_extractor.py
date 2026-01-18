import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

# Basic skill list (we will expand later)
SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "machine learning",
    "data science", "flask", "django", "git", "api",
    "html", "css", "javascript"
]


def extract_skills(text):
    text = text.lower()

    found = set()

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found.add(skill)

    return list(found)


if __name__ == "__main__":
    sample_text = """
    I have experience in Python, Flask, Machine Learning and SQL.
    I also used Git and worked with APIs.
    """

    print(extract_skills(sample_text))
    
def format_skills(skills):
    return [skill.upper() if skill.isupper() else skill.capitalize() for skill in skills]
