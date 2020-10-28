from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired, Length

class FormListaAlumno(FlaskForm):
    malla= SelectField('Elegir año hábil:')
    curso=SelectField('Elegir curso:')