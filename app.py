import pandas as pd
import joblib
from flask import (Flask,  url_for, render_template)
from forms import InputeForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def predict():
    form = InputeForm()
    
    return render_template("index.html", title = "Home", form=form)


if __name__ == "__main__":
    app.run(debug=True)