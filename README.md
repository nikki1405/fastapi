---
title: BugWise AI - Smart Bug Tracking System
---

# 🐞 BugWise AI

## 🚩 Problem Statement

In software development, **bug tracking and resolution** is one of the most time-consuming and error-prone processes. Manual triaging of bug reports leads to:

- **Delayed developer assignment**
- **Improper prioritization of bugs**
- **Developer burnout** due to poor distribution
- Lack of **real-time monitoring** for admins

Many organizations struggle to route bugs effectively, especially as the team size and product complexity grow.

---

## ✅ Proposed Solution

**BugWise AI** is an **AI-powered bug tracking system** that automates the bug triage and assignment process. It intelligently predicts the **priority** and **category** of bugs using a trained machine learning model and routes them to the dashboard for admins and developers.

Key Features:

- 🧠 **ML-based Bug Prediction** – Auto-predicts priority level (High, Medium, Low) based on bug description.
- 👩‍💼 **Role-Based Access** – Separate views for admin and users.
- 🧾 **Bug Reporting Form** – Users can submit bugs with title, description, and category.
- 📊 **Admin Dashboard** – View, update, and assign bugs to developers.
- 🔐 **JWT Auth** – Secure login/register system with access control.

---

## ⚙️ Tech Stack

| Layer            | Technologies Used                            |
|------------------|-----------------------------------------------|
| Frontend         | React.js, Axios, Bootstrap 5                  |
| Backend (API)    | FastAPI, SQLAlchemy, JWT Auth                 |
| Machine Learning | Scikit-learn, Pandas, Pickle                  |
| Database         | SQLite (Development), PostgreSQL (Optional)   |
| Deployment       | Uvicorn, Gunicorn, Docker (Optional)          |

---

## 🧠 ML Model: Bug Priority Classifier

We developed a **bug priority classifier** trained on a labeled dataset of real-world bug reports. The model learns to detect whether a bug is **High**, **Medium**, or **Low** priority based on its description.

### 🔍 How It Works:

1. **Preprocessing**:
   - Text cleaning (lowercasing, stopword removal)
   - Tokenization and vectorization (TF-IDF)

2. **Training**:
   - Model used: `LogisticRegression` or `RandomForestClassifier`
   - Dataset: Custom or open-source bug tracker datasets (e.g., Bugzilla)

3. **Export**:
   - Final model serialized using `pickle` as `model.pkl`

4. **Prediction Flow**:
   - When a user fills the form and clicks “Predict Priority”:
     - The description is sent to `/bugs/predict`
     - FastAPI loads the model and returns the predicted priority
   - This priority is then used when submitting the bug to `/bugs/`

---

## 🛠 Backend API Endpoints

- `POST /auth/register` – Create new user
- `POST /auth/login` – Login and get JWT token
- `GET /bugs/` – View all bugs (Admin only)
- `POST /bugs/` – Submit new bug (requires token)
- `POST /bugs/predict` – Get predicted priority (uses ML model)
- `PUT /bugs/{id}` – Admin updates bug status, priority, or developer

---

## 🚀 Future Enhancements

- 📈 Track bug resolution timelines
- 🧠 Fine-tune ML model with more data and NLP techniques
---

## 🧑‍💻 Team Roles

- **Frontend** – React-based UI components and routing
- **Backend** – FastAPI endpoints and JWT Auth
- **ML Model** – Training, exporting, and integration
