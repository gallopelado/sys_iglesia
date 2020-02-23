from datetime import date,time, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField, DecimalField 
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length
from app.Models.ReferencialModel import ReferencialModel
from app.Models.actividad_models.SolicitudHospitalModel import SolicitudHospitalModel

class FormularioVisita(FlaskForm):
    # Fuentes de datos    
    soli = SolicitudHospitalModel()    
    lista_idiomas = soli.obtenerIdiomas()
    lista_solicitantes = soli.obtenerSolicitantes()
    lista_personas = soli.obtenerPacientes()        
    # Se cargan los objetos
    idioma = SelectField('Idioma', validators=[DataRequired()], choices=[(item[0], f"{item[1]}") for item in lista_idiomas], coerce=int)
    solicitante = SelectField('Solicitante', validators=[DataRequired()], choices=[(item[0], f"{item[1]} {item[2]}") for item in lista_solicitantes], coerce=int)
    descripcion = TextAreaField('Descripcion', validators=[DataRequired()])     
    paciente = SelectField('Nombre del paciente', validators=[DataRequired()],choices=[(item[0], f"{item[1]} {item[2]}") for item in lista_personas], coerce=int)
    esmiembro = BooleanField('Es miembro de la Iglesia ?')
    estaenterado = BooleanField('Esta enterado de esta solicitud ?')    
    hospital = StringField('Nombre del Hospital', validators=[DataRequired()])
    nrocuarto = StringField('N. de cuarto', validators=[DataRequired()])
    telefcuarto = StringField('N. telefono en el cuarto')
    fechaadmision = DateField('Fecha de admisión', format='%Y-%m-%d', default=date.today)
    diagnostico = TextAreaField('Diagnóstico')
    direccionhospi = StringField('Dirección del hospital',validators=[DataRequired()])
    horariovisita = TimeField('Horarios de visita', validators=[DataRequired()])
    # Checks de los dias de visita
    lunes = BooleanField('Lunes')
    martes = BooleanField('Martes')
    miercoles = BooleanField('Miercoles')
    jueves = BooleanField('Jueves')
    viernes = BooleanField('Viernes')
    sabado = BooleanField('Sabado')
    domingo = BooleanField('Domingo')   
    registrar = SubmitField('Registrar')

    # Constructor
    def __init__(self, *args, **kwargs):
        super(FormularioVisita, self).__init__(*args, **kwargs)                
        self.paciente.choices = [(item[0], f"{item[1]} {item[2]}") for item in self.lista_personas]       
        
class Formulario(FlaskForm):
    miembro = SelectField('Elegir Miembro', validators=[DataRequired()], choices=[('01', 'Juan Jose')])
    edad = StringField('Edad', validators=[DataRequired()])
    ecivil = SelectField('Estado Civil', validators=[DataRequired()], choices=[('01', 'Soltero')])
    conyuge = StringField('Conyuge', validators=[DataRequired()])
    edadconyuge = StringField('Edad Conyuge', validators=[DataRequired()])
    tiempocasado = StringField('Tiempo de casado/a', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    religion = SelectField('Religion', validators=[DataRequired()], choices=[('01', 'Catolico')])
    asiste_regular = BooleanField('Asiste regularmente a los servicios ?')
    servicio_central = BooleanField('Servicio central')
    grupo_creci = BooleanField('Grupos de crecimiento')
    servicio_semanal = BooleanField('Servicios entre semana')
    descri_matriant = TextAreaField('Dar una breve descripcion acerca de los matrimonios anteriores')
    descri_hijos = TextAreaField('Tiene hijos, indicar nombre y edad')
    grupo_asiste = SelectField('Grupo de crecimiento al que asiste', validators=[DataRequired()], choices=[('01', 'Villa Elisa')])
    consultagrupo = BooleanField('Ha consultado con ellos acerca de su preocupación?')
    descri_recibio = TextAreaField('Ha recibido a Jesucristo como su Salvador personal? Explique brevemente')
    descri_asesoria = TextAreaField('Ha recibido asesoría para este problema en particular antes? Si es así, quién le aconsejó, cuándo y cuál fue el resultado?')
    consejero = SelectField('Elegir consejero', validators=[DataRequired()], choices=[('01', 'Maria de los Pollos')])
    fecha = StringField('Fecha', validators=[DataRequired()])

