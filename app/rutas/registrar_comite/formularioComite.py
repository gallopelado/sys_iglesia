from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField 
from wtforms.validators import DataRequired, Length

class FormularioComite(FlaskForm):
    idcomite =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idcomite' )
    comite = StringField('Comité', validators=[Length(max=64)], id='txt_comite')
    idlider =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idlider' )
    lider = StringField('Líder', validators=[DataRequired(), Length(max=64)], id='txt_lider')
    idsuplente =  HiddenField( id='txt_idsuplente' )
    suplente = StringField('Suplente', id='txt_suplente', validators=[Length(max=64)])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()], id='txt_descripcion')
    observacion = TextAreaField('Observación', id='txt_observacion')  
     