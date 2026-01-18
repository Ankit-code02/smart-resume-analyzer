LEARNING_RESOURCES = {
    "python": {
        "beginner": "https://www.learnpython.org/",
        "advanced": "https://docs.python.org/3/tutorial/"
    },
    "c++": {
        "beginner": "https://www.learncpp.com/",
        "advanced": "https://cplusplus.com/doc/tutorial/"
    },
    "java": {
        "beginner": "https://www.w3schools.com/java/",
        "advanced": "https://docs.oracle.com/javase/tutorial/"
    },
    "javascript": {
        "beginner": "https://www.javascript.info/",
        "advanced": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
    },
    "sql": {
        "beginner": "https://sqlbolt.com/",
        "advanced": "https://mode.com/sql-tutorial/"
    }
}


def get_learning_links(skills, level):
    recommendations = []

    for skill in skills:
        skill = skill.lower()
        if skill in LEARNING_RESOURCES:
            link = (
                LEARNING_RESOURCES[skill]["beginner"]
                if level != "Strong"
                else LEARNING_RESOURCES[skill]["advanced"]
            )
            recommendations.append({
                "skill": skill,
                "link": link
            })

    return recommendations
