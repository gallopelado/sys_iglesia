from datetime import date,time, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField, DecimalField 
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length
from app.Models.ReferencialModel import ReferencialModel
from app.Models.actividad_models.ReservaModel import ReservaModel

class FormularioVisita(FlaskForm):    
    refm = ReferencialModel()    
    #lista_idiomas = refm.getAll('referenciales.idioma')           
    #idioma = SelectField('Idioma', validators=[DataRequired()], choices=[(item[0], item[1]) for item in lista_eventos], coerce=int)
    idioma = SelectField('Idioma', validators=[DataRequired()], choices=[("1", "ES")])
    solicitante = SelectField('Solicitante', choices=[('1', 'Juan')])
    descripcion = TextAreaField('Descripcion', validators=[DataRequired()])     
    paciente = SelectField('Nombre del paciente', choices=[('1', 'Juan')])
    esmiembro = BooleanField('Es miembro de la Iglesia ?')
    estaenterado = BooleanField('Esta enterado de esta solicitud ?')
    requiere = BooleanField('Requiere el paciente que se haga la visita en español ?')
    hospital = StringField('Nombre del Hospital')
    nrocuarto = DecimalField('N. de cuarto')
    telefcuarto = StringField('N. telefono en el cuarto')
    fechaadmision = DateField('Fecha de admisión', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    diagnostico = TextAreaField('Diagnóstico')
    direccionhospi = StringField('Dirección del hospital')
    horariovisita = StringField('Horarios de visita')
    # Checks de los dias de visita
    lunes = BooleanField('Lunes')
    martes = BooleanField('Martes')
    miercoles = BooleanField('Miercoles')
    jueves = BooleanField('Jueves')
    viernes = BooleanField('Viernes')
    sabado = BooleanField('Sabado')
    domingo = BooleanField('Domingo')   
    registrar = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(FormularioVisita, self).__init__(*args, **kwargs)        
        #self.evento.choices = self.refm.getAll('referenciales.eventos')        
        

