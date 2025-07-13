import joblib
import os

# Get the correct absolute path relative to project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "../model")


bug_model = joblib.load(os.path.join(MODEL_DIR, "bug_model.pkl"))
priority_model = joblib.load(os.path.join(MODEL_DIR, "priority_model.pkl"))
type_model = joblib.load(os.path.join(MODEL_DIR, "type_model.pkl"))
vectorizer = joblib.load(os.path.join(MODEL_DIR, "vectorizer.pkl"))


def predict_bug_info(description):
    X = vectorizer.transform([description])
    predicted_type = bug_model.predict(X)[0]
    predicted_priority = priority_model.predict(X)[0]
    return {
        "type": predicted_type,
        "priority": predicted_priority
    }
