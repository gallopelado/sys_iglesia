from datetime import date,time, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField 
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length
from app.Models.ReferencialModel import ReferencialModel

class FormAgregar(FlaskForm):
    refm = ReferencialModel()    
    lista_eventos = refm.getAll('referenciales.eventos')
    lista_ministerios = refm.getAll('referenciales.ministerios')
    lista_lugares = refm.getAll('referenciales.lugares')
    lista_plazos = refm.getAll('referenciales.plazos')

    anho = StringField('Año hábil')
    evento = SelectField('Elegir Evento', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_eventos], coerce=int)
    comite = SelectField('Organiza', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_ministerios], coerce=int)
    lugar = SelectField('Lugar', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_lugares], coerce=int)
    fechainicio = DateField('Fecha inicio', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    horainicio = TimeField('Hora inicio', validators=[DataRequired()], format='%H:%M', default=datetime.now())
    fechafin = DateField('Fecha fin', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    horafin = TimeField('Hora fin', validators=[DataRequired()], format='%H:%M',default=datetime.now())
    plazo = SelectField('Plazo', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_plazos], coerce=int)
    repite = BooleanField('Se repite cada año ?')
    obs = TextAreaField('Observación')
    registrar = SubmitField('Registrar')

