from datetime import date,time, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField 
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length
from app.Models.ReferencialModel import ReferencialModel
from app.Models.actividad_models.ReservaModel import ReservaModel

class FormAgregar(FlaskForm):
    resm = ReservaModel()
    refm = ReferencialModel()    
    lista_eventos = refm.getAll('referenciales.eventos')
    lista_solicitante = resm.obtenerSolicitantes()    
    lista_lugares = refm.getAll('referenciales.lugares')    

    anho = StringField('Año hábil')
    evento = SelectField('Elegir Evento', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_eventos], coerce=int)

    solicitante = SelectField('Solicitante', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_solicitante], coerce=int)

    lugar = SelectField('Lugar', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_lugares], coerce=int)
    fechainicio = DateField('Fecha inicio', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    horainicio = TimeField('Hora inicio', validators=[DataRequired()], format='%H:%M', default=datetime.now())
    fechafin = DateField('Fecha fin', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    horafin = TimeField('Hora fin', validators=[DataRequired()], format='%H:%M',default=datetime.now())        
    obs = TextAreaField('Observación', validators=[DataRequired()])
    registrar = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(FormAgregar, self).__init__(*args, **kwargs)        
        self.evento.choices = self.refm.getAll('referenciales.eventos')
        self.solicitante.choices  = self.resm.obtenerSolicitantes()
        self.lugar.choices =  self.refm.getAll('referenciales.lugares')
        

