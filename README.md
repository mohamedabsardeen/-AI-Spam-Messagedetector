# AI Spam Detector

A small Flask web app that uses a TF-IDF + Logistic Regression model to classify messages as spam or not spam.

## Project structure

```
AI Spam Detector/
├── app.py
├── train_model.py
├── spam.csv
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Run it (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

Do not open `index.html` with Live Server or by double-clicking it. The page must be served by Flask.

## Improve accuracy

Replace `spam.csv` with a larger dataset that has the columns `label,message` (labels `spam` or `ham`), then run `python train_model.py` again.
