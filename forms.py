from flask_wtf import FlaskForm
from wtforms import (SelectField, FloatField, IntegerField, SubmitField, BooleanField)
from wtforms.validators import (DataRequired, Optional, InputRequired)

class InputeForm(FlaskForm):

    gender = SelectField(label="Gender", choices=["Male", "Female"], validators=[DataRequired()])

  
    age = IntegerField(label='Age (years)', validators=[DataRequired()])


    currentSmoker = BooleanField('Are you a current Smoker?') 
    
    cigsPerDay = IntegerField(label='Amount of cigarettes you smoke per day (enter 0 if non-smoker)', 
                              validators=[InputRequired()])

  
    diabetes = BooleanField(label='Do you have diabetes?')

    totChol = FloatField(label='Total Cholesterol (mg/dL)', validators=[DataRequired()])

    sysBP = FloatField(label='Systolic Blood Pressure (mmHg)', validators=[DataRequired()])

    BMI = FloatField(label='Body Mass Index (BMI)', validators=[DataRequired()])

    heartRate = FloatField(label='Heart Rate (beats/min)', validators=[DataRequired()])
    
    submit = SubmitField("Predict Risk")