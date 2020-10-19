from datetime import date
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, length

class Formulario(FlaskForm):
    malla_id = HiddenField()
    idmaestro = HiddenField()
    maestro = StringField('Maestro:')
    cur_id = HiddenField()
    curso = StringField('Curso:')
    asi_id = HiddenField()
    num_id = HiddenField()
    turno = StringField('Turno:')
    turno_h = HiddenField()
    asignatura = StringField('Asignatura:')
    fecha = DateField('Fecha:', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    hora = TimeField('Hora:', validators=[DataRequired()])
    examenes = SelectField('Escoger Examen:')
    agregar = SubmitField('Agregar')