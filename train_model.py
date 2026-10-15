import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# 1. Load the dataset (columns: label, message)
data = pd.read_csv("spam.csv")
data = data.dropna()
data["label"] = data["label"].str.strip().str.lower()

X = data["message"]
y = data["label"].map({"ham": 0, "spam": 1})

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Build the model: text -> TF-IDF numbers -> Logistic Regression
model = Pipeline(
    [
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(X_train, y_train)

# 4. Check how good it is
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print(classification_report(y_test, predictions, target_names=["ham", "spam"]))

# 5. Retrain on all data and save
model.fit(X, y)
joblib.dump(model, "spam_model.joblib")
print("Model saved as spam_model.joblib")
