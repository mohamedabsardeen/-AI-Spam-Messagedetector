import os

import joblib
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "spam_model.joblib")

if not os.path.exists(MODEL_PATH):
    raise SystemExit("spam_model.joblib not found. Run:  python train_model.py  first.")

model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    proba = model.predict_proba([message])[0]
    spam_probability = float(proba[1])
    is_spam = spam_probability >= 0.5

    return jsonify(
        {
            "label": "Spam" if is_spam else "Not Spam",
            "is_spam": is_spam,
            "confidence": round((spam_probability if is_spam else 1 - spam_probability) * 100, 2),
            "spam_probability": round(spam_probability * 100, 2),
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
