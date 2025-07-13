import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample bug data
data = [
    {"desc": "login button not working on UI", "priority": "High", "type": "UI"},
    {"desc": "database crash on load", "priority": "High", "type": "Backend"},
    {"desc": "app loading slow on mobile", "priority": "Medium", "type": "Performance"},
    {"desc": "security bug allows access without login", "priority": "High", "type": "Security"},
    {"desc": "minor UI layout bug", "priority": "Low", "type": "UI"},
    {"desc": "backend timeout when querying", "priority": "High", "type": "Backend"},
    {"desc": "input form takes time to validate", "priority": "Medium", "type": "Performance"},
]

df = pd.DataFrame(data)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["desc"])

# Train models
priority_model = LogisticRegression()
priority_model.fit(X, df["priority"])

type_model = LogisticRegression()
type_model.fit(X, df["type"])


# Save models and vectorizer
joblib.dump(vectorizer, "app/model/vectorizer.pkl")
joblib.dump(priority_model, "app/model/priority_model.pkl")
joblib.dump(type_model, "app/model/type_model.pkl")
joblib.dump(type_model, "app/model/bug_model.pkl")  # Also save as bug_model.pkl for backend compatibility

print("✅ ML Models trained and saved.")
