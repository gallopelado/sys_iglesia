from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, BooleanField, RadioField 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

""" class FormAgregar(FlaskForm):
    idpostulacion = HiddenField(validators=[DataRequired()])
    idcomite =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idcomite' )
    comite = StringField('Comité', validators=[Length(max=64)], id='txt_comite')
    idlider =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idlider' )
    lider = StringField('Líder', validators=[DataRequired(), Length(max=64)], id='txt_lider')
    lista_admitido = SelectField('Elegir Lista de admitidos')
    agregaObrero = SubmitField('Agregar nuevo obrero')

class FormDatosObrero(FlaskForm):
    idpostulacion = HiddenField(validators=[DataRequired()])
    idcomite =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idcomite' )
    idobrero = HiddenField(validators=[DataRequired(), Length(min=1)])
    obrero = StringField('Obrero', validators=[DataRequired(), Length(min=1,max=100)])
    fechaingreso = StringField('Fecha de ingreso')
    entrenamiento = BooleanField('En entrenamiento')
    observacion = StringField('Observación', validators=[Length(max=100)])
    guardar = SubmitField('Guardar') """

class FormGenerar(FlaskForm):        
    fechainicio = DateField('Fecha inicio', format='%Y-%m-%d')
    fechafin = DateField('Fecha fin')
    estado = SelectField('Estado', choices=[('','Seleccionar'), ('ACTIVO, CON CARGOS','ACTIVO, CON CARGOS'), ('ACTIVO, SIN CARGOS', 'ACTIVO, CON CARGOS'), ('INACTIVO','INACTIVO'), ('A PRUEBA','A PRUEBA'), ('DADO DE BAJA','DADO DE BAJA'),('EN OBSERVACION','EN OBSERVACION')], default='')
    razonalta = SelectField('Razón de alta', choices=[('', 'Seleccionar'), ('BAUTISMO','BAUTISMO'), ('RECOMENDACION','RECOMENDACION'), ('TESTIMONIO','TESTIMONIO')], default='')
    ecivil = RadioField('Estado Civil', choices=[('','Ninguno'), ('SOLTERO/A','SOLTERO/A'), ('CASADO/A','CASADO/A'),('CONCUBINATO','CONCUBINATO')], default='')
    sexo = RadioField('Sexo', choices=[('', 'Ninguno'), ('MASCULINO','MASCULINO'), ('FEMENINO','FEMENINO')], default='')
    cumplemes = SelectField('Cumple años en', choices=[('','Seleccionar'),('1','ENERO'),('2','FEBRERO'),('3','MARZO'),('4','ABRIL'),('5','MAYO'),('6','JUNIO'),('7','JULIO'),('8','AGOSTO'),('9','SEPTIEMBRE'),('10','OCTUBRE'),('11','NOVIEMBRE'),('12','DICIEMBRE')], default='')
    generar = SubmitField('GENERAR')
