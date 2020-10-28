from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired, Length

class FormMalla(FlaskForm):
    malla= SelectField('Elegir año hábil:')