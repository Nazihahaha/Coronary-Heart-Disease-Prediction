from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField, DateField, TimeField, IntegerField, SubmitField)
from wtforms.validators import DataRequired


X_data = pd.read_csv("framingham.csv")


class InputeForm(FlaskForm):
    airline = SelectField(label="Airline",
                          choices = X_data.airline.unique().tolist(),
                          validators = [DataRequired()]
                          )
    
    source = SelectField(
        label = "Source",
        choices= X_data.source.unique().tolist(),
        validators = [DataRequired()]
    )
    
    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    duration=IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops=IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
'''