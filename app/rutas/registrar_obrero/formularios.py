from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField, SelectField 
from wtforms.validators import DataRequired, Length

class FormAgregar(FlaskForm):
    idcomite =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idcomite' )
    comite = StringField('Comité', validators=[Length(max=64)], id='txt_comite')
    idlider =  HiddenField( validators=[DataRequired(), Length(min=1)], id='txt_idlider' )
    lider = StringField('Líder', validators=[DataRequired(), Length(max=64)], id='txt_lider')
    lista_admitido = SelectField('Elegir Lista de admitidos', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])