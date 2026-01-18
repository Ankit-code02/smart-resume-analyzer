def profile_level(match_score):
    if match_score < 40:
        return "Beginner"
    elif match_score < 70:
        return "Intermediate"
    else:
        return "Strong"


def ai_insights(level, missing_skills):
    insights = []

    if level == "Beginner":
        insights.append("Your profile is at an early stage. Focus on core technical skills.")
    elif level == "Intermediate":
        insights.append("You have a decent profile. Strengthening a few skills will improve your chances.")
    else:
        insights.append("Strong profile. Focus on interview preparation and advanced topics.")

    if missing_skills:
        insights.append(
            "Recommended to learn: " + ", ".join(missing_skills[:5])
        )
    else:
        insights.append("Your skills match well with the job requirements.")

    return insights
