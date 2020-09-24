from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, length

class Formulario(FlaskForm):
    usu_id = HiddenField()
    id = HiddenField()
    descripcion = StringField('Descripcion', validators=[DataRequired(), length(max=60)])
    guardar = SubmitField('Guardar')