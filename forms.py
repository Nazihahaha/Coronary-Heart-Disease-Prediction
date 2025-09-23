from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField, DateField, TimeField, FloatField, IntegerField, SubmitField, BooleanField, validators)
from wtforms.validators import (DataRequired, Length, Email, Optional, EqualTo)



X_data = pd.read_csv("framingham.csv")


class InputeForm(FlaskForm):
    gender = SelectField(label="Gender", choices=["Male", "Female", "Other"], validators=[Optional()])

    age = IntegerField(label='Age')

    currentSmoker = BooleanField('Are you a current Smoker?', validators=[validators.InputRequired()])

    cigsPerDay = IntegerField(label='Amount of cigarettes you smoke per day')

    diabetes = FloatField(label='How much is your diabetes?')

    totChol = FloatField(label='How much is your total Cholesterol?')

    sysBP = FloatField(label='How much is your systolic Blood Pressure (Upper value)?')

    BMI = FloatField(label='What is your Body Mass Index (BMI)?')

    heartRate = FloatField(label='What is your heart rate?')
    
    submit = SubmitField("Predict")
