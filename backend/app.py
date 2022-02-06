from flask import Flask, render_template, Response, request, redirect
from flask_cors import CORS
import pickle
import warnings
import pandas as pd

warnings.simplefilter('ignore', UserWarning)

categories = ['Business', 'Entertainment', 'Politics', 'Sport', 'Tech']

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)
with open("vectorizer.pkl", 'rb') as file:
    vectorizer = pickle.load(file)

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return {"Data": "Make POST request to get results"}
    else:
        news = request.get_json()["text"]
        y_pred = [news]
        y_pred = vectorizer.transform(y_pred)
        results = pd.DataFrame(model.best_estimator_.predict_proba(y_pred)[0].round(2), categories, columns=["Results"]).sort_values(by="Results",ascending=False)
        return results.to_json()