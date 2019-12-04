from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, DateField, BooleanField, TimeField 
from wtforms.validators import DataRequired, Length

class FormAgregar(FlaskForm):    
    anho = StringField('Año hábil')
    evento = SelectField('Elegir Evento', validators=[DataRequired()])
    comite = SelectField('Organiza', validators=[DataRequired()])
    lugar = SelectField('Lugar', validators=[DataRequired()])
    fechainicio = DateField('Fecha inicio', validators=[DataRequired()], format='%Y-%m-%d')
    horainicio = TimeField('Hora inicio', validators=[DataRequired()], format='%H:%M')
    fechafin = DateField('Fecha fin', validators=[DataRequired()], format='%Y-%m-%d')
    horafin = TimeField('Hora fin', validators=[DataRequired()], format='%H:%M')
    plazo = SelectField('Plazo', validators=[DataRequired()])
    repite = BooleanField('Se repite cada año ?')
    obs = TextAreaField('Observación')
    registrar = SubmitField('Registrar')

