from typing import Text
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, length

class Formulario(FlaskForm):
    malla_id = HiddenField()
    alu_id = HiddenField()
    idmaestro = HiddenField()
    fecha_clase = HiddenField()
    alumno = StringField('Alumno:')
    cur_id = HiddenField()
    curso = StringField('Curso:')
    asi_id = HiddenField()
    num_id = HiddenField()
    turno = HiddenField()
    turno_t = StringField('Turno:')
    asignatura = StringField('Asignatura:')
    examenes = SelectField('Escoger Examen:')
    guardar = SubmitField('Guardar')