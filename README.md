<h1 align="center">ReachHR 🚀</h1>
<p align="center">
  <b>Find HRs. Connect Smart. Land Opportunities.</b><br>
  AI-powered tool to discover HR profiles and craft personalized cold messages.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Cohere-Command R+-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/Google-Custom_Search-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.10+-brightgreen?style=flat-square" />
</p>

---

## ✨ Overview

**ReachHR** is a smart and lightweight AI-powered web app built with Streamlit that helps students and professionals reach out to HRs and recruiters effectively. Given a **company name** and **location**, the app:

1. 📡 Fetches the **official website**
2. 🔍 Extracts relevant **HR or recruiter LinkedIn profiles**
3. ✉️ Generates a **personalized cold message** using Cohere (Command R+)

> Whether you're looking for an internship, referral, or full-time role — ReachHR.ai saves your time and boosts your reach.

---

## 🚀 Live Demo

👉 [Click here to try ReachHR](#)  
*(Insert your Streamlit Cloud deployment link once live)*

---

## 🔧 Tech Stack

| Tool              | Role                             |
|-------------------|----------------------------------|
| Python            | Core logic and integration       |
| Streamlit         | Frontend & UI                    |
| Cohere API        | AI-powered message generation    |
| Google CSE API    | Web & LinkedIn search            |

---

## 📸 Screenshots

| Home | Results |
|------|---------|
| ![home](./assets/home.png) | ![results](./assets/results.png) |

---

## ⚙️ How It Works

1. 🔎 Enter **Company Name** & **Location**
2. 🌐 App fetches official website + LinkedIn HRs
3. 🧠 Enter your **purpose** (e.g. ask for internship)
4. ✉️ App generates a **concise cold message** you can directly paste on LinkedIn

---

## 🛠️ Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reachhr.ai.git
cd reachhr.ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env file in root directory

```bash
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX=your_search_engine_cx
COHERE_API_KEY=your_cohere_api_key
```
✅ Ensure .env is listed in .gitignore

### 💻 Run the App

```bash
streamlit run app.py
```

### 🌐 Deployment (Streamlit Cloud)

1. Push your repo to GitHub

2. Go to Streamlit Cloud

3. Connect your repo

4. In "Secrets", add:

```bash
GOOGLE_API_KEY = "your_key"
GOOGLE_CX = "your_cx"
COHERE_API_KEY = "your_key"
```

Click “Deploy” 🚀

---

<h2 align="center">🙌 Made By</h2>

<p align="center">
  Built with ❤️ by <a href="https://www.linkedin.com/in/harjyot-singh-75a835254/" target="_blank"><b>Harjyot Singh</b></a><br>
  A passionate learner & builder focused on Python, AI & ML, automation & impactful tools.
</p>

<p align="center">
  If you found this project useful, feel free to ⭐ star the repo and connect on LinkedIn!
</p>
