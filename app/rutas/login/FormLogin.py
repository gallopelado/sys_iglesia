from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, length

class FormLogin(FlaskForm):
    user = StringField('Usuario', validators=[DataRequired(), length(max=6)])
    loginPassword = PasswordField('Clave', validators=[DataRequired()])
    showPasswordCheck = BooleanField('Mostrar')