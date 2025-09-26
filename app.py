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
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            male = [form.gender.data]
            age = [form.age.data]
            currentSmoker = [form.currentSmoker.data]
            cigsPerDay = [form.cigsPerDay.data]
            diabetes = [form.diabetes.data]
            totChol = [form.totChol.data]
            sysBP = [form.sysBP.data]
            BMI = [form.BMI.data]
            heartRate = [form.heartRate.data] ))
        predict = model.predict(x_new)
        message = f"Prediction: "
    return render_template("index.html", title = "Home", form=form)


if __name__ == "__main__":
    app.run(debug=True)