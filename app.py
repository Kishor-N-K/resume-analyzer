from flask import Flask, render_template, request, redirect, send_file
import os
import pdfplumber
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.corpus import stopwords

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from skills import SKILLS

# Ensure NLTK stopwords
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


# Utility Functions


def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text.lower()


def extract_skills(text):
    found = set()
    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found.add(skill)
    return sorted(found)


def detect_experience(text):
    if any(k in text for k in ["senior", "lead", "5+ years", "6 years", "7 years"]):
        return "Senior Level"
    if any(k in text for k in ["mid", "3+ years", "4 years"]):
        return "Mid Level"
    return "Entry Level"


def calculate_skill_match_percentage(matched, missing):
    total = len(matched) + len(missing)
    if total == 0:
        return 0
    return round((len(matched) / total) * 100, 2)


def calculate_tfidf_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("english"))
    tfidf = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)


def generate_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Consider adding experience or projects related to {skill}.")
    if not suggestions:
        suggestions.append("Your resume aligns well with this job description.")
    return suggestions


# Routes
@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")


@app.route("/analyze", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        resume = request.files.get("resume")
        job_text = request.form.get("job_description", "")
        job_intent = request.form.get("job_intent", "")

        if not resume:
            return redirect("/analyze")

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
        resume.save(resume_path)

        resume_text = extract_text_from_pdf(resume_path)

        jobs = [j.strip() for j in job_text.split("---") if j.strip()]
        if not jobs and job_intent:
            jobs = [job_intent]

        results = []

        for idx, job in enumerate(jobs, start=1):
            job_lower = job.lower()

            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_lower)

            matched = sorted(set(resume_skills) & set(job_skills))
            missing = sorted(set(job_skills) - set(resume_skills))

            skill_score = calculate_skill_match_percentage(matched, missing)
            tfidf_score = calculate_tfidf_similarity(resume_text, job_lower)

            final_score = round(
                (0.7 * skill_score) + (0.3 * tfidf_score),
                2
            )

            results.append({
                "job_number": idx,
                "score": final_score,
                "experience": detect_experience(resume_text),
                "matched": matched,
                "missing": missing,
                "suggestions": generate_suggestions(missing)
            })

    return render_template("index.html", results=results)


@app.route("/download")
def download_pdf():
    file_path = "resume_analysis_report.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, y, "Resume Analysis Report")
    y -= 30

    c.setFont("Helvetica", 11)
    c.drawString(40, y, "Generated using AI - ATS Scoring")
    y -= 25

    c.line(40, y, width - 40, y)
    y -= 20

    # Dummy note (PDF generated after analysis)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(40, y, "This report summarizes how your resume matches job requirements.")
    y -= 30

    # Example content placeholder
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Summary")
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(40, y, "- Resume evaluated using keyword matching and ATS similarity")
    y -= 15
    c.drawString(40, y, "- Scores reflect alignment with job descriptions")
    y -= 30

    # Footer
    c.line(40, 60, width - 40, 60)
    c.setFont("Helvetica", 9)
    c.drawString(40, 45, "</> Crafted with 💙 by Kishor N K")

    c.save()
    return send_file(file_path, as_attachment=True)

# Run App

if __name__ == "__main__":
    app.run(debug=True)
