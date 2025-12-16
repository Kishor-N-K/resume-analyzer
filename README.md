<h1 align="center">
  <img src="static/images/favicon.png" width="40" style="vertical-align: middle;">
  &nbsp;Resume Analyzer (ATS)
</h1>

<p align="center">
  <em>AI-powered resume analysis & ATS scoring</em>
</p>

---


<p align="center">
  
</p>


A professional **ATS Resume Analyzer** built with **Flask & Python** that helps users evaluate how well their resume matches job descriptions using keyword matching and NLP-based scoring.

## 🚀 **Live Demo:**  
Click Me : <a href="https://resume-analyzer-pro-vm1v.onrender.com">Resume Analyzer</a>

---

## ✨ Features

- 📑 Upload resume in PDF format
- 📊 ATS-style resume matching score
- 🧠 Skill gap detection (matched & missing skills)
- 🧩 Experience level detection
- 📝 Resume improvement suggestions
- 📄 Download professional PDF report
- ⏳ Full-page loading indicator during analysis
- 🌐 Clean landing page + dashboard UI
- 🎨 Modern, responsive design

---

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript (vanilla)

**Backend**
- Python
- Flask
- Gunicorn (production server)

**Libraries**
- pdfplumber – Resume PDF parsing
- scikit-learn – ATS scoring (TF-IDF similarity)
- nltk – Text preprocessing
- reportlab – PDF report generation

**Deployment**
- Render (Free Tier)

---

## 📂 Project Structure
```
resume-analyzer/
├── app.py
├── skills.py
├── requirements.txt
├── templates/
│ ├── landing.html
│ └── index.html
├── static/
│ ├── styles.css
│ ├── images/
│ │ ├── logo.png
│ │ └── favicon.png
│ └── favicon.ico
└── uploads/ (ignored in git)
```

---

## 🚀 How It Works

1. User uploads a resume (PDF)
2. Resume text is extracted using `pdfplumber`
3. Job description & resume are compared using NLP
4. ATS match score is calculated
5. Missing & matched skills are identified
6. Results are displayed on the dashboard
7. A professional PDF report can be downloaded

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kishor-N-K/resume-analyzer.git
cd resume-analyzer
```
2️⃣ Create & activate virtual environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the app
```
python app.py
```
Open browser:
```
Open browser:
```
Deployment

This project is deployed on Render using Gunicorn.

Start Command
```
gunicorn app:app
```
## Use Cases

- Students & job seekers

- Resume optimization

- ATS compatibility checks

## 👨‍💻 Author

Kishor N K
- </> and Crafted with 💙 by Kishor N K

⭐ Support

If you found this project useful, please star the repository ⭐
It really helps!
