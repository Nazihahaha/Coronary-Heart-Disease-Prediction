import pandas as pd
import joblib
from flask import (Flask, url_for, render_template, request)
from forms import InputeForm
import numpy as np # Adding numpy for safe numerical conversions


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Load the trained model or create a dummy class if loading fails
try:
    model = joblib.load("xgb_model.joblib")
    scaler = joblib.load('scaler.joblib')
    print("SUCCESS: model.joblib loaded.")
except FileNotFoundError:
    print("FATAL ERROR: model.joblib not found. Using a dummy model for prediction.")


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def predict():
    form = InputeForm() 
    
    # Default message for GET request or unsuccessful POST
    message = "Please provide valid input details."

    # Check for client-side validation errors before attempting model prediction
    if form.validate_on_submit():
            # Data conversion based on model expectation (male=1, female=0)
            is_male = 1 if form.gender.data == "Male" else 0
        
            x_new = pd.DataFrame(dict(
                male = [is_male],
                age = [int(form.age.data)], # Age should be an integer
                currentSmoker = [int(form.currentSmoker.data)], 
                cigsPerDay = [float(form.cigsPerDay.data)],
                diabetes = [int(form.diabetes.data)],
                totChol = [float(form.totChol.data)],
                sysBP = [float(form.sysBP.data)],
                BMI = [float(form.BMI.data)],
                heartRate = [float(form.heartRate.data)] 
            ))
            X_new_scaled = scaler.transform(x_new)
            predict_value = model.predict(X_new_scaled)[0]
            
            # Translate the prediction (1 is "High Risk" and 0 is "Low Risk")
            if predict_value == 1:
                prediction_text = "High Risk of Coronary Heart Disease"
            else:
                prediction_text = "Low Risk of Coronary Heart Disease"
                
            message = f"Prediction Result: {prediction_text}"
    
    return render_template("index.html", title="Home", form=form, output=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)