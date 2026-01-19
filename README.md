🧠 Smart Resume Analyzer

A web-based application that analyzes a candidate’s resume against a given job description, calculates a match score, identifies missing skills, and suggests areas for improvement.

🔗 Live Demo:
https://smart-resume-analyzer-i8q0.onrender.com

⚠️ Note: The app is hosted on Render (free tier). First load may take ~30–50 seconds due to cold start.

🚀 Features

Upload resume in PDF / DOCX / TXT format

Paste any job description

Extracts key skills from resume

Compares resume skills with job requirements

Calculates match percentage

Identifies missing skills

Shows profile strength level (Beginner / Intermediate / Advanced)

Recommends skills to learn for improvement

Clean, responsive, and modern UI

🛠️ Tech Stack

Frontend

HTML5

CSS3 (custom styling, gradients, animations)

Backend

Python

Flask

Libraries & Tools

pdfminer.six (PDF parsing)

python-docx (DOCX parsing)

scikit-learn (skill matching logic)

Git & GitHub

Render (deployment)

⚙️ How It Works (Architecture)

User uploads a resume and enters a job description

Resume text is extracted based on file type (PDF / DOCX / TXT)

A predefined skill database is used to extract skills from resume text

Job description is analyzed for required skills

Resume skills are compared with job skills

Match score and missing skills are calculated

Results are displayed with visual indicators and insights

📂 Project Structure
resume-analyzer/
│
├── app.py
├── requirements.txt
├── uploads/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   ├── file_reader.py
│   ├── skill_extractor.py
│   └── matcher.py
└── README.md

▶️ Run Locally
# Clone the repository
git clone https://github.com/Ankit-code02/smart-resume-analyzer.git

# Move into project directory
cd smart-resume-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py


Open browser and go to:
http://127.0.0.1:5000

🌐 Deployment

Deployed on Render

CI/CD enabled via GitHub

Optimized for free-tier deployment (fast startup, lightweight dependencies)

📈 What I Learned

Building a full-stack Flask web application

Resume parsing and text extraction

Skill-matching logic using real-world job descriptions

Debugging production deployment issues

Managing dependencies for cloud deployment

Git, GitHub, and CI/CD workflow

Writing production-ready code

🔮 Future Improvements

Role-based analysis (Frontend / Backend / ML roles)

Downloadable analysis report (PDF)

User login and history tracking

More advanced NLP-based skill extraction

Resume improvement suggestions section

👤 Author

Ankit Maurya
Final Year Engineering Student
GitHub: https://github.com/Ankit-code02