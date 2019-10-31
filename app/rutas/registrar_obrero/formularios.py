from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField, DateField, BooleanField 
from wtforms.validators import DataRequired, Length

class FormAgregar(FlaskForm):
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
    guardar = SubmitField('Guardar')
