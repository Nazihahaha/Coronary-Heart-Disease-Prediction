from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField, DateField, TimeField, FloatField, IntegerField, SubmitField, BooleanField, validators)
from wtforms.validators import (DataRequired, Length, Email, Optional, EqualTo)



X_data = pd.read_csv("framingham.csv")


class InputeForm(FlaskForm):
    gender = SelectField(label="Gender", choices=["Male", "Female", "Other"], validators = [DataRequired()])

    age = IntegerField(label='Age', validators = [DataRequired()])

    currentSmoker = BooleanField('Are you a current Smoker?', validators=[validators.InputRequired()])

    cigsPerDay = IntegerField(label='Amount of cigarettes you smoke per day', validators = [DataRequired()])

    diabetes = BooleanField(label='Do you have diabetes?', validators=[validators.InputRequired()])

    totChol = FloatField(label='How much is your total Cholesterol?', validators = [DataRequired()])

    sysBP = FloatField(label='How much is your systolic Blood Pressure (Upper value)?', validators = [DataRequired()])

    BMI = FloatField(label='What is your Body Mass Index (BMI)?', validators = [DataRequired()])

    heartRate = FloatField(label='What is your heart rate?', validators = [DataRequired()])
    
    submit = SubmitField("Predict")
