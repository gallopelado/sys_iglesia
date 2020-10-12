from typing import Text
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length

class Formulario(FlaskForm):
    malla_id = HiddenField()
    alu_id = HiddenField()
    idmaestro = HiddenField()
    alumno = StringField('Alumno:')
    cur_id = HiddenField()
    curso = StringField('Curso:')
    asi_id = HiddenField()
    num_id = HiddenField()
    turno = HiddenField()
    asignatura = StringField('Asignatura:')
    descripcion = TextAreaField('Descripcion:', validators=[DataRequired(), length(max=300)])
    guardar = SubmitField('Guardar')