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
        is_male = 1 if form.gender.data == "Male" else 0
        x_new = pd.DataFrame(dict(
            male = [is_male],
            age = [form.age.data],
            currentSmoker = [form.currentSmoker.data],
            cigsPerDay = [form.cigsPerDay.data],
            diabetes = [form.diabetes.data],
            totChol = [form.totChol.data],
            sysBP = [form.sysBP.data],
            BMI = [form.BMI.data],
            heartRate = [form.heartRate.data] ))
        predict = model.predict(x_new)[0]
        message = f"Prediction: {predict}"
    else:
        message = "Please provide valid input details."
    return render_template("index.html", title = "Home", form=form, output = message)


if __name__ == "__main__":
    app.run(debug=True)