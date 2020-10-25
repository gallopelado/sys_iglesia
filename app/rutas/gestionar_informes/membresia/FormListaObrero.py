from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField, RadioField 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

class FormListaObrero(FlaskForm):
    comites = SelectField('Elegir comite:')
    fechadesde = DateField('Fecha desde:', format='%Y-%m-%d')
    fechahasta = DateField('Fecha hasta:', format='%Y-%m-%d')
    entrenamiento = RadioField('En Entrenamiento', choices=[(True, 'SI'), (False, 'NO')], default=True)
    estado = RadioField('Estado', choices=[(True, 'ACTIVO'), (False, 'INACTIVO')], default=True)