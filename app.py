import os
import sys

# ensure project root is in path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template, request
from utils.file_reader import read_resume
from utils.skill_extractor import extract_skills, format_skills
from utils.matcher import calculate_match_score
from utils.profile_analyzer import profile_level, ai_insights
from utils.learning_resources import get_learning_links

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume_file = request.files.get("resume_file")
        job_text = request.form.get("job_text")

        resume_text = ""

        if resume_file and resume_file.filename:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
            resume_file.save(file_path)
            resume_text = read_resume(file_path)

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)

        missing_skills = list(set(job_skills) - set(resume_skills))

        resume_skills = format_skills(resume_skills)
        missing_skills = format_skills(missing_skills)

        match_score = calculate_match_score(resume_text, job_text)
        level = profile_level(match_score)
        insights = ai_insights(level, missing_skills)
        learning_links = get_learning_links(missing_skills, level)

        result = {
            "match_score": match_score,
    "profile_level": level,
    "resume_skills": resume_skills,
    "missing_skills": missing_skills,
    "insights": insights,
    "learning_links": learning_links
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
