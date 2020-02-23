from datetime import date,time, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField, DecimalField 
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length
from app.Models.ReferencialModel import ReferencialModel
from app.Models.actividad_models.ConsejeriaModel import ConsejeriaModel

class Formulario(FlaskForm):
    #Cargar el combo de miembros, consejeros.
    cons = ConsejeriaModel()
    rfm = ReferencialModel()
    
    miembros = [(str(miembro['idmiembro']), miembro['miembro']) for miembro in cons.getMiembros()]
    miembros = list(miembros)
    miembros.insert(0, ('', '...'))
    
    consejeros = [(str(consejero['idconsejero']), consejero['consejero']) for consejero in cons.getConsejeros()]
    consejeros = list(consejeros)
    consejeros.insert(0, ('', '...'))
    
    grupos = [(str(grupo['id']), grupo['descripcion']) for grupo in rfm.getReferencialJson('referenciales.grupo_crecimiento')]
    grupos = list(grupos)
    grupos.insert(0, ('', '...')) 

    religiones = [(str(religion['id']), religion['descripcion']) for religion in rfm.getReferencialJson('referenciales.religion')]
    religiones = list(religiones)
    religiones.insert(0, ('', '...'))   

    miembro = SelectField('Elegir Miembro', validators=[DataRequired()], choices=miembros)
    edad = StringField('Edad')
    ecivil = StringField('Estado Civil')
    conyuge = StringField('Conyuge')
    edadconyuge = StringField('Edad Conyuge')
    tiempocasado = StringField('Tiempo de casado/a')
    edad = StringField('Edad')
    religion = SelectField('Religion', validators=[DataRequired()], choices=religiones)
    asiste_regular = BooleanField('Asiste regularmente a los servicios ?')
    servicio_central = BooleanField('Servicio central')
    grupo_creci = BooleanField('Grupos de crecimiento')
    servicio_semanal = BooleanField('Servicios entre semana')
    descri_matriant = TextAreaField('Dar una breve descripcion acerca de los matrimonios anteriores')
    descri_hijos = TextAreaField('Tiene hijos, indicar nombre y edad')
    grupo_asiste = SelectField('Grupo de crecimiento al que asiste', validators=[DataRequired()], choices=grupos)
    consultagrupo = BooleanField('Ha consultado con ellos acerca de su preocupación?')
    descri_recibio = TextAreaField('Ha recibido a Jesucristo como su Salvador personal? Explique brevemente' , validators=[DataRequired()])
    descri_asesoria = TextAreaField('Ha recibido asesoría para este problema en particular antes? Si es así, quién le aconsejó, cuándo y cuál fue el resultado?', validators=[DataRequired()])
    consejero = SelectField('Elegir consejero', validators=[DataRequired()], choices=consejeros)    

